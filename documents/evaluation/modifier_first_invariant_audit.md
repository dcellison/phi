# Modifier-first invariant audit

## Result

Phi has one modifier-first rule and no syntactic exception to it. Every active construction reviewed here keeps modifying, specifying, or relating material before what it affects. Coordination joins equal constituents rather than modifying the left one; a complementizer closer marks the end of material already opened on the left; a standalone `kona` phrase is outside the clause. These are boundaries, not counterexamples.

The audit excludes `archive/`. Historical material has no authority over current Phi and was neither searched nor used as evidence.

## What was checked

The review covered the current canon, grammar references, manual, pamphlets, primer, book, texts, project guidance, all 1,275 vocabulary entries, generated reference material, and the validator. It searched both English explanations and Phi examples. The structured lexicon contains 1,375 examples and 1,398 sentences. The review's scan covered 5,313 active Markdown Phi spans recognized by the validator. Of these, 489 had a Slot 0 frame, 319 had a discourse marker, and 109 used `lu`. The same scan found 246 clause-relator spans and 393 with `rena`.

| Construction | Required order | Audit result |
|---|---|---|
| Predicate clause | subject, circumstances, object, predicative complement, manner and Slot 1 material before the predicate | No licensed post-predicate argument or modifier was found. The validator reports no Slot 1 misorder, and the later complement-order ruling keeps the complement before the Slot 1 stack. |
| Noun phrase | possessors, descriptions, quantity, classifiers and Slot 2 material before the noun | Current teaching and examples agree. The fixed `mo ko` superlative remains wholly before its target. |
| Prepositional phrase | preposition before its object; the phrase before the object or predicate it modifies | All 27 preposition entries agree, and the detectable postposition check reports no violation. |
| Dependent frame | `pheo`, `phoe`, `lao`, `shai` or `lila` before its dependent material; a complete dependent clause before the main clause | Every current relator span was screened. Twenty causal or concessive renderings that looked backward across a result or sentence boundary were repaired. The `lila` check reports no postposed purpose frame. |
| Conditional frame | optional outer `pi`, then `lu` and its complete condition sentence; the complete consequence follows | Every current `lu` span was screened. Inline consequences, postposed conditions, and condition fragments now use the two-sentence frame. |
| Complement frame | opener and embedded content before the closer; the complete frame before the matrix predicate | Every complete active example now has a matrix predicate after its closer. Closers are right boundaries inside a frame, not modifiers of material to their left. |
| Relative clause | `rena` and the relative clause before an explicit head noun, or in noun-phrase position when headless | All current `rena` spans were screened. An oblique preposition remains before its gap; the later head noun is outside the relative clause and is not a postposed prepositional object. |
| Discourse and address | Slot 0 first, then any discourse marker, then dependent material and the sentence it frames; `kona` before the addressee | Late question, directive, wish, politeness, and condition frames were repaired. A vocative may stand as its own extra-clausal utterance. |

## Repairs made

Four lexicon entries stated the order backwards. `thunaro` put the learner after the verb, `ma` put the predicate before the particle, `moloi` placed the craft after the apprentice, and `phiora` placed a describing noun after spirit. A wider pass found other notes that used "follows" for an object, complement, condition, or scope and left the order needlessly uncertain. Those notes now say what precedes the predicate or noun. A detail stated later goes into its own clause.

Three places called Phi head-final even though its prepositions make its typological direction mixed. They now say predicate-final or modifier-first, whichever the passage needs. The two explanations of oblique relative gaps now separate the in-clause gap from the head noun outside the clause.

Three dictionary examples used `keru` (bright) as if it meant give. They now end in `loa` (give): a rose gives scent, hemp gives fibre, and an elm gives shade. This was a word-class error rather than an alternative order, but it had hidden inside complete-sentence data and belonged in the same structural repair.

The active text shelf contained causal fragments modelled too closely on English "for" and "since." The affected *Solarpunk Manifesto* and *News from Nowhere* passages now put each reason before its result in the same Phi sentence. One standalone `shai` fragment became a sentence-level contrast with `whekai`. Source citations and meanings remain intact.

Several literary passages treated `shola ... sholo` as freestanding written quotation marks. Phi uses the pair as a complement frame, so a bare closer left the framed words without the predicate they were meant to modify. The affected reference sample and text renderings now place context-dropped `to haolu` after `sholo`. This repairs 81 active occurrences, including continuous-reading copies of the same passages.

The remaining conditionals in two *News from Nowhere* chapters had often followed English punctuation: condition and result shared one sentence, an "unless" clause came after its result, or a quote ended before giving the condition any consequence. The repaired passages finish the `lu` sentence first. Where the source deliberately breaks off after "unless," the Phi rendering states the consequence the interrupted speaker was about to imply.

A smaller set put Slot 0 behind a discourse marker or a dependent clause. Questions now use `wa whekai`, directives use `no thelao` or `no whekai`, and wishes use `su whekai`. Purpose, reason, and temporal frames follow the utterance frame but still precede the main clause. These repairs occur in the philosophical test corpus and four literary works, including the same two novel chapters.

## Enforcement

The validator now requires every structured lexicon sentence to finish with a predicate or to be a standalone interjection or `kona` call. It verifies that Slot 0 precedes discourse and dependent material, that a discourse marker follows Slot 0 and precedes sentence content, and that every `lu` condition ends before a complete consequence begins. It also matches `mena ... meno`, `wela ... welo` and `shola ... sholo`, then requires the complete frame to precede a matrix predicate in both structured examples and complete active documentation examples. Regression tests reject adjective-final assertions and bare quotation frames. They also reject late utterance framing and malformed condition pairs. Positive cases cover a standalone vocative, coordinated questions, nested quotation, and a polite optative.

A static checker cannot infer every attachment in unrestricted prose. For example, a verb-shaped event noun and a finite verb share one form, while a noun before `rena` may be a matrix subject rather than a postnominal head. Those cases received direct review instead of a guessed parser rule. The machine checks guard the structures they can determine, and the reviewed active corpus contains no remaining modifier-first exception.
