// Generates the default Open Graph share card (1200x630) from brand-kit vectors.
// Run: node scripts/generate-og.mjs  →  writes public/og-default.png
import { Resvg } from "@resvg/resvg-js";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));

const INK = "#0B0D10";
const BLUE = "#2B7FF0";
const PAPER_SOFT = "#E9EEF4";

// Lockup geometry is locked artwork from Brand Kit v1.0 — do not re-type.
const svg = `
<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="630" fill="${INK}"/>
  <!-- faint beat watermark -->
  <path d="M3 21.7 H8.1 L14.9 3 L23.4 37 L30.2 21.7 H35.3"
        transform="translate(830,330) scale(11)"
        fill="none" stroke="#142C55" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.35"/>

  <!-- mono eyebrow -->
  <text x="600" y="150" text-anchor="middle" font-family="IBM Plex Mono" font-weight="600"
        font-size="22" letter-spacing="6" fill="#4292F2">LIVE STREAMING &#183; PRODUCTION &#183; 7-DAY SUPPORT</text>

  <!-- lockup, centered at (600, 265), scaled 1.75x -->
  <g transform="translate(600,265) scale(1.75) translate(-156,-48)">
    <text x="139" y="59" text-anchor="end" font-family="Archivo" font-weight="800"
          font-size="34" letter-spacing="-1" fill="${PAPER_SOFT}">worship</text>
    <path d="M145 48 H151 L158.6 27.8 L167.8 64.6 L175.4 48 H181"
          fill="none" stroke="${BLUE}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="187" y="59" text-anchor="start" font-family="Archivo" font-weight="800"
          font-size="34" letter-spacing="-1" fill="${BLUE}">metrics</text>
  </g>

  <!-- tagline -->
  <text x="600" y="450" text-anchor="middle" font-family="Archivo" font-weight="800"
        font-size="68" letter-spacing="-1.5" fill="#FFFFFF">Your live stream, <tspan fill="${BLUE}">handled.</tspan></text>

  <!-- bottom line -->
  <text x="600" y="560" text-anchor="middle" font-family="IBM Plex Mono" font-weight="600"
        font-size="19" letter-spacing="4" fill="#78828F">WORSHIPMETRICS.COM &#183; 910-WORSHIP &#183; 7 DAYS A WEEK</text>
</svg>`;

const resvg = new Resvg(svg, {
  fitTo: { mode: "width", value: 1200 },
  font: {
    fontFiles: [
      join(here, "fonts", "Archivo-ExtraBold.ttf"),
      join(here, "fonts", "Archivo-SemiBold.ttf"),
      join(here, "fonts", "IBMPlexMono-SemiBold.ttf"),
    ],
    loadSystemFonts: false,
  },
});

const png = resvg.render().asPng();
const out = join(here, "..", "public", "og-default.png");
writeFileSync(out, png);
console.log(`Wrote ${out} (${png.length} bytes)`);
