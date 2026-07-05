# Phi Vocabulary Management Scripts

The vocabulary JSON files under `vocabulary/` are the single source of truth. These scripts validate them, keep the derived artifacts in sync, and support coining. All of them are pure standard-library Python.

## validate_examples.py — the main validator

Checks the entire language for internal consistency, and runs in CI on every pull request:

- **Lexicon integrity**: required schema fields, no undeclared fields, valid pillar keys, phonotactic legality of every word, `syllables` arrays matching canonical hiatus syllabification, canonical IPA and serialization, gloss-derived filenames, duplicate words, duplicate glosses (warning).
- **Minimal-pair ratchet**: two content words at edit distance 1 are an error unless grandfathered in `documents/minimal_pairs_baseline.txt`, which may only shrink.
- **Documentation examples**: every Phi word quoted in `documents/`, `manual/`, `pamphlets/`, `primer/`, `CLAUDE.md`, `kia.md`, and `README.md` must exist in the vocabulary. Works on fenced code blocks and *italicized/bold* spans.
- **Collision check for new coinages**: `neighbors WORD` lists every existing word within edit distance 1 of a candidate.

```bash
python3 scripts/validate_examples.py                 # full check
python3 scripts/validate_examples.py --lexicon-only
python3 scripts/validate_examples.py --docs-only
python3 scripts/validate_examples.py --paths manual/part4_grammar
python3 scripts/validate_examples.py --show-warnings
python3 scripts/validate_examples.py neighbors phika # before coining
```

Exit code 0 means no errors. Run the full check — as its own command, so the exit code is not swallowed by a pipeline — before every commit that touches vocabulary or documentation examples.

Known limitation: single-word *italic* mentions in prose are not checked (the English/Phi heuristic needs at least two tokens). When retiring or renaming a word, grep for it explicitly.

## generate_reference.py

Regenerates the Part VII lexicon reference (`manual/part7_reference/lexicon/`) from the vocabulary. Must run after any vocabulary change; CI fails if the committed reference drifts from the vocabulary.

```bash
python3 scripts/generate_reference.py
```

## build_explorer.py

Bundles the vocabulary into `web/lexicon.json` (generated, gitignored) for the lexicon explorer.

```bash
python3 scripts/build_explorer.py
python3 -m http.server -d web        # then open http://localhost:8000
```

## lexicon_tool_simple.py

Lightweight SQLite index (`lexicon.db`) over the JSON files, for fast lookups. Scans `vocabulary/content/`, `vocabulary/function/` (recursive), and `vocabulary/interjection/`. Glosses may repeat; words may not.

```bash
python3 scripts/lexicon_tool_simple.py init     # rebuild from JSON
python3 scripts/lexicon_tool_simple.py find WORD_OR_GLOSS
python3 scripts/lexicon_tool_simple.py view WORD
python3 scripts/lexicon_tool_simple.py list
python3 scripts/lexicon_tool_simple.py sync
```

Note: `find` exits 1 when the term EXISTS (i.e. "not available for coinage") and 0 when it is free.

Retired one-off scripts live in `archive/scripts/`; everything in this directory is current and in use.
