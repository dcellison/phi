# Part 5: Advanced patterns

This section covers more complex uses of relative clauses, including nesting, interaction with complementizers, and extended discourse.

## Nested relative clauses

A relative clause can contain another relative clause. This happens when describing something that is itself described by a clause.

### Basic nesting

```
mia rena rena nophi kealo miona to thumela lopia sano
1SG REL REL story create person PST teach child know
(i know the child whom the person who creates stories taught.)
```

Breaking this down:
- Inner relative clause: `rena nophi kealo miona`, "the person who creates stories"
- Outer relative clause: `rena [inner clause] to thumela lopia`, "the child whom [that person] taught"
- Main clause: `mia ... sano`, "i know..."

The structure nests like parentheses:

```
mia [rena [rena nophi kealo miona] to thumela lopia] sano
```

### Processing nested relatives

Nested relatives require careful attention. The listener must:
1. Recognize the first `rena`: a relative clause is starting
2. Recognize the second `rena`: another relative clause is starting inside the first
3. Find the noun after the inner clause's verb: that closes the inner clause
4. Find the noun after the outer clause's verb: that closes the outer clause
5. Continue with the main clause

This is cognitively demanding. In practice, speakers often break complex descriptions into separate sentences:

**Instead of:**
```
mia rena rena nophi kealo miona to thumela lopia sano
```

**Consider:**
```
miona nophi kealo. mia rena ha miona to thumela lopia sano.
person story create. 1SG REL PROX person PST teach child know.
(a person creates stories. i know the child whom this person taught.)
```

Splitting reduces nesting and aids comprehension.

### When nesting is unavoidable

Sometimes the nested structure is exactly what you need:

```
rena rena mia lothea miona to kealo nophi phelora nai
REL REL 1SG love person PST create story beautiful be
(the story that the person whom i love created is beautiful.)
```

This precisely captures: there's a person I love; that person created a story; that story is beautiful. The relationships are all contained in one utterance.

### Depth limits

In principle, nesting can continue indefinitely. In practice, more than two levels becomes nearly impossible to process:

```
rena rena rena ... miona ... nophi ... shelu ...
```

If you find yourself going three levels deep, restructure. Break it into multiple sentences. Phi's topic-drop makes this easy:

```
miona ha nai. ha miona nophi kealo. mia rena ha miona to kealo nophi lothea.
person PROX be. PROX person story create. 1SG REL PROX person PST create story love.
(a person is here. this person creates stories. i love the story that this person created.)
```

## Relative clauses with complementizers

Relative clauses can contain embedded statements (`mena`/`meno`), quotations (`shola`/`sholo`), or embedded questions (`wela`/`welo`).

### Containing `mena`/`meno`

```
rena mena mia so shua meno sano miona ha nai
REL DECL.COMP 1SG FUT come DECL.COMP.CLOSE know person PROX be
(the person who knows that i will come is here.)
```

Structure:
- Relative clause subject gap: "the person who knows [something]"
- Inside the relative: `mena mia so shua meno`, "that I will come"
- The person knows that I will come

Another example:

```
mia rena mena shea welao nai meno haolu nophi theo
1SG REL DECL.COMP peace good be DECL.COMP.CLOSE speak story read
(i read the story that says that peace is good.)
```

The gap is in subject position: the story is what does the saying. `meno` closes the embedded statement; the head noun `nophi` closes the relative clause.

### Containing `shola`/`sholo`

```
rena shola mia so shua sholo to haolu miona mia melu nai
REL QUOT.COMP 1SG FUT come QUOT.COMP.CLOSE PST speak person 1SG friend be
(the person who said "i will come" is my friend.)
```

The quotation sits inside the relative clause. The quoted words are preserved exactly.

### Containing `wela`/`welo`

```
rena wela shia so shua welo ma sano miona si remo
REL INT.COMP 3SG FUT come INT.COMP.CLOSE NEG know person IPFV think
(the person who doesn't know whether they will come is still thinking.)
```

The embedded question `wela shia so shua welo` is the object of `sano` inside the relative clause.

## Interaction with topic-drop

Topic-drop and relative clauses work together. A noun introduced with a relative clause becomes a topic that subsequent sentences can reference implicitly.

### Establishing and continuing

```
rena mia to nila peloru phelora nai. thuroa. mia lothea.
REL 1SG PST see flower beautiful be. grow. 1SG love.
(the flower that i saw is beautiful. [it] grows. i love [it].)
```

The flower, once introduced with its full description, becomes the understood topic. Two subsequent sentences refer to it without naming it.

### Switching topics

When you want to change the topic, introduce a new noun (with or without a relative clause):

```
rena mia to nila peloru phelora nai. shiro ha nai. whalo nai.
REL 1SG PST see flower beautiful be. tree PROX be. large be.
(the flower that i saw is beautiful. a tree is here. [it] is large.)
```

The tree becomes the new topic; "large" describes the tree, not the flower.

### Extended discourse example

```
mia serao miona to nila. rena nophi kealo miona phue nai.
1SG old person PST see. REL story create person wise be.
(i saw an old person. the person who creates stories is wise.)

shia wei mia nophi to haolu. rena mia to hea nophi phelora nai.
3SG DAT 1SG story PST speak. REL 1SG PST hear story beautiful be.
(they told me a story. the story that i heard is beautiful.)

mia kau ha miona so turema.
1SG ALL PROX person FUT return.
(i will return to this person.)
```

Topics shift naturally: person → story → person. Relative clauses identify which person and which story we mean, while topic-drop keeps the prose flowing.

## Relative clauses in reported speech

When quoting or reporting speech that contains relative clauses, the structure embeds naturally.

### Direct quotation

```
shia shola rena mia to kealo shelu phelora nai sholo to haolu
3SG QUOT.COMP REL 1SG PST create book beautiful be QUOT.COMP.CLOSE PST speak
(they said "the book that i created is beautiful.")
```

The relative clause `rena mia to kealo shelu` sits inside the quotation.

### Indirect report

```
shia mena rena shia to kealo shelu phelora nai meno to haolu
3SG DECL.COMP REL 3SG PST create book beautiful be DECL.COMP.CLOSE PST speak
(they said that the book that they created is beautiful.)
```

Note the pronoun shift: inside indirect speech, "I" becomes "they."

## Possessed nouns inside relative clauses

Possession is bare juxtaposition, the possessor standing directly before the possessed noun. Inside a relative clause, nothing changes:

```
rena mia shelu to theo miona ha nai
REL 1SG book PST read person PROX be
(the person who read my book is here.)
```

"My book" (`mia shelu`) is the clause's object; the head `miona` is the one who read it.

```
mia rena mia mua shia peloru to nila thepalu sano
1SG REL 1SG LOC 3SG flower PST see garden know
(i know the garden where i saw their flower.)
```

Here the possessed phrase `shia peloru` ("their flower") is the object, and the stranded `mua` marks the oblique gap that the head `thepalu` fills.

## Complex real-world example

Let's build a paragraph using multiple relative clauses, complementizers, and topic-drop:

```
mia mua rena mua shelira nai womu to kamo. phelora nai.
1SG LOC REL LOC forest be home PST arrive. beautiful be.
(i arrived at the home that is in the forest. [it] is beautiful.)

rena mua ha womu nai miona phue nai.
REL LOC PROX home be person wise be.
(the person who is in this home is wise.)

shia wei mia nophi to haolu. rena mia to hea nophi mena shea mua shelira nai meno to haolu.
3SG DAT 1SG story PST speak. REL 1SG PST hear story DECL.COMP peace LOC forest be DECL.COMP.CLOSE PST speak.
(they told me a story. the story that i heard said that peace is in the forest.)

mia rena shia to haolu shelomu. shea mua mia nai.
1SG REL 3SG PST speak understand. peace LOC 1SG be.
(i understand what they said. peace is in me.)
```

This passage uses:
- Locative relative clause (`rena mua shelira nai womu`)
- Subject-gap relative clause (`rena mua ha womu nai miona`)
- Object-gap relative clause (`rena mia to hea nophi`)
- Embedded `mena`/`meno` inside a relative clause
- Headless relative clause (`rena shia to haolu`)
- Topic-drop throughout

Nothing new was needed to combine them; each pattern keeps its own rules.
