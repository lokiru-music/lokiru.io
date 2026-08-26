# lokiru.io

Marketing site for Lokiru — music software, plus the horn libraries recorded
with MSXII Sound.
Astro (static) deployed to GitHub Pages at the apex domain `lokiru.io`.

## Run it

```bash
npm run dev       # http://localhost:4321
npm run build     # -> dist/
npm run preview   # serve the built output
```

## Adding products — no code required

Everything on the page comes from Markdown in `src/content/`. Add a file, it
appears; delete a file, it disappears. Order is controlled by `order:`.

**Software** — `src/content/software/<slug>.md`

```markdown
---
title: Valvetrain
kind: Live performance suite   # what it is, in the reader's words
blurb: One sentence, said plainly.
modules: [Harmonizer, Looper, Plate reverb]   # optional; parts of a suite
formats: [macOS]                              # optional
price: Free                                   # optional — omit until priced
url: https://...                              # optional; without it the
status: soon                                  #   button points at contact
order: 3                                      # available | beta | soon
---
```

**A horn library** — `src/content/packs/<slug>.md`

```markdown
---
title: Vintage Soul Horns
url: https://...     # optional; defaults to drews.studio
order: 1
---
```

The seven packs link out to Drew's Studio as a group — neither that site nor
MSXII's storefront exposes per-pack product URLs. If you get direct links, drop
one into each file's `url:` and the list will use them.

## Design

The palette is taken from `design/lokiru-color-pallate.jpeg`, the LKRU tartan:
a scarlet field, a warm ladder of red-orange → amber → yellow, and one cold
cobalt thread cutting across it. Tokens live at the top of
`src/styles/global.css`; change them there and the whole site follows.

The page runs 01 Rack (software) then 02 Library (horn packs), ending on
Output (contact). Both stage names are real audio terms, not decoration.

Type is Archivo (using its width axis for display vs. body) with IBM Plex Mono
for every panel label and readout.

## Deploying

Pushing to `main` builds and publishes via `.github/workflows/deploy.yml`.

One-time setup on GitHub:

1. Create the repo and push `main`.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. **Settings → Pages → Custom domain**: enter `lokiru.io`, save.
4. Tick **Enforce HTTPS** once the certificate is issued (can take ~15 min).

`public/CNAME` already contains `lokiru.io`, so the custom domain survives
every deploy.

## DNS at your registrar

For the apex domain `lokiru.io`, four A records and four AAAA records:

| Type | Host | Value |
|------|------|-------|
| A    | @ | 185.199.108.153 |
| A    | @ | 185.199.109.153 |
| A    | @ | 185.199.110.153 |
| A    | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | `<your-github-username>.github.io.` |

Check propagation with `dig lokiru.io +short`.
