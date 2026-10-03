# Validation — approved production cutover, 2026-10-02

## Approval and recovery

- Junhyoung approved removing the writing archive and replacing production with the redesign.
- Original revision: `f69ddd4b2d636ef892f324acacc82d282bda643f`; recoverable via `pre-redesign-2026-10-02` and Git history.
- Implementation remains isolated in `redesign/just-the-docs` until the production merge.
- Deployment results and observed Pages settings will be recorded separately after cutover.

## Automated checks passed

- Development and production Jekyll builds: 15 HTML pages, all local links and fragments resolve, no duplicate IDs.
- CV and both Google verification files match the original revision byte for byte.
- Five publication titles and Journal Papers → Conference Paper order preserved.
- Home alias, research, publications, materials, and 404 routes exist.
- Archive, posts, drafts, dated article outputs, and MathJax are absent. Internal authoring and private SOP verification files are excluded.
- Seven material records validate; unsafe URLs and invalid/mismatched presentation dates are rejected.
- CLI authoring tests verify local/external PDFs, thumbnails, duplicate protection, and date validation.
- GA4 loader uses original ID `G-CH97FJJG6N` exactly once on the exact production hostname. Local, preview, and lookalike hostnames do not load Analytics. Development HTML has no Analytics loader.
- No PDF iframe exists before selection. JavaScript syntax and Git whitespace checks pass.

## Browser verification

- Sidebar portrait above the name without overlapping navigation; first-year introduction and LinkedIn links present.
- Desktop and 320px mobile layout checked; no horizontal overflow.
- All seven material selections create exactly one iframe pointing to the expected PDF; Close/Escape removes it and restores focus.
- ICML poster rendered visibly in Chrome. Native browser PDF support can vary on actual phones; Open PDF remains available.
- Seminar dates descend: 2025-08-19, 2025-07-10, 2025-01-09, 2024-07-25, 2024-06-26. These are title-slide dates, including January 2025 in the 2024 winter folder.
- Screenshots are local review artifacts under ignored `review/screenshots/`.

## SOP verification

- Recompiled a separate source copy after replacing the three program-fit faculty names with OOO; no overlay masking.
- Extracted output contains three OOO replacements and none of the three original target names. Remaining text matches the original after line-wrap normalization.
- All three rendered pages visually inspected; original PDF checksum unchanged.
- Original sources and the name checklist remain outside public assets, under ignored private working files where needed.

## Size

- Full production output after removing writing assets: approximately 13.18 MiB.
- Seven material PDFs: 7.40 MiB; seven thumbnails: 223.2 KiB combined.
- Optimized portrait: 78,198 bytes. Original portrait sources retained.
- PDF bytes load only after selection. File sizes are not public-network speed measurements.

## Remaining deployment verification

- Repository source/settings, successful GitHub Actions deployment, live routes/PDFs, archive 404, and GA tag/event delivery must be verified after publishing.
- Public tag/event delivery does not establish account-side Realtime ingestion without access to the GA4 property.
- No cloud storage account, bucket, domain, or billing setting has been created.
