# Repository Workflow

## Markdown prose formatting

- Keep each prose paragraph and each list-item paragraph on one physical line in Markdown source. Let the Markdown viewer wrap it for the display width.
- Preserve structural line breaks for headings, blank separators, tables, blockquotes, and fenced code or interlinear examples.
- Do not hard-wrap Markdown prose to a fixed column width.

## Reader-facing Phi prose generation

Apply this section only to prose that Phi speakers or general readers are expected to read as project content. This includes the book, manual, primer, pamphlets, literary texts, Kia, the Short Road, public website copy, prose fields exposed through the lexicon, commit messages, pull-request titles and bodies, and public GitHub issue titles, bodies, and comments. Before creating or revising one of these artifacts, read `documents/reference/voice_for_models.md` in full and load the installed Humanizer skill. The voice guide sets Phi's register and mechanics. Humanizer then gives the generated passage a separate editing pass.

Do not load or apply the voice guide or Humanizer for disposable or internal operational writing. Handoff documents, plans, roadmaps, development logs, decision records, audit notes, validation reports, temporary reports, and internal boilerplate need direct, accurate prose instead. Apply the full voice process to one of these only when the user explicitly requests it or the text is being prepared for a reader-facing publication.

Use this order for every in-scope prose task:

1. Draft the complete text under `canon.md`, the applicable schema, and the artifact's factual requirements.
2. Apply the Humanizer skill as a separate revision pass across the whole draft. A vocabulary prose field gets the pass just as a chapter does. Reader-facing tables and other small content pieces are not exempt.
3. Audit the revision against `documents/reference/voice_for_models.md`, including its mechanical counts and batch-stamping check. Phi's project voice calls for human personality in reference prose as well as teaching prose; compactness is not an exemption.
4. Run every applicable validator and repair any factual, grammatical, structural, or formatting damage introduced during revision.

For an in-scope artifact, Humanizer reviews the whole draft, but accuracy does not move: Phi forms and lexicon glosses stay exact, while source quotations and previously validated examples remain as found. New English prose inside an example receives the pass before validation, and schema data stays intact. When reporting completed reader-facing prose work, name at least one concrete pattern found and corrected during the Humanizer or voice audit.

## Completed-work PR publication

After requested repository work is complete and every applicable check passes, use this sequence unless the user explicitly asks to keep the work local or pause for review:

1. Commit only the files that belong to the task on the current feature branch.
2. Push that feature branch to `origin`.
3. Create a detailed pull request against `main` with a clear summary and the checks that passed.

Treat commit, push, and pull-request creation as the customary finish to completed repository work. Leave unrelated tracked changes and untracked files out of the commit and pull request.

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
