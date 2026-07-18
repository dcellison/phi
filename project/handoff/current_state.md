# Current state

This snapshot was first assembled after pull request #418 merged on 17 July 2026 and has been refreshed through D044. Its counts describe the current tracked work; Git history remains the source for branch and merge identifiers.

## Active execution sequence

The roadmap's current sequence is not an invitation to choose among several equal tasks. It records one active path:

1. SEM-09D: inspect active Phi passages now that the base queue is zero.
2. SEM-09C: migrate 209 legacy module entries.
3. PED-08: resume the book at chapter 7.

Do not jump into module prose before the post-base corpus sweep is complete. A previous batch briefly crossed the base-first boundary; the maintainer corrected it, and D044 has now completed that base work.

## Lexicon migration counts

| Inventory | Total | Target | Legacy |
|---|---:|---:|---:|
| Entire lexicon | 1,260 | 1,051 | 209 |
| Content vocabulary | 1,130 | 921 | 209 |
| Base content vocabulary | 884 | 884 | 0 |
| Optional-module content vocabulary | 246 | 37 | 209 |
| Function vocabulary | 110 | 110 | 0 |
| Interjections | 20 | 20 | 0 |

There are no partial or dual entries. A target entry has both `articulatory_notes` and structured `examples` and has neither legacy `concept` nor `grammatical_notes`. The committed evidence is [`documents/validation/vocabulary_prose_coverage.json`](../../documents/validation/vocabulary_prose_coverage.json).

The latest completed prose batch is D044, Roles, places, relations, and remaining concrete nouns. It migrated the final 18 base nouns without adding a root and closed SEM-09B. The immediately preceding batches covered reason and value, language and art, space and orientation, tools and travel, dwelling and food, materials, living systems, landscape and weather, and time. Do not reopen those entries merely to make their English prose different; reopen one only for a real semantic, factual, voice, or corpus problem.

## Decision register

[`project/content_vocabulary_decisions.json`](../content_vocabulary_decisions.json) is the canonical operational register. Its readable view is generated.

| Item | Count |
|---|---:|
| Semantic batches | 55 |
| Decisions | 145 |
| Implemented | 39 |
| Compositional | 47 |
| Deferred with return condition | 30 |
| Source-bound | 25 |
| Declined | 4 |
| Open | 0 |
| Accepted but not implemented | 0 |

The latest development decision is D044 in [`project/development_log.md`](../development_log.md). Check the live log before assigning the next identifier.

## Base queue complete

D044 migrated `rulami`, `menua`, `pukea`, `kenua`, `woru`, `nepha`, `phaliso`, `panuri`, `thunepa`, `phewo`, `thelui`, `thonua`, `kupela`, `phirenu`, `thena`, `themoka`, `silawo`, and `niro`. Their forms and exact glosses did not change. The pass removed idealised role and place claims, separated practical warning from quantified risk, kept medicine apart from treatment and exact product identity, clarified web, net, network, and system, and retained resource as a relationship to a stated purpose rather than an inherent status.

The broad completeness review added seventeen decisions and linked six earlier ones. No new root was needed. Registered `thero muralo` supplies ordinary fuel, while specialist fuels keep their existing material return condition. Electricity, electric charge and current, and related electrical phenomena have the concrete `CV-ENERGY-01` return point for connected Systems or related module work. Exact clinical, technical, legal, academic, cultural, security, weather, and civic identities remain source-bound. The live query that proves the base queue is empty is:

```bash
jq -r 'select((has("concept") or has("grammatical_notes")) and (((.modules // []) | length) == 0)) | [input_filename,.word,.gloss,.pos,((.semantic_domains // {}) | keys | join(","))] | @tsv' vocabulary/content/*.json | sort
```

Run it before trusting the zero count. The snapshot is not a substitute for the files.

## Module state

Phi has eight established vocabulary modules, one grammar, 246 optional roots, and 355 module memberships. A root may appear in several modules.

| Module | Total current memberships | Legacy entries in that learning path |
|---|---:|---:|
| Household and Daily Life | 42 | 40 |
| Medical and Bodily Care | 48 | 42 |
| Systems and Shared Infrastructure | 37 | 31 |
| Philosophical Reasoning | 21 | 17 |
| Accessibility and Participation | 45 | 32 |
| Commons and Collective Governance | 51 | 46 |
| Ecological Systems and Material Life | 46 | 42 |
| Work, Craft, and Repair | 65 | 51 |

The legacy counts overlap because a shared word appears once in the 209-entry queue but contributes to each module it belongs to. Preserve the complete `modules` array when an entry is migrated. When SEM-09C begins, the historical creation order is a useful default: Philosophical Reasoning; Systems and Shared Infrastructure; Ecological Systems and Material Life; Commons and Collective Governance; Household and Daily Life; Medical and Bodily Care; Accessibility and Participation; Work, Craft, and Repair. Confirm the order with Daniel before the first module PR if the sequence matters to him then.

All eight profiles already have canonical JSON membership, a generated module index, and a speaker-facing Part VII chapter. No ninth profile is proposed. [`documents/modules/potential_profile_explorations.md`](../../documents/modules/potential_profile_explorations.md) holds conditional possibilities without making them active work.

## Corpus state

The literary shelf has completed its full review against the current lexicon. It contains nine close translations and eleven transmutations; seven works have both. *News from Nowhere* is one 32-chapter work with the first three chapters transmuted and reviewed. The current review record is [`documents/evaluation/active_text_corpus_review.md`](../../documents/evaluation/active_text_corpus_review.md).

SEM-09D is now active. It is not a blind replacement pass. The sweep covers the book, manual, primer, pamphlets, texts, and current documents for paraphrases or workarounds involving words coined during the base expansion. A Phi passage changes only when the newer form is more faithful or natural in that passage. A transparent composition stays when its parts still teach or express the thought better, and every changed sentence and dependency receives validation.

The shelf's method distinction remains settled:

- A translation is answerable to every source proposition, relation, and image as closely as Phi permits.
- A transmutation may change the source under Phi's five pillars, but every departure must be deliberate, visible in the back-translation, and recorded honestly.
- Phi prefers transmutation as its own literary practice. Close translations show what the language can carry without implying that source fidelity is the preferred creative method.

## Book state

The book has eight drafted files: the cold open, chapters 1 through 6, and chapter 11. All appear on the website. Every chapter has a references section and a `Phi sources` subsection.

| Chapter | File | Approximate words |
|---|---|---:|
| Cold open: The boatman | `book/00_the_boatman.md` | 940 |
| 1. The hurried tongue | `book/01_the_hurried_tongue.md` | 2,481 |
| 2. What a refusal is | `book/02_what_a_refusal_is.md` | 1,628 |
| 3. The invented century | `book/03_the_invented_century.md` | 3,049 |
| 4. Announce, then deliver | `book/04_announce_then_deliver.md` | 2,532 |
| 5. The web | `book/05_the_web.md` | 2,542 |
| 6. What it will not say | `book/06_what_it_will_not_say.md` | 1,684 |
| 11. The lens, not the cage | `book/11_the_lens_not_the_cage.md` | 4,073 |

The treatment aims for 4,000 to 6,000 words per chapter and 70,000 to 90,000 words overall, but Daniel chose to continue rather than pad early chapters merely to meet a projection. Do not silently lengthen merged chapters. A later structural edit can decide where depth is genuinely missing.

The next planned draft is chapter 7, "A literature before a community." It comes after SEM-09D and SEM-09C. Read [`book/treatment.md`](../../book/treatment.md), chapter 6, and several neighbouring finished chapters before drafting. Each chapter is its own PR. Audit every external citation after the draft, repair the prose from the audit, preserve the consistent `Phi sources` subsection, and use restrained Jerome humour where it fits.

The leading book title remains *A Language You Cannot Hurry*. *Announce, Then Deliver* is the alternate. The title is open. "Hurry" must continue to mean attention discarded under pressure, not fast speech.

Citation work performed in earlier conversations is not preserved as a complete set of repository audit reports. Do not infer that a citation is sound merely because the chapter is merged. Recheck any citation whose surrounding claim changes, and audit every new chapter from primary sources before calling it complete.

## Parked and future work

[`project/deferred_questions.md`](../deferred_questions.md) is the maintained list. Its live entries are:

| Item | State | Return condition |
|---|---|---|
| Native glyph mode | Parked | Daniel chooses to resume exploration of Phi's one intended native script. |
| Spoken source material and code-switching | Open design question | Live conversational examples make the current outside-syntax boundary inadequate. Do not reintroduce guest or exact frames. |
| Sexual and reproductive anatomy | Queued scenario-led vocabulary effort | Begin as its own respectful corpus and vocabulary project, not as an unnoticed extension of Medical vocabulary. |
| Legacy vocabulary prose audit | Active | Complete the post-base corpus retrofit and 209 module entries; the base queue reached zero in D044. |
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
