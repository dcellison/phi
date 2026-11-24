# The small words and the clause relations: study and rulings sheet

Date: 2026-11-24. Measured on `main` at `6c0a8002`, after pull requests #726 and #727, before any of the rulings below were implemented. This is the sheet the maintainer ruled from, kept as he read it. His rulings, given the same day: point 1, coin the word, and the form is `ture`; points 2 to 5, as recommended; point 6, license `tei` over a clause; point 7, register the lines as written. Decisions D130 and D131 record the result, and `canon.md` carries the rules.

Scope: assessment section 4.7 and recommendation 16. How Phi says again, still, already, not yet, no longer, even, instead, and except; and the clause relations when, whenever, as soon as, until with a clause, since, unless, and even if.

Two kinds of evidence stand under each point.

- **The texts.** Every aligned unit on the texts shelf (about two thousand) was searched by its source line, and the Phi that carries each English small word was sorted by device. Counts are close, not exact.
- **A reading test.** Thirty-eight short invented sentences, each using one candidate form, went to four fresh readers who saw only the Phi, a word-for-word gloss, and the lexicon entries for the words used. Two readers read each form. No reader saw two forms for the same meaning. Every sentence parses, except the one that tests an unlicensed form in point 6. The test measures what a reader gets from the entries as they stand today, before any teaching. The readers are models and the sentences are few, so it shows direction, not proof. The full table is at the end.

Seven points. Six need a ruling. Point 6 is the only one that changes grammar.

## 1. Again

**Now.** Phi has no word for it. The `we` entry describes addition only ("also", "too").

**The texts.** The sources say "again" or "once more" in about 32 units.

| Device | Units | Example |
|---|---|---|
| `we` before the verb | 16 | `shia we to hola.` |
| `turema` (return), where the source means "came back" | 6 | `shia nua whalo perola sholei to turema.` |
| nothing | 5 | `shia to pa haolu.` for "began to speak again" |
| `phirae` or `mawha thimu` | 3 | `mua mawha phirae thimu` for "never again" |
| `nu wi shemu` (a second time) | 2 | `shia nu wi shemu sha mia ma rinu sho to haolu.` |

Chapter 1 of *News from Nowhere* is the only chapter whose English was made source-blind. Its three `we` lines for "again" all came back as "also" ("they also fell asleep").

**Reading test.**

| Form | Both readers |
|---|---|
| `lopia to hola. ... shia we to hola.` | "laughed as well, that is, again", at 65 to 70 percent |
| `... shia to newu hola.` | "laughed anew", about 65 percent; the other reading is "laughed in a new way" |
| `shia ha philo nu wi shemu to shua.` | "came a second time"; exact, but only for a second occurrence |
| `mia phirae shemu ha so theo.` | "I will read it another time", about 60 percent again; the other reading is "some other time, not now" |

No existing device says "again" cleanly.

**Options.**

- **A. Coin one content word (recommended).** An adjective meaning repeated, once more. In the manner position it is again: `shia to rono hola` (they laughed again). Before a noun it is the additive "another": `rono hola` (another laugh, one more laugh). That leaves `phirae` to mean different, which is what its entry says. `turema` stays right for "come back". `we` returns to "also".
- **B. `newu` in the manner position.** No coinage: `to newu hola`, laughed anew. Readers get there two times in three, and "afresh" is not always what again means ("fell under the water again").
- **C. Widen `we` to cover again.** What the texts do now. The readers show it does not hold.
- **D. Ordinals only.** `nu wi shemu` is exact and stays available, but it counts, and most uses of again do not.

**If A.** The word goes through the word-creation protocol with a decision ID. Three forms are legal and have no neighbour at edit distance 1 (checked with the validator's `neighbors` command):

| Form | Note |
|---|---|
| `rono` | Two syllables. The manual already ties the recurring tap of `r` to return in `ro`. No English homonym. |
| `ture` | Two syllables. Shares its opening with `turema` (return), an audible kinship like `sileta` and `silero`. The assessment criticized words that contain an older word, so this cuts both ways. No English homonym. |
| `ronami` | Three syllables, for the assessment's advice against new two-syllable words. No English homonym. |

Again is a daily-round word, which is the protocol's own test for two syllables. The form is the maintainer's choice by ear; these are only cleared candidates.

## 2. Still, already, not yet, no longer

**Now.** The aspect particles are the nearest tools: `si` (in progress), `ki` (complete), `pa` (begins), `te` (stops). No entry or reference says how the four phase meanings are made.

**The texts.**

| English | Source uses | What the Phi does |
|---|---|---|
| still (in time) | about 11 | `si` five times, `manolu` once, `nosa` once, `nosa we` once, nothing three times |
| already | 1 | nothing |
| not yet | 5 | five different ways: `nosa` with `ma`, `li nosa ki`, `te ma`, `phoe ha shemu mawha thimu`, and "isn't up yet" turned round into `si nulae` (is sleeping) |
| no longer, any more | 8 | `te` four times, `mawha thimu` twice (read back once as "never again"), `nosa` with `ma` once, nothing once |

**Reading test.**

| Meaning | Form | Both readers |
|---|---|---|
| still | `lopia tei nosa si nulae.` | "has been sleeping up to now (is still asleep)", fairly confident |
| still | `lopia te ma nulae.` | "does not stop sleeping", about 60 percent; the other reading is "stops not sleeping" |
| not yet | `melu tei nosa ma kamo.` | "has not arrived yet", no doubt |
| not yet | `melu ki ma kamo.` | "has not arrived"; "nothing says yet" |
| already | `mia phoe nosa ki nuola.` | "I have already eaten", no doubt |
| already | `mia ki nuola.` | "I have eaten"; "nothing says already" |
| no longer | `pheralu te lepa.` and `ha lopia mua ha womu te menui.` | "is stopping", "is ceasing to live here"; all four took present `te` as the moment of stopping, not the state after it |

In the certified *Velveteen Rabbit*, past `to te` was read back as "stopped being a toy" and "no longer protected it".

**Options.**

- **A. Compose with `nosa` (recommended).** No new word and no new grammar. Four registry lines:
  - still: `tei nosa` (until now), with `si` on an activity: `lopia tei nosa si nulae`.
  - not yet: `tei nosa` with `ma`: `melu tei nosa ma kamo`.
  - already: `phoe nosa` (before now) with `ki`: `mia phoe nosa ki nuola`.
  - no longer: `to te`, because the stopping lies in the past: `lopia mua ha womu to te menui` (the child no longer lives in this home).
  - In past narration `ra shemu` takes the place of `nosa`: `tei ra shemu`, `phoe ra shemu`. Chapters 3 and 4 already write `phoe ra shemu` and `phoe ha shemu`.
- **B. Coin two descriptors,** one for still and yet, one for already. Shorter, but each would only rename what `tei nosa` and `phoe nosa` say exactly, which is the reason canon gave for refusing "seldom".
- **C. Leave it to aspect.** The readers show that `si` does not say still, `ki` does not say already, and present `te` says "is stopping".

**Cost of A.** Still takes two words where English has one. English "until now" can hint that something has just changed; one reader noted that as the weaker reading and none chose it.

## 3. Even

**Now.** `we` adds and `ko` focuses. The Slot 2 order in canon already places `we` before `ko`, so `we ko` is grammatical today. The texts never use it.

**The texts.** The sources use scalar "even" in about 18 units: `we` in 12 (the derived English says "even" in 4 and "too" or "also" in 8), `ko` once (read as "even this part"), nothing in 5.

**Reading test.**

| Form | Readers |
|---|---|
| `we ko lopia ha po thalo.` | both "even a child can walk it" |
| `we ko phao ha ma shelomu.` | both "the parent, too, does not understand", each adding that also plus focus "comes close to even" |
| `we lopia ...`, `we phao ...` | all four "too" or "either"; "even is my inference" |

**Options.**

- **A. Even is `we ko` (recommended).** Not even is `we ko` with a negated verb. The two entries and the registry say so. Addition plus focus is how many languages build the word, and the grammar already allows the pair.
- **B. Leave `we` to mean both.** The texts' practice. Readers do not recover "even" from it.
- **C. Coin a particle.** It would reopen the closed inventory for something two existing particles already say together.

Two of the four readers read `we ko` as plain "even" and two as "close to even", from entries that do not mention the pairing. I expect it to hold once the entries say it; that is my expectation, not a measurement.

## 4. Instead and except

Neither needs a new word. Each needs one line so that every text does it the same way.

**Instead.** Eight source uses, and no line has a word for it: about six restate it as a negation, a contrast, or a stopping, and two drop it. Readers took `mia hasumi ma milau thona phialu milau.` as "I don't drink tea, but I drink water" (both, no doubt). They took the place calque `mia mua hasumi lokue phialu milau.` as "I drink water at the tea place" (both, 70 to 75 percent).

- **Recommended:** instead is the refused thing negated and then the chosen thing, joined by `thona` inside one sentence or by `whekai` across two. `mua X lokue` is not used for it.

**Except.** Seventeen source uses of except and save: `li` with the polarity turned in 7, Gibran's four "save when" lines as `lu mawha ...` (if there is no ...), `phirae` in 3, other in 3. Readers took `li ne samira kau kowela to ma shua.` as "only Samira did not come to the council (everyone else came)", both confident. They split on `theula phewani whuo ne samira kau kowela to shua.`: about 60 percent "all except Samira", 40 percent "all came, without Samira along".

- **Recommended:** except is `li` on the exception with the predicate turned. All but X did is "only X did not" (`li X ... ma V`). None but X did is "only X did" (`li X ... V`). `whuo` is not used for exception.

## 5. When and whenever

**Now.** The six relators give after, before, while, because, although, and in order to. `weno` is the question word only. Nothing settles "when".

**The texts.** The sources say "when" in about 83 units.

| Device | Units |
|---|---|
| `lu` | 33 |
| no relator (restructured, dropped, or left to sequence) | 20 |
| `pheo` | 10 |
| a time-noun phrase (`mua ra shemu`, `mua mia lopia thimu`, `whu ... shemu`) | about 9 |
| `whau` | 7 |
| other (`phoe`, `lao`) | 4 |

Most of the `lu` lines are general truths, where if and when meet ("when you are Real you don't mind being hurt"). About a dozen `lu` sentences on the shelf carry a past verb.

**Reading test.**

| Form | Both readers |
|---|---|
| `lu phao to turema. lopia siora to kelu.` | "If the parent returned, the child became joyful": an open condition, not "when" |
| `pheo melu to kamo lo mia to nuola.` | "After the friend arrived, we ate", no doubt |
| `whau melu to kamo lo mia to si nuola.` | understood as "when the friend arrived, we were eating", but both called it odd: the entry says the `whau` clause holds the span open, and an arrival is a point |
| `lu pheralu lepa. lo mia mua womu ro manolu.` | "If it rains, we stay home, as a custom", "close to whenever" |
| `whau pheralu lepa lo mia mua womu ro manolu.` | "Whenever it is raining, we stay home" |

**Options.**

- **A. No new word; sort "when" and say how (recommended).**
  - One occasion, one event and then the other: `pheo`. `pheo melu to kamo lo mia to nuola.`
  - One occasion, the two overlapping: `whau`, with its description widened so that the dependent event may be the shorter one, a point inside the main clause's span. The time anchor can then come first, as dependent clauses do: `whau melu to kamo lo mia to si nuola.` Canon already calls `whau` the relator that "declines to order" two events. Only the entry's wording about holding the span open narrows it.
  - Whenever, and "when" in a general truth: `lu`, with `ro` on the consequence where the point is a habit. `lu pheralu lepa. lo mia mua womu ro manolu.`
  - `lu` is never "when" for a single past occasion.
  - A time named by a noun stays a phrase: `mua mia lopia thimu` (in my childhood).
- **B. The same, with `whau` kept strict.** The longer event always stands under `whau` (`whau lo mia to si nuola melu to kamo.`). Canon is untouched, and the speaker turns the sentence round.
- **C. Coin a seventh relator for "when".** It would reopen a closed set to import the one ambiguity (after or while) that Phi's relators exist to remove.

**If A or B.** The parser can add an advisory for a `lu` sentence with a past verb whose consequence has no `ro`. It cannot be an error, because an open condition about the past is legitimate.

## 6. Until with a clause

**Now.** `tei` is a preposition and takes a noun phrase. The parser rejects a tensed clause after it.

**The texts.** Five source uses of until or till with a clause. Three turned the clause into a noun phrase: `tei thia luwi` (until your flexibility), `tei pai kaeli thorui` (until near the beginning of liking), `tei pai ta phoi wi shao torua` (until about fifteen years). Two dropped the until altogether (chapter 1 unit 68, *Velveteen Rabbit* unit 225). Gibran's `tei thia lumeo` (until your death) is the noun pattern again.

**Reading test.**

| Form | Both readers |
|---|---|
| `lopia tei phao turema nia whelina to wile.` (event noun) | "until the parent's return", low doubt |
| `lopia tei whu phao mua to turema shemu nia whelina to wile.` (relative clause on `shemu`) | correct, and both called the stranded `mua` awkward |
| `tei pheralu to te lepa lo mia mua womu to manolu.` (clause, not licensed today) | "until the rain stopped falling, we stayed at home"; meaning clear to both, and both noticed that the entry calls `tei` a preposition |

**Options.**

- **A. License `tei` over a clause (recommended).** `pheo` and `phoe` already stand over both a time phrase and a clause; `tei` would do the same. The clause comes first, carries its own tense under the ruling of 2026-11-24, and ends at its verb. `tei` over a noun is unchanged. The reason is the one canon gave for `whau`: under a preposition the event becomes a noun, its subject is demoted to a possessor, and it can carry no tense, negation, or object. That is why two of five lines gave up.
- **B. Keep `tei` a preposition.** Register `tei` with an event noun for the simple case and `tei whu ... shemu` for the rest. No grammar changes; the heavy cases stay heavy.

**A is a grammar extension,** so it is the maintainer's to open. It touches canon (the relator set and its count), the parser, the `tei` entry, the preposition reference, and the adverbial-clause teaching in the manual and pamphlet.

## 7. The remaining relations

No options here. These are what the existing grammar already says, most of them tested. One approval registers them as written.

| English | Phi | Evidence |
|---|---|---|
| at once, immediately | `pheo mu thimu` (after zero time) | both readers "at once"; *The North Wind and the Sun* uses it twice. Elsewhere the texts write `nosa` (now) four times and `reshi` (fast) five times for it. |
| as soon as | a `pheo` clause, then `pheo mu thimu` in the main clause: `pheo melu to kamo lo mia pheo mu thimu to wepu.` | both "left at once", "close to as soon as". `whuo hasi` (without waiting) read at 70 percent. |
| soon | `pheo teku shemu` with `so` | both "in a little while, soon" |
| since (time) | `lue` with a time phrase and `tei nosa`: `mia lue ra philo tei nosa shia ma nila.` Over a clause: a `pheo` clause with `tei nosa` in the main clause. | both "from that day until now", "amounts to since". A bare `pheo` clause read as "after", with since only implied. |
| unless | `lu` with a negated condition: `lu pheralu ma lepa. lo mia so thalo.` | both, no doubt |
| even if | `shai` with `po` in its clause: `shai pheralu po lepa lo mia so thalo.` | both "although it may rain", "close to even if" |
| whether or not | `lu` with the verb and its negation joined by `sola`: `lu pheralu lepa sola ma lepa. lo mia so thalo.` | both, no doubt |
| only if | `lu` with both clauses negated: `lu thia ma naphe. mia ha so po ma phoa.` | not tested; it is the same statement turned round |
| as if | `phea whu ...` and a noun (like one who ...), with `ke` on the verb for "seemed" | the texts' steady practice, about ten units |
| so ... that | `ru` and the quality, then `thelao` and the result | three of five source uses, in *The Velveteen Rabbit* and *The North Wind and the Sun* |
| the more ... the more | `mo` in both clauses, under `lao` or `lu` | *The North Wind and the Sun* |

## Not on this sheet

- **Other, another, else.** The texts use `phirae` (different) for all three. That belongs to the vocabulary step (recommendation 22). If point 1 is ruled as A, the new word covers the additive "another" and narrows what is left to decide.
- **Phrase boundaries** (recommendations 6, 11, 31). Next on the list, with the parse-count instrument built first.

## What follows the rulings

1. One pull request for the language: a registry of small words and clause relations beside the compound registry, with a validated example for every line; canon bullets for whatever is ruled; the entries concerned (`we`, `ko`, `te`, `tei`, `whau`, `lu`, `nosa`); the manual's time chapter and adverbial-clause pages; and the parser if point 6 is opened.
2. The "again" word through the word-creation protocol, with its decision ID, in that pull request or its own.
3. No text is changed. The lines each ruling makes wrong are listed for the single sweep at the end: about 16 units with `we` for again, about 12 with `we` for even, about a dozen past `lu` sentences, and the scattered still, already, and no longer lines.

## Appendix: the reading test

Two packets, two readers each. "Both" means the two readers of that packet agreed.

| Meaning tested | Phi | Read as |
|---|---|---|
| again | `lopia to hola. pheo teku shemu shia we to hola.` | both "laughed as well (again)", 65 to 70 percent |
| again | `lopia to hola. pheo teku shemu shia to newu hola.` | both "laughed anew", 65 percent |
| again | `melu luera philo to shua. shia ha philo nu wi shemu to shua.` | both "today they came a second time"; 30 percent "today's second moment" |
| again | `mia ha shelu to theo. mia phirae shemu ha so theo.` | both "another time", 60 percent again |
| still | `sileta ki rihe. lopia te ma nulae.` | both "does not stop sleeping", 60 percent |
| still | `sileta ki rihe. lopia tei nosa si nulae.` | both "sleeping up to now (still asleep)" |
| not yet | `howai nai. melu tei nosa ma kamo.` | both "has not arrived yet" |
| not yet | `howai nai. melu ki ma kamo.` | both "has not arrived" |
| already | `no nurome ma thilonu. mia phoe nosa ki nuola.` | both "I have already eaten" |
| already | `no nurome ma thilonu. mia ki nuola.` | both "I have eaten" |
| no longer | `no shua. pheralu te lepa.` | both "the rain is stopping" |
| no longer | `ha lopia mua ha womu te menui.` | both "is ceasing to live in this home", 60 percent |
| even | `ha ruela siloma nai. we ko lopia ha po thalo.` | both "even a child can walk it" |
| even | `ha ruela siloma nai. we lopia ha po thalo.` | both "a child, too, can walk this" |
| not even | `ha shelu kethua nai. we ko phao ha ma shelomu.` | both "a parent, too, does not understand this", "close to even" |
| not even | `ha shelu kethua nai. we phao ha ma shelomu.` | both "the parent does not understand it either" |
| instead | `mia hasumi ma milau thona phialu milau.` | both "I don't drink tea, but I drink water" |
| instead | `mia mua hasumi lokue phialu milau.` | both "I drink water at the tea place" |
| except | `li ne samira kau kowela to ma shua.` | both "only Samira did not come" |
| except | `theula phewani whuo ne samira kau kowela to shua.` | both 60 percent "all except Samira" |
| when (sequence) | `pheo melu to kamo lo mia to nuola.` | both "after the friend arrived, we ate" |
| when (sequence) | `pheo phao to turema lopia siora to kelu.` | both "after the parent returned, the child became joyful" |
| when (single past, `lu`) | `lu phao to turema. lopia siora to kelu.` | both "if the parent returned ..." |
| when (overlap) | `whau melu to kamo lo mia to si nuola.` | both "while the friend arrived, we were eating"; odd |
| whenever | `lu pheralu lepa. lo mia mua womu ro manolu.` | both "if it rains, we stay home (as a custom)" |
| whenever | `whau pheralu lepa lo mia mua womu ro manolu.` | both "whenever it is raining, we stay home" |
| as soon as | `pheo melu to kamo lo mia pheo mu thimu to wepu.` | both "we left at once" |
| as soon as | `pheo melu to kamo lo mia whuo hasi to wepu.` | both "left without waiting", 70 percent |
| until, clause | `lopia tei phao turema nia whelina to wile.` | both "until the parent's return" |
| until, clause | `lopia tei whu phao mua to turema shemu nia whelina to wile.` | both correct; awkward |
| until, clause | `tei pheralu to te lepa lo mia mua womu to manolu.` | both "until the rain stopped falling, we stayed at home"; grammar doubted |
| since | `mia lue ra philo tei nosa shia ma nila.` | both "from that day until now I have not seen them" |
| since | `pheo melu to wepu mia ki ma nulae.` | both "after the friend left, I have not slept" |
| unless | `lu pheralu ma lepa. lo mia so thalo.` | both "if it does not rain, we will walk" |
| even if | `shai pheralu po lepa lo mia so thalo.` | both "although it may rain, we will walk" |
| whether or not | `lu pheralu lepa sola ma lepa. lo mia so thalo.` | both "whether it rains or not, we will walk" |
| soon | `melu pheo teku shemu so kamo.` | both "will arrive in a short while" |
| at once | `shia pheo mu thimu to wepu.` | both "left at once" |

Two faults in my own test sentences, which the readers caught: the first two rows open the second sentence with `pheo teku shemu` before its subject, against the adjunct ruling of 2026-11-24; and `ha po thalo` gives `thalo` (walk) a direct object, which its entry does not show. Neither affects the word under test.
