# Review evidence — 2026-10-02

## Isolation

- Worktree: `/Users/junhyoungchung/Documents/GitHub/Junhyoung-Chung.github.io-redesign`
- Branch: `redesign/just-the-docs`
- Original local `main` and remote `refs/heads/main` both remain at `f69ddd4b2d636ef892f324acacc82d282bda643f`.
- Original worktree is clean. No branch was pushed, no merge was made, and no Pages/account/domain/cloud settings were changed.
- Development preview: <http://127.0.0.1:4173/>. Restart with the README command if the local server has stopped.

## Automated checks passed

- Jekyll 4.4.1 + Just the Docs 0.12.0 development and production builds.
- 20 generated HTML pages; all local links and anchors resolve; no duplicate IDs.
- CV and both Google verification files match the original revision byte for byte.
- Five publication titles and Journal Papers → Conference Paper order preserved.
- Home alias, research, archive, and four dated article routes exist.
- Production GA4 uses the original `G-CH97FJJG6N` ID once. Executing its generated loader against local, preview, and lookalike hostnames produces no tracking requests; the exact production hostname loads the one configured tag.
- Development HTML contains no Analytics loader or measurement ID.
- No PDF iframe exists before selection. Internal authoring/review files and drafts are excluded from the build.
- Material records validate local/external URLs and reject unsafe schemes, credentials, traversal, missing files, incorrect kinds/years, and non-PDF local documents.
- Authoring command tested in temporary sites: generated first-page thumbnails and metadata, copied a local PDF, omitted a PDF when an external URL was supplied, and rejected duplicate names without overwriting.
- Empty collection tested in a temporary build: honest empty state, no fabricated cards or eager viewer.
- Ruby and JavaScript syntax checks, Python compilation, workflow YAML parsing, and `git diff --check` passed.

## Browser checks passed

- Desktop at 1280px and mobile layout at 320px.
- Mobile menu opens and reaches Materials; no horizontal overflow on Home, Publications, and Materials.
- Both the thumbnail and Preview action open the local ICML poster in Chrome's viewer; all seven material selections point to the correct local PDF and retain only one iframe.
- Enter activates the preview. Close/Escape remove the iframe and return focus to the triggering link.
- The ICML poster detail page links to the final PMLR publication. The selected preview appears within its year section.
- Five seminar dates appear in descending order: 2025-08-19, 2025-07-10, 2025-01-09, 2024-07-25, 2024-06-26. Dates come from title slides, including the January 2025 presentation stored in the 2024 winter folder.
- Portrait appears fully above the sidebar name without overlapping navigation; mobile retains a smaller portrait above the name. First-year introduction and LinkedIn links are present.
- At 320px, Home and the seven-card Materials gallery have no horizontal overflow. Enter opens the SOP preview with a 290px frame; Escape closes it.
- Existing horse-race article rendered 41 MathJax containers with no MathJax error nodes and no page-wide overflow at 320px.
- Screenshots are local review outputs under `review/screenshots/`, excluded from Git and the site build.

## Size evidence

- Full production output, including preserved archive images: approximately 20.84 MiB.
- Seven first-page thumbnails: approximately 223.2 KiB combined.
- Optimized portrait: 78,198 bytes (original source retained).
- Material interaction script: approximately 2.6 KiB; theme script: 5,075 bytes.
- Seven local PDFs: approximately 7.40 MiB combined. Only the sanitized SOP is included. External HTTPS PDFs remain supported for future larger files.
- These are file sizes, not a claim of measured public-network loading speed.

## Remaining deployment boundaries

- GitHub Actions workflows have been prepared and parsed locally, not run on GitHub. The future deployment workflow only permits a manual approved run on `main`.
- GitHub Pages' current build configuration has not been changed; confirm/switch it at the approved cutover.
- No R2 account/bucket has been provisioned. Local and external public PDF URLs work now; connecting a future file host only changes material metadata.
- Mobile layout testing used a 320px desktop browser viewport. Actual mobile PDF viewers vary; the Open PDF link remains the fallback.
- Gallery contains the user-selected ICML poster, five seminar decks, and a sanitized SOP. These additions are local only; nothing has been pushed or publicly deployed.
- Writing archive and drafts remain preserved pending the owner's decision; they are not in primary navigation.

## SOP verification

- Compiled a separate copy after replacing the three faculty names in the program-fit paragraph with `OOO`; no overlay-based masking.
- Extracted output contains exactly three `OOO` replacements and none of the three original target names. Text matches the original after those replacements and line-wrap normalization.
- Rendered and visually inspected all three output pages. Original PDF SHA-256 is unchanged.
- Private TeX, bibliography, original-name checklist, logs, and page renders remain under ignored `review/private/`; the entire review directory is excluded from Jekyll.
