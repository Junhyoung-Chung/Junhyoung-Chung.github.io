# Isolated website redesign

This branch is a review candidate, not a production deployment.

- Branch: `redesign/just-the-docs`
- Worktree: `../Junhyoung-Chung.github.io-redesign`
- Original worktree: `../Junhyoung-Chung.github.io` (`main`)
- Original revision: `f69ddd4b2d636ef892f324acacc82d282bda643f`
- Do not merge/push to `main` or change GitHub Pages settings until Junhyoung gives final approval.

## Implementation sequence

1. Capture preservation checks for the CV, verification files, publication titles/order, and existing public routes.
2. Replace the TeXt theme scaffold only in this worktree with Just the Docs; preserve author content and old article URLs.
3. Add the Materials collection, local/external PDF URLs, compressed first-page thumbnails, and on-demand preview.
4. Carry forward GA4 with production-build and production-hostname gates.
5. Build development and production variants; check links, data, JS syntax, resource sizes, keyboard interactions, and desktop/mobile rendering.
6. Record review instructions and validation evidence. Leave production untouched.

## Production cutover — only after explicit final approval

1. Check that production `main` has not changed since the base revision; integrate any later content changes into this branch first.
2. Create a backup tag for the then-current production revision, without rewriting history.
3. Merge the approved branch. Configure GitHub Pages to use GitHub Actions if required by the existing Pages setup.
4. Run the manually gated deployment workflow on `main` with its required confirmation value.
5. Check the live home, publications, CV, material previews, Google verification URLs, and Analytics tag/hostname.

Rollback by reverting the migration merge and restoring the previous Pages build configuration if it changed. Do not force-push or delete the original repository.

## External files

The website supports root-relative local PDF paths and public HTTPS PDF URLs. No R2 account, domain, bucket, billing setting, or upload is created by this migration. Public cloud setup can be completed later while the site and its existing URL stay unchanged.
