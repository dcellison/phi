# Understanding embedded clauses

## What is an embedded clause?

When we speak, we often need to express not just simple actions, but thoughts *about* thoughts. Consider the difference:

**Simple:** *She left.*
**Embedded:** *I know that she left.*

In the second sentence, "she left" is no longer a standalone statement. It has become the *content* of knowing, tucked inside a larger sentence. The embedded clause "that she left" is what I know, the object of my mental verb.

This lets us take a complete thought and make it part of a larger thought. We can report what others said, wonder about possibilities, express beliefs, and stack knowledge upon knowledge, all through embedding.

## Three types of embedding

Languages generally embed three kinds of content. The first is statements: facts, beliefs, reports of what someone communicated. I know *that the sun is warm*; she believes *that rain will come*; he said *that you arrived*. The second is questions: uncertainties, wonderings, inquiries being considered. I wonder *whether she will come*; she asked *if I had seen the book*; we don't know *whether it's true*. The third is quotation, someone's exact words preserved verbatim. She said, *"I am leaving."* He asked, *"Are you well?"* The teacher announced, *"Class begins now."*

English handles these differently. Statements use "that" (often optional). Questions use "whether" or "if." Quotations use quotation marks in writing, and intonation shifts in speech.

Phi handles all three with one system: paired complementizers that open and close the embedded material, like spoken brackets.

## How English does it

In English, embedding is somewhat casual. The word "that" introduces embedded statements, but speakers often drop it:

- I know (that) she left.
- He believes (that) it's true.
- She said (that) you called.

The boundary between the embedded clause and the main clause is unmarked at the end. English relies on word order and context to signal where the embedded content stops.

For questions, English uses "whether" or "if":

- I wonder whether she came.
- He asked if you were ready.

Again, no explicit closer. The sentence just ends, or the main clause continues without marking.

For quotations, English uses quotation marks in writing. In speech, there is no audible marker. A subtle pause or intonation shift might signal the quotation, but nothing explicit:

- She said, "I'm leaving."
- He announced, "The meeting is canceled."

This works reasonably well in simple sentences. But consider:

- I believe that she knows that he said that you think that it's true.

Where does each embedded clause end? English speakers parse this through accumulated practice, but the boundaries are implicit, recoverable only through semantic plausibility and verb valency.

## How Phi does it differently

Phi makes all boundaries explicit. Every embedded clause gets both an opener and a closer: spoken brackets.

| Type | Opener | Closer | Function |
|------|--------|--------|----------|
| Declarative | `mena` | `meno` | Embeds statements (that...) |
| Interrogative | `wela` | `welo` | Embeds questions (whether...) |
| Quotative | `shola` | `sholo` | Preserves exact words ("...") |

The opener announces what kind of content follows. The closer marks exactly where that content ends. The main verb then follows the closer, unambiguously.

**English:** I understand that they left.
**Phi structure:** I [DECL.COMP they left DECL.COMP.CLOSE] understand.

```
mia mena shia to wepu meno shelomu
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE understand
(I understand that they left.)
```

The `mena` opens the embedded statement. The `meno` closes it. The main verb `shelomu` follows, and there is no ambiguity about what belongs to the embedded clause versus the main clause.

## Why closers matter

You might wonder: why does Phi need closers? English manages without them.

The answer lies in Phi's word order. Phi is strictly SOV (Subject-Object-Verb), meaning verbs come at the end of their clauses. When you embed one clause inside another, you get verb-verb sequences:

**Without closer (ungrammatical):**

```
*mia mena shia to wepu shelomu
1SG DECL.COMP 3SG PST go understand
```

Is this "I understand that they left"? Or is it attempting to say something about "they leaving-understanding"? Where does `wepu` end and `shelomu` begin? Two verbs in sequence, no boundary marked.

**With closer (unambiguous):**

```
mia mena shia to wepu meno shelomu
1SG DECL.COMP 3SG PST go DECL.COMP.CLOSE understand
(I understand that they left.)
```

Now the boundary is explicit. The `meno` says so: the embedded clause has ended. What follows is the main verb.

This is especially important when clauses nest:

```
mia mena thia mena shia to wepu meno phaelo meno shelomu
1SG DECL.COMP 2SG DECL.COMP 3SG PST go DECL.COMP.CLOSE feel DECL.COMP.CLOSE understand
(I understand that you feel that they left.)
```

Three verbs in sequence: `wepu`, `phaelo`, `shelomu`. Without the closers, parsing would be impossible. With them, each `meno` resolves exactly one `mena`, like matched parentheses in mathematics.

## The opener-closer pattern

Phi uses a consistent phonetic pattern for complementizer pairs:

- **Openers end in `-a`**: mena, wela, shola
- **Closers end in `-o`**: meno, welo, sholo

The vowel shift is not arbitrary decoration. `a` is the openest sound the mouth makes; `o` rounds the lips toward closure. Every time a frame opens or closes, the mouth acts out the boundary: jaw dropped at the opening, lips drawn round and nearly shut at the close. When you hear a complementizer ending in `-a`, something is opening. When you hear the same root ending in `-o`, it just closed.

## Cross-linguistic perspective

Phi's approach resembles several natural languages more than it resembles English:

**Japanese** uses quotative particles (`to`, `tte`) that follow quoted material, and clause-final particles that mark clause types. While Japanese does not use paired brackets exactly as Phi does, it shares the verb-final structure that motivates explicit boundary marking.

**Korean** similarly places verbs at the end and uses various complementizers and quotative markers to manage embedded clauses.

**Turkish** embeds clauses through nominalization and explicit case marking, which keeps the structural boundaries of its verb-final sentences clear.

What these languages share is the recognition that when verbs cluster at clause boundaries, explicit marking prevents ambiguity. Phi takes this principle further by systematically pairing every opener with a closer.

**Lisp and formal languages** offer another parallel. In Lisp programming, every opening parenthesis has a matching closing parenthesis: `(outer (inner content) continues)`. Phi's complementizers work the same way: every opener finds its closer, and the whole parses without guesswork. This is not coincidental. Phi was designed with awareness that spoken language can be structurally unambiguous when delimiters match.

## Where this leads

The next section explains why the closers exist and why `rena` alone does without one. The three sections after it give each pair its own room, and the rest of the pamphlet turns the system into reflex: nesting, the errors English invites, exercises, and a reference page.

None of it is decoration. Every belief you report, every doubt you voice, and every word you repeat for someone absent will pass through one of these frames. A speaker who can open and close them without thinking is free to attend to what actually matters: whose thought is being held, and how carefully.
