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
- Making Phi cover every domain without marked external material.
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
| **PENDING** | Specified, but waiting for one or more roadmap prerequisites. |
| **EVIDENCE** | Repository preparation may be complete, but the outcome requires elapsed time or observations from actual use. |
| **DEFERRED** | Intentionally postponed until the stated trigger occurs. |

An item is not **DONE** merely because a protocol, prompt, or script exists. A listening protocol with no recordings is **READY**; a language change waiting on those recordings is **PENDING**; a learner study with no learners is **EVIDENCE**.

## Current snapshot

| Workstream | Status | Current position |
|---|---|---|
| Purpose, scope, and solo governance | **DONE** | Philosophy-first scope and honest-claims policy are canonical. |
| External interoperability | **DONE** | Guest and exact registers are canonical, taught, rendered, and validated. |
| Productive proper names | **DONE** | `ne` licenses validated two- through four-syllable Phi-form onyms. |
| Philosophical capability | **PARTIAL** | Matrix, repair conventions, and fifteen test dialogues exist; several operations remain gaps. |
| Solo evaluation | **NEXT** | Structural checks are complete; choice, paraphrase, transformation, and repair trials remain. |
| Speech and listening evidence | **READY** | Audit tooling and protocols exist; recordings and perception results do not. |
| Evidence-led semantic growth | **READY** | Gap-selection rules exist; no post-baseline expansion cycle has been completed. |
| Practice and domain profiles | **PARTIAL** | An experimental contract, five domain profiles, one shared-core practice profile, one cross-domain accessibility profile, and a recorded proposed-profile catalogue exist. The format still needs use evidence. |
| Original Phi corpus | **PARTIAL** | Fifteen philosophical dialogues exist; sustained essays and spontaneous transcripts do not. |
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

## Phase 1: External interoperability

**Objective:** Let Phi preserve identity, precision, quotation, and analytically necessary outside concepts without weakening the distinction between core choices and external material.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| EXT-01 | **DONE** | Adapted guest frame `hasha ... hasho`. | `canon.md`; complementizer reference; four lexicon entries | Guest payload remains pronounceable, bounded, and non-lexical. |
| EXT-02 | **DONE** | Exact opaque frame `patha ... patho`, including literal-closer escaping. | `canon.md`; `scripts/external_register.py` | Exact source material remains opaque and safely bounded. |
| EXT-03 | **DONE** | Nominal-atom syntax and ethical reporting policy. | Canon rulings on external syntax and reporting | Source grammar never silently enters Phi; provenance does not imply approval. |
| EXT-04 | **DONE** | Validator, gloss, HTML-escaping, and mixed-Tengwar support. | `scripts/validate_examples.py`; `scripts/tengwar.py`; external tests | CI continues to cover malformed, opaque, escaped, and injection-like payloads. |
| EXT-05 | **DONE** | Advanced teaching material. | Manual chapter 24; `pamphlets/external_register/` | Examples stay synchronized with canon and validation. |
| EXT-06 | **READY** | Human layer-choice trial across core composition, registered compounds, productive names, guest forms, and exact forms. | `documents/solo_evaluation_tasks.md` section 2 | Complete twenty shuffled prompts after a delay; record ambiguous cases and revise teaching before grammar. |
| EXT-07 | **EVIDENCE** | Outside-reader interpretation of the boundary as provenance rather than stigma or approval. | No outside result yet | Collect qualitative responses from multiple consenting readers with different backgrounds. |

## Phase 2: Productive identity and naming

**Objective:** Let people and communities retain or choose usable names without requiring semantic reassignment or permanent guest framing.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| NAM-01 | **DONE** | Redefine `ne` as a proper-designation marker rather than a personhood marker. | `canon.md`; naming pamphlet | Applies consistently to people, animals, places, communities, works, events, and artifacts. |
| NAM-02 | **DONE** | Productive two-, three-, or four-syllable Phi-form onyms with duplicate syllables prohibited. | `scripts/name_forms.py`; Phi 2026.2 release manifest | Charter remains synchronized across canon, teaching, and validator. |
| NAM-03 | **DONE** | Strictly reserve every listed non-content form from productive onym use. | `validate_examples.py name FORM`; whole-inventory regression test | CI fails if any non-content entry becomes acceptable as a standalone productive onym. |
| NAM-04 | **DONE** | Preserve content-word names, guest names, exact names, and bearer authority. | Naming pamphlet and canon | No adaptation is assigned against a bearer's preference. |
| NAM-05 | **READY** | Repeated-name narrative trial comparing `ne` plus onym with full guest framing. | Solo evaluation name prompts | Write and read a short narrative with at least ten mentions; record burden and ambiguity. |
| NAM-06 | **EVIDENCE** | Test shared names, changed names, multi-part names, and preferred forms with actual users. | No outside result yet | Record whether clarification conventions suffice before adding more name grammar. |

## Phase 3: Philosophical capability baseline

**Objective:** Determine what Phi can actually do in connected argument before adding vocabulary or discourse machinery.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| PHL-01 | **DONE** | Capability matrix with demonstrated, compositional, external-bridge, and gap classifications. | `documents/philosophical_capability_matrix.md` | Matrix remains the gate for philosophical additions. |
| PHL-01A | **PARTIAL** | Organize existing reasoning resources as a shared-core Philosophical Reasoning profile. | `documents/modules/philosophical_reasoning.md`; capability matrix; regression corpus | Complete the profile's argument transformations and repair test before proposing a reasoning extension. |
| PHL-02 | **DONE** | Fifteen original regression dialogues covering ecological tradeoff, repair/replace, evidential revision, external-language critique, definition under pressure, two measurement/systems challenges, bodily-care decision-making, two access cases, commons allocation, shared-infrastructure accountability, two ecological-systems challenges, and work-sharing during a craft repair. | `documents/philosophical_test_corpus.md` | Existing dialogues remain validated and revisable. |
| PHL-03 | **PARTIAL** | Repair conventions for clarification, error, withdrawal, disagreement, turn handoff, waiting, consent, refusal, and source requests. | `documents/grammar/philosophical_conversation.md` | Move conventions to demonstrated only after unscripted use succeeds repeatedly. |
| PHL-04 | **PARTIAL** | Demonstrate definition, truth, evidence, conditionals, consequence, example, summary, agreement, agency, and revision in connected text. | Demonstrated rows in the capability matrix | Add at least one independent original passage per operation, not merely a reference example. |
| PHL-05 | **PARTIAL** | Test compositional operations: cause versus reason, retraction, competing goods, responsibility, uncertainty, and suspended judgment. | Competing-goods and responsibility cases now exist in scenarios 11, 12, and 15; other operations and transformations remain | Transform the commons and craft-repair scenarios and record where priority, responsibility scope, competence, capacity, authority, and provisional acceptance are lost in paraphrase. |
| PHL-06 | **PARTIAL** | Test current gaps: logical validity, contradiction, consistency, counterexample, systems, feedback, and emergence. | Feedback cases in scenarios 6 and 7; ecological systems cases and exact terms with core analysis in scenarios 13 and 14 | Transform the ecology cases and test blind systems recovery; write independent logic and counterexample dialogues before proposing core forms. |
| PHL-07 | **READY** | Distinguish understanding, agreement, endorsement, and willingness to continue. | Repair conventions | Complete unscripted dialogues whose successful ending includes disagreement or suspension. |
| PHL-08 | **EVIDENCE** | Determine whether other speakers recover intended propositions and distinctions. | No outside result yet | Use blind paraphrase and dialogue tasks with consenting readers; report losses without blaming learners. |

## Phase 4: Solo evaluation cycle

**Objective:** Use disciplined self-testing to find internal weaknesses without presenting maintainer performance as learner evidence.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| EVA-01 | **DONE** | Structural regression for lexicon, examples, external frames, productive names, generated references, and rendering. | CI and release verification | Continue on every relevant change. |
| EVA-02 | **NEXT** | External-layer and name-choice prompt set. | Protocol in `documents/solo_evaluation_tasks.md` | Create twenty balanced prompts, delay, classify blind, and record ambiguity. |
| EVA-03 | **DONE** | Exact-payload safety trial with script, case, notation, URL, closer escaping, and HTML-looking material. | External-register tests and generated-site inspection | Repeat whenever rendering architecture changes. |
| EVA-04 | **READY** | Delayed philosophical paraphrase. | Solo task 5 | After a documented seven-day blind interval, paraphrase one dialogue and score lost/added propositions, evidentials, modality, negation, and participants. |
| EVA-05 | **READY** | Argument transformation. | Solo task 6 | For every baseline dialogue, separately vary a premise and conclusion; log constructions that cannot preserve the distinction. |
| EVA-06 | **READY** | Unrehearsed conversation-repair trial. | Solo task 7 and repair reference | Read both roles aloud, insert misunderstandings, and record every point where English is required. |
| EVA-07 | **READY** | Productive-name burden trial. | NAM-05 | Compare repeated onym and guest-frame versions without changing the underlying referent. |
| EVA-08 | **READY** | Consolidated evaluation record. | Result table in `documents/solo_evaluation_tasks.md` | Add dated results, material, failures, and follow-up; never replace a pending row with an undocumented impression. |

## Phase 5: Speech, phonology, and listening

**Objective:** Preserve a clear reference pronunciation while designing for real accents, conversational tempo, and perceptual evidence.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| SPH-01 | **DONE** | Separate careful reference pronunciation from accepted conversational and accented variants. | Canon pronunciation ruling; phonetics documents | New teaching avoids moralizing accent or tempo. |
| SPH-02 | **DONE** | Phoneme-aware, feature-weighted neighbor audit and reproducible baseline. | `scripts/audit_phonetic_neighbors.py`; phonetic baseline | Baseline regenerates exactly and remains advisory. |
| SPH-03 | **DONE** | Rename gate requiring repeated observed confusion rather than distance alone. | `documents/listening_audit.md` | No breaking rename bypasses the gate. |
| SPH-04 | **READY** | Maintainer ABX recordings for high-priority function pairs and external boundaries. | Listening-audit protocol and prompt generator | Record careful and conversational sessions on three nonconsecutive days, in quiet and moderate noise. |
| SPH-05 | **READY** | Record observations and replay/confidence data. | Pending observation table | Fill actual trials for `hasha/hasho`, `patha/patho`, and prioritized dense pairs. |
| SPH-06 | **EVIDENCE** | Outside-listener results across accents and language backgrounds. | No outside result yet | Begin with function words and boundary pairs; preserve consent and keep raw voice private by default. |
| SPH-07 | **EVIDENCE** | Learner-facing reference recordings and accepted-variation examples. | No curated audio set yet | Publish only reviewed recordings whose speaker consent and purpose are recorded. |
| SPH-08 | **DEFERRED** | Broad lexical renaming campaign. | Explicitly excluded from Phi 2026.1 | Reconsider only after repeated, high-impact perceptual confusion survives careful-production review. |

## Phase 6: Evidence-led semantic growth

**Objective:** Expand Phi where recurring discourse demonstrates need, especially for philosophical and solarpunk community discussion, without converting every external concept into a core root.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| SEM-01 | **DONE** | Establish the admission gate: compose first, use external material when faithful, coin only after recurring failure. | Development protocol and capability matrix | Every proposal cites the passages it repairs. |
| SEM-01A | **PARTIAL** | Test practice and domain profiles as shared-core, non-grammatical organization. | Module contract; Household and Daily Life; Medical and Bodily Care; Systems and Shared Infrastructure; Philosophical Reasoning; Accessibility and Participation; Commons and Collective Governance; Ecological Systems and Material Life | Run each profile's next-use test before treating the format as a durable extension policy. |
| SEM-01B | **PARTIAL** | Evaluate the recorded proposed-profile catalogue. | `documents/modules/README.md`; Accessibility, Commons, and Ecological Systems moved to active; the Work, Craft, and Repair audit and scenario gate is satisfied | Create the zero-new-root Work, Craft, and Repair profile; keep solarpunk cross-module and sensitive domains scenario-gated. |
| SEM-02 | **PARTIAL** | Map weak modern domains: technology, science, government, law, work, disability, reproductive health, sexuality, and institutions. | Assessment, survey, two access scenarios and profile, two commons scenarios and profile, two ecological scenarios and profile, and the work/craft vocabulary audit plus scenario | Create Work, Craft, and Repair, then test inhabited-place heat and cooling, accessibility outside meetings, and a standing institution outside councils while keeping sensitive domains scenario-gated. |
| SEM-03 | **PARTIAL** | Solarpunk philosophical scenario corpus. | Original regression corpus and the ecological profile now cover ecology, energy, care, consent, accessibility, commons allocation, collective decisions, accountability, watershed evidence, habitat, material return, shared craft, work refusal, and repair safety | Continue with mutual aid, institutional failure beyond one council, climate and heat, and conflicting visions of a good future. |
| SEM-04 | **READY** | Tradition-specific philosophy protocol. | Exact-first/explain-in-core pattern in the capability matrix | Test several traditions without claiming one Phi paraphrase exhausts the source concept. |
| SEM-05 | **READY** | Evidence packet for each proposed root or construction. | Development protocol | Require at least several independent failures, attempted compositions, external alternatives, scope, contrasts, example dialogue, phonetic checks, and migration impact. |
| SEM-06 | **PARTIAL** | Case-by-case review of core refusals. | Canon refusal and external-reporting rulings | Reconsider any refusal that obstructs care, identity, consent, safety, testimony, or analysis; document the result whether admitted or retained. |
| SEM-07 | **PENDING** | First post-baseline philosophical expansion cycle. | Depends on EVA-04 through EVA-06 and PHL-05/06 | Select one recurring gap, make the smallest justified change, add corpus evidence and teaching, then re-test before choosing another. |

### Default admission test

A new philosophical form should normally satisfy all of the following:

1. The need recurs in more than one independently written or transformed passage.
2. Ordinary composition has been attempted and its loss can be stated precisely.
3. Guest or exact carriage is insufficient for the intended core discussion, not merely longer.
4. The proposal has a bounded meaning and contrasts with neighboring words or constructions.
5. It passes structural, phonetic, corpus, gloss, rendering, and teaching checks.
6. It improves a re-run of the motivating task without creating a broader ambiguity.

This is a default evidence threshold, not an automatic formula. An exception requires a recorded decision in the development log.

## Phase 7: Original corpus and teaching

**Objective:** Make original Phi use, especially disagreement and inquiry, the primary evidence for future development while keeping the learning path honest and usable.

| ID | Status | Deliverable | Evidence | Completion or next criterion |
|---|---|---|---|---|
| COR-01 | **DONE** | A validated shelf of transmuted literature and extensive teaching examples. | `pamphlets/`; manual; primer | Continue to distinguish transmutation choices from general expressive capacity. |
| COR-02 | **DONE** | Fifteen original philosophical regression dialogues. | `documents/philosophical_test_corpus.md` | Preserve as baseline tests rather than polished doctrine. |
| COR-03 | **READY** | Sustained original philosophical essays in Phi. | Depends on PHL-05/06 scenario selection | Write at least three essays with claims, objections, revision, and unresolved tension; maintain proposition and gap logs. |
| COR-04 | **READY** | Dialogue set whose successful outcome is disagreement, suspension, or revised framing rather than consensus. | Repair conventions | Add validated dialogues and re-run repair tests. |
| COR-05 | **EVIDENCE** | Transcripts or reconstructions of spontaneous Phi conversation. | No spontaneous corpus yet | With consent, preserve normalized text and an error/repair log; do not publish raw voice by default. |
| COR-06 | **PARTIAL** | Corpus-attestation data for phonetic and lexical decisions. | Phonetic audit counts documentation examples | Separate authored Phi usage from mentions in explanation as the corpus grows. |
| PED-01 | **DONE** | Complete primer, reference manual, pamphlet shelf, quick reference, and generated explorer. | `primer/`; `manual/`; `pamphlets/`; `web/` build | Keep generated outputs synchronized. |
| PED-02 | **DONE** | Advanced teaching for external registers and productive names. | Manual chapter 24 and relevant pamphlets | Maintain exercises and answers as rules evolve. |
| PED-03 | **PARTIAL** | Claims about learning burden aligned with actual grammar. | Revised introductory and manual prose | Continue auditing “one rule,” speed, and ease language. |
| PED-04 | **EVIDENCE** | First complete outside learner walkthrough. | No result yet | Record chapter time, errors, questions, abandoned points, and prior language background. |
| PED-05 | **EVIDENCE** | Curriculum pacing and retention evidence. | No result yet | Re-test selected material after a delay; revise ordering before adding explanations. |
| PED-06 | **READY** | Maintainer-as-learner regression pass after a blind interval. | Existing curriculum | Complete the primer exercises without consulting answers and log friction without generalizing to all learners. |
| PED-07 | **EVIDENCE** | Accessibility review for visual, auditory, cognitive, and motor needs. | Organizational profile and two scripted scenarios exist; no affected-user review yet | Invite affected users to identify barriers; prioritize practical access over aesthetic doctrine. |

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

## Critical path: next execution sequence

The next work should gather evidence, not add grammar. Complete these packages in order unless a real user need intervenes.

### Work package A: Choice and naming trial

**Roadmap items:** EVA-02, EXT-06, NAM-05.

1. Create twenty balanced prompts covering core composition, registered compound, productive name, guest, and exact form.
2. Include personal and place names, non-Latin exact form, technical precision, harmful historical terminology, community practice, and a recurring philosophical gap.
3. Write paired ten-mention narratives using a productive onym and a guest frame.
4. Leave the prompts untouched for at least one day.
5. Classify them without the key and record ambiguous or burdensome cases.
6. Revise examples or selection guidance before considering grammar changes.

**Exit criterion:** dated result rows exist, every ambiguous case has an explanation, and any proposed rule change cites the failed prompt.

### Work package B: Blind philosophical paraphrase

**Roadmap items:** EVA-04, PHL-04.

1. Select one baseline dialogue and record the selection without rereading its translation.
2. Wait a documented seven-day interval.
3. Paraphrase the Phi into plain language.
4. Compare propositions, sources, modality, negation, participants, and discourse relations.
5. Record losses and additions separately.

**Exit criterion:** one scored paraphrase record exists and the matrix reflects every observed failure.

### Work package C: Argument and repair stress test

**Roadmap items:** EVA-05, EVA-06, PHL-03, PHL-05, PHL-07.

1. Transform each baseline dialogue once by changing a premise and once by changing its conclusion.
2. Read both roles aloud without rehearsal.
3. Insert a hearing problem, a meaning problem, an evidence challenge, and understood disagreement.
4. Use only documented repair conventions until one fails.
5. Record every English rescue and every convention heard differently from its intended function.

**Exit criterion:** repair conventions are marked demonstrated, revised, or retained as gaps based on dated trials.

### Work package D: Maintainer listening baseline

**Roadmap items:** SPH-04, SPH-05.

1. Generate fixed-seed ABX prompts.
2. Record careful and conversational versions on three nonconsecutive days.
3. Test quiet and moderate-noise conditions without visible spelling.
4. Enter trials, errors, replays, and confidence in the listening audit.
5. Open a rename candidate only if the existing rename gate is met.

**Exit criterion:** the two external boundary pairs and a prioritized function-word set have actual observation rows; automated scores alone trigger no rename.

### Work package E: First evidence-led language change

**Roadmap items:** PHL-06, SEM-03, SEM-05, SEM-07.

1. Choose the most recurrent failure from packages B and C.
2. Write additional solarpunk or philosophical passages that require the same distinction.
3. Attempt composition and external carriage explicitly.
4. Propose the smallest lexical, constructional, or teaching change that repairs the failure.
5. Re-run every motivating task and the full regression suite.

**Exit criterion:** one narrowly justified change is released with evidence, alternatives, migration impact, teaching, and re-test results. Do not bundle unrelated gaps.

### Work package F: First outside-reader packet

**Roadmap items:** PHL-08, SPH-06, PED-04, COM-03.

Prepare this only after the solo tasks have been run, so outside readers are not asked to find failures already visible to the maintainer.

The packet should contain a short consent statement, pronunciation reference, a small primer segment, one external-register task, one philosophical dialogue, one repair task, and open-ended questions. Collect language background and qualitative observations. Do not claim percentages from a handful of participants.

**Exit criterion:** at least one outside reader completes the packet, their consent and conditions are recorded, and the roadmap distinguishes their observation from maintainer inference.

## Milestone view

These labels describe logical milestones, not promised dates.

| Milestone | Status | Included work |
|---|---|---|
| Phi 2026.1: external register and honest scope | **DONE** | FND-01 through FND-04; EXT-01 through EXT-05; initial PHL and SPH tooling. |
| Phi 2026.2: productive names | **DONE** | NAM-01 through NAM-04 and strict name validation. |
| Solo evidence baseline | **NEXT** | Work packages A through D. |
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
3. the smallest justified change is made or the external bridge is retained;
4. teaching and tooling agree with the decision;
5. the motivating task improves on re-test;
6. outside users can report different results without those results being absorbed into a predetermined claim;
7. recurring speakers have a credible path to influence decisions that affect them.

At that point Phi will still be unfinished, as any living language is, but the original improvement plan will have achieved its purpose: development will be driven by philosophical use, honest evidence, and community accountability rather than by the completeness of a private design.
