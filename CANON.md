# Phi Canon: Which Documents Are Authoritative

When documents disagree, this is the authority order. Anything lower in
the list must be corrected to match anything higher.

## Authority order

1. **`vocabulary/`** — the lexicon JSON files are the single source of
   truth for every word: its form, gloss, IPA, syllables, and meaning.
   A word not in the lexicon does not exist. A gloss in a document that
   contradicts the lexicon is wrong.
2. **Grammar references** — `documents/grammar/PARTICLE_REFERENCE.md`,
   `COMPLEMENTIZER_REFERENCE.md`, `NUMERAL_REFERENCE.md`. These define
   the grammatical system: particle inventory and slot order,
   complementizer pairs, numeral structure.
3. **Grammar chapters** — `documents/grammar/01-*.md` through `06-*.md`.
   Narrative explanations of the system defined in (2).
4. **`manual/`** — the teaching text. Must agree with (1)–(3).
5. **`pamphlets/`** — focused deep-dives. Must agree with (1)–(3).
6. **Philosophy documents** — `documents/language_guide.md`,
   `MODIFIER_FIRST_PHILOSOPHY.md`, and
   `PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT.md`. Authoritative for *why*, not for word forms
   or grammar details.
7. **`archive/`** — historical record only. Never a reference for the
   current language.

`CLAUDE.md` is the working protocol for language development and should
always reflect (1)–(3).

## Settled decisions (2026-07)

These were explicitly decided and should not silently fork again:

- **Aspect inventory**: `ki` (PFV), `si` (IPFV), `pa` (INCH), `te`
  (CESS), `ro` (HAB). There is no `tha`.
- **Slot 1 order**: Tense > Aspect > Voice > Evidentiality > Modality >
  Negation. The order is fixed; negation scope does not move `ma`.
  There are no exceptions to established rules — ever.
- **Modal negation** (settled 2026-07): `po ma V` = cannot (possibility
  denied); `na ma V` = must not (necessity of refraining). "Need not"
  (absence of obligation) is not expressed by reordering; it uses the
  freedom periphrasis: `S lila V ralu nai` — "S is free as to V-ing"
  (`thia lila wepu ralu nai`, you need not go). Absence of obligation
  is stated as presence of freedom.
- **Conditionals**: `lu` (realis) and `lu he` (irrealis), Slot 0 only.
  The conjunction `thoe` is retired.
- **`wela`/`welo`** is the interrogative complementizer pair. The old
  content word `wela` ("good/beautiful") is retired; use `welao`
  (good), `towe` (well), `phelora` (beautiful).
- **Slot 0 combination order**: politeness first — `pi wa …`, `pi no …`.
- **Punctuation**: periods only in Phi text; no commas.
- **Classifiers** (settled 2026-07): four only (himo/lipha/themo/nophe),
  always optional. Nature-now rule: living parts of living beings take
  `lipha`; time units and events take `nophe`; `themo` is for detached
  and crafted objects. The superlative is `mo ko`; the particle `mi`
  is retired. Subordinating conjunctions: pheo, phoe, lao, shai, lila.
- **Embedded clauses** carry their own tense marking; closers
  (`meno`, `welo`, `sholo`) are required.

## Validation

Run before committing anything that touches vocabulary or examples:

```bash
python3 scripts/validate_examples.py
```

It checks lexicon integrity (schema, phonotactics, syllable arrays,
duplicates) and that every Phi word used in documentation examples
exists in the lexicon. Check collision distance before coining:

```bash
python3 scripts/validate_examples.py neighbors <candidate>
```
