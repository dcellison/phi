# Temporal-Modal Integration

## Complex Temporal-Modal Architecture

The integration of **temporal and modal systems** creates phi's most sophisticated expressive capabilities. Through systematic interactions between tense, aspect, mood, and negation particles, speakers can express complex temporal-modal relationships that capture nuanced speaker attitudes across time frames.

## Modal Particles in Temporal Context

### Core Modal Particles

| Particle | Function | Modal Type | Temporal Interaction | Example |
|----------|----------|------------|---------------------|---------|
| `to` | Imperative | Command | Present/future oriented | `to whera` "Learn!" |
| `ru` | Obligation | Necessity | All temporal frames | `mia ru whera` "I should learn" |
| `we` | Desiderative | Volition | All temporal frames | `mia we whera` "I want to learn" |
| `me` | Negation | Polarity reversal | All temporal frames | `mia me whera` "I don't learn" |

### Slot 1 Ordering Architecture

**Tense > Aspect > Mood > Negation**

```
mia li la ru me whera
1SG PST PROG OBLG NEG learn
"I was not supposed to be learning."

Slot breakdown:
li (tense: past)
la (aspect: progressive) 
ru (mood: obligation)
me (negation)
```

## Temporal-Obligation Integration

### Obligation Across Time Frames

**Past obligation** - actions that should have occurred:
```
mia li ru whera.
1SG PST OBLG learn
"I should have learned." (past obligation not fulfilled)

mia li ru me whera.
1SG PST OBLG NEG learn
"I should not have learned." (past prohibition)
```

**Present obligation** - current duties and requirements:
```
mia ta ru whera.
1SG PRS OBLG learn
"I should learn." (current obligation)

mia ta ru la whera.
1SG PRS OBLG PROG learn
"I should be learning." (current progressive obligation)
```

**Future obligation** - upcoming necessities:
```
mia su ru whera.
1SG FUT OBLG learn
"I will need to learn." (future necessity)

mia su ru ni whera.
1SG FUT OBLG PRF learn
"I will need to have learned." (future perfect obligation)
```

### Aspectual-Modal Combinations

**Obligation with different aspects**:

**Habitual obligation**:
```
mia ru po whera.
1SG OBLG HAB learn
"I should usually learn." (regular obligation)
```

**Perfect obligation**:
```
mia ru ni whera.
1SG OBLG PRF learn
"I should have learned." (obligation for completion)
```

**Progressive obligation**:
```
mia ru la whera.
1SG OBLG PROG learn
"I should be learning." (obligation for ongoing action)
```

## Temporal-Desiderative Integration

### Volition Across Time Frames

**Past desires** - what was wanted:
```
mia li we whera.
1SG PST DES learn
"I wanted to learn." (past desire)

mia li we na he nowhea whelu.
1SG PST DES OBJ HUM person love
"I wanted to love the person." (past romantic desire)
```

**Present desires** - current wants:
```
mia ta we whera.
1SG PRS DES learn
"I want to learn." (current desire)

mia ta we la whera.
1SG PRS DES PROG learn
"I want to be learning." (desire for ongoing action)
```

**Future desires** - projected wants:
```
mia su we whera.
1SG FUT DES learn
"I will want to learn." (future desire)
```

### Complex Desiderative-Aspectual Patterns

**Desiderative + inceptive**:
```
mia we wi whera.
1SG DES INCEP learn
"I want to start learning." (desire for initiation)
```

**Desiderative + cessative**:
```
mia we wu whera.
1SG DES CESS learn
"I want to finish learning." (desire for completion)
```

**Desiderative + perfect**:
```
mia we ni whera.
1SG DES PRF learn
"I want to have learned." (desire for completed state)
```

## Temporal-Negation Integration

### Negation Scope Across Time

**Past negation** - actions that didn't occur:
```
mia li me whera.
1SG PST NEG learn
"I didn't learn." (past negative action)

mia li me la whera.
1SG PST NEG PROG learn
"I wasn't learning." (past negative progressive)
```

**Present negation** - current non-occurrence:
```
mia ta me whera.
1SG PRS NEG learn
"I don't learn." (present negative)

mia ta me po whera.
1SG PRS NEG HAB learn
"I don't usually learn." (negative habitual)
```

**Future negation** - projected non-occurrence:
```
mia su me whera.
1SG FUT NEG learn
"I won't learn." (future negative)
```

### Complex Negation Patterns

**Negation with modal + aspectual combinations**:

**Negative obligation + aspect**:
```
mia ru me la whera.
1SG OBLG NEG PROG learn
"I should not be learning." (obligation against progressive action)

mia me ru whera.
1SG NEG OBLG learn
"I don't have to learn." (no obligation)
```

**Negative desiderative**:
```
mia me we whera.
1SG NEG DES learn
"I don't want to learn." (lack of desire)

mia we me whera.
1SG DES NEG learn
"I want not to learn." (desire for non-action)
```

## Temporal-Evidential Integration

### Evidence-Time Compatibility

**Compatible evidential-temporal combinations**:

**Memory + Past** (natural combination):
```
mu mia li whera.
MEM 1SG PST learn
"I learned." (I remember past learning)

mu mia li po whera.
MEM 1SG PST HAB learn
"I used to learn." (I remember past habits)
```

**Direct + Present** (immediate observation):
```
hi mia ta whera.
DIR 1SG PRS learn
"I learn." (I directly observe current learning)

hi mia ta la whera.
DIR 1SG PRS PROG learn
"I am learning." (I directly observe ongoing action)
```

**Inference + Future** (projected reasoning):
```
ro mia su whera.
INF 1SG FUT learn
"I will learn." (I infer future learning)

ro mia su ru whera.
INF 1SG FUT OBLG learn
"I will need to learn." (I infer future obligation)
```

### Problematic Evidential-Temporal Combinations

**Direct evidential + future** (cannot observe future):
```
❌ *hi mia su whera.
    DIR 1SG FUT learn
    (Cannot directly observe future events)
```

**Memory evidential + present** (memories are past):
```
? mu mia ta whera.
  MEM 1SG PRS learn
  "I learn." (remembering present - marked)
```

## Complex Multi-System Integration

### Full Temporal-Modal-Evidential Integration

**Academic precision contexts**:
```
so ro mia li ru la ni na he lo ma ruphea te whera.
POL INF 1SG PST OBLG PROG PRF OBJ HUM PL EMPH information VRB learn

"I should have been progressively learning from *the* information." 
(polite, inferential, past obligation, progressive, perfect, emphasis)

Breakdown:
Slot 0: so (politeness) + ro (inference)
Slot 1: li (past) + ru (obligation) + la (progressive)  
Slot 2: ni (perfect) + na (object) + he (human) + lo (plural) + ma (emphasis)
```

**Conversational efficiency**:
```
mia me li whera.
1SG NEG PST learn
"I didn't learn." (minimal temporal-modal marking)
```

## Temporal-Modal Discourse Effects

### Register Variation

**Formal contexts** use explicit temporal-modal marking:
```
so ke mia li ru ni na he ma riphe nowhea te whera.
POL KNOW 1SG PST OBLG PRF OBJ HUM EMPH important person VRB learn
"I should have learned from the *important* person." (formal, explicit)
```

**Casual contexts** reduce temporal-modal complexity:
```
mia ru whera.
1SG OBLG learn  
"I should learn." (casual, simplified)
```

### Narrative Temporal-Modal Progression

**Story sequences with modal development**:
```
Narrative progression:
mia li we whera.         (past desire)
1SG PST DES learn
"I wanted to learn."

mia li ru whera.         (past obligation)
1SG PST OBLG learn  
"I should have learned."

mia li me whera.         (past negative)
1SG PST NEG learn
"I didn't learn."

mia ta ru whera.         (present obligation)
1SG PRS OBLG learn
"I should learn."
```

## Processing and Acquisition

### Cognitive Processing Advantages

**Systematic scope ordering**: Each particle type has predictable scope relationships
**Incremental interpretation**: Left-to-right processing builds temporal-modal meaning systematically
**Compositional transparency**: Complex meanings arise from predictable particle combinations

### Learning Progression

**Stage 1**: Master basic temporal-modal combinations
- Tense + obligation: `li ru`, `ta ru`, `su ru`
- Tense + negation: `li me`, `ta me`, `su me`

**Stage 2**: Learn aspectual-modal integration
- Aspect + obligation: `po ru`, `la ru`, `ni ru`
- Aspect + desiderative: `wi we`, `wu we`

**Stage 3**: Handle complex multi-system integration
- Full Slot 1 sequences: tense + aspect + mood + negation
- Cross-slot integration with evidentiality and emphasis

**Stage 4**: Develop discourse sensitivity
- Register-appropriate temporal-modal complexity
- Narrative temporal-modal progression patterns

### Common Learning Challenges

**Scope ordering**: Understanding that broader scope particles come first
**Evidential compatibility**: Learning which evidentials work with which temporal references
**Modal distinctions**: Distinguishing obligation, desiderative, and imperative functions
**Negation scope**: Understanding where negation affects meaning in complex constructions

---

**Navigation:**
- *Previous: [10.3 Aspectual System](3-aspectual-system.md)*
- *Up: [Section 10: Tense and Aspect](1-overview.md)*
- *Next: [10.5 Narrative and Discourse Applications](5-narrative-and-discourse-applications.md)* 