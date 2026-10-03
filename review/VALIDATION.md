# Review evidence — 2026-10-02

## Isolation

- Worktree: `/Users/junhyoungchung/Documents/GitHub/Junhyoung-Chung.github.io-redesign`
- Branch: `redesign/just-the-docs`
- Original local `main` and remote `refs/heads/main` both remain at `f69ddd4b2d636ef892f324acacc82d282bda643f`.
- Original worktree is clean. No branch was pushed, no merge was made, and no Pages/account/domain/cloud settings were changed.
- Development preview: <http://127.0.0.1:4173/>. Restart with the README command if the local server has stopped.

## Automated checks passed

- Jekyll 4.4.1 + Just the Docs 0.12.0 development and production builds.
- 14 generated HTML pages; all local links and anchors resolve; no duplicate IDs.
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
- Both the thumbnail and Preview action open the actual external arXiv PDF in Chrome's viewer.
- Enter activates the preview. Close/Escape remove the iframe and return focus to the triggering link.
- PDF version is explicitly labeled, and the detail page links to the final PMLR publication.
- Existing horse-race article rendered 41 MathJax containers with no MathJax error nodes and no page-wide overflow at 320px.
- Screenshots are local review outputs under `review/screenshots/`, excluded from Git and the site build.

## Size evidence

- Full production output, including preserved archive images: approximately 13.22 MiB.
- New first-page thumbnail: 76,788 bytes.
- Optimized portrait: 78,198 bytes (original source retained).
- Material interaction script: 2,489 bytes; theme script: 5,075 bytes.
- External PDF original is not stored in the Git repository or deployment artifact.
- These are file sizes, not a claim of measured public-network loading speed.

## Remaining deployment boundaries

- GitHub Actions workflows have been prepared and parsed locally, not run on GitHub. The future deployment workflow only permits a manual approved run on `main`.
- GitHub Pages' current build configuration has not been changed; confirm/switch it at the approved cutover.
- No R2 account/bucket has been provisioned. Local and external public PDF URLs work now; connecting a future file host only changes material metadata.
- Mobile layout testing used a 320px desktop browser viewport. Actual mobile PDF viewers vary; the Open PDF link remains the fallback.
- Initial gallery contains only the already-public ICML paper. Additional private seminar/poster/note files have not been published.
