# Advanced Patterns and Nesting

This section explores complex structures: nested embeddings, interactions between complementizer types, complementizers inside relative clauses, and multi-level constructions. These patterns are less common in everyday speech but essential for expressing sophisticated thoughts.

## Nested declarative clauses

When we think about what others think, or know what others know, we nest `mena`/`meno` clauses:

### Two levels

```
mia mena thia mena shia to wepu meno phaelo meno shelomui
1SG DECL 2SG DECL 3SG PST leave DECL.CLOSE feel DECL.CLOSE understand
(I understand that you feel that they left.)
```

Structure:
```
mia mena [thia mena [shia to wepu] meno phaelo] meno shelomui
    └────────────────────────────────────────────┘
              └─────────────────────┘
```

Each `mena` has its own `meno`. They nest like parentheses.

### Three levels

```
shia mena mia mena thia mena melu to wepu meno sano meno nohero meno haolu
3SG DECL 1SG DECL 2SG DECL friend PST leave DECL.CLOSE know DECL.CLOSE believe DECL.CLOSE say
(They said that I believe that you know that the friend left.)
```

This is grammatically correct but approaches the limit of comfortable processing. In practice, speakers break complex nestings into separate sentences:

```
melu to wepu. thia shewo mena melu to wepu meno sano. mia mena thia sano meno nohero. shia mena mia nohero meno haolu
friend PST leave. 2SG true DECL friend PST leave DECL.CLOSE know. 1SG DECL 2SG know DECL.CLOSE believe. 3SG DECL 1SG believe DECL.CLOSE say
(The friend left. You truly know that the friend left. I believe that you know. They said that I believe.)
```

Both express the same meaning; the second is easier to follow.

## Nested interrogative clauses

Wondering about wondering:

```
mia wela thia wela shia so turema welo phaelo welo remo
1SG INT.COMP 2SG INT.COMP 3SG FUT return INT.COMP.CLOSE wonder INT.COMP.CLOSE think
(I'm thinking about whether you wonder whether they will return.)
```

Each `wela` pairs with its own `welo`.

## Mixing complementizer types

Different complementizer types can nest within each other:

### Declarative inside interrogative

```
mia wela thia mena shia to wepu meno sano welo phaelo
1SG INT.COMP 2SG DECL 3SG PST leave DECL.CLOSE know INT.COMP.CLOSE wonder
(I wonder whether you know that they left.)
```

Structure:
```
mia wela [thia mena [shia to wepu] meno sano] welo phaelo
    └───────────────────────────────────────────────┘
              └──────────────────────┘
```

The `mena`/`meno` pair is inside the `wela`/`welo` pair.

### Interrogative inside declarative

```
mia mena thia wela shia to wepu welo phaelo meno sano
1SG DECL 2SG INT.COMP 3SG PST leave INT.COMP.CLOSE wonder DECL.CLOSE know
(I know that you wonder whether they left.)
```

### Quotative inside declarative

```
mia mena shia shola mia so turema sholo haolu meno shelomui
1SG DECL 3SG QUOT 1SG FUT return QUOT.CLOSE say DECL.CLOSE understand
(I understand that they said: "I will return.")
```

### Declarative inside quotative

```
shia shola mia mena thia towe nai meno sano sholo haolu
3SG QUOT 1SG DECL 2SG well be DECL.CLOSE know QUOT.CLOSE say
(They said: "I know that you are well.")
```

## Relative clauses containing complementizers

Relative clauses (`rena`) can contain embedded clauses:

### Relative clause with `mena`/`meno`

```
rena mia mena shia towe nai meno sano miona
REL 1SG DECL 3SG well be DECL.CLOSE know person
(the person whom I know is well)
```

Here, the relative clause contains an embedded declarative. The structure:
```
[rena mia mena [shia towe nai] meno sano] miona
```

The head noun `miona` closes the relative clause. The `mena`/`meno` pair is fully contained within it.

### Relative clause with `wela`/`welo`

```
rena thia wela towe nai welo phaelo miona
REL 2SG INT.COMP well be INT.COMP.CLOSE wonder person
(the person about whom you wonder whether (they are) well)
```

### Relative clause with `shola`/`sholo`

```
rena shola mia so turema sholo haolu miona
REL QUOT 1SG FUT return QUOT.CLOSE say person
(the person who said: "I will return")
```

## Complementizers containing relative clauses

The embedded clause can itself contain a relative clause:

### `mena`/`meno` containing relative clause

```
mia mena rena nophi kealo miona to wepu meno sano
1SG DECL REL story create person PST leave DECL.CLOSE know
(I know that the person who creates stories left.)
```

Structure:
```
mia mena [[rena nophi kealo] miona to wepu] meno sano
```

The relative clause `rena nophi kealo` modifies `miona`, and the whole noun phrase is subject of the embedded clause.

### `wela`/`welo` containing relative clause

```
mia wela rena mia to nila shelu shewo nai welo phaelo
1SG INT.COMP REL 1SG PST see book true be INT.COMP.CLOSE wonder
(I wonder whether the book that I saw is true.)
```

### `shola`/`sholo` containing relative clause

```
shia shola rena mia kealo nophi phelora nai sholo haolu
3SG QUOT REL 1SG create story beautiful be QUOT.CLOSE say
(They said: "The story that I created is beautiful.")
```

## Multiple embeddings at the same level

A sentence can contain multiple embedded clauses that are not nested:

### Coordinated embedded clauses

```
mia mena shia towe nai meno sano. nai mia mena shia so turema meno nohero
1SG DECL 3SG well be DECL.CLOSE know. and 1SG DECL 3SG FUT return DECL.CLOSE believe
(I know that they are well, and I believe that they will return.)
```

### Different embedding types in sequence

```
mia mena shia towe nai meno sano. ta mia wela shia so turema welo ma sano
1SG DECL 3SG well be DECL.CLOSE know. but 1SG INT.COMP 3SG FUT return INT.COMP.CLOSE NEG know
(I know that they are well. But I don't know whether they will return.)
```

## Embedded clauses as subjects

Embedded clauses can serve as the subject of a main clause:

```
mena shia to wepu meno shewo nai
DECL 3SG PST leave DECL.CLOSE true be
(That they left is true.)
```

The embedded clause `mena shia to wepu meno` functions as subject of `shewo nai`.

```
wela shia so turema welo ma shewo nai
INT.COMP 3SG FUT return INT.COMP.CLOSE NEG clear be
(Whether they will return is unclear.)
```

## Embedded clauses with topic-comment structure

Phi can topicalize embedded content:

```
mena shia to wepu meno ko. mia shelomui
DECL 3SG PST leave DECL.CLOSE FOC. 1SG understand
(As for that they left: I understand.)
```

The embedded clause is fronted and focused, then commented upon.

## Processing strategies for complex structures

When encountering or producing complex nested structures:

### For comprehension:

1. **Track openers:** Each time you hear `mena`, `wela`, or `shola`, note that a clause has opened.

2. **Match closers:** Each `meno`, `welo`, or `sholo` closes the most recent unmatched opener of the same type.

3. **Find the main verb:** The verb after the outermost closer is the main verb.

4. **Build meaning from inside out:** Understand the innermost clause first, then see how it functions in the next level out.

### For production:

1. **Start with meaning:** What do you ultimately want to say?

2. **Identify the levels:** What is embedded inside what?

3. **Open in order:** Start with the outermost structure, open each level as you reach it.

4. **Close in reverse order:** The last opened clause is the first closed.

5. **Verify matching:** Count that each opener has its closer.

### Simplification strategies:

When a structure becomes too complex:

1. **Break into sentences:** Express each level as a separate sentence.

2. **Use anaphora:** Refer back to established information with pronouns.

3. **Reorder for clarity:** Sometimes a different organization is clearer.

## Limits of nesting

Grammatically, Phi places no limit on nesting depth. Practically, human processing limits apply:

**Comfortable:** 1-2 levels of embedding
**Challenging:** 3 levels
**Difficult:** 4+ levels

Beyond two levels, consider restructuring. The grammar supports complexity, but communication serves understanding.

## Examples of maximal complexity

For the ambitious learner, here are grammatically correct but demanding examples:

### Three-level mixed nesting

```
mia mena thia wela shia mena melu so turema meno sano welo phaelo meno shelomui
1SG DECL 2SG INT.COMP 3SG DECL friend FUT return DECL.CLOSE know INT.COMP.CLOSE wonder DECL.CLOSE understand
(I understand that you wonder whether they know that the friend will return.)
```

### Relative clause with nested embedding

```
rena mia mena thia mena shia towe nai meno phaelo meno sano miona
REL 1SG DECL 2SG DECL 3SG well be DECL.CLOSE feel DECL.CLOSE know person
(the person about whom I know that you feel that they are well)
```

### Quotation of complex content

```
shia shola mia mena melu so turema meno nohero sholo haolu
3SG QUOT 1SG DECL friend FUT return DECL.CLOSE believe QUOT.CLOSE say
(They said: "I believe that the friend will return.")
```

## Summary

Advanced patterns demonstrate the power and regularity of Phi's complementizer system:

- **Nesting is unlimited:** Each opener pairs with its closer, regardless of depth.
- **Types can mix:** Declarative, interrogative, and quotative can nest within each other.
- **Relative clauses interact cleanly:** They can contain complementizers or be contained by them.
- **Structure remains parseable:** The opener-closer matching ensures unambiguous interpretation.

In practice, prioritize clarity over complexity. The system supports whatever depth meaning requires, but simpler expression usually serves communication better.

---

*Next: Common Errors and How to Avoid Them*
