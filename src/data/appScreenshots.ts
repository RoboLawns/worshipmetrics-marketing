/**
 * Real Tech Manager captures used across the Present pages.
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
