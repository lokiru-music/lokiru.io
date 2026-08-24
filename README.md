# lokiru.io

Marketing site for Lokiru — audio plugins and apps, sample packs, and production.
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

**A sample pack** — `src/content/packs/<slug>.md`

```markdown
---
title: Tape Room
blurb: One sentence, said plainly.
contents: 24-bit WAV · 120 loops · 80 one-shots
bpm: 82–104          # optional
price: $39
url: https://...     # optional; falls back to the contact section
order: 1
---
```

**A plugin or app** — `src/content/plugins/<slug>.md`

```markdown
---
title: Ferrite
kind: Tape saturator
blurb: One sentence, said plainly.
formats: [VST3, AU, AAX]
price: $79
status: available    # available | beta | soon
url: https://...     # optional
order: 1
---
```

The three packs and three plugins currently in there are **placeholders** —
replace them with the real catalogue.

## Design

The palette is taken from `design/lokiru-color-pallate.jpeg`, the LKRU tartan:
a scarlet field, a warm ladder of red-orange → amber → yellow, and one cold
cobalt thread cutting across it. Tokens live at the top of
`src/styles/global.css`; change them there and the whole site follows.

The page is structured as a signal chain — 01 Source (packs), 02 Insert
(plugins), 03 Master (studio) — because the business actually is one.

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
