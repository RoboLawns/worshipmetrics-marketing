const LOGO_BASE = "https://pub-a4845709a76642e7943bcb8b80677531.r2.dev/main/central-control-logos";

const LOGOS = {
  vmix: `${LOGO_BASE}/vmix.png`,
  blackmagic: `${LOGO_BASE}/blackmagic-design.svg`,
  obs: `${LOGO_BASE}/obs-studio.svg`,
  roland: `${LOGO_BASE}/roland.svg`,
  ma: `${LOGO_BASE}/ma-lighting.svg`,
  avolites: `${LOGO_BASE}/avolites.svg`,
  chamsys: `${LOGO_BASE}/chamsys.svg`,
  resolume: `${LOGO_BASE}/resolume.svg`,
  qlab: `${LOGO_BASE}/figure53-qlab.svg`,
  ptzoptics: `${LOGO_BASE}/ptzoptics.svg`,
  panasonic: `${LOGO_BASE}/panasonic.svg`,
  behringer: `${LOGO_BASE}/behringer.svg`,
  soundcraft: `${LOGO_BASE}/soundcraft.svg`,
  bitfocus: `${LOGO_BASE}/bitfocus-companion.svg`,
  magewell: `${LOGO_BASE}/magewell.svg`,
  ross: `${LOGO_BASE}/Ross%20Logo.png`,
} as const;

function getLogoUrl(brand: string, name: string) {
  const key = `${brand} ${name}`.toLowerCase();

  if (key.includes("blackmagic")) return LOGOS.blackmagic;
  if (key.includes("studiocoast") || key.includes("vmix")) return LOGOS.vmix;
  if (key.includes("obs")) return LOGOS.obs;
  if (key.includes("roland")) return LOGOS.roland;
  if (key.includes("ross")) return LOGOS.ross;
  if (key.includes("magewell")) return LOGOS.magewell;
  if (key.includes("ma lighting") || key.includes("grandma")) return LOGOS.ma;
  if (key.includes("avolites")) return LOGOS.avolites;
  if (key.includes("chamsys") || key.includes("magicq")) return LOGOS.chamsys;
  if (key.includes("resolume")) return LOGOS.resolume;
  if (key.includes("figure 53") || key.includes("qlab")) return LOGOS.qlab;
  if (key.includes("ptzoptics")) return LOGOS.ptzoptics;
  if (key.includes("panasonic")) return LOGOS.panasonic;
  if (key.includes("behringer") || key.includes("midas")) return LOGOS.behringer;
  if (key.includes("soundcraft")) return LOGOS.soundcraft;
  if (key.includes("bitfocus") || key.includes("companion")) return LOGOS.bitfocus;

  return undefined;
}

/**
 * Honest per-item status:
 *  - "control": WorshipMetrics drives the device directly (Tech Manager and/or cloud).
 *  - "cue": Present fires outbound cues at it (OSC / RossTalk / MIDI / HTTP presets).
 *  - "monitored": live status monitoring, no control surface.
 *  - "documented": lives in the device catalog — Signal Map, factory port maps, health checks.
 */
export type IntegrationStatus = "control" | "cue" | "monitored" | "documented";

export const STATUS_META: Record<IntegrationStatus, { label: string; dotClass: string }> = {
  control: { label: "Direct control", dotClass: "bg-emerald-500" },
  cue: { label: "Cue target via Present", dotClass: "bg-indigo-500" },
  monitored: { label: "Status monitoring", dotClass: "bg-sky-500" },
  documented: { label: "Documented & monitored", dotClass: "bg-slate-400" },
};

/** The current device-catalog census (shared/device-catalog.ts in the app). */
export const catalogStats = {
  entries: 422,
  manufacturers: 114,
  portMapped: 348,
};

export const DATA = {
  switchers: {
    title: "Video Switchers",
    tagline: "The heart of your live production.",
    items: [
      { brand: "StudioCoast", name: "vMix", status: "control" },
      { brand: "OBS Project", name: "OBS Studio", status: "control" },
      { brand: "Blackmagic", name: "ATEM", status: "control" },
      { brand: "Roland", name: "V-160HD", status: "documented" },
      { brand: "Ross", name: "Carbonite", status: "documented" },
    ],
  },
  cameras: {
    title: "PTZ Cameras",
    tagline: "Pan, tilt, zoom — from anywhere.",
    items: [
      { brand: "PTZOptics", name: "All Models", status: "control" },
      { brand: "VISCA", name: "VISCA-over-IP (TCP)", status: "control" },
      { brand: "BirdDog", name: "PTZ Cameras", status: "control" },
      { brand: "Panasonic", name: "UE Series", status: "documented" },
    ],
  },
  audio: {
    title: "Audio Mixers & DSP",
    tagline: "Dialed in from FOH to livestream.",
    items: [
      { brand: "Behringer", name: "X32", status: "control" },
      { brand: "Midas", name: "M32", status: "control" },
      { brand: "QSC", name: "Q-SYS", status: "control" },
      { brand: "Behringer", name: "X-Air", status: "documented" },
      { brand: "Soundcraft", name: "Ui Series", status: "documented" },
    ],
  },
  lighting: {
    title: "Lighting Consoles",
    tagline: "Your rig, documented and monitored.",
    items: [
      { brand: "MA Lighting", name: "grandMA3", status: "documented" },
      { brand: "MA Lighting", name: "grandMA2", status: "documented" },
      { brand: "Avolites", name: "Titan", status: "documented" },
      { brand: "Chamsys", name: "MagicQ", status: "documented" },
    ],
  },
  media: {
    title: "Playback & Presentation",
    tagline: "Playback and graphics, cued from Present.",
    items: [
      { brand: "Renewed Vision", name: "ProPresenter", status: "cue" },
      { brand: "Figure 53", name: "QLab", status: "cue" },
      { brand: "Resolume", name: "Arena", status: "cue" },
      { brand: "disguise", name: "Media Servers", status: "cue" },
      { brand: "Blackmagic", name: "HyperDeck", status: "monitored" },
    ],
  },
  routing: {
    title: "Video Routing & Conversion",
    tagline: "Documented paths for every pixel.",
    items: [
      { brand: "Blackmagic", name: "VideoHub", status: "documented" },
      { brand: "Magewell", name: "ProConvert", status: "documented" },
    ],
  },
  network: {
    title: "Network",
    tagline: "The network under it all, watched.",
    items: [
      { brand: "Ubiquiti", name: "UniFi", status: "control" },
    ],
  },
  ecosystem: {
    title: "Ecosystem & Protocols",
    tagline: "The plumbing that connects everything.",
    items: [
      { brand: "Bitfocus", name: "Companion", status: "cue" },
      { brand: "Generic", name: "OSC", status: "cue" },
      { brand: "Generic", name: "RossTalk", status: "cue" },
      { brand: "Generic", name: "MIDI", status: "cue" },
      { brand: "Generic", name: "HTTP", status: "cue" },
    ],
  },
} as const;

export const INTEGRATION_CATEGORY_ORDER = [
  "switchers",
  "cameras",
  "audio",
  "lighting",
  "media",
  "routing",
  "network",
  "ecosystem",
] as const;

export type IntegrationCategoryKey = (typeof INTEGRATION_CATEGORY_ORDER)[number];

export const integrationCategories = INTEGRATION_CATEGORY_ORDER.map((key) => ({
  key,
  ...DATA[key],
  items: DATA[key].items.map((item) => ({
    ...item,
    logoUrl: getLogoUrl(item.brand, item.name),
  })),
  count: DATA[key].items.length,
}));

export const integrationTotals = {
  totalDevices: integrationCategories.reduce((sum, category) => sum + category.count, 0),
  totalCategories: integrationCategories.length,
};

export const homepageIntegrationTiles = [
  { brand: "Blackmagic", meta: "ATEM", logoUrl: LOGOS.blackmagic },
  { brand: "vMix", meta: "StudioCoast", logoUrl: LOGOS.vmix },
  { brand: "OBS", meta: "Studio", logoUrl: LOGOS.obs },
  { brand: "PTZOptics", meta: "PTZ", logoUrl: LOGOS.ptzoptics },
  { brand: "BirdDog", meta: "PTZ", logoUrl: undefined },
  { brand: "Behringer", meta: "X32", logoUrl: LOGOS.behringer },
  { brand: "Midas", meta: "M32", logoUrl: LOGOS.behringer },
  { brand: "Q-SYS", meta: "QSC", logoUrl: undefined },
  { brand: "UniFi", meta: "Ubiquiti", logoUrl: undefined },
  { brand: "HyperDeck", meta: "Blackmagic", logoUrl: LOGOS.blackmagic },
  { brand: "ProPresenter", meta: "Cue target", logoUrl: undefined },
  { brand: "Q-Lab", meta: "Cue target", logoUrl: LOGOS.qlab },
  { brand: "Resolume", meta: "Cue target", logoUrl: LOGOS.resolume },
  { brand: "Companion", meta: "Cue target", logoUrl: LOGOS.bitfocus },
  { brand: "grandMA3", meta: "Documented", logoUrl: LOGOS.ma },
];

export const homepageCategoryCounts = [
  { label: "device families under direct control", count: "8" },
  { label: "devices documented & monitored", count: String(catalogStats.entries) },
  { label: "manufacturers", count: String(catalogStats.manufacturers) },
  { label: "factory port maps", count: String(catalogStats.portMapped) },
];
