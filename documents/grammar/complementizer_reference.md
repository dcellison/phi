# Phi Complementizer and Vocative Reference

This document covers complementizers and the vocative marker—function words that introduce subordinate clauses or mark direct address. These are distinct from particles (which are single-syllable and fit the three-slot system).

---

## Complementizers

Complementizers are one-syllable function words that introduce subordinate clauses, and they hold the bracketing shape of the function-word charter: a fricative digraph and a vowel, a shape nothing else in the language takes. They announce the relationship between the main clause and the embedded clause that follows, and the three opener and closer pairs share a sound pattern: each pair keeps its consonant and contrasts only the vowel, `-a` to open a frame and `-o` to close it.

### `wha` - Relativizer (REL)

**Function**: Introduces relative clauses that describe a noun
**IPA**: /ˈre̞.n̪ä/
**Position**: Before the relative clause and the noun it modifies
**Structure**: `[wha CLAUSE] NOUN`

**Examples**:
```
[wha nophi kealo] miona
[REL story create] person
(the person who creates stories)

[wha mia to nila] shelu
[REL 1SG PST see] book
(the book that I saw)

[wha mua shelira nai] ruela
[REL LOC forest be] path
(the path that is in the forest)
```

**Headless relative clauses** (when the noun is implicit):
```
[wha thia to kealo]
[REL 2SG PST create]
(what you created)
```

---

### `sha` / `sho` - Quotative (QUOT.COMP / QUOT.COMP.CLOSE)

**Function**: Introduces and closes direct speech, preserving the exact words spoken
**IPA**: /ˈʃo̞.lä/ and /ˈʃo̞.lo̞/
**Position**: `sha` opens the quoted material; `sho` closes it. The main verb follows `sho`.
**Structure**: `[Subject] sha [Quote] sho [Verb of speaking or receiving speech]`

The frame verb may be a verb of speaking (`haolu`, `shemui`, `thilou`) or of receiving speech (`hea`): the quote is bounded by `sho` either way, and hearing exact words is as sayable as speaking them.

**`sho` is required.** It marks where the quotation ends so the main verb can follow unambiguously.

**Examples**:
```
shia sha sileta mioru nai sho haolu.
3SG QUOT.COMP sun beautiful be QUOT.COMP.CLOSE speak.
(They say, "The sun is beautiful.")

mia sha mia so wepu sho to haolu.
1SG QUOT.COMP 1SG FUT go QUOT.COMP.CLOSE PST speak.
(I said: "I will leave.")
```

**Note**: Distinct from `tha`/`tho` (declarative); `sha`/`sho` preserves exact words, `tha`/`tho` reports content/meaning.

---

### `tha` / `tho` - Declarative Complementizer (DECL.COMP / DECL.COMP.CLOSE)

**Function**: Introduces and closes embedded declarative clauses (reports content, not exact words)
**IPA**: /ˈme̞.n̪ä/ and /ˈme̞.n̪o̞/
**Position**: `tha` opens the embedded statement; `tho` closes it. The main verb follows `tho`.
**Structure**: `[Subject] tha [Embedded statement] tho [Main verb]`

**`tho` is required.** Because Phi's SOV word order places the main verb after the complement clause, `tho` is needed to mark where the embedded clause ends and the main verb begins. Without it, two adjacent verbs would be ambiguous.

**Examples**:
```
mia tha shia to wepu tho shelomu.
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE understand.
(I understand that they left.)

shia tha thia to wepu tho to haolu.
3SG DECL.COMP 2SG PST go DECL.COMP.CLOSE PST speak.
(They said that you left.)

mia tha sileta sulae nai tho phaelo.
1SG DECL.COMP sun warm be DECL.COMP.CLOSE feel.
(I feel that the sun is warm.)
```

**Nesting**: `tha`/`tho` clauses can nest. Each `tha` must have its own `tho`:
```
mia tha thia tha shia to wepu tho phaelo tho shelomu.
1SG DECL.COMP 2SG DECL.COMP 3SG PST go DECL.COMP.CLOSE feel DECL.COMP.CLOSE understand.
(I understand that you feel that they left.)
```

**Comparison with `sha`/`sho`**:
- `shia sha mia wepu sho to haolu` = They said: "I'm leaving." (exact words)
- `shia tha thia to wepu tho to haolu` = They said that you left. (reported content)

---

### `pha` / `pho` - Interrogative Complementizer (INT.COMP / INT.COMP.CLOSE)

**Function**: Introduces and closes embedded yes/no questions
**IPA**: /ˈwe̞.lä/ and /ˈwe̞.lo̞/
**Position**: `pha` opens the embedded question; `pho` closes it. The main verb follows `pho`.
**Structure**: `[Subject] pha [Embedded yes/no question] pho [Main verb]`

**`pho` is required.** Like `tha`/`tho` and `sha`/`sho`, the closer marks where the embedded clause ends so the main verb can follow without ambiguity.

**Examples**:
```
mia pha shia to wepu pho phaelo.
1SG INT.COMP 3SG PST go INT.COMP.CLOSE feel.
(I wonder whether they left.)

shia pha mia to nila pho to thilou.
3SG INT.COMP 1SG PST see INT.COMP.CLOSE PST inquire.
(They asked whether I had seen.)

lo mia pha sileta mioru nai pho ma shelomu.
PL 1SG INT.COMP sun beautiful be INT.COMP.CLOSE NEG understand.
(We don't know whether the sun is beautiful.)
```

**Distinction from related words**:
- `wa` (question particle): Marks direct questions expecting response
- `lu` (Slot 0 conditional particle): Marks hypothetical conditions with consequences
- `pha`/`pho` (interrogative complementizer pair): Embeds questions as content

**Comparison**:
- `wa thia wepu` = Are you going? (direct question)
- `lu thia wepu. mia so ma towe phaelo` = If you go, I won't feel well. (conditional)
- `mia pha thia wepu pho phaelo` = I wonder whether you're going. (embedded question)

---

## Source material and names

Complementizers frame Phi clauses only. Foreign wording, source-script names, source-form exact values and records, identifiers, formulas, and other unassimilated artifacts remain outside Phi syntax and appear separately through the surrounding document, interface, or conversation. Exact integers from 0 through 242 may also be rendered with internal Phi numerals when that representation is adequate. Phi can refer to a separately presented record, translate its meaning with `tha ... tho`, or quote grammatical Phi with `sha ... sho`, but no outside token occupies a nominal position merely because it is printed beside Phi.

`ne` directly licenses one lowercase name-form of two, three, or four legal Phi syllables (`ne samira`) or a listed content word borne as a name. A preferred name with five or more syllables, multiple tokens, a non-Phi shape, or dependence on another script remains outside the Phi passage unless the bearer or naming community accepts a valid Phi-form onym.

---

## Vocative

The vocative is a separate part of speech for direct address, existing outside the clause structure.

### `kona` - Vocative Marker (VOC)

**Function**: Announces that someone is being directly addressed
**IPA**: /ˈko̞.n̪ä/
**Position**: Before the name/title of the addressee, outside the main clause
**Structure**: `kona [ne] [Name/Title]. [Sentence]`

**Examples**:
```
kona melu. mia ha nai.
VOC friend. 1SG PROX be.
(Friend, I am here.)

kona ne sa sulae. wa thia towe nai.
VOC NAME HON.RESPECT sulae. Q 2SG well be.
(Honored sulae, are you well?)

kona ne ni moli. mia thia lothea.
VOC NAME HON.INTIM moli. 1SG 2SG love.
(Dear moli, I love you.)
```

**Note**: The vocative phrase is extra-clausal—it frames who is being addressed but does not participate in the main clause's subject-object-verb structure. When addressing someone by name, the proper name particle `ne` precedes the name (and any honorific). When addressing by role or common noun (e.g., `melu`, "friend"), `ne` is not used.

---

## Summary

| Word | Gloss | Function | Closer |
|------|-------|----------|--------|
| `wha` | REL | Introduces relative clauses | — (pre-nominal position bounds it) |
| `sha` | QUOT.COMP | Opens direct quotation (exact words) | `sho` (required) |
| `sho` | QUOT.COMP.CLOSE | Closes direct quotation | — |
| `tha` | DECL.COMP | Opens embedded statements (reported content) | `tho` (required) |
| `tho` | DECL.COMP.CLOSE | Closes embedded statements | — |
| `pha` | INT.COMP | Opens embedded yes/no questions | `pho` (required) |
| `pho` | INT.COMP.CLOSE | Closes embedded yes/no questions | — |
| `kona` | VOC | Marks direct address | none (extra-clausal) |

---

**Related Documentation:**
- Particles: `documents/grammar/particle_reference.md`
- Complex constructions: the manual, Part V (`manual/part5_complex/`)
- Main instructions: `project/development_protocol.md`
