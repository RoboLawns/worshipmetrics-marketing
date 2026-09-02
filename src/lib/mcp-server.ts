// MCP server (Model Context Protocol, Streamable HTTP transport) backing the
// endpoint advertised by /.well-known/mcp/server-card.json (SEP-1649).
//
// Stateless by design: every POST is a complete JSON-RPC message answered with
// a single application/json body — no SSE streams, no session ids, so GET and
// DELETE both get 405. The tools read only public site content (the search
// index prerendered at /kb/search-index.json and the prerendered KB article
// pages), so there is no auth and CORS is open. Church data stays behind
// sign-in in the web app and is not reachable from here.
//
// Dispatched from middleware (like the API catalog) rather than a src/pages
// route so /mcp and /mcp/ both resolve regardless of the site-wide
// `trailingSlash: 'always'` setting.

import type { APIContext } from 'astro';
import { htmlToMarkdown } from './html-to-markdown';

const SITE_ORIGIN = 'https://worshipmetrics.com';

// Versions whose feature set our tools-only surface satisfies. An unknown
// requested version gets our latest; the client may then disconnect.
const PROTOCOL_VERSIONS = new Set(['2024-11-05', '2025-03-26', '2025-06-18']);
const LATEST_PROTOCOL = '2025-06-18';

// Mirrored in /.well-known/mcp/server-card.json — keep the two in sync.
const SERVER_INFO = {
  name: 'worshipmetrics',
  title: 'WorshipMetrics',
  version: '1.0.0',
};

const INSTRUCTIONS =
  'Public product-information server for WorshipMetrics, the all-in-one platform ' +
  'for church worship and production teams. Use search_knowledge_base to find ' +
  'guides in the free church A/V knowledge base, get_kb_article to read one as ' +
  'markdown, and get_product_overview for what the platform does and how churches ' +
  'get started. No authentication is needed. Church account data is not available ' +
  'here — it stays behind sign-in at https://app.worshipmetrics.com.';

const PRODUCT_OVERVIEW = `# WorshipMetrics

WorshipMetrics is an all-in-one platform for church worship and production
teams: service planning, presentation, volunteer scheduling, attendance,
live streaming, digital signage, and A/V monitoring.

Key pages:

- Platform overview: ${SITE_ORIGIN}/platform/
- Pricing: ${SITE_ORIGIN}/pricing/
- Live streaming: ${SITE_ORIGIN}/live-streaming/
- Knowledge base (free church A/V guides): ${SITE_ORIGIN}/kb/
- Contact: ${SITE_ORIGIN}/contact/

Getting started: churches join through a conversation with the team — book a
call at ${SITE_ORIGIN}/discovery-call/ or email paul@worshipmetrics.com. The
web app for member churches is at https://app.worshipmetrics.com (sign-in
required; church data is not available through this MCP server).

Any page on worshipmetrics.com is also available as markdown: request it with
an \`Accept: text/markdown\` header.
`;

const TOOL_DEFINITIONS = [
  {
    name: 'get_product_overview',
    title: 'Product overview',
    description:
      'What WorshipMetrics is — the platform areas (service planning, presentation, ' +
      'volunteer scheduling, attendance, live streaming, digital signage, A/V ' +
      'monitoring), key pages, and how churches get started.',
    inputSchema: { type: 'object', properties: {}, additionalProperties: false },
  },
  {
    name: 'search_knowledge_base',
    title: 'Search the knowledge base',
    description:
      'Search the free WorshipMetrics church A/V knowledge base: hundreds of guides ' +
      'covering PTZ cameras, video switchers, audio mixers, hardware encoders, ' +
      'streaming software (OBS, vMix, ProPresenter, and more), complete setups by ' +
      'budget, comparisons, and troubleshooting. Returns matching articles with URLs.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'What to search for, e.g. "atem mini audio delay" or "ptz camera under 500".',
        },
        limit: {
          type: 'integer',
          minimum: 1,
          maximum: 25,
          description: 'Maximum results to return (default 10).',
        },
      },
      required: ['query'],
      additionalProperties: false,
    },
  },
  {
    name: 'get_kb_article',
    title: 'Read a knowledge-base article',
    description:
      'Fetch one knowledge-base article as markdown by its URL (use ' +
      'search_knowledge_base to find URLs). Only worshipmetrics.com /kb/ pages.',
    inputSchema: {
      type: 'object',
      properties: {
        url: {
          type: 'string',
          description: 'Article URL or path, e.g. "/kb/switchers/blackmagic/blackmagic-atem-mini-setup-guide/".',
        },
      },
      required: ['url'],
      additionalProperties: false,
    },
  },
];

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers':
    'Content-Type, Accept, Authorization, Mcp-Session-Id, MCP-Protocol-Version, Last-Event-ID',
  'Access-Control-Max-Age': '86400',
};

type RpcId = string | number;

function jsonResponse(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
  });
}

function rpcResult(id: RpcId, result: unknown): Response {
  return jsonResponse({ jsonrpc: '2.0', id, result });
}

function rpcError(id: RpcId | null, code: number, message: string, status = 200): Response {
  return jsonResponse({ jsonrpc: '2.0', id, error: { code, message } }, status);
}

// Tool output. Tool-level failures (bad argument, article not found) are
// results with isError, not JSON-RPC errors, so the model can read and
// recover from them.
function textResult(text: string, isError = false) {
  return { content: [{ type: 'text', text }], ...(isError ? { isError: true } : {}) };
}

// Static site output (the prerendered search index and KB article pages).
// Production serves them from the Cloudflare assets binding (Astro v6 exposes
// bindings via the `cloudflare:workers` env import, not Astro.locals). When
// the binding is missing or misses — `astro dev` prerenders nothing — fall
// back to a same-origin fetch, which renders the page on demand.
async function fetchStatic(path: string, context: APIContext): Promise<Response> {
  const url = new URL(path, context.url.origin);

  let fromAssets: Response | null = null;
  try {
    const { env } = await import('cloudflare:workers');
    const assets = (env as { ASSETS?: { fetch(input: Request): Promise<Response> } }).ASSETS;
    if (assets) {
      let response = await assets.fetch(new Request(url.href));
      if (response.status >= 301 && response.status <= 308) {
        const location = response.headers.get('Location');
        if (location) response = await assets.fetch(new Request(new URL(location, url).href));
      }
      if (response.ok) return response;
      fromAssets = response;
    }
  } catch {
    // Not running on the Cloudflare adapter runtime — use the fetch fallback.
  }

  try {
    return await fetch(url.href, { headers: { Accept: 'text/html' } });
  } catch (error) {
    if (fromAssets) return fromAssets;
    throw error;
  }
}

interface IndexRow {
  title: string;
  description: string;
  tags: string[];
  section: string;
  url: string;
}

// Cached per Worker isolate; the index only changes with a deploy.
let searchIndex: IndexRow[] | null = null;

async function loadSearchIndex(context: APIContext): Promise<IndexRow[]> {
  if (searchIndex) return searchIndex;
  const response = await fetchStatic('/kb/search-index.json', context);
  if (!response.ok) {
    throw new Error(`knowledge-base index unavailable (HTTP ${response.status})`);
  }
  searchIndex = (await response.json()) as IndexRow[];
  return searchIndex;
}

async function searchKnowledgeBase(context: APIContext, args: Record<string, unknown>) {
  const query = typeof args.query === 'string' ? args.query.trim() : '';
  if (!query) return textResult('The "query" argument is required and must be a non-empty string.', true);
  const rawLimit = typeof args.limit === 'number' && Number.isFinite(args.limit) ? Math.floor(args.limit) : 10;
  const limit = Math.min(Math.max(rawLimit, 1), 25);

  const phrase = query.toLowerCase();
  const terms = phrase.split(/[^a-z0-9]+/).filter((t) => t.length > 1);
  const index = await loadSearchIndex(context);

  const scored: { score: number; row: IndexRow }[] = [];
  for (const row of index) {
    const title = row.title.toLowerCase();
    const description = row.description.toLowerCase();
    const tags = row.tags.join(' ').toLowerCase();
    const url = row.url.toLowerCase();
    let score = 0;
    if (terms.length > 1 && title.includes(phrase)) score += 8;
    for (const term of terms) {
      if (title.includes(term)) score += 4;
      if (tags.includes(term)) score += 2;
      if (url.includes(term)) score += 2;
      if (description.includes(term)) score += 1;
    }
    if (score > 0) scored.push({ score, row });
  }
  scored.sort((a, b) => b.score - a.score || a.row.title.localeCompare(b.row.title));

  const results = scored.slice(0, limit).map(({ row }) => ({
    title: row.title,
    description: row.description,
    section: row.section,
    url: SITE_ORIGIN + row.url,
  }));
  return textResult(
    JSON.stringify(
      {
        query,
        totalMatches: scored.length,
        results,
        tip: 'Pass a result url to the get_kb_article tool for the full guide as markdown.',
      },
      null,
      2,
    ),
  );
}

async function getKbArticle(context: APIContext, args: Record<string, unknown>) {
  const raw = typeof args.url === 'string' ? args.url.trim() : '';
  if (!raw) return textResult('The "url" argument is required, e.g. a url from search_knowledge_base results.', true);

  let path: string;
  try {
    const parsed = new URL(raw, SITE_ORIGIN);
    const allowedHosts = new Set(['worshipmetrics.com', 'www.worshipmetrics.com', context.url.hostname]);
    if (!allowedHosts.has(parsed.hostname)) {
      return textResult(`Only worshipmetrics.com pages can be fetched; got host "${parsed.hostname}".`, true);
    }
    path = parsed.pathname;
  } catch {
    return textResult(`"${raw}" is not a valid URL or path.`, true);
  }

  if (!path.startsWith('/kb/')) {
    return textResult(
      'Only knowledge-base pages under /kb/ are available through this tool. ' +
        'Use search_knowledge_base to find article URLs; for other pages, fetch the ' +
        'page itself with an "Accept: text/markdown" header.',
      true,
    );
  }
  if (!path.endsWith('/')) path += '/';

  const response = await fetchStatic(path, context);
  if (!response.ok) {
    return textResult(
      `No article found at ${path} (HTTP ${response.status}). Use search_knowledge_base to find valid URLs.`,
      true,
    );
  }
  const html = await response.text();
  return textResult(htmlToMarkdown(html, new URL(path, SITE_ORIGIN)));
}

async function handleToolCall(
  context: APIContext,
  id: RpcId,
  params: Record<string, unknown> | undefined,
): Promise<Response> {
  const name = params?.name;
  const args = (params?.arguments ?? {}) as Record<string, unknown>;
  switch (name) {
    case 'get_product_overview':
      return rpcResult(id, textResult(PRODUCT_OVERVIEW));
    case 'search_knowledge_base':
      return rpcResult(id, await searchKnowledgeBase(context, args));
    case 'get_kb_article':
      return rpcResult(id, await getKbArticle(context, args));
    default:
      return rpcError(id, -32602, `Unknown tool: ${String(name)}`);
  }
}

export async function handleMcpRequest(context: APIContext): Promise<Response> {
  const httpMethod = context.request.method.toUpperCase();
  if (httpMethod === 'OPTIONS') {
    return new Response(null, { status: 204, headers: CORS_HEADERS });
  }
  if (httpMethod !== 'POST') {
    // No server-initiated SSE stream (GET) and no session to end (DELETE).
    return new Response(null, { status: 405, headers: { Allow: 'POST, OPTIONS', ...CORS_HEADERS } });
  }

  let message: unknown;
  try {
    message = await context.request.json();
  } catch {
    return rpcError(null, -32700, 'Parse error: request body is not valid JSON.', 400);
  }
  if (Array.isArray(message)) {
    return rpcError(null, -32600, 'JSON-RPC batching is not supported.', 400);
  }
  if (typeof message !== 'object' || message === null) {
    return rpcError(null, -32600, 'Invalid request: expected a JSON-RPC message object.', 400);
  }

  const { id, method, params } = message as {
    id?: RpcId | null;
    method?: unknown;
    params?: Record<string, unknown>;
  };

  // Notifications and client responses expect no body back.
  if (typeof method !== 'string' || id === undefined || id === null) {
    return new Response(null, { status: 202, headers: CORS_HEADERS });
  }

  try {
    switch (method) {
      case 'initialize': {
        const requested = typeof params?.protocolVersion === 'string' ? params.protocolVersion : '';
        return rpcResult(id, {
          protocolVersion: PROTOCOL_VERSIONS.has(requested) ? requested : LATEST_PROTOCOL,
          capabilities: { tools: { listChanged: false } },
          serverInfo: SERVER_INFO,
          instructions: INSTRUCTIONS,
        });
      }
      case 'ping':
        return rpcResult(id, {});
      case 'tools/list':
        return rpcResult(id, { tools: TOOL_DEFINITIONS });
      case 'tools/call':
        return await handleToolCall(context, id, params);
      default:
        return rpcError(id, -32601, `Method not found: ${method}`);
    }
  } catch (error) {
    return rpcError(id, -32603, `Internal error: ${error instanceof Error ? error.message : String(error)}`);
  }
}
