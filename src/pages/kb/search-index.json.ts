// Compact machine-readable index of every knowledge-base article, prerendered
// at build time so the /mcp server (and any agent that finds it) can search
// the KB at runtime without bundling article bodies into the Worker. One row
// per entry: title, description, tags, human section label, and site-relative
// URL matching the collection's page route.

import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const prerender = true;

interface IndexRow {
  title: string;
  description: string;
  tags: string[];
  section: string;
  url: string;
}

// Same slugification the kb page routes use for brand path segments.
function brandSlug(brand: string): string {
  return brand.toLowerCase().replace(/[\s\/]+/g, '-');
}

// deviceCategory → [path segment, section label]. Categories without a page
// route (none exist today) are skipped rather than indexed as dead links.
const DEVICE_SECTIONS: Record<string, [string, string]> = {
  encoder: ['encoders', 'Hardware Encoders'],
  mixer: ['mixers', 'Audio Mixers'],
  switcher: ['switchers', 'Video Switchers'],
};

export const GET: APIRoute = async () => {
  const rows: IndexRow[] = [];
  const push = (
    data: { title: string; description: string; tags?: string[] },
    section: string,
    url: string,
  ) => {
    rows.push({
      title: data.title,
      description: data.description,
      tags: data.tags ?? [],
      section,
      url,
    });
  };

  for (const e of await getCollection('articles')) {
    push(e.data, 'Platform Guides', `/kb/articles/${e.id}/`);
  }
  for (const e of await getCollection('cameras')) {
    push(e.data, 'PTZ Cameras', `/kb/cameras/${brandSlug(e.data.brand)}/${e.id}/`);
  }
  for (const e of await getCollection('devices')) {
    const section = DEVICE_SECTIONS[e.data.deviceCategory];
    if (section) push(e.data, section[1], `/kb/${section[0]}/${brandSlug(e.data.brand)}/${e.id}/`);
  }
  for (const e of await getCollection('software')) {
    push(e.data, 'Streaming Software', `/kb/software/${e.data.app}/${e.id}/`);
  }
  for (const e of await getCollection('workflows')) {
    push(e.data, 'Complete Workflows', `/kb/workflows/${e.id}/`);
  }
  for (const e of await getCollection('comparisons')) {
    push(e.data, 'Comparisons', `/kb/compare/${e.id}/`);
  }
  for (const e of await getCollection('troubleshooting')) {
    push(e.data, 'Troubleshooting', `/kb/troubleshooting/${e.id}/`);
  }
  for (const e of await getCollection('budget')) {
    push(e.data, 'Budget Guides', `/kb/budget/${e.id}/`);
  }

  return new Response(JSON.stringify(rows), {
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
