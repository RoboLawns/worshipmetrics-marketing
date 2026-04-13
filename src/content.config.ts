import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum([
      'device-management',
      'streaming',
      'video-clipping',
      'audio',
      'display',
      'operations',
    ]),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    featured: z.boolean().default(false),
    productCTA: z.boolean().default(true),
    coverImage: z.string().optional(),
    readingTime: z.number().optional(),
  }),
});

const cameras = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/cameras' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    brand: z.string(),
    modelId: z.string(),
    modelFullName: z.string(),
    articleType: z.enum([
      'setup-guide', 'troubleshooting', 'integration',
      'firmware-update', 'multi-unit', 'software-control',
      'comparison', 'overview', 'workflow',
    ]),
    category: z.enum(['device-setup', 'troubleshooting', 'how-to', 'streaming', 'audio', 'comparison']),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    priceRange: z.enum(['under-500', '500-1500', '1500-plus']).optional(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    relatedModels: z.array(z.string()).optional(),
    productCTA: z.boolean().default(true),
    readingTime: z.number().optional(),
  }),
});

const devices = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/devices' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    deviceCategory: z.enum(['switcher', 'encoder', 'mixer', 'capture-card', 'converter']),
    brand: z.string(),
    modelId: z.string(),
    modelFullName: z.string(),
    articleType: z.enum([
      'setup-guide', 'troubleshooting', 'integration',
      'firmware-update', 'multi-unit', 'software-control',
      'comparison', 'overview', 'workflow',
    ]),
    category: z.enum(['device-setup', 'troubleshooting', 'how-to', 'streaming', 'audio', 'comparison']),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    priceRange: z.enum(['under-500', '500-1500', '1500-plus']).optional(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    relatedModels: z.array(z.string()).optional(),
    productCTA: z.boolean().default(true),
    readingTime: z.number().optional(),
  }),
});

const software = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/software' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    app: z.enum(['obs', 'vmix', 'propresenter', 'easyworship', 'restream', 'castr', 'streamlabs', 'wirecast', 'atem-software']),
    articleType: z.enum(['setup-guide', 'feature-guide', 'integration', 'troubleshooting', 'comparison']),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    productCTA: z.boolean().default(true),
    readingTime: z.number().optional(),
  }),
});

const workflows = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/workflows' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    churchSize: z.enum(['small', 'medium', 'large', 'multi-campus']),
    budget: z.enum(['under-1k', '1k-5k', '5k-plus']),
    gearList: z.array(z.string()),
    tags: z.array(z.string()),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    productCTA: z.boolean().default(true),
  }),
});

const comparisons = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/comparisons' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    competitorA: z.string(),
    competitorB: z.string(),
    competitorC: z.string().optional(),
    verdict: z.string(),
    tags: z.array(z.string()),
    publishedAt: z.coerce.date(),
    productCTA: z.boolean().default(true),
  }),
});

const troubleshooting = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/troubleshooting' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    symptom: z.string(),
    affectedDevices: z.array(z.string()),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    productCTA: z.boolean().default(true),
  }),
});

const budget = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/budget' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    tier: z.enum(['under-500', 'under-1000', 'under-2500', 'under-5000', 'under-10000', 'upgrade-roadmap']),
    gearList: z.array(z.string()),
    tags: z.array(z.string()),
    publishedAt: z.coerce.date(),
    productCTA: z.boolean().default(true),
  }),
});

export const collections = { articles, cameras, devices, software, workflows, comparisons, troubleshooting, budget };
