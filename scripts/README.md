# Phi Vocabulary Management Scripts

The vocabulary JSON files under `vocabulary/` are the single source of truth. These scripts validate them, keep the derived artifacts in sync, and support coining. All of them are pure standard-library Python.

## validate_examples.py — the main validator

Checks the entire language for internal consistency, and runs in CI on every pull request:

- **Lexicon integrity**: required schema fields, no undeclared fields, valid pillar, semantic-domain, and optional-module classifications, phonotactic legality of every word, `syllables` arrays matching canonical hiatus syllabification, canonical IPA and serialization, gloss-derived filenames, duplicate words, duplicate glosses (warning).
- **Minimal-pair ratchet**: two content words at edit distance 1 are an error unless grandfathered in `documents/minimal_pairs_baseline.txt`, which may only shrink.
- **Documentation examples**: every Phi word quoted in `documents/`, `project/`, `manual/`, `pamphlets/`, `primer/`, `texts/`, `CLAUDE.md`, `kia.md`, and `README.md` must exist in the vocabulary, except a valid productive name-form selected by `ne`. Works on fenced code blocks and *italicized/bold* spans.
- **Source citations**: every labeled literary citation must occur verbatim in its stored source. A source clause belongs to one aligned unit, except on a declared paired page where it may appear once in each named rendering.
- **Productive names**: after `ne`, a name-form absent from the current lexicon must be lowercase, content-shaped, and two, three, or four syllables. Any legal four-syllable candidate is accepted without consulting lexical history. A name may match a current lexicon entry only when that entry is a content word; every current function and other non-content form remains unavailable.
- **Three-syllable ceiling**: every lexical form must have at most three syllables, with no exception. The finite migration ledger records completed replacements rather than authorizing old forms.
- **Compound registry**: every member word of a compound in `documents/compounds.md` must exist in the lexicon, no registry row repeats, and the generated Part VII compound reference must match what the registry would generate.
- **Collision check for new coinages**: `neighbors WORD` lists every existing word within edit distance 1 of a candidate.

```bash
python3 scripts/validate_examples.py                 # full check
python3 scripts/validate_examples.py --lexicon-only
python3 scripts/validate_examples.py --docs-only
python3 scripts/validate_examples.py --paths manual/part4_grammar
python3 scripts/validate_examples.py --show-warnings
python3 scripts/validate_examples.py neighbors phika # before coining
python3 scripts/validate_examples.py name samira    # before using an onym
```

Exit code 0 means no errors. Run the full check — as its own command, so the exit code is not swallowed by a pipeline — before every commit that touches vocabulary or documentation examples.

Known limitation: single-word *italic* mentions in prose are not checked (the English/Phi heuristic needs at least two tokens). When retiring or renaming a word, grep for it explicitly.

The focused regression suite covers the productive-name open class, unconditional four-syllable name acceptance, current non-content exclusion, short retired lexical forms, the completed migration ledger, and the absence of long lexicon entries:

```bash
python3 scripts/test_name_forms.py
```

## generate_reference.py

Regenerates the Part VII alphabetical, semantic-domain, optional-module, and part-of-speech lexicon references under `manual/part7_reference/lexicon/`, and the Part VII compound reference (`manual/part7_reference/compounds.md`) from `documents/compounds.md`. Must run after any vocabulary or compound-registry change; the validator fails if a committed reference drifts from its source. The registry parser the validator and both build scripts share lives in `compound_registry.py`.

```bash
python3 scripts/generate_reference.py
```

## build_site.py

Builds the complete deployment tree under `build/site/`. It copies the maintained assets from `site/`, generates the explorer's vocabulary and compound data, and renders the primer, manual, book, texts, and pamphlets. Optional module metadata powers the explorer's module filter, nested Part VII module chapters appear in the manual site, and registered compounds appear in search results and on their member words' entries.

```bash
python3 scripts/build_site.py
python3 -m http.server -d build/site  # then open http://localhost:8000
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

## audit_phonetic_neighbors.py

Ranks lexicon pairs by phoneme-unit and feature-weighted similarity, with function-word and corpus-attestation context. It complements the validator's character-distance rule; it never makes an automatic rename decision.

```bash
python3 scripts/audit_phonetic_neighbors.py --output documents/phonetic_neighbors_baseline.txt
python3 scripts/audit_phonetic_neighbors.py --candidate proposed_word
python3 scripts/audit_phonetic_neighbors.py --kind function --prompts 40 --seed 202601
```

Retired one-off scripts live in `archive/scripts/`; everything in this directory is current and in use.
