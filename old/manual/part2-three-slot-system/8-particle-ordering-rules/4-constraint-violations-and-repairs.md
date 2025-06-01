# Constraint Violations and Repairs

## Understanding Ordering Violations

Ordering violations occur when phi's systematic particle constraints are broken, resulting in **ungrammatical or semantically anomalous constructions**. Understanding these violations and their repair strategies is crucial for mastering phi's particle system and diagnosing errors in production and comprehension.

## Types of Violations

### 1. Inter-Slot Violations

**Slot order reversals**: Higher-numbered slots appearing before lower-numbered slots.

```
❌ Violation: mia na he nowhea so hi ta whera.
   [2] [2] [2] WORD [0] [0] [1] VERB
   (Slot 2 before Slot 0)

✅ Repair: so hi mia na he nowhea ta whera.
   [0] [0] [2] [2] [2] WORD [1] VERB
   "I politely learn from the person." (I see this directly)
```

**Cross-slot separation violations**: Breaking required adjacency patterns.

```
❌ Violation: mia na he ta whera nowhea.
   (Verb separating Slot 2 particles from target word)

✅ Repair: mia na he nowhea ta whera.
   "I learn from the person."
```

### 2. Intra-Slot Violations

**Slot 0 ordering violations**:
```
❌ Violation: wa hi mia ta whera.
   (Sentence type before evidentiality)

✅ Repair: hi wa mia ta whera.
   "Do I learn?" (I can observe the answer)
```

**Slot 1 ordering violations**:
```
❌ Violation: mia me li whera.
   (Negation before tense)

✅ Repair: mia li me whera.
   "I didn't learn."
```

**Slot 2 ordering violations**:
```
❌ Violation: ma mo riphe
   (Emphasis before comparison)

✅ Repair: mo ma riphe
   "*more* important"
```

### 3. Semantic Violations

**Contradictory particle combinations**:
```
❌ Violation: hi mia su whera.
   (Direct evidence + future tense)
   (Cannot directly observe future events)

✅ Repair: ro mia su whera.
   "I will learn." (I infer this)
```

**Redundant or conflicting particles**:
```
❌ Violation: si na mia whera.
   (Subject + object markers on same noun)

✅ Repair: si mia whera. OR na mia whera.
   "I learn." OR "learn from me."
```

## Violation Effects on Interpretation

### Ungrammaticality

Some violations render sentences completely ungrammatical:

```
❌ *mia so hi whera.    (Slot 2 before Slot 0)
   (No possible interpretation)

❌ *wa hi mia ta whera. (Question + direct evidence)
   (Logically contradictory)
```

### Semantic Anomaly

Other violations create interpretable but semantically strange meanings:

```
? me hi mia whera.      (Negation scoping over evidentiality)
  "It's not the case that I directly observe myself learning."
  (Grammatical but pragmatically odd)

? ha mi mia ta whera.   (Topic + contrast with no established topic)
  "As for that, but I learn."
  (Requires specific discourse context)
```

### Processing Difficulty

Some violations are interpretable but increase processing complexity:

```
? so wa hi mia ta whera.  (Non-canonical Slot 0 ordering)
  "May I ask - do I learn?" (I observe this)
  (Interpretable but harder to process than canonical order)
```

## Systematic Repair Strategies

### 1. Reordering Repairs

**Move particles to correct positions** without changing meaning:

```
❌ wa hi → ✅ hi wa   (Evidentiality before sentence type)
❌ me li → ✅ li me   (Tense before negation)
❌ he na → ✅ na he   (Case before animacy)
```

**Complex reordering**:
```
❌ wa so hi mia me li whera.
✅ hi wa so mia li me whera.
   "May I politely ask - didn't I learn?" (I can observe this)
```

### 2. Substitution Repairs

**Replace incompatible particles** with compatible alternatives:

```
❌ hi mia su whera. → ✅ ro mia su whera.
   (Direct → inferential evidence for future)

❌ to pe mia whera. → ✅ to hi mia whera.
   (Hearsay → direct evidence for commands)
```

### 3. Deletion Repairs

**Remove redundant or conflicting particles**:

```
❌ si na mia whera. → ✅ si mia whera.
   (Remove redundant object marker)

❌ hi ro mia ta whera. → ✅ hi mia ta whera.
   (Remove conflicting evidential)
```

### 4. Insertion Repairs

**Add missing particles** to complete required constructions:

```
❌ wa mia ta whera. → ✅ ro wa mia ta whera.
   (Add compatible evidential for questions)

❌ ma nowhea → ✅ he ma nowhea
   (Add required animacy marker)
```

## Common Learner Errors

### Beginner Errors

**Slot order confusion**:
```
❌ Common: mia so whera.        (Politeness after subject)
✅ Correct: so mia whera.       (Politeness in Slot 0)
```

**Missing animacy markers**:
```
❌ Common: mia na nowhea whera. (No animacy marking)
✅ Correct: mia na he nowhea whera. (Human animacy required)
```

### Intermediate Errors

**Intra-slot ordering mistakes**:
```
❌ Common: mia la li whera.     (Aspect before tense)
✅ Correct: mia li la whera.    (Tense before aspect)
```

**Semantic incompatibilities**:
```
❌ Common: hi mia su whera.     (Direct evidence + future)
✅ Correct: ro mia su whera.    (Inferential evidence + future)
```

### Advanced Errors

**Complex multi-slot violations**:
```
❌ Common: wa so hi mia li la me na he ma nowhea te whera.
   (Non-canonical Slot 0 ordering)

✅ Correct: hi wa so mia li la me na he ma nowhea te whera.
   "May I politely ask - was I not learning from *the* person?"
```

## Diagnostic Procedures

### Step-by-Step Error Detection

**1. Check inter-slot ordering**:
- Are all Slot 0 particles before Slot 1?
- Are all Slot 1 particles before Slot 2?
- Are Slot 2 particles adjacent to their words?

**2. Check intra-slot ordering**:
- Slot 0: Evidentiality > Sentence Type > Politeness > Discourse
- Slot 1: Tense > Aspect > Mood > Negation
- Slot 2: Case > Animacy > Number > Comparison > Emphasis

**3. Check semantic compatibility**:
- Do evidentials match temporal reference?
- Are modal and aspectual combinations logical?
- Do particles create coherent meaning?

### Repair Priority

**1. Fix inter-slot violations first** (most disruptive):
```
❌ mia so hi whera → ✅ so hi mia whera
```

**2. Fix intra-slot violations second**:
```
❌ so wa hi mia whera → ✅ hi wa so mia whera
```

**3. Address semantic issues last**:
```
❌ hi wa so mia su whera → ✅ ro wa so mia su whera
```

## Marked Constructions

### Acceptable Violations

Some violations are grammatical in specific discourse contexts:

**Evidential scope marking**:
```
Standard: hi mia me whera.
         "I don't learn." (I directly observe this)

Marked:   me hi mia whera.
         "It's not the case that I directly observe learning."
         (Negation scopes over evidentiality for contrastive focus)
```

**Topic prominence**:
```
Standard: ha mia ta whera.
         "As for that, I learn."

Marked:   mia ha ta whera.
         "I, as for that topic, learn."
         (Topic embedded within clause for specific discourse effect)
```

### Licensing Conditions

Marked constructions require specific **discourse licensing**:
- Contrastive focus
- Corrective emphasis  
- Metalinguistic commentary
- Poetic or rhetorical effect

## Pedagogical Applications

### Teaching Sequence

**1. Establish basic slot ordering** (Slot 0 > Slot 1 > Slot 2)
**2. Teach intra-slot ordering** for each slot individually
**3. Practice violation detection** with simple examples
**4. Learn systematic repair** strategies
**5. Explore marked constructions** in advanced contexts

### Exercise Types

**Ordering exercises**:
```
Given: wa so hi mia whera
Task: Reorder correctly
Answer: hi wa so mia whera
```

**Error correction**:
```
Given: mia la li whera
Error: Aspect before tense
Repair: mia li la whera
```

**Semantic compatibility**:
```
Given: hi mia su whera
Issue: Direct evidence + future
Repair: ro mia su whera
```

---

**Navigation:**
- *Previous: [8.3 Intra-Slot Ordering](3-intra-slot-ordering.md)*
- *Up: [Section 8: Particle Ordering Rules](1-overview.md)*
- *Next: [8.5 Style and Register Effects](5-style-and-register-effects.md)* 