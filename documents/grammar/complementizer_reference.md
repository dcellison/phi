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
[REL in forest be] path
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
**Structure**: `[Subject] shola [Quote] sholo [Verb of speaking]`

**`sholo` is required.** It marks where the quotation ends so the main verb can follow unambiguously.

**Examples**:
```
shia shola sorae phelora nai sholo haolu
3SG QUOT.COMP sun beautiful be QUOT.COMP.CLOSE say
(She says, "The sun is beautiful.")

mia shola mia so wepu sholo haolu
1SG QUOT.COMP 1SG FUT leave QUOT.COMP.CLOSE say
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
1SG DECL.COMP 3SG PST leave DECL.COMP.CLOSE understand
(I understand that ko left.)

shia mena thia to wepu meno to haolu
3SG DECL.COMP 2SG PST leave DECL.COMP.CLOSE PST say
(She said that you left.)

mia mena sorae sulae nai meno phaelo
1SG DECL.COMP sun warm be DECL.COMP.CLOSE feel
(I feel that the sun is warm.)
```

**Nesting**: `mena`/`meno` clauses can nest. Each `mena` must have its own `meno`:
```
mia mena thia mena shia to wepu meno phaelo meno shelomui
1SG DECL.COMP 2SG DECL.COMP 3SG PST leave DECL.COMP.CLOSE feel DECL.COMP.CLOSE understand
(I understand that you feel that ko left.)
```

**Comparison with `shola`/`sholo`**:
- `shia shola "mia wepu" sholo haolu` = She said: "I'm leaving." (exact words)
- `shia mena thia to wepu meno to haolu` = She said that you left. (reported content)

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
1SG INT.COMP 3SG PST leave INT.COMP.CLOSE wonder
(I wonder whether ko left.)

shia wela mia to nila welo to thilou
3SG INT.COMP 1SG PST see INT.COMP.CLOSE PST ask
(She asked whether I had seen.)

lo mia wela sorae phelora nai welo ma shelomui
1PL INT.COMP sun beautiful be INT.COMP.CLOSE NEG understand
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
VOC friend. 1SG here be
(Friend, I am here.)

kona ne sa thala. wa thia towe nai
VOC NAME HON.RESPECT Thala, Q 2SG well be
(Honored Thala, are you well?)

kona ne ni hino, mia thia lothea
VOC NAME HON.INTIM Hino, 1SG 2SG love
(Dear Hino, I love you.)
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
| `kona` | VOC | Marks direct address | — (extra-clausal) |

---

**Related Documentation:**
- Particles: `documents/grammar/particle_reference.md`
- Complex constructions: `documents/grammar/05-complex-constructions.md`
- Main instructions: `CLAUDE.md`
