# Phi near-term development plan

This document records the recommended sequence after the first ten isolated translation certifications and before further expansion of the public corpus. It is a near-term execution plan, not a new authority over the language. [`canon.md`](../canon.md) governs Phi, the [development roadmap](roadmap.md) governs the broader programme, the [translation certification register](translation_process_status.json) owns the live certification state, and the [deferred-questions ledger](deferred_questions.md) owns work that has deliberately been parked.

## Assessment

Phi no longer needs a search for major missing features. Its grammar and particle system are complete, its base and module vocabulary are broad, its teaching shelves are substantial, and its validators provide unusually strong structural checks. The useful work now is to make those accomplishments durable, finish the finite certification backlog without allowing it to consume the project, preserve continuity across the planned thirty-two chapters of *News from Nowhere*, and keep original Phi composition alongside translation.

A pending certification does not imply that a translation is poor. Several pending works have already received extensive source-fidelity and Phi-grammar review. Pending means only that the published version has not completed the newer isolated Phi-to-English process recorded in [How a Phi translation is made](../documents/reference/translation_process.md). The plan therefore uses evidence from a Morris pilot before deciding whether all existing chapters must be recertified before another chapter is written.

Community engagement is outside this plan. Phi can strengthen its language, corpus, tools, and private learning experience without preparing outreach, contribution governance, adoption material, or claims about other speakers.

## Working principles

- Close obsolete compatibility paths once a migration is demonstrably complete; a schema that still accepts the old form can silently recreate finished work.
- Make machine guarantees match public claims where the repository has enough source evidence to do so.
- Record series-wide translation choices once, in a source-to-Phi continuity record, rather than expecting chapter files or conversational memory to carry them unaided.
- Keep the certification register authoritative for current counts and states instead of copying figures into planning prose.
- Certify new translations as part of creating them so the pending queue only shrinks.
- Use translation to test expressive fidelity and original Phi writing to test how the language organizes thought without an outside author supplying the discourse.
- Reopen grammar, particles, or the module system only for a demonstrated language-level defect and an explicit maintainer decision, not as ordinary corpus development.

## Recommended sequence

| ID | Status | Work package | Completion gate |
|---|---|---|---|
| NTP-01 | **DONE** | Close the migrated vocabulary schema | Current entries pass a schema that requires the target prose fields and no longer accepts the retired fields. |
| NTP-02 | **NEXT** | Add independent source-reconstruction checking | At least the locally stored Morris source can be compared mechanically with each chapter's ordered citation stream. |
| NTP-03 | **READY** | Establish the *News from Nowhere* continuity record | Recurring source-to-Phi choices have one maintained home that is excluded from Phi-to-English derivation. |
| NTP-04 | **READY** | Reconcile stale project records | The roadmap, development protocol, and deferred records describe the actual completed corpus and closed grammar boundary. |
| NTP-05 | **READY** | Finish the short-work certification queue | The present Gibran, Taoist, and Buddhist short works have completed the isolated process and the generated register passes. |
| NTP-06 | **PENDING** | Certify *News from Nowhere* chapter 1 as a pilot | The chapter has a current certification record and its findings have been classified as local or series-wide. |
| NTP-07 | **PENDING** | Choose the Morris backlog route from pilot evidence | The decision and its evidence are recorded before either blocking chapter 7 or interleaving old and new chapters. |
| NTP-08 | **PENDING** | Continue the Morris translation | Every newly written chapter completes certification in its creation effort, with continuity checks at regular narrative checkpoints. |
| NTP-09 | **READY** | Add another sustained original Phi work | One Phi-first work exercises several under-demonstrated philosophical capabilities in connected discourse. |
| NTP-10 | **LATER** | Create a release checkpoint and optional reading modes | Reconsider after the chosen Morris checkpoint and the present finite certification queue. |

## NTP-01: Close the vocabulary schema

The lexicon migration was complete while [`vocabulary/schema.json`](../vocabulary/schema.json) still permitted the deprecated `concept` and `grammatical_notes` fields and allowed old alternatives to `articulatory_notes` and structured `examples`. That tolerance had changed from a migration aid into a regression path.

This package requires `articulatory_notes` and `examples` directly, removes the two retired properties and their fallback branches, replaces tests that prove legacy acceptance with tests that prove legacy rejection, and revises the development and voice references that described migration tolerance. It does not rewrite vocabulary prose or change any word. Completion means the complete inventory and all schema, example, sentence, generation, and site checks pass under the stricter contract.

Completed under D115. The target fields are direct requirements, the retired properties are invalid, and the migration report remains as regression evidence rather than a compatibility path.

## NTP-02: Verify source reconstruction independently

The certification register verifies unit counts, digests, aligned layers, and recorded normalized source counts. It does not by itself compare an ordered citation stream with an independently stored source witness. That leaves a gap between a strong process and the strongest reading of the public reconstruction claim.

Begin with *News from Nowhere*, whose source witness is stored in the repository. A small manifest should identify the source file, citation label, selected chapter boundary, and normalization rule. A checker should join the chapter's decoded citations in order and compare the result character for character with the selected normalized source. It should report a missing span, duplicated span, reordering, or altered text directly. The design may later support other works with independently stored witnesses, but it should not pretend that every source has one when it does not.

## NTP-03: Preserve Morris continuity

Create `project/news_from_nowhere_continuity.md` when this package begins. It should be an internal source-to-Phi record, not a literary introduction or certification log.

The record should contain recurring characters and their settled Phi onyms, recurring places and source-name treatment, repeated social and material concepts and their chosen Phi renderings, narrator and evidential conventions, quotation and continuing-speech conventions, rejected renderings likely to recur, unresolved continuity questions, and brief checkpoint findings. Each entry should be useful across chapters and should point to canon or a language decision where one governs the choice.

The record must not contain unit-by-unit audit history, copied source passages, glosses, derived English, certification evidence, or general project planning. It is available during source-to-Phi work and cross-chapter review. It is forbidden input to a fresh Phi-to-English context, just like filenames, titles, source summaries, and task history.

Start with Markdown. A machine-readable schema would add maintenance without demonstrated benefit; introduce one only if actual drift shows that prose cannot carry the record reliably.

## NTP-04: Reconcile project records

The broad roadmap and protocol should be corrected rather than replaced with another general roadmap. The existing original corpus now includes a sustained dialogue and three reviewed philosophical essays, so the corresponding corpus milestone and snapshot need reassessment. Obsolete exact vocabulary counts should be removed from prose where arithmetic is not the subject. The development protocol's instructions for adding particles and constructions should become an amendment boundary: Phi's grammar and particles are closed unless a demonstrated defect and explicit maintainer decision reopen canon.

This is a focused state correction. It should not trigger a general documentation audit, prose-polishing pass, or handoff rewrite.

## NTP-05: Finish the short-work queue

After the hardening interval, certify the remaining shorter translations in this order:

1. Gibran, *On Giving*.
2. Gibran, *On Work*.
3. *Tao Te Ching* selections.
4. *Heart Sutra*.

This closes the finite non-Morris queue before the novel becomes the principal translation work. Do not add further Gibran selections during this interval. The machine-readable register and its generated ledger remain the authority if the queue changes.

## NTP-06 and NTP-07: Use chapter 1 as the Morris gate

Certify chapter 1 under the current isolated process, including independent source reconstruction and continuity review. Classify every substantive finding after the work is complete.

Choose immediate backfill when the pilot reveals a recurring construction error, systematic source loss, naming drift, a shared derived-English problem, or another defect likely to affect several existing chapters. In that case, certify chapters 2 through 6 before chapter 7 so the common fault is repaired once across a bounded corpus.

Choose interleaving when the pilot's findings are local and the earlier exhaustive reviews remain broadly sound. In that case, chapter 7 may proceed under certification from birth while chapters 2 through 6 are recertified at deliberate checkpoints. Pending status remains visible and honest; it is not hidden or relabelled as completion.

Record this ruling in the development log. Do not decide it in advance merely to preserve an older work order.

## NTP-08: Continue *News from Nowhere* without new debt

Every chapter from chapter 7 onward should complete source partition, source-to-Phi translation, Phi validation, freeze, anonymous Phi-to-English derivation, independent risk review, source reconstruction, status registration, and publication in the same chapter effort. A chapter should not be published as a new pending translation.

Run a cross-chapter continuity check after every three newly written chapters or at a natural narrative boundary, whichever comes first. Check names, recurring concepts, voice and evidential choices, continuing-speech framing, and registered vocabulary. If the check changes a frozen Phi unit, recertify only the affected unit under the ordinary invalidation rule and refresh the published digests.

## NTP-09: Keep original Phi alive

Translation shows whether Phi can carry another author's propositions. It cannot by itself show how Phi naturally arranges sustained thought. After the next Morris checkpoint, write one original Phi work that combines commons deliberation, ecological or material systems, responsibility, uncertainty, and unresolved disagreement. A discussion that ends without forced consensus would exercise several capabilities that remain compositional or lightly demonstrated in the [philosophical capability matrix](../documents/evaluation/philosophical_capability_matrix.md).

The work should begin in Phi, receive the established Phi-first review, and derive its English only from settled Phi. It should not be designed to satisfy every matrix row or used as a reason to coin an English-shaped list of abstractions. Actual compositional pressure should determine whether vocabulary work is needed.

## NTP-10: Later durability and reading work

After the certification and Morris checkpoint, consider a new release manifest that records the language and tooling state reached since Phi 2026.2. Also consider a reader control with `Phi only`, `Phi + gloss`, and `full apparatus` views so the certified shelf can serve private study as well as textual inspection. These are useful but should not interrupt schema closure, reconstruction checking, certification, or chapter work.

## Explicitly outside the near-term plan

- Community outreach, recruitment, adoption campaigns, public governance, and contribution processes.
- New grammar, particles, or incompatible module syntax without a demonstrated defect and explicit reopening of canon.
- New vocabulary modules merely to enlarge the inventory.
- Further Gibran expansion before the current translation queue and Morris pilot are settled.
- Speech and listening studies before the maintainer chooses to return to them.
- Another general roadmap, state-of-Phi essay, or planning layer that duplicates the records already maintained here.

## Completion of this plan

The plan has done its job when the schema enforces the completed vocabulary contract, stored Morris source coverage is checked independently, continuity survives chapter-by-chapter work, the short certification queue is closed, the Morris backlog follows a recorded evidence-based route, new chapters create no certification debt, and original Phi composition continues beside translation. At that point the broad roadmap should be reassessed and this document may be retired rather than extended indefinitely.
