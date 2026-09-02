// Agent discovery: RFC 8288 Link headers + the RFC 9727 API catalog.
//
// Machine clients (AI agents, crawlers, API tooling) learn what WorshipMetrics
// offers without scraping HTML: every HTML page advertises the well-known API
// catalog via Link headers, and the catalog itself is served at the RFC 8615
// path. Both live here in middleware because the site is `output: 'server'` —
// response headers can't come from public/_headers (that file only applies to
// static assets, not Worker-rendered pages), and a public/ file could not carry
// the extensionless path's application/linkset+json Content-Type.
//
// isitagentready.com's scanner exercises both halves: `discoverability.linkHeaders`
// wants a Link header on GET /, and `discovery.apiCatalog` fetches
// GET /.well-known/api-catalog with `Accept: application/linkset+json`.

import { defineMiddleware } from 'astro:middleware';
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

  const response = await next();

  // Advertise on every rendered page, not just /: KB articles and pillar pages
  // are common agent entry points, and the header costs ~100 bytes.
  const contentType = response.headers.get('Content-Type') ?? '';
  if (contentType.includes('text/html')) {
    for (const value of LINK_HEADER_VALUES) {
      response.headers.append('Link', value);
    }
  }

  return response;
});
