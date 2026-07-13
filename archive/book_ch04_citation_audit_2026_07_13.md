# Citation audit: *Announce, then deliver*

Audit date: 13 July 2026

## Scope and method

This audit covers every reference in `book/04_announce_then_deliver.md` as merged in PR #303, along with each quotation, number, study description, and conclusion that depends on a source. I followed the references to publication records or full texts, read past the abstracts into the methods and results, checked the Phi passages against their repository sources, and ran the repository example validator. The chapter itself was not edited.

Line numbers below refer to the merged chapter on 13 July 2026. I use four labels: **verified** means the cited source supports the claim as written; **qualified** means the source supports a narrower version; **needs another source** means the claim may be sound but the present citation does not establish it; **unsupported** means the available evidence does not justify the wording.

## Overall finding

All five works in the reference list are genuine, the authors are correctly named, and the publication details are substantially accurate. The direct quotations from Gibran, Slobin, Goldin-Meadow and colleagues, and Özçalışkan and colleagues match their sources. There is no fabricated citation here. The chisel survives the audit.

The trouble begins after the quotations. Results from small, bounded studies become claims about a lifetime, every speaker, and the wordless mind. The 2008 experiment found a strong shared preference in two tasks; it did not find a categorical order in every response. The 2016 experiment found convergence in the predominant silent-gesture patterns; small language-group differences remained, and the authors said that one of them might reflect English. Later pantomime work also shows that the kind of event can change the preferred order. The phrase "everyone's wordless default" is too large for this evidence.

A second gap opens between first-language development and Phi. Slobin's work concerns habits acquired with a native language from childhood, and he explicitly says those habits resist restructuring in adult second-language learning. That evidence supports a restrained account of thinking for speaking. It does not establish that adult learners of Phi will acquire the proposed attentional routine, much less that repeated Phi use will change them. The proposed outcome belongs in the chapter as a design hypothesis, not an observed mechanism.

The central argument can remain. Phi orders relations before the heads they modify, and speakers must produce the words in that order. That is a fact about utterance structure. The evidence also permits a careful comparison with native-language thinking for speaking and with silent-gesture preferences. Line 59 already gives the right epistemic limit: repeated performance is not proof that the performer changes. The earlier sections should keep the same limit.

## Priority corrections

| Priority | Location | Finding | Required repair |
| --- | --- | --- | --- |
| High | Lines 47, 51, 53, and 57 | The 2008 results become categorical and universal: "every group ... produced one order," Phi "will not" affect nonverbal event representation, actor-patient-act is "everyone's wordless default," and the studies "close that door." | Report the observed preferences and task limits. Replace universal conclusions with what these studies found in their samples. |
| High | Lines 49 to 51 | The 2016 study is summarized as if all language effects vanished from silent gesture. Small but statistically detectable group differences remained in rare response types, and co-speech gesture order was too sparse for a firm comparison. | Say that the predominant packaging and ordering patterns converged. Separate the stronger packaging result from the weak co-speech ordering evidence. |
| High | Lines 39 to 41 and 57 | Findings about native-language habits acquired in childhood are transferred to adult Phi learners without evidence. Slobin's own second-language observation makes this transfer uncertain. | Present Phi's proposed effect as a hypothesis to test. Distinguish required word sequence from any claimed change in attention. |
| High | Line 31 | Dryer 2013, chapter 81, does not support the claim about OV languages and adpositions. | Add Dryer 2013, chapter 95. Its sample has 472 OV and postpositional languages, 14 OV and prepositional languages, and 158 languages outside the four principal combinations. |
| Medium | Line 29 | The WALS numbers are correct, but "largest survey" is unsourced and "two of every five languages on earth" treats a typological sample as a census. | Say "In the WALS sample, 564 of 1,376 languages..." Remove the superlative unless a source and comparison set are supplied. |
| Medium | Line 37 | The chapter attributes the whole frog-story corpus and method to Slobin 1996. That chapter is a synthesis; the underlying study is Berman and Slobin 1994. | Add Berman and Slobin 1994, and describe the project as a five-language corpus. |
| Medium | Line 37 | "The pattern was not a habit of age or schooling" states more causation than an age comparison can show. | Say that language-specific patterns appeared from the youngest sampled ages and continued into adulthood. |
| Medium | Line 31 | The Japanese and Turkish word-order claims are broadly right but uncited and too casual about what movement does. | Add language-specific sources or say only that both languages permit discourse-governed alternatives to their dominant SOV order. |
| Medium | Line 41 | "The whole condition must be composed" sounds like a claim about advance mental planning. The grammar establishes utterance order, not how much of a clause must be planned before speech begins. | Use "uttered" or "heard" instead of "composed," unless psycholinguistic evidence is added. |
| Low | Lines 65 to 73 | The bibliography identifies the works but omits DOI links, live URLs, and the source most directly responsible for the frog corpus. | Replace bare web text with linked references, add both DOIs, and add Berman and Slobin 1994 plus Dryer chapter 95. |

## Passage-by-passage audit

### The chisel, the rule, and the local source trail, lines 3 to 25

#### Verified

The chisel example is reproduced exactly from [`short_road.md`](short_road.md), and `canon.md` gives the same sentence as the model for S PP O V order. The lexical forms and glosses pass `python3 scripts/validate_examples.py`; the validator reported 1,168 entries checked with zero errors and zero warnings.

The statement that whatever modifies, specifies, or relates comes before what it affects is also reproduced faithfully from `short_road.md`. The manual's chapter on the modifier-first principle and `documents/modifier_first_philosophy.md` give the fuller account named in the final source note. The adjective, possessor, preposition, interrogative, and dependent-clause examples are consistent with those sources.

The Gibran passage at lines 18 to 20 is copied exactly from [`texts/prophet_excerpts.md`](texts/prophet_excerpts.md). Its source line corresponds to the sentence in the "On Giving" section of the [1923 Project Gutenberg text](https://www.gutenberg.org/files/58585/58585-h/58585-h.htm). [WorldCat's first-edition record](https://search.worldcat.org/title/283875) confirms Kahlil Gibran, New York, Alfred A. Knopf, and 1923. Calling the Phi line a rendering is correct.

The boatman sentence summarized at line 25 appears exactly in [`book/00_the_boatman.md`](book/00_the_boatman.md). That chapter supports the account of `mena`, `meno`, `to ho`, and the final verb `remo`.

#### Qualification worth preserving

"One structural rule" is the project's established shorthand for the ordering principle, not a claim that Phi has only one grammatical rule. `kia.md` states the distinction cleanly: learners still meet particles, clause frames, classifiers, conversion rules, and ternary numerals. Line 25 partly protects itself with "in one real sense," but "there is no other law to obey" can still be misread. If this passage is revised, keep "one organizing rule" or "one ordering rule." The short road itself moves directly from the one rule to thirty-five grammatical particles, so the source does not support a grammar with nothing else in it.

#### Interpretive prose, not an empirical finding

The claims that the verb "lands" in a complete scene and that the listener never has to "go back and repair" the condition are explanations of linear form. They work as literary descriptions. Reading them as findings about real-time comprehension would require processing evidence that is not cited here.

### Word-order typology, lines 27 to 33

#### Counts verified, scope overstated

[WALS chapter 81](https://wals.info/chapter/81) reports exactly 564 SOV languages out of 1,376, compared with 488 SVO, 95 VSO, 25 VOS, 11 OVS, 4 OSV, and 189 without a dominant order. SOV is the most frequent of the six dominant-order types in that sample. Japanese is WALS's own first SOV example. The ordinary classification of Turkish, Hindi, and Korean as SOV is sound.

WALS is not a census of every language. Chapter 81 describes a particular kind of transitive declarative clause with nominal subject and object, and its map records dominant order rather than every permitted order. The chapter itself warns that many languages with a dominant order are flexible. "Roughly two of every five languages in the WALS sample" is accurate. "Two of every five languages on earth" is an extrapolation.

"In the largest survey" is not supported by the cited chapter. It may be possible to defend WALS as one of the broadest standard typological samples, but a superlative needs a measure and a comparison set. The simplest repair is to name WALS rather than rank it.

#### The adposition claim needs Dryer chapter 95

[WALS chapter 95](https://wals.info/chapter/95), not chapter 81, carries the relevant comparison. It reports 472 languages with OV order and postpositions, 14 with OV order and prepositions, 42 with VO order and postpositions, 456 with VO order and prepositions, and 158 that do not fall into those four groups. Dryer calls OV with prepositions relatively uncommon and gives Persian and Tigre as examples. This strongly supports the description of Phi's combination as unusual.

"Mixed directionality" is a defensible explanatory label because the verb phrase is object-before-verb while the adpositional phrase is adposition-before-object. It is not Dryer's label in the cited chapter. For maximum precision, call Phi "OV and prepositional," then explain the mixed head direction in ordinary prose.

#### Japanese and Turkish need narrower wording

The claim that natural languages permit alternate orders is well founded. WALS explicitly distinguishes rigid and flexible systems and notes that pragmatic factors often govern the alternatives. [Satoshi Imamura's corpus study](https://ricl.aelinco.es/index.php/ricl/article/view/40) confirms both SOV and OSV in Japanese and links their distribution to information structure. Calling the Japanese alternative movement "for emphasis" is too vague: topic status and discourse continuity do more work than that phrase admits.

[F. Nihan Ketrez's Cambridge grammar chapter](https://www.cambridge.org/core/books/abs/student-grammar-of-turkish/word-order/BE1EF414A06CA27A2F1F96982B0F1927) describes Turkish as SOV with extensive case-supported word-order variation. Research on Turkish information structure likewise connects constituent position with topic and focus. "Reorders freely" should be "permits substantial reordering," since grammatical possibility does not make every order equally neutral in every context.

The final contrast with Phi is sound if it remains specific: Japanese and Turkish have discourse-governed alternatives, while Phi's canon does not. "Natural languages bend" sounds universal and is unnecessary. "Many natural languages bend" says what the evidence shows.

### The frog-story research, lines 35 to 41

#### Reference and quotations verified

Dan I. Slobin's chapter is correctly identified as "From 'thought and language' to 'thinking for speaking,'" pages 70 to 96 of *Rethinking Linguistic Relativity* (1996), edited by John J. Gumperz and Stephen C. Levinson. [Cambridge bibliographic records](https://books.google.com/books/about/Rethinking_Linguistic_Relativity.html?id=dPXvxgL2t1oC) confirm the volume, year, publisher, and page range. The quotations assigned to pages 76, 78, and 89 match the source. This check covered both descriptions of English and Spanish narrative tendencies and the warning about adult second-language restructuring.

The account of *Frog, Where Are You?* is substantially accurate. The project began around 1980, used the same wordless picture book, compared English, German, Spanish, Hebrew, and Turkish, and included children from age three through adults. The [publisher's record for Berman and Slobin 1994](https://www.routledge.com/Relating-Events-in-Narrative-A-Crosslinguistic-Developmental-Study/Berman-Slobin/p/book/9781138984912) describes more than 250 narratives across the five languages. That book, rather than Slobin's later synthesis alone, should be cited for the corpus and method.

The phrase "five countries" appears in Berman and Slobin's own methods discussion, so it is not invented. "Five language communities" is still the more useful description because the corpus is organized by language and the Spanish comparison drew on more than one national setting. This is a precision issue, not a substantive historical error.

#### The age conclusion needs one step less certainty

The source supports language-specific narrative patterns from the youngest groups onward. It does not isolate language from every cultural, educational, or elicitation effect. "The pattern was not a habit of age or schooling" treats a cross-sectional comparison as a causal test. A safer sentence would say that the preferences appeared in young children as well as adults, with development changing the sophistication of the narratives rather than erasing language-specific tendencies.

#### The transfer to Phi is untested

Slobin's thinking-for-speaking proposal is about the attention used to formulate utterances in a language. The chapter initially keeps that claim away from a stronger claim about general perception. Trouble arrives when the native-language finding is made to explain what adult Phi use "obliges" a speaker to attend to. No cited study tests Phi speakers, constructed-language learners, or an exceptionless modifier-first system learned after childhood.

Slobin's statement about resistance in adult second-language acquisition makes the proposed Phi effect less automatic, not more. An adult may learn to produce Phi's order while relying on established planning habits from another language. Repeated Phi composition may invite attention to dependency and relation, but that remains a prediction or practice goal until speakers are studied.

"The whole condition must be composed before its consequence can begin" also passes from word order into an untested planning claim. Phi requires the condition to be uttered before the consequence. Incremental speech production does not require a speaker to finish planning the entire first clause in silence before beginning it.

### Goldin-Meadow and colleagues 2008, lines 43 to 48

#### Bibliography and method verified

The citation is genuine and complete enough to identify the paper. The [open PNAS article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2453738/) gives the full title, the four authors, volume 105, issue 27, pages 9163 to 9168, and DOI [`10.1073/pnas.0710060105`](https://doi.org/10.1073/pnas.0710060105).

The two samples are reported accurately. Forty monolingual adults, ten each for English, Turkish, Spanish, and Mandarin Chinese, described 36 events in speech and then in silent gesture. A different forty adults, again ten per language, reconstructed the events with transparencies. The experimenter occupied herself with another task during the transparency trials, so the account of deliberate nonattention is faithful. The spoken-order summary is accurate too: English and Spanish favored actor-act-patient, Turkish favored actor-patient-act, and Mandarin differed between in-place and crossing-space transitive events.

The participants were urban university students tested in Chicago, Istanbul, Madrid, and Beijing. That sampling fact matters once the prose begins to say "everyone."

#### Preference is not categorical production

Across languages, 90 percent of 614 gesture strings and 81 percent of 1,423 transparency trials used actor-patient-act order. Those are strong results. They are not 100 percent. "Every group ... produced one order" should become "every group strongly preferred the same order" or give the percentages.

The quoted sentence from the abstract is accurate. In context, its result concerns the measured orders in these two tasks. It does not prove that a lifetime of language use has no effect on any nonverbal representation. The study is cross-sectional and has no before-and-after measure of a lifetime's influence.

The authors describe actor-patient-act as evidence for a natural order, but their discussion says they "speculate" that this sequence may reflect a natural way of representing events. That caution belongs in the book too. A result can be strong while its proposed cause remains open.

#### Later work narrows the "default"

[Hall, Mayberry, and Ferreira 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC4224279/) tested reversible events in elicited pantomime and found that SOV-like order drops when both participants are plausible agents, as in a woman pushing a boy. The paper also reviews similar results in Hebrew, Turkish, English, Japanese, and Korean. Event meaning therefore helps determine the order that silent gesturers prefer.

This later work does not erase the 2008 result. It gives it a boundary: actor-patient-act is a strong preference for the simple, mostly non-reversible events used there, not a single default that every wordless mind uses for every event. Line 53 should name that boundary or omit the universal conclusion.

#### "Unoccupied mind" is rhetoric, not method

Participants followed laboratory instructions. They watched prepared vignettes and consciously represented them by hand or transparency. The noncommunicative task removed an attentive addressee; it did not reveal an unoccupied mind. "With no grammar watching" and "the unoccupied mind" are attractive phrases, but they give the experiment a purity it did not claim.

### Özçalışkan, Lucero, and Goldin-Meadow 2016, lines 49 to 51

#### Bibliography and central comparison verified

The [open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4724526/) confirms the authors, title, *Cognition* volume 148, pages 10 to 18, and DOI [`10.1016/j.cognition.2015.12.001`](https://doi.org/10.1016/j.cognition.2015.12.001). The study used 40 adults, 20 native English speakers and 20 native Turkish speakers, who described 12 physical-motion scenes in speech with natural hand use and then in silent gesture. The abstract quotation is exact.

The study found the expected language differences in speech and co-speech gesture and did not find those same predominant patterns in silent gesture. Both groups mainly conflated manner and path in silent gesture, and both mainly ordered figure-ground-motion. This convergence supports the narrower point that silent gesture did not simply copy each group's spoken pattern.

#### "The difference vanished" is too neat

Small group differences remained. English speakers produced more of the rare separated silent gestures than Turkish speakers, and more of the rare figure-motion-ground order. Both effects were statistically detectable. The authors note that the ordering difference might reflect an influence of English. Their abstract's word "identical" describes the shared predominant organization, not literal identity across every response category.

The study also says that most co-speech gestures were single gestures and could not be analyzed for element order. The few Turkish multi-gesture strings resembled Turkish speech, while the English strings did not clearly resemble English speech; the authors say the numbers were too small for a conclusion. It is fair to say that co-speech gesture packaging differed by language. The ordering evidence cannot carry the same confidence.

All participants completed the speech condition before silent gesture. The authors chose that fixed order because silent gesture first might have changed natural co-speech gesture. This design choice is reasonable and disclosed, but it means condition order was not counterbalanced.

The paper itself treats a default conceptual order as one possible explanation and says it should be tested in infants who have not yet learned a language. "Take speech away and the shaping leaves with it" turns that possibility into a law. "In these tasks, the predominant language-specific patterns did not carry over into silent gesture" is supported.

### The closing argument, lines 51 to 61

#### Claims that exceed the studies

"A lifetime under the chisel sentence's order will not restructure" is unsupported. No participant had a lifetime of Phi exposure, no study manipulated long-term exposure, and neither paper proves the impossibility of an effect. The studies found little or no carryover from particular native-language patterns in particular nonverbal tasks.

"The gesture studies close that door" has the same problem. They narrow a claim; they do not close every route by which language experience might affect a nonverbal task. The later pantomime literature shows why open wording matters: preferences shift with event reversibility, production demands, and communicative conditions.

"The frog stories show grammars doing exactly that to their speakers, from early childhood, durably" is valid for language-specific thinking-for-speaking habits in the studied native languages. It does not demonstrate the proposed rehearsal effect in adult Phi users. The sentence should keep the native-language result and mark the Phi comparison as an inference.

#### Claims the chapter can keep

Phi's linear order does structure the act of speaking Phi. Relations and dependents are pronounced before the heads they affect, and the verb comes after its arguments in an ordinary transitive clause. A speaker repeats that sequence whenever the relevant construction occurs. None of this requires a claim about rewiring.

The rehearsal metaphor also works if it names deliberate practice rather than an experimentally established cognitive effect. Line 59 is the model: the chapter admits that repetition does not prove change and confines certainty to the structure of the performance. Bringing lines 51, 53, and 57 into agreement with line 59 would leave a more credible chapter and a more interesting open question.

## Reference ledger

| Reference as listed | Identity check | Support check | Bibliographic action |
| --- | --- | --- | --- |
| Dryer 2013, chapter 81 | Verified at [WALS Online](https://wals.info/chapter/81). The counts in line 29 are exact. | Supports SOV frequency, Japanese as an example, and the distinction between dominant and permitted orders. It does not support the adposition counts or the "largest survey" claim. | Keep it, add a live link and access date, and describe the 1,376-language set as the WALS sample. |
| Gibran 1923 | Verified through the [1923 text](https://www.gutenberg.org/files/58585/58585-h/58585-h.htm) and [WorldCat](https://search.worldcat.org/title/283875). | Supports the source sentence behind the Phi rendering. | Name the section "On Giving" and add a stable link. Page numbers vary by edition. |
| Goldin-Meadow et al. 2008 | Verified in [PNAS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2453738/). Authors, year, journal, volume, issue, and pages are correct. | Strong support for a shared predominant order in the two studied nonverbal tasks. It does not support universal claims about every response, every event, every person, or lifelong Phi exposure. | Add DOI `10.1073/pnas.0710060105` and retain the task and sample limits in the prose. |
| Özçalışkan, Lucero, and Goldin-Meadow 2016 | Verified in [Cognition/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4724526/). Authors, year, volume, and pages are correct. | Supports convergence in predominant silent-gesture packaging and order. Small group differences remained, and co-speech gesture order was too sparse for a firm conclusion. | Add DOI `10.1016/j.cognition.2015.12.001` and qualify the summary. |
| Slobin 1996 | Verified through the book record and indexed full text. Author, chapter title, editors, pages, place, and publisher are correct. | Supports thinking for speaking, the quoted motion-description contrasts, early native-language patterns, and resistance in adult L2 acquisition. It does not show that Phi causes the proposed attentional practice. | Keep it and add a stable book or chapter link. Add Berman and Slobin 1994 for corpus details. |

## Sources to add

1. Dryer, Matthew S. 2013. "Relationship between the Order of Object and Verb and the Order of Adposition and Noun Phrase." In *The World Atlas of Language Structures Online*, edited by Matthew S. Dryer and Martin Haspelmath. [WALS chapter 95](https://wals.info/chapter/95). This is the missing source for the OV and preposition comparison.
2. Berman, Ruth A., and Dan Isaac Slobin, eds. 1994. *Relating Events in Narrative: A Crosslinguistic Developmental Study*. Hillsdale, NJ: Lawrence Erlbaum Associates. [Publisher record](https://www.routledge.com/Relating-Events-in-Narrative-A-Crosslinguistic-Developmental-Study/Berman-Slobin/p/book/9781138984912). This is the direct source for the five-language frog corpus, its ages, and its methods.
3. Hall, Matthew L., Rachel I. Mayberry, and Victor S. Ferreira. 2013. "Cognitive constraints on constituent order: Evidence from elicited pantomime." *Cognition* 129(1): 1 to 17. [Open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4224279/). DOI [`10.1016/j.cognition.2013.05.004`](https://doi.org/10.1016/j.cognition.2013.05.004). This supplies the event-reversibility limit missing from the "wordless default" discussion.
4. Imamura, Satoshi. 2016. "A corpus-based analysis of scrambling in Japanese in terms of anaphoric and cataphoric co-referencing." *Research in Corpus Linguistics* 4: 39 to 49. [Article](https://ricl.aelinco.es/index.php/ricl/article/view/40). This supports a more precise account of Japanese scrambling and information structure.
5. Ketrez, F. Nihan. 2012. "Word order." In *A Student Grammar of Turkish*. Cambridge: Cambridge University Press. [Chapter record](https://www.cambridge.org/core/books/abs/student-grammar-of-turkish/word-order/BE1EF414A06CA27A2F1F96982B0F1927). This supports Turkish SOV order and case-supported alternatives.

## Suggested replacement language

These are repair models, not a required rewrite. They keep the chapter's cadence while taking the weight off claims the sources cannot carry.

### Line 29

> In the WALS sample, 564 of 1,376 languages use subject-object-verb as their dominant order, more than any other single pattern (Dryer 2013). That is roughly two languages in five within the sample.

### Line 31

> The uncommon part is the pairing. WALS records 472 languages with object-before-verb order and postpositions, but only 14 with object-before-verb order and prepositions (Dryer 2013, chapter 95). Phi belongs to that smaller group because its relators obey the same modifier-first order as everything else.

### Line 37

> Beginning around 1980, Ruth Berman, Dan Slobin, and their colleagues used the wordless picture book *Frog, Where Are You?* to gather more than 250 narratives in English, German, Spanish, Hebrew, and Turkish from children and adults (Berman and Slobin 1994; Slobin 1996).

### Line 41

> Phi makes the same kind of question available as a design hypothesis. Its speaker must utter the instrument before the action and the condition before its consequence. Whether repeated use also trains a durable habit of attention remains untested.

### Lines 47 to 48

> Every language group strongly preferred actor-patient-act in silent gesture and in the transparency task. Across the full samples, that order appeared in 90 percent of gesture strings and 81 percent of transparency trials (Goldin-Meadow et al. 2008). The result crossed four native languages in these tasks; it was a preference, not the only order anyone produced.

### Lines 49 to 51

> In the later motion study, English and Turkish speakers converged on the same predominant packaging and order when they gestured without speech, although small differences remained in rarer responses (Özçalışkan, Lucero and Goldin-Meadow 2016). The study found no simple transfer of each language's dominant pattern into silent gesture. It did not test lifelong Phi use or rule out every nonverbal effect of language.

### Line 53

> For the simple events in the 2008 study, actor-patient-act was a strong wordless preference across all four language groups. Later studies found that reversible events can pull gesturers toward other orders (Hall, Mayberry and Ferreira 2013). Phi's order therefore follows one well-attested human preference without claiming it as the mind's single default.

### Line 57

> The evidence leaves Phi with a proposal rather than a verdict. Native languages guide attention during speaking, and silent gesture does not simply preserve every spoken pattern. Phi certainly orders the performance of its own sentences; whether that rehearsal settles into a durable habit is work for future speakers and future evidence.

## Suggested revision order

1. Repair lines 47 to 57 first. They contain the largest gap between the studies and the chapter's conclusions.
2. Add Dryer chapter 95 and correct the WALS sample wording in lines 29 to 31.
3. Add Berman and Slobin 1994, then recast the transfer from childhood native-language evidence to adult Phi as a hypothesis.
4. Add the Japanese and Turkish sources or shorten those examples to claims already carried by WALS.
5. Normalize the bibliography with live links, DOIs, and full source details.
6. Run `python3 scripts/validate_examples.py` after prose revision even if the Phi blocks are left untouched.

## Bottom line

The sources are real, the quotations are accurate, and the chapter has chosen research that belongs in this discussion. Its present certainty does not. The evidence supports three modest conclusions: SOV is common, Phi's OV-plus-preposition profile is uncommon, and language-specific habits often appear while people prepare speech without simply dictating every silent representation. The last step, from those findings to what Phi practice will do, is still a question. The chapter becomes stronger when it leaves that question open.
