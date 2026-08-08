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
  alt: "The WorshipMetrics scripture browser showing the KJV translation, book and chapter navigation, and Numbers 1 verses building into slides",
  caption:
    "Pick a translation, click the book, shift-click the verse range. Verses-per-slide and reference style are set before anything is generated, and Add to Current drops the passage straight into the live playlist.",
  width: 1920,
  height: 1113
};

export const stageDisplay: AppScreenshot = {
  src: `${APP}/worship-metrics-stage-display-chords.jpg`,
  alt: "The WorshipMetrics stage display editor showing a band confidence layout with chords above the lyrics and a note reading Capo 2",
  caption:
    "The band's confidence monitor is its own layout, not a mirror of the projector — chords above the words, the next line underneath, and the worship leader's note sitting where the drummer can read it.",
  width: 1920,
  height: 1115
};

export const overlays: AppScreenshot = {
  src: `${APP}/worship-metrics-overlays-editor.jpg`,
  alt: "The WorshipMetrics overlay editor showing a transparent canvas with a media overlay selected and a list of saved overlays",
  caption:
    "Overlays are built on a transparent canvas — the checkerboard is what the projector will see straight through. Name keys, announcements, and media sit in a list you can show or hide without touching the slide underneath.",
  width: 1920,
  height: 1017
};
