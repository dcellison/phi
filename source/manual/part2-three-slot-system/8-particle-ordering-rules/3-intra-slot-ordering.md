# Intra-Slot Ordering

## Systematic Internal Structure

Each of phi's three slots maintains **rigid internal ordering** based on semantic scope and functional hierarchy. These intra-slot rules ensure that particles within each slot create coherent, interpretable sequences that build meaning incrementally.

## Slot 0: Sentence Frame Particles

### Internal Ordering Hierarchy

**Evidentiality > Sentence Type > Politeness > Discourse**

```
[Evidence] [Question/Exclamation] [Politeness] [Topic/Contrast] [Content...]
```

This ordering reflects the **logical flow of sentence-level information**:
1. **Evidence source** (what kind of knowledge claim)
2. **Speech act type** (question, statement, exclamation)  
3. **Social register** (politeness level)
4. **Discourse relation** (topic, contrast with previous)

### Complete Slot 0 Ordering

| Position | Category | Particles | Function | Example |
|----------|----------|-----------|----------|---------|
| 1 | Evidentiality | `hi`, `ro`, `mu`, `pe`, `ke`, `no` | Knowledge source | `hi` (direct) |
| 2 | Sentence Type | `wa`, `ho`, `tu`, `hu` | Speech act | `wa` (question) |
| 3 | Politeness | `so` | Social register | `so` (polite) |
| 4 | Discourse | `ha`, `mi` | Information structure | `ha` (topic) |

### Basic Slot 0 Patterns

**Single particles**:
```
hi mia ta whera.        (evidentiality only)
DIR 1SG PRS learn
"I learn." (I see this directly)

wa mia ta whera.        (sentence type only)
Q 1SG PRS learn
"Do I learn?"

so mia ta whera.        (politeness only)
POL 1SG PRS learn
"I politely learn."
```

**Two-particle combinations**:
```
hi wa mia ta whera.     (evidence + question)
DIR Q 1SG PRS learn
"Do I learn?" (I can directly observe the answer)

so hi mia ta whera.     (politeness + evidence)
POL DIR 1SG PRS learn
"I politely learn." (direct evidence, polite register)

ha mi mia ta whera.     (topic + contrast)
TOP CNTR 1SG PRS learn
"As for that topic, but I learn."
```

**Full Slot 0 sequence**:
```
hi wa so ha mia ta whera.
DIR Q POL TOP 1SG PRS learn
"May I politely ask, as for that topic, do I learn?" (I can observe the answer)
```

### Slot 0 Ordering Violations

```
❌ *wa hi mia ta whera.  (sentence type before evidentiality)
❌ *ha so mia ta whera.  (discourse before politeness)
❌ *so wa hi mia ta whera. (politeness before sentence type)
```

## Slot 1: Verb Phrase Particles

### Internal Ordering Hierarchy

**Tense > Aspect > Mood > Negation**

```
[Temporal] [Aspectual] [Modal] [Negative] [Verb]
```

This ordering reflects **temporal-modal-negative scope relationships**:
1. **Tense** (when - broadest temporal scope)
2. **Aspect** (how the action unfolds)
3. **Mood** (modal attitude toward action)
4. **Negation** (polarity - narrowest scope)

### Complete Slot 1 Ordering

| Position | Category | Particles | Function | Example |
|----------|----------|-----------|----------|---------|
| 1 | Tense | `li`, `ta`, `su` | Temporal reference | `li` (past) |
| 2 | Aspect | `we`, `la`, `ni`, `po`, `pu`, `ri`, `wi`, `wu` | Temporal structure | `la` (progressive) |
| 3 | Mood | `to`, `ru` | Modal attitude | `ru` (obligation) |
| 4 | Negation | `me` | Polarity | `me` (negative) |

### Basic Slot 1 Patterns

**Tense + Aspect**:
```
mia li la whera.        (past + progressive)
1SG PST PROG learn
"I was learning."

mia ta ni whera.        (present + perfect)
1SG PRS PRF learn
"I have learned."

mia su po whera.        (future + habitual)
1SG FUT HAB learn
"I will usually learn."
```

**Mood combinations**:
```
mia ru whera.           (obligation only)
1SG OBLG learn
"I should learn."

mia ta ru whera.        (present + obligation)
1SG PRS OBLG learn
"I should learn (now)."

mia su we whera.        (future + desiderative)
1SG FUT DES learn
"I will want to learn."
```

**Negation patterns**:
```
mia me whera.           (negation only)
1SG NEG learn
"I don't learn."

mia li me whera.        (past + negative)
1SG PST NEG learn
"I didn't learn."

mia ru me whera.        (obligation + negative)
1SG OBLG NEG learn
"I should not learn."
```

**Full Slot 1 sequence**:
```
mia li la ru me whera.
1SG PST PROG OBLG NEG learn
"I was not supposed to be learning."
```

### Slot 1 Ordering Violations

```
❌ *mia la li whera.    (aspect before tense)
❌ *mia me ru whera.    (negation before mood)
❌ *mia to ta whera.    (mood before tense)
```

## Slot 2: Core Word Particles

### Internal Ordering Hierarchy

**Case > Animacy > Number > Comparison > Emphasis**

```
[Role] [Semantic Class] [Quantity] [Degree] [Focus] [Word]
```

This ordering reflects **grammatical and semantic priority**:
1. **Case** (grammatical role - most fundamental)
2. **Animacy** (semantic categorization)
3. **Number** (quantification)
4. **Comparison** (degree relationships)
5. **Emphasis** (information structure - closest to word)

### Complete Slot 2 Ordering

| Position | Category | Particles | Function | Example |
|----------|----------|-----------|----------|---------|
| 1 | Case | `si`, `na`, `te` | Grammatical role | `na` (object) |
| 2 | Animacy | `he`, `pi`, `ne` | Semantic class | `he` (human) |
| 3 | Number | `wo`, `lo`, `no` | Quantification | `lo` (plural) |
| 4 | Comparison | `pa`, `mo`, `sa`, `le`, `re` | Degree | `mo` (more) |
| 5 | Emphasis | `ma` | Focus | `ma` (emphasis) |

### Basic Slot 2 Patterns

**Case + Animacy**:
```
na he nowhea           (object + human)
OBJ HUM person
"the person (as object)"

si pi shiphe           (subject + animate)
SUBJ ANIM dog
"the dog (as subject)"
```

**Animacy + Number**:
```
he lo nowhea           (human + plural)
HUM PL person
"people"

ne wo whethea          (inanimate + paucal)
INAN PAUC book
"a few books"
```

**Comparison + Emphasis**:
```
mo ma riphe            (more + emphasis)
CMPR EMPH important
"*more* important"

pa ma misha            (most + emphasis)
SPRL EMPH beautiful
"*most* beautiful"
```

**Full Slot 2 sequence**:
```
na he lo mo ma nowhea
OBJ HUM PL CMPR EMPH person
"*more* people (object, human, plural, emphasized)"
```

### Slot 2 Ordering Violations

```
❌ *he na nowhea       (animacy before case)
❌ *ma mo riphe        (emphasis before comparison)
❌ *lo he nowhea       (number before animacy)
```

## Cross-Slot Intra-Ordering Interactions

### Parallel Structure Effects

Similar ordering principles across slots create **systematic parallels**:

**Scope-based ordering** (broader scope first):
- Slot 0: Knowledge source > Speech act > Social context > Discourse
- Slot 1: Time > Aspect > Attitude > Polarity  
- Slot 2: Grammar > Semantics > Quantity > Degree > Focus

**Processing efficiency**: Each slot builds meaning **left-to-right incrementally**.

### Constraint Interaction

Intra-slot ordering can interact with inter-slot constraints:

**Slot 0-1 semantic coherence**:
```
✅ hi mia li whera.    (direct evidence + past - compatible)
✅ ro mia su whera.    (inference + future - compatible)
❌ *hi mia su whera.   (direct evidence + future - incompatible)
```

**Slot 1-2 grammatical coherence**:
```
✅ mia ru na he nowhea whera.     (obligation + object - compatible)
❌ *to si mia whera.              (imperative + subject - redundant)
```

## Complex Intra-Slot Patterns

### Multiple Particles per Category

Some functional categories allow multiple particles:

**Multiple aspects** (when semantically compatible):
```
mia li la pu whera.    (past + progressive + perfective)
1SG PST PROG PFV learn
"I was completely learning." (ongoing but completed process)
```

**Multiple comparisons** (contrastive contexts):
```
he nowhea mo riphe mi le misha ta phera.
HUM person CMPR important CNTR LESS beautiful PRS be
"The person is more important but less beautiful."
```

### Semantic Restrictions

Not all particle combinations within slots are allowed:

**Contradictory aspects**:
```
❌ *mia wi wu whera.   (inceptive + cessative)
    (Cannot start and stop simultaneously)

❌ *mia pu ri whera.   (perfective + imperfective)
    (Contradictory completion aspects)
```

**Redundant case marking**:
```
❌ *si na mia whera.   (subject + object on same noun)
    (Cannot be both subject and object)
```

## Learning and Processing Implications

### Acquisition Sequence

**Stage 1**: Master basic intra-slot ordering for each slot individually
**Stage 2**: Learn semantic restrictions within slots  
**Stage 3**: Integrate multi-slot constructions with proper intra-slot ordering

### Processing Advantages

- **Predictable structure**: Each slot has fixed internal logic
- **Incremental interpretation**: Meaning builds left-to-right within slots
- **Error detection**: Violations are immediately recognizable
- **Memory efficiency**: Systematic patterns reduce cognitive load

---

**Navigation:**
- *Previous: [8.2 Inter-Slot Constraints](2-inter-slot-constraints.md)*
- *Up: [Section 8: Particle Ordering Rules](1-overview.md)*
- *Next: [8.4 Constraint Violations and Repairs](4-constraint-violations-and-repairs.md)* 