# Current state

This snapshot was first assembled after pull request #418 merged on 17 July 2026 and has been refreshed through D053, the fifteenth SEM-09D literary retrofit, the drafted-book pass, chapter 7, and the manual Parts I through IV teaching passes. Its counts describe the current tracked work; Git history remains the source for branch and merge identifiers.

## Active execution sequence

The literary shelf and Phi book are current through chapter 7. The execution sequence is now:

1. Resume SEM-09D at manual Part V, then continue through the rest of the manual, primer, pamphlets, and current documents.
2. Return to PED-08 at chapter 8 after that sweep.

D044 completed the base-first boundary, and D045 through D052 completed all eight learning paths in their historical order. The full migration has one editorial judgement and voice. SEM-09D began with Schleicher's fable. That pilot preserved every Phi line after checking later base roots and optional terms, while D053 repaired `kawhera` and `pilora` after their target prose proved narrower than their validated animal uses. The second pass replaced three older circumlocutions in *The North Wind and the Sun* with `mesatu` (try), `komeri` (forehead), and `phesari` (flee) in both the translation and transmutation. The third replaced four detours in the Metta Sutta with `sheraki` (search), `tupeka` (burden), `rinu` (want), and `huwa` (weak). The fourth leaves both UDHR Article 1 renderings intact and identifies `remo` as thinking rather than a dedicated rational faculty. The fifth repairs Babel's physical joining, the tower's top, the builders' wish for renown, imagined action, and punitive scattering without adding a root. The sixth restores reverence, perception, change, and verse in the Heart Sutra. It also removes a quantitative misuse of `thenoi` and keeps physical `whalo` out of the English "great" homonym. The seventh brings `phomila`, `lioru`, `lima`, and `mesatu` into *The Prophet, On Children*. The eighth gives the Tao Te Ching translation `kowanu`, `monaki`, and direct `kethua`; both renderings distinguish `lioru`, life, and state completed withering through `ki kureno`. The ninth revises seventeen Solarpunk units, uses all eight modules, and removes technical vocabulary from general solutions, human ability, social power, and ordinary living. The tenth replaces unadorned `mueli` with simple `siloma` in *The Little Prince* and uses perfective `ki` for the bond whose result still holds. The eleventh preserves the Ring Verse refusal's 12 base and function forms while bringing its account of dominion into line with the completed Commons and Systems distinctions. The twelfth changes 46 units in *The Velveteen Rabbit*, separates search from finding and wear from age, and brings exact household and bodily words into the nursery without changing Williams's source witness. The thirteenth changes 29 units in *News from Nowhere* chapter 1, separates authority from guidance and representation from thought, and brings direct words for coercion, winter, wear, waking, and observation into Morris's first night without changing his source witness. The fourteenth now changes 57 units in chapter 2, adds direct tide and service to its earlier repairs, and preserves every Morris line. The fifteenth changes 46 units in chapter 3, gives the house and breakfast direct household language, gives the weaver his craft terms, and preserves all 245 Morris lines. The drafted-book pass preserves thirteen of fifteen fenced examples, revises two in the cold open, corrects the account of `wia` and transmutation, and aligns the schema discussion with the completed lexicon contract. The first teaching pass reviews all nine Part I files, corrects determinist and universal claims, replaces obsolete sound lore with current articulation, and rebuilds the beginner exchange without adding a root or module term. The second reviews all nineteen Part II files, preserves the two current sound essays, and repairs the remaining chapters' cultural, phonesthetic, grammatical, social, and learning claims without adding a root or module term.

The third teaching pass reviews all eleven Part III files. It preserves the current IPA reference, repairs the other ten lessons' articulation, accent, word-shape, and writing-mode claims, and finds no lexical gap or module need.

The fourth teaching pass reviews all fifty-three Part IV files. It restores the closed particle inventories and their scope, removes psychological guarantees from word order, repairs noun, numeral, pronoun, tense, aspect, voice, modality, and evidential teaching, and finds no lexical gap. One optional Work word appears only in an explicitly labelled comparison with its base description. The pass also reconciles the canon account of ceremony, ritual, festival, and source-bound named rites.

## Lexicon migration counts

| Inventory | Total | Target | Legacy |
|---|---:|---:|---:|
| Entire lexicon | 1,275 | 1,275 | 0 |
| Content vocabulary | 1,145 | 1,145 | 0 |
| Base content vocabulary | 884 | 884 | 0 |
| Optional-module content vocabulary | 261 | 261 | 0 |
| Function vocabulary | 110 | 110 | 0 |
| Interjections | 20 | 20 | 0 |

There are no partial or dual entries. A target entry has both `articulatory_notes` and structured `examples` and has neither legacy `concept` nor `grammatical_notes`. The committed evidence is [`documents/validation/vocabulary_prose_coverage.json`](../../documents/validation/vocabulary_prose_coverage.json).

The latest completed prose batch is D052, Work, Craft, and Repair. It migrated sixteen inherited entries without adding a root and brought the eighth learning path to zero legacy prose. D044 remains the base-first boundary. Do not reopen completed entries merely to make their English prose different; reopen one only for a real semantic, factual, voice, or corpus problem.

## Decision register

[`project/content_vocabulary_decisions.json`](../content_vocabulary_decisions.json) is the canonical operational register. Its readable view is generated.

| Item | Count |
|---|---:|
| Semantic batches | 63 |
| Decisions | 235 |
| Implemented | 49 |
| Compositional | 110 |
| Deferred with return condition | 29 |
| Source-bound | 43 |
| Declined | 4 |
| Open | 0 |
| Accepted but not implemented | 0 |

The latest development decision is D053 in [`project/development_log.md`](../development_log.md). Check the live log before assigning the next identifier.

## Base queue complete

D044 migrated `rulami`, `menua`, `pukea`, `kenua`, `woru`, `nepha`, `phaliso`, `panuri`, `thunepa`, `phewo`, `thelui`, `thonua`, `kupela`, `phirenu`, `thena`, `themoka`, `silawo`, and `niro`. Their forms and exact glosses did not change. The pass removed idealised role and place claims, separated practical warning from quantified risk, kept medicine apart from treatment and exact product identity, clarified web, net, network, and system, and retained resource as a relationship to a stated purpose rather than an inherent status.

The broad base completeness review added seventeen decisions and linked six earlier ones. Registered `thero muralo` supplies ordinary fuel, while specialist fuels keep their existing material return condition. D046 has now implemented the former electrical return point with `thewaki` electricity, `rishonu` charge, `sephaki` current, `poweshi` voltage, and `phoselu` technical power. Exact clinical, technical, legal, academic, cultural, security, weather, and civic identities remain source-bound. The live query that proves the base queue is empty is:

```bash
jq -r 'select((has("concept") or has("grammatical_notes")) and (((.modules // []) | length) == 0)) | [input_filename,.word,.gloss,.pos,((.semantic_domains // {}) | keys | join(","))] | @tsv' vocabulary/content/*.json | sort
```

Run it before trusting the zero count. The snapshot is not a substitute for the files.

## Module state

Phi has eight established vocabulary modules, one grammar, 261 optional roots, and 393 module memberships. A root may appear in several modules.

| Module | Total current memberships | Legacy entries in that learning path |
|---|---:|---:|
| Household and Daily Life | 44 | 0 |
| Medical and Bodily Care | 51 | 0 |
| Systems and Shared Infrastructure | 50 | 0 |
| Philosophical Reasoning | 24 | 0 |
| Accessibility and Participation | 46 | 0 |
| Commons and Collective Governance | 53 | 0 |
| Ecological Systems and Material Life | 55 | 0 |
| Work, Craft, and Repair | 70 | 0 |

Every module learning path now has zero legacy prose, and every complete `modules` array was preserved during migration. D045 through D052 complete SEM-09C in the modules' historical order.

All eight profiles already have canonical JSON membership, a generated module index, and a speaker-facing Part VII chapter. No ninth profile is proposed. [`documents/modules/potential_profile_explorations.md`](../../documents/modules/potential_profile_explorations.md) holds conditional possibilities without making them active work.

## Corpus state

The literary shelf has completed its full review against the current lexicon. It contains nine close translations and eleven transmutations; seven works have both. *News from Nowhere* is one 32-chapter work with the first three chapters transmuted and reviewed. The current review record is [`documents/evaluation/active_text_corpus_review.md`](../../documents/evaluation/active_text_corpus_review.md).

SEM-09D is in progress. Fifteen literary passes complete the shelf, and all three drafted *News from Nowhere* chapters are among them. The Phi book is current through chapter 7. Manual Parts I through IV are reviewed without a lexical gap; Part IV uses one explicitly labelled optional Work term. The remaining active-corpus retrofit resumes at manual Part V, followed by the rest of the manual, primer, pamphlets, and current documents. A Phi passage changes only when the current form is more faithful or natural there. A transparent composition stays when its parts still teach or express the thought better, and every changed sentence and dependency receives validation.

The shelf's method distinction remains settled:

- A translation is answerable to every source proposition, relation, and image as closely as Phi permits.
- A transmutation may change the source under Phi's five pillars, but every departure must be deliberate, visible in the back-translation, and recorded honestly.
- Phi prefers transmutation as its own literary practice. Close translations show what the language can carry without implying that source fidelity is the preferred creative method.

## Book state

The book has nine drafted files: the cold open, chapters 1 through 7, and chapter 11. All appear on the website. Every chapter has a references section and a `Phi sources` subsection.

| Chapter | File | Approximate words |
|---|---|---:|
| Cold open: The boatman | `book/00_the_boatman.md` | 993 |
| 1. The hurried tongue | `book/01_the_hurried_tongue.md` | 2,481 |
| 2. What a refusal is | `book/02_what_a_refusal_is.md` | 1,621 |
| 3. The invented century | `book/03_the_invented_century.md` | 3,049 |
| 4. Announce, then deliver | `book/04_announce_then_deliver.md` | 2,532 |
| 5. The web | `book/05_the_web.md` | 2,545 |
| 6. What it will not say | `book/06_what_it_will_not_say.md` | 1,675 |
| 7. A literature before a community | `book/07_a_literature_before_a_community.md` | 3,076 |
| 11. The lens, not the cage | `book/11_the_lens_not_the_cage.md` | 4,073 |

The treatment aims for 4,000 to 6,000 words per chapter and 70,000 to 90,000 words overall, but Daniel chose to continue rather than pad early chapters merely to meet a projection. Do not silently lengthen merged chapters. A later structural edit can decide where depth is genuinely missing.

The next planned draft is chapter 8, "The workshop," after the remaining SEM-09D teaching and project-document sweep. Its targeted research includes current disclosure norms for generative tools in creative work and a historical check of the Morris and Co. analogy. Read [`book/treatment.md`](../../book/treatment.md), chapter 7, and several neighbouring finished chapters before drafting. Each chapter is its own PR. Audit every external citation after the draft, repair the prose from the audit, preserve the consistent `Phi sources` subsection, and use restrained Jerome humour where it fits.

The leading book title remains *A Language You Cannot Hurry*. *Announce, Then Deliver* is the alternate. The title is open. "Hurry" must continue to mean attention discarded under pressure, not fast speech.

Citation work performed in earlier conversations is not preserved as a complete set of repository audit reports. Do not infer that a citation is sound merely because the chapter is merged. Recheck any citation whose surrounding claim changes, and audit every new chapter from primary sources before calling it complete.

## Parked and future work

[`project/deferred_questions.md`](../deferred_questions.md) is the maintained list. Its live entries are:

| Item | State | Return condition |
|---|---|---|
| Native glyph mode | Parked | Daniel chooses to resume exploration of Phi's one intended native script. |
| Spoken source material and code-switching | Open design question | Live conversational examples make the current outside-syntax boundary inadequate. Do not reintroduce guest or exact frames. |
| Sexual and reproductive anatomy | Queued scenario-led vocabulary effort | Begin as its own respectful corpus and vocabulary project, not as an unnoticed extension of Medical vocabulary. |
| Legacy vocabulary prose audit | Complete; contextual retrofit in progress | D044 completed the base queue, and D045 through D052 completed all eight module learning paths. The literary shelf, drafted book, and manual Parts I through IV are current; the remaining teaching and project-document sweep begins at manual Part V. |
| Lexical relations between content words | Parked | The explorer or project needs curated related-word navigation strongly enough to add and maintain a schema field. |
| Tengwar renderer verification | Parked | Tengwar work resumes or approaches publication status. |
| Solarpunk community engagement | Open strategic question | Daniel is ready to offer Phi outside its repository and decide what a healthy invitation looks like. |

Speech evidence, outside learner evidence, community governance, and print publication remain evidence-gated or deferred in the roadmap. Do not mark them complete because tools or materials exist. Do not invent participants, observations, or adoption.

## State checks for a new session

Use these commands before trusting this snapshot:

```bash
git status --short --branch
git log -1 --oneline --decorate
python3 scripts/vocabulary_prose_coverage.py
python3 scripts/content_vocabulary_decisions.py --check
jq '{total,states,by_kind,fields}' documents/validation/vocabulary_prose_coverage.json
```

If running `vocabulary_prose_coverage.py` changes the committed report on an otherwise untouched branch, stop and inspect the live lexicon before continuing. A stale report means the state has moved beyond this handoff.
