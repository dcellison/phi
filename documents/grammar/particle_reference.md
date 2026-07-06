# Phi Particle Reference

This document provides a complete inventory of all particles in Phi, organized by the three-slot system. All particles follow strict CV structure and announce their grammatical function BEFORE the content they modify.

## The Three-Slot System

Particles appear in a fixed order based on their slot:

**[Slot 0] [Subject] [Object] [Slot 1 stack] [Verb]** — Slot 2 particles attach directly before whichever word they modify

Example:
```
pi mia so ki po shelomui.
POL 1SG FUT PFV POT understand.
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
wa thia lumani lothea.
Q 2SG family love.
(Do you love your family?)
```

### `no` - Imperative Marker (IMP)
**Function**: Announces that the sentence is a command or request
**Position**: Sentence-initial only
**Example**:
```
no lumani naphe.
IMP family help.
(Help the family.)
```

### `lu` - Realis Conditional (COND)
**Function**: Announces a real or likely conditional ("if")
**Position**: Sentence-initial only
**Example**:
```
lu thia naphe. mia towe phaelo.
COND 2SG help. 1SG well feel.
(If you help, I will feel well.)
```

### `lu he` - Irrealis Conditional (COND.IRR)
**Function**: Announces an unreal, hypothetical, or counterfactual conditional ("if only", "if it were that")
**Position**: Sentence-initial only (two particles)
**Example**:
```
lu he mia to naphe. shia to ma wepu.
COND IRR 1SG PST help. 3SG PST NEG go.
(If I had helped [but I didn't], they would not have left.)
```

### `su` - Optative Marker (OPT)
**Function**: Announces a wish, hope, or prayer
**Position**: Sentence-initial only
**Example**:
```
su sila towe nai.
OPT community well be.
(May the community be well / I hope the community is well.)
```

### `pi` - Politeness Marker (POL)
**Function**: Announces that the entire utterance is polite/respectful
**Position**: Sentence-initial only (can combine with other Slot 0 particles)
**Example**:
```
pi no lumani naphe.
POL IMP family help.
(Please help the family.)

pi wa thia po naphe.
POL Q 2SG POT help.
(Could you please help?)
```

---

## Slot 1: Verb Phrase Particles

These particles appear **before the verb** and announce temporal, aspectual, evidential, and modal information about the action. When multiple Slot 1 particles appear together, they **must follow this order**:

**Tense > Aspect > Voice > Evidentiality > Modality > Negation**

Each rank admits at most one particle per clause; the single ruled pairing is voice's `se ka`, the passive of a causative (canon, *One per rank*).

### Tense Particles

#### `to` - Past Tense (PST)
**Function**: Announces action occurred in the past
**Example**:
```
mia to shelomui.
1SG PST understand.
(I understood.)
```

#### `so` - Future Tense (FUT)
**Function**: Announces action will occur in the future
**Example**:
```
mia so shelomui.
1SG FUT understand.
(I will understand.)
```

**Note**: Present tense is unmarked (zero particle).

### Aspect Particles

#### `ki` - Perfective Aspect (PFV)
**Function**: Announces completion at the tense's reference time: `ki` have done, `to ki` had done, `so ki` will have done
**Example**:
```
mia to ki shelomui.
1SG PST PFV understand.
(I had understood.)
```

#### `si` - Imperfective Aspect (IPFV)
**Function**: Announces ongoing, progressive action — in mid-flow; habits take `ro`
**Example**:
```
mia si shelomui.
1SG IPFV understand.
(I am understanding.)
```

#### `pa` - Inchoative Aspect (INCH)
**Function**: Announces the beginning of an action
**Example**:
```
mia pa shelomui.
1SG INCH understand.
(I begin to understand / I am starting to understand.)
```

#### `te` - Cessative Aspect (CESS)
**Function**: Announces the ending of an action
**Example**:
```
mia te shelomui.
1SG CESS understand.
(I stop understanding / I cease to understand.)
```

#### `ro` - Habitual Aspect (HAB)
**Function**: Announces that the action recurs regularly or characteristically
**Example**:
```
mia ro theo.
1SG HAB read.
(I read regularly / I habitually read.)
```

### Voice Particles

#### `se` - Passive Voice (PASS)
**Function**: Announces that the subject receives the action (promotes object to subject)
**Structure**: `[Patient] se [Verb]`
**Example**:
```
Active:  mia nophi kealo.    (I create the story.)
Passive: nophi se kealo.     (The story is created.)
```

#### `ka` - Causative Voice (CAUS)
**Function**: Announces that the subject causes someone/something else to do the action — a voice particle: like `se`, it restructures who acts and claims nothing about certainty or obligation
**Structure**: Changes sentence structure - the causer becomes subject, original subject becomes object
**Examples**:
```
Base:      lopia nulae.           (The child sleeps.)
Causative: mia lopia ka nulae.    (I make the child sleep.)

Base:      thia nophi shelomui.      (You understand the story.)
Causative: mia thia nophi ka shelomui. (I make you understand the story.)
```
**Combinations**: the voice pair is fixed `se ka` (`lopia se ka nulae.` — The child is made to sleep.); with modals, voice precedes modality (`ka na` must make, `ka po` can make); `ka ma` denies the causation itself.

### Evidentiality Particles

Evidential particles mark the source of the speaker's knowledge. They are optional — an unmarked sentence is a plain assertion, claiming no source — and they provide explicit epistemic transparency when the source is part of the message.

#### `hi` - Direct Evidence (DIR)
**Function**: Announces that the speaker directly witnessed the event through their own senses
**Position**: After voice, before modality (optional; `hi` adds the witness claim explicitly)
**Example**:
```
mia hi nila.
1SG DIR see.
(I see [I directly witness this].)
```

#### `ke` - Inferential Evidence (INFER)
**Function**: Announces that the speaker inferred the information from evidence
**Example**:
```
shia to ke wepu.
3SG PST INFER go.
(She left [I infer from evidence].)
```

#### `ti` - Reportative Evidence (REP)
**Function**: Announces that the speaker received this information from another source
**Example**:
```
lo miona to ti naphe.
PL person PST REP help.
(People helped [I was told].)
```

#### `ho` - Assumptive Evidence (ASSUM)
**Function**: Announces that the speaker is assuming or supposing rather than knowing
**Example**:
```
thia ho shelomui.
2SG ASSUM understand.
(You understand [I assume].)
```

### Modality Particles

#### `po` - Possibility/Ability Modal (POT)
**Function**: Announces that the action is possible or that the subject has ability
**Example**:
```
mia po shelomui.
1SG POT understand.
(I can understand / I am able to understand.)
```

#### `na` - Necessity Modal (NEC)
**Function**: Announces that the action is necessary or obligatory
**Example**:
```
mia na naphe.
1SG NEC help.
(I must help / I have to help.)
```

### Negation

#### `ma` - Negation (NEG)
**Function**: Announces that the action does NOT occur
**Position**: After all other Slot 1 particles
**Example**:
```
mia ma shelomui.
1SG NEG understand.
(I do not understand.)

mia so ki po ma shelomui.
1SG FUT PFV POT NEG understand.
(I will not be able to have understood.)
```

**Modal negation conventions** (order is always modal-then-`ma`):
- `po ma V` — cannot (the possibility is denied)
- `na ma V` — must not (the necessity is to refrain)
- `ka ma V` — the causation is denied (I did not make them V); making
  someone refrain takes its own verb or two clauses.
- "Need not" (absence of obligation) is never expressed by reordering.
  Use the freedom periphrasis: `S lila V ralu nai` — "S is free as to
  V-ing": `thia lila wepu ralu nai` (you need not go).

### Stacking Example

When multiple Slot 1 particles combine, they follow strict ordering:
```
mia to si ke po ma shelomui.
1SG PST IPFV INFER POT NEG understand.
(I was not being able to understand [I infer].)
```
Order: Tense (`to`) > Aspect (`si`) > Voice (`se`) > Evidentiality (`hi`/`ke`/`ti`/`ho`) > Modality (`po`) > Negation (`ma`)

---

## Slot 2: Word-Level Particles

These particles appear **immediately before** the specific word they modify (noun, verb, or adjective). When several modify the same word, wider relations stand earlier — `we`/`li` > `ha`/`ra` > `lo`/numerals > `ko` > `ru`/`mo` > word — modifier-first inside the phrase (canon, *Slot 2 nests*).

### Number

#### `lo` - Plural Marker (PL)
**Function**: Announces plurality for unquantified nouns
**Usage**: Use `lo` when indicating plurality WITHOUT a number or quantifier. When a numeral or quantifier is present, the number itself indicates plurality, making `lo` redundant.

**With `lo` (unquantified plural)**:
```
lo melu.
PL friend.
(friends - plural, no specific quantity)

mia lo melu phaelo.
1SG PL friend feel.
(I feel my friends - multiple, uncounted)
```

**Without `lo` (number implies plurality)**:
```
wi melu          (two friends - 'wi' already implies plural)
ta shao lipha shiro (three trees - number implies plural)
sheloi melu      (many friends - quantifier implies plural)
```

**Rule**: Never combine `lo` with numerals or quantifiers—this would be redundant.

### Ordinality

#### `nu` - Ordinal Marker (ORD)
**Function**: Announces that a numeral indicates position rather than quantity
**Structure**: `nu [cardinal number] [noun]`
**Example**:
```
nu ta lopia.
ORD one child.
(first child)

nu wi philo.
ORD two day.
(second day)
```

### Focus

#### `ko` - Focus Marker (FOC)
**Function**: Announces emphatic focus on a particular element
**Example**:
```
mia ko lothea shelomui.
1SG FOC love understand.
(I understand *love* [specifically, not other things].)
```

### Addition and restriction

#### `we` - Additive (ALSO)
**Function**: Announces that the marked element is added to what came before ("also", "too")
**Example**:
```
we mia shua.
ALSO 1SG come.
(I come too.)
```

#### `li` - Restrictive (RESTR)
**Function**: Announces that the statement holds for the marked element alone ("only")
**Example**:
```
li shia shelomui.
RESTR 3SG understand.
(Only they understand.)
```
**Note**: `li` fences identity — who, which, when — never quantity; counts are stated exactly or with `henoi` (canon: *li is a fence, not a sigh*).

### Intensity

#### `ru` - Intensifier (INTS)
**Function**: Announces intensification of the following word ("very", "truly")
**Example**:
```
ru welao.
INTS good.
(very good)
```

### Comparison

#### `mo` - Comparative Marker (CMPR)
**Function**: Announces comparative degree ("more")
**Example**:
```
thepalu sheo shelira mo phelora nai.
garden THAN forest CMPR beautiful be.
(The garden is more beautiful than the forest.)
```

#### `mo ko` - Superlative Marker (SUPL)
**Function**: Announces superlative degree ("most")
**Example**:
```
ha thepalu mo ko phelora nai.
PROX garden CMPR FOC beautiful be.
(This garden is the most beautiful.)
```

### Deixis (Demonstratives)

#### `ha` - Proximal Demonstrative (PROX)
**Function**: Announces proximity ("this/these")
**Example**:
```
ha melu.
PROX friend.
(this friend)
```

#### `ra` - Distal Demonstrative (DIST)
**Function**: Announces distance ("that/those")
**Example**:
```
ra melu.
DIST friend.
(that friend)
```

### Proper Name Marker

#### `ne` - Proper Name (NAME)
**Function**: Announces that the following word is a proper name, not vocabulary
**Position**: Before the name (and before any honorific)
**Example**:
```
ne keruko shua.
NAME keruko come.
(keruko comes.)
```
**Note**: The default when no honorific is present — formal and neutral speech keep it at every mention, and the family register may let an established name rest bare (canon: *Names are made of Phi*). Optional when an honorific already signals that a name follows. Also used with place names and other proper nouns.

### Honorifics

These particles announce the speaker's social relationship to the person being named, appearing **before the name** and after `ne` when present.

#### `sa` - Respect Honorific (HON.RESPECT)
**Function**: Announces respect for a mentor, elder, or person of authority
**Example**:
```
ne sa sulae.
NAME HON.RESPECT sulae.
(honored sulae)
```

#### `ni` - Intimacy Honorific (HON.INTIM)
**Function**: Announces intimacy with a close friend or family member
**Example**:
```
ne ni moli.
NAME HON.INTIM moli.
(dear moli)
```

#### `le` - Role Honorific (HON.ROLE)
**Function**: Announces respect for a community role or function
**Example**:
```
ne le siora.
NAME HON.ROLE siora.
(respected siora [in their role])
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
- **`wia`** (which, how many) - announces inquiry about selection or quantity

**Examples**:
```
sua lothea shelomui.
who love understand.
(Who understands love?)

mia hina shelomui.
1SG what understand.
(What do I understand?)

thia weno wepu.
2SG when go.
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
mia lothea shelomui. kewai shia ma shelomui.
1SG love understand. CONTR 3SG NEG understand.
(I understand love. However, they do not understand.)
```

---

## Coordinating Conjunctions

These announce relationships between equal elements (words, phrases, or clauses).

- **`nela`** - and (basic coordination)
- **`thona`** - but (adversative coordination)
- **`sola`** - or (alternative coordination)

**Examples**:
```
mia shea nela sila lothea.
1SG peace COORD community love.
(I love peace and community.)

wa [shia phelora] sola [thiku].
Q [3SG beautiful] OR [small].
(Is it beautiful or small?)
```

---

## Special Pronouns

### `miso` - Reflexive Pronoun (REFL)
**Function**: Announces that the action refers back to the subject
**Example**:
```
mia miso nila.
1SG REFL see.
(I see myself.)
```

### `wiso` - Reciprocal Pronoun (RECP)
**Function**: Announces mutual action between plural subjects
**Example**:
```
lo mia wiso lothea.
PL 1SG RECP love.
(We love each other.)
```

---

## Summary: Particle Slot Quick Reference

| Slot | Function | Examples |
|------|----------|----------|
| **0** | Sentence frame | `wa`, `no`, `lu`, `lu he`, `su`, `pi` |
| **1** | Verb phrase (Tense > Aspect > Voice > Evid > Modal > Neg) | `to`, `so`, `ki`, `si`, `pa`, `te`, `ro`, `se`, `hi`, `ke`, `ti`, `ho`, `po`, `na`, `ka`, `ma` |
| **2** | Word-level | `lo`, `nu`, `ko`, `mo`, `ha`, `ra`, `ne`, `sa`, `ni`, `le`, `ru`, `we`, `li` |

**Note**: Complementizers (`rena`, `shola`/`sholo`, `mena`/`meno`, `wela`/`welo`) and vocative (`kona`) are not particles—see `complementizer_reference.md`.

---

**Related Documentation:**
- Complete grammar: `documents/grammar/01-principles.md` through `06-numerals.md`
- The three-slot system: `documents/grammar/02-particles.md`
- Main instructions: `documents/development_protocol.md`
