# Phi Canon: Which Documents Are Authoritative

When documents disagree, this is the authority order. Anything lower in
the list must be corrected to match anything higher.

## Authority order

1. **`vocabulary/`** — the lexicon JSON files are the single source of
   truth for every lexical word: its form, gloss, IPA, syllables, and
   meaning. A lexical word not in the lexicon does not exist. Productive
   name-forms licensed by `ne` are proper designations rather than lexical
   words and gain no gloss or dictionary meaning. A gloss in a document
   that contradicts the lexicon is wrong.
2. **Grammar references** — `documents/grammar/particle_reference.md`,
   `complementizer_reference.md`, `numeral_reference.md`. These define
   the grammatical system: particle inventory and slot order,
   complementizer pairs, numeral structure.
3. **`manual/`** — the teaching text. Must agree with (1)–(2).
4. **`texts/`** — translations and transmutations. Must agree with (1)–(3).
5. **`pamphlets/`** — focused deep-dives. Must agree with (1)–(3).
6. **Design rationale:** `documents/reference/language_guide.md`, `documents/design/modifier_first_philosophy.md`, and `documents/design/psychological_violence_of_measurement.md`. Authoritative for *why*, not for word forms or grammar details.
7. **`archive/`** — historical record only. Never a reference for the
   current language. (The six narrative grammar chapters were dissolved
   into the manual, July 2026.)

`project/development_protocol.md` is the working protocol for language development and should always reflect (1) through (3); `CLAUDE.md` is a thin tool shim that points at it.

## Governing description

Phi is a philosophical constructed language for practising mindful and compassionate speech. It asks speakers to attend to the present utterance: what they know, what they intend, and how their words may enter a relationship. Its unhurried quality is freedom from needless haste, not a prescribed speaking speed.

## Settled decisions (2026-07 / Phi 2026.2)

These were explicitly decided and should not silently fork again:

- **Mindful speech, not mandatory slowness** (settled 2026-07-14): the governing description above draws openly on Buddhist mindfulness and Right Speech, while peace linguistics extends its attention to relationship, power, repair, and nonviolence. Slow speech may be a useful exercise or a natural result of careful articulation, but fluent Phi may be quick when the occasion calls for it; tempo is neither a virtue nor evidence of mindfulness. Grammar can make choices available and audible, but it cannot undertake the practice for the speaker.
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
  (good), `towe` (well), `mioru` (beautiful).
- **Slot 0 combination order**: politeness first — `pi wa …`, `pi no …`.
- **Punctuation** (revised 2026-07-10): the period is Phi's only visible punctuation. Phi's punctuation is spoken: the question mark is `wa`, the quotation marks are `shola` and `sholo`, the comma of address is `kona`, the clause commas are the closers and Slot 0 announcers, and the capital letter of a name is `ne`. A silent mark is justified only where no word is visible to do its work; sentence-end is the one such place, so the period is the one such mark. Pauses are free and cannot change a Phi sentence's meaning. Source material presented outside Phi follows the punctuation convention of its own medium and is not parsed as part of the Phi sentence. The validator enforces the Phi rule.
- **Letters** (revised 2026-07-10): Phi has no capital letters, including for names. Romanization is one mode of writing among peers, including Tengwar and the glyph mode; a mark may carry Phi meaning only if every mode can carry it, while case belongs only to some outside writing systems. What capitals do for Phi-form names, `ne` does aloud. Source material outside a Phi passage retains its own script and case without becoming Phi. The validator enforces lowercase in Phi text.
- **`ne` licenses a name atom** (revised 2026-07-10): `ne` announces that the following Phi token is a proper designation, not that its bearer is a person and not that its form is vocabulary. It may name a person, animal, place, community, institution, work, event, or artifact. A name atom may be a content word borne as a name (`ne sulae`) or one productive Phi-form onym (`ne samira`). An honorific, when present, stands between `ne` and the atom.
- **Productive Phi-form onyms** (revised 2026-07-12): a speaker may choose a lowercase, single-token name-form of two, three, or four Phi syllables. It follows ordinary phonotactics, including open syllables, the three-vowel constraint, and no duplicated syllable with an onset. It remains a proper designation rather than a lexicon entry, so it has no shared gloss or part of speech; the register rule below governs when `ne` may be omitted. Names are an open class and do not enter the lexicon's minimal-pair baseline. Every otherwise valid four-syllable form is available as an onym without a retirement or migration check. If a proposed name matches a current lexicon entry, that entry must be a content word; no current function or other non-content word can also be a name. A form absent from the current lexicon follows the ordinary onym charter whether it is new or retired, and name use restores no former meaning or lexical status. The bearer or relevant naming community controls whether an adapted form represents the name.
- **Name register and source names** (revised 2026-07-12): formal, neutral, portable, and machine-validated Phi keeps `ne` at every mention. Conversational or household speech may omit it after a referent is established and while reference remains unambiguous; keeping `ne` is always correct. Phi-form names are lowercase everywhere. A source name with five or more syllables, multiple tokens, a non-Phi shape, or dependence on another script remains outside the Phi passage unless the bearer or naming community accepts a valid Phi-form onym.
- **Three-syllable lexical ceiling** (settled 2026-07-10; completed 2026-07-12): every current and future Phi lexicon word is limited to one, two, or three syllables. Modules receive no exception, and the validator has no temporary allowance. Productive onyms are proper designations rather than lexical words and may have two, three, or four syllables under their separate charter. The four-syllable migration ledger records the 112 completed replacements; it is a history of lexical change, not a list of forms reserved from names.
- **Sun and star lexical family** (settled 2026-07-12): `sileta` names the sun, the particular star Earth orbits, while `silero` names the wider class of stars. Their shared `si.le` opening marks audible kinship without creating a productive affix or a minimal pair. The former sun word `sorae` is retired from vocabulary and unavailable for lexical reassignment; it remains an eligible onym under the productive-name charter.
- **Beautiful and beauty share one root** (settled 2026-07-15): `mioru` is the adjective beautiful, and the ordinary quality-noun rule gives it the noun use beauty without a second lexical entry. The former adjective `phelora` is retired from vocabulary and unavailable for lexical reassignment; it remains an eligible onym under the productive-name charter.
- **Warm and hot lexical boundary** (settled 2026-07-15): `sulae` names moderate warmth, while `sukaro` names heat that is strongly felt. `neri` remains cool and `pelui` cold. The form `ru sulae` remains very warm; `sukaro` states hot without asking the intensifier to supply a second lexical meaning. The shared `su` opening in `sulae`, `sukaro`, and `suloru` gives the thermal family an audible link without creating a productive affix.
- **Basic dimension and distance boundaries** (settled 2026-07-15): `ponalu` names overall physical size before a speaker judges it large or small. `waleru` names spatial end-to-end length, while `mosha` retains bounded duration. `hirawo` names spatial separation; route length, travel time, and effort remain separate facts. `whalo` and `thiku` describe overall size; `laeno` and `teku` describe end-to-end length or duration; `losha` and `hieru` describe width; `raelu` and `mulu` describe vertical extent or position. `noshi` and `wuero` are the ordinary adjectival near/far pair for space and time, while `pai` and `woe` introduce an explicit reference object. The unused adjective `thaeru` is retired because it duplicated `wuero`; the form remains eligible as an onym under the productive-name charter but cannot return to the lexicon.
- **Source material remains outside Phi** (settled 2026-07-10): foreign wording, source-script names, source-form exact values and records, identifiers, formulas, quotations, legal text, medical records, citations, and other unassimilated artifacts appear beside or around Phi through the surrounding document, interface, or conversation. Phi may point to, describe, translate, or analyze that material, but source tokens occupy no Phi syntactic position. An exact integer within Phi's numeral range may also be rendered as Phi when that rendering is adequate; the source form remains separately preserved whenever its notation, unit, identity, or fidelity matters. This separation preserves script parity and does not imply approval, condemnation, or loss of precision.
- **Finite ternary numerals and audible operands** (settled 2026-07-11): exact Phi integers run from `mu` (0) through `wi rei wi lau wi phoi wi shao wi` (242). Each scale appears at most once in descending order with `ta` or `wi`; zero places are omitted, and scale units are not recursively counted. A bare scale marks contextual approximation without a fixed rounding interval or a claim of literal uncountability. Larger exact values, negative numbers, fractions, units, formulas, and exact technical notation remain source material outside the Phi passage. Arithmetic, pure equality, and two-explicit-quantity magnitude comparison require `nela` between operands; pauses and context do not replace it. Addition and subtraction require commensurable quantities, multiplication takes a counted quantity plus a factor, and division takes a total plus recipients or groups while its quotient inherits the total's kind.
- **Retired external boundaries** (settled 2026-07-10; clarified 2026-07-12): the former guest and exact boundary forms are not Phi words and cannot be reassigned as lexical forms. They have no special status in the productive-name system: because they are absent from the current lexicon, a bearer may choose one as an onym without restoring its former grammar. Historical releases preserve their earlier design status; current grammar, tooling, and teaching do not parse or recommend them as boundaries. `shola ... sholo` remains distinct because it quotes grammatical Phi as Phi.
- **Optional lexical modules** (settled 2026-07-10 / Phi 2026.2): Phi has one canonical lexicon and one grammar. A content entry may carry validated `modules` metadata so learners can choose specialized vocabulary without treating it as required general study. Module words obey ordinary Phi phonology, syntax, event and quality noun rules, and the complete vocabulary schema; a module adds no particle, inflection, parser mode, or incompatible construction. Speakers unfamiliar with a module term may ask for a core paraphrase. Every active module has a Part VII speaker guide, and the current inventories live in `documents/modules/README.md`. A profile pass places a word in base vocabulary when ordinary use or a core need makes optional study the wrong home. The absence of a `modules` field marks that placement without changing the word's grammar or authority.
- **Lexicon prose contract** (settled 2026-07-14): every new lexicon entry and every entry given a complete prose revision defines its range in `description`, describes the physical spoken form in `articulatory_notes`, and stores at least one validated Phi and English pair in `examples`. `search_terms` and `usage_notes` are optional aids. `sound_symbolism` is optional Phi-specific phonesthetic interpretation, not universal phoneme meaning or hidden morphology. `pillars` appears only for direct, specific connections and may be absent. Content entries retain required `semantic_domains`. The schema temporarily accepts legacy `concept`, `sound_symbolism`, and `grammatical_notes` shapes while the inherited vocabulary is migrated, and the committed coverage report records that work.
- **Careful and conversational pronunciation** (settled 2026-07-10): lexicon IPA records the careful reference pronunciation, with full hiatus, penultimate stress, dental `t`/`n`, `/ɸ θ ʃ ʍ/`, and trilled or tapped `r`. Conversational and accented Phi may use [f] for `/ɸ/`, [w̥] or [hw] for `/ʍ/`, [r], [ɾ], or [ɹ] for `r`, alveolar [t n] for the dental stops, light stop aspiration, and [t̪θ] for `/θ/`. These variants are accepted when the phonemic contrasts and syllable count remain recoverable; `/θ/` must remain distinct from `t`, `s`, and `ph`, and `wh` from `w`. Vowels may shorten or shift within the five-vowel system but may not merge, and adjacent vowels remain separate syllables. Tempo and accent are not moral or grammatical registers.
- **Main-clause tense** (settled 2026-07-05): tense particles are
  not optional — a clause whose translation is past carries `to` on
  its own verb (`sholo to haolu`, they said), as ch14 requires and
  the texts practice. An unmarked verb is present. Embedded clauses
  keep their own marking, relative to the matrix event (see the
  embedded-clauses ruling below).
- **Covered by design — do not coin** (settled 2026-07): anger is
  `korua thero` and contempt `thiku nila` (compound registry);
  east/west are `sileta thorui`/`sileta lumae`; dream is `whemura`;
  stop/cease is the particle `te`; wife/husband is `tewema`; thought
  is `remo` and every other event noun comes by the event-noun
  rule; statement is `phelui`/`haolu` with the complementizers;
  timbre is `haoni welisha`; loneliness composes as `sonu` + `nuhe`;
  greeting is `kia`/`whelani`. The full gap-campaign record, with
  all fourteen rulings, is preserved in `archive/GAP_INVENTORY.md`.
- **Refused in the core lexicon** (extended 2026-07-10): universal gendered person classes such as *woman/man* are not currently admitted; `miona` (person), `tewema` (partner), and `phao` (parent) remain the unmarked terms, while a person's exact self-description may remain in source material outside Phi and any future core proposal receives case-by-case review. Also currently refused: *hunt*; generic *bad* (things are harmful, broken, or unwell); *blade* as weapon-part (knife exists only as a kitchen or craft tool); *marriage* as institution; and the vocabulary of domination, including *to rule*, *lord/master*, *throne*, and *bind-as-captivity*. The Ring Verse refusal (`texts/ring_verse_refusal.md`) uses `kulo` (guide), `theluo` (steward), and `nolami` (mutual bond) instead. These decisions govern unmarked core vocabulary; faithful source material remains outside Phi and the case-by-case review standard remains controlling.
- **Classifiers** (settled 2026-07; clarified 2026-07-11): four only (`himo`, `lipha`, `themo`, `nophe`), always optional after a numeral or `wia`; ordinary quantifiers modify the noun directly and do not take a classifier. Nature-now rule: living parts of living beings take `lipha`; time units and events take `nophe`; `themo` is for detached and crafted objects. Classifier use foregrounds a category but does not encode respect or mindfulness. The superlative is `mo ko`; the particle `mi` is retired. Subordinating conjunctions: `pheo`, `phoe`, `lao`, `shai`, `lila`.
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
  taught in manual ch14.
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
  a noun standing before a noun already modifies it, as ch11 has
  always taught for possession — `nitho ruela` (the north path),
  `wheo kowela` (the elder council) — and meaning chooses the
  reading. The 24 adjective+noun dual listings were pruned to a
  single class (14 nouns, 10 adjectives, adjudicated by primary
  sense in `archive/quality_noun_adjudication.md`); the validator
  refuses the combination. One word, one class; position and the
  two one-way rules do all the bridging.
- **Qualities do not name their acts** (settled 2026-07-06): the
  adjective→verb direction is refused, completing one-word-one-class
  — no content entry lists two parts of speech, and the validator
  enforces it. Entering a state is `kelu` (become) with the quality
  before it (`lureko seroli kelu`, the fruit ripens — the Velveteen
  text's own `thia shewo kelu`); causing one is ordinary Slot 1
  voice on the verbs of being and becoming (`mia noru hiso ka
  kelu`, I clean the bowl; `mia lopia shena ka nai`, I keep the
  child calm). The 12 dual listings were pruned to adjective-only —
  except `phae` (open), which like `kulo` was verb-primary all
  along: the primer teaches it beside verb-only `tapu` (close), so
  it keeps the verb and sheds the adjective. Word-by-word audit in
  `archive/adjective_verb_adjudication.md`.
- **Manner is a descriptor before the verb** (settled 2026-07-06):
  Phi has no adverb class and needs none — the same descriptors
  that modify nouns modify verbs, standing immediately before the
  verb, inside the Slot 1 block: `to shena haolu` (said calmly),
  `to reshi wepu` (moved fast), both from the complementizers
  pamphlet. The verb phrase thus mirrors the noun phrase — function
  words, then descriptors, then the head: `ha mioru thepalu` /
  `to reshi kolua`. Depictives share the position (`thia ma
  mioru nila`, see you as unbeautiful — Velveteen). Two early
  texts had the descriptor outside the Slot 1 block; both were
  realigned (Schleicher fable, Velveteen). Evidence in
  `archive/manner_placement_study.md`; taught in ch10 §4.
- **The function-word shape charter** (extended 2026-07-10): every
  function class has a chartered shape with
  conformance validator-enforced. CV
  monosyllables are the grammar's atoms — the 35 particles (plain
  CV, never a digraph onset, for instant recognition) and the base
  numerals `mu ta wi` — and nothing else may take that shape.
  Hiatus disyllables ((C)V.V) are relators: all 27 prepositions and
  the core pronouns `mia thia shia`; the reflexive/reciprocal pair
  `miso wiso` is the designed -so extension of the pronoun set.
  Plain disyllables are frames: the eleven complementizers (openers
  in -a, closers in -o), the vocative `kona`, the four classifiers,
  and the frame conjunctions — while the clause-relators `lao pheo
  phoe shai` carry the relator shape instead, prepositions over
  clauses (frame words stay two-syllable, settled, PR #78).
  Quantifiers, discourse markers, and interrogatives are
  content-shaped (two or three syllables, patterns free): they ride
  in descriptor and adverbial positions where content words live.
  Audit and two unruled observations in
  `archive/function_word_shape_audit.md`.
- **The breath before reframing** (settled 2026-07-06): discourse
  markers begin with a fricative digraph — the breath a speaker
  takes before redirecting the conversation (`phisu, sheno, shorela,
  shekoi, shelao, thelao`). The one exception, `kewai` (CONTR), was
  recoined to `whekai`, keeping its pivot `ka` and bright final `i`
  behind the new opening breath; the validator enforces the onset
  for the class.
- **The natural clock** (settled 2026-07-06): Phi tells time by the
  sun's eight stations — `horathe` (dawn), `kelua` (morning),
  `thaeso` (midday), `lorui` (afternoon), `howai` (evening),
  `norawhi` (dusk), `shero` (night), `phoemu` (midnight) — located
  with the ordinary prepositions: `sui kelua` (during the morning),
  `tei howai` (until evening), `mua shero` (in the night). Hour,
  minute, second, and clock-time are refused as unmarked core vocabulary — the
  counted minute is exactly the precise measurement the language
  declines (`documents/design/psychological_violence_of_measurement.md`);
  the day is read from the sky, not sliced into units. A required clock time remains in an exact source record outside the Phi passage when coordination, testimony, or safety depends on it.
- **Age is held, not been** (settled 2026-07-06): age is said with
  predicative possession — `mia [numeral] torua phelu.` (I hold N
  years): `mia wi phoi ta shao torua phelu.` (I am twenty-one —
  literally, I hold two nine-groups and a three-group of years).
  The clause-initial-pronouns ruling supplies the pattern; the
  classifier, optional as always, is `nophe`, the class of time
  units. Years are something a person carries, not something a
  person is.
- **Temporal distance** (settled 2026-07-06): `pheo` (POST) and
  `phoe` (ANT) stand over counted time noun phrases as well as
  clauses — `pheo wi philo` (after two days: in two days, with `so`
  on the verb), `phoe wi philo` (before two days: two days ago,
  with `to`). The shape charter already classes them as relators,
  prepositions over clauses; this extends their reach, not their
  class. The phrase stands where adjuncts stand — before the
  object, circumstances announced first.
- **Frequency composes** (settled 2026-07-06): how often is a
  quantifier over moments — `sheloi shemu` (often), `phina shemu`
  (rarely), `soli shemu` (sometimes), `theula thimu` (always),
  `mawha thimu` (never). The pattern is productive and preferred
  to coining: any quantifier may count `shemu` (moments) or claim
  `thimu` (time entire); a coined "seldom" would only relabel
  `phina shemu`. The registry carries the five.
- **Color composes** (settled 2026-07-06): the seven color
  adjectives are the whole coined palette: `nuko` (black), `whilo`
  (white), `rulo` (red), `liro` (green), `soriu` (yellow), `shilu`
  (blue), `mureli` (brown), each anchored to a natural referent.
  These are the perceptual universals (Berlin and Kay stages I
  through VI); hue adjectives beyond them are refused by design,
  because the further hues are culturally negotiated and Phi lets
  them keep the thing they came from visible. Further hues take
  `welisha` after the referent that carries them, the
  nouns-describe rule doing its ordinary work: `kerou welisha`
  (stone color, gray), `thero welisha` (fire color, orange),
  `horathe welisha` (dawn color, pink), `norawhi welisha` (dusk
  color, violet); the registry carries the four. Brightness and
  paleness stack as descriptors do: `nuelo shilu` (dark blue),
  `keru rulo` (bright red), `whilo shilu` (pale blue). `nuko`
  names the hue and `nuelo` the illumination; the entries carve
  the pair.
- **The natural ruler** (extended 2026-07-15): core Phi has no unit words: no meter, no mile, no kilogram, no liter, and none will be coined. This extends the clock refusal to the ruler and the scale, on the same grounds (`documents/design/psychological_violence_of_measurement.md`). `masue` (measure) means gauging against a shared standard, not counting units (`shia sheo pelio wetha masue.`, they measure the cloth against an arm, the entry's own example); ranking, where ranking is the honest point, is `sheo` with `mo` (`tomora sheo shiro mo raelu nai.`, the mountain is taller than the tree); and journey scale may be stated through travel time (`ruela wi philo thalo nai.`, the path is a two-day walk, the nouns-describe rule at ordinary work). The neutral nouns `ponalu` (size), `waleru` (length), `hirawo` (distance), `raeli` (height), `lonai` (width), and `nusho` (depth) identify what is gauged without supplying a unit. When an exact unit or quantity is required for repair, health, science, testimony, or interoperability, the source record remains outside the Phi passage while the Phi sentence identifies and discusses that record.
- **Sides come from a body** (settled 2026-07-06): `lawe` (left)
  and `kuri` (right) name sides a body lends to the scene. Bare,
  they are the speaker's: `womu mua lawe nai.` (the house is on
  my left). A possessor re-anchors them: `thia lawe` (your left),
  `keruko kuri` (keruko's right). No absolute left exists, so
  none can be imposed; the hearer always knows whose body
  orients the scene.
- **States are worn, sensations are felt** (settled 2026-07-06):
  inner and bodily states that are adjectives predicate with
  `nai`: `mia kumoli nai.` (I am hungry), `thia mokela nai.`
  (you are sick), `mia towe nai.` (I am well). Sensations and
  feelings that are nouns are objects of `phaelo` (feel): `mia
  kipona phaelo.` (I feel pain), `mia shea phaelo.` (I feel
  peace), the pattern the journal practice has always used. A
  body part locates the feeling with `mua` in the ordinary
  adjunct slot: `mia mua rokai kipona phaelo.` (I feel pain in
  my back); the healer's question is `thia kua kipona phaelo.`
  (where do you feel pain). The identity shortcut is refused:
  never `mia kipona nai`; a person has never been their pain.
- **Death is named plainly** (settled 2026-07-06): `lumeo` is the
  word, and no softened synonym will ever be coined; a language
  built for honesty does not grow a fog bank around the one
  certainty. `shia to lumeo.` (she died); the dead one is `rena
  to lumeo`; death the noun comes by the event-noun rule and may
  stand as subject (`lumeo wei theula lioru shua.`, death comes
  to all life, the entry's own sentence). Gentleness lives in the
  grammar, not in avoidance: grief takes the feeling pattern
  (`mia nuhe phaelo.`, `mia holume phaelo.`), mourning marks the
  mourned with `wei` (`mia wei ni melu nuhemi.`), and the
  optative holds what cannot be fixed.
- **Rites are described, never prescribed** (settled 2026-07-06):
  `thorea` (ceremony) is the only rite word Phi will ever have.
  Specific rites (funeral, wedding, baptism, and their kin) are
  refused by design: naming a rite standardizes it, and Phi's
  speakers come from every tradition. A ceremony is described
  (`lumeo thorea`, a death ceremony; `sila wei shia thorea
  kealo.`, the community makes a ceremony for them) and the
  content belongs to whoever holds it. The stance the Prophet
  transmutation stated in passing is hereby canon.
- **The heart composes** (settled 2026-07-06): the felt basics
  are the whole coined emotion lexicon: the noun feelings taken
  by `phaelo` (`shea`, `nuhe`, `sukima`, `nupira`, `thomari`)
  and the adjective states worn with `nai` (`siora`, `loshi`,
  `shena`, `phaelu`, `noalu`, `thiro`, `nuloe`, `nemo`, `kuelo`,
  `phaeli`, `hurao`, `shaelo`, `phena`, `thoru`). Complex and
  social emotions are not coined; they compose from their
  mechanisms, as the registry teaches: `korua thero` (anger, and
  hatred with it), `thiku nila` (contempt), `phelu pula` (envy),
  `sonu` + `nuhe` (loneliness), and wonder as a question held
  inside feeling (`wela … welo` under `phaelo`, ch19's own
  rendering). A root for a complex feeling would hide the
  mechanism its compound lays open; the envy row's aside is
  hereby the rule for the class.
- **A work is its making** (settled 2026-07-06): art-form and
  genre roots (poem, painting, sculpture, novel, and their kin)
  are refused by design; each would name a container where Phi
  names an act. A work is the event noun of the verb that made
  it: a weaving (`selomi`), a shaping (`kire`, which covers
  drawing), a singing (`meliho`); the coined artifacts of the
  voice are `melira` (song), `meliphe` (music), and `nophi`
  (story), and a poem is `melira`, because Phi's page is a score
  for the voice. `shela` (art) is the whole category; `mioru`
  (beautiful) supplies its quality noun, beauty, for what art expresses. The two coined instruments are
  named for their own voices, `kuma` carrying rhythm and `phui`
  carrying melody; further instruments may be coined by the full
  protocol when the household genuinely meets one, in the same
  voice-named pattern, and playing any of them is `wile` (`sulai
  kuma wile.`, the musician plays the drum).
- **The gap-word stands where the answer will** (settled
  2026-07-06): a content question places its interrogative
  exactly where the answer's phrase will stand, in the unmarked
  sentence shape: `thia hina nila.` (you see what?), `lohau kua
  nai.` (the dog is where?), `thia kua kipona phaelo.` (where do
  you feel pain?). The gap-word alone marks the question; `wa`
  asks yes/no about the whole and never co-occurs with a
  gap-word. The askers are seven: `sua` (who), `hina` (what),
  `weno` (when), `kua` (where), `misa` (why), `thela` (how), and
  `wia` (how many), which stands before a classifier or noun as
  a quantifier does (`thia wia torua phelu.`, how old are you).
  Selection ("which cup") is `hina` before the noun, what-kind
  being Phi's honest which. `wia`'s gloss is corrected from
  "which" to "how many" to match its designed and attested use.
- **The economy is a gift** (settled 2026-07-06): money, coin, price, pay, buy, sell, debt, wage, wealth, and poor are refused by design, completing the measurement family: the clock, ruler, and price tag fall on the same grounds (`documents/design/psychological_violence_of_measurement.md`). What changes hands is said with the hands' verbs: `loa` (give), `howela` (receive), `phowe` (share), and `wisola` (exchange), whose grammar leans mutual (`lo mia wiso wisola.`, we exchange with each other), with `loami` (gift) and `piru` (trader) beside them. An exchange uses exact counts when the difference affects what participants give or receive, while agreed estimates remain possible and exact economic source records stay outside the Phi passage. Worth stays carved: `rolia` is inherent, `sone` is a verb because valuing is something someone does, `simoe` (rich) enriches soil and colors but ranks no one, and scarcity is described with `phina`, `whemoa`, or `henoi` rather than named as a class of person. A market place, if one ever needs naming, composes by the nouns-describe rule.

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
  done, `so ki` = will have done — as the lexicon entry and ch14 have
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
- **Aspect under `ka` describes the causing** (settled 2026-07-09):
  Slot 1 particles describe their own clause's event, and in a
  causative clause that event is the act of causing — `to ro ka wepu`
  can only mean that the making-go recurs. An aspect that belongs to
  what the caused ones themselves do moves out of the cluster, into
  its own clause (`punoa roe nurako lo miona to ka wepu. ha wepu keno
  to kelu.` — society made people go by railway; this going became a
  custom) or into a word that carries the repetition. Ruled from the
  News from Nowhere railway line: civilization does nothing
  habitually.
- **`li` is a fence, not a sigh** (settled 2026-07-05): `li` restricts
  identity — `li shia sano` (only they know), `li nosa` (only now) —
  and is refused on quantities: exact counts and `henoi` carry
  quantity-honesty. "Only three eggs" is a count plus a feeling, and
  Phi states the count.
- **Slot 2 nests** (settled 2026-07-05): within a phrase, wider
  relations stand earlier — `we`/`li` > `ha`/`ra` > `lo`/numerals >
  `ko` > `ru`/`mo` > the word — modifier-first applied inside the
  phrase (attested: `ha lo ru mioru peloru`). `we` and `li` do not
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
