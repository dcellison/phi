# Phi repository scripts

The entry JSON under `vocabulary/content/`, `vocabulary/function/`, and `vocabulary/interjection/` is the single source of truth. [`vocabulary/schema.json`](../vocabulary/schema.json) owns the shared field and classification metadata. These scripts validate the entries, keep derived artifacts in sync, and support coining. Install the validator's pinned dependency once in each Python environment:

```bash
python3 -m pip install --requirement project/requirements.txt
```

## validate_examples.py — the main validator

Checks the entire language for internal consistency, and runs in CI on every pull request:

- **Lexicon integrity**: complete Draft 2020-12 schema validation, phonotactic legality of every word, `syllables` arrays matching canonical hiatus syllabification, canonical IPA and serialization, gloss-derived filenames, structured Phi examples, prose-contract coverage, duplicate words, and duplicate glosses (warning).
- **Minimal-pair ratchet**: two content words at edit distance 1 are an error unless grandfathered in `documents/validation/minimal_pairs_baseline.txt`, which may only shrink.
- **Documentation examples**: every Phi word quoted in `documents/`, `project/`, `manual/`, `pamphlets/`, `primer/`, `texts/`, `CLAUDE.md`, `kia.md`, and `README.md` must exist in the vocabulary, except a valid productive name-form selected by `ne`. The validator checks fenced code blocks and *italicized/bold* spans. It also rejects a noun phrase that combines `lo` with a numeral or quantifier while preserving deliberately marked counterexamples.
- **Source citations**: every labeled literary citation must occur verbatim in its stored source, and each source clause belongs to one aligned unit.
- **Productive names**: after `ne`, a name-form absent from the current lexicon must be lowercase, content-shaped, and two, three, or four syllables. Any legal four-syllable candidate is accepted without consulting lexical history. A name may match a current lexicon entry only when that entry is a content word; every current function and other non-content form remains unavailable.
- **Three-syllable ceiling**: every lexical form must have at most three syllables, with no exception. The finite migration ledger records completed replacements rather than authorizing old forms.
- **Compound registry**: every member word of a compound in `documents/reference/compounds.md` must exist in the lexicon, no registry row repeats, and the generated Part VII compound reference must match what the registry would generate.
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

## validate_sentences.py: the full-sentence parser

Parses complete Phi utterances independently of the main lexical validator. The syntax tree holds each sentence frame, embedded clause, and predicate. Separate checks cover the three particle slots, numerals, prepositions, and the modifier-first positions that the surface makes determinate.

```bash
python3 scripts/validate_sentences.py
python3 scripts/test_sentence_validator.py
python3 scripts/validate_sentences.py --sentence "thepalu thiku to nai." --show-tree
python3 scripts/validate_sentences.py --paths manual/part4_grammar
python3 scripts/validate_sentences.py --docs
```

The default command checks every structured vocabulary example and the maintained teaching corpus: canon, grammar references, manual, pamphlets, primer, book, Kia, and the Short Road. `--paths` checks selected active Markdown beside the lexicon, `--lexicon-only` narrows the run to dictionary examples, and `--docs` extends the parser to every recognized complete example in active Markdown; `archive/` is excluded. Literary texts and older evaluation material remain a migration audit until each area has been reviewed. The parser's contract and limits are recorded in [`documents/validation/sentence_validator.md`](../documents/validation/sentence_validator.md).

The focused regression suites cover:

- the executable vocabulary contract, its required prose shape, and rejection of retired prose fields;
- Slot 1 metadata and Slot 2 quantity alternatives;
- the productive-name open class, four-syllable names, and non-content exclusions;
- retired lexical forms, the completed migration ledger, and the three-syllable vocabulary limit.

```bash
python3 scripts/test_vocabulary_schema.py
python3 scripts/test_name_forms.py
python3 scripts/test_sentence_validator.py
```

## content_vocabulary_decisions.py

Validates the canonical content-vocabulary decision register in `project/content_vocabulary_decisions.json` and generates its readable Markdown view. The check requires every registered batch and carried-forward lexical question to have an explicit state. It verifies reciprocal links, batch closure, implementation evidence, and coverage-ledger IDs, then compares the decision-count snapshot in `project/handoff/current_state.md` with the live register.

```bash
python3 scripts/content_vocabulary_decisions.py --write
python3 scripts/content_vocabulary_decisions.py --check
python3 scripts/test_content_vocabulary_decisions.py
```

## vocabulary_prose_coverage.py

Writes the committed contract report at `documents/validation/vocabulary_prose_coverage.json`. Each entry is classified as legacy, partial, dual, or target according to its prose fields. The first three shapes are schema-invalid, but keeping them visible in the report makes a regression plain. The main validator compares the report with the live lexicon and fails when a vocabulary edit leaves it stale.

```bash
python3 scripts/vocabulary_prose_coverage.py
```

## generate_reference.py

Regenerates the Part VII alphabetical, semantic-domain, optional-module, and part-of-speech lexicon references under `manual/part7_reference/lexicon/`, and the Part VII compound reference (`manual/part7_reference/compounds.md`) from `documents/reference/compounds.md`. Must run after any vocabulary or compound-registry change; the validator fails if a committed reference drifts from its source. The registry parser the validator and both build scripts share lives in `compound_registry.py`.

```bash
python3 scripts/generate_reference.py
```

## build_site.py

Builds the complete deployment tree under `build/site/`. It copies the maintained assets from `site/`, generates the explorer's vocabulary and compound data, and renders the primer, manual, book, texts, and pamphlets. Optional module metadata powers the explorer's module filter, nested Part VII module chapters appear in the manual site, and registered compounds appear in search results and on their member words' entries. The ordered reading shelves and their display metadata come from `texts/catalogue.json` and `pamphlets/catalogue.json`; the build rejects catalogue entries that drift from the content directories.

```bash
python3 scripts/build_site.py
python3 -m http.server -d build/site  # then open http://localhost:8000
```

## lexicon_tool_simple.py

Lightweight SQLite index (`build/lexicon.db`) over the JSON files, for fast lookups. Scans `vocabulary/content/`, `vocabulary/function/` (recursive), and `vocabulary/interjection/`. Glosses may repeat; words may not.

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
python3 scripts/audit_phonetic_neighbors.py --output documents/validation/phonetic_neighbors_baseline.txt
python3 scripts/audit_phonetic_neighbors.py --candidate proposed_word
python3 scripts/audit_phonetic_neighbors.py --kind function --prompts 40 --seed 202601
```

## translation_layers.py

Builds the isolated working views required by D102. The source-to-Phi view exposes only numbered Phi units and their decoded source citations. That view can itself become the input to the Phi-to-English phase, so a new translation may begin in the same two-layer format before any gloss or natural English exists.

The recommended Phi-to-English command writes bounded anonymous packets, a shared compact reference, and a JSON manifest. The reference contains compact records for only the lexical forms and registered compounds used by the selected units. Each packet includes stable unit numbers and hashes, the complete frozen-stream digest, a generated lexical gloss scaffold, structural review flags, and a response template that requires clause analysis before the exact gloss and natural English. The scaffold supplies token glosses but leaves structural brackets to that analysis. A single source-blind context reads the reference once and then handles packets in order.

`--audit-only` selects every unit whose structure crosses the independent-audit threshold, then adds a deterministic ten-percent sample of the remainder. The manifest records both groups. `--units` makes a small fresh packet after a frozen unit changes, so unaffected English does not have to be derived again. A single-file `--output` remains available for short work and retries.

```bash
python3 scripts/translation_layers.py texts/north_wind_and_sun.md --phase source-to-phi --output /tmp/north_source_phi.md
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --output-dir /tmp/north_derive --batch-size 8
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --audit-only --output-dir /tmp/north_audit --batch-size 8
python3 scripts/translation_layers.py /tmp/north_source_phi.md --phase phi-to-english --units 3,7-8 --output /tmp/north_retry.md
python3 scripts/translation_layers.py texts/north_wind_and_sun.md --digest-only
python3 scripts/test_translation_layers.py
```

## translation_process_status.py

Validates the complete D102 certification queue and generates its readable ledger. Standalone translations and Gibran selections come from their catalogues; every catalogued book must declare whether the process applies, and the current *News from Nowhere* chapter glob supplies that book's documents. A certified row records both the frozen Phi digest and a digest over all four published layers, so later drift in Phi, gloss, derived English, or source citations stops CI.

```bash
python3 scripts/translation_process_status.py --write
python3 scripts/translation_process_status.py --check
python3 scripts/test_translation_process_status.py
```

## Tengwar renderer and extractor

`tengwar.py` converts validated romanized Phi into deterministic inline SVG using the committed outlines in `tengwar/glyphs.json`. The site build uses it for paired examples in the Tengwar pamphlet; it does not attempt to render foreign source material.

`extract_tengwar_glyphs.py` rebuilds that JSON from `tengwar/fonts/TengwarTelcontar.ttf` while preserving hand-tuned placement adjustments. It is a manual maintenance tool, not part of an ordinary build, and requires `fontTools`.

Retired one-off scripts live in `archive/scripts/`; everything in this directory is current and in use.
