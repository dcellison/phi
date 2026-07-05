# Phi Canon: Which Documents Are Authoritative

When documents disagree, this is the authority order. Anything lower in
the list must be corrected to match anything higher.

## Authority order

1. **`vocabulary/`** — the lexicon JSON files are the single source of
   truth for every word: its form, gloss, IPA, syllables, and meaning.
   A word not in the lexicon does not exist. A gloss in a document that
   contradicts the lexicon is wrong.
2. **Grammar references** — `documents/grammar/particle_reference.md`,
   `complementizer_reference.md`, `numeral_reference.md`. These define
   the grammatical system: particle inventory and slot order,
   complementizer pairs, numeral structure.
3. **`manual/`** — the teaching text. Must agree with (1)–(2).
4. **`pamphlets/`** — focused deep-dives. Must agree with (1)–(3).
5. **Philosophy documents** — `documents/language_guide.md`,
   `modifier_first_philosophy.md`, and
   `psychological_violence_of_measurement.md`. Authoritative for *why*, not for word forms
   or grammar details.
6. **`archive/`** — historical record only. Never a reference for the
   current language. (The six narrative grammar chapters were dissolved
   into the manual, July 2026.)

`documents/development_protocol.md` is the working protocol for language
development and should always reflect (1)–(3); `CLAUDE.md` is a thin
tool shim that points at it.

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
- **Punctuation** (extended 2026-07-05): the period is Phi's only
  visible punctuation — no commas, question marks, or exclamation
  marks, in any mode of writing. Phi's punctuation is spoken: the
  question mark is `wa`, the quotation marks are `shola` and
  `sholo`, the comma of address is `kona`, the clause commas are the
  closers and the Slot 0 announcers, and the capital letter of a
  name is `ne`. A silent mark is justified only where no word is
  visible to do its work; sentence-end is the one such place, so the
  period is the one such mark. Pauses are free — no pause can change
  a Phi sentence's meaning — so none is ever written. The validator
  enforces all of this.
- **Letters** (settled 2026-07-05): Phi has no capital letters — not
  for sentences, not for names. Romanization is one mode of writing
  Phi among peers (the Tengwar mode, the glyph mode); a mark may
  carry meaning only if every mode can carry it, and case exists
  only in Latin script. What capitals do for names, `ne` does aloud.
  The validator enforces lowercase.
- **Names are made of Phi** (settled 2026-07-05): a person's name is
  a lexicon word borne as a name, announced by `ne` (plus any
  honorific) — the recurring cast: `sulae` (warm, the honored
  friend), `siora` (joy, the visiting child), `thinoe` (seed, the
  elder's elder), `moli` (gentle, the beloved of the intimate
  examples), `keruko` (sturdy, the neutral-register everyman).
  Because names are words, the collision rules protect them and the
  validator needs no whitelist. Formal speech keeps `ne`; family
  speech may drop it — the primer shows this rather than stating it.
  Names are lowercase everywhere, including gloss lines and English
  narration.
- **Main-clause tense** (settled 2026-07-05): tense particles are
  not optional — a clause whose translation is past carries `to` on
  its own verb (`sholo to haolu`, they said), as ch15 requires and
  the texts practice. An unmarked verb is present. Embedded clauses
  keep their own marking, relative to the matrix event (see the
  embedded-clauses ruling below).
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
  *marriage* as institution (`telu`, partner, suffices); the
  vocabulary of domination — *to rule*, *lord/master*, *throne*,
  *bind-as-captivity* — refused 2026-07-05 and demonstrated in the
  Ring Verse refusal (`pamphlets/ring_verse_refusal.md`): the
  nearest words are `kulo` (guide), `theluo` (steward), and `nolami`
  (bond, which is mutual by definition).
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
- **Gloss lines** (settled 2026-07-05): the GLOSS line beneath a Phi
  example renders every word by its lexicon gloss, verbatim — function
  words by their uppercase labels (PROX, ABL, UNIV, THING.CLF, …),
  content words by the bare gloss even in rule-derived senses (`kealo`
  the noun still glosses "create"; the event-noun rule stays visible).
  Parenthetical disambiguators in a gloss field ("spring (season)")
  are dropped in gloss lines. Sense belongs to the free-translation
  line: "wonder" is what `wela … welo` around feel *means*, and the
  gloss line shows that composition rather than hiding it.
- **Predicative deictics** (settled 2026-07-05): `ha` and `ra` stand
  alone as locative predicates with `nai` — `mia ha nai` (I am here),
  `shia ra nai` (they are there) — as the manual's deixis section
  teaches; the lexicon entries record both uses. No separate
  here/there nouns exist or are needed.
- **Quotative frame verbs** (settled 2026-07-05): `shola … sholo`
  closes with a verb of speaking or of receiving speech — `haolu`,
  `shemui`, `thilou`, `hea`. The closer bounds the quote either way;
  hearing exact words is as sayable as speaking them.
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
