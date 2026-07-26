# Part 2: The mechanics of `whu`

## The word itself

The relativizer `whu` announces that what follows is a descriptive clause. It's a complementizer, not a pronoun. This distinction matters: `whu` doesn't stand in for the noun or change form based on grammatical role. It simply marks the beginning of a relative clause.

### Sound symbolism

Say it aloud: breath through rounded lips, then a vowel that keeps exactly the same rounding, gone almost before it starts. The mouth never changes shape from one end of the word to the other, which is a fair sound for a word that opens something and then waits. `whu` is the only bracket in Phi that never closes, and its vowel is the announcement: the three pairs end in `-a` or `-o`, and this one ends in neither, so no closer is coming. What `whu` opens is held open by grammar rather than by sound, until the head noun arrives to close it.

### Gloss and category

In linguistic glosses, `whu` is abbreviated as **REL** (relativizer). It belongs to the complementizer category alongside:

- `tha`/`tho` (DECL.COMP/DECL.COMP.CLOSE): introduces embedded statements
- `sha`/`sho` (QUOT.COMP/QUOT.COMP.CLOSE): introduces direct quotation
- `pha`/`pho` (INT.COMP/INT.COMP.CLOSE): introduces embedded questions

All complementizers announce what kind of clause is coming. `whu` specifically announces: "a descriptive clause follows; wait for the noun to learn what it describes."

## Position and scope

### Where `whu` appears

`whu` always appears at the very beginning of the relative clause:

```
[whu ...clause... ] NOUN
```

There are no exceptions. Unlike English, where relative pronouns can sometimes be omitted ("the book I read" vs. "the book that I read"), `whu` is consistently present when a relative clause is explicitly marked.

### What counts as "the clause"

Everything between `whu` and the head noun is part of the relative clause. This includes:

- The subject (if not gapped)
- The object (if not gapped)
- Tense and aspect particles
- Negation
- Adverbials and prepositional phrases
- Even embedded clauses within the relative clause

The scope of `whu` extends until the head noun appears. That noun closes the relative clause and receives all the preceding description.

### The structural formula

```
[whu CLAUSE] NOUN MAIN-CLAUSE
```

Or more precisely:

```
[whu (subject) (object) (adverbials) VERB] NOUN (rest of sentence)
```

The noun can then serve any role in the main clause: subject, object, or part of a prepositional phrase.

## No closer needed

### Comparison with other complementizers

Phi's other clause-embedding complementizers require closers:

- `tha` ... `tho` (DECL.COMP ... DECL.COMP.CLOSE): required pair for embedded statements
- `pha` ... `pho` (INT.COMP ... INT.COMP.CLOSE): required pair for embedded questions
- `sha` ... `sho` (QUOT.COMP ... QUOT.COMP.CLOSE): required pair for quotations

These closers exist because the embedded clause is followed by more material (the main verb), and without a boundary marker, the listener wouldn't know where the embedded clause ends.

But `whu` has no closer. Why not?

### Pre-nominal position creates natural bounding

The answer lies in position. Embedded statements with `tha` are followed by the main verb:

```
mia tha shia to wepu tho sano
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE know
(I know that they went.)
```

Without `tho`, the sentence would be ambiguous: where does the embedded clause end? Which verb belongs to which clause?

Relative clauses with `whu` are followed by a noun:

```
whu shia to kealo nophi mioru nai
REL 3SG PST create story beautiful be
(The story that they created is beautiful.)
```

The noun `nophi` ("story") itself signals that the relative clause has ended. Not every noun does this: a noun inside the clause is one of the clause's own arguments, as in `whu nophi kealo miona` (the person who creates stories), where `nophi` is the clause's object. The head is the noun that arrives after the clause is complete, the first noun after the clause's verb. That noun *is* the closer.

This is the advantage of pre-nominal relatives: they're self-delimiting. The structure has a built-in endpoint.

### When the noun arrives

Train yourself to listen for the noun as a signal:

1. You hear `whu`: a description is starting
2. You hear clause material: subjects, objects, particles, the verb
3. You hear a noun after the clause's verb: the description is complete
4. That noun is what was being described

## The gap strategy

### What is a gap?

In a relative clause, the head noun plays a role inside the clause's action. In "the book that I read," the book is what was read; in "the person who helped me," the person is the helper.

But the noun itself appears outside the clause, at the end. Inside the clause, there's a gap: an empty position where the noun would be if it were a normal sentence.

Think of it as a place laid at the table before the guest arrives. The clause sets everything around one empty seat, and the head noun, when it comes, sits down exactly there.

### Gap in subject position

When the head noun is the subject of the relative clause's action:

```
whu ___ nophi kealo miona phue nai
REL [gap] story create person wise be
(The person who creates stories is wise.)
```

Analysis:
- The gap is in subject position (before the object and verb)
- The person is the one who creates stories
- If this were a standalone sentence: "miona nophi kealo" (a person creates stories)
- In the relative clause, the subject's seat stands empty, and `miona` waits outside as the head

More examples:

```
whu ___ to shua miona ha nai
REL [gap] PST come person PROX be
(The person who came is here.)
```

```
whu ___ mioru nai peloru thuroa
REL [gap] beautiful be flower grow
(The flower that is beautiful grows.)
```

### Gap in object position

When the head noun is the object of the relative clause's action:

```
mia whu mia ___ to nila shelu lothea
1SG REL 1SG [gap] PST see book love
(I love the book that I saw.)
```

Analysis:
- The gap is in object position (after subject, before tense+verb)
- The book is what was seen
- If this were a standalone sentence: "mia shelu to nila" (I saw a book)
- In the relative clause, the object's seat stands empty, and `shelu` waits outside as the head

More examples:

```
whu thia ___ to kealo nophi mioru nai
REL 2SG [gap] PST create story beautiful be
(The story that you created is beautiful.)
```

```
mia whu shia ___ thumela lopia sano
1SG REL 3SG [gap] teach child know
(I know the child whom they teach.)
```

### Gap in oblique position

When the head noun is part of a prepositional phrase inside the relative clause:

```
whu mia mua ___ to thalo shelira mioru nai
REL 1SG LOC [gap] PST walk forest beautiful be
(The forest that I walked in is beautiful.)
```

Analysis:
- The gap is inside the locative phrase, where the object of `mua` would be
- The forest is where the walking happened
- The preposition `mua` (in/at) remains; its object is gapped

More examples:

```
whu shia wei ___ to haolu miona ha nai
REL 3SG DAT [gap] PST speak person PROX be
(The person whom they spoke to is here.)
```

### No case marking

In languages like English, different relative pronouns indicate different roles: "who" vs. "whom," "which" vs. "whose." Phi doesn't do this. `whu` is invariant. The gap's position tells you the role.

This keeps the system simple but requires attention to structure. When you hear or read a relative clause, notice where something seems to be missing. That's the gap, and it tells you how the head noun relates to the clause's action.

### Identifying the gap: practice

For each relative clause, ask: "If I turned this into a standalone sentence with the head noun inside, where would it go?"

```
whu shia lothea miona
```
→ "shia miona lothea" (they love a person)
→ gap is in object position
→ "the person whom they love"

```
whu to shua miona
```
→ "miona to shua" (a person came)
→ gap is in subject position
→ "the person who came"

```
whu mia mua shelira to nila ruela
```
→ "mia mua shelira ruela to nila" (I saw a path in the forest)
→ gap is in... wait, which noun is the head?

This last example shows that you must wait for the head noun to know what's gapped. The word `ruela` (path) at the end is the head, so the path is what was seen. The forest (`shelira`) is inside the clause, not gapped.

The rule of thumb: find the clause's verb, take the noun after it as the head, and ask which role inside the clause is empty.
