// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import icon from 'astro-icon';

import tailwindcss from '@tailwindcss/vite';

import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  site: 'https://worshipmetrics.com',
  integrations: [mdx(), sitemap(), icon()],

  vite: {
    plugins: [tailwindcss()]
  },

  adapter: cloudflare()
});