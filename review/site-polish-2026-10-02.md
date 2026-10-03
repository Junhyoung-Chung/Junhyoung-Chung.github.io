# Whole-site design refinement — 2026-10-02

User scope: retain existing content and refine Home, Research, Publications, Materials, document details, navigation and responsive layout. Add Research above Publications.

## Changes
- Shared page headers, typography, spacing, dividers, link/action treatments, and a more compact portrait/sidebar.
- Home interest columns and dated news rows; publication author/title/venue hierarchy.
- Semantic Research sections, responsive figures, intrinsic image dimensions and lazy decoding/loading.
- Two-column material gallery with aligned actions, a full-row single-document layout, and consistent document details.
- Mobile navigation links have 44px touch targets; narrow screens stack figures and documents.

## Verification
- Exact source visible-text comparison against 96bd534 passed for all changed content templates/pages.
- Independent review compared rendered text and link sequences on the four main routes and all seven material detail pages; no content loss or link changes.
- CV, material PDFs/metadata, Analytics configuration/includes and Google verification files remain unchanged.
- Development and production Jekyll builds passed. Materials metadata validation, Ruby/Python material tests, JS syntax check, Analytics gating test, preservation checks, internal-link/anchor/site checks and git diff whitespace checks passed.
- 15 generated HTML pages; production output 13.21 MiB, with no new dependencies or fonts and no eager PDF iframe.
- Browser: desktop Home/Research/Publications/Materials/detail inspected; 320px Home, Publications, Research, Materials and detail inspected without horizontal overflow. Menu order and 44px targets verified. PDF preview creates one iframe, Escape removes it and restores trigger focus. All five Research images load and retain aspect ratio. All five page types also fit a 768px viewport; 1024px detail inspected.
- Code reviewer found no regressions; Jekyll Sass compilation and HTML5 parsing supplied syntax checks (no LSP surface available).

Local screenshots are under ignored review/screenshots/. Public content is unchanged; DESIGN.md records the updated design contract.
