# Phi Development Roadmap

This document reconstructs the long improvement plan for Phi as a status-tracked roadmap. It is the execution view of the project: `canon.md` says what Phi is, `documents/development_log.md` records accepted decisions, release manifests say what shipped, and this roadmap says what remains to be done.

The roadmap is written for one maintainer. It uses no RFC queue, voting process, fixed release calendar, or imaginary community roles. Work that can be completed inside the repository is separated from work that requires elapsed time, recorded speech, another reader, or recurring speakers.

## North star

Bring Phi closer to being a values-explicit language in which a small community, including communities interested in solarpunk thought, can conduct sustained philosophical discussion without pretending that Phi is a neutral auxiliary language or that grammar guarantees ethical conduct.

Success would mean that speakers can:

- state and examine competing values rather than assuming that all desirable values harmonize;
- define, distinguish, support, challenge, revise, and withdraw claims;
- preserve names, testimony, technical facts, harmful terminology, and tradition-specific concepts without silently adopting them as core vocabulary;
- repair misunderstanding and separate comprehension from agreement;
- discuss ecological stewardship, commons, mutual aid, consent, accountability, accessibility, technology, and collective futures with enough precision for disagreement;
- use careful or conversational pronunciation without losing the language's contrasts;
- learn from materials whose difficulty and effects are described honestly;
- influence future development through observed use rather than being recruited as evidence for claims already decided.

## Non-goals

- Turning Phi into an international auxiliary language.
- Making Phi contain every outside artifact instead of acknowledging source material outside the language.
- Eliminating ordinary ambiguity, shared names, dialect, repair, or variation.
- Claiming that Phi makes speakers peaceful, rational, mindful, sustainable, or culturally neutral.
- Coining a core root whenever an English word lacks a one-word equivalent.
- Renaming crowded vocabulary from automated distance scores alone.
- Building public governance before recurring users make it useful.
- Treating publication, audience size, or growth as proof that the language works.

## Status vocabulary

| Status | Meaning |
|---|---|
| **DONE** | Implemented, documented, and verified at the level the item claims. |
| **PARTIAL** | A useful artifact or baseline exists, but the stated outcome is not complete. |
| **NEXT** | The current recommended work package. It can begin without another prerequisite. |
| **READY** | Specified and unblocked, but not the current work package. |
| **OPTIONAL** | Available for practice or observation, but not required for another roadmap item. |
| **PENDING** | Specified, but waiting for one or more roadmap prerequisites. |
| **EVIDENCE** | Repository preparation may be complete, but the outcome requires elapsed time or observations from actual use. |
| **DEFERRED** | Intentionally postponed until the stated trigger occurs. |

An item is not **DONE** merely because a protocol, prompt, or script exists. A listening protocol with no recordings is **READY**; a language change waiting on those recordings is **PENDING**; a learner study with no learners is **EVIDENCE**.

## Current snapshot

| Workstream | Status | Current position |
|---|---|---|
| Purpose, scope, and solo governance | **DONE** | Philosophy-first scope and honest-claims policy are canonical. |
| Source-material interoperability | **DONE** | Unassimilated source material remains outside Phi passages; active teaching and tooling no longer parse guest or exact frames. |
| Productive proper names | **DONE** | `ne` licenses validated Phi-form onyms of two, three, or four syllables. |
| Three-syllable lexical ceiling | **DONE** | All 112 inherited four-syllable entries have replacements, and the validator permits no lexical exception. |
| Philosophical capability | **PARTIAL** | Matrix, repair conventions, and fifteen test dialogues exist; several operations remain gaps. |
| Solo evaluation | **READY** | Structural checks are complete; choice, paraphrase, transformation, and repair trials remain available after the breaking migration. |
| Speech and listening evidence | **READY** | Audit tooling and protocols exist; recordings and perception results do not. |
| Evidence-led semantic growth | **PARTIAL** | All eight active profiles have completed first vocabulary passes; later use may deepen them or justify another profile. |
| Practice and domain profiles | **DONE** | Eight active profiles are established vocabulary modules with speaker chapters, and further possibilities remain recorded separately. |
| Original Phi corpus | **PARTIAL** | Fifteen philosophical dialogues exist, and the literary shelf has completed its after-state review. Scenarios, dialogues, and teaching texts remain; sustained essays and spontaneous transcripts do not yet exist. |
| Learner and community evidence | **EVIDENCE** | Materials exist, but there is no recorded outside learner or recurring speaker evidence. |
| Public governance and print publication | **DEFERRED** | Reconsider after recurring use and stable evidence-led development. |

## Phase 0: Honest foundation and stewardship

**Objective:** Make Phi's purpose explicit, remove unsupported promises, and give one maintainer a lightweight way to record consequential decisions.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| FND-01 | **DONE** | Classify Phi as a philosophy-first artlang/engineered contemplative practice, not an auxlang. | `documents/language_assessment.md`; `documents/development_log.md` D001 | Revisit only if actual use changes the project's purpose. |
| FND-02 | **DONE** | Replace deterministic claims about peace, cognition, pace, precision, neutrality, and ease with design intentions or hypotheses. | `canon.md`; revised manual and philosophy documents | Future claims continue to identify their evidence level. |
| FND-03 | **DONE** | Establish a solo-maintainer decision record rather than an RFC process. | `documents/development_log.md` D002 | Every consequential change records rationale and consequences. |
| FND-04 | **DONE** | Establish verified release manifests and CI-backed internal consistency. | `documents/releases/phi_2026_1.md`; `documents/releases/phi_2026_2.md`; `.github/workflows/validate.yml` | Every release states what machine checks do and do not establish. |
| FND-05 | **DONE** | Reconstruct the long plan as a status-tracked roadmap. | This document | Update statuses and evidence links in the same PR as future roadmap work. |

## Phase 1: Source-material interoperability

**Objective:** Preserve identity, precision, quotation, and analytically necessary source material without pretending that outside strings occupy Phi syntax or work in every Phi writing mode.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| EXT-01 | **DONE** | Remove adapted guest frames from current Phi. | D003 superseded by D012; boundary entries and parser removed | Recurring useful concepts become vocabulary or transparent expressions; temporary adaptations do not become a third lexical class. |
| EXT-02 | **DONE** | Remove exact opaque frames from current Phi. | D004 superseded by D012; mixed-script rendering removed | Exact artifacts remain in their source medium rather than breaking Phi script parity. |
| EXT-03 | **DONE** | Establish source-material separation and ethical reporting policy. | Canon ruling and `documents/word_shape_and_external_boundaries.md` | Phi may point to, translate, and analyze a separately preserved source without importing its grammar or claiming to exhaust it. |
| EXT-04 | **DONE** | Simplify validation, glossing, HTML generation, Tengwar rendering, and phonetic auditing. | Current scripts and whole-inventory non-content tests | Tooling accepts Phi text only and blocks lexical reassignment of the four historical boundaries. |
| EXT-05 | **DONE** | Replace frame teaching with source-material practice. | Manual chapter 24 and source-material pamphlet | Examples keep Phi passages and source artifacts visibly separate. |
| EXT-06 | **OPTIONAL** | Human choice exercise across core vocabulary, modules, transparent expressions, productive names, translation, and separate source presentation. | `documents/solo_evaluation_tasks.md` section 2 | Record cases where the intended boundary or referent remains unclear and revise teaching where useful. |
| EXT-07 | **EVIDENCE** | Outside-reader interpretation of source separation as honest scope rather than stigma or approval. | No outside result yet | Collect qualitative responses from consenting readers if Phi gains other users. |

## Phase 2: Productive identity and naming

**Objective:** Let people and communities retain or choose usable Phi-form names without semantic reassignment while leaving non-Phi preferred forms intact outside Phi passages.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| NAM-01 | **DONE** | Redefine `ne` as a proper-designation marker rather than a personhood marker. | `canon.md`; naming pamphlet | Applies consistently to people, animals, places, communities, works, events, and artifacts. |
| NAM-02 | **DONE** | Productive Phi-form onyms of two, three, or four syllables with duplicate syllables prohibited. | `scripts/name_forms.py`; name-form regression tests | Charter remains synchronized across canon, teaching, and validator. |
| NAM-03 | **DONE** | Exclude every current non-content lexicon form from productive onym use. | `validate_examples.py name FORM`; whole-inventory regression test | CI fails if any current function or other non-content entry becomes acceptable as a name. |
| NAM-04 | **DONE** | Preserve content-word names, retired-content names, productive onyms, separate source names, and bearer authority. | Naming pamphlet and canon | Name use gives a retired form no gloss, no adaptation is assigned against a bearer's preference, and a preferred source form is not forced into Phi phonology. |
| NAM-05 | **READY** | Repeated-name narrative trial using `ne` plus a bearer-approved onym. | Solo evaluation name prompts | Write and read a short narrative with at least ten mentions; record burden and ambiguity. |
| NAM-06 | **EVIDENCE** | Test shared names, changed names, multi-part names, and preferred forms with actual users. | No outside result yet | Record whether clarification conventions suffice before adding more name grammar. |

## Phase 3: Philosophical reasoning and vocabulary

**Objective:** Develop connected philosophical expression, useful optional terminology, and clear repair practices without adding incompatible grammar.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| PHL-01 | **DONE** | Capability matrix with demonstrated, compositional, external-bridge, and gap classifications. | `documents/philosophical_capability_matrix.md` | Use the matrix as a descriptive reference rather than an admission gate. |
| PHL-01A | **DONE** | Establish Philosophical Reasoning as Phi's first optional vocabulary module. | Profile, 18 complete module entries, four base words established with the pass, generated module index, speaker-facing Part VII chapter, regression corpus, and six authored transformations | Revise the vocabulary through actual writing and discussion when a compound or coined term feels inadequate. |
| PHL-02 | **DONE** | Fifteen original regression dialogues covering ecological tradeoff, repair/replace, evidential revision, external-language critique, definition under pressure, two measurement/systems challenges, bodily-care decision-making, two access cases, commons allocation, shared-infrastructure accountability, two ecological-systems challenges, and work-sharing during a craft repair. | `documents/philosophical_test_corpus.md` | Existing dialogues remain validated and revisable. |
| PHL-03 | **PARTIAL** | Repair conventions for clarification, error, withdrawal, disagreement, turn handoff, waiting, consent, refusal, and source requests. | `documents/grammar/philosophical_conversation.md` | Move conventions to demonstrated only after unscripted use succeeds repeatedly. |
| PHL-04 | **PARTIAL** | Demonstrate definition, truth, evidence, conditionals, consequence, example, summary, agreement, agency, and revision in connected text. | Demonstrated rows in the capability matrix | Add at least one independent original passage per operation, not merely a reference example. |
| PHL-05 | **PARTIAL** | Express cause versus reason, retraction, competing goods, responsibility, uncertainty, and suspended judgment. | Base vocabulary supplies `remotha` reason; Philosophical Reasoning adds `whamoi`, `norethi`, `soneho`, and `manawi`; Commons adds `naseru` obligation and `lothoni` accountability; the corpus provides material for use | Write original passages using the vocabulary and revise any term or composition that feels unclear or unnatural. |
| PHL-06 | **PARTIAL** | Express logical validity, contradiction, consistency, counterexample, systems, feedback, and emergence. | Philosophical Reasoning supplies the logical vocabulary, and Systems and Shared Infrastructure supplies system, state, dependency, control, and feedback terminology; emergence remains thinner | Use the terms in connected philosophical and systems writing, then add emergence or other vocabulary where desired. |
| PHL-07 | **READY** | Distinguish understanding, agreement, endorsement, and willingness to continue. | Repair conventions | Complete unscripted dialogues whose successful ending includes disagreement or suspension. |
| PHL-08 | **EVIDENCE** | Determine whether other speakers recover intended propositions and distinctions. | No outside result yet | Use blind paraphrase and dialogue tasks with consenting readers; report losses without blaming learners. |

## Phase 4: Solo evaluation cycle

**Objective:** Use disciplined self-testing to find internal weaknesses without presenting maintainer performance as learner evidence.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| EVA-01 | **DONE** | Structural regression for lexicon, examples, productive names, retired forms, generated references, and rendering. | CI and release verification | Continue on every relevant change. |
| EVA-02 | **OPTIONAL** | Source-material and name-choice prompt set. | Protocol in `documents/solo_evaluation_tasks.md` | Use the prompts when they would improve teaching or reveal a practical burden; no delay is required. |
| EVA-03 | **DONE** | Source-material separation and rendering trial with script, case, notation, URL, and HTML-looking material. | Source Material teaching and generated-site inspection | Repeat whenever rendering architecture changes. |
| EVA-04 | **OPTIONAL** | Open-reference philosophical paraphrase. | Phi-only transformation packet with a separate key | A learner who has not seen the key may work through a prompt immediately with or without the lexicon; treat difficulty as learning feedback, not a gate on vocabulary. |
| EVA-05 | **OPTIONAL** | Argument transformation practice. | Six controlled prompts cover premise and conclusion variation for three baseline dialogues; proposition key exists | Use or expand the packet when it serves learning, writing, or revision; no delay is required. |
| EVA-06 | **OPTIONAL** | Conversation-repair practice. | Repair reference and authored clarification, evidence-challenge, retraction, and understood-disagreement probes | Use the probes during dialogue practice and record only observations that are useful to future teaching or revision. |
| EVA-07 | **READY** | Productive-name burden trial. | NAM-05 | Test repeated onym use while preserving the source name separately and without changing the referent. |
| EVA-08 | **READY** | Consolidated evaluation record. | Result table in `documents/solo_evaluation_tasks.md` | Add dated results, material, failures, and follow-up; never replace a pending row with an undocumented impression. |

## Phase 5: Speech, phonology, and listening

**Objective:** Preserve a clear reference pronunciation while designing for real accents, conversational tempo, and perceptual evidence.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| SPH-01 | **DONE** | Separate careful reference pronunciation from accepted conversational and accented variants. | Canon pronunciation ruling; phonetics documents | New teaching avoids moralizing accent or tempo. |
| SPH-02 | **DONE** | Phoneme-aware, feature-weighted neighbor audit and reproducible baseline. | `scripts/audit_phonetic_neighbors.py`; phonetic baseline | Baseline regenerates exactly and remains advisory. |
| SPH-03 | **DONE** | Rename gate requiring repeated observed confusion rather than distance alone. | `documents/listening_audit.md` | No discretionary or collision-driven rename bypasses the gate; an independently accepted structural migration records and validates its separate reason. |
| SPH-04 | **READY** | Maintainer ABX recordings for high-priority function pairs. | Listening-audit protocol and prompt generator | Record careful and conversational sessions on three nonconsecutive days, in quiet and moderate noise. |
| SPH-05 | **READY** | Record observations and replay/confidence data. | Pending observation table | Fill actual trials for valid productive names, current-function rejection, and prioritized dense pairs. |
| SPH-06 | **EVIDENCE** | Outside-listener results across accents and language backgrounds. | No outside result yet | Begin with function words, productive names, current-function rejection, and dense pairs; preserve consent and keep raw voice private by default. |
| SPH-07 | **EVIDENCE** | Learner-facing reference recordings and accepted-variation examples. | No curated audio set yet | Publish only reviewed recordings whose speaker consent and purpose are recorded. |
| SPH-08 | **DEFERRED** | Broad collision-driven lexical renaming campaign. | Explicitly excluded from Phi 2026.1 | Reconsider only after repeated, high-impact perceptual confusion survives careful-production review; the accepted three-syllable migration is a separate structural change. |

## Phase 6: Semantic growth and optional modules

**Objective:** Expand Phi according to its maintainer's values and intended uses, using transparent compounds where they help and confident coinage where a domain benefits from dedicated vocabulary.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| SEM-01 | **DONE** | Establish the coinage quality protocol: compare composition and coinage, choose freely, then require complete semantics, schema, sound, examples, and references. | Development protocol and eight completed vocabulary passes | Apply the same quality standard without treating it as an external burden of proof. |
| SEM-01A | **DONE** | Develop practice and domain profiles as optional lexical organization under one grammar. | Eight established profiles with 244 optional roots, 352 memberships, generated indexing, speaker chapters, and sixteen base words established through profile passes | Revise an established profile through use, or add another only when its organization would help. |
| SEM-01B | **DONE** | Record the intended profile catalogue. | `documents/modules/README.md`; eight active profiles and preserved future explorations | Add another profile when its organizational purpose is clear; no audience or external evidence gate is required. |
| SEM-01C | **IN PROGRESS** | Revisit active Phi texts after the current module set and classification reviews are complete. | The [active text corpus review](active_text_corpus_review.md) records completed reviews of all twelve literary works, including three close translations and the full nine-work transmutation shelf | Inventory scenarios, dialogues, and teaching texts; repair accidental loss and stale vocabulary without rewriting before-state evidence. |
| SEM-01D | **DONE** | Assess genuine multi-module vocabulary membership after all current modules are established. | Complete overlap assessment; 77 shared roots, 137 roots with one module, thirteen promoted to base vocabulary, regenerated indexes, and corrected profile and speaker counts | Reopen the assessment when later vocabulary or sustained use exposes another genuine learning-path overlap. |
| SEM-01E | **DONE** | Review base vocabulary for older roots whose lexical center belongs in an existing module. | Complete base-placement assessment; thirty roots receive 35 memberships, 789 content roots remain base, and all generated and speaker-facing counts agree | Reopen placement when new modules give an older base word a genuine specialist home or when use shows that a classified word belongs in general study. |
| SEM-02 | **PARTIAL** | Map weak modern domains: technology, science, government, law, work, disability, reproductive health, sexuality, and institutions. | Assessment, survey, eight established vocabulary modules, two access scenarios, and work and care scenarios | Test the Work, Medical, Accessibility, and Household modules beyond their source scenarios, inhabited-place heat and cooling, and a standing institution outside councils while keeping sensitive domains scenario-gated. |
| SEM-03 | **PARTIAL** | Solarpunk philosophical scenario corpus. | Original regression corpus and the established Ecological and Commons modules now cover ecology, energy, care, consent, accessibility, allocation, collective procedure, authority, accountability, watershed evidence, habitat, material return, shared craft, work refusal, and repair safety | Continue with mutual aid, institutional failure beyond one council, climate and heat, and conflicting visions of a good future. |
| SEM-04 | **READY** | Tradition-specific philosophy protocol. | Separate-source-first and explain-in-Phi pattern in the capability matrix | Test several traditions without claiming one Phi paraphrase exhausts the source concept. |
| SEM-05 | **DONE** | Complete implementation standard for each new word. | Development protocol, 244 optional entries across all eight established modules, and sixteen base words established through the same profile passes | Require full schema fields, bounded scope, semantic contrasts, examples, phonetic checks, appropriate core or module placement, and generated references. |
| SEM-06 | **PARTIAL** | Case-by-case review of core refusals. | Canon refusal and source-material rulings | Reconsider any refusal that obstructs care, identity, consent, safety, testimony, or analysis; preserve necessary source material separately whether the concept is admitted or retained outside the lexicon. |
| SEM-07 | **DONE** | First philosophical vocabulary expansion. | 18 Philosophical Reasoning module words, four base words established with the pass, and Part VII teaching chapter | Continue through original writing and future vocabulary passes; no delayed evaluation prerequisite remains. |
| SEM-07A | **DONE** | First systems and shared infrastructure vocabulary expansion. | 24 Systems and Shared Infrastructure module words, base `phelure` store, retained compositions, generated index, and Part VII teaching chapter | Use the module in original technical and infrastructure writing and revise any term or composition that feels inadequate. |
| SEM-07B | **DONE** | First ecological systems and material life vocabulary expansion. | 27 Ecological Systems and Material Life module words, three base words established with the pass, retained compositions, generated index, and Part VII teaching chapter | Use the module in original ecological and material writing and revise any term or composition that feels inadequate. |
| SEM-07C | **DONE** | First commons and collective governance vocabulary expansion. | 27 Commons and Collective Governance module words, three base words established with the pass, retained compositions, generated index, and Part VII teaching chapter | Use the module in original governance and institutional writing and revise any term or composition that feels inadequate. |
| SEM-07D | **DONE** | First work, craft, and repair vocabulary expansion. | 28 Work, Craft, and Repair module words, two base words established with the pass, retained compositions and source boundaries, generated index, and Part VII teaching chapter | Use the module in original work, learning, repair, and labor writing and revise any term or composition that feels inadequate. |
| SEM-07E | **DONE** | First medical and bodily care vocabulary expansion. | 30 Medical and Bodily Care module words, shared-core `lesawi` consent, retained compositions and source boundaries, generated index, and Part VII teaching chapter | Use the module in original care, recovery, intervention, and public-health writing and revise any term or composition that feels inadequate. |
| SEM-07F | **DONE** | First accessibility and participation vocabulary expansion. | 30 Accessibility and Participation module words, shared-core `sowelu` disabled, retained compositions and source boundaries, generated index, and Part VII teaching chapter | Use the module in routes, communication, timing, support, and collective participation, then revise any term or composition that feels inadequate. |
| SEM-07G | **DONE** | First household and daily life vocabulary expansion. | 30 Household and Daily Life module words, shared-core `mirewu` private, retained core coverage and compositions, generated index, and Part VII teaching chapter | Use the module in solitary and shared dwellings, meal preparation, upkeep, visits, and domestic-work disagreements, then revise any term or composition that feels inadequate. |
| SEM-08 | **DONE** | Enforce a universal three-syllable lexical ceiling. | D013 and D016; completed 112-row migration ledger; unconditional validator rule | No lexicon entry exceeds three syllables, and four-syllable forms need no individual retirement record. |
| SEM-08A | **DONE** | Replace 19 four-syllable base-vocabulary forms. | Migration ledger scope `base`; synchronized active corpus | Reopen only if an active use of an old form is found. |
| SEM-08B | **DONE** | Replace 10 Philosophical Reasoning forms. | Completed ledger scope and regenerated speaker references | Reopen only if an active use of an old form is found. |
| SEM-08C | **DONE** | Replace 24 Systems and Shared Infrastructure forms. | Completed ledger scope and phonetic-neighbor baseline | Reopen only if an active use of an old form is found. |
| SEM-08D | **DONE** | Replace 30 Ecological Systems and Material Life forms. | Completed ledger scope, scenarios, profile, and generated reference | Reopen only if an active use of an old form is found. |
| SEM-08E | **DONE** | Replace 29 Commons and Collective Governance forms and close the migration. | Completed ledger scope; validator has no long-form exception | Reopen only if an active use of an old form is found. |

### Default coinage checklist

A new philosophical or module word should normally satisfy all of the following:

1. Check whether an existing word already carries the intended meaning accurately.
2. Consider whether a transparent compound makes the idea clearer than a new root.
3. Coin freely when the concept deserves lexical presence or a compound would be cumbersome, ambiguous, or aesthetically wrong for Phi.
4. Give the proposal a bounded meaning and explicit contrasts with neighboring words or constructions.
5. Fill every canonical schema field accurately, including natural grammatical examples and appropriate semantic tags or module membership.
6. Run structural, phonetic-neighbor, gloss, reference-generation, and documentation checks.

This checklist protects implementation quality. It does not require external approval, repeated failure, or proof that no alternative word could have been avoided.

## Phase 7: Original corpus and teaching

**Objective:** Make original Phi use, especially disagreement and inquiry, the primary evidence for future development while keeping the learning path honest and usable.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| COR-01 | **DONE** | A validated shelf of three close translations, eleven transmuted works, and extensive teaching examples; two fables appear in both forms. | `pamphlets/`; manual; primer | Keep every rendering labeled by method and continue to distinguish deliberate transmutation choices from Phi's general expressive capacity. |
| COR-02 | **DONE** | Fifteen original philosophical regression dialogues. | `documents/philosophical_test_corpus.md` | Preserve as baseline tests rather than polished doctrine. |
| COR-03 | **READY** | Sustained original philosophical essays in Phi. | Depends on PHL-05/06 scenario selection | Write at least three essays with claims, objections, revision, and unresolved tension; maintain proposition and gap logs. |
| COR-04 | **READY** | Dialogue set whose successful outcome is disagreement, suspension, or revised framing rather than consensus. | Repair conventions | Add validated dialogues and re-run repair tests. |
| COR-05 | **EVIDENCE** | Transcripts or reconstructions of spontaneous Phi conversation. | No spontaneous corpus yet | With consent, preserve normalized text and an error/repair log; do not publish raw voice by default. |
| COR-06 | **PARTIAL** | Corpus-attestation data for phonetic and lexical decisions. | Phonetic audit counts documentation examples | Separate authored Phi usage from mentions in explanation as the corpus grows. |
| PED-01 | **DONE** | Complete primer, reference manual, pamphlet shelf, quick reference, and generated explorer. | `primer/`; `manual/`; `pamphlets/`; `web/` build | Keep generated outputs synchronized. |
| PED-02 | **DONE** | Advanced teaching for source-material boundaries and productive names. | Manual chapter 24 and relevant pamphlets | Maintain exercises and answers as rules evolve. |
| PED-03 | **PARTIAL** | Claims about learning burden aligned with actual grammar. | Revised introductory and manual prose | Continue auditing “one rule,” speed, and ease language. |
| PED-04 | **EVIDENCE** | First complete outside learner walkthrough. | No result yet | Record chapter time, errors, questions, abandoned points, and prior language background. |
| PED-05 | **EVIDENCE** | Curriculum pacing and retention evidence. | No result yet | Re-test selected material after a delay; revise ordering before adding explanations. |
| PED-06 | **READY** | Maintainer-as-learner regression pass after a blind interval. | Existing curriculum | Complete the primer exercises without consulting answers and log friction without generalizing to all learners. |
| PED-07 | **EVIDENCE** | Accessibility review for visual, auditory, cognitive, and motor needs. | Established vocabulary module, speaker chapter, and two scripted scenarios exist; no affected-user review yet | Invite affected users to identify barriers; prioritize practical access over aesthetic doctrine. |

## Phase 8: Community practice and cultural accountability

**Objective:** Let community values emerge through voluntary practice and feedback rather than claiming that the current five pillars represent everyone interested in solarpunk or philosophical language.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| COM-01 | **DONE** | State Phi's values as explicit design commitments rather than neutrality. | Language guide, canon, revised philosophy documents | Continue naming tradeoffs and burdens. |
| COM-02 | **PARTIAL** | Community practice suggestions for pairs, circles, artifacts, and collaborative transmutation. | Manual chapter 23 | Treat as invitations, not evidence of an existing community. |
| COM-03 | **EVIDENCE** | Community-of-two pilot. | No recurring pair documented | Two people use Phi repeatedly for learning, original discussion, and repair; record consented qualitative feedback. |
| COM-04 | **EVIDENCE** | Small-circle solarpunk discussion pilot. | Depends on COM-03 and core evaluation | Test values conflict, decision-making, access, and disagreement rather than ceremonial agreement alone. |
| COM-05 | **EVIDENCE** | Cultural interpretation review of Buddhist, solarpunk, pre-industrial, peace-linguistic, and aesthetic claims. | No multi-perspective review yet | Seek specific critique; remove borrowed authority and universalizing language where identified. |
| COM-06 | **EVIDENCE** | Feedback path that distinguishes grammar bugs, lexical gaps, identity harms, teaching friction, and preference. | Solo log exists; public path does not | Introduce only when people are actually submitting recurring feedback. |
| COM-07 | **DEFERRED** | Council, voting rules, community ratification, or formal standards body. | Development log deferred-infrastructure ruling | Reconsider after recurring speakers face decisions one maintainer should not make alone. |

## Phase 9: Public access, governance, and publication

**Objective:** Make Phi durable and accessible without allowing publication machinery to outrun language use.

This phase is adjacent to the linguistic improvement plan and follows the order recorded in `publishing.md`.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| PUB-01 | **DONE** | Web explorer, primer, manual, texts, and pamphlets build from repository sources. | `scripts/build_explorer.py` | Builds remain reproducible and safe. |
| PUB-02 | **DONE** | Public hosting and a canonical public URL. | `.github/workflows/pages.yml`; public URL in `README.md` | Keep deployment reproducible and update the documented URL if hosting changes. |
| PUB-03 | **DEFERRED** | Automated print/PDF pipeline from the same Markdown and lexicon sources. | Strategy in `publishing.md` | Begin after content and learner evidence stabilize enough for page design. |
| PUB-04 | **DEFERRED** | Circulated review PDF. | Depends on PUB-03 and outside readers | Gather corrections before physical production. |
| PUB-05 | **DEFERRED** | Physical publication. | Depends on a waiting audience, not projected demand | Print when the book is an artifact of existing use rather than its substitute. |
| GOV-01 | **DONE** | Versioned canon, development log, release manifests, CI, and post-merge branch hygiene. | Repository practice | Continue for every merged milestone. |
| GOV-02 | **READY** | Lightweight contribution and consent guidance for first outside participants. | Existing consent notes are task-specific | Write only before inviting contributions or collecting feedback. |
| GOV-03 | **DEFERRED** | Fixed release cadence and compatibility policy beyond current manifests. | No recurring downstream users yet | Introduce when other work depends on predictable releases. |

## Current execution sequence

The three-syllable lexical migration and literary-shelf review are complete. SEM-01C continues with scenarios, dialogues, and teaching texts; original philosophical use, evaluation, and speech work remain available alongside it.

### Completed work package 0: Three-syllable lexical migration

**Roadmap items:** SEM-08A through SEM-08E.

| Scope | Replacements |
|---|---:|
| Base vocabulary | 19 |
| Philosophical Reasoning | 10 |
| Systems and Shared Infrastructure | 24 |
| Ecological Systems and Material Life | 30 |
| Commons and Collective Governance | 29 |

All 112 replacements preserve the vocabulary schema and active uses under forms of no more than three syllables. The ledger records the old-to-new mappings, generated references and phonetic baselines agree with the current lexicon, and the validator now applies the ceiling without an exception list. Old four-syllable forms are absent from vocabulary by class rather than copied into the short-form retirement list.

### Work package A: Continue vocabulary module passes

**Roadmap items:** SEM-01A, SEM-02, SEM-05.

1. Select one of the remaining active profiles.
2. Inventory the domain concepts and the existing core words that already serve them.
3. Keep transparent compounds where their parts illuminate the concept.
4. Coin complete module entries wherever a dedicated word is useful, precise, or desirable.
5. Add a Part VII speaker chapter, regenerate module references, expose the module in the web lexicon, and run the full validation suite.

**Exit criterion:** the selected profile has a documented vocabulary pass, complete canonical entries, validated examples, generated indexing, and accessible speaker guidance.

### Work package B: Original Philosophical Reasoning use

**Roadmap items:** PHL-04 through PHL-07, COR-03, COR-04.

1. Choose a philosophical question worth exploring rather than a test constructed only to exercise vocabulary.
2. Write a sustained Phi argument or dialogue using the new module terms where they feel natural.
3. Include an objection, a response, revision or clarified scope, and either an unresolved tension or a reasoned conclusion.
4. Revise any word, definition, compound, or example that feels awkward in actual use.

**Exit criterion:** at least one original connected work uses the module naturally and records any vocabulary changes it prompted.

### Work package C: Optional reading and repair practice

**Roadmap items:** EVA-04 through EVA-06, PHL-03.

1. Select an unread prompt whose proposition key remains closed.
2. Read it immediately or later, with the grammar and lexicon available as needed.
3. Paraphrase or discuss it, then compare the result with the key.
4. Record useful learning friction separately from possible language ambiguity.
5. Use a clarification, evidence challenge, retraction, or understood disagreement when that would make the exercise worthwhile.

**Exit criterion:** optional; completed practice may improve teaching or revision but does not gate vocabulary development.

### Work package D: Later listening baseline

**Roadmap items:** SPH-04, SPH-05.

1. Generate fixed-seed ABX prompts.
2. Record careful and conversational versions on three nonconsecutive days.
3. Test quiet and moderate-noise conditions without visible spelling.
4. Enter trials, errors, replays, and confidence in the listening audit.
5. Open a discretionary or collision-driven rename candidate only if the existing rename gate is met.

**Exit criterion:** a prioritized function-word set has actual observation rows; automated scores alone trigger no rename.

### Work package E: First outside-reader packet

**Roadmap items:** PHL-08, SPH-06, PED-04, COM-03.

Prepare this when an outside reader exists and participation would be useful; solo tasks are not a prerequisite.

The packet should contain a short consent statement, pronunciation reference, a small primer segment, one source-material boundary task, one philosophical dialogue, one repair task, and open-ended questions. Collect language background and qualitative observations. Do not claim percentages from a handful of participants.

**Exit criterion:** at least one outside reader completes the packet, their consent and conditions are recorded, and the roadmap distinguishes their observation from maintainer inference.

## Milestone view

These labels describe logical milestones, not promised dates.

| Milestone | Status | Included work |
|---|---|---|
| Phi 2026.1: external register and honest scope | **DONE** | FND-01 through FND-04; EXT-01 through EXT-05; initial PHL and SPH tooling. |
| Phi 2026.2: productive names | **DONE** | NAM-01 through NAM-04 and strict name validation. |
| Three-syllable lexical migration | **DONE** | SEM-08A through SEM-08E; 112 replacements and an unconditional lexical ceiling. |
| Solo evidence baseline | **READY** | Work packages A through D. |
| First evidence-led philosophical expansion | **PENDING** | Work package E and one narrowly justified release. |
| Outside-reader pilot | **EVIDENCE** | Work package F. |
| Recurring community practice | **EVIDENCE** | COM-03 through COM-06. |
| Public governance and print | **DEFERRED** | COM-07, PUB-03 through PUB-05, GOV-03. |

## Roadmap maintenance rules

1. Update this file in the same change that completes, defers, or materially redefines an item.
2. Link evidence to a repository artifact or dated result record; conversation memory alone is not completion evidence.
3. Keep at most one solo work package marked **NEXT**.
4. Do not mark an empirical item **DONE** when only its tooling or protocol is complete.
5. Record accepted language decisions in `documents/development_log.md`; do not turn this roadmap into a second canon.
6. Add release verification to a release manifest, not to every roadmap row.
7. Split new work rather than expanding a work item until its exit criterion becomes meaningless.
8. Preserve negative results. A failed construction, ambiguous prompt, or abandoned coinage is evidence.
9. Move governance and publication forward only when their stated trigger is real.
10. After a roadmap PR merges, perform the customary local and remote branch cleanup.

## Completion condition for the long plan

The long plan is not complete when every gap has a word. It is complete when Phi has demonstrated a repeatable development cycle:

1. original use exposes a specific failure;
2. solo evaluation reproduces and describes it;
3. the smallest justified change is made or the source material remains separately preserved;
4. teaching and tooling agree with the decision;
5. the motivating task improves on re-test;
6. outside users can report different results without those results being absorbed into a predetermined claim;
7. recurring speakers have a credible path to influence decisions that affect them.

At that point Phi will still be unfinished, as any living language is, but the original improvement plan will have achieved its purpose: development will be driven by philosophical use, honest evidence, and community accountability rather than by the completeness of a private design.
