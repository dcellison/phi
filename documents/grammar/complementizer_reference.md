# Phi Complementizer and Vocative Reference

This document covers complementizers and the vocative marker—function words that introduce subordinate clauses or mark direct address. These are distinct from particles (which are single-syllable and fit the three-slot system).

---

## Complementizers

Complementizers are multi-syllable function words that introduce subordinate clauses. They announce the relationship between the main clause and the embedded clause that follows.

### `rena` - Relativizer (REL)

**Function**: Introduces relative clauses that describe a noun
**IPA**: /re.na/
**Position**: Before the relative clause and the noun it modifies
**Structure**: `[rena CLAUSE] NOUN`

**Examples**:
```
[rena nophi kealo] miona
[REL story create] person
(the person who creates stories)

[rena mia to nila] shelu
[REL 1SG PST see] book
(the book that I saw)

[rena mua shelira nai] ruela
[REL LOC forest be] path
(the path that is in the forest)
```

**Headless relative clauses** (when the noun is implicit):
```
[rena lothea shelomui] shia
[REL love understand] 3SG
(The one who understands love.)
```

---

### `shola` / `sholo` - Quotative (QUOT.COMP / QUOT.COMP.CLOSE)

**Function**: Introduces and closes direct speech, preserving the exact words spoken
**IPA**: /ʃo.la/ and /ʃo.lo/
**Position**: `shola` opens the quoted material; `sholo` closes it. The main verb follows `sholo`.
**Structure**: `[Subject] shola [Quote] sholo [Verb of speaking or receiving speech]`

The frame verb may be a verb of speaking (`haolu`, `shemui`, `thilou`) or of receiving speech (`hea`): the quote is bounded by `sholo` either way, and hearing exact words is as sayable as speaking them.

**`sholo` is required.** It marks where the quotation ends so the main verb can follow unambiguously.

**Examples**:
```
shia shola sorae phelora nai sholo haolu
3SG QUOT.COMP sun beautiful be QUOT.COMP.CLOSE speak
(They say, "The sun is beautiful.")

mia shola mia so wepu sholo to haolu
1SG QUOT.COMP 1SG FUT go QUOT.COMP.CLOSE PST speak
(I said: "I will leave.")
```

**Note**: Distinct from `mena`/`meno` (declarative); `shola`/`sholo` preserves exact words, `mena`/`meno` reports content/meaning.

---

### `mena` / `meno` - Declarative Complementizer (DECL.COMP / DECL.COMP.CLOSE)

**Function**: Introduces and closes embedded declarative clauses (reports content, not exact words)
**IPA**: /me.na/ and /me.no/
**Position**: `mena` opens the embedded statement; `meno` closes it. The main verb follows `meno`.
**Structure**: `[Subject] mena [Embedded statement] meno [Main verb]`

**`meno` is required.** Because Phi's SOV word order places the main verb after the complement clause, `meno` is needed to mark where the embedded clause ends and the main verb begins. Without it, two adjacent verbs would be ambiguous.

**Examples**:
```
mia mena shia to wepu meno shelomui
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE understand
(I understand that they left.)

shia mena thia to wepu meno to haolu
3SG DECL.COMP 2SG PST go DECL.COMP.CLOSE PST speak
(They said that you left.)

mia mena sorae sulae nai meno phaelo
1SG DECL.COMP sun warm be DECL.COMP.CLOSE feel
(I feel that the sun is warm.)
```

**Nesting**: `mena`/`meno` clauses can nest. Each `mena` must have its own `meno`:
```
mia mena thia mena shia to wepu meno phaelo meno shelomui
1SG DECL.COMP 2SG DECL.COMP 3SG PST go DECL.COMP.CLOSE feel DECL.COMP.CLOSE understand
(I understand that you feel that they left.)
```

**Comparison with `shola`/`sholo`**:
- `shia shola mia wepu sholo to haolu` = They said: "I'm leaving." (exact words)
- `shia mena thia to wepu meno to haolu` = They said that you left. (reported content)

---

### `wela` / `welo` - Interrogative Complementizer (INT.COMP / INT.COMP.CLOSE)

**Function**: Introduces and closes embedded yes/no questions
**IPA**: /we.la/ and /we.lo/
**Position**: `wela` opens the embedded question; `welo` closes it. The main verb follows `welo`.
**Structure**: `[Subject] wela [Embedded yes/no question] welo [Main verb]`

**`welo` is required.** Like `mena`/`meno` and `shola`/`sholo`, the closer marks where the embedded clause ends so the main verb can follow without ambiguity.

**Examples**:
```
mia wela shia to wepu welo phaelo
1SG INT.COMP 3SG PST go INT.COMP.CLOSE feel
(I wonder whether they left.)

shia wela mia to nila welo to thilou
3SG INT.COMP 1SG PST see INT.COMP.CLOSE PST inquire
(They asked whether I had seen.)

lo mia wela sorae phelora nai welo ma shelomui
PL 1SG INT.COMP sun beautiful be INT.COMP.CLOSE NEG understand
(We don't know whether the sun is beautiful.)
```

**Distinction from related words**:
- `wa` (question particle): Marks direct questions expecting response
- `lu` (Slot 0 conditional particle): Marks hypothetical conditions with consequences
- `wela`/`welo` (interrogative complementizer pair): Embeds questions as content

**Comparison**:
- `wa thia wepu` = Are you going? (direct question)
- `lu thia wepu. mia ma towe phaelo` = If you go, I won't feel well. (conditional)
- `mia wela thia wepu welo phaelo` = I wonder whether you're going. (embedded question)

---

## External register

A proper name does not require an external frame merely because it is absent from the lexicon. `ne` directly licenses one productive lowercase name-form of two or three legal Phi syllables (`ne samira`). The guest frame remains useful for longer, multi-token, or explicitly external adaptations; the exact frame preserves source form.

### `hasha` / `hasho` - Adapted Guest Frame (EXT.GUEST / EXT.GUEST.CLOSE)

**Function**: Carries a longer, multi-token, or explicitly external name or term adapted to Phi pronunciation and romanization without making it a lexicon word
**IPA**: /ˈhä.ʃä/ and /ˈhä.ʃo̞/
**Position**: The complete frame occupies one nominal position; `ne`, prepositions, and other Phi particles remain outside it
**Structure**: `[Phi function words] hasha [adapted payload] hasho`

Guest payload uses Phi's permitted sounds and open syllables, begins with an onset, remains lowercase, and takes penultimate stress. Unlike a core lexicon word, it may repeat syllables and may extend across several adapted tokens. It is not looked up in the lexicon, and every occurrence remains framed.

```
mia ne hasha toronoto hasho nila
1SG NAME EXT.GUEST [toronoto] EXT.GUEST.CLOSE see
(I see Toronto.)
```

`hasho` cannot appear as a standalone guest token because it closes the frame. Choose a different adaptation if one would produce it. Guest frames cannot nest.

### `patha` / `patho` - Exact Opaque Frame (EXT.EXACT / EXT.EXACT.CLOSE)

**Function**: Preserves external material exactly without subjecting it to Phi spelling, punctuation, phonology, or vocabulary rules
**IPA**: /ˈpä.θä/ and /ˈpä.θo̞/
**Position**: The complete frame occupies one nominal position; all Phi grammar remains outside it
**Structure**: `[Phi function words] patha [opaque payload] patho`

Exact payload may contain any script, case, punctuation, numeral, unit, formula, URL, identifier, quotation, or external term. The Phi boundary words remain present in every writing mode; the payload remains in its source form.

```
mia ne patha Toronto patho nila
1SG NAME EXT.EXACT [Toronto] EXT.EXACT.CLOSE see
(I see Toronto.)

mia patha E = mc² patho theo
1SG EXT.EXACT [E = mc²] EXT.EXACT.CLOSE read
(I read "E = mc².")

shia patha lord patho to haolu
3SG EXT.EXACT [lord] EXT.EXACT.CLOSE PST speak
(They said the word "lord.")
```

A single standalone `patho` closes the frame. To preserve a literal standalone occurrence inside payload, double it as `patho patho`; the next single `patho` closes. Exact payload is opaque, so apparent frame words inside it have no Phi syntax. Written exact payload is authoritative. A speaker may reproduce, spell, or describe it through a shared external convention, but Phi makes no letter-perfect oral-recovery claim for that payload.

### External frames as atoms

Both external frames are nominal atoms. They may be a subject, object, preposition object, possessive or noun modifier, or predicate before `nai`. They do not import source-language verbs, adjectives, agreement, or word order. `ne` precedes the whole atom for a proper name, and any Phi particle scopes over the whole frame.

The frame marks provenance, not judgment. Exact material may faithfully report a concept that core Phi declines to lexicalize when testimony, history, critique, identity, consent, safety, quotation, or precision requires it. Repeated guest use never grants core status; core admission follows the ordinary word-creation protocol.

---

## Vocative

The vocative is a separate part of speech for direct address, existing outside the clause structure.

### `kona` - Vocative Marker (VOC)

**Function**: Announces that someone is being directly addressed
**IPA**: /ko.na/
**Position**: Before the name/title of the addressee, outside the main clause
**Structure**: `kona [ne] [Name/Title]. [Sentence]`

**Examples**:
```
kona melu. mia ha nai
VOC friend. 1SG PROX be
(Friend, I am here.)

kona ne sa sulae. wa thia towe nai
VOC NAME HON.RESPECT sulae. Q 2SG well be
(Honored sulae, are you well?)

kona ne ni moli. mia thia lothea
VOC NAME HON.INTIM moli. 1SG 2SG love
(Dear moli, I love you.)
```

**Note**: The vocative phrase is extra-clausal—it frames who is being addressed but does not participate in the main clause's subject-object-verb structure. When addressing someone by name, the proper name particle `ne` precedes the name (and any honorific). When addressing by role or common noun (e.g., `melu`, "friend"), `ne` is not used.

---

## Summary

| Word | Gloss | Function | Closer |
|------|-------|----------|--------|
| `rena` | REL | Introduces relative clauses | — (pre-nominal position bounds it) |
| `shola` | QUOT.COMP | Opens direct quotation (exact words) | `sholo` (required) |
| `sholo` | QUOT.COMP.CLOSE | Closes direct quotation | — |
| `mena` | DECL.COMP | Opens embedded statements (reported content) | `meno` (required) |
| `meno` | DECL.COMP.CLOSE | Closes embedded statements | — |
| `wela` | INT.COMP | Opens embedded yes/no questions | `welo` (required) |
| `welo` | INT.COMP.CLOSE | Closes embedded yes/no questions | — |
| `hasha` | EXT.GUEST | Opens adapted external material | `hasho` (required) |
| `hasho` | EXT.GUEST.CLOSE | Closes adapted external material | none |
| `patha` | EXT.EXACT | Opens exact opaque material | `patho` (required) |
| `patho` | EXT.EXACT.CLOSE | Closes exact opaque material | none |
| `kona` | VOC | Marks direct address | none (extra-clausal) |

---

**Related Documentation:**
- Particles: `documents/grammar/particle_reference.md`
- Complex constructions: the manual, Part V (`manual/part5_complex/`)
- Main instructions: `documents/development_protocol.md`
