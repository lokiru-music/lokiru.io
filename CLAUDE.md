# lokiru.io

Astro static site for Lokiru (audio plugins/apps, sample packs, production),
deployed to GitHub Pages at the apex domain `lokiru.io`.

## Conventions

- **Content is data, not markup.** Products live in `src/content/packs/` and
  `src/content/plugins/` as Markdown with frontmatter; schemas are in
  `src/content.config.ts`. Never hardcode a product into a template.
- **Colour only via tokens.** Every colour is a custom property defined at the
  top of `src/styles/global.css`, sampled from the LKRU tartan in
  `design/lokiru-color-pallate.jpeg`. Do not introduce raw hex values in
  component styles.
- **Three type roles**: `.display` (Archivo, wide + heavy), body (Archivo
  normal width), and `--mono` (IBM Plex Mono) for every label, spec and
  readout. Labels use the `.label` class.
- The page reads as a signal chain — 01 Source / 02 Insert / 03 Master. Keep
  that structure if adding sections; it maps to the three business lines.
- `public/CNAME` must keep containing `lokiru.io` or the custom domain drops on
  the next deploy.

## Commands

`npm run dev` · `npm run build` · `npm run preview`

## Docs

https://docs.astro.build — see the guides for
[routing](https://docs.astro.build/en/guides/routing/),
[components](https://docs.astro.build/en/basics/astro-components/), and
[content collections](https://docs.astro.build/en/guides/content-collections/).
