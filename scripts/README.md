# Phi Vocabulary Management Scripts

The vocabulary JSON files under `vocabulary/` are the single source of
truth. These scripts validate them and keep the SQLite index in sync.

## validate_examples.py — the main validator

Checks the entire language for internal consistency:

- **Lexicon integrity**: required schema fields, no undeclared fields,
  valid pillar keys, phonotactic legality of every word, `syllables`
  arrays matching canonical hiatus syllabification, duplicate words,
  duplicate glosses (warning).
- **Documentation examples**: every Phi word used in examples in
  `documents/`, `manual/`, `pamphlets/`, and `CLAUDE.md` must exist in
  the vocabulary. Works on fenced code blocks and *italicized* spans.
- **Collision check for new coinages**: `neighbors WORD` lists every
  existing word within edit distance 1 of a candidate.

```bash
python3 scripts/validate_examples.py                 # full check
python3 scripts/validate_examples.py --lexicon-only
python3 scripts/validate_examples.py --docs-only
python3 scripts/validate_examples.py --paths manual/part4_grammar
python3 scripts/validate_examples.py --show-warnings
python3 scripts/validate_examples.py neighbors phika # before coining
```

Exit code 0 means no errors. Run the full check before every commit
that touches vocabulary or documentation examples.

Known limitation: single-word *italic* mentions in prose are not checked
(the English/Phi heuristic needs at least two tokens). When retiring or
renaming a word, grep for it explicitly.

## check_duplicates.py

Strict duplicate word/gloss checker across all vocabulary JSON.
Exits non-zero if any duplicates exist.

## lexicon_tool_simple.py

Lightweight SQLite index (`lexicon.db`) over the JSON files, for fast
lookups. Scans `vocabulary/content/`, `vocabulary/function/` (recursive),
and `vocabulary/interjection/`. Glosses may repeat; words may not.

```bash
python3 scripts/lexicon_tool_simple.py init     # rebuild from JSON
python3 scripts/lexicon_tool_simple.py find WORD_OR_GLOSS
python3 scripts/lexicon_tool_simple.py view WORD
python3 scripts/lexicon_tool_simple.py list
python3 scripts/lexicon_tool_simple.py sync
```

Note: `find` exits 1 when the term EXISTS (i.e. "not available for
coinage") and 0 when it is free.

## Formatters

`format_json.py`, `reformat_json.py`, `reformat_json_compact.py`,
`batch_format.py`, `standardize_ipa.py` — JSON/IPA formatting utilities.

## deprecated/

Scripts that no longer match the repository layout and produce wrong
results. See `deprecated/README.md` before touching anything in there.
