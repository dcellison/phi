# Section 8: Particle Ordering Rules

## Overview

Particle ordering rules form the backbone of phi's grammatical system, establishing **systematic constraints and preferences** for how the language's 42 particles are organized across three hierarchical slots. These rules ensure that particle combinations are both grammatically correct and communicatively effective.

## Core Function

**Particle ordering** answers the essential question: *In what sequence should particles appear to create well-formed, interpretable utterances?*

- **Structural constraints**: What orderings are grammatically required?
- **Semantic dependencies**: Which particles must co-occur or are mutually exclusive?
- **Processing preferences**: What orderings are easier to parse and produce?
- **Stylistic variations**: How do register and context affect ordering choices?

## The Complete Three-Slot Architecture

Phi's particle system operates through **strict hierarchical ordering** across three major slots:

| Slot | Level | Particle Count | Scope | Core Function |
|------|--------|----------------|-------|---------------|
| **Slot 0** | Sentence Frame | 13 particles | Entire clause | Communicative context |
| **Slot 1** | Verb Phrase | 14 particles | Predicate phrase | Temporal-modal context |
| **Slot 2** | Core Word | 15 particles | Individual words | Grammatical relationships |

### Fundamental Ordering Principle

**Slot 0 > Slot 1 > Slot 2 > Lexical Word**

```
[Slot 0] [Slot 1] [Slot 2] [WORD] [Slot 1] [Slot 2] [WORD] ...
```

This creates a consistent left-to-right flow from broadest to narrowest scope.

## Constraint Types

### 1. Absolute Constraints (Unviolatable)

**Inter-slot ordering**: Slot 0 always precedes Slot 1, which always precedes Slot 2
```
✅ so hi mia li me na he ma nowhea ta whera.
    [0] [0] [2] [1] [1] [2] [2] [2] WORD [1] VERB
    "I politely did not learn from *the* person." (direct evidence)

❌ *mia so hi li me na he ma nowhea ta whera.
    [2] [0] [0] [1] [1] [2] [2] [2] WORD [1] VERB
    (Slot 2 before Slot 0 = ungrammatical)
```

**Particle-word adjacency**: Slot 2 particles must immediately precede their words
```
✅ na he ma nowhea    (Slot 2 particles + word)
❌ *na he nowhea ma   (word interrupting Slot 2 sequence)
```

### 2. Strong Preferences (Violatable under marked conditions)

**Intra-slot ordering**: Fixed sequences within each slot
```
Slot 0: Evidentiality > Sentence Type > Politeness > Discourse
Slot 1: Tense > Aspect > Mood > Negation  
Slot 2: Case > Animacy > Number > Comparison > Emphasis
```

**Semantic coherence**: Related particles tend to cluster
```
✅ hi so mia ta la whera.
    "I am politely learning." (evidence + politeness cluster)

? so hi mia ta la whera.  
    (grammatical but less preferred ordering)
```

### 3. Stylistic Preferences (Context-dependent)

**Register formality**: More particles in formal contexts
```
Formal:   so hi si mia ta la na he ma nowhea te whera.
Informal: mia ta la na he nowhea whera.
```

**Information structure**: Emphasis and topic particles affected by discourse needs
```
Topic-prominent:    ha mia ta whera.
Subject-prominent:  ma mia ta whera.
```

## Cross-Linguistic Perspective

### Universal Patterns
Phi's ordering system reflects cross-linguistic tendencies:
- **Scope hierarchy**: Broader scope elements appear earlier
- **Head-final tendency**: Modifiers precede heads
- **Processing efficiency**: Predictable left-to-right parsing

### Innovative Features
- **Three-slot rigidity**: Unlike natural language flexibility
- **Systematic intra-slot ordering**: Eliminates free variation
- **Scope transparency**: Clear semantic-syntactic mapping
- **Learner accessibility**: Predictable rules reduce complexity

## Processing and Acquisition

### Cognitive Advantages
1. **Predictable parsing**: Fixed slot order enables efficient processing
2. **Incremental interpretation**: Earlier particles set context for later ones
3. **Error detection**: Violations are immediately recognizable
4. **Memory management**: Hierarchical structure reduces cognitive load

### Learning Progression
**Beginner**: Master basic Slot 0 > Slot 1 > Slot 2 ordering
**Intermediate**: Learn intra-slot sequences and preferences
**Advanced**: Handle complex multi-slot constructions and stylistic variation

## Violation Types and Repairs

### Common Violations
1. **Slot reversal**: Placing later slots before earlier ones
2. **Intra-slot scrambling**: Mixing particle order within slots
3. **Particle-word separation**: Breaking Slot 2 adjacency
4. **Semantic conflicts**: Incompatible particle combinations

### Repair Strategies
- **Reordering**: Move particles to correct positions
- **Deletion**: Remove conflicting or redundant particles
- **Substitution**: Replace inappropriate particles
- **Context adjustment**: Change discourse context to license marked orders

## Section Organization

This section explores each aspect of particle ordering in detail:

### 8.2 Inter-Slot Constraints
The fundamental rules governing relationships between Slot 0, Slot 1, and Slot 2, including scope interactions and dependency patterns.

### 8.3 Intra-Slot Ordering
The systematic ordering principles within each slot, covering the specific sequences required for each particle category.

### 8.4 Constraint Violations and Repairs
Analysis of ordering violations, their interpretive consequences, and systematic repair strategies for achieving grammaticality.

### 8.5 Style and Register Effects
How formal vs. informal contexts, discourse goals, and register requirements influence particle ordering choices and preferences.

---

**Navigation:**
- *Previous: [Section 7: Slot 2 Particles](../7-slot-2-core-word-particles/1-overview.md)*
- *Up: [Part 2: Three-Slot System](../README.md)*
- *Next: [8.2 Inter-Slot Constraints](2-inter-slot-constraints.md)* 