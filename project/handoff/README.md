# Phi continuation handoff

This directory is the transfer package for continuing Phi after 17 July 2026. It was first assembled from the live repository after pull request #418 merged and is maintained as the work advances. It records the current position, the working method, the tools, and the maintainer's standing instructions that are easy to lose when a conversation ends.

This package is a map, not a new authority. When anything here disagrees with a live source, follow the authority order in [`canon.md`](../../canon.md), repair this package, and record a language decision where the disagreement is substantive.

## Read this first

Before changing anything, read these sources in order:

1. [`AGENTS.md`](../../AGENTS.md) for Markdown, Humanizer, publication, and post-merge rules.
2. [`canon.md`](../../canon.md) for the authority order and settled language decisions.
3. [`documents/reference/voice_for_models.md`](../../documents/reference/voice_for_models.md) in full, then the complete Humanizer skill installed for this model, before generating any Phi project prose. Locate the skill through the active installation's own skill registry rather than a remembered absolute path.
4. [`project/development_protocol.md`](../development_protocol.md) for word creation, source material, names, semantic choices, and validation.
5. [`project/roadmap.md`](../roadmap.md) for the execution sequence and evidence gates.
6. [`project/content_vocabulary_coverage.md`](../content_vocabulary_coverage.md) and the generated [`project/content_vocabulary_decisions.md`](../content_vocabulary_decisions.md) for the active vocabulary migration.
7. The four files beside this one for the exact handoff state and operating method.

Do not use `archive/` as current evidence. It preserves history, including approaches that were deliberately retired.

## Where the work stopped

SEM-09B and SEM-09C are complete. D045 through D052 migrated all eight module learning paths, and all 1,275 lexicon entries are target-shaped. There are no legacy, partial, or dual entries. SEM-09D is in progress: fifteen literary passes complete the shelf, the drafted Phi book is current through chapter 7, all seven manual parts have received teaching passes, all twenty-seven primer files are reviewed, and all nine pamphlets are current. Parts I through III repair the beginner's conceptual foundation, the philosophy and learning chapters, and pronunciation and writing-mode teaching. Part IV brings all fifty-three grammar lessons under the closed inventories and current lexical meanings. Part V restores the exact scopes and orders of coordination, discourse marking, clause frames, and relative clauses; D054 corrects purpose order, and D055 enforces modifier-first structure across the active corpus. Part VI repairs social-force claims, transmutation method, measured practice, completed-vocabulary use, and exact source handling. Part VII corrects the compact grammar and reading samples, reviews all eight module chapters, and reconciles the compound registry with the completed lexicon. The primer pass repairs pronunciation, modality, evidentiality, names, and missing word-table support while preserving the household course. The evidentiality pamphlet restores the four claimed-source particles; the three-slots pamphlet restores the closed particle inventory, exact rank order, and contextual limits of grammatical marking; the spoken-punctuation pamphlet keeps those lexical forms distinct from typographic marks and narrows dictation to what speech can recover; the complementizers pamphlet brings the three clause frames under main-clause tense, in-situ content questions, and the closed quotative frame-verb set, with the register rules applied in the same pass; the naming pamphlet, already current in doctrine, has its citations brought to precision and the same in-situ repair carried through its examples; the relative-clauses pamphlet loses its unlicensed `rena`-omission teaching and movement framing, gains the missing answer key, and joins the corpus translation convention; the source-material pamphlet, already current in doctrine, takes the four-syllable onym correction and the additive pass its spare register owed; the Tengwar pamphlet, written inside the current voice, needs only its rómen-and-órë account aligned to the positional decision and its examples brought under the closed Slot 0 combinations and the adjunct-order ruling, whose five-copy violation it exposed; the ternary-numerals pamphlet recovers the imagery an early doctrinal correction stripped while keeping every fact that correction fixed, repairs its false citations, gains the magnitude comparison its arithmetic owed, and again carries the honest about its catalogue entry promises. None of these teaching passes found a lexical gap. Part IV uses one labelled optional Work root with a base alternative, and Part VI does the same for Commons `kowela`; the general primer and eight of the nine pamphlets are module-free; the source-material pamphlet uses four labelled optional terms where its record and specification examples call for them, the module choice its own first chapter teaches. A warmth revision then re-tuned the whole manual's register without touching facts, Phi, glosses, or IPA. Part I set the method: ration the no-guarantee hedge, restore the original manuscripts' imagery on design-intent verbs rather than effect claims, and end each part on a threshold. Parts II through VII followed part by part, a dedicated additive pass returned salvaged imagery to the drier middle grammar chapters, and the voice guide's anti-pattern table now carries both governing rules: the waiver row, whose budget was subsequently ruled a ceiling rather than a quota so that the general charter lives once in Part I and each chapter keeps only boundaries that teach its own subject, and the effect-verb-under-an-image row, with a gallery pair showing that the cure for a false effect claim is changing the verb, not deleting the image. The three retrofitted pamphlets then received the same register pass: the evidentiality pamphlet gained its well image and four-syllable map, the three-slots pamphlet its room, deed, and thing, and the spoken-punctuation pamphlet its read-aloud-without-loss vista, with the per-particle hedge tails converted throughout.

The execution sequence is settled:

1. The literary shelf and Phi book are current through chapter 7.
2. Finish SEM-09D with the current documents; all nine pamphlets are current.
3. Return to the Phi book at chapter 8 after that sweep.

The immediate task is the current-documents sweep, running as directory batches: the grammar references and `documents/reference/` are done, and `documents/design/` with `documents/modules/` is next, then the evaluation corpus. The teaching review's resume point tracks the batches and holds the open `nai`-order fork awaiting a canon ruling.

## The maintainer's working contract

The following habits came from direct maintainer corrections. Treat them as standing instructions unless Daniel changes them.

- A question is not permission to edit. Answer questions and act on commands.
- Do not wait for outside proof before coining a useful word. Phi is a personal constructed language, not an RFC process or an auxiliary-language standards body.
- Do not turn Phi into an English relex. Test composition, semantic family, and actual conceptual need, then coin confidently when a root is the better Phi choice.
- Never let a noticed lexical gap vanish into conversation. Give it a decision ID before closing the batch, even when the decision is compositional, deferred, source-bound, or declined.
- Keep base vocabulary ordinary and broadly useful. Specialized words may belong to several modules; the `modules` field is an array for a reason.
- Modules add vocabulary only. Phi's grammar and particle system are complete, and no module may add syntax, parsing rules, or incompatible constructions.
- Peace linguistics is a design boundary, not decoration. Do not introduce generic conflict or direct combat vocabulary, weapon-centred framing, domination terms, or combat metaphors into Phi-authored material. Phi must still name danger, harm, coercion, injury, testimony, protection, accountability, redress, and repair.
- Exact clock units, physical units, money language, and industrial measurement are settled refusals. Read [`documents/design/psychological_violence_of_measurement.md`](../../documents/design/psychological_violence_of_measurement.md) before working near time, quantity, distance, weight, or exchange.
- Point out accidental English homonyms whenever they appear in a proposed Phi form or an existing form under review.
- Never use the discarded hyphenated adjective pattern recorded in [`language_and_voice.md`](language_and_voice.md). The maintainer has ruled it out without exception.
- `sound_symbolism` is optional embodied phonesthetics. It is not hidden morphology and should not become grandiose prose. `articulatory_notes` is the physical account of how the complete word is spoken.
- Apply Humanizer to every generated English string, including JSON fields, table cells, reports, and PR boilerplate. Then run the Phi voice audit separately and name at least one pattern corrected.
- Keep every Markdown prose paragraph and list-item paragraph on one physical line.
- Do not spend the remaining vocabulary-migration sequence on Canadian or British spelling checks. A later sweep can settle spelling without interrupting the prose-contract work.
- Book humour should borrow the kind, not the quantity, of Jerome K. Jerome's *Three Men in a Boat*: mild self-exposure, practical absurdity, and an occasional dry turn. It must not become a string of jokes.
- Do not describe Phi merely as a "slow language." Its unhurried quality is freedom from needless haste, and the centre is mindful and compassionate speech in the present utterance.
- Warmth is never rationed downward. On every teaching-corpus and retrofit pass, and on any commission naming an additive goal such as warmth, richness, or aspiration, the additive pass runs first, file by file, before the accuracy pass. A file already judged accurate is not thereby finished; dryness is its own finding, and the latent-image hunt runs on every file whether or not anything was ever stripped from it.
- No file closes at zero additions on the model's own judgment. When a file seems genuinely saturated, the pull request flags it as claimed saturated and Daniel confirms or sends it back; only he closes a file at zero. This rule exists because the model twice judged restraint correct on an additive commission and was wrong both times.
- Every pass's pull request body carries a per-file additions ledger: every file listed, what was added to it, zeros visible. Presenting a low-addition tally as restraint, taste, or virtue is the exact failure these three rules prevent.
- Do not start a local web server for routine handoff or vocabulary work. Daniel connects to the Mac mini over SSH and cannot use a server bound only to that machine. Build the site, but leave it stopped unless a specific remote-access arrangement is requested.
- Use one coherent pull request per completed effort. Pass every PR body with `--body-file`, never as an inline shell argument.
- When Daniel reports that a PR has merged, perform the full local and remote branch cleanup without waiting for a second request.

## Package contents

| File | What it contains |
|---|---|
| [`current_state.md`](current_state.md) | Counts, latest decisions, the active corpus task, book state, and parked work. |
| [`vocabulary_migration.md`](vocabulary_migration.md) | The full batch method, prose contract, decision register, coinage checks, regeneration, validation, and failure recovery. |
| [`repository_workflow.md`](repository_workflow.md) | Repository map, utility commands, generated files, CI, branch and PR procedure, cleanup, site builds, and citation audits. |
| [`language_and_voice.md`](language_and_voice.md) | Authority, governing purpose, canon constraints most likely to be violated, source and name practice, peace linguistics, writing voice, Humanizer, and book register. |

## Starting a continuation turn

A replacement model can use this opening checklist:

```text
1. Confirm the newest user request and whether it is a question or a command.
2. Read AGENTS.md, canon.md, the full voice guide, and the full Humanizer skill.
3. Run git status --short --branch and verify that main is clean and current.
4. Read the current coverage resume point and decision register counts.
5. If continuing SEM-09D, inspect each Phi passage in context, including its translation or transmutation method, dependencies, and validated examples, before replacing an older workaround.
6. Create a feature branch only after the scope is understood.
7. Carry the work through prose, Humanizer, voice audit, validation, commit, push, PR, and CI unless the user explicitly asks to pause.
```

The handoff is successful when the next model can begin from the live state without re-deriving Phi's boundaries, and without treating this snapshot as permission to ignore the repository that produced it.
