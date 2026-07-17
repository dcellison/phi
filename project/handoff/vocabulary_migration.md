# Vocabulary migration

This guide describes the active SEM-09 prose migration and the content-coverage gate around it. It supplements the live [`development protocol`](../development_protocol.md), [`schema`](../../vocabulary/schema.json), [`coverage ledger`](../content_vocabulary_coverage.md), and [`decision register`](../content_vocabulary_decisions.json). Those sources remain authoritative.

## What counts as migrated

The target prose contract is not a cosmetic rewrite. A completed content entry has:

- the stable identity fields `word`, `gloss`, `ipa`, `syllables`, and one scalar `pos`;
- an accurate `description` that defines its range and gives the nearby distinction a speaker is likely to need;
- a physical `articulatory_notes` account of the complete spoken form;
- at least one structured `examples` pair using a complete lowercase Phi sentence and a natural English translation;
- one or more `semantic_domains` assignments, each with a word-specific retrieval rationale;
- any useful `search_terms`, `usage_notes`, `sound_symbolism`, direct `pillars`, and established `modules` memberships;
- no legacy `concept` or `grammatical_notes` field.

The schema still accepts legacy forms while migration is underway. That compatibility is not permission to leave old fields in an entry that receives a complete revision.

Entry state is computed by `scripts/vocabulary_prose_coverage.py`:

| State | Meaning |
|---|---|
| `legacy` | Neither target field is complete; old prose fields remain. |
| `partial` | Only one of `articulatory_notes` and `examples` exists. |
| `dual` | Both target fields exist, but at least one legacy field remains. |
| `target` | Both target fields exist and neither legacy field remains. |

The present inventory has no partial or dual entries. Keep it that way.

## Batch preflight

### 1. Start from current `main`

Verify the reported merge, fetch and fast-forward, and confirm a clean worktree before creating a feature branch. Never build a vocabulary PR on a branch whose parent PR is still open unless Daniel explicitly chooses stacked work.

### 2. Read the governing material

Read `canon.md`, the development protocol, the full voice guide, the full Humanizer skill, the schema, and the last one or two completed entries nearest the new batch. Read the relevant manual or module chapter when the batch touches a settled teaching pattern. Read the measurement essay before work involving quantity, time, weight, dimensions, exchange, or exact values. Read the peace-linguistics audit and current canon refusal before work involving harm, power, coercion, protection, disagreement, or social institutions.

### 3. Inventory the whole proposed batch

Do not edit the first word before seeing the whole set. For every entry, inspect:

- the current JSON and exact lexical class;
- every active corpus use found with `rg`;
- nearby words and registered compounds that divide the same area;
- applicable event-noun, quality-noun, noun-as-modifier, and relative-clause strategies;
- current base or module placement and every existing module membership;
- canon rulings that refuse, compose, or source-bind part of the apparent English range;
- the opposites, intermediate conditions, changes, results, and ordinary scenarios that can expose a missing concept.

Use the SQLite lexicon for quick exploration when useful, but believe the JSON when the index and source disagree:

```bash
python3 scripts/lexicon_tool_simple.py init
python3 scripts/lexicon_tool_simple.py find TERM
python3 scripts/lexicon_tool_simple.py view WORD
```

`find` has a deliberate but counterintuitive exit code: it exits 1 when a term exists and 0 when the form is free for coinage.

### 4. Define the semantic tests before writing definitions

Add a detailed section to `project/content_vocabulary_coverage.md`. Its table should ask conceptual questions rather than reproduce a list of English headwords. A useful row names the area being tested, current Phi coverage, a status, and the boundary that makes the decision intelligible.

The coverage review asks whether Phi can conduct ordinary and intended discussion. It does not ask whether the language has one root for every English near-synonym. Composition is a success when the parts show the relation Phi wants to keep visible. Coinage is a success when a dedicated form makes a recurring concept clearer, easier, or more natural.

## Never lose a noticed question

Earlier batches sometimes mentioned possible gaps such as brain, throat, and joint in prose without implementing them or preserving them in a queue. The maintainer regarded that as a serious failure. The register now prevents a repeat, but only if the model records the question immediately.

Before the batch closes:

1. Add the batch heading to the coverage ledger in the same order used by `project/content_vocabulary_decisions.json`.
2. Add a batch object with `migration_status`, `decision_status`, and reciprocal `candidate_ids`.
3. Give every noticed question a `CV-...` identifier, even when the answer seems obvious.
4. Choose an explicit state and supply the state-specific evidence.
5. Leave the batch open when any candidate is `open` or `accepted`.
6. Regenerate the readable Markdown view and run its tests.

Decision states have executable requirements:

| State | Required evidence |
|---|---|
| `open` | A precise `question`. |
| `accepted` | A `planned_implementation`; the batch remains open until it lands. |
| `implemented` | An `implementation` object naming the actual words, files, or registered compounds. |
| `compositional` | A nonempty `expressions` list using existing Phi. |
| `deferred` | A concrete `revisit_when` condition, not a vague preference for more evidence. |
| `source-bound` | A `source_rule` stating which exact identity remains outside the Phi passage. |
| `declined` | A direct `decision` explaining the refusal. |

Every candidate also needs `concept`, `placement`, `summary`, and reciprocal `batches` links. The generator verifies files, word forms, registered compounds, links, batch closure, and coverage headings.

The maintainer has already authorized coinage. Do not use `deferred` as a polite way to avoid deciding. Defer when the distinction genuinely belongs to a connected specialist practice that has not yet been designed, or when a particular scenario is needed to avoid harmful assumptions. Sexual and reproductive anatomy is one such recorded case. An ordinary concept with a clear semantic boundary should be implemented in the same batch when a root is the better solution.

## Composition, coinage, modules, source material, and refusal

Each concept receives the treatment that fits Phi rather than the treatment that most resembles English.

### Composition

Prefer an existing construction when its parts reveal a useful relation. The registry already carries settled forms such as dawn color for pink, sun beginning for east, and writing dye for ink. Event nouns name acts and the works produced through those acts where canon establishes that reading. Adjectives license quality nouns without a second lexical class. A noun may modify a following noun. Relative clauses name occasional roles without turning a person into a permanent category.

Phi has no noun-to-verb or adjective-to-verb conversion. It rejected the former direction and removed 45 old dual listings. Becoming uses `kelu`, causing uses ordinary voice, and manner is a descriptor immediately before the verb inside the Slot 1 block.

### Coinage

Coin when the concept deserves easy lexical presence or a composition would be cumbersome, ambiguous, or aesthetically wrong. A personal language may coin because a distinction is useful or valued. External proof of necessity is not a gate.

A new lexical form must:

- use legal Phi phonology and open syllables;
- begin with a permitted onset and end in a vowel;
- contain no VVV sequence and no duplicated syllable;
- contain at most three syllables, with three syllables preferred unless everyday frequency justifies scarce two-syllable space;
- pass the character-distance collision rule and the advisory phonetic-neighbour audit;
- avoid accidental English homonyms where reasonably possible;
- remain comfortable when spoken several times in a natural sentence;
- receive the complete target schema, examples, coverage decision, references, and any speaker-facing module update in the same work.

Run both collision tools before settling a form:

```bash
python3 scripts/validate_examples.py neighbors CANDIDATE
python3 scripts/audit_phonetic_neighbors.py --candidate CANDIDATE
```

The validator's distance-1 rule is a hard gate subject only to the existing grandfathered baseline. The phonetic-neighbour score is advisory and never orders a rename by itself. Natural opposites should be easy to distinguish, not designed as minimal pairs.

When a form replaces another form, search the entire active repository explicitly. The validator has a known limitation around single-word italic mentions. Update examples, grammatical notes, compounds, manual and primer teaching, texts, generated references, and sound-related prose in context. Retire the old short form in `documents/validation/retired_forms.txt` when canon requires lexical protection. Four-syllable forms are excluded by class and do not belong in that file.

### Base and modules

Base versus module placement controls what a general learner is expected to study. It does not create two grammars or two levels of lexical legitimacy.

Keep ordinary life, identity, consent, safety, testimony, and general communication available in base vocabulary. Put specialized terms in every module whose speakers genuinely need them. Preserve an existing `modules` array during migration, including multiple memberships. Do not reduce it to the first module named in a profile.

### Source material

Exact foreign wording, names in their source form, quotations, identifiers, formulas, units, medical and legal records, exact measurements, classifications, and other unassimilated artifacts remain outside Phi syntax. Phi can point to them and discuss them. Do not restore the retired guest or exact frames, and do not imply that separate presentation approves or condemns the source.

### Refusal

A refusal must express a value without making care, identity, consent, safety, testimony, or critique impossible. Current refusals include generic conflict and direct combat vocabulary, weapons and enemies, domination roles, marriage as a universal institution, universal gendered person classes, generic bad, specific prescribed rites, clock and physical units, money vocabulary, and the extended color palette. Read the exact canon wording before applying any refusal.

## Writing the entry

Use canonical schema order. The stable and target fields ordinarily appear in this sequence:

```text
word
gloss
ipa
syllables
pos
search_terms, when useful
description
articulatory_notes
sound_symbolism, when honest
usage_notes, when needed
examples
pillars, when direct
semantic_domains
modules, when optional
```

### Description

Write two to four sentences that define the actual range. Begin with a concrete use, form, relation, or contrast where the word allows it. Cite a nearby Phi word as `'word' (exact gloss)` only when the distinction helps. State one boundary once. Do not finish with an insurance-policy list of everything the word does not mean.

Definitions must respect the entry's single lexical class. A noun can be used before another noun as an ordinary modifier, but that does not make it an adjective entry. A verb's event noun and an adjective's quality noun are grammar rules, not extra values in `pos`.

### Articulatory notes

Follow the whole word through the mouth. Describe onset contact or constriction, voicing and airflow, vowel height and backness, lip rounding, dental `t` and `n`, stress, and every hiatus boundary that matters. Do not assign semantic labels to syllables. Compare a target entry with the same sounds, then verify the mechanics rather than copying its sentence shape.

### Sound symbolism

Omit the field when the form offers no honest Phi-specific association. When it does fit, describe a felt contour, audible family resemblance, or physical mnemonic as an interpretation. It may be poetic, but it may not claim that a phoneme universally means an abstract idea. Semantic boundaries belong in `description`; speaking instructions belong in `articulatory_notes`.

### Examples

Store one or more objects with `phi` and `translation`. At least one example must use the entry word. Phi is lowercase, uses periods only, keeps strict modifier-first grammar, and uses current words. The English should sound natural while preserving the Phi claim. Validate examples early with a path-restricted run, then validate the entire repository.

Do not write a new Phi sentence by intuition alone. Inspect the relevant taught pattern, search for established examples, and use the lexicon for every form. The validator catches nonexistent words and many structural errors; it cannot determine whether a semantically legal sentence is good Phi.

### Pillars and semantic domains

Pillars are optional. Include only direct connections that pass the paste test: the rationale becomes false when pasted into a different entry. Neutral words need no philosophical decoration.

Semantic domains are required for content words and may be revised during migration. Each assignment is a retrieval route with a specific rationale. A setting where the word can appear is not enough. `community` and `wisdom` are not badges of approval, and `nature` does not collect every quality found outdoors.

## Humanizer and voice pass

Draft the complete, accurate batch first. Then make a separate Humanizer pass across every generated string, including decision summaries, coverage cells, semantic-domain rationales, and the PR body. Preserve exact forms, glosses, source quotations, schema structure, and validated Phi.

After Humanizer, audit the whole batch against `documents/reference/voice_for_models.md`:

- count negative litanies, disclaimer tails, compliance imperatives, rule-of-three constructions, present-participle tails, and copula avoidance;
- scan explicitly for em and en dashes, curly quotes, banned inflation vocabulary, and the rejected hyphenated carrying-suffix construction;
- compare opening sentence shapes, closers, and repeated phrases across all entries;
- count pet verbs such as "names," "carries," and "remains";
- read articulatory notes together so repeated anatomy does not become identical prose;
- keep approved boilerplate identical, but vary everything that is meant to be an observation about one word.

A prior 18-entry batch initially opened 13 descriptions with the same `A 'word' is ...` frame. Another repeated `instrument heard for` and `role through which` across neighbouring entries. Both passed per-file reading and failed the batch count. Measure the collection.

When reporting the work, name a concrete pattern found and corrected. "Humanizer applied" is not evidence of a pass.

## Batch artifacts

A completed SEM-09B batch normally changes:

1. The selected canonical JSON entries under `vocabulary/content/`.
2. `project/content_vocabulary_coverage.md`, including the overview row, current-position row, full conceptual-test section, semantic-domain crosswalk where applicable, and resume point.
3. `project/content_vocabulary_decisions.json`, with reciprocal batch and candidate links.
4. Generated `project/content_vocabulary_decisions.md`.
5. `project/development_log.md`, normally one new D-numbered decision summarizing the batch.
6. `project/roadmap.md`, with the remaining base count and evidence references.
7. Generated `documents/validation/vocabulary_prose_coverage.json`.
8. Generated Part VII lexicon references whose source data changed, often `manual/part7_reference/lexicon/by_domain.md` and possibly the other generated indexes.
9. `documents/reference/compounds.md` and generated `manual/part7_reference/compounds.md` when a new registered composition is accepted.
10. A speaker-facing module chapter only when new module vocabulary is implemented or existing module guidance must change.

Do not hand-edit generated Markdown. Edit the JSON or source registry and run the generator.

## Regeneration and validation

Run the generators after prose and decision edits:

```bash
python3 scripts/content_vocabulary_decisions.py --write
python3 scripts/vocabulary_prose_coverage.py
python3 scripts/generate_reference.py
```

Run the complete local check set:

```bash
python3 scripts/validate_examples.py --show-warnings
python3 scripts/test_vocabulary_schema.py
python3 scripts/content_vocabulary_decisions.py --check
python3 scripts/test_content_vocabulary_decisions.py
python3 scripts/test_name_forms.py
python3 scripts/audit_phonetic_neighbors.py --output /tmp/phonetic_neighbors_baseline.txt
diff -u documents/validation/phonetic_neighbors_baseline.txt /tmp/phonetic_neighbors_baseline.txt
python3 scripts/build_site.py
git diff --check
```

Zero errors and zero warnings is the vocabulary bar. The neighbour baseline should remain byte-for-byte identical when no form changes. If forms change, inspect every changed pair and update the committed baseline only as part of the accepted lexical decision.

After staging the intended files, rerun all generators and use `git diff --exit-code` to prove they produced no unstaged drift. Then run `git diff --cached --check` and inspect the staged file list. Do not commit unrelated tracked or untracked work.

## The post-base corpus retrofit

When the coverage report reaches zero legacy base entries, begin SEM-09D before module migration.

Build a list of base roots coined or materially narrowed during the coverage work. Search active prose and Phi passages in `book/`, `manual/`, `primer/`, `pamphlets/`, `texts/`, `documents/`, `kia.md`, `short_road.md`, and current root documentation. Ignore `archive/`.

For each match or likely workaround:

1. Read the complete surrounding passage and its job for the reader.
2. Decide whether the old composition remains transparent and good Phi.
3. Replace it only when the current root improves fidelity or naturalness.
4. Update glosses, translations, citations, compound notes, exercises, and repeated excerpts that depend on the changed line.
5. Preserve before-state evaluation material whose old limitation is itself evidence.
6. Record the review in `documents/evaluation/active_text_corpus_review.md` or the roadmap artifact chosen for SEM-09D.
7. Validate targeted paths first, then run the whole suite and site build.

Changing an English lexicon definition is not a reason to rewrite a Phi text. A corpus passage changes because the language available to that passage improved.

## Failure patterns to guard against

- Do not record a gap only in narrative prose. Give it a decision ID.
- Do not defer a clear ordinary concept merely because no outside speaker has asked for it.
- Do not coin every English synonym. Phi needs distinctions, not a mirrored dictionary.
- Do not let module vocabulary enter a base-only migration batch unless a separate placement decision moves the concept into base vocabulary.
- Do not strip secondary module memberships from shared entries.
- Do not invent noun-to-verb, adjective-to-verb, adverb, or irregular role derivations.
- Do not smuggle combat vocabulary into neutral prose through "target," "attack," "defend," "weapon," "master," or "servant" metaphors.
- Do not convert exact clock time, units, prices, or technical identifiers into ordinary Phi roots.
- Do not use source separation to sanitize, stigmatize, or evade exact testimony.
- Do not write sound symbolism as semantic etymology.
- Do not write articulatory notes as mood or metaphor.
- Do not apply one prose template to a batch.
- Do not trust generated references over canonical JSON.
- Do not trust the validator alone to judge semantic quality, peace-linguistic fit, source fidelity, or voice.

The process is thorough because lost questions are expensive. It should still move. A complete batch ends with decisions in the repository, not with another round of permission-seeking for work Daniel has already authorized.
