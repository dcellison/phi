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

## Translation layer isolation

Before creating or revising a translation under `texts/`, read `.claude/skills/translate/SKILL.md`. Translation work has a strict one-way order:

1. In the source-to-Phi phase, work from the source, `canon.md`, the lexicon, and the grammar. Do not draft or consult a parenthetical English reading. When revising an existing work, use `scripts/translation_layers.py --phase source-to-phi` so its old glosses, parenthetical English, notes, and limits stay outside the working view.
2. Settle and validate the Phi, its unit boundaries, and its source citations before beginning the next phase. Treat the Phi sentence stream as frozen.
3. In the Phi-to-English phase, run `scripts/translation_layers.py` against the frozen source-to-Phi packet with `--phase phi-to-english --output-dir DIR --batch-size 8`. The output directory contains a manifest, one compact anonymous reference, and bounded packets whose stable unit numbers and digests trace back to the complete frozen stream. The packets omit the work's filename as well as the source, citations, prior English, notes, and limits. Give the reference once and the packets in order to one fresh, non-forked context that has never received the source or prior English; do not carry a source summary into it, and do not let that context inspect repository status, filenames, catalogues, task history, or the earlier conversation that contained the source. For each unit, require a clause analysis before the exact gloss and natural English. Treat the generated lexical gloss scaffold as a token check, not as a finished exact gloss. Produce the English from the frozen Phi alone, consulting only canon, the supplied lexical material, the grammar, and the required reader-facing voice references.
4. After the primary derivation, generate the independent audit queue with `--phase phi-to-english --audit-only --output-dir DIR`. Give it to a second fresh source-blind context. The queue contains structurally risky units plus a deterministic sample of the remainder; its output is internal, so it does not need the voice guide or Humanizer. Different English phrasing is harmless. A disagreement about participants, attachment, scope, complement boundaries, or antecedents must be resolved from Phi and canon. Audit source-to-Phi fidelity and Phi-to-English fidelity as separate directions in separate views. Never compare the source directly with the derived English or adjust either layer to resemble the other.

Any change to a frozen Phi sentence invalidates that sentence's gloss and derived English. Discard both and generate a fresh unit-scoped retry packet with `--units`; unaffected units stay settled. Record the manifest's full Phi digest, the audit selection, every resolved semantic disagreement, and compliance with this ordering in the pull-request body.

The readable procedure lives in `documents/reference/translation_process.md`. Before publishing a completed translation, update `project/translation_process_status.json`, regenerate its readable ledger, and run `python3 scripts/translation_process_status.py --check`. A translation is not certified merely because an older fidelity review exists.

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
