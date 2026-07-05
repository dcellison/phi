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
3. **`manual/`** — the teaching text. Must agree with (1)–(2).
4. **`pamphlets/`** — focused deep-dives. Must agree with (1)–(3).
5. **Philosophy documents** — `documents/language_guide.md`,
   `MODIFIER_FIRST_PHILOSOPHY.md`, and
   `PSYCHOLOGICAL_VIOLENCE_OF_MEASUREMENT.md`. Authoritative for *why*, not for word forms
   or grammar details.
6. **`archive/`** — historical record only. Never a reference for the
   current language. (The six narrative grammar chapters were dissolved
   into the manual, July 2026.)

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
- **Covered by design — do not coin** (settled 2026-07): anger is
  `korua thero` and contempt `thiku nila` (compound registry);
  east/west are `sorae thorui`/`sorae lumae`; dream is `whemura`;
  stop/cease is the particle `te`; wife/husband is `telu`; thought
  is `remo` and every other event noun comes by the event-noun
  rule; statement is `phelui`/`haolu` with the complementizers;
  timbre is `haoni welisha`; loneliness composes as `sonu` + `nuhe`;
  greeting is `kia`/`whelani`. The full gap-campaign record, with
  all fourteen rulings, is preserved in `archive/GAP_INVENTORY.md`.
- **Refused by design** (settled 2026-07): gendered person-words
  (woman/man) do not exist and will not — distinguishing genders
  anywhere in the language would exclude people outside the binary;
  `miona` (person), `telu` (partner), `phao` (parent) carry the load
  equally for everyone. Also refused: *hunt*; generic *bad* (things
  are harmful, broken, or unwell — never simply "bad"); *blade* as
  weapon-part (knife exists only as a kitchen/craft tool);
  *marriage* as institution (`telu`, partner, suffices).
- **Classifiers** (settled 2026-07): four only (himo/lipha/themo/nophe),
  always optional. Nature-now rule: living parts of living beings take
  `lipha`; time units and events take `nophe`; `themo` is for detached
  and crafted objects. The superlative is `mo ko`; the particle `mi`
  is retired. Subordinating conjunctions: pheo, phoe, lao, shai, lila.
- **Embedded clauses** carry their own tense marking; closers
  (`meno`, `welo`, `sholo`) are required.
- **Motion and place** (settled 2026-07): the allative is `kau` (to,
  the goal of motion), completing the pair with `lue` (from). `wea`
  is toward without promised arrival; `mua` is the place where an
  action happens, never a motion endpoint; `kamo` (arrive) takes
  `mua`, because arrival is an event at a place.
- **Adjunct order** (settled 2026-07): prepositional phrases stand
  before the direct object — S PP O V (`mia roe kiru wolea kati`,
  `lopia lue phitura phialu kolua`). The circumstances are announced
  before the thing acted on.
- **Clause-initial pronouns** (settled 2026-07): in a predicate
  clause, a bare clause-initial pronoun is the subject — `mia lohau
  nai` can only mean "I am a dog." Predicative possession is not
  expressed by fronting a possessor; use `phelu` (`mia lohau phelu`,
  I have a dog / this dog is mine). Possessive readings of an
  initial pronoun require structure that forces them (`mia lohau
  welao nai`, my dog is good — unambiguous, since "I am a good dog"
  would be `mia welao lohau nai`).
- **`lumae` is a noun only** (settled 2026-07): the old ch25 example
  using it as a verb was corrected (`shero shua.`); noun→verb use of
  noun-only words is an error, not a liberty.
- **Oblique relative gaps** (settled 2026-07): when the relativized
  element is a preposition's object, the preposition remains and its
  object is gapped: `rena mia mua ___ to thalo shelira` (the forest
  that I walked in). The preposition is never dropped and never moves.
- **The event-noun rule** (settled 2026-07): every verb licenses its
  event/result noun with no change of form — `remo` is to think and a
  thought, `thalo` to walk and a walk, `kati` to cut and a cut. This
  is a grammar-level rule, not a per-word fact; entries do NOT list
  "noun" in `pos` for this sense. A listed noun+verb `pos` therefore
  always signals an idiosyncratic pairing that must be learned
  (instrument `kiru`, role `phao`, phenomenon `pheralu`, substance
  `keluo`, entity `haoni`) — the
  word-by-word audit is preserved in `archive/EVENT_NOUN_ADJUDICATION.md`. When a
  counted event noun carries a classifier (always optional), it is
  `nophe` (`ta nophe thalo`, one walk). `whunema` (breathe) is retired: `whunei` is the verb
  breathe, and "a breath" is its rule-derived noun. The rule is
  taught in manual ch15.

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
