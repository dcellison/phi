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
  stop/cease is the particle `te`; wife/husband is `tewema`; thought
  is `remo` and every other event noun comes by the event-noun
  rule; statement is `phelui`/`haolu` with the complementizers;
  timbre is `haoni welisha`; loneliness composes as `sonu` + `nuhe`;
  greeting is `kia`/`whelani`. The full gap-campaign record, with
  all fourteen rulings, is preserved in `archive/GAP_INVENTORY.md`.
- **Refused by design** (settled 2026-07): gendered person-words
  (woman/man) do not exist and will not — distinguishing genders
  anywhere in the language would exclude people outside the binary;
  `miona` (person), `tewema` (partner), `phao` (parent) carry the load
  equally for everyone. Also refused: *hunt*; generic *bad* (things
  are harmful, broken, or unwell — never simply "bad"); *blade* as
  weapon-part (knife exists only as a kitchen/craft tool);
  *marriage* as institution (`tewema`, partner, suffices); the
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
  "noun" in `pos` for this sense — and since the things-do-not-verb
  ruling (below), no entry lists noun and verb together at all. The
  word-by-word audit is preserved in `archive/EVENT_NOUN_ADJUDICATION.md`. When a
  counted event noun carries a classifier (always optional), it is
  `nophe` (`ta nophe thalo`, one walk). `whunema` (breathe) is retired: `whunei` is the verb
  breathe, and "a breath" is its rule-derived noun. The rule is
  taught in manual ch15.
- **Things do not name their deeds** (settled 2026-07-05): the
  noun→verb direction is refused. The 45 idiosyncratic dual listings
  (instruments, roles, phenomena, substances, artifacts, entities)
  were pruned to a single part of speech; no entry lists both noun
  and verb, and the validator enforces it. What a thing does is said
  with a verb: `pheralu lepa` (rain falls), `mia roe kiru wolea
  kati` (I cut the wood with the chisel), `thema nai` (is a
  guardian), `phao lopia numelo` (the parent nurtures the child).
  The event-noun rule is the only bridge between verb and noun and it
  runs one way: a deed names its event; a thing does not name its
  deed. One word changed direction rather than losing one: `kulo`
  (guide) was verb-primary all along — the Ring Verse refusal's own
  poem uses it (`ta sorui theula miona kulo`) — so it keeps the verb
  and sheds the role-noun (`rena kulo miona`, the one who guides).
- **Qualities and their names** (settled 2026-07-06): every
  adjective licenses its quality noun with no change of form —
  `thua` fair and fairness, `siloma` simple and simplicity — a
  grammar-level rule mirroring the event-noun rule; entries do NOT
  list "noun" for this sense. The reverse direction needs no rule:
  a noun standing before a noun already modifies it, as ch13 has
  always taught for possession — `nitho ruela` (the north path),
  `wheo kowela` (the elder council) — and meaning chooses the
  reading. The 24 adjective+noun dual listings were pruned to a
  single class (14 nouns, 10 adjectives, adjudicated by primary
  sense in `archive/quality_noun_adjudication.md`); the validator
  refuses the combination. One word, one class; position and the
  two one-way rules do all the bridging.

- **The unmarked sentence claims no source** (settled 2026-07-05): an
  unmarked sentence is a plain assertion — it states the fact and names
  no source. Direct knowledge is the natural assumption for present,
  perceivable events, but the grammar claims nothing; `hi` exists
  precisely so witnesshood can be claimed explicitly and accountably.
  Marking settled knowledge manufactures doubt; the unmarked form is
  the system's resting state.
- **`si` and `ro` do not overlap** (settled 2026-07-05): `si` is
  ongoing/progressive only — action in mid-flow; `ro` is
  habitual/characteristic only — the pattern an action wears across
  occasions (`misheko ro nulae`). Habits never take `si`.
- **`ki` completes at the tense's reference time** (settled
  2026-07-05): `ki` = have done (complete as of now), `to ki` = had
  done, `so ki` = will have done — as the lexicon entry and ch15 have
  always said; the stray "have done" translations of `to ki` were the
  error.
- **One per rank** (settled 2026-07-05): each Slot 1 rank admits at
  most one particle per clause — one tense, one aspect, one source,
  one modal — with a single ruled pairing inside voice: `se ka`, the
  passive of a causative. Complexity otherwise goes into more clauses,
  not thicker stacks; two sources are two sentences.
- **`ka` is voice** (settled 2026-07-05): the causative restructures
  arguments, exactly as the passive does, and claims nothing about
  certainty or obligation; it sits in the Voice rank beside `se`.
  Within the rank the order is fixed `se ka` (`lopia se ka nulae`, the
  child is made to sleep). With modals, voice precedes modality:
  `ka na` (must make), `ka po` (can make), the modal scoping the whole
  caused event. `ka ma` denies the causation itself (`mia lopia to ka
  ma nulae`, I did not make the child sleep); caused refraining is
  said with its own verb or two clauses.
- **`li` is a fence, not a sigh** (settled 2026-07-05): `li` restricts
  identity — `li shia sano` (only they know), `li nosa` (only now) —
  and is refused on quantities: exact counts and `henoi` carry
  quantity-honesty. "Only three eggs" is a count plus a feeling, and
  Phi states the count.
- **Slot 2 nests** (settled 2026-07-05): within a phrase, wider
  relations stand earlier — `we`/`li` > `ha`/`ra` > `lo`/numerals >
  `ko` > `ru`/`mo` > the word — modifier-first applied inside the
  phrase (attested: `ha lo ru phelora peloru`). `we` and `li` do not
  stack with each other; the pair micro-orders stand (`mo ko`, `ne`
  before any honorific, `nu` before its numeral).

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
