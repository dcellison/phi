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

### `shola` - Quotative (QUOT)

**Function**: Introduces direct speech, preserving the exact words spoken
**IPA**: /ʃo.la/
**Position**: Before the quoted material
**Structure**: `[Subject] shola "[Quote]" [Verb of speaking]`

**Examples**:
```
shia shola "remo wela" shemui
3SG QUOT "sun beautiful" say
(She says, "The sun is beautiful.")

mia shola "mia so wepu" nophi
1SG QUOT "1SG FUT leave" tell
(I said: "I will leave.")
```

**Note**: Distinct from `mena` (declarative)—`shola` preserves exact words, `mena` reports content/meaning.

---

### `mena` - Declarative Complementizer (DECL)

**Function**: Introduces embedded declarative clauses (reports content, not exact words)
**IPA**: /me.na/
**Position**: After the main clause, before the embedded statement
**Structure**: `[Main clause] mena [Embedded statement]`

**Examples**:
```
mia kela mena shia wepu
1SG understand DECL 3SG leave
(I understand that ko left.)

shia nophi mena thia wepu
3SG say DECL 2SG leave
(She said that you left.)

nai phaelo mena remo wela
1PL feel DECL sun beautiful
(We feel that the sun is beautiful.)
```

**Nesting**: `mena` clauses can nest:
```
mia kela mena thia phaelo mena shia wepu
1SG understand DECL 2SG feel DECL 3SG leave
(I understand that you feel that ko left.)
```

**Comparison with `shola`**:
- `shia shola "mia wepu" nophi` = She said: "I'm leaving." (exact words)
- `shia nophi mena thia wepu` = She said that you left. (reported content)

---

### `wena` - Interrogative Complementizer (INT.COMP)

**Function**: Introduces embedded yes/no questions
**IPA**: /we.na/
**Position**: After the main clause, before the embedded question
**Structure**: `[Main clause] wena [Embedded yes/no question]`

**Examples**:
```
mia wena shia wepu phaelo
1SG INT.COMP 3SG leave wonder
(I wonder whether ko left.)

shia wena mia to nila nomei
3SG INT.COMP 1SG PST see ask
(She asked whether I had seen.)

nai wena remo wela ma kela
1PL INT.COMP sun beautiful NEG know
(We don't know whether the sun is beautiful.)
```

**Distinction from related words**:
- `wa` (question particle): Marks direct questions expecting response
- `thoe` (conditional conjunction): Marks hypothetical conditions with consequences
- `wena` (interrogative complementizer): Embeds questions as content

**Comparison**:
- `wa thia wepu` = Are you leaving? (direct question)
- `thoe thia wepu, mia sola nai` = If you leave, I'll be alone. (conditional)
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

| Word | Gloss | Function |
|------|-------|----------|
| `rena` | REL | Introduces relative clauses |
| `shola` | QUOT | Introduces direct quotation (exact words) |
| `mena` | DECL | Introduces embedded statements (reported content) |
| `wena` | INT.COMP | Introduces embedded yes/no questions |
| `kona` | VOC | Marks direct address |

---

**Related Documentation:**
- Particles: `documents/grammar/PARTICLE_REFERENCE.md`
- Complex constructions: `documents/grammar/05-complex-constructions.md`
- Main instructions: `CLAUDE.md`
