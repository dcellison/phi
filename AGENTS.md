# Repository Workflow

## Markdown prose formatting

- Keep each prose paragraph and each list-item paragraph on one physical line in Markdown source. Let the Markdown viewer wrap it for the display width.
- Preserve structural line breaks for headings, blank separators, tables, blockquotes, and fenced code or interlinear examples.
- Do not hard-wrap Markdown prose to a fixed column width.

## Post-merge PR cleanup

After a pull request has been confirmed as merged:

1. Verify the PR's merged state and merge commit.
2. Run `git fetch origin --prune`.
3. Switch to `main`.
4. Fast-forward with `git pull --ff-only origin main`.
5. Delete the merged local feature branch with `git branch -d <branch>`.
6. Delete the remote feature branch with `git push origin --delete <branch>` if it still exists.
7. Confirm that `main` tracks `origin/main` and that no stale feature-branch references remain.

Leave unrelated tracked changes and untracked files untouched throughout cleanup.
