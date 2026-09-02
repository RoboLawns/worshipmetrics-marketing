// HTML → Markdown for agent content negotiation.
//
// Agents that send `Accept: text/markdown` get the rendered page as clean
// markdown instead of scraping our Tailwind-dense HTML. The output follows the
// shape Cloudflare documents for its "Markdown for agents" feature
// (https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/):
// YAML frontmatter from the page's meta tags, the `<main>` content as markdown,
// then any JSON-LD structured data as a fenced ```json block.
//
// Hand-rolled rather than a library because the converter has to run in two
// runtimes with one bundle: workerd in production and Vite/Node in `astro dev`.
// Turndown needs a DOM and workerd's HTMLRewriter doesn't exist in Node, so a
// dependency-free tokenizer over our own well-formed Astro output is the only
// option that behaves identically in both.

const VOID_ELEMENTS = new Set([
  'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
  'param', 'source', 'track', 'wbr',
]);

// Content inside these is raw text: a `<` in a script body is not a tag.
const RAW_TEXT_ELEMENTS = new Set(['script', 'style', 'textarea', 'title']);

// Dropped wholesale, subtree included: non-content, interactive-only, or
// decorative. `nav`/`form` match what Cloudflare's converter strips.
const SKIP_ELEMENTS = new Set([
  'script', 'style', 'svg', 'noscript', 'template', 'iframe', 'canvas',
  'object', 'embed', 'audio', 'video', 'select', 'option', 'input', 'textarea',
  'button', 'dialog', 'nav', 'form', 'source', 'track', 'map', 'area',
]);

// Structural containers whose open/close just terminates the current paragraph.
const BLOCK_ELEMENTS = new Set([
  'div', 'section', 'article', 'aside', 'main', 'figure', 'figcaption', 'p',
  'address', 'details', 'summary', 'dd', 'header', 'footer',
]);

// Tailwind classes that make an element invisible: its content (pagefind
// metadata, screen-reader duplicates of visual content) isn't page copy.
const HIDDEN_CLASS_TOKENS = new Set(['hidden', 'sr-only', 'invisible']);

function isHiddenByClass(classValue: string | undefined): boolean {
  if (!classValue) return false;
  return classValue.split(/\s+/).some((token) => HIDDEN_CLASS_TOKENS.has(token));
}

const NAMED_ENTITIES: Record<string, string> = {
  amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ',
  mdash: '—', ndash: '–', hellip: '…',
  lsquo: '‘', rsquo: '’', ldquo: '“', rdquo: '”',
  copy: '©', reg: '®', trade: '™', times: '×',
  middot: '·', bull: '•', deg: '°',
  larr: '←', rarr: '→', uarr: '↑', darr: '↓',
};

function decodeEntities(text: string): string {
  return text.replace(/&(#x?[0-9a-f]+|[a-z]+);/gi, (match, body: string) => {
    if (body[0] === '#') {
      const code = body[1].toLowerCase() === 'x'
        ? parseInt(body.slice(2), 16)
        : parseInt(body.slice(1), 10);
      return Number.isNaN(code) ? match : String.fromCodePoint(code);
    }
    return NAMED_ENTITIES[body.toLowerCase()] ?? match;
  });
}

function collapseWhitespace(text: string): string {
  return text.replace(/[\s ]+/g, ' ').trim();
}

interface Token {
  kind: 'open' | 'close' | 'text';
  name?: string;
  attrs?: Record<string, string>;
  selfClosing?: boolean;
  text?: string;
}

const ATTR_RE = /([a-zA-Z_:][-\w:.]*)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+)))?/g;

function parseAttrs(raw: string): Record<string, string> {
  const attrs: Record<string, string> = {};
  for (const match of raw.matchAll(ATTR_RE)) {
    attrs[match[1].toLowerCase()] = decodeEntities(match[2] ?? match[3] ?? match[4] ?? '');
  }
  return attrs;
}

function* tokenize(html: string): Generator<Token> {
  const tagRe = /<!--[\s\S]*?-->|<!(?:DOCTYPE|doctype)[^>]*>|<\/([a-zA-Z][\w-]*)\s*>|<([a-zA-Z][\w-]*)((?:[^>"']|"[^"]*"|'[^']*')*?)(\/?)>/g;
  let last = 0;
  let match: RegExpExecArray | null;
  while ((match = tagRe.exec(html)) !== null) {
    if (match.index > last) {
      yield { kind: 'text', text: html.slice(last, match.index) };
    }
    last = tagRe.lastIndex;
    const [full, closeName, openName, attrRaw, selfClose] = match;
    if (closeName) {
      yield { kind: 'close', name: closeName.toLowerCase() };
    } else if (openName) {
      const name = openName.toLowerCase();
      yield {
        kind: 'open',
        name,
        attrs: attrRaw ? parseAttrs(attrRaw) : {},
        selfClosing: selfClose === '/' || VOID_ELEMENTS.has(name),
      };
      // Raw-text elements: everything up to the matching close tag is text,
      // even if it contains `<`.
      if (RAW_TEXT_ELEMENTS.has(name) && selfClose !== '/') {
        const closeRe = new RegExp(`</${name}\\s*>`, 'i');
        const rest = html.slice(last);
        const closeMatch = closeRe.exec(rest);
        const end = closeMatch ? closeMatch.index : rest.length;
        yield { kind: 'text', text: rest.slice(0, end) };
        yield { kind: 'close', name };
        last = closeMatch ? last + end + closeMatch[0].length : html.length;
        tagRe.lastIndex = last;
      }
    }
    void full;
  }
  if (last < html.length) {
    yield { kind: 'text', text: html.slice(last) };
  }
}

class MarkdownBuilder {
  private blocks: { text: string; tight: boolean }[] = [];
  // Inline frames: index 0 accumulates the current block; a/strong/em/code
  // push a frame and wrap its text on close.
  private frames: { tag: string; href?: string }[] = [];
  private bufs: string[] = [''];
  private listStack: { type: 'ul' | 'ol'; index: number }[] = [];
  private quoteDepth = 0;
  private liPrefix: string | null = null;
  private headingLevel = 0;
  private preText: string | null = null;
  private tableRows: string[][] | null = null;
  private tableRow: string[] | null = null;
  private inCell = false;
  private skipDepth = 0;

  constructor(private baseUrl: URL) {}

  private resolve(href: string): string {
    try {
      return new URL(href, this.baseUrl).href;
    } catch {
      return href;
    }
  }

  private append(text: string): void {
    this.bufs[this.bufs.length - 1] += text;
  }

  private flushBlock(prefix = ''): void {
    if (this.inCell) {
      // Block boundaries inside a table cell just separate words.
      this.append(' ');
      return;
    }
    const text = collapseWhitespace(this.bufs.join(''));
    this.frames = [];
    this.bufs = [''];
    if (!text) return;

    let line = prefix + text;
    let tight = false;
    if (this.liPrefix !== null) {
      line = this.liPrefix + line;
      // Later blocks in the same <li> continue under the marker's indent.
      this.liPrefix = ' '.repeat(this.liPrefix.length);
      tight = true;
    }
    if (this.quoteDepth > 0) {
      line = '> '.repeat(this.quoteDepth) + line;
    }
    this.blocks.push({ text: line, tight });
  }

  private openInline(tag: string, href?: string): void {
    this.frames.push({ tag, href });
    this.bufs.push('');
  }

  private closeInline(tag: string): void {
    // Be lenient about interleaving: unwind to the matching frame.
    while (this.frames.length > 0) {
      const frame = this.frames.pop()!;
      const text = this.bufs.pop()!;
      const inner = collapseWhitespace(text);
      let wrapped = text;
      if (inner) {
        if (frame.tag === 'a' && frame.href) {
          wrapped = `[${inner}](${frame.href})`;
        } else if (frame.tag === 'strong') {
          wrapped = `**${inner}**`;
        } else if (frame.tag === 'em') {
          wrapped = `*${inner}*`;
        } else if (frame.tag === 'code') {
          wrapped = `\`${inner}\``;
        } else if (frame.tag === 'del') {
          wrapped = `~~${inner}~~`;
        }
      }
      this.append(wrapped);
      if (frame.tag === tag) return;
    }
  }

  private listItemMarker(): string {
    const list = this.listStack[this.listStack.length - 1];
    const indent = '  '.repeat(Math.max(0, this.listStack.length - 1));
    if (!list) return '- ';
    if (list.type === 'ol') {
      list.index += 1;
      return `${indent}${list.index}. `;
    }
    return `${indent}- `;
  }

  handle(token: Token): void {
    // Inside a skipped subtree: count nesting until it closes, emit nothing.
    if (this.skipDepth > 0) {
      if (token.kind === 'open' && !token.selfClosing) this.skipDepth += 1;
      else if (token.kind === 'close') this.skipDepth -= 1;
      return;
    }

    if (token.kind === 'text') {
      if (this.preText !== null) {
        this.preText += decodeEntities(token.text!);
      } else if (/\S/.test(token.text!)) {
        this.append(decodeEntities(token.text!));
      } else if (token.text!.length > 0) {
        this.append(' ');
      }
      return;
    }

    const name = token.name!;

    if (token.kind === 'open') {
      const attrs = token.attrs!;
      if (
        SKIP_ELEMENTS.has(name) ||
        attrs['aria-hidden'] === 'true' ||
        'hidden' in attrs ||
        isHiddenByClass(attrs.class)
      ) {
        if (!token.selfClosing) this.skipDepth = 1;
        return;
      }
      if (this.preText !== null) return; // only text matters inside <pre>

      switch (name) {
        case 'h1': case 'h2': case 'h3': case 'h4': case 'h5': case 'h6':
          this.flushBlock();
          this.headingLevel = Number(name[1]);
          break;
        case 'ul': case 'ol':
          this.flushBlock();
          this.listStack.push({ type: name, index: Number(attrs.start ?? 0) });
          break;
        case 'li':
          this.flushBlock();
          this.liPrefix = this.listItemMarker();
          break;
        case 'blockquote':
          this.flushBlock();
          this.quoteDepth += 1;
          break;
        case 'pre':
          this.flushBlock();
          this.preText = '';
          break;
        case 'table':
          this.flushBlock();
          this.tableRows = [];
          break;
        case 'tr':
          this.tableRow = [];
          break;
        case 'th': case 'td':
          if (this.tableRow) {
            this.inCell = true;
            this.bufs = [''];
            this.frames = [];
          }
          break;
        case 'a':
          this.openInline('a', attrs.href && !attrs.href.startsWith('#')
            ? this.resolve(attrs.href)
            : undefined);
          break;
        case 'strong': case 'b':
          this.openInline('strong');
          break;
        case 'em': case 'i':
          this.openInline('em');
          break;
        case 'code':
          this.openInline('code');
          break;
        case 'del': case 's':
          this.openInline('del');
          break;
        case 'img':
          if (attrs.src) {
            this.append(`![${collapseWhitespace(attrs.alt ?? '')}](${this.resolve(attrs.src)})`);
          }
          break;
        case 'br':
          this.append(' ');
          break;
        case 'hr':
          this.flushBlock();
          this.blocks.push({ text: '---', tight: false });
          break;
        case 'dt':
          this.flushBlock();
          this.openInline('strong');
          break;
        default:
          if (BLOCK_ELEMENTS.has(name)) this.flushBlock();
      }
      return;
    }

    // close
    if (this.preText !== null) {
      if (name === 'pre') {
        const code = this.preText.replace(/^\n+|\s+$/g, '');
        this.preText = null;
        if (code) this.blocks.push({ text: '```\n' + code + '\n```', tight: false });
      }
      return;
    }

    switch (name) {
      case 'h1': case 'h2': case 'h3': case 'h4': case 'h5': case 'h6': {
        const level = this.headingLevel || Number(name[1]);
        this.headingLevel = 0;
        this.flushBlock('#'.repeat(level) + ' ');
        break;
      }
      case 'ul': case 'ol':
        this.flushBlock();
        this.listStack.pop();
        break;
      case 'li':
        this.flushBlock();
        this.liPrefix = null;
        break;
      case 'blockquote':
        this.flushBlock();
        this.quoteDepth = Math.max(0, this.quoteDepth - 1);
        break;
      case 'table':
        if (this.tableRows) {
          const rows = this.tableRows;
          this.tableRows = null;
          if (rows.length > 0) {
            const width = Math.max(...rows.map((row) => row.length));
            const pad = (row: string[]) =>
              Array.from({ length: width }, (_, i) => row[i] ?? '');
            const lines = [
              `| ${pad(rows[0]).join(' | ')} |`,
              `| ${Array.from({ length: width }, () => '---').join(' | ')} |`,
              ...rows.slice(1).map((row) => `| ${pad(row).join(' | ')} |`),
            ];
            this.blocks.push({ text: lines.join('\n'), tight: false });
          }
        }
        break;
      case 'tr':
        if (this.tableRows && this.tableRow) this.tableRows.push(this.tableRow);
        this.tableRow = null;
        break;
      case 'th': case 'td':
        if (this.inCell) {
          this.inCell = false;
          const cell = collapseWhitespace(this.bufs.join('')).replace(/\|/g, '\\|');
          this.tableRow?.push(cell);
          this.bufs = [''];
          this.frames = [];
        }
        break;
      case 'a': case 'strong': case 'b': case 'em': case 'i':
      case 'code': case 'del': case 's':
        this.closeInline(
          name === 'b' ? 'strong'
          : name === 'i' ? 'em'
          : name === 's' ? 'del'
          : name,
        );
        break;
      case 'dt':
        this.closeInline('strong');
        this.flushBlock();
        break;
      default:
        if (BLOCK_ELEMENTS.has(name)) this.flushBlock();
    }
  }

  render(): string {
    this.flushBlock();
    let out = '';
    for (let i = 0; i < this.blocks.length; i += 1) {
      const block = this.blocks[i];
      if (i > 0) {
        out += block.tight && this.blocks[i - 1].tight ? '\n' : '\n\n';
      }
      out += block.text;
    }
    return out;
  }
}

interface HeadMetadata {
  title?: string;
  description?: string;
  canonical?: string;
  image?: string;
  jsonLd: unknown[];
}

function extractHead(html: string): HeadMetadata {
  const meta: HeadMetadata = { jsonLd: [] };

  const titleMatch = /<title[^>]*>([\s\S]*?)<\/title>/i.exec(html);
  if (titleMatch) meta.title = collapseWhitespace(decodeEntities(titleMatch[1]));

  for (const tag of html.matchAll(/<(meta|link)\b((?:[^>"']|"[^"]*"|'[^']*')*?)\/?>/gi)) {
    const attrs = parseAttrs(tag[2]);
    if (tag[1].toLowerCase() === 'meta') {
      const key = (attrs.name ?? attrs.property ?? '').toLowerCase();
      if (key === 'description' && !meta.description) meta.description = attrs.content;
      if (key === 'og:image' && !meta.image) meta.image = attrs.content;
    } else if ((attrs.rel ?? '').toLowerCase() === 'canonical' && !meta.canonical) {
      meta.canonical = attrs.href;
    }
  }

  for (const script of html.matchAll(
    /<script\b[^>]*type\s*=\s*["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi,
  )) {
    try {
      const parsed = JSON.parse(script[1]);
      meta.jsonLd.push(...(Array.isArray(parsed) ? parsed : [parsed]));
    } catch {
      // Malformed structured data never blocks the markdown response.
    }
  }

  return meta;
}

function yamlValue(value: string): string {
  return `"${value.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\s+/g, ' ').trim()}"`;
}

// Content boundary: `<main>` on every layout holds the page content, with nav
// and footer chrome outside it. Fall back to <body> for anything unusual.
function extractContent(html: string): string {
  for (const boundary of ['main', 'body']) {
    const openMatch = new RegExp(`<${boundary}(?:\\s[^>]*)?>`, 'i').exec(html);
    if (!openMatch) continue;
    const start = openMatch.index + openMatch[0].length;
    const end = html.toLowerCase().lastIndexOf(`</${boundary}>`);
    return end > start ? html.slice(start, end) : html.slice(start);
  }
  return html;
}

/** Rough token estimate (~4 characters per token) for x-*-tokens headers. */
export function estimateTokens(text: string): number {
  return Math.ceil(text.length / 4);
}

// True when the Accept header explicitly asks for text/markdown at least as
// strongly as text/html. Wildcards ("text/*", "*/*") never opt in — browsers
// send those and must keep getting HTML.
export function prefersMarkdown(accept: string | null): boolean {
  if (!accept || !/text\/markdown/i.test(accept)) return false;

  let markdownQ = 0;
  let htmlQ = 0;
  for (const part of accept.split(',')) {
    const [rawType, ...params] = part.split(';');
    const type = rawType.trim().toLowerCase();
    let q = 1;
    for (const param of params) {
      const [key, value] = param.split('=');
      if (key?.trim().toLowerCase() === 'q') {
        const parsed = parseFloat(value);
        if (!Number.isNaN(parsed)) q = parsed;
      }
    }
    if (type === 'text/markdown') markdownQ = Math.max(markdownQ, q);
    if (type === 'text/html') htmlQ = Math.max(htmlQ, q);
  }
  return markdownQ > 0 && markdownQ >= htmlQ;
}

/**
 * Convert a rendered HTML page to the agent-facing markdown document:
 * frontmatter, body markdown, then JSON-LD in a fenced block.
 */
export function htmlToMarkdown(html: string, requestUrl: URL): string {
  const head = extractHead(html);

  const builder = new MarkdownBuilder(requestUrl);
  for (const token of tokenize(extractContent(html))) {
    builder.handle(token);
  }
  const body = builder.render();

  const frontmatter = ['---'];
  if (head.title) frontmatter.push(`title: ${yamlValue(head.title)}`);
  if (head.description) frontmatter.push(`description: ${yamlValue(head.description)}`);
  frontmatter.push(`url: ${yamlValue(head.canonical ?? requestUrl.href)}`);
  if (head.image) frontmatter.push(`image: ${yamlValue(head.image)}`);
  frontmatter.push('---');

  const parts = [frontmatter.join('\n'), body];
  if (head.jsonLd.length > 0) {
    parts.push('```json\n' + JSON.stringify(head.jsonLd, null, 2) + '\n```');
  }
  return parts.filter(Boolean).join('\n\n') + '\n';
}
