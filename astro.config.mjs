// @ts-check
import { defineConfig, sessionDrivers } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import icon from 'astro-icon';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://worshipmetrics.com',
  trailingSlash: 'always',
  redirects: {
    '/platform/operations': '/volunteers',
    '/features': '/platform',
    '/integrations/central-control': '/services',
    '/av-team/build-your-av-team': '/av-team',
  },
  output: 'server',
  adapter: cloudflare(),
  session: {
    driver: sessionDrivers.lruCache(),
  },
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => ![
        'https://worshipmetrics.com/kb/search/',
        'https://worshipmetrics.com/pilot-program/thank-you/',
      ].includes(page),
    }),
    icon(),
  ],
  vite: {
    plugins: [tailwindcss()]
  }
});
