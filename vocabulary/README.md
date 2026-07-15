# Phi vocabulary

The JSON entries in this directory are Phi's canonical lexicon. Each file records one word and carries its grammatical and philosophical notes. Generated references and indexes are views of these files; when there is a disagreement, the entry wins.

## Directory map

| Path | Contents |
|---|---|
| [`content/`](content/) | Content words in base vocabulary or one or more optional modules. |
| [`function/`](function/) | Grammatical words, divided into their function classes. |
| [`interjection/`](interjection/) | Conventional whole utterances such as greetings and reactions. |
| [`schema.json`](schema.json) | The machine-readable entry contract and the canonical identifiers for fields, parts of speech, pillars, semantic domains, and modules. |
| [`semantic_domains.md`](semantic_domains.md) | The fifteen semantic domains and the guidance for assigning them. |

Module membership does not create a second lexicon. A content entry may name several optional learning paths in its `modules` array, while the absence of that field places the word in base vocabulary. Either way, the word follows the same grammar.

## The entry contract

An entry's filename comes from its English gloss, and the JSON keeps the field order declared in [`schema.json`](schema.json). The `pos` field holds one lexical class. Every content entry maps at least one `semantic_domains` identifier to a reason that belongs to that word.

The target prose contract requires a definition in `description`, a physical account of pronunciation in `articulatory_notes`, and worked `examples` stored as Phi and English pairs. `search_terms` and `usage_notes` are optional aids. `sound_symbolism` is also optional: it records an honest Phi-specific phonesthetic association when one exists, not a universal claim about sounds or a hidden analysis of the word. `pillars` records only direct, specific relationships, so an entry may have none.

The schema remains transitional while the inherited lexicon is revised. An entry may temporarily use legacy `sound_symbolism` in place of `articulatory_notes`, and legacy `grammatical_notes` in place of structured `examples`. The deprecated `concept` and `grammatical_notes` fields belong only to that migration. New entries and entries that receive a complete prose revision use the target fields.

The validator first runs the complete entry through Draft 2020-12 JSON Schema. It then checks the rules the schema cannot settle: the spoken form, cross-entry collisions, canonical file layout, Phi examples, and the word's place in the lexicon. Slot 1 ordering comes from each particle's `slot1_rank` metadata rather than a second list hidden in the validator. [`documents/validation/vocabulary_prose_coverage.json`](../documents/validation/vocabulary_prose_coverage.json) records how many entries are legacy, partial, dual, or fully target-shaped; validation fails when that report is stale.

## Working on an entry

1. Read the [development protocol](../project/development_protocol.md) and the schema before coining or revising a word.
2. Test a proposed form with `python3 scripts/validate_examples.py neighbors WORD`.
3. Fill the target fields and keep the entry in canonical serialization.
4. Refresh the prose coverage report with `python3 scripts/vocabulary_prose_coverage.py`.
5. Rebuild the manual's derived lexicon with `python3 scripts/generate_reference.py`.
6. Run `python3 scripts/validate_examples.py` as a standalone command and resolve every error and warning.

Install the validator dependency in a new Python environment with `python3 -m pip install --requirement project/requirements.txt` from the repository root.

The website build writes its lexicon view to `build/site/lexicon.json`. The optional SQLite lookup tool writes `build/lexicon.db`. Both are disposable: when either disagrees with a vocabulary entry, rebuild the generated file and believe the JSON.
