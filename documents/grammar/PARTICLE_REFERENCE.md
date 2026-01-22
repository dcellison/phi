# Phi Particle Reference

This document provides a complete inventory of all particles in Phi, organized by the three-slot system. All particles follow strict CV structure and announce their grammatical function BEFORE the content they modify.

## The Three-Slot System

Particles appear in a fixed order based on their slot:

**[Slot 0] [Slot 1 stack] [Subject] [Slot 2] [Content]**

Example:
```
pi mia so ki po kela
POL 1SG FUT PFV POSS understand
(Politely, I will be able to have understood.)
```

---

## Slot 0: Sentence Frame Particles

These particles appear at the **very beginning** of a sentence and announce the communicative intent of the entire utterance. They frame how the listener should receive what follows.

### `wa` - Question Marker (Q)
**Function**: Announces that the sentence is a yes/no question
**Position**: Sentence-initial only
**Example**:
```
wa thi minu lothea
Q 2SG family love
(Do you love your family?)
```

### `no` - Imperative Marker (IMP)
**Function**: Announces that the sentence is a command or request
**Position**: Sentence-initial only
**Example**:
```
no minu shele
IMP family help
(Help the family.)
```

### `lu` - Realis Conditional (COND)
**Function**: Announces a real or likely conditional ("if")
**Position**: Sentence-initial only
**Example**:
```
lu thi shele, mia wela hisu
COND 2SG help, 1SG good feel
(If you help, I will feel good.)
```

### `lu he` - Irrealis Conditional (COND.IRR)
**Function**: Announces an unreal, hypothetical, or counterfactual conditional ("if only", "if it were that")
**Position**: Sentence-initial only (two particles)
**Example**:
```
lu he mia to shele, shia ma to wepu
COND IRR 1SG PST help, 3SG NEG PST leave
(If I had helped [but I didn't], ko would not have left.)
```

### `su` - Optative Marker (OPT)
**Function**: Announces a wish, hope, or prayer
**Position**: Sentence-initial only
**Example**:
```
su weola wela nio
OPT community good be
(May the community be well / I hope the community is well.)
```

### `pi` - Politeness Marker (POL)
**Function**: Announces that the entire utterance is polite/respectful
**Position**: Sentence-initial only (can combine with other Slot 0 particles)
**Example**:
```
pi no minu shele
POL IMP family help
(Please help the family.)

pi wa thi po shele
POL Q 2SG POSS help
(Could you please help?)
```

---

## Slot 1: Verb Phrase Particles

These particles appear **before the verb** and announce temporal, aspectual, evidential, and modal information about the action. When multiple Slot 1 particles appear together, they **must follow this order**:

**Tense > Aspect > Voice > Evidentiality > Modality > Negation**

### Tense Particles

#### `to` - Past Tense (PST)
**Function**: Announces action occurred in the past
**Example**:
```
mia to kela
1SG PST understand
(I understood.)
```

#### `so` - Future Tense (FUT)
**Function**: Announces action will occur in the future
**Example**:
```
mia so kela
1SG FUT understand
(I will understand.)
```

**Note**: Present tense is unmarked (zero particle).

### Aspect Particles

#### `ki` - Perfective Aspect (PFV)
**Function**: Announces completed action with present relevance
**Example**:
```
mia to ki kela
1SG PST PFV understand
(I have understood.)
```

#### `si` - Imperfective Aspect (IPFV)
**Function**: Announces ongoing, habitual, or progressive action
**Example**:
```
mia si kela
1SG IPFV understand
(I am understanding / I habitually understand.)
```

#### `pa` - Inchoative Aspect (INCH)
**Function**: Announces the beginning of an action
**Example**:
```
mia pa kela
1SG INCH understand
(I begin to understand / I am starting to understand.)
```

#### `te` - Cessative Aspect (CESS)
**Function**: Announces the ending of an action
**Example**:
```
mia te kela
1SG CESS understand
(I stop understanding / I cease to understand.)
```

### Voice Particles

#### `se` - Passive Voice (PASS)
**Function**: Announces that the subject receives the action (promotes object to subject)
**Structure**: `[Patient] se [Verb]`
**Example**:
```
Active:  mia nophi kealo    (I create the story.)
Passive: nophi se kealo     (The story is created.)
```

### Evidentiality Particles

Evidential particles mark the source of the speaker's knowledge. They are optional—direct experience is the unmarked default—but provide explicit epistemic transparency when needed.

#### `hi` - Direct Evidence (DIR)
**Function**: Announces that the speaker directly witnessed the event through their own senses
**Position**: After voice, before modality (optional, as direct experience is the default)
**Example**:
```
mia hi nila
1SG DIR see
(I see [I directly witness this].)
```

#### `ke` - Inferential Evidence (INFER)
**Function**: Announces that the speaker inferred the information from evidence
**Example**:
```
shia to ke wepu
3SG PST INFER leave
(She left [I infer from evidence].)
```

#### `ti` - Reportative Evidence (REP)
**Function**: Announces that the speaker received this information from another source
**Example**:
```
lo miona ti shele
PL person REP help
(People helped [I was told].)
```

#### `ho` - Assumptive Evidence (ASM)
**Function**: Announces that the speaker is assuming or supposing rather than knowing
**Example**:
```
thi ho kela
2SG ASM understand
(You understand [I assume].)
```

### Modality Particles

#### `po` - Possibility/Ability Modal (POSS)
**Function**: Announces that the action is possible or that the subject has ability
**Example**:
```
mia po kela
1SG POSS understand
(I can understand / I am able to understand.)
```

#### `na` - Necessity Modal (NEC)
**Function**: Announces that the action is necessary or obligatory
**Example**:
```
mia na shele
1SG NEC help
(I must help / I have to help.)
```

#### `ka` - Causative Modal (CAUS)
**Function**: Announces that the subject causes someone/something else to do the action
**Structure**: Changes sentence structure - the causer becomes subject, original subject becomes object
**Examples**:
```
Base:      pilo nima           (The child sleeps.)
Causative: mia pilo ka nima    (I make the child sleep.)

Base:      thi thola kela      (You understand the story.)
Causative: mia thi thola ka kela (I make you understand the story.)
```

### Negation

#### `ma` - Negation (NEG)
**Function**: Announces that the action does NOT occur
**Position**: After all other Slot 1 particles
**Example**:
```
mia ma kela
1SG NEG understand
(I do not understand.)

mia so ki po ma kela
1SG FUT PFV POSS NEG understand
(I will not be able to have understood.)
```

### Stacking Example

When multiple Slot 1 particles combine, they follow strict ordering:
```
mia to si ke po ma kela
1SG PST IPFV INFER POSS NEG understand
(I was not being able to understand [I infer].)
```
Order: Tense (`to`) > Aspect (`si`) > Voice (`se`) > Evidentiality (`hi`/`ke`/`ti`/`ho`) > Modality (`po`) > Negation (`ma`)

---

## Slot 2: Word-Level Particles

These particles appear **immediately before** the specific word they modify (noun, verb, or adjective).

### Number

#### `lo` - Plural Marker (PL)
**Function**: Announces plurality for unquantified nouns
**Usage**: Use `lo` when indicating plurality WITHOUT a number or quantifier. When a numeral or quantifier is present, the number itself indicates plurality, making `lo` redundant.

**With `lo` (unquantified plural)**:
```
lo whelea
PL friend
(friends - plural, no specific quantity)

mia lo whelea hisu
1SG PL friend feel
(I feel my friends - multiple, uncounted)
```

**Without `lo` (number implies plurality)**:
```
wi whelea          (two friends - 'wi' already implies plural)
ta shao lipha shiro (three trees - number implies plural)
sheloi whelea      (many friends - quantifier implies plural)
```

**Rule**: Never combine `lo` with numerals or quantifiers—this would be redundant.

### Ordinality

#### `nu` - Ordinal Marker (ORD)
**Function**: Announces that a numeral indicates position rather than quantity
**Structure**: `nu [cardinal number] [noun]`
**Example**:
```
nu ta pilo
ORD one child
(first child)

nu wi nila
ORD two day
(second day)
```

### Focus

#### `ko` - Focus Marker (FOC)
**Function**: Announces emphatic focus on a particular element
**Example**:
```
mia ko lothea kela
1SG FOC love understand
(I understand *love* [specifically, not other things].)
```

### Comparison

#### `mo` - Comparative Marker (CMPR)
**Function**: Announces comparative degree ("more")
**Example**:
```
noshale sheo shiro mo wela nio
garden than forest CMPR good be
(The garden is more beautiful than the forest.)
```

#### `mo ko` - Superlative Marker (SUPL)
**Function**: Announces superlative degree ("most")
**Example**:
```
ha noshale mo ko wela nio
PROX garden CMPR FOC good be
(This garden is the most beautiful.)
```

### Deixis (Demonstratives)

#### `ha` - Proximal Demonstrative (PROX)
**Function**: Announces proximity ("this/these")
**Example**:
```
ha whelea
PROX friend
(this friend)
```

#### `ra` - Distal Demonstrative (DIST)
**Function**: Announces distance ("that/those")
**Example**:
```
ra whelea
DIST friend
(that friend)
```

### Honorifics

These particles announce the speaker's social relationship to the person being named, appearing **before the name**.

#### `sa` - Respect Honorific (HON.RESPECT)
**Function**: Announces respect for a mentor, elder, or person of authority
**Example**:
```
sa Thala
HON.RESPECT Thala
(Honored Thala / Esteemed Thala)
```

#### `ni` - Intimacy Honorific (HON.INTIM)
**Function**: Announces intimacy with a close friend or family member
**Example**:
```
ni Hino
HON.INTIM Hino
(Dear Hino / Beloved Hino)
```

#### `le` - Role Honorific (HON.ROLE)
**Function**: Announces respect for a community role or function
**Example**:
```
le Mako
HON.ROLE Mako
(Respected Mako [in their role])
```

---

## Interrogative Pronouns

While not technically particles, these function words occupy argument positions and announce what information is being sought.

- **`sua`** (who) - announces inquiry about a person
- **`hina`** (what) - announces inquiry about a thing or action
- **`weno`** (when) - announces inquiry about time
- **`kua`** (where) - announces inquiry about place
- **`misa`** (why) - announces inquiry about reason
- **`thela`** (how) - announces inquiry about manner

**Examples**:
```
sua lothea kela
who love understand
(Who understands love?)

mia hina kela
1SG what understand
(What do I understand?)

thi weno wepu
2SG when leave
(When do you leave?)
```

---

## Discourse Adverbs

These announce how the current sentence relates to prior discourse. They appear **after any Slot 0 particle but before the subject**.

**Position**: `[Slot 0] [Discourse Adverb] [Subject]...`

- **`thelao`** - therefore, for this reason (causal connection)
- **`kewai`** - however, on the other hand (contrastive connection)
- **`sheno`** - in addition, furthermore (additive connection)
- **`phisu`** - for example, for instance (illustrative connection)

**Example**:
```
mia lothea kela. kewai, shia ma kela.
1SG love understand. however, 3SG NEG understand
(I understand love. However, ko does not understand.)
```

---

## Coordinating Conjunctions

These announce relationships between equal elements (words, phrases, or clauses).

- **`nela`** - and (basic coordination)
- **`thona`** - but (adversative coordination)
- **`sola`** - or (alternative coordination)

**Examples**:
```
mia sela nela weola lothea
1SG peace COORD community love
(I love peace and community.)

wa [shia miro] sola [philo]
Q [3SG beautiful] OR [calm]
(Is it beautiful or calm?)
```

---

## Special Pronouns

### `miso` - Reflexive Pronoun (REFL)
**Function**: Announces that the action refers back to the subject
**Example**:
```
mia miso nila
1SG REFL see
(I see myself.)
```

### `wiso` - Reciprocal Pronoun (RECP)
**Function**: Announces mutual action between plural subjects
**Example**:
```
nio wiso lothea
1PL RECP love
(We love each other.)
```

---

## Summary: Particle Slot Quick Reference

| Slot | Function | Examples |
|------|----------|----------|
| **0** | Sentence frame | `wa`, `no`, `lu`, `lu he`, `su`, `pi` |
| **1** | Verb phrase (Tense > Aspect > Voice > Evid > Modal > Neg) | `to`, `so`, `ki`, `si`, `pa`, `te`, `se`, `hi`, `ke`, `ti`, `ho`, `po`, `na`, `ka`, `ma` |
| **2** | Word-level | `lo`, `nu`, `ko`, `mo`, `ha`, `ra`, `sa`, `ni`, `le`, `ru` |

**Note**: Complementizers (`rena`, `shola`, `mena`, `wena`) and vocative (`kona`) are not particles—see `COMPLEMENTIZER_REFERENCE.md`.

---

**Related Documentation:**
- Complete grammar: `documents/grammar/01-principles.md` through `06-numerals.md`
- The three-slot system: `documents/grammar/02-particles.md`
- Main instructions: `CLAUDE.md`
