# Roles and valency: study and rulings sheet

Date: 2026-11-24. Measured on main at `7efccfb0`, lexicon at 1,308 entries, with the instruments merged in #729 to #731, before the ruling was implemented. This is the sheet the maintainer read, kept as written, with an addendum for what the implementation found. Following his instruction that sheets settle the obvious points and ask only what cannot be decided without him, eight points were settled on the evidence (section 3) and one was put to him (section 4). He ruled for the rule: a lone bare phrase before a verb is its subject, and an object standing alone takes `ku`. Decision D136 records the result, and the rules live in `/canon.md`.

Scope: the third structural exposure, after seams (`ku`, D134) and reference (`hia`, D135). The November assessment's section 4.8 says "verbs do not show their valency" and recommendation 27 asks for a valency field. Behind it is the open role: Phi marks no case and lets a subject or an object go unsaid, so one bare phrase before a verb that takes an object may be either.

One point is put to the maintainer, in section 4. The rest are settled on the evidence and listed in section 3, to be flagged as judgement calls in the pull request.

## 1. What is there now

**The entries.** All 367 verb entries have usage notes, and that is where valency lives. A pattern search finds a plain statement in 219 of them: 172 say transitive or name a direct object, 34 say intransitive or that an object needs `ka`, and 13 say both. The other 148 leave it to the examples. The notes also disagree in kind: `thape` (burn), `helui` (change), and `rato` (turn) let the affected thing stand alone as subject or be the object of whoever acts, while `pukate` (break), `wilanu` (dissolve), and `thuroa` (grow) are intransitive and take `ka` for the one who causes it.

**The corpus.** It shows 154 verbs with an object at least once. The role counter uses that list today, which is a stopgap: a verb that happens never to have taken an object in a text is treated as if it cannot.

**The open role, measured.** On the texts shelf 214 main or dependent clauses have one bare phrase before a verb the corpus shows with an object.

| Head of the lone phrase | Clauses |
|---|---:|
| `mia` or `thia` | 76 |
| `shia` | 46 |
| a name | 19 |
| a noun | 69 |
| a quotation or complement frame | 3 |
| other | 1 |

Read one by one against their English, the lone phrase is the subject in all but about five: `wethalu lomare` (having dressed), `serao miona ma thumela` (not teach old people), `wisola lokue thela thiranu` (how to keep an exchange-place), `sheloi thena po phelu` (can hold many things), `mioru nai menoa nila` (sees a face). The three frames are speeches whose speaker is unsaid, which D128 licenses. Outside the texts, about 270 more clauses have the same shape; 207 open with `mia` or `thia`, and none of the others I read is a lone object.

The one verified misreading of this kind went the other way. In the certified *Velveteen Rabbit*, `shia tha lo phirae tupiwa so ma nila tho to soliru` means it hoped the other rabbits would not notice; the source-blind English has "it would not see the other rabbits". A lone subject was taken for an object.

**Relative clauses are different.** Of 38 relative clauses with one phrase inside and an object-taking verb, the phrase is the subject in about 26 (`whu mia sano luphore`, the river I know) and the object in about 12 (`whu shelu kealo miona`, people who make books). Both are everyday shapes.

## 2. What readers do with a lone phrase

Eight short passages put one bare phrase before a verb that takes an object, in a context where either role makes sense (`telo sio luphore to thalo. lohau to hekawi.`: the farmer walked beside the river, then the dog found, or was found). One is the *Velveteen Rabbit* line with a neutral subject. Two fresh readers saw them with today's grammar. Two others saw a version with one sentence added to the grammar notes, "A single bare phrase before a verb is that verb's subject. An object that stands alone, with its subject left unsaid, is opened by `ku`", and with `ku` placed on four of the eight.

| Packet | Reading | Mean confidence |
|---|---|---:|
| Today's grammar | lone phrase taken as subject in 14 of 16; the two readers agreed on 6 of 8 | 54% |
| Rule stated | 16 of 16 as the rule says | 79% |
| of which a lone object opened by `ku` | 8 of 8 | 90% |
| of which a bare lone phrase, subject by rule | 8 of 8 | 68% |

- Readers already lean to the subject. Without a rule they chose it fourteen times in sixteen, and one of them wrote that "the file gives nothing that decides between them; my first readings rest on plausibility only".
- The rule turns a lean into a reading. Confidence on the bare phrase rose from 54% to 68%, and both ruled readers said of the object reading that the notes "exclude it".
- Where the scene argues for the object (the farmer finds the dog, the child sees the frog), the ruled readers still followed the rule, at 60% to 72%, and said the writer "may have meant" the other. A writer who means the object writes `ku`, and that is read at 90%.

## 3. Settled on the evidence

These go into the pull request as judgement calls.

1. **A `valency` field on every verb entry**, required by the schema for verbs and refused elsewhere. It sits in the entry's structured head, beside `pos`.
2. **Four values.** `intransitive`: one participant, the subject, and an object needs `ka`. `transitive`: a subject and an object, where the object may go unsaid. `both`: the affected thing stands alone as subject or is the object of whoever acts on it. `complement`: `nai` and `kelu`, which take a complement and never an object. The words transitive and intransitive are already what the usage notes use.
3. **Classification follows each entry's own note, then its examples and the corpus.** No verb changes what it does. Where a note and the corpus disagree, the pull request lists the verb and which was followed. The 148 entries that do not say are classified from their examples and sense, and each of those is listed too.
4. **Which verbs are `both` stays a fact about each verb**, as recorded. Making every change-of-state verb work one way would rewrite entries and text for no gain in reading: with a `both` verb the lone phrase is the affected thing either way.
5. **The role counter reads the field** instead of the corpus-derived list.
6. **The parser advises and does not reject.** `ku` or passive `se` on an intransitive verb, and two bare argument phrases before one, become an advisory in the review ledger. They become errors only after the ledger has been read and is clean.
7. **Complement clauses and recipients are not encoded now.** Which verbs take a `tha` frame or a `wei` phrase stays in the notes. A second field can follow if the first earns its keep.
8. **Usage notes keep their sentences.** The field is added beside them, and a note is edited only where it contradicts the value.

## 4. The point to rule on

**Should a lone bare phrase before a verb be its subject by rule?**

Stated in full: in a main or dependent clause, one bare phrase before the verb is the subject. An object that stands alone, with its subject unsaid, is opened by `ku`. A quotation or complement frame is exempt, since it cannot be taken for a subject. Relative clauses are exempt: the head noun is one of the two parties there, both shapes are common, and `ku` stays optional as canon has it.

For it:

- It is what readers already do fourteen times in sixteen, and what the texts already do in all but about five clauses of 214.
- Stated, it lifts the bare phrase from 54% to 68% and gives the marked object 90%.
- It closes the open role in main and dependent clauses outright, by rule and not by count.
- It would have settled the misread *Velveteen Rabbit* line.
- The cost on the shelf is `ku` in about five clauses.

Against it:

- Canon says of `ku`, as ruled today, that "it is never required: the unmarked clause is the resting state." This makes it required in one configuration. The bullet would be amended to say that `ku` is optional wherever a subject is said, and needed when an object stands alone.
- A learner's first object-only sentences, in answer to a question or in a list of chores, would need the particle.
- The parser cannot enforce it, since it cannot know which role was meant. It would be a reading rule that texts and certification apply.

The alternative is to teach the lean without ruling it: say in the manual that a lone phrase is most naturally the subject and that `ku` is there for an object. That changes no canon and leaves the open role as an exposure the ledger keeps counting.

Recommended: the rule.

## 5. What follows

One pull request: the schema and its test, the field on 367 entries, the generated reference pages (the field shown in the explorer and the part-of-speech listing), the role counter and the advisory, the manual's page on verbs with a short section on what the three values mean for a learner, the decision record, and this study archived. If the rule is adopted: the canon bullet for `ku` amended, a canon bullet for the lone phrase, the manual's sentence page, and the five text lines added to the reference-sweep entry in the deferred ledger. No text changes.

## Appendix: limits

- The reading test is four model readers on eight invented passages built so that either role makes sense. Real text usually favors one.
- The counts of subject and object among the 214 clauses, and among the 38 relative clauses, are my reading of each against its derived English or source. A few of the 214 are clauses where the counter saw one bare phrase and a human would see a prepositional phrase and an object.
- The pattern search over usage notes is crude. It undercounts entries that state valency in other words, which is why the classification will be done by reading each entry.

## Addendum: what the classification found

Written after the field was added to all 367 verb entries.

**The notes say more than the pattern search found.** Four fresh readers each classified a quarter of the verbs from the entry's own prose, examples, and corpus counts. They found the valency stated in the entry's notes for 354 verbs and had to rely on the examples for 13 (`kelai`, `meropi`, `mupelo`, `nolami`, `nurima`, `pheru`, `rashelo`, `selu`, `shorai`, `therilu`, `thole`, `warosha`, `whano`). Section 1's figure of 148 entries that "leave it to the examples" measured the crudeness of the search and not the entries.

**The result.** 258 transitive, 92 intransitive, 15 both, 2 complement (`nai`, `kelu`). The fifteen that work both ways: `helui`, `hinolu`, `koluma`, `moluki`, `phae`, `pisha`, `rato`, `sewaro`, `sholei`, `sunoe`, `thape`, `theala`, `therapi`, `thiwera`, `welura`.

**Calls made against a reader or a note.** Forty-one verbs were flagged, by a reader's low confidence or by disagreement with the pattern search or the corpus, and each was read again. Four reader calls were changed. `phae` (open) became `both`: its note called it transitive, but the certified *Velveteen Rabbit* has `phirali ... to phae` (the blossom opened) and the note itself mentions a resulting open state, so the note was amended to say both. `pheru` (endure), `shorai` (commune), and `thole` (practice) became transitive, because each note says the verb "may stand alone" or "without an object" when something is understood, which is how the entries of plainly transitive verbs speak. `peshu` (lie) stays intransitive on its note's plain word, although the same note lets a quotation or a `tha` frame stand before it.

**What the corpus check found.** No sentence in the corpus puts `ku` or a passive on a verb entered as intransitive, so the new advisory `PHL006` begins empty. Three text lines give an intransitive verb a bare object against its own entry: `shia mia lo haolu to la therua hasi` (`hasi` takes `wei`), `ne kulo lo kalora tiwa to roke` (`roke` takes `ka`), and `lo thilou lonae` twice (`lonae` takes `wei`). All are in uncertified chapters of *News from Nowhere* and are listed for the sweep.

**Coordination, which the sheet missed.** The count of "about five" lone objects in section 1 left out clauses after `nela`, `thona`, or `sola`. Looked at separately, the corpus has seventeen such clauses with one bare phrase before a transitive verb: the phrase is an object sharing the earlier subject in about six (`mia hasumi ma milau thona phialu milau`, the example D130 ruled for instead) and a new subject in about four (`mia theo nela thia sheluo`), with the rest two-phrase clauses the counter saw as one. That is the mixed picture relative clauses show, so a coordinated clause is treated the same way: outside the rule, with `ku` optional. Under that reading three lone objects on the shelf need `ku`, and five more stand after a coordinator and need judging line by line. The maintainer ruled without this case in front of him, and the pull request flags it first.

**No confirmation read was run.** The rule's wording in canon is the sentence the four readers of section 2 were given, and no entry carries it except the one line added to `ku`.
