# Part 2: The mechanics of `rena`

## The word itself

The relativizer `rena` announces that what follows is a descriptive clause. It's a complementizer, not a pronoun. This distinction matters: `rena` doesn't stand in for the noun or change form based on grammatical role. It simply marks the beginning of a relative clause.

### Sound symbolism

The rolling `r` links and the grounding nasal `na` anchors: `rena` opens a descriptive space and holds it until the head noun arrives to close it.

### Gloss and category

In linguistic glosses, `rena` is abbreviated as **REL** (relativizer). It belongs to the complementizer category alongside:

- `mena`/`meno` (DECL.COMP/DECL.COMP.CLOSE): introduces embedded statements
- `shola`/`sholo` (QUOT.COMP/QUOT.COMP.CLOSE): introduces direct quotation
- `wela`/`welo` (INT.COMP/INT.COMP.CLOSE): introduces embedded questions

All complementizers announce what kind of clause is coming. `rena` specifically announces: "a descriptive clause follows; wait for the noun to learn what it describes."

## Position and scope

### Where `rena` appears

`rena` always appears at the very beginning of the relative clause:

```
[rena ...clause... ] NOUN
```

There are no exceptions. Unlike English, where relative pronouns can sometimes be omitted ("the book I read" vs. "the book that I read"), `rena` is consistently present when a relative clause is explicitly marked.

### What counts as "the clause"

Everything between `rena` and the head noun is part of the relative clause. This includes:

- The subject (if not gapped)
- The object (if not gapped)
- Tense and aspect particles
- Negation
- Adverbials and prepositional phrases
- Even embedded clauses within the relative clause

The scope of `rena` extends until the head noun appears. That noun closes the relative clause and receives all the preceding description.

### The structural formula

```
[rena CLAUSE] NOUN MAIN-CLAUSE
```

Or more precisely:

```
[rena (subject) (object) (adverbials) VERB] NOUN (rest of sentence)
```

The noun can then serve any role in the main clause: subject, object, or part of a prepositional phrase.

## No closer needed

### Comparison with other complementizers

Phi's other clause-embedding complementizers require closers:

- `mena` ... `meno` (DECL.COMP ... DECL.COMP.CLOSE): required pair for embedded statements
- `wela` ... `welo` (INT.COMP ... INT.COMP.CLOSE): required pair for embedded questions
- `shola` ... `sholo` (QUOT.COMP ... QUOT.COMP.CLOSE): required pair for quotations

These closers exist because the embedded clause is followed by more material (the main verb), and without a boundary marker, the listener wouldn't know where the embedded clause ends.

But `rena` has no closer. Why not?

### Pre-nominal position creates natural bounding

The answer lies in position. Embedded statements with `mena` are followed by the main verb:

```
mia mena shia to wepu meno sano
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE know
(i know that they went.)
```

Without `meno`, the sentence would be ambiguous: where does the embedded clause end? Which verb belongs to which clause?

Relative clauses with `rena` are followed by a noun:

```
rena shia to kealo nophi phelora nai
REL 3SG PST create story beautiful be
(the story that they created is beautiful.)
```

The noun `nophi` ("story") itself signals that the relative clause has ended. Not every noun does this: a noun inside the clause is one of the clause's own arguments, as in `rena nophi kealo miona` (the person who creates stories), where `nophi` is the clause's object. The head is the noun that arrives after the clause is complete, the first noun after the clause's verb. That noun IS the closer.

This is the advantage of pre-nominal relatives: they're self-delimiting. The structure has a built-in endpoint.

### When the noun arrives

Train yourself to listen for the noun as a signal:

1. You hear `rena`: a description is starting
2. You hear clause material: subjects, objects, particles, the verb
3. You hear a noun after the clause's verb: the description is complete
4. That noun is what was being described

## The gap strategy

### What is a gap?

In a relative clause, the head noun plays a role inside the clause's action. In "the book that I read," the book is what was read; in "the person who helped me," the person is the helper.

But the noun itself appears outside the clause, at the end. Inside the clause, there's a gap: an empty position where the noun would be if it were a normal sentence.

### Gap in subject position

When the head noun is the subject of the relative clause's action:

```
rena ___ nophi kealo miona phue nai
REL [gap] story create person wise be
(the person who creates stories is wise.)
```

Analysis:
- The gap is in subject position (before the object and verb)
- The person is the one who creates stories
- If this were a standalone sentence: "miona nophi kealo" (a person creates stories)
- In the relative clause, `miona` moves to the end, leaving a gap

More examples:

```
rena ___ to shua miona ha nai
REL [gap] PST come person PROX be
(the person who came is here.)
```

```
rena ___ phelora nai peloru thuroa
REL [gap] beautiful be flower grow
(the flower that is beautiful grows.)
```

### Gap in object position

When the head noun is the object of the relative clause's action:

```
mia rena mia ___ to nila shelu lothea
1SG REL 1SG [gap] PST see book love
(i love the book that i saw.)
```

Analysis:
- The gap is in object position (after subject, before tense+verb)
- The book is what was seen
- If this were a standalone sentence: "mia shelu to nila" (i saw a book)
- In the relative clause, `shelu` moves to the end, leaving a gap where the object was

More examples:

```
rena thia ___ to kealo nophi phelora nai
REL 2SG [gap] PST create story beautiful be
(the story that you created is beautiful.)
```

```
mia rena shia ___ thumela lopia sano
1SG REL 3SG [gap] teach child know
(i know the child whom they teach.)
```

### Gap in oblique position

When the head noun is part of a prepositional phrase inside the relative clause:

```
rena mia mua ___ to thalo shelira phelora nai
REL 1SG LOC [gap] PST walk forest beautiful be
(the forest that i walked in is beautiful.)
```

Analysis:
- The gap is inside the locative phrase, where the object of `mua` would be
- The forest is where the walking happened
- The preposition `mua` (in/at) remains; its object is gapped

More examples:

```
rena shia wei ___ to haolu miona ha nai
REL 3SG DAT [gap] PST speak person PROX be
(the person whom they spoke to is here.)
```

### No case marking

In languages like English, different relative pronouns indicate different roles: "who" vs. "whom," "which" vs. "whose." Phi doesn't do this. `rena` is invariant. The gap's position tells you the role.

This keeps the system simple but requires attention to structure. When you hear or read a relative clause, notice where something seems to be missing. That's the gap, and it tells you how the head noun relates to the clause's action.

### Identifying the gap: practice

For each relative clause, ask: "If I turned this into a standalone sentence with the head noun inside, where would it go?"

```
rena shia lothea miona
```
→ "shia miona lothea" (they love a person)
→ gap is in object position
→ "the person whom they love"

```
rena to shua miona
```
→ "miona to shua" (a person came)
→ gap is in subject position
→ "the person who came"

```
rena mia mua shelira to nila ruela
```
→ "mia mua shelira ruela to nila" (i saw a path in the forest)
→ gap is in... wait, which noun is the head?

This last example shows that you must wait for the head noun to know what's gapped. The word `ruela` (path) at the end is the head, so the path is what was seen. The forest (`shelira`) is inside the clause, not gapped.

The rule of thumb: find the clause's verb, take the noun after it as the head, and ask which role inside the clause is empty.
