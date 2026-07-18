# Phi continuation handoff

This directory is the transfer package for continuing Phi after 17 July 2026. It was first assembled from the live repository after pull request #418 merged and is maintained as the work advances. It records the current position, the working method, the tools, and the maintainer's standing instructions that are easy to lose when a conversation ends.

This package is a map, not a new authority. When anything here disagrees with a live source, follow the authority order in [`canon.md`](../../canon.md), repair this package, and record a language decision where the disagreement is substantive.

## Read this first

Before changing anything, read these sources in order:

1. [`AGENTS.md`](../../AGENTS.md) for Markdown, Humanizer, publication, and post-merge rules.
2. [`canon.md`](../../canon.md) for the authority order and settled language decisions.
3. [`documents/reference/voice_for_models.md`](../../documents/reference/voice_for_models.md) in full, then the complete Humanizer skill installed for this model, before generating any Phi project prose. On the current Codex installation its source is `/Users/daniel/.codex/skills/humanizer/SKILL.md`; use the active skill locator rather than assuming that absolute path on another host.
4. [`project/development_protocol.md`](../development_protocol.md) for word creation, source material, names, semantic choices, and validation.
5. [`project/roadmap.md`](../roadmap.md) for the execution sequence and evidence gates.
6. [`project/content_vocabulary_coverage.md`](../content_vocabulary_coverage.md) and the generated [`project/content_vocabulary_decisions.md`](../content_vocabulary_decisions.md) for the active vocabulary migration.
7. The four files beside this one for the exact handoff state and operating method.

Do not use `archive/` as current evidence. It preserves history, including approaches that were deliberately retired.

## Where the work stopped

SEM-09B and SEM-09C are complete. D045 through D052 migrated all eight module learning paths, and all 1,275 lexicon entries are target-shaped. There are no legacy, partial, or dual entries. SEM-09D is in progress: its first literary pass preserved both Schleicher renderings and prompted D053's animal-range repair; its second replaced three old detours in both *The North Wind and the Sun* renderings with base `mesatu`, `komeri`, and `phesari`; its third brought base `sheraki`, `tupeka`, `rinu`, and `huwa` into the Metta Sutta.

The execution order is fixed in the roadmap:

1. Continue the text shelf one work at a time, with UDHR Article 1 next.
2. Sweep the remaining active Phi passages for old workarounds that the completed vocabulary can improve.
3. Return to the Phi book with chapter 7, "A literature before a community."

The immediate task is the next SEM-09D literary pass, UDHR Article 1, described in [`current_state.md`](current_state.md). Inspect both of its renderings, source, notes, comparison, and every dependency against the completed base and module vocabulary. Change a Phi passage only when current vocabulary makes it more faithful or natural. A transparent composition is not obsolete merely because a direct word now exists.

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
- Do not start a local web server for routine handoff or vocabulary work. Daniel connects to the Mac mini over SSH and cannot use a server bound only to that machine. Build the site, but leave it stopped unless a specific remote-access arrangement is requested.
- Use one coherent pull request per completed effort. Pass every PR body with `--body-file`, never as an inline shell argument.
- When Daniel reports that a PR has merged, perform the full local and remote branch cleanup without waiting for a second request.

## Package contents

| File | What it contains |
|---|---|
| [`current_state.md`](current_state.md) | Counts, latest decisions, the active module-migration task, corpus state, book state, and parked work. |
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
