# Current state

This snapshot describes the repository immediately after pull request #418 merged on 17 July 2026. The merge commit is `287d8673bd48ed31e3c70b42e51d5fb89dab09e2`. Local `main` and `origin/main` matched, the feature branch had been removed locally and remotely, and the worktree was clean before this handoff branch was created.

## Active execution sequence

The roadmap's current sequence is not an invitation to choose among several equal tasks. It records one active path:

1. SEM-09B: migrate the final 36 base content entries.
2. SEM-09D: inspect active Phi passages after the base queue reaches zero.
3. SEM-09C: migrate 209 legacy module entries.
4. PED-08: resume the book at chapter 7.

Do not jump into module prose before the base queue and the post-base corpus sweep are complete. A previous batch briefly crossed that boundary; the maintainer corrected it and asked that base vocabulary be finished first.

## Lexicon migration counts

| Inventory | Total | Target | Legacy |
|---|---:|---:|---:|
| Entire lexicon | 1,260 | 1,015 | 245 |
| Content vocabulary | 1,130 | 885 | 245 |
| Base content vocabulary | 884 | 848 | 36 |
| Optional-module content vocabulary | 246 | 37 | 209 |
| Function vocabulary | 110 | 110 | 0 |
| Interjections | 20 | 20 | 0 |

There are no partial or dual entries. A target entry has both `articulatory_notes` and structured `examples` and has neither legacy `concept` nor `grammatical_notes`. The committed evidence is [`documents/validation/vocabulary_prose_coverage.json`](../../documents/validation/vocabulary_prose_coverage.json).

The latest completed prose batch is D042, Language, story, art, and representation. It migrated 18 base nouns without adding a root. The immediately preceding batches covered space and orientation, tools and travel, dwelling and food, materials, living systems, landscape and weather, and time. Do not reopen those entries merely to make their English prose different; reopen one only for a real semantic, factual, voice, or corpus problem.

## Decision register

[`project/content_vocabulary_decisions.json`](../content_vocabulary_decisions.json) is the canonical operational register. Its readable view is generated.

| Item | Count |
|---|---:|
| Semantic batches | 53 |
| Decisions | 117 |
| Implemented | 39 |
| Compositional | 33 |
| Deferred with return condition | 30 |
| Source-bound | 13 |
| Declined | 2 |
| Open | 0 |
| Accepted but not implemented | 0 |

The next completed batch will normally become D043 in [`project/development_log.md`](../development_log.md), unless an intervening decision uses that identifier first. Check the live log before assigning it.

## The final 36 base entries

The table below gives every base entry still using legacy prose. Forms and exact glosses remain fixed unless a separate lexical decision changes them. Existing semantic domains are starting evidence, not a command to preserve an old classification that no longer makes sense.

Two 18-entry batches would close SEM-09B with less repository churn than several tiny PRs. The proposed split is deliberately marked as a suggestion. Read all entries, their neighbours, canon rulings, and corpus uses before choosing the final headings.

### Suggested batch A: Reason, belief, ritual, and value

| File | Phi | Exact gloss | Current semantic domains |
|---|---|---|---|
| `vocabulary/content/ceremony.json` | `thorea` | ceremony | community, ritual, temporal |
| `vocabulary/content/criterion.json` | `kirema` | criterion | cognition, wisdom |
| `vocabulary/content/custom.json` | `keno` | custom | community, temporal |
| `vocabulary/content/evidence.json` | `thesori` | evidence | cognition, wisdom |
| `vocabulary/content/festival.json` | `holia` | festival | emotion, ritual |
| `vocabulary/content/insight.json` | `sorai` | insight | cognition, wisdom |
| `vocabulary/content/justice.json` | `theloma` | justice | communication, community, wisdom |
| `vocabulary/content/luck.json` | `soleha` | luck | cognition, temporal |
| `vocabulary/content/magic.json` | `whekelu` | magic | cognition, nature |
| `vocabulary/content/method.json` | `norae` | method | cognition, wisdom |
| `vocabulary/content/purpose.json` | `porua` | purpose | cognition, wisdom |
| `vocabulary/content/reason.json` | `remotha` | reason | cognition, communication, wisdom |
| `vocabulary/content/ritual.json` | `thelumo` | ritual | community, ritual, temporal, wisdom |
| `vocabulary/content/soul.json` | `norea` | soul | cognition, wisdom |
| `vocabulary/content/spirit.json` | `phiora` | spirit | cognition, nature |
| `vocabulary/content/tradition.json` | `therema` | tradition | community, ritual, temporal, wisdom |
| `vocabulary/content/vision.json` | `lunai` | vision | cognition, temporal |
| `vocabulary/content/worth.json` | `rolia` | worth | community, wisdom |

This batch contains several canon-sensitive boundaries. `thorea` is the only ceremony word and specific rites are refused. `rolia` is inherent worth, while `sone` is the act of valuing. Evidence, reason, criterion, method, insight, and justice must remain distinct. Soul, spirit, magic, luck, vision, custom, tradition, ritual, ceremony, and festival must be described without declaring one metaphysics or tradition to be universal. Source-bound religious and cultural names keep their own forms.

### Suggested batch B: Roles, places, relations, and remaining concrete nouns

| File | Phi | Exact gloss | Current semantic domains |
|---|---|---|---|
| `vocabulary/content/adventure.json` | `rulami` | adventure | activity, temporal |
| `vocabulary/content/counselor.json` | `menua` | counselor | community, wisdom |
| `vocabulary/content/danger.json` | `pukea` | danger | community, nature, physical |
| `vocabulary/content/energy.json` | `kenua` | energy | nature, physical |
| `vocabulary/content/keeper.json` | `woru` | keeper | community, temporal |
| `vocabulary/content/medicine.json` | `nepha` | medicine | creation, physical |
| `vocabulary/content/network.json` | `phaliso` | network | community, creation |
| `vocabulary/content/resource.json` | `panuri` | resource | activity, community, physical |
| `vocabulary/content/sacred-place.json` | `thunepa` | sacred place | ritual, spatial |
| `vocabulary/content/sage.json` | `phewo` | sage | community, wisdom |
| `vocabulary/content/sanctuary.json` | `thelui` | sanctuary | ritual, spatial |
| `vocabulary/content/scholar.json` | `thonua` | scholar | cognition, community |
| `vocabulary/content/secret.json` | `kupela` | secret | cognition, communication |
| `vocabulary/content/snow.json` | `phirenu` | snow | nature, temporal |
| `vocabulary/content/thing.json` | `thena` | thing | cognition, physical |
| `vocabulary/content/treasure.json` | `themoka` | treasure | cognition, emotion |
| `vocabulary/content/village.json` | `silawo` | village | community, spatial |
| `vocabulary/content/web.json` | `niro` | web | nature, spatial |

This is a residual batch, so its completeness review must be broader than its heading. Check whether any word is too specialized for base vocabulary, but do not move an established base word into a module merely because one module uses it. Pay particular attention to `energy`, whose ordinary and technical senses can drift; `medicine`, which must remain distinct from remedy, treatment, and clinical source records; `resource`, which can reduce living relations to use; and role nouns, which must not acquire verbs under the rejected noun-to-verb direction.

The live query for this queue is:

```bash
jq -r 'select((has("concept") or has("grammatical_notes")) and (((.modules // []) | length) == 0)) | [input_filename,.word,.gloss,.pos,((.semantic_domains // {}) | keys | join(","))] | @tsv' vocabulary/content/*.json | sort
```

Run it again before every batch. The table in this snapshot is not a substitute for the files.

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

SEM-09D begins only after the 36 base entries reach target state. It is not a blind replacement pass. Search the book, manual, primer, pamphlets, texts, and current documents for paraphrases or workarounds involving words coined during the base expansion. Change a Phi passage only when the newer form is more faithful or natural in that passage. Preserve a transparent composition when its parts still teach or express the thought better. Validate every changed sentence and its dependencies.

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

The next planned draft is chapter 7, "A literature before a community." It comes after SEM-09B, SEM-09D, and SEM-09C. Read [`book/treatment.md`](../../book/treatment.md), chapter 6, and several neighbouring finished chapters before drafting. Each chapter is its own PR. Audit every external citation after the draft, repair the prose from the audit, preserve the consistent `Phi sources` subsection, and use restrained Jerome humour where it fits.

The leading book title remains *A Language You Cannot Hurry*. *Announce, Then Deliver* is the alternate. The title is open. "Hurry" must continue to mean attention discarded under pressure, not fast speech.

Citation work performed in earlier conversations is not preserved as a complete set of repository audit reports. Do not infer that a citation is sound merely because the chapter is merged. Recheck any citation whose surrounding claim changes, and audit every new chapter from primary sources before calling it complete.

## Parked and future work

[`project/deferred_questions.md`](../deferred_questions.md) is the maintained list. Its live entries are:

| Item | State | Return condition |
|---|---|---|
| Native glyph mode | Parked | Daniel chooses to resume exploration of Phi's one intended native script. |
| Spoken source material and code-switching | Open design question | Live conversational examples make the current outside-syntax boundary inadequate. Do not reintroduce guest or exact frames. |
| Sexual and reproductive anatomy | Queued scenario-led vocabulary effort | Begin as its own respectful corpus and vocabulary project, not as an unnoticed extension of Medical vocabulary. |
| Legacy vocabulary prose audit | Active | Complete the 36 base entries, corpus retrofit, and 209 module entries. |
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
