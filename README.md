# Junhyoung Chung's academic website

A small Jekyll site using Just the Docs 0.12.0, with a first-page material gallery and on-demand PDF previews.

**This branch is an isolated review candidate. Production replacement requires Junhyoung's final approval.** See [MIGRATION.md](MIGRATION.md) for the cutover and rollback procedure, and [DESIGN.md](DESIGN.md) for the approved design.

## Local preview

Use Ruby 3.2.10 (the repository includes `.ruby-version`). On this Mac, prefix Ruby/Bundler commands with `rbenv exec` if needed.

```sh
bundle _2.4.19_ config set --local path vendor/bundle
bundle _2.4.19_ install
bundle _2.4.19_ exec jekyll serve --host 127.0.0.1 --port 4173
```

Open <http://127.0.0.1:4173/>. Preview builds do not load Google Analytics. A production build also refuses to load Analytics on any hostname except `junhyoung-chung.github.io`.

## Add a material

Each Markdown file in `_materials/` creates one gallery entry and detail page. Only the thumbnail loads when browsing the gallery; the PDF is embedded after clicking Preview or the thumbnail. With JavaScript disabled, those links open the original PDF.

To create the metadata and first-page thumbnail from a local PDF:

```sh
ruby scripts/add_material.rb \
  --file '/absolute/path/to/seminar.pdf' \
  --slug 'seminar-2026' \
  --title 'Seminar title' \
  --kind 'Seminar slides' \
  --year 2026 \
  --venue 'Seminar name'
```

The command requires Poppler's `pdftoppm` (already available on the development Mac; install `poppler-utils` on Ubuntu). It creates a 480px first-page JPEG, an `_materials/*.md` entry, and a copy of the PDF under `assets/materials/`. Existing files are never overwritten. Local PDFs above 20 MiB must use an external URL.

Kinds: `Seminar slides`, `Poster`, `Lecture notes`, `Research paper`.

### Keep the original PDF outside Git

Add `--pdf-url 'https://files.your-domain.example/seminar.pdf'` to the same command. The local PDF is used only to generate the thumbnail; **no PDF is copied into the repository**. The command does not upload files or create a cloud account.

You can also edit a record directly:

```yaml
---
title: Seminar title
kind: Seminar slides
year: 2026
venue: Seminar name
pdf_url: https://files.your-domain.example/seminar.pdf
thumbnail: /assets/thumbnails/seminar-2026.jpg
---

Optional description, authors, or context.
```

For slides/posters, `thumbnail_width` and `thumbnail_height` can optionally record the image dimensions. Cards always contain the complete thumbnail rather than cropping it. Optional `source_url` and `source_label` provide a publication link; `preview_caption` can name a particular document version.

Use a stable public HTTPS URL. The file server should return `Content-Type: application/pdf`, allow embedding from the homepage, and preferably support byte-range requests. Avoid expiring links. Browser PDF support varies, especially on phones; the original-file link remains available beside every preview. Cross-origin downloads use the PDF viewer/new tab rather than promising that the HTML `download` attribute will force a download.

The initial research-paper entry uses the arXiv PDF, explicitly labeled as that version, with a separate final PMLR publication link. PMLR's raw GitHub PDF currently sends `X-Frame-Options: deny` and cannot be embedded directly.

### Optional R2 setup later

No R2 account, bucket, domain, billing subscription, or upload has been created. When ready:

1. Create a bucket for approved public documents, and connect an owned domain such as `files.example.org`.
2. Upload the PDF with `Content-Type: application/pdf` and an inline content disposition. Publish only files intended to be public.
3. Check the file URL without login, then put that URL in `pdf_url`. The homepage's `github.io` address can stay unchanged.
4. Keep R2 access keys in a local credential store or CI secrets. They are not needed by the website or the browser.

Native cross-origin PDF frames do not need a JavaScript fetch. If a future PDF.js viewer is introduced, configure the file host's CORS policy for the website origin.

Official references: [R2 public buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/), [R2 pricing](https://developers.cloudflare.com/r2/pricing/).

## Existing content and tracking

- The CV remains at `/assets/CV.pdf`; update `cv_updated` when replacing it.
- Publications retain **Journal Papers → Conference Paper**, including the intentional singular.
- `/home/` forwards to the new homepage. `/research/`, `/archive/`, and four dated article URLs remain available.
- Drafts are retained as source and never published by the normal build.
- `google5272b05d391d3ed0.html` and `googlee35a5a5e4a9bd991.html` remain unchanged for Google site verification.
- The original GA4 ID, `G-CH97FJJG6N`, is configured in `_config.yml`. Its loader is in `_includes/analytics.html`; do not set `ga_tracking` as well, which would duplicate tracking.
- MathJax loads only on archived articles. Search, comments, external fonts, and the old TeXt frontend are not loaded on the main pages.

## Validation

```sh
ruby scripts/validate_materials.rb
ruby tests/materials_test.rb
python3 tests/materials_cli_test.py
node --check assets/js/materials.js
bundle _2.4.19_ exec jekyll build
python3 scripts/check_preservation.py --site _site --compare-base
python3 scripts/check_site.py _site
JEKYLL_ENV=production bundle _2.4.19_ exec jekyll build --destination _site-production
python3 scripts/check_site.py _site-production --production
node tests/analytics.test.cjs
```

`--compare-base` is specifically for this migration review and checks that the CV matches the original revision byte for byte. Omit it for future intentional CV updates. Both Google verification files always retain their original bytes.

The check workflow builds and validates without publishing. The production workflow has no push trigger and only runs on `main` with the explicit `publish-just-the-docs` confirmation input. GitHub Pages must be configured to use Actions at the approved cutover; no Pages settings are changed by building locally.
