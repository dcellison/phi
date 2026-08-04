# Phi continuation handoff

This directory is the transfer package for continuing Phi after 17 July 2026. It was first assembled from the live repository after pull request #418 merged and is current through pull request #702 and decision D113 on 4 August 2026. It records the current position, the working method, the tools, and the maintainer's standing instructions that are easy to lose when a conversation ends.

This package is a map, not a new authority. When anything here disagrees with a live source, follow the authority order in [`canon.md`](../../canon.md), repair this package, and record a language decision where the disagreement is substantive.

## Read this first

Before changing anything, read these sources in order:

1. [`AGENTS.md`](../../AGENTS.md) for Markdown, Humanizer, publication, and post-merge rules.
2. [`canon.md`](../../canon.md) for the authority order and settled language decisions.
3. [`documents/reference/voice_for_models.md`](../../documents/reference/voice_for_models.md) in full, then the complete Humanizer skill installed for this model, before generating reader-facing Phi project prose. Locate the skill through the active installation's own skill registry rather than a remembered absolute path.
4. [`project/development_protocol.md`](../development_protocol.md) for word creation, source material, names, semantic choices, and validation.
5. [`project/roadmap.md`](../roadmap.md) for the execution sequence and evidence gates.
6. [`project/content_vocabulary_coverage.md`](../content_vocabulary_coverage.md) and the generated [`project/content_vocabulary_decisions.md`](../content_vocabulary_decisions.md) for the completed migration record and any later vocabulary work.
7. The four files beside this one for the exact handoff state and operating method.

Do not use `archive/` as current evidence. It preserves history, including approaches that were deliberately retired.

## Where the work stopped

The vocabulary migration is complete. All 1,305 lexicon entries are target-shaped, all eight optional modules have complete learning paths, SEM-09D is closed, and the decision register has no open or accepted-but-unimplemented item. The book is complete, the manual and primer are current, the fourteen-pamphlet shelf has complete practice coverage, the renderer-led identities for the principal shelves are complete, and Kia, the Short Road, and the Phi Book contents page have their finished entrance treatments. Tengwar is Phi's sole alternative writing system; the retired native-glyph studies remain under `archive/writing_systems/`.

The full-sentence parser is established as a strict grammar gate beside the main example validator. Its adopted repairs include universal modifier-first structure, one content gap per clause, the fixed reason position of `misa`, the required `pha ... pho` boundary around every embedded content question, and rejection of doubled quantity-tier marking such as `lo` plus a numeral or quantifier. The parser's default asserted-document set passes 3,313 complete examples with no error. A full `--docs` run parses 5,532 examples and retains two pre-existing diagnostics in `documents/evaluation/narrative_test_corpus.md`: PHS103 at line 46 and PHS115 at line 212. Treat those as separate parser-versus-corpus triage; do not rewrite the evaluation corpus merely to silence them.

The active literary shelf now uses translation, source refusal, or original Phi writing. D082 and D083 completed post-conversion fidelity sweeps of *The Little Prince* excerpts and *The Velveteen Rabbit*. D084 retired source-recasting as a general method and removed its manual chapter. Gibran's four present selections are translations, the six formerly paired works retain only their translations, all four original Phi works have received Phi-first reviews, and the Ring Verse remains an explicitly labelled refusal. English titles on the texts index and catalogue use title case consistently.

The first six chapters of *News from Nowhere* are now source-faithful translations rather than inherited adaptations. D085 through D096 give each chapter a translation pass followed by a separate exhaustive fidelity sweep. Every final source citation stream reconstructs its complete normalized Morris chapter body, every Phi sentence passes the strict validator, every exact gloss has been checked against the lexicon, and every derived-English line has been checked against the Phi proposition. No chapter in this six-chapter conversion added a root, module membership, registered compound, or grammar rule. D099 later adds Work `toreku` arch and replaces the eight architectural uses of `loriphi` across chapters 2 through 6. D100 adds Ecological `lomathu` manure, moves `tomewu` and `mokathi` into Medical and Bodily Care, and repairs the manure line in chapter 5. Neither decision changes a source citation or unit boundary.

D097 completed the horizontal consistency sweep across those six chapters, and pull requests #677 through #679 closed what it and the maintainer's own reading then exposed. Characters who recur carry one Phi onym in every chapter under the new canon rule that a translation is the naming community for people who cannot accept a name, and a continuing speech opens one quotative frame rather than one per sentence. D098 established that derived English must follow Phi rather than the adjacent source. D102 makes the production order strict: source to Phi first, then Phi to English with the source and prior English hidden. D103 makes *The North Wind and the Sun* the first certified translation under that process: seventeen Aesop units reconstruct exactly, the frozen Phi digest is `63fbc9282fe0651f27f18107ad34914e2358be446301e1bdf08f638d9296f470`, and a fresh context derives its glosses and English from the anonymous Phi packet. D104 establishes the exhaustive machine-checked queue in [`translation_process_status.md`](../../documents/evaluation/translation_process_status.md). D105 certifies the Metta Sutta as the second work: thirty-six Fausböll units reconstruct all 1,615 normalized source characters, the Phi freezes at `73851696237e395421f8dd12b005d8e6bee0332a1654a4734d317679c4c7d7d1`, and affected units receive new source-blind derivations after source-side repairs. D106 certifies *A Solarpunk Manifesto* as the third work: thirty-eight units reconstruct all 4,538 normalized source characters, the Phi freezes at `57baf00910adb9e5d0ec9c23ab0d56e2dcc3c023c787f336b279dce9c4b840ee`, and every English replacement comes from a fresh source-blind context after the affected Phi is settled. D107 certifies Schleicher's fable as the fourth work: four units reconstruct all 703 normalized source characters, the Phi freezes at `dec1e02503f0c9571c4da870a80d67610508efce1d8aa65cbd44d6e9641c3fca`, and a fresh derivation and audit follow the repair that distinguishes all three horses. D108 certifies UDHR Article 1 as the fifth work: two units reconstruct all 170 normalized source characters, the Phi freezes at `1fe727d7a07ead2ac96c2deb2a082f9356d3780c57326f1e9de5ea26bc831fa5`, and a fresh retry confirms that the framed sibling-spirit phrase modifies the required reciprocal action. D109 certifies the Babel text as the sixth work: nine units and ten citations reconstruct all 1,191 normalized King James characters, the Phi freezes at `2cb3d2ccc6b5bb33a1860a6081e45842ee0911a6bfa40637e410185e859da136`, and repaired relative roles receive new source-blind derivation before an isolated retry restores the earth's surface in English. D110 certifies *The Little Prince* selections as the seventh work: five citations reconstruct all 238 normalized Woods characters, the Phi freezes at `0cd1f7cd946000b9d6c635a645e90141ada25dacb0443845a912d8470226e3d2`, and an independent source-blind reader confirms the responsibility passage after two source-side units receive structural repairs. D111 certifies *The Velveteen Rabbit* as the eighth work: 426 units freeze at `16597a3af79e10b9ff4e66638108da09e4c9fb6bce6ccd4d275ccb4b841c3f59`, all final English comes from fresh source-blind derivation, and independent readers audit the repaired units before publication. D112 certifies Gibran's *On Love* as the ninth work: thirty-three units reconstruct all 2,403 normalized source characters, the Phi freezes at `7494350b9f12a5a616c046057cf8dffcfc5e9ad8ea54f7e7c35e0f48a85d6125`, and fresh source-blind retries close the final attachment ambiguities. D113 certifies Gibran's *On Children* as the tenth work: eighteen units reconstruct all 980 normalized source characters, the Phi freezes at `028a864fb7bb333245159dcf9e2048b9021c3dab04a34f0e299506da9d059455`, and fresh unit-scoped derivations follow every Phi repair exposed by independent review. *The Prophet, On Giving* is next in the queue.

The book's title remains The Phi Book for now, with *A Language You Cannot Hurry* and *Announce, Then Deliver* recorded as candidates. The maintained future-work ledger remains [`project/deferred_questions.md`](../deferred_questions.md); do not turn a parked item into active work without a command.

## The maintainer's working contract

The following habits came from direct maintainer corrections. Treat them as standing instructions unless Daniel changes them.

- A question is not permission to edit. Answer questions and act on commands.
- Do not wait for outside proof before coining a useful word. Phi is a personal constructed language, not an RFC process or an auxiliary-language standards body.
- Do not turn Phi into an English relex. Test composition, semantic family, and actual conceptual need, then coin confidently when a root is the better Phi choice.
- Never let a noticed lexical gap vanish into conversation. Give it a decision ID before closing the batch, even when the decision is compositional, deferred, source-bound, or declined.
- Keep base vocabulary ordinary and broadly useful. Specialized words may belong to several modules; the `modules` field is an array for a reason.
- Modules add vocabulary only. Phi's grammar and particle system are complete, and no module may add syntax, parsing rules, or incompatible constructions.
- Lexical words have no more than three syllables, including module vocabulary. Productive names alone may use a legal four-syllable form.
- Every voice in *News from Nowhere* may use the full vocabulary, including optional modules. Module membership limits what a general learner is expected to study; it does not divide the novel's speakers into lexical registers.
- Translation has two isolated phases. Finish source to Phi before deriving English, then give the shared compact reference and bounded anonymous packets to a fresh, non-forked model context that has never seen the source or prior English. A second source-blind context checks the risk-selected queue and deterministic sample. Discard the affected English whenever Phi changes, use a unit-scoped retry, and never compare the source directly with derived English.
- Peace linguistics is a design boundary, not decoration. Do not introduce generic conflict or direct combat vocabulary, weapon-centred framing, domination terms, or combat metaphors into Phi-authored material. Phi must still name danger, harm, coercion, injury, testimony, protection, accountability, redress, and repair.
- Exact clock units, physical units, money language, and industrial measurement are settled refusals. Read [`documents/design/psychological_violence_of_measurement.md`](../../documents/design/psychological_violence_of_measurement.md) before working near time, quantity, distance, weight, or exchange.
- Point out accidental English homonyms whenever they appear in a proposed Phi form or an existing form under review.
- Never use the discarded hyphenated adjective pattern recorded in [`language_and_voice.md`](language_and_voice.md). The maintainer has ruled it out without exception.
- `sound_symbolism` is optional embodied phonesthetics. It is not hidden morphology and should not become grandiose prose. `articulatory_notes` is the physical account of how the complete word is spoken.
- Apply the installed Humanizer skill and [`documents/reference/voice_for_models.md`](../../documents/reference/voice_for_models.md) in full only to reader-facing content. That includes the book, manual, primer, pamphlets, literary texts, Kia, the Short Road, public site copy, lexicon prose, commit messages, pull-request titles and bodies, and public GitHub issue prose. Handoffs, plans, roadmaps, development logs, decision records, audit notes, validation reports, temporary reports, and internal boilerplate need direct, accurate prose instead. A public PR remains in scope even when the repository files it describes are internal. For reader-facing work, invoke the skill per artifact, run the full protocol, and report a concrete correction; do not manufacture a Humanizer finding for an internal document.
- Keep every Markdown prose paragraph and list-item paragraph on one physical line.
- Do not spend a substantive vocabulary, corpus, or renderer pass on Canadian, British, or American spelling checks. A later sweep can settle the repository's mixture.
- Book humour should borrow the kind, not the quantity, of Jerome K. Jerome's *Three Men in a Boat*: mild self-exposure, practical absurdity, and an occasional dry turn. It must not become a string of jokes.
- Do not describe Phi merely as a "slow language." Its unhurried quality is freedom from needless haste, and the centre is mindful and compassionate speech in the present utterance.
- Warmth is never rationed downward. On every teaching-corpus and retrofit pass, and on any commission naming an additive goal such as warmth, richness, or aspiration, the additive pass runs first, file by file, before the accuracy pass. A file already judged accurate is not thereby finished; dryness is its own finding, and the latent-image hunt runs on every file whether or not anything was ever stripped from it.
- No file closes at zero additions on the model's own judgment. When a file seems genuinely saturated, the pull request flags it as claimed saturated and Daniel confirms or sends it back; only he closes a file at zero. This rule exists because the model twice judged restraint correct on an additive commission and was wrong both times.
- Every pass's pull request body carries a per-file additions ledger: every file listed, what was added to it, zeros visible. Presenting a low-addition tally as restraint, taste, or virtue is the exact failure these three rules prevent.
- Do not start a local web server for routine handoff or vocabulary work. Daniel connects to the Mac mini over SSH and cannot use a server bound only to that machine. Build the site, but leave it stopped unless a specific remote-access arrangement is requested.
- Use one coherent pull request per completed effort. Pass every PR body with `--body-file`, never as an inline shell argument.
- When Daniel reports that a PR has merged, perform the full local and remote branch cleanup without waiting for a second request.
- The manual is a standalone document. Reader-facing manual text carries no repository paths, no vocabulary field names, and no tooling instructions, because a reader has never seen a stored entry and cannot open `documents/`, `vocabulary/`, `scripts/`, or canon from the website. Point only at what the site publishes: the lexicon, the primer, the short road, the book, the pamphlets, the texts, Part VII, the colophon. Where nothing published covers the point, drop the pointer and let the sentence carry its own claim.
- Do not write an exact repository count into prose. Nothing checks it, so it goes stale silently and stays wrong for months. Use a round lower bound that survives growth, measure before writing even that, and keep an exact figure only where the arithmetic is the content. A number attached to a past event is a record: leave it alone or drop the number rather than renumbering the event.

## Package contents

| File | What it contains |
|---|---|
| [`current_state.md`](current_state.md) | Counts, latest decisions, the active corpus task, book state, and parked work. |
| [`vocabulary_migration.md`](vocabulary_migration.md) | The full batch method, prose contract, decision register, coinage checks, regeneration, validation, and failure recovery. |
| [`repository_workflow.md`](repository_workflow.md) | Repository map, utility commands, generated files, CI, branch and PR procedure, cleanup, site builds, source reconstruction, and citation audits. |
| [`language_and_voice.md`](language_and_voice.md) | Authority, governing purpose, canon constraints most likely to be violated, source and name practice, peace linguistics, writing voice, Humanizer, and book register. |

## Starting a continuation turn

A replacement model can use this opening checklist:

```text
1. Confirm the newest user request and whether it is a question or a command.
2. Read AGENTS.md and canon.md. If the request creates or revises reader-facing prose, also read the full voice guide and load the full Humanizer skill.
3. Run git status --short --branch and verify that main is clean and current.
4. Read current_state.md, project/deferred_questions.md, and project/roadmap.md before assuming that an older sequence is still active.
5. If revising a translation, read the translate skill and use separate source-to-Phi and Phi-to-English working views. For other corpus work, inspect the passage's declared relationship, dependencies, module vocabulary, and validated examples.
6. Create a feature branch only after the scope is understood.
7. Carry the work through drafting, any applicable Humanizer and voice audit, validation, commit, push, PR, and CI unless the user explicitly asks to pause.
```

The handoff is successful when the next model can begin from the live state without re-deriving Phi's boundaries, and without treating this snapshot as permission to ignore the repository that produced it.
