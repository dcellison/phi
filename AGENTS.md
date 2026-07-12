# Repository Workflow

## Markdown prose formatting

- Keep each prose paragraph and each list-item paragraph on one physical line in Markdown source. Let the Markdown viewer wrap it for the display width.
- Preserve structural line breaks for headings, blank separators, tables, blockquotes, and fenced code or interlinear examples.
- Do not hard-wrap Markdown prose to a fixed column width.

## Phi prose generation

Before creating or revising any text for Phi, read `documents/voice_for_models.md` in full and load the installed Humanizer skill. The voice guide sets Phi's register and mechanics. Humanizer then gives every generated passage a separate editing pass.

Use this order for every prose task:

1. Draft the complete text under `canon.md`, the applicable schema, and the artifact's factual requirements.
2. Apply the Humanizer skill as a separate revision pass across the whole draft. A vocabulary field gets the pass just as a chapter does. So do tables, reports, boilerplate, and other small or technical pieces.
3. Audit the revision against `documents/voice_for_models.md`, including its mechanical counts and batch-stamping check. Phi's project voice calls for human personality in reference prose as well as teaching prose; compactness is not an exemption.
4. Run every applicable validator and repair any factual, grammatical, structural, or formatting damage introduced during revision.

Humanizer reviews the whole artifact, but accuracy does not move: Phi forms and lexicon glosses stay exact, while source quotations and previously validated examples remain as found. New English prose inside an example receives the pass before validation, and schema data stays intact. When reporting completed prose work, name at least one concrete pattern found and corrected during the Humanizer or voice audit.

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
