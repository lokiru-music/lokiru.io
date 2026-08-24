import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/** Sample packs — the source stage. */
const packs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/packs' }),
  schema: z.object({
    title: z.string(),
    blurb: z.string(),
    /** e.g. "24-bit WAV · 140 loops · 90 one-shots" */
    contents: z.string(),
    bpm: z.string().optional(),
    price: z.string(),
    url: z.string().url().optional(),
    order: z.number().default(0),
  }),
});

/** Plugins and apps — the insert stage. */
const plugins = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/plugins' }),
  schema: z.object({
    title: z.string(),
    kind: z.string(),          // "Saturator", "Granular delay", "iOS app"
    blurb: z.string(),
    formats: z.array(z.string()).default([]),
    price: z.string(),
    url: z.string().url().optional(),
    status: z.enum(['available', 'beta', 'soon']).default('available'),
    order: z.number().default(0),
  }),
});

export const collections = { packs, plugins };
