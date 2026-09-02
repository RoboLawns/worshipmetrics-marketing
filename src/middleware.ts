// Agent discovery: RFC 8288 Link headers, the RFC 9727 API catalog, RFC 9728
// OAuth protected resource metadata, and markdown content negotiation.
//
// Machine clients (AI agents, crawlers, API tooling) learn what WorshipMetrics
// offers without scraping HTML: every HTML page advertises the well-known API
// catalog via Link headers, the catalog itself is served at the RFC 8615 path,
// and any request preferring `Accept: text/markdown` gets the page converted
// to markdown (Cloudflare's "Markdown for agents" shape — the zone-level
// feature needs a paid plan + dashboard toggle, so we do the conversion in the
// Worker instead). All of it lives here in middleware because the site is
// `output: 'server'` — response headers can't come from public/_headers (that
// file only applies to static assets, not Worker-rendered pages), and a
// public/ file could not carry the extensionless path's
// application/linkset+json Content-Type.
//
// isitagentready.com's scanner exercises all of it: `discoverability.linkHeaders`
// wants a Link header on GET /, `discovery.apiCatalog` fetches
// GET /.well-known/api-catalog with `Accept: application/linkset+json`,
// `discovery.oauthProtectedResource` fetches
// GET /.well-known/oauth-protected-resource, and
// `contentAccessibility.markdownNegotiation` sends `Accept: text/markdown`
// expecting a text/markdown Content-Type back.

import { defineMiddleware } from 'astro:middleware';
import { htmlToMarkdown, prefersMarkdown, estimateTokens } from './lib/html-to-markdown';
import { handleMcpRequest } from './lib/mcp-server';

const SITE_ORIGIN = 'https://worshipmetrics.com';
const APP_ORIGIN = 'https://app.worshipmetrics.com';

const API_CATALOG_PATH = '/.well-known/api-catalog';

// RFC 9264 linkset. Every href here resolves today. The API is first-party and
// requires authentication, so there is deliberately no `service-desc` (OpenAPI)
// entry yet — add one when a real description document exists rather than
// pointing agents at a 404.
const API_CATALOG = {
  linkset: [
    {
      anchor: `${APP_ORIGIN}/api/`,
      'service-doc': [
        {
          href: `${SITE_ORIGIN}/kb/`,
          type: 'text/html',
          title: 'WorshipMetrics knowledge base',
        },
      ],
      status: [{ href: `${APP_ORIGIN}/health`, type: 'application/json' }],
    },
  ],
};

const API_CATALOG_BODY = JSON.stringify(API_CATALOG, null, 2) + '\n';

const OAUTH_PROTECTED_RESOURCE_PATH = '/.well-known/oauth-protected-resource';

// RFC 9728 OAuth protected resource metadata. Truthful about today's reality:
// WorshipMetrics runs no OAuth authorization server anywhere (accounts are
// provisioned person to person — see /auth.md), so `authorization_servers`
// and `bearer_methods_supported` are deliberately EMPTY rather than listing
// an issuer that doesn't exist — same philosophy as the missing
// `service-desc` above. If a real authorization server ships (e.g. a
// Cloudflare Access team at https://<team>.cloudflareaccess.com), put its
// issuer URL in `authorization_servers` and update /auth.md to match.
// `resource` derives from the request origin so the document also stays
// spec-correct on preview deployments; on production it is the canonical
// https://worshipmetrics.com.
function oauthProtectedResourceMetadata(origin: string) {
  return {
    resource: origin,
    authorization_servers: [],
    bearer_methods_supported: [],
    scopes_supported: [],
    resource_name: 'WorshipMetrics',
    resource_documentation: `${SITE_ORIGIN}/auth.md`,
  };
}

// rel values are IANA-registered link relations: api-catalog (RFC 9727) and
// service-doc (RFC 8631, human-readable documentation for the service).
const LINK_HEADER_VALUES = [
  `<${API_CATALOG_PATH}>; rel="api-catalog"`,
  '</kb/>; rel="service-doc"; type="text/html"',
];

export const onRequest = defineMiddleware(async (context, next) => {
  const { pathname } = context.url;

  // The MCP endpoint advertised by /.well-known/mcp/server-card.json.
  // Dispatched here for the same reason the API catalog is: both slash forms
  // must resolve despite `trailingSlash: 'always'`.
  if (pathname === '/mcp' || pathname === '/mcp/') {
    return handleMcpRequest(context);
  }

  if (pathname === API_CATALOG_PATH || pathname === `${API_CATALOG_PATH}/`) {
    return new Response(API_CATALOG_BODY, {
      headers: {
        'Content-Type': 'application/linkset+json',
        'Cache-Control': 'public, max-age=3600',
      },
    });
  }

  if (pathname === OAUTH_PROTECTED_RESOURCE_PATH || pathname === `${OAUTH_PROTECTED_RESOURCE_PATH}/`) {
    const body = JSON.stringify(oauthProtectedResourceMetadata(context.url.origin), null, 2) + '\n';
    return new Response(body, {
      headers: {
        'Content-Type': 'application/json',
        // Public by definition; browser-hosted agents read it cross-origin.
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=3600',
      },
    });
  }

  const response = await next();

  // RFC 9728 §5.1: a 401 challenge points the client at the resource metadata.
  // Nothing on this site returns 401 today; this future-proofs any route that
  // starts to.
  if (response.status === 401 && !response.headers.has('WWW-Authenticate')) {
    response.headers.set(
      'WWW-Authenticate',
      `Bearer resource_metadata="${SITE_ORIGIN}${OAUTH_PROTECTED_RESOURCE_PATH}"`,
    );
  }

  const contentType = response.headers.get('Content-Type') ?? '';
  if (!contentType.includes('text/html')) {
    return response;
  }

  // Markdown negotiation: an explicit `Accept: text/markdown` (at least as
  // preferred as text/html) gets the rendered page converted to markdown.
  // Browsers never send it, so HTML stays the default.
  if (prefersMarkdown(context.request.headers.get('Accept'))) {
    const html = await response.text();
    let markdown: string;
    try {
      markdown = htmlToMarkdown(html, context.url);
    } catch {
      // Conversion must never take a page down — fall back to the HTML body.
      const fallback = new Response(html, response);
      fallback.headers.append('Vary', 'Accept');
      return fallback;
    }
    const headers = new Headers();
    const cacheControl = response.headers.get('Cache-Control');
    if (cacheControl) headers.set('Cache-Control', cacheControl);
    for (const value of LINK_HEADER_VALUES) {
      headers.append('Link', value);
    }
    headers.set('Content-Type', 'text/markdown; charset=utf-8');
    headers.set('Vary', 'Accept');
    headers.set('x-markdown-tokens', String(estimateTokens(markdown)));
    headers.set('x-original-tokens', String(estimateTokens(html)));
    return new Response(markdown, {
      status: response.status,
      statusText: response.statusText,
      headers,
    });
  }

  // Advertise on every rendered page, not just /: KB articles and pillar pages
  // are common agent entry points, and the header costs ~100 bytes. Vary keeps
  // caches from serving the HTML variant to markdown-preferring agents.
  for (const value of LINK_HEADER_VALUES) {
    response.headers.append('Link', value);
  }
  response.headers.append('Vary', 'Accept');

  return response;
});
