const LOGO_BASE = "https://pub-a4845709a76642e7943bcb8b80677531.r2.dev/main/central-control-logos";

const LOGOS = {
  vizrt: `${LOGO_BASE}/vizrt.svg`,
  newtek: `${LOGO_BASE}/newtek.svg`,
  vmix: `${LOGO_BASE}/vmix.png`,
  blackmagic: `${LOGO_BASE}/blackmagic-design.svg`,
  obs: `${LOGO_BASE}/obs-studio.svg`,
  livestream: `${LOGO_BASE}/livestream-vimeo.svg`,
  roland: `${LOGO_BASE}/roland.svg`,
  magewell: `${LOGO_BASE}/magewell.svg`,
  osee: `${LOGO_BASE}/osee.svg`,
  aja: `${LOGO_BASE}/aja.svg`,
  turtleav: `${LOGO_BASE}/turtle-av.svg`,
  zen: `${LOGO_BASE}/zen-videowall.svg`,
  ma: `${LOGO_BASE}/ma-lighting.svg`,
  obsidian: `${LOGO_BASE}/obsidian-control.svg`,
  avolites: `${LOGO_BASE}/avolites.svg`,
  chamsys: `${LOGO_BASE}/chamsys.svg`,
  showcad: `${LOGO_BASE}/showcad.svg`,
  elation: `${LOGO_BASE}/elation.svg`,
  resolume: `${LOGO_BASE}/resolume.svg`,
  qlab: `${LOGO_BASE}/figure53-qlab.svg`,
  millumin: `${LOGO_BASE}/millumin.svg`,
  mitti: `${LOGO_BASE}/imimot-mitti.svg`,
  h2r: `${LOGO_BASE}/h2r-graphics.svg`,
  ptzoptics: `${LOGO_BASE}/ptzoptics.svg`,
  aida: `${LOGO_BASE}/aida-imaging.svg`,
  panasonic: `${LOGO_BASE}/panasonic.svg`,
  elgato: `${LOGO_BASE}/elgato.svg`,
  xkeys: `${LOGO_BASE}/xkeys.svg`,
  akai: `${LOGO_BASE}/akai-pro.svg`,
  behringer: `${LOGO_BASE}/behringer.svg`,
  novation: `${LOGO_BASE}/novation.svg`,
  soundcraft: `${LOGO_BASE}/soundcraft.svg`,
  bitfocus: `${LOGO_BASE}/bitfocus-companion.svg`,
  irisdown: `${LOGO_BASE}/irisdown.svg`,
  tyst: `${LOGO_BASE}/tyst.svg`,
  sankeys: `${LOGO_BASE}/sankeys.svg`,
  katovision: `${LOGO_BASE}/katovision.svg`,
  ross: `${LOGO_BASE}/Ross%20Logo.png`,
} as const;

function getLogoUrl(brand: string, name: string) {
  const key = `${brand} ${name}`.toLowerCase();

  if (key.includes("blackmagic")) return LOGOS.blackmagic;
  if (key.includes("studiocoast") || key.includes("vmix")) return LOGOS.vmix;
  if (key.includes("vizrt") || key.includes("tricaster") || key.includes("vectar") || key.includes("3play")) return LOGOS.vizrt;
  if (key.includes("newtek")) return LOGOS.newtek;
  if (key.includes("obs")) return LOGOS.obs;
  if (key.includes("livestream") || key.includes("vimeo")) return LOGOS.livestream;
  if (key.includes("roland")) return LOGOS.roland;
  if (key.includes("ross")) return LOGOS.ross;
  if (key.includes("magewell")) return LOGOS.magewell;
  if (key.includes("osee")) return LOGOS.osee;
  if (key.includes("aja")) return LOGOS.aja;
  if (key.includes("turtle av")) return LOGOS.turtleav;
  if (key.includes("zen ndi") || key.includes("zen videowall")) return LOGOS.zen;
  if (key.includes("ma lighting") || key.includes("grandma")) return LOGOS.ma;
  if (key.includes("obsidian") || key.includes("onyx")) return LOGOS.obsidian;
  if (key.includes("avolites")) return LOGOS.avolites;
  if (key.includes("chamsys") || key.includes("magicq")) return LOGOS.chamsys;
  if (key.includes("showcad")) return LOGOS.showcad;
  if (key.includes("elation")) return LOGOS.elation;
  if (key.includes("resolume")) return LOGOS.resolume;
  if (key.includes("figure 53") || key.includes("qlab")) return LOGOS.qlab;
  if (key.includes("millumin")) return LOGOS.millumin;
  if (key.includes("imimot") || key.includes("mitti")) return LOGOS.mitti;
  if (key.includes("h2r")) return LOGOS.h2r;
  if (key.includes("ptzoptics")) return LOGOS.ptzoptics;
  if (key.includes("aida")) return LOGOS.aida;
  if (key.includes("panasonic")) return LOGOS.panasonic;
  if (key.includes("elgato") || key.includes("stream deck")) return LOGOS.elgato;
  if (key.includes("x-keys") || key.includes("xkeys") || key.includes("pi engineering")) return LOGOS.xkeys;
  if (key.includes("akai")) return LOGOS.akai;
  if (key.includes("behringer") || key.includes("midas")) return LOGOS.behringer;
  if (key.includes("novation")) return LOGOS.novation;
  if (key.includes("soundcraft")) return LOGOS.soundcraft;
  if (key.includes("bitfocus") || key.includes("companion")) return LOGOS.bitfocus;
  if (key.includes("irisdown")) return LOGOS.irisdown;
  if (key.includes("tyst")) return LOGOS.tyst;
  if (key.includes("san-keys") || key.includes("sankeys")) return LOGOS.sankeys;
  if (key.includes("katovision")) return LOGOS.katovision;

  return undefined;
}

export const DATA = {
  switchers: {
    title: "Video Switchers",
    tagline: "The heart of your live production.",
    items: [
      { brand: "Blackmagic", name: "ATEM" },
      { brand: "StudioCoast", name: "vMix" },
      { brand: "Vizrt", name: "TriCaster" },
      { brand: "Vizrt", name: "Vectar" },
      { brand: "Vizrt", name: "3Play" },
      { brand: "OBS Project", name: "OBS Studio" },
      { brand: "Livestream", name: "Studio" },
      { brand: "Roland", name: "V-160HD" },
      { brand: "Magewell", name: "Director Mini" },
      { brand: "Osee", name: "GoStream Deck" },
      { brand: "Ross", name: "Carbonite" },
    ],
  },
  lighting: {
    title: "Lighting Consoles",
    tagline: "From house lights to stage looks.",
    items: [
      { brand: "MA Lighting", name: "grandMA3" },
      { brand: "MA Lighting", name: "grandMA2" },
      { brand: "Obsidian", name: "Onyx" },
      { brand: "Avolites", name: "Titan" },
      { brand: "Chamsys", name: "MagicQ" },
      { brand: "ShowCAD", name: "Artist" },
    ],
  },
  cameras: {
    title: "PTZ Cameras",
    tagline: "Pan, tilt, zoom — from anywhere.",
    items: [
      { brand: "PTZOptics", name: "All Models" },
      { brand: "AIDA Imaging", name: "PTZ Cameras" },
      { brand: "Blackmagic", name: "HTTP Camera Control" },
      { brand: "Panasonic", name: "UE Series" },
      { brand: "NDI", name: "PTZ" },
      { brand: "VISCA", name: "TCP" },
      { brand: "VISCA", name: "UDP" },
    ],
  },
  audio: {
    title: "Audio Mixers",
    tagline: "Dialed in from FOH to livestream.",
    items: [
      { brand: "Behringer", name: "X32" },
      { brand: "Behringer", name: "X-Air" },
      { brand: "Midas", name: "M32" },
      { brand: "Soundcraft", name: "Ui Series" },
    ],
  },
  media: {
    title: "Media & Graphics",
    tagline: "Lower thirds, lyrics, and playback.",
    items: [
      { brand: "H2R", name: "Graphics" },
      { brand: "Resolume", name: "Arena" },
      { brand: "Figure 53", name: "Q-Lab" },
      { brand: "Millumin", name: "Millumin" },
      { brand: "Imimot", name: "Mitti" },
      { brand: "Blackmagic", name: "HyperDeck" },
      { brand: "Microsoft", name: "PowerPoint" },
    ],
  },
  routing: {
    title: "Video Routing & Conversion",
    tagline: "Move pixels where they need to go.",
    items: [
      { brand: "Blackmagic", name: "VideoHub" },
      { brand: "AJA", name: "Kumo Routers" },
      { brand: "Turtle AV", name: "4x4 / 8x8 Videowall" },
      { brand: "NDI Stuff", name: "Zen NDI Router" },
      { brand: "Magewell", name: "ProConvert" },
    ],
  },
  surfaces: {
    title: "Control Surfaces",
    tagline: "Hands-on control for your volunteers.",
    items: [
      { brand: "Elgato", name: "Stream Deck" },
      { brand: "Elgato", name: "Stream Deck XL" },
      { brand: "Elgato", name: "Stream Deck Mini" },
      { brand: "Elgato", name: "Stream Deck Plus" },
      { brand: "Elgato", name: "Stream Deck Pedal" },
      { brand: "X-keys", name: "XK-24 / XK-68 / XK-80 / XK-128" },
      { brand: "X-keys", name: "XKE-64 Replay" },
      { brand: "X-keys", name: "XKE-124 T-Bar" },
      { brand: "Hexler", name: "TouchOSC" },
      { brand: "NewTek", name: "RS8 / LC-11 / TC Series" },
    ],
  },
  midi: {
    title: "MIDI Controllers",
    tagline: "Repurpose that controller in the closet.",
    items: [
      { brand: "AKAI", name: "APC40 MK2" },
      { brand: "AKAI", name: "APC Mini" },
      { brand: "AKAI", name: "MIDIMIX" },
      { brand: "AKAI", name: "LPD8" },
      { brand: "AKAI", name: "Fire" },
      { brand: "Behringer", name: "X-Touch" },
      { brand: "Behringer", name: "X-Touch Compact / Mini" },
      { brand: "Novation", name: "Launchpad X" },
      { brand: "Novation", name: "Launchkey Mk3" },
      { brand: "Elation", name: "MIDICon 2" },
      { brand: "Generic", name: "MIDI" },
    ],
  },
  ecosystem: {
    title: "Ecosystem & Protocols",
    tagline: "The plumbing that connects everything.",
    items: [
      { brand: "Bitfocus", name: "Companion" },
      { brand: "IrisDown", name: "Remote Show Control" },
      { brand: "IrisDown", name: "Countdown Timer" },
      { brand: "Vicreo", name: "Listener" },
      { brand: "NDI", name: "Router / Connect" },
      { brand: "Generic", name: "OSC" },
      { brand: "Generic", name: "HTTP Listener" },
      { brand: "Generic", name: "HTTP Requester" },
      { brand: "Generic", name: "Websocket Client" },
    ],
  },
} as const;

export const INTEGRATION_CATEGORY_ORDER = [
  "switchers",
  "cameras",
  "lighting",
  "audio",
  "media",
  "routing",
  "surfaces",
  "midi",
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
  { brand: "TriCaster", meta: "Vizrt", logoUrl: LOGOS.vizrt },
  { brand: "OBS", meta: "Studio", logoUrl: LOGOS.obs },
  { brand: "PTZOptics", meta: "PTZ", logoUrl: LOGOS.ptzoptics },
  { brand: "AIDA", meta: "Imaging", logoUrl: LOGOS.aida },
  { brand: "grandMA3", meta: "MA Lighting", logoUrl: LOGOS.ma },
  { brand: "Onyx", meta: "Obsidian", logoUrl: LOGOS.obsidian },
  { brand: "Chamsys", meta: "MagicQ", logoUrl: LOGOS.chamsys },
  { brand: "Behringer", meta: "X32", logoUrl: LOGOS.behringer },
  { brand: "Soundcraft", meta: "Ui Series", logoUrl: LOGOS.soundcraft },
  { brand: "Stream Deck", meta: "Elgato", logoUrl: LOGOS.elgato },
  { brand: "H2R", meta: "Graphics", logoUrl: LOGOS.h2r },
  { brand: "Resolume", meta: "Arena", logoUrl: LOGOS.resolume },
  { brand: "Q-Lab", meta: "Figure 53", logoUrl: LOGOS.qlab },
  { brand: "HyperDeck", meta: "Blackmagic", logoUrl: LOGOS.blackmagic },
  { brand: "Companion", meta: "Bitfocus", logoUrl: LOGOS.bitfocus },
  { brand: "Ross", meta: "Carbonite", logoUrl: LOGOS.ross },
];

export const homepageCategoryCounts = [
  { label: "Switchers", count: "11" },
  { label: "PTZ Cameras", count: "7" },
  { label: "Lighting", count: "6" },
  { label: "Audio Mixers", count: "4" },
  { label: "Media & Graphics", count: "7" },
  { label: "Control Surfaces", count: "25+" },
];
