# Website cutover

Junhyoung approved replacing the production website and removing the writing archive on October 2, 2026.

- Implementation branch: `redesign/just-the-docs`
- Isolated worktree: `../Junhyoung-Chung.github.io-redesign`
- Production source worktree: `../Junhyoung-Chung.github.io` (`main`)
- Previous production revision: `f69ddd4b2d636ef892f324acacc82d282bda643f`
- Backup tag: `pre-redesign-2026-10-02`

## Routine deployment

Automatic deployment on pushes to `main` was requested by Junhyoung on October 2, 2026.

1. Commit and push changes to `main`, or merge a pull request into `main`.
2. **Actions → Publish website** automatically builds and validates the site, then deploys the validated artifact to GitHub Pages. A failed build or validation prevents deployment.
3. Check the workflow result and the live page. GitHub Pages or browser caches may briefly show an older page after a successful deployment.

The workflow also supports **Run workflow → main** for manual retries, with no confirmation input. Other branches and pull requests do not publish; routine local builds and checks never publish.

## Initial cutover (completed)

1. Confirm production has no new commits or uncommitted changes; retain the previous revision under the backup tag.
2. Run material, content-preservation, link, Analytics, and production-build checks.
3. Merge the approved redesign into `main` and push the branch and backup tag without rewriting history.
4. Set GitHub Pages Source to GitHub Actions. Run `pages.yml` on `main` with confirmation `publish-just-the-docs`.
5. Verify the completed deployment and live Home, Publications, Materials, CV, Google verification files, PDF previews, and GA4 tag requests.

The confirmation input above was used for the initial cutover and has been removed from routine deployment.

## Removed writing

The writing archive, posts, drafts, article layout, MathJax, and unused writing images were intentionally removed. Old article URLs return the site's 404 page. Research pages, publications, CV, material PDFs, portrait, and both Google verification files remain.

## Rollback

Revert the migration merge (with `git revert -m 1 <merge-commit>`) rather than force-pushing. The backup tag retains the former source. To return to the old GitHub Pages builder, restore its prior branch-based publishing source (`main`, repository root) as well. Record the actual prior Pages source during cutover before relying on that default.

## External files

The website supports local PDFs and public HTTPS PDF URLs. No new storage account, bucket, domain, billing setting, or upload is needed. Large future materials can move to an external file host by updating their metadata.
