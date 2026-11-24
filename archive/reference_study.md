# Who is `shia`? Study and rulings sheet

Date: 2026-11-24. Measured from the `add_object_particle` branch with `scripts/phi_readings.py`, `scripts/phi_roles.py`, and `scripts/audit_phrase_readings.py` on the lexicon at 1,307 entries, before the ruling was implemented. This is the sheet the maintainer read, kept as written, with an addendum for the test his ruling asked for. He first said the sheet asked too many points and that the obvious ones should be settled on the recommendations given; points 3 to 8 were settled that way. On point 1 he ruled: "If adding a second third-person pronoun reduces forced naming then add it." On point 2 he chose `hia`. The addendum reports the test of that condition. Decision D135 records the result, and the rule lives in `/canon.md`.

Scope: the November assessment's section 4.4 and its recommendation 15. Phi has one third-person pronoun. The assessment asked for two things: a reflexive possessor, which D128 settled with `miso`, and a way to keep two third persons apart, for which it proposed teaching `ha` and `ra` and said this "needs teaching and a few examples, nothing more". This sheet tests that proposal and its rivals.

Any option that adds a word reopens a closed inventory, here the core pronouns. That decision is the maintainer's. Section 5, point 1 says plainly how this case stands against canon's Grammar Amendment Boundary, and it stands less strongly than the seams did.

## 1. The size of it

Counts are of the translations unless a row says otherwise. All are upper bounds on what the grammar leaves open. None is a rate of misreading.

| | Count | Share |
|---|---:|---:|
| Uses of `shia` | 1,102 | |
| Of which singular (no `lo` before it) | 846 | |
| Singular uses while the tracker holds two or more third persons live, things included | 264 | 31% |
| Singular uses while two or more people or animals are live (hand list of 34 nouns and names) | 93 | 11% |
| Of those, in *The Velveteen Rabbit* | 72 | |
| Of those, with exactly two rivals | 80 | |
| Of those, opening their sentence | 41 | |

Three findings narrow the problem.

**Inside one clause the work is nearly done.** The ledger counts 38 clauses with two separate `shia`. Read against their source lines, 29 are the same person twice (its own neck, her own arms, he and his great-grandparent), which `miso` covers since D128 and which wait only for the text sweep. Five set a singular against a plural, which `lo` keeps apart. Three hold two different singular persons (`shia shia to ru kema lothea`, he loved him), and there subject-before-object order does what English order does. One is the misread line, below.

**The exposure is across sentences.** The question a listener cannot answer is who the `shia` at the head of the next sentence is. The one verified misreading in certified text is of this kind: `waeshi tupiwa sha ... sho to haolu. shia roa shia to pa rato. shia to pa rotiku.` The source has the wild rabbit whirl and dance; the source-blind English has Tupiwa do it.

**Naming is what the texts do instead, and it has a price.** *The Velveteen Rabbit* names a character with `ne` 205 times. In 77 of those the source line has no name at that point, only a pronoun or nothing. `ne tupiwa` alone stands 109 times, 51 of them where the source line does not say *Rabbit*.

Two improvised forms are already on the shelf, once each, both in *The Velveteen Rabbit*: `ha shia` for the source's "this one" and `phirae shia` for "the other". The source-blind reader rendered the first as "At that, the wild rabbit stretched its neck", taking `ha` as a separate word.

## 2. What the grammar offers today

- One third-person pronoun, `shia`, with `lo shia` for the plural. The manual says its "whole ambition is to let a person be mentioned without being categorized."
- A name or noun repeated. Always available, never ambiguous.
- `miso`, for the subject of the same clause, as object, after a preposition, and as possessor.
- An unsaid subject, once a subject is established.
- `ha` and `ra` before a noun (`ra tupiwa`, that rabbit), and alone in any noun position as this and that (canon, Predicative deictics).

How lone `ha` and `ra` are used now matters for what follows. By a search for the deictic followed by a Slot 1 particle, a preposition, a frame word, or a clause end, `ha` stands alone on the texts shelf as a subject or object 91 times and after a preposition 7 times. Every one I read points at a thing or at the matter just said (`mia ha to remo`, I thought this; `ha wei mia nuwi nai`, this is clear to me). None clearly points at a person. `ra` stands alone as a subject or object nowhere on the shelf; it appears alone 6 times after a preposition (from there, like that) and twice as a place.

The parser on this branch does not yet accept everything canon allows a lone deictic. It rejects `lo ra to wepu` and `lo ha to wepu` (those left, these left), `ha ku lopia to nila` (this one saw the child, with the object marked), `ne tupiwa ku ha to nila` (Tupiwa saw this one), and `ha ra to nila` (this one saw that one). The first is a gap older than `ku`. The second and third are gaps in pull request #730.

## 3. What readers do

Twelve short passages were written with two third persons each, both able to do what the second sentence says. Seams were closed with `ku` so that only reference stayed open. One passage is the misread *Velveteen Rabbit* line with its two preceding sentences shortened. Four packets went to two fresh readers each, who saw only the Phi, a gloss, and the entries:

- **Unmarked.** `shia` throughout, entries as they stand.
- **Lone `ha` and `ra`, entries as they stand.** No convention stated.
- **Lone `ha` and `ra`, convention stated.** Three sentences added to the entries: plain `shia` stays with the subject of the sentence before; lone `ha` resumes that one; lone `ra` is the other third person; once `ra` has been a subject, the next `shia` continues it.
- **A second pronoun.** The placeholder `ria`, glossed 3OTHER, with a four-sentence entry stating the same convention.

In the marked packets the marker was placed to select, in most passages, the reading the unmarked readers had not chosen. Four passages used no marker and relied on the stated rule for plain `shia`.

| Packet | Read as marked | Mean confidence |
|---|---|---:|
| Unmarked | (the two readers agreed with each other on 11 of 12) | 56% |
| Lone `ha` and `ra`, today's entries | `ra`: one reader 7 of 8, the other 2 of 8; they agreed on 1 of 8. `ha`: neither reader, 0 of 2 | 52% |
| Lone `ha` and `ra`, convention stated | both readers, 12 of 12 | 71% |
| `ria`, entry stated | both readers, 12 of 12 | 74% |

By passage (first reading, with confidence where both readers agreed):

| Passage, as unmarked | Unmarked | Marked for | `ha`/`ra` today | `ha`/`ra` taught | `ria` |
|---|---|---|---|---|---|
| `ne samira ku ne timothi to nila. shia to seniku.` | Samira smiled, 60 and 55 | Timothi | split | Timothi, 88 and 82 | Timothi, 92 and 90 |
| `wheo wei lopia ku lureko to loa. shia to hola.` | the child laughed, 55 and 55 | the elder (`ha`, or `shia` by rule) | the child, 60 and 70 | the elder, 80 and 72 | the elder, 72 and 70 |
| `ne samira wei ne timothi sha thia kua wepu sho to thilou. shia to pa wepu.` | Timothi set off, 55 and 60 | Samira (`ha`, or `shia` by rule) | Timothi, 60 and 70 | Samira, 70 and 65 | Samira, 68 and 60 |
| `telo ku lohau to hekawi. shia ru siora to phaelo.` | the farmer rejoiced, 65 and 60 | the dog | split | the dog, 62 and 58 | the dog, 78 and 80 |
| `ne samira ku ne timothi to hea. shia wea shia to shua.` | split | Timothi came to Samira | split | as marked, 83 and 80 | as marked, 90 and 82 |
| `phao nua lopia to thalo. shia manuwe neri to nai.` | the child's hand, 50 and 50 | the child's | split | the child's, 55 and 55 | the child's, 85 and 80 |
| `melu wei wheo ku shelu to loa. shia ku shelu to theo.` | the elder read it, 70 and 70 | the friend (`shia` by rule) | the elder, 60 and 55 | the friend, 68 and 62 | the friend, 60 and 62 |
| `thiku tupiwa mua whelina to meilo. waeshi tupiwa wea shia to shua. shia to pa rotiku.` | the wild rabbit danced, 50 and 50 | the small rabbit | split | the small rabbit, 72 and 60 | the small rabbit, 55 and 58 |
| `ne manoe ku ne tiloa to naphe. shia shorui to nai. shia to nulae.` | Manoe was weary and slept, 45 and 45 | Tiloa, both | split | Tiloa, 85 and 78 | Tiloa, 65 and 75 |
| `wheo ku lopia to hea. melu ku shia to naphe.` | a friend helped the child, 55 and 55 | the elder (`shia` by rule) | the child, 50 and 50 | the elder, 70 and 65 | the elder, 70 and 65 |
| the *Velveteen Rabbit* line: `... shia roa shia to pa rato. shia to pa rotiku.` | the wild rabbit circled Tupiwa and danced, 45 and 40 | the same | the same, 55 and 60 | the same, 68 and 60 | the same, 70 and 70 |
| `phao ku melu to hea. mua womu to manolu.` (subject unsaid) | the parent stayed, 70 and 75 | the friend | split | the friend, 82 and 76 | the friend, 88 and 80 |

What stands out.

- **Unmarked, readers choose by the scene.** The receiver laughs, the finder rejoices, the one asked sets off. No rule is in use. Every reader listed the other assignment as open, and one wrote that an overt `shia` where the subject could have gone unsaid "may even hint at a switch".
- **The unsaid subject is the firmest thing Phi has.** It drew the highest unmarked confidence (70% and 75%), both readers taking it as the same subject continued.
- **Lone `ra` has a meaning already, and it points the other way.** With today's entries one reader took `ra` as the other one. The other took it as "the farther-back one in the discourse", the first-mentioned person, which is what the entry's own words ("an earlier matter in the discourse") suggest. They agreed on one passage in eight, and confidence fell below the unmarked packet.
- **Lone `ha` was read against the proposed convention by both.** The assessment would have `ha` resume the current topic. Both uninstructed readers took it as the nearest-mentioned person, the latter of two.
- **Taught, both devices work.** A three-sentence convention was enough for twelve of twelve from both readers in either form.
- **They differ where a noun follows.** In the two passages where the marker stands directly before nominal material (`ra ru siora`, `ra manuwe`), the lone deictic drew 58% and both readers wrote that "that great joy" and "that hand" are the parses the grammar favours. The pronoun drew 81% in the same two. In the six passages where a particle or preposition follows, the two forms were level at 76%.
- **A rule for plain `shia` is followed but not trusted.** In the four passages that relied on "`shia` stays with the last subject" and no marker, readers obeyed (66%) and each said the scene pulled the other way.
- **My draft rule had a hole, and four readers found it.** In the rabbit passage, "not the subject of the sentence before" gives the small rabbit, while "not the one `shia` now stands for" gives the wild rabbit, because the sentence before has `shia` as its object. A ruling must pick one anchor. See point 3.

## 4. The options

### A. Teach what exists and add nothing

Name or rename at each change of subject. Use `miso` for the subject's own. Leave the subject unsaid when it continues, and say so in the manual as a convention: an unsaid subject is the subject of the sentence before. For two of a kind, `ha` and `ra` before the noun (`ra tupiwa`).

- No inventory cost. All of it can be written today, and the unsaid subject already reads firmly.
- It is what the texts do now. The price is the 77 namings in one story where the source has a pronoun, and the texture that the assessment's reviewers noticed.
- It would have repaired the misread line: `waeshi tupiwa roa thiku ne tupiwa to pa rato`.

### B. Lone `ha` and `ra` as this one and the other

The assessment's recommendation 15. No new word.

- Works when taught: twelve of twelve.
- Untaught it misleads. `ra` is read as the former as readily as the other, and `ha` as the latter. A convention here does not fill an empty place; it overrides what the words already say.
- Lone `ha` has a job: 91 uses on the shelf as "this matter". Every one would become a choice between the matter and a person. `ra` is free of that; a system of plain `shia` and lone `ra` would not need `ha` at all.
- It fails before a noun, by structure. A deictic directly before nominal material is a determiner first. 355 of 943 singular `shia` on the texts shelf (38%) stand directly before a noun, an adjective, a quantity, or `lo`, which is every possessor and many subjects. `ra manuwe` is "that hand" before it is "the other's hand". `ku` rescues a subject (`ra ku lopia to nila`) and nothing rescues a possessor.
- The parser needs the four repairs listed in section 2 either way.

### C. A second third-person pronoun (recommended)

A fourth core pronoun, in the relator shape of `mia thia shia`, for the other one. It takes every position `shia` takes, takes `lo` for the plural, and marks no gender, number, or kind.

With the placeholder `ria`:

| Phi | Reading |
|---|---|
| `ne samira ku ne timothi to nila. ria to seniku.` | Samira saw Timothi. Timothi smiled. |
| `phao nua lopia to thalo. ria manuwe neri to nai.` | The parent walked with the child. The child's hand was cool. |
| `waeshi tupiwa sha ... sho to haolu. shia roa ria to pa rato. shia to pa rotiku.` | The wild rabbit circled Tupiwa and danced. |

- Read as marked in twelve of twelve by both readers, at the highest confidence of the four packets, with no weak position: before a noun it is a possessor exactly as `shia` is.
- It has no earlier meaning to teach against.
- With `miso` and the unsaid subject it completes a small set, each anchored to a subject: `miso` is this clause's subject; an unsaid subject is the last sentence's subject; the new word is not the last sentence's subject; `shia` stays unmarked.
- **Reach.** Of the 93 contested singular uses in the translations, 80 have exactly two rivals, where one word for the other settles the choice. It does nothing for three or more; there a name is still needed.
- **Costs.** A closed class reopens, for the first new core pronoun the language has taken. One more word for a learner in the first week. And a matter of stance: a word for "the other" could be heard as ranking one person behind another. What it marks is position in the telling, not kind or worth, and it passes to whoever was not last the subject; the gloss label should say that and avoid a word like "outsider".

### D. An animate and inanimate split of `shia`

Raised for completeness. Not recommended.

- It would settle at most the 107 singular uses where one person or animal stands against things, and none of the 93 where two people or animals stand against each other, which is where the misreading was.
- It sorts the world into persons and things at every mention. The texts where reference is hardest are the ones where that line is the story's subject: a toy rabbit that becomes real, a Sun and a Wind that argue, Love as "he" in Gibran, the Way.
- It runs against the manual's own sentence about `shia`, and against the pillar that asks Phi to keep animacy open.

### E. A rule for plain `shia`

That `shia` always stays with the last subject. Tested as part of the two taught packets.

- Readers followed it at 66% while saying the scene disagreed.
- It would silently change the reading of existing text. In five of the twelve unmarked passages both readers took `shia` as someone other than the last subject, and the shelf is written the same way.
- Not recommended as a rule. If C or B is adopted, the marked word carries the convention and plain `shia` can stay as it is: wherever the other was available and not said, the listener leans to the one being followed.

## 5. Points to rule on

Revised the same day on the maintainer's instruction to settle the obvious points and ask only what cannot be decided without him. Points 1 and 2 are his: the first reopens a closed class and the second is a matter of ear. Points 3 to 8 are settled as recommended below and will be flagged as judgement calls in the pull request.

**Point 1. Which option, and whether the bar for an amendment is met.** Recommended: **C**, with everything in A taught beside it. The honest state of the showing: existing grammar can always resolve this by naming, so the relation is expressible without structural ambiguity, and the boundary test in canon is met less clearly than it was for `ku`. The verified misreading is one line. The case for C is that the assessment's cheaper remedy (B) reads backwards untaught and breaks before a noun in 38% of positions, and that the remedy which works today costs a long narrative its pronouns. A alone is a defensible ruling. B is the one I would rule out.

**Point 2. The form, if C.** Seven hiatus disyllables in the `-ia` rhyme are free. The word will stand where `mia`, `thia`, and `shia` stand.

| Form | Nearest words | English echo | Note |
|---|---|---|---|
| `hia` | `ha`, `hi`, `hea` (hear) | "hear", "here" in some accents | Its rivals differ by a whole vowel, which hiatus keeps audible. Lone `ha` stands in the same positions. |
| `ria` | `ra`, `lia` (yes), `roa` | none common | Easy to remember beside `ra`. Against `lia` it rests on `l` and `r`, and both open sentences: `ria to seniku` beside `lia. to seniku` (yes, they smiled). |
| `pia` | `pi`, `pa`, `pio`, `mia` | the name Pia | `pi` also opens sentences. `p` against `m` separates it from "I". |
| `phia` | `thia`, `shia`, `phea` | faintly "fear" | Would differ from "you" only in `ph` against `th`. |
| `sia` | `shia`, `sio`, `sua` | "see a" | One fricative from `shia` in the same position. Not advised. |
| `tia` | `thia`, `tua` (no) | "tea" | One fricative from `thia`. Not advised. |
| `whia` | `wia` | | Barred: `wh` against `w` would be the only difference from `wia`. |

`ria` was the placeholder in the test. Each of the first four has one mark against it; my lean is `hia`. The form is for the maintainer's ear, and a form outside the rhyme is open too, as `miso` and `wiso` show.

**Point 3. What it is the other of, if C or B.** The readers found two anchors in my draft. Recommended: **the subject of the sentence before**, and within one clause, the subject of that clause. It is the anchor readers already trust (the unsaid subject), it matches `miso`, and a tool can check it. The alternative, "whoever `shia` last stood for", needs the listener to carry a referent across sentences. In the one passage where the two came apart, all four taught readers named the conflict, and it was the pronoun packet's lowest confidence (55% and 58%). Under the recommended anchor, once the new word has been a subject, the next unsaid subject or `shia` continues that one.

**Point 4. Plain `shia`.** Recommended: no new rule. `shia` stays unmarked and leans on context, as now.

**Point 5. The unsaid subject.** Recommended: state in the manual what readers already do, that an unsaid subject is the subject of the sentence before, and teach it as the way to say "the same one went on". No inventory change.

**Point 6. Lone `ha` and `ra`.** Recommended: leave them meaning this and that, mostly of things and matters, and do not load them with persons. Repair the four parser gaps in section 2 in the pull request that follows this sheet, since canon already licenses those sentences. Teach `ha` or `ra` before a repeated noun for two of a kind.

**Point 7. Gloss label and name, if C.** Recommended: a label that says position, such as `3ALT`, with the entry describing "the other of two third persons in the telling".

**Point 8. Whether the texts must use it.** Recommended: no rule, as with `ku`. Certification can let the source-blind reader's doubts decide where it is needed.

## 6. What follows the rulings

If C: one pull request under the amendment checklist. Canon bullet and the shape charter's pronoun count; the entry; the pronoun chapter of the manual (the new word, the unsaid-subject convention, and the set of four); the parser (the word in every position `shia` takes, the lone-deictic repairs) with tests; `ReferenceTracker`, so the ledger stops counting a marked use as contested; the finder pages; the decision record. Then a confirmation packet built from the real entry. No text changes. The primer and pamphlets wait, as agreed.

If A alone: the manual section, the parser repairs, and a row in `project/deferred_questions.md` recording that a second pronoun was weighed and declined.

## Appendix: limits of the evidence

- The reading test is eight model readers, two per packet, on twelve invented passages built to be reversible. Real text is less evenly balanced. One reader recognized the *Velveteen Rabbit* scene and said so.
- The marked packets tested a stated convention. They show that it can be learned from a few sentences, not that an untaught listener would arrive at it.
- The count of 93 rests on my hand list of nouns and names for people and animals and on the tracker's three-sentence window. It does not know who a given `shia` is.
- The 77 namings in *The Velveteen Rabbit* come from a word match between each Phi name and its English name on the same source line.
- The 29, 5, 3, and 1 for clauses with two `shia` are my reading of each against its source line.

## Addendum: does a second pronoun reduce forced naming?

Written after the maintainer's conditional ruling on point 1.

**A count.** *The Velveteen Rabbit* names a character 75 times where the source line has no name for that character. Sorted by where the name stands and who was subject just before: 41 stand where the rule would let `hia` stand (31 not the subject of their own clause, with someone else as subject; 10 a subject after a sentence with a different third-person subject), 11 where the subject before was the same person, so that `shia` or an unsaid subject would do, and 23 in other positions, many of them the subject's own (`ne woru roe ne woru theko wethalu`, with her own apron), which is `miso`. The count is mechanical and does not know whether a third person is also in play.

**A reading test on real text.** Three stretches of the story (the Fairy and the Rabbit, the wild rabbit, the sickbed) were each set three ways and given to two fresh readers per version, who resolved every pronoun and unsaid subject to a participant. `miso` was used for the subject's own in all three versions, since D128 already rules it.

| Version | Names said | Every assignment as in the source | Mean confidence |
|---|---:|---|---:|
| Named, as a careful writer names today | 22 | both readers | 76% |
| Names stripped to bare `shia` wherever the source has a pronoun | 11 | both readers | 73% |
| Stripped, with `hia`, `miso`, and an unsaid subject by rule | 11 | both readers | 79% |

Every reader of every version got every assignment right. The version with `hia` carried half the names and read at least as well as the named one. The version with bare `shia` also survived: with `miso` available the readers ruled out self-reference in so many words, and the story carried the rest. Its readers listed more open assignments (three unmarked `shia` in one sentence, a direction that "could be reversed") where the readers of the `hia` version called the same places fixed.

**What this shows.** A good part of the naming in these stretches was caution, and can go without any new word now that `miso` exists. `hia` replaces the names that are forced in the strict sense, between two evenly matched people where the scene does not decide. That is the case section 3 tested, where bare `shia` was chosen by plausibility at 56% and the second pronoun was read as marked in twelve of twelve. The condition is met, narrowly, and D135 says so.

**Limits.** Six model readers, three passages, one story, and passages short enough that a reader can hold everyone in mind. One clause in the wild-rabbit passage (`shia laeno menoa whila wuloe wetha ne tupiwa shonui to moli palo`) was flagged by five of six readers as two bare phrases with no edge between them, which is a seam and not a matter of reference.

## Addendum: confirmation read

After the entry was written, a packet built from the real entries went to two more fresh readers: the twelve passages of section 3, with `hia` where the other one was meant and an unsaid subject where the same one went on. Plain `shia` carries no rule in the entries, so no passage relied on one. Both readers gave all twelve the intended reading, at a mean confidence of 77%. The nine passages with `hia` averaged 81%. The three that relied on an unsaid subject against the pull of the scene (the giver laughs, the asker sets off, the giver reads the book) averaged 62%: both readers followed the convention and both said the scene argued the other way. Both also pointed out that the entry had not said how `hia` reads as the possessor inside a subject phrase (`hia manuwe neri to nai`); the entry, canon, and the manual now say that it looks to the sentence before, as a subject does.
