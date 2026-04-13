import typography from '@tailwindcss/typography';

export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#0B0E14',
        surface: '#13181F',
        accent: '#3B82F6',
        'accent-warm': '#F59E0B',
        border: '#1E2733',
        muted: '#64748B',
      },
      fontFamily: {
        display: ['"DM Serif Display"', 'serif'],
        sans: ['"IBM Plex Sans"', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'monospace'],
      },
    },
  },
  plugins: [typography],
};
