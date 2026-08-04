# How a Phi translation is made

Readers looking for the promise behind the mark, without all the workshop detail, can begin with [What certified means](translation_certification.md). A certified text can still contain errors; the mark records a completed process and a checked published version, not immunity from correction.

A Phi translation is made in two directions, at two different times. First the source is carried into Phi. Once that work is settled, the source leaves the desk and the Phi is carried into English. The separation matters because a familiar source sentence is very good at lending details to an English rendering that the Phi never actually said. A fluent result can hide a weak translation with alarming politeness.

The work follows two one-way paths:

```text
source -> Phi
frozen Phi -> derived English
```

The exact gloss belongs to the second path. It explains the settled Phi word by word; it is not a crib used while composing the Phi.

## What the reader sees

An aligned translation unit has four layers:

```text
Phi sentence
exact word-by-word gloss
(natural English derived from the Phi)
source-label: "the author's wording"
```

The final page places these layers together so a reader can compare them. The translator does not draft them together. Their proximity is for inspection, not production.

## 1. Establish the source

The work begins with an identified source witness. Its wording is tied to an edition and translator. Its publication status determines how much may be quoted, and its chosen extent establishes what the translation promises to cover. The source is divided into non-overlapping units that preserve its order and reconstruct the complete chosen passage after the repository's documented normalization. A source citation is evidence of coverage, not proof of a good translation; it still has to be read against the Phi proposition beside it.

Before drafting Phi, make a proposition record for each source unit. It need not become part of the finished page. The record says who is present, what happens or holds, how the claims relate, and which details of stance, degree, repetition, or imagery matter. Check each item against the Phi before the unit crosses the phase boundary. This catches a missing relation even when every surviving sentence is grammatical.

## 2. Translate only into Phi

During the first phase, the translator may see the source and Phi's complete language references. Parenthetical English, old back-translations, summaries of earlier English, and glosses are removed from the working view. The translator searches the whole vocabulary before composing around a concept and may coin a word when Phi genuinely needs one, subject to the ordinary development protocol. Module vocabulary is available without hesitation when it fits the thought.

Each unit is checked before the next layer is attempted:

| Reading | What it checks |
|---|---|
| Source fidelity | Participants and claims; images and deliberate repetition; logical and discourse relations; aspect, evidence, modality, and degree. |
| Source boundary | Exact names and measurements; quotations, technical labels, and other identities that canon keeps in the adjacent source material. |
| Phi grammar | Modifier-first order and particle scope; frames and complement boundaries; coordination and topic drop; complete assertions. |

Phi does not quietly invent an approximation and ask the source line to repair it. The source-fidelity reading and the Phi-grammar readback are separate jobs. The grammatical readback treats each sentence as Phi rather than inferring its structure from what the source must have meant. Every complete sentence passes the full-sentence validator, and every applicable repository validator passes before the Phi is frozen.

## 3. Freeze the Phi

When the source partition and every Phi unit are settled, the aligned Phi stream receives a SHA-256 digest. The digest records the phase boundary; it does not claim that the wording can never improve. It proves which Phi stream supplied the later English.

The source-to-Phi working view can be made with:

```bash
python3 scripts/translation_layers.py texts/north_wind_and_sun.md --phase source-to-phi --output /tmp/north_source_phi.md
```

That view contains numbered Phi units and their decoded source citations. It omits glosses, derived English, notes, and limits. A new translation begins directly in the same numbered Phi-and-source form under `/tmp`; there is no English layer to extract. Before the freeze is accepted, the source citations must still reconstruct the chosen source passage exactly.

## 4. Make compact anonymous bundles

The frozen source-to-Phi view becomes the input to the second phase. For a work of ordinary length, make a directory of bounded packets:

```bash
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --output-dir /tmp/north_derive --batch-size 8
```

The directory contains three kinds of file:

| File | Contents |
|---|---|
| `manifest.json` | The full frozen digest, selected unit numbers, unit and batch digests, reference digest, review policy, and packet order. |
| `reference.md` | Compact records for only the lexical forms and registered compounds used by the selected Phi, followed by a short grammar checklist. |
| `derive_*.md` | At most eight numbered Phi units, their unit digests, structural review flags, and lexical gloss scaffolds. |

The shared reference is read once rather than copied into every packet. Eight units is a practical default, not another law of grammar. A dense passage may need six; a run of short clauses may be comfortable at ten.

The command refuses a non-empty output directory, so an old packet cannot be mistaken for part of the current freeze.

The bundles contain Phi and only what is needed to read it. Everything source-facing is absent, including the title. That last omission matters more than it may seem: a familiar title can recall half a sentence before anyone has translated a word.

## 5. Make the primary derivation from Phi alone

A fresh, non-forked model context receives `reference.md` once and the derivation packets in order. It has never seen the source, prior English, or a summary of either. Canon, the grammar, and the required voice references are open; everything source-facing and every repository-navigation surface stays closed.

For every unit, it first records each complete assertion's predicate and arguments, modifier attachments, particle and complement scope, and pronoun antecedents. Only then does it produce an exact gloss and natural English. This order makes the syntax visible before an agreeable English sentence has a chance to disguise it.

The generated gloss scaffold is lexical, not final. It supplies the canonical gloss of each token without attempting to settle relative-clause brackets, coordination grouping, or other structure. The reader verifies it token by token and adds structural brackets from the completed analysis.

The gloss preserves lexical identity and grammatical marking closely enough to expose the construction. The natural English says what the Phi says in ordinary English syntax.

| Natural English may | Natural English may not |
|---|---|
| Use ordinary English order; unfold a transparent compound; avoid wooden repetition when English can state the same Phi distinction naturally. | Recover source-only gender or names; borrow emphasis or imagery; restore attribution order or literary phrasing that Phi does not encode. |

If Phi says less, the English says less. If that result exposes a poor Phi sentence, the problem belongs to the first phase.

Reader-facing English receives the normal Humanizer and Phi voice passes while the source remains hidden. Those passes may improve rhythm and clarity, but they may not add a proposition, strengthen a modal, guess an identity, or smooth away a distinction that Phi marks.

## 6. Give difficult units an independent reading

After the primary derivation, generate the audit queue from the same frozen Phi:

```bash
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --audit-only --output-dir /tmp/north_audit --batch-size 8
```

The queue contains every unit whose structure crosses the independent-review threshold, plus a deterministic ten-percent sample of the remaining units. The selector groups its reasons like this:

| Queue rule | Result |
|---|---|
| Any two review flags | The unit enters the independent queue. |
| One high-attention flag | `long-sentence`, `many-assertions`, `multiple-complement-frames`, `complex-coordination`, `relative-clause-attachment`, `question-or-condition`, or `compound-interpretation` places the unit in the queue by itself. |
| Below the threshold | The unit remains eligible for the deterministic sample. |

| Review family | What draws a flag |
|---|---|
| Length and structure | A long sentence, several assertions, or complex coordination. |
| Embedded grammar | Nested or repeated complement frames, a question or condition, or a relative clause whose attachment needs care. |
| Scope and reference | A particle stack or several uses of the third-person pronoun in a structure where antecedents may compete. |
| Lexical reading | Several registered compounds or several words from optional modules. A form absent from both the lexicon and the productive-name rules stops bundle generation as an error. |

A flag directs attention; it does not declare the sentence wrong.

A second fresh, source-blind context reads this queue independently. Its response is an internal semantic check, so it uses direct prose without the voice guide or Humanizer. It performs the same assertion, attachment, scope, and antecedent analysis before giving its gloss and English reading.

Compare the two readings by meaning. Different rhythm or word choice is harmless. A difference in participants, roles, attachment, scope, complement boundaries, assertion count, or antecedents must be settled from the Phi and its grammar. If a sampled low-risk unit reveals a class of structural error that the flags missed, repair the selector and regenerate the queue. The sample keeps the filter honest.

When both readers agree on the semantic structure and the gloss is correct, the unit is settled. Do not commission another reading merely because the two English sentences have different styles. The purpose of the audit is agreement about what Phi says, not a contest for the prettiest paraphrase.

## 7. Assemble and audit one direction at a time

Only after both phases are complete are the four layers assembled. The audits remain separate:

1. Read the source against Phi. Confirm that Phi carries the source faithfully and that the citations cover the chosen passage in order.
2. Put the source aside. Read Phi against the exact gloss and derived English. Confirm that both English layers carry only what Phi encodes and that the natural line remains readable.

The source is never compared directly with the derived English as a translation test. That comparison would reward the English for borrowing from the source and would conceal the very problem the isolation rule is meant to expose.

Assembly can reveal a bad grouping or an awkward English line. Derive its replacement from the affected anonymous Phi unit in another fresh source-blind context. Do not repair it while looking at the source.

After both directional audits pass, the introduction and notes may be written with the complete work in view. They describe the translation but do not reopen its aligned layers.

## 8. Retry only the Phi units that changed

Any change to a frozen Phi unit invalidates that unit's gloss and derived English. Discard both. The unchanged units remain settled because their numbered Phi and unit digests have not moved. Make a fresh self-contained retry packet for the affected units:

```bash
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --units 3,7-8 --output /tmp/north_retry.md
```

The retry goes to a fresh source-blind context under the same rules as the primary derivation. Once the changed Phi is final, generate new derivation and audit manifests for the complete stream. The full digest will change, and revised structure may change the audit selection, but unchanged derivations do not need to be written again. Unit hashes show which ones remain identical.

Even a small Phi correction can change scope, tense, participant roles, or emphasis. Reusing the old English for that unit would make the digest ceremonial rather than useful.

The digest can be checked at any time with:

```bash
python3 scripts/translation_layers.py texts/north_wind_and_sun.md --digest-only
```

The certification registry recomputes this value from the published document. It also checks a second digest over the published Phi, gloss, derived English, and citations. A later edit to any aligned layer therefore fails CI until the work has been checked and recertified.

## 9. Certify the result

A certification record contains this evidence:

| Evidence | What it fixes in the record |
|---|---|
| Development decision, pull request, and date | Where and when certification was accepted. |
| Aligned-unit count and source-reconstruction count | The extent of the translation and its exact source coverage. |
| Frozen Phi digest | The Phi stream from which English was derived. |
| Published aligned-layer digest | The final Phi, gloss, derived English, and citations as one checked set. |
| Derivation and restart note | The fresh source-blind context and any material unit replacement or retry. |

An earlier fidelity sweep is useful evidence, but it is not retrospective proof that the source was hidden during English derivation.

The pull-request body links the final derivation manifest and records the independent queue, its sample, and any semantic resolution or unit-scoped retry. This evidence remains attached to the public review that accepted the work.

The [certification ledger](../evaluation/translation_process_status.md) is the readable record. Its machine-readable source is `project/translation_process_status.json`. The registry discovers the standalone translations and Gibran selections from their catalogues and the current *News from Nowhere* chapters from the book directory. A new translation cannot quietly fall outside the queue, and a certified Phi change cannot quietly retain old English.

Update and check the ledger with:

```bash
python3 scripts/translation_process_status.py --write
python3 scripts/translation_process_status.py --check
```

Certification records how a particular published version was made. It does not make the translation immune to criticism. A later fidelity finding may reopen the Phi, but it must also reopen everything downstream of the Phi.

## Scope

This process applies to translations. Original Phi works begin in Phi and already give English the second-place role, so they need a Phi-first review rather than a source-to-Phi phase. The Ring Verse is an explicit refusal and is judged by whether the refusal states its relationship to Tolkien honestly. Source witnesses, collection indexes, and book navigation pages support translations but are not translation documents themselves.
