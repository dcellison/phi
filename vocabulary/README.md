# Phi vocabulary

The JSON entries in this directory are Phi's canonical lexicon. Each file records one word and carries its grammatical and philosophical notes. Generated references and indexes are views of these files; when there is a disagreement, the entry wins.

## Directory map

| Path | Contents |
|---|---|
| [`content/`](content/) | Content words in base vocabulary or one or more optional modules. |
| [`function/`](function/) | Grammatical words, divided into their function classes. |
| [`interjection/`](interjection/) | Conventional whole utterances such as greetings and reactions. |
| [`schema.json`](schema.json) | The machine-readable entry contract and the canonical identifiers for fields, parts of speech, pillars, semantic domains, and modules. |
| [`semantic_domains.md`](semantic_domains.md) | The thirteen semantic tags, with the reasoning and practical guidance behind them. |

Module membership does not create a second lexicon. A content entry may name several optional learning paths in its `modules` array, while the absence of that field places the word in base vocabulary. Either way, the word follows the same grammar.

## The entry contract

An entry's filename comes from its English gloss, and the JSON keeps the field order declared in [`schema.json`](schema.json). Content entries have one lexical part of speech and at least one semantic-domain tag. A definition draws the useful boundary. Sound symbolism attends to the whole spoken form, while grammatical notes show the word at work.

The validator reads the schema's classifications directly and then checks the rules that JSON Schema cannot settle neatly. It verifies the spoken form, the file layout, and the word's place in the lexicon. Run it after every lexicon change.

## Working on an entry

1. Read the [development protocol](../project/development_protocol.md) and the schema before coining or revising a word.
2. Test a proposed form with `python3 scripts/validate_examples.py neighbors WORD`.
3. Fill every required field and keep the entry in canonical serialization.
4. Rebuild the manual's derived lexicon with `python3 scripts/generate_reference.py`.
5. Run `python3 scripts/validate_examples.py` as a standalone command and resolve every error and warning.

The website build writes its lexicon view to `build/site/lexicon.json`. The optional SQLite lookup tool writes `build/lexicon.db`. Both are disposable: when either disagrees with a vocabulary entry, rebuild the generated file and believe the JSON.
