/**
 * Real Tech Manager captures used across the Present and Patch pages.
 * Served from public/ rather than R2 so the files live with the repo.
 */
const APP = "/images/app";

export type AppScreenshot = {
  src: string;
  alt: string;
  /** Caption printed under the frame — point at what the reader should notice. */
  caption: string;
  /** Intrinsic size. These differ per capture — never share one height, or the
   *  shorter images stretch to fill the taller box. */
  width: number;
  height: number;
};

export const slideEditor: AppScreenshot = {
  src: `${APP}/worship-metrics-slide-editor.jpg`,
  alt: "The WorshipMetrics slide editor with the Amazing Grace presentation open, showing the layers panel and a 1920x1080 canvas",
  caption:
    "The Edit tab, mid-song. Every element on the slide is its own layer — the attribution line, the lyric block, the shape behind it — so the background can change without touching a word of the text.",
  width: 1920,
  height: 889
};

export const cloudEditor: AppScreenshot = {
  src: `${APP}/worship-metrics-cloud-slide-editor.jpg`,
  alt: "The WorshipMetrics slide editor open in a browser, editing an Amazing Grace lyric slide over a galaxy background with the full text properties panel and media library",
  caption:
    "The full editor — canvas, text properties, media library — is a browser tab, not an install. Sign in from the study or the sofa, fix the line, and the change is already in Sunday's playlist for the whole team.",
  width: 1920,
  height: 1080
};

export const lyricsSlides: AppScreenshot = {
  src: `${APP}/worship-metrics-lyrics-slides.jpg`,
  alt: "The WorshipMetrics Present tab showing all 34 lyric slides for Amazing Grace with the arrangement roadmap above them",
  caption:
    "Every slide in the song, laid out at once, with the arrangement running along the top — Verse 1, Verse 2, Exodus 1:1. The operator can see where the song is going before the worship leader gets there.",
  width: 1920,
  height: 1172,
};

export const scriptureBrowser: AppScreenshot = {
  src: `${APP}/worship-metrics-scripture-browser.jpg`,
  alt: "The WorshipMetrics scripture browser in Live Mode showing John 3:16-28 in the KJV as ready slides, with the live verse marked orange and mirrored on the program monitor",
  caption:
    "Pick a translation, click the book, shift-click the verse range — the passage becomes slides before you finish reading it. In Live Mode the verse you click goes straight to the program screen, one slide per verse, with the timers still running beside it.",
  width: 1920,
  height: 1080
};

export const stageDisplay: AppScreenshot = {
  src: `${APP}/worship-metrics-stage-display-chords.jpg`,
  alt: "The WorshipMetrics stage display editor showing the Band Confidence layout with green chord rows above the lyrics of Amazing Grace, a chords toggle, and a key selector set to as written (G)",
  caption:
    "The band's confidence monitor is its own layout, not a mirror of the projector — chord rows draw above the lyrics in a color the band can spot at a glance, the next lines wait underneath, and the key selector re-chords the whole song when the capo goes on.",
  width: 1920,
  height: 1080
};

export const overlays: AppScreenshot = {
  src: `${APP}/worship-metrics-overlays-editor.jpg`,
  alt: "The WorshipMetrics overlay editor showing a transparent canvas with a media overlay selected and a list of saved overlays",
  caption:
    "Overlays are built on a transparent canvas — the checkerboard is what the projector will see straight through. Name keys, announcements, and media sit in a list you can show or hide without touching the slide underneath.",
  width: 1920,
  height: 1017
};

export const patchDevicesGrid: AppScreenshot = {
  src: `${APP}/worship-metrics-patch-devices-grid.jpg`,
  alt: "The Devices inventory in WorshipMetrics Patch: 80 devices grouped by category — AV receivers, PTZ cameras, security cameras, displays, and network gear — each card carrying its brand, model, and IP address",
  caption:
    "The inventory after a network scan: every device becomes a card with its brand, model, and IP address, grouped the way a tech thinks — audio, video, network, computers. Ping the room, scan for newcomers, or import the integrator's drawing, all from the same toolbar.",
  width: 2067,
  height: 1122,
};

export const patchDevicesList: AppScreenshot = {
  src: `${APP}/worship-metrics-patch-devices-list.jpg`,
  alt: "The Devices list view in WorshipMetrics Patch: a table of devices with type, brand, model, IP address, status, and capability flags like PTZ, NDI, RTSP, and AirPlay",
  caption:
    "The same inventory as a table — type, brand, model, IP, status — with capability flags the platform detected on its own: which cameras speak NDI and RTSP, which displays answer to AirPlay. One toggle away from the card view.",
  width: 2062,
  height: 1120,
};

export const patchSignalMap: AppScreenshot = {
  src: `${APP}/worship-metrics-patch-signal-map.jpg`,
  alt: "The Signal Map in WorshipMetrics Patch: dozens of device nodes wired with labeled Ethernet runs, category filters along the top, and a wiring-audit counter flagging issues to review",
  caption:
    "The Signal Map in Detailed mode: every node carries its ports, PoE draw, and labeled cable runs, and the issues counter up top is the wiring audit working through the map. Filter by category, search for a cable ID, or flip to Simple when you just need the shape of the system.",
  width: 2076,
  height: 1131,
};

export const printableWiringDiagram: AppScreenshot = {
  src: `${APP}/worship-metrics-printable-wiring-diagram.jpg`,
  alt: "A printable WorshipMetrics System Wiring Diagram: 14 devices and 16 cables drawn as clean labeled boxes and routed Ethernet runs, with a generation timestamp under the title",
  caption:
    "The one-click System Wiring Diagram — integrator-proposal style, every run carrying its permanent cable ID, and a generation timestamp under the title, so the page answers its own “is this current?” question.",
  width: 1300,
  height: 997,
};

export const printablePatchSheet: AppScreenshot = {
  src: `${APP}/worship-metrics-printable-patch-sheet.jpg`,
  alt: "A printable WorshipMetrics Patch Sheet listing 16 connections — cable ID, signal type, from-device and port, to-device and port — with a generation timestamp under the title",
  caption:
    "The Patch Sheet, cable by cable: each row names the signal, both devices, and both ports, keyed to the same IDs on the map and on the physical labels. Clip it to the rack door and re-patching after an event stops being archaeology.",
  width: 1006,
  height: 1136,
};
