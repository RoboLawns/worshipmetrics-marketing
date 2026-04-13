export const categories = [
  {
    slug: 'device-management',
    label: 'Device Management',
    description: 'Monitor, update, and manage AV hardware across your entire campus — cameras, encoders, mixers, and more.',
    icon: 'heroicons:server-stack',
    color: 'purple',
  },
  {
    slug: 'streaming',
    label: 'Streaming',
    description: 'Live streaming setup, multiplatform delivery, encoders, switchers, and NDI workflows.',
    icon: 'heroicons:signal',
    color: 'blue',
  },
  {
    slug: 'video-clipping',
    label: 'Video Clipping',
    description: 'Repurpose sermons into social content, build archives, add captions, and manage your video library.',
    icon: 'heroicons:scissors',
    color: 'green',
  },
  {
    slug: 'audio',
    label: 'Audio',
    description: 'Mixing consoles, gain staging, feedback elimination, and multi-track recording for worship.',
    icon: 'heroicons:speaker-wave',
    color: 'amber',
  },
  {
    slug: 'display',
    label: 'Display & Presentation',
    description: 'ProPresenter, LED walls, projectors, stage displays, and multi-screen setups.',
    icon: 'heroicons:tv',
    color: 'pink',
  },
  {
    slug: 'operations',
    label: 'Operations',
    description: 'Budgeting, volunteer training, maintenance schedules, runsheets, and team documentation.',
    icon: 'heroicons:clipboard-document-list',
    color: 'red',
  },
] as const;

export const categoryMap = Object.fromEntries(categories.map((category) => [category.slug, category]));
