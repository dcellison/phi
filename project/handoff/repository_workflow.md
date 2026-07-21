# Repository workflow and utilities

Phi is maintained as repository source, generated views, and machine checks. A replacement model should work from the source layer and use the generators rather than patching rendered output.

## Repository map

| Path | Role |
|---|---|
| `vocabulary/` | Canonical lexicon JSON, executable schema, and semantic-domain catalogue. |
| `canon.md` | Authority order and settled language decisions. |
| `documents/grammar/` | Canonical grammar inventories for particles, complementizers, numerals, prepositions, and conversation practice. |
| `documents/reference/` | Current phonology, phonetics, compounds, taught patterns, language overview, and model voice. |
| `documents/design/` | Design rationale, including modifier-first syntax and the measurement refusal. |
| `documents/evaluation/` | Capability, corpus, vocabulary, listening, peace-linguistic, and solo-evaluation records. |
| `documents/modules/` | Eight active vocabulary profiles and profile assessments. |
| `documents/validation/` | Committed baselines and migration evidence. |
| `manual/` | Complete teaching reference and generated Part VII views. |
| `primer/` | Graded reader and exercises. |
| `texts/` | Translation and transmutation shelf, catalogued for the site. |
| `pamphlets/` | Focused teaching companions, also catalogued. |
| `book/` | General-reader book treatment and drafted chapters. |
| `site/` | Maintained browser assets. No generated pages or data belong here. |
| `build/` | Ignored, disposable build products such as the site and SQLite lexicon. |
| `project/` | Operational protocol, roadmap, decisions, publishing strategy, releases, and this handoff. |
| `scripts/` | Current validation, generation, audit, build, lookup, catalogue, and writing-system utilities; [`scripts/README.md`](../../scripts/README.md) is their maintained index. |
| `archive/` | Historical material only. Never use it to establish current Phi. |

[`documents/README.md`](../../documents/README.md), [`project/README.md`](../README.md), [`vocabulary/README.md`](../../vocabulary/README.md), [`book/README.md`](../../book/README.md), [`texts/README.md`](../../texts/README.md), and [`site/README.md`](../../site/README.md) give the local maps for their areas.

## Reader-facing roles

Several surfaces cover neighbouring ground, but they do different work. Preserve that division when revising one of them.

| Surface | Contract |
|---|---|
| `kia.md` | The lightest invitation into Phi. It should feel hospitable and concrete without carrying the short road's exacting load. |
| `short_road.md` | The compact serious route through the language's commitments, costs, and main mechanics. It may ask more attention than `kia.md`. |
| `primer/` | A graded first course built around use and exercises. |
| `manual/` | The complete teaching and reference authority beneath canon and the lexicon. Generated Part VII views belong here. |
| `pamphlets/` | Focused companions for one practice or feature. They are neither a miscellaneous document drawer nor the literary shelf. |
| `texts/` | Phi literature, with every work labelled as translation or transmutation and every source witness preserved. |
| `book/` | Narrative nonfiction about Phi for a general reader, governed by `book/treatment.md` and its warmer chapter voice. |

## Worktree discipline

The repository may contain unrelated user changes. Never reset, revert, delete, stage, or reformat work you did not create. Read overlapping changes and work with them. Leave unrelated files out of the commit and PR.

The customary GitHub remote is `origin`, currently `git@github.com:dcellison/phi.git`. Use it for fetches, feature-branch pushes, PRs, and post-merge deletion. Other configured remotes are outside the routine PR workflow and should be left alone unless Daniel asks for them.

At the beginning of an effort:

```bash
git status --short --branch
git fetch origin --prune
git switch main
git pull --ff-only origin main
git status --short --branch
git switch -c descriptive_feature_branch
```

Do not commit to `main`. Use lowercase snake_case for self-generated filenames except the repository's established `README.md`, `CLAUDE.md`, and licence names.

Use `rg` and `rg --files` for searching. Search retired or replaced forms explicitly across active directories because the documentation validator cannot reliably identify every single italicized token.

## Python environment

CI uses Python 3.12 and installs the pinned dependency set:

```bash
python3 -m pip install --requirement project/requirements.txt
```

Local runs on the Mac mini may use a newer Python. A local pass does not replace GitHub's Python 3.12 check.

## Main validator

`scripts/validate_examples.py` is the primary integrity gate. Run it as a standalone command so its exit status remains visible.

```bash
python3 scripts/validate_examples.py
python3 scripts/validate_examples.py --show-warnings
python3 scripts/validate_examples.py --lexicon-only
python3 scripts/validate_examples.py --docs-only
python3 scripts/validate_examples.py --paths manual/part4_grammar texts/example.md
python3 scripts/validate_examples.py neighbors CANDIDATE
python3 scripts/validate_examples.py name PROPOSED_ONYM
```

The full run checks JSON Schema, canonical serialization, phonotactics, IPA, syllables, filenames, duplicate words, duplicate-gloss warnings, minimal pairs, documentation vocabulary, source citations, productive names, the three-syllable ceiling, compound registry integrity, generated references, and prose-coverage freshness.

For vocabulary and Phi prose, zero errors and zero warnings is the expected result. A duplicate-gloss warning may expose a genuine semantic collision even when schema validation succeeds.

## Focused test suites

```bash
python3 scripts/test_vocabulary_schema.py
python3 scripts/test_name_forms.py
python3 scripts/test_content_vocabulary_decisions.py
```

Invoke these files directly from the repository root. Running them through `python3 -m unittest scripts/...` can fail to resolve sibling imports even when the tests themselves are sound.

At the #418 checkpoint the suites contain 21 schema tests, 20 name tests, and 6 decision-register tests.

## Vocabulary coverage and decisions

`scripts/vocabulary_prose_coverage.py` writes the committed migration report:

```bash
python3 scripts/vocabulary_prose_coverage.py
```

`scripts/content_vocabulary_decisions.py` owns the readable decision view and validates reciprocal links, state requirements, implementation files, compounds, batch closure, and coverage headings:

```bash
python3 scripts/content_vocabulary_decisions.py --write
python3 scripts/content_vocabulary_decisions.py --check
```

Edit `project/content_vocabulary_decisions.json`, never the generated Markdown view. The coverage report and readable decision view are committed source-derived evidence, not disposable build products.

## Reference generation

`scripts/generate_reference.py` rebuilds:

- `manual/part7_reference/lexicon/alphabetical.md`;
- `manual/part7_reference/lexicon/by_domain.md`;
- `manual/part7_reference/lexicon/by_module.md`;
- `manual/part7_reference/lexicon/by_pos.md`;
- `manual/part7_reference/compounds.md`.

Run it after any vocabulary or compound-registry change:

```bash
python3 scripts/generate_reference.py
```

The canonical compound registry is `documents/reference/compounds.md`. `scripts/compound_registry.py` is a shared parser used by validation, reference generation, and site generation. It is a library rather than a separate maintenance command.

After staging intended source and generated changes, rerun the generator and use `git diff --exit-code` to verify that no generated drift remains unstaged.

## Site build and catalogues

`scripts/build_site.py` writes the complete deployable site under ignored `build/site/`:

```bash
python3 scripts/build_site.py
```

It renders the invitation, colophon, short road, primer, manual, book, texts, and pamphlets; generates lexicon and compound data; and checks that the text and pamphlet catalogues match their directories.

The maintained shelf order and display metadata live in `texts/catalogue.json` and `pamphlets/catalogue.json`. `scripts/content_catalogues.py` is the shared library that rejects duplicate, missing, uncatalogued, or malformed entries. Update the catalogue in the same PR as any shelf addition, removal, rename, or reorder.

The explorer has several settled interaction rules. `any module` includes base vocabulary and every module word; `base vocabulary` includes only entries whose `modules` array is absent or empty; a named module includes every word listing that module, including words shared with other modules. The `Phi word` search scope matches the entry form alone and never returns registered compounds. Compounds appear in `all fields` when no word facet is active, or under their own search scope. Pressing `/` focuses the search box. Preserve these distinctions when changing `site/app.js` or `site/explore.html`.

Do not leave a local server running by default. Daniel uses SSH to reach the Mac mini. A successful `build_site.py` run is enough for routine repository work. If a specific preview arrangement is requested, the disposable command is:

```bash
python3 -m http.server -d build/site
```

The public site deploys from `build/site/` on each push to `main` through `.github/workflows/pages.yml` and is available at [dcellison.github.io/phi](https://dcellison.github.io/phi/).

Routine content work does not require headless Chrome or a screenshot. Use browser automation only when a UI change genuinely needs visual or interaction verification.

## Lexicon lookup tool

`scripts/lexicon_tool_simple.py` creates ignored `build/lexicon.db` from the canonical JSON:

```bash
python3 scripts/lexicon_tool_simple.py init
python3 scripts/lexicon_tool_simple.py find WORD_OR_GLOSS
python3 scripts/lexicon_tool_simple.py view WORD
python3 scripts/lexicon_tool_simple.py list
python3 scripts/lexicon_tool_simple.py sync
```

The index is disposable. Rebuild it after vocabulary changes. `find` exits 1 when the term exists and 0 when it is free, because the command is also used as a coinage availability check.

## Phonetic-neighbour audit

`scripts/audit_phonetic_neighbors.py` measures phoneme-unit and feature-weighted similarity. It supplements the hard edit-distance rule and cannot make a rename decision.

```bash
python3 scripts/audit_phonetic_neighbors.py --candidate CANDIDATE
python3 scripts/audit_phonetic_neighbors.py --output /tmp/phonetic_neighbors_baseline.txt
diff -u documents/validation/phonetic_neighbors_baseline.txt /tmp/phonetic_neighbors_baseline.txt
python3 scripts/audit_phonetic_neighbors.py --kind function --prompts 40 --seed 202601
```

The committed baseline had 250 pairs after #418. Its attestation counts track the active corpus, so the generated file changes whenever cited examples change, even when no word form does; regenerate it unconditionally before any corpus pull request and commit the result when it differs. Distance scores are prompts for listening work, not proof that two words must change.

## Productive-name utility

`scripts/name_forms.py` implements the open proper-name class used by the validator and Tengwar renderer. Normal maintenance uses the validator wrapper:

```bash
python3 scripts/validate_examples.py name samira
```

A productive onym is a lowercase single token with two, three, or four legal Phi syllables. It is not vocabulary and receives no JSON entry, gloss, part of speech, or collision-baseline row. A legal four-syllable name needs no retirement check. A current lexicon match is allowed only when the entry is a content word.

## Tengwar utilities

`scripts/tengwar.py` is the renderer library used by the site build. It converts validated Romanized Phi lines into deterministic inline SVG using committed outlines in `writing_systems/tengwar_glyphs.json`. It is not a general foreign-text renderer, and source material remains outside the Phi SVG passage.

`scripts/extract_tengwar_glyphs.py` is a manual one-off extraction tool, still current but not part of ordinary builds. It requires `fontTools`, reads Tengwar Telcontar, preserves hand-tuned placement offsets, and rewrites the committed glyph outline JSON. Do not run it during normal vocabulary or site work. Its documented isolated environment is:

```bash
python3 -m venv /tmp/ftenv
/tmp/ftenv/bin/pip install fonttools
/tmp/ftenv/bin/python scripts/extract_tengwar_glyphs.py
```

Visual verification gaps remain parked in `project/deferred_questions.md`. Do not infer that default tehta placement has independent reference evidence merely because the renderer produces an SVG.

## Full local check sequence

Use this set for vocabulary batches and any broad documentation change:

```bash
python3 scripts/validate_examples.py --show-warnings
python3 scripts/test_vocabulary_schema.py
python3 scripts/content_vocabulary_decisions.py --check
python3 scripts/test_content_vocabulary_decisions.py
python3 scripts/test_name_forms.py
python3 scripts/audit_phonetic_neighbors.py --output /tmp/phonetic_neighbors_baseline.txt
diff -u documents/validation/phonetic_neighbors_baseline.txt /tmp/phonetic_neighbors_baseline.txt
python3 scripts/generate_reference.py
python3 scripts/build_site.py
git diff --check
```

Run `generate_reference.py` before its synchronization check, and remember that intended generated changes will appear in the working diff until staged. Once the task files are staged, rerun generators and confirm `git diff --exit-code` is clean. Then run:

```bash
git diff --cached --check
git diff --cached --stat
git diff --cached --name-only
```

Inspect the actual staged diff, not only the summary.

## GitHub validation

`.github/workflows/validate.yml` runs on every pull request and on pushes to `main`. It uses Python 3.12 and checks:

1. dependency installation;
2. the main validator;
3. schema tests;
4. decision-register validation and tests;
5. productive-name tests;
6. phonetic-neighbour baseline synchronization;
7. generated reference synchronization.

`.github/workflows/pages.yml` builds and deploys the site only from `main` or a manual workflow dispatch. A PR can pass validation without running the deployment workflow.

After opening a PR, watch the checks rather than assuming local success is enough:

```bash
gh pr checks PR_NUMBER --watch
```

If CI fails, inspect the failed job with `gh run view` or `gh pr checks`, reproduce the exact command locally, repair the branch, push, and wait for the new run. Do not close the PR or create a replacement unless the branch itself is wrong.

## Commit and PR publication

Completed repository work normally ends in a PR without another prompt. The sequence is:

1. Stage only task files with explicit paths.
2. Run `git diff --cached --check` and inspect the staged diff.
3. Commit with a concise imperative description and no AI attribution or `Co-Authored-By` trailer.
4. Push the feature branch with upstream tracking.
5. Write a detailed PR body to a temporary Markdown file.
6. Create the PR against `main` with `--body-file`.
7. Watch CI to completion.

Example commands:

```bash
git add path/to/task_file another/task_file
git diff --cached --check
git commit -m "Migrate ritual vocabulary prose"
git push -u origin feature_branch
gh pr create --base main --head feature_branch --title "Migrate ritual vocabulary prose" --body-file /tmp/phi_pr_body.md
gh pr checks PR_NUMBER --watch
```

Never pass the PR body inline. Shell interpretation has damaged formatting before; Daniel explicitly requires a body file.

A detailed PR body should state the semantic scope, words or documents changed, lexical decisions, generated artifacts, checks and counts, and one concrete Humanizer or voice issue found and corrected.

## Post-merge cleanup

When Daniel says a PR has merged, do the customary cleanup immediately:

```bash
gh pr view PR_NUMBER --json number,state,mergedAt,mergeCommit,headRefName,baseRefName,url
git fetch origin --prune
git switch main
git pull --ff-only origin main
git branch -d FEATURE_BRANCH
git push origin --delete FEATURE_BRANCH
git status --short --branch
git rev-parse main origin/main
```

Delete the remote branch only when it still exists. Confirm that the local and remote feature refs are absent and that `main` and `origin/main` point to the same merge commit. Leave unrelated work untouched.

## Citation audits for the book

Book citations require a separate factual audit after prose drafting. Use the web and prefer primary publications, publisher records, court opinions, official data, and the actual repository source witness. Do not rely on a search-result snippet or another model's bibliography.

For every external citation:

1. Confirm that the work exists.
2. Verify every author, title, year, venue, volume, issue, page range, DOI, and URL used in the chapter.
3. Open the source and check that it supports the exact nearby claim, including the direction and size of an effect.
4. Distinguish data, review, commentary, and anecdote.
5. Check for corrections, expressions of concern, retractions, failed replications, and later qualification.
6. Ensure quoted wording is exact and stays within copyright limits.
7. Replace or narrow a claim when the source does less work than the sentence asks of it.
8. Verify every local `Phi sources` path and the claim drawn from it.

A missing citation cannot be filled with a plausible substitute merely to satisfy a treatment receipt. If a source cannot be found or does not support the sentence, cut or rewrite the claim. Earlier audit reports are not comprehensively stored in the repository, so merged prose is not a substitute for renewed checking when a claim changes.

## Reporting to Daniel

Keep working updates short and factual. State what context is being read, what boundary or pattern has emerged, and what is being validated. Do not praise the work, manufacture urgency, or turn a status message into a tutorial.

The final message for a completed PR should include the PR link, the main result, the checks, the commit identifier when useful, and the concrete Humanizer correction. When work cannot be completed, say exactly what remains and why. Daniel does not see raw command output, so relay the result that matters.
