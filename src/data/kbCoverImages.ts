export const kbCoverImages = {
  cameras: '/images/kb-device-management.svg',
  switchers: '/images/kb-streaming.svg',
  encoders: '/images/kb-streaming.svg',
  mixers: '/images/kb-audio.svg',
  software: '/images/kb-streaming.svg',
  workflows: '/images/kb-operations.svg',
  comparisons: '/images/kb-streaming.svg',
  troubleshooting: '/images/kb-device-management.svg',
  budget: '/images/kb-operations.svg',
};

export function getKbCoverImage(primary: string | undefined, fallback: keyof typeof kbCoverImages) {
  return primary || kbCoverImages[fallback];
}
