import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/** Software — the rack. */
const software = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/software' }),
  schema: z.object({
    title: z.string(),
    /** What it is, in the reader's words: "Browser metronome", "macOS app". */
    kind: z.string(),
    blurb: z.string(),
    /** Named parts of a suite, shown on the card. */
    modules: z.array(z.string()).default([]),
    formats: z.array(z.string()).default([]),
    /** Omit while a product has no price yet. */
    price: z.string().optional(),
    url: z.string().url().optional(),
    status: z.enum(['available', 'beta', 'soon']).default('available'),
    order: z.number().default(0),
  }),
});

/** Sample packs — the library. Collaborations, sold elsewhere. */
const packs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/packs' }),
  schema: z.object({
    title: z.string(),
    url: z.string().url().optional(),
    order: z.number().default(0),
  }),
});

export const collections = { software, packs };
