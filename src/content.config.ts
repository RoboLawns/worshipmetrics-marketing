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

export const collections = { articles };
