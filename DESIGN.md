# Design

## Source of truth
- Status: Active for the isolated redesign; production replacement awaits Junhyoung's final approval.
- Last refreshed: 2026-10-02
- Primary product surfaces: Home, Publications, Materials, CV; existing research and article URLs remain available.
- Evidence reviewed: existing home/index.html, publications/index.html, research/index.html, _posts, assets/CV.pdf, Analytics configuration, Google verification files, and the approved Just the Docs thumbnail-gallery proposal.
- Base revision: f69ddd4b2d636ef892f324acacc82d282bda643f.

## Brand
- Personality: quiet, precise, approachable academic homepage.
- Trust signals: real biography, unchanged publication metadata, original PDF links, dates, affiliation.
- Avoid: oversized hero banners, gradients, decorative dashboards, invented materials, blog-first navigation.

## Product goals
- Goals: quickly understand Junhyoung's research and find/read research materials without mandatory downloads.
- Non-goals: a new posting platform, accounts, an upload CMS, automatic public cloud provisioning.
- Success signals: small initial page load, working PDF previews and fallback links, complete publication/CV preservation, no production changes before approval.

## Personas and jobs
- Primary personas: researchers, prospective collaborators, seminar attendees, students.
- User jobs: read background/publications; visually locate materials; open, preview, or download PDFs.
- Key contexts: desktop research browsing and mobile links shared after talks.

## Information architecture
- Primary navigation: Home / Publications / Materials / CV.
- Core routes: /, /home/, /publications/, /materials/, /assets/CV.pdf.
- Content hierarchy: Home contains introduction, research interests and news; publications retain Journal Papers then Conference Paper (intentional singular); materials use first-page thumbnails.
- Compatibility: /research/, /archive/, and the four existing dated article URLs remain available without occupying primary navigation.

## Design principles
- Let content, whitespace, and typography establish hierarchy.
- Reuse Just the Docs' responsive shell; extend only the material gallery and personal content.
- Tradeoffs: native PDF embedding is lighter than shipping a PDF renderer; always provide an original-file fallback.

## Visual language
- Color: white canvas, pale gray sidebar, dark neutral text, muted plum links and selected states.
- Typography: system sans serif; no network font dependency.
- Spacing/layout rhythm: generous section spacing, readable line length, compact navigation.
- Shape/radius/elevation: thin dividers, small radii, no decorative shadows.
- Motion: no decorative animation; honor reduced motion when scrolling to previews.
- Imagery/iconography: portrait above the name in the sidebar (smaller above the name in the mobile header); real PDF first-page thumbnails, proportionally contained.

## Components
- Existing components to reuse: Just the Docs layout, navigation, mobile menu, accessible skip link.
- New/changed components: sidebar portrait, first-year Ph.D. introduction with LinkedIn, publication list, material thumbnail gallery grouped by year, inline PDF preview with close/open/download actions.
- Variants and states: local PDF or external HTTPS PDF URL; empty gallery; selected card; open/closed preview.
- Token/component ownership: _sass/color_schemes/academic.scss and _sass/custom/custom.scss; materials templates and a small deferred script.

## Accessibility
- Target standard: WCAG 2.2 AA-oriented implementation, with keyboard and narrow-screen checks.
- Keyboard/focus behavior: native links/buttons; visible focus; close restores the selected preview button; Escape closes the preview.
- Contrast/readability: dark text and plum links on light backgrounds; no essential text inside thumbnail images.
- Screen-reader semantics: descriptive PDF iframe title, live selection announcement, meaningful page headings.
- Reduced motion and sensory considerations: static initial render and reduced-motion-aware scrolling.

## Responsive behavior
- Supported breakpoints/devices: 320px mobile through desktop.
- Layout adaptations: Just the Docs mobile menu; three/two/one gallery columns; viewer and actions remain within viewport.
- Touch/hover differences: preview is explicitly activated; no hover-only content.

## Interaction states
- Loading: PDF loads only after selection; fallback links are always present.
- Empty: short honest message; no fabricated content.
- Error: original PDF link remains available even when a browser cannot embed a PDF.
- Success: selected material name shown above the viewer.
- Disabled: no inert download controls.
- Offline/slow network: metadata and thumbnails render independently of the document viewer.

## Content voice
- Tone: clear academic English; author's Korean name preserved.
- Terminology: Materials, Seminar slides, Posters, Lecture notes, Research papers.
- Microcopy rules: describe the action, avoid implementation details in public pages.

## Implementation constraints
- Framework/styling system: Jekyll + pinned Just the Docs theme, no frontend framework.
- Design-token constraints: use theme extension hooks rather than copying the entire theme.
- Performance constraints: local system fonts, disabled search until needed, no eagerly embedded PDFs, compressed first-page thumbnails, no R2 credentials in the browser or repository.
- Compatibility constraints: original GA4 ID and Google Search Console verification files preserved; GA loads only for production builds on the real production hostname.
- Test/screenshot expectations: check preserved URLs/files, internal links, development/production Analytics gates, hostile material URLs, empty/nonempty gallery, keyboard interactions, desktop and 320px mobile layouts.
- Deployment boundary: only isolated local worktree/branch work is authorized now. No main merge/push, Pages settings changes, public preview, or new cloud account/bucket until authorized.

## Open questions
- [x] Initial materials: ICML poster, five seminar presentations ordered by their title-slide dates, and a separate SOP copy with the three program-fit faculty names replaced by OOO. Original source files remain untouched.
- [ ] Writing archive: retained outside primary navigation to preserve existing links; owner is considering removing posts and drafts. No deletion performed in this revision.
- [ ] Future external storage provider/domain: use explicit HTTPS file URLs now; R2 provisioning and billing are separate from this local implementation.
