// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import icon from 'astro-icon';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://worshipmetrics.com',
  output: 'server',
  adapter: cloudflare(),
  integrations: [mdx(), sitemap(), icon()],
  vite: {
    plugins: [tailwindcss()]
  }
});
