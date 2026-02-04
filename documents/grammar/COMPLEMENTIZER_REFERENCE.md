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

[rena shiro mue nai] thimu
[REL forest in be] path
(the path that is in the forest)
```

**Headless relative clauses** (when the noun is implicit):
```
[rena lothea kela] shia
[REL love understand] 3SG
(The one who understands love.)
```

---

### `shola` / `sholo` - Quotative (QUOT / QUOT.CLOSE)

**Function**: Introduces and closes direct speech, preserving the exact words spoken
**IPA**: /ʃo.la/ and /ʃo.lo/
**Position**: `shola` opens the quoted material; `sholo` closes it. The main verb follows `sholo`.
**Structure**: `[Subject] shola [Quote] sholo [Verb of speaking]`

**`sholo` is required.** It marks where the quotation ends so the main verb can follow unambiguously.

**Examples**:
```
shia shola suno phelora nai sholo haolu
3SG QUOT sun beautiful be QUOT.CLOSE say
(She says, "The sun is beautiful.")

mia shola mia so wepu sholo haolu
1SG QUOT 1SG FUT leave QUOT.CLOSE say
(I said: "I will leave.")
```

**Note**: Distinct from `mena`/`meno` (declarative); `shola`/`sholo` preserves exact words, `mena`/`meno` reports content/meaning.

---

### `mena` / `meno` - Declarative Complementizer (DECL / DECL.CLOSE)

**Function**: Introduces and closes embedded declarative clauses (reports content, not exact words)
**IPA**: /me.na/ and /me.no/
**Position**: `mena` opens the embedded statement; `meno` closes it. The main verb follows `meno`.
**Structure**: `[Subject] mena [Embedded statement] meno [Main verb]`

**`meno` is required.** Because Phi's SOV word order places the main verb after the complement clause, `meno` is needed to mark where the embedded clause ends and the main verb begins. Without it, two adjacent verbs would be ambiguous.

**Examples**:
```
mia mena shia wepu meno shelomui
1SG DECL 3SG leave DECL.CLOSE understand
(I understand that ko left.)

shia mena thia wepu meno haolu
3SG DECL 2SG leave DECL.CLOSE say
(She said that you left.)

mia mena suno theru nai meno phaelo
1SG DECL sun warm be DECL.CLOSE feel
(I feel that the sun is warm.)
```

**Nesting**: `mena`/`meno` clauses can nest. Each `mena` must have its own `meno`:
```
mia mena thia mena shia wepu meno phaelo meno shelomui
1SG DECL 2SG DECL 3SG leave DECL.CLOSE feel DECL.CLOSE understand
(I understand that you feel that ko left.)
```

**Comparison with `shola`/`sholo`**:
- `shia shola "mia wepu" sholo haolu` = She said: "I'm leaving." (exact words)
- `shia mena thia wepu meno haolu` = She said that you left. (reported content)

---

### `wena` - Interrogative Complementizer (INT.COMP)

**Function**: Introduces embedded yes/no questions
**IPA**: /we.na/
**Position**: After the subject, before the embedded question. The main verb follows the embedded clause.
**Structure**: `[Subject] wena [Embedded yes/no question] [Main verb]`

**No closer needed.** Unlike `mena`/`meno` and `shola`/`sholo`, embedded questions are structurally bounded: the embedded clause's own verb marks its end, and the main verb's semantic role (wondering, asking, knowing) is distinct enough to resolve the boundary. All `we_V` syllable combinations are taken in the vocabulary, so no closer was available.

**Examples**:
```
mia wena shia wepu phaelo
1SG INT.COMP 3SG leave wonder
(I wonder whether ko left.)

shia wena mia to nila nomei
3SG INT.COMP 1SG PST see ask
(She asked whether I had seen.)

lo mia wena suno phelora nai ma shelomui
1PL INT.COMP sun beautiful be NEG understand
(We don't know whether the sun is beautiful.)
```

**Distinction from related words**:
- `wa` (question particle): Marks direct questions expecting response
- `thoe` (conditional conjunction): Marks hypothetical conditions with consequences
- `wena` (interrogative complementizer): Embeds questions as content

**Comparison**:
- `wa thia wepu` = Are you leaving? (direct question)
- `thoe thia wepu. mia sola nai` = If you leave, I'll be alone. (conditional)
- `mia wena thia wepu phaelo` = I wonder whether you're leaving. (embedded question)

---

## Vocative

The vocative is a separate part of speech for direct address, existing outside the clause structure.

### `kona` - Vocative Marker (VOC)

**Function**: Announces that someone is being directly addressed
**IPA**: /ko.na/
**Position**: Before the name/title of the addressee, outside the main clause
**Structure**: `kona [ne] [Name/Title], [Sentence]`

**Examples**:
```
kona melu, mia ha nai
VOC friend, 1SG here be
(Friend, I am here.)

kona ne sa thala, wa thia wela nai
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
| `shola` | QUOT | Opens direct quotation (exact words) | `sholo` (required) |
| `sholo` | QUOT.CLOSE | Closes direct quotation | — |
| `mena` | DECL | Opens embedded statements (reported content) | `meno` (required) |
| `meno` | DECL.CLOSE | Closes embedded statements | — |
| `wena` | INT.COMP | Introduces embedded yes/no questions | — (structurally bounded) |
| `kona` | VOC | Marks direct address | — (extra-clausal) |

---

**Related Documentation:**
- Particles: `documents/grammar/PARTICLE_REFERENCE.md`
- Complex constructions: `documents/grammar/05-complex-constructions.md`
- Main instructions: `CLAUDE.md`
