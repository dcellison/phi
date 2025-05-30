# Inter-Slot Constraints

## The Fundamental Architecture

Inter-slot constraints form the core architectural rules of phi's particle system, establishing **inviolable relationships** between the three hierarchical slots. These constraints ensure that particles maintain their proper scope relationships and create interpretable utterances.

## Primary Ordering Constraint

### The Slot Hierarchy Rule

**Slot 0 > Slot 1 > Slot 2 > Lexical Word**

This is phi's most fundamental constraint: particles from higher-numbered slots NEVER precede particles from lower-numbered slots within the same structural domain.

```
✅ Correct ordering:
so hi mia li la me na he ma nowhea ta whera.
[0] [0] [2] [1] [1] [1] [2] [2] [2] WORD [1] VERB

❌ Slot order violation:
*mia so hi ta whera.
[2] [0] [0] [1] VERB
(Slot 2 before Slot 0 is ungrammatical)
```

### Structural Domains

The slot hierarchy applies within **structural domains** - typically clauses and major phrases:

**Single clause domain**:
```
hi mia li me na he nowhea ta whera.
DIR 1SG PST NEG OBJ HUM person PRS learn
"I did not learn from the person." (I see this directly)
```

**Multi-clause domains** (each clause has independent slot ordering):
```
hi mia ta whera mi ro sha su whema.
DIR 1SG PRS learn CNTR INF 3SG FUT work
"I learn (I see this) but s/he will work (I infer)."
```

## Scope-Based Interactions

### Semantic Scope Principles

Particles in earlier slots have **broader semantic scope** than particles in later slots:

**Slot 0 scopes over entire propositions**:
```
wa [mia ta whera].
Q [1SG PRS learn]
"Do I learn?" (question scopes over entire proposition)
```

**Slot 1 scopes over verb phrases**:
```
mia [li me whera].
1SG [PST NEG learn]
"I [did not learn]." (negation scopes over past learning)
```

**Slot 2 scopes over individual words**:
```
mia ta na [he ma nowhea] whera.
1SG PRS OBJ [HUM EMPH person] learn
"I learn from [*the* person]." (emphasis scopes over person)
```

### Scope Interaction Effects

Different slots can interact to create complex meanings:

**Evidentiality + Negation**:
```
hi mia me whera.        (DIR + NEG)
DIR 1SG NEG learn
"I don't learn." (I directly observe that I don't learn)

me hi mia whera.        (NEG + DIR - marked order)
NEG DIR 1SG learn
"It's not the case that I directly observe learning."
```

**Question + Politeness**:
```
so wa mia ta whera.     (POL + Q)
POL Q 1SG PRS learn
"May I ask - do I learn?" (polite question)

wa so mia ta whera.     (Q + POL - less natural)
Q POL 1SG PRS learn
"Do I politely learn?" (questioning politeness)
```

## Cross-Slot Dependencies

### Required Co-occurrence

Some particles across slots must or preferentially co-occur:

**Evidentiality + Tense interactions**:
```
✅ hi mia ta whera.     (direct evidence with present)
    "I learn." (I see this now)

✅ mu mia li whera.     (memory evidence with past)
    "I learned." (I remember this)

? hi mia li whera.      (direct evidence with past - marked)
    "I learned." (I directly see past events - unusual)
```

**Politeness + Imperative patterns**:
```
✅ so to whera.         (politeness with imperative)
    "Please learn."

❌ *to so whera.        (imperative before politeness)
    (violates slot ordering)
```

### Mutual Exclusions

Some particles across slots cannot co-occur due to semantic incompatibility:

**Contradictory evidentials and sentence types**:
```
❌ *wa hi mia ta whera. (question + direct evidence)
    (Cannot directly observe the answer to your own question)

❌ *to pe mia whera.    (imperative + hearsay)
    (Cannot command based on second-hand information)
```

**Temporal incompatibilities**:
```
❌ *hi mia su whera.    (direct evidence + future)
    (Cannot directly observe future events)

✅ ro mia su whera.     (inference + future)
    "I will learn." (I infer this about the future)
```

## Adjacency Constraints

### Slot 2 Word Adjacency

**Absolute requirement**: Slot 2 particles must immediately precede their target words.

```
✅ mia ta na he ma nowhea whera.
    "I learn from *the* person."

❌ *mia ta na he ma ta whera nowhea.
    (word separating Slot 2 particles from target)
```

### Slot 0-1 Flexibility

Slot 0 and Slot 1 particles can be separated by subjects and other elements:

```
✅ hi mia li whera.     (Slot 0-Subject-Slot 1)
✅ hi si mia li whera.  (Slot 0-Case-Subject-Slot 1)
```

But the relative ordering within domains must be maintained:

```
❌ *mia hi li whera.    (Subject between Slot 0 particles)
```

## Complex Multi-Slot Patterns

### Full Slot Integration

All three slots working together systematically:

```
so hi mia li la me na he lo ma nowhea te whera.
POL DIR 1SG PST PROG NEG OBJ HUM PL EMPH person VRB learn

"I was politely not learning from *the* people." (I see this directly)

Slot 0: so hi    (politeness + direct evidence)
Slot 1: li la me (past + progressive + negation)  
Slot 2: na he lo ma (object + human + plural + emphasis)
```

---

**Navigation:**
- *Previous: [8.1 Overview](1-overview.md)*
- *Up: [Section 8: Particle Ordering Rules](1-overview.md)*
- *Next: [8.3 Intra-Slot Ordering](3-intra-slot-ordering.md)* 