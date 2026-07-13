# Citation audit: Chapter 5, "The web"

**Audit date:** 2026-07-13

**Chapter audited:** `book/05_the_web.md` at merge commit `4a0c28bd`

## Scope and method

This audit checks every named external work, every factual claim attached to it, and every repository source named in the chapter's closing note. It uses the original papers or authoritative publication records rather than summaries. Repository claims were checked first against the canonical lexicon, compound registry, and manual. The protocol documents and the code behind both collision tools supplied the rest. The two form-space figures were independently reproduced against both the historical vocabulary snapshot that produced them and the current lexicon.

The chapter itself was not edited. This report separates errors that need correction from qualifications that would make an already sound account more exact.

## Overall finding

All four external works exist, and their bibliographic metadata is correct. Sapir's experiment is summarized well, while the broad descriptions of the Ćwiek and Blasi studies match their results. The local compounds and lexicon entries also check out. So do the protocol, word-shape rule, and listening procedure.

Two passages need substantive correction. First, the chapter calls the designed likeness between `sileta` and `silero` systematicity. Under Dingemanse and colleagues' terminology, that two-word analogy is better described as relative iconicity; systematicity is a statistical relation across a group of words and cannot be established by one pair. Second, 355,428 is a valid historical calculation but is no longer the count for the current lexicon. Repeating the same method now leaves 347,268 available three-syllable forms.

Three smaller changes would improve precision. The bouba/kiki result should report its pooled 72 percent estimate and make clear that 17 of 25 language groups were reliably above chance. The Blasi paragraph should distinguish the broad 40-item dataset from the much smaller extended-list evidence for `small` and `i`. The field-wide claim that evidence is "strongest" in particular domains goes beyond what this short set of citations establishes.

## Corrections by priority

| Priority | Chapter location | Finding | Required response |
|---|---|---|---|
| High | Lines 47-49 | The stable total of 376,740 legal three-syllable forms is correct. The available-form count of 355,428 describes the lexicon at commit `d5f93aaa5`, not the current lexicon. The current count is 347,268. | Replace the stale figure in the chapter and in `documents/word_shape_and_external_boundaries.md`, or make the book use a rounded, explicitly dynamic figure. A small reproducible counting script would prevent the source document from aging silently again. |
| High | Lines 23-31 | `sileta` and `silero` are presented as an example of systematicity. Dingemanse et al. define systematicity as a statistical relation between forms and usage across a group of words. Their definition of relative iconicity fits a relation between two forms that echoes a relation between two meanings. | Recast the pair as relative iconicity. Discuss systematicity separately and say that Phi would need a lexicon-wide analysis before claiming it. |
| Medium | Line 13, Ćwiek et al. | "Held strongly across the whole sample" is defensible as a pooled statement but can sound as though every language group showed the effect. The pooled estimate was 72 percent; 17 of 25 language groups were reliably above the conservative 50 percent baseline. | Give the pooled result and the 17-of-25 qualification. Describe the study as an online opportunity sample if space permits. |
| Medium | Line 13, Blasi et al. | The 6,447 word lists represented 4,298 languages and covered 62 percent of the world's languages, but most lists contained only 28 to 40 concepts. Only 328 lists extended toward 100 concepts. `nose` and `tongue` belonged to the broad core; `small` belonged to the extended set, and its `i` association was supported across 78 lineages and three of five adequately covered macroareas. | Keep the three examples, but do not let their placement imply equal coverage. Replace the loose "controlled for inheritance and geography" with the study's actual safeguards: genealogical balancing, two classifications, macroarea screening, and a spatial analysis. |
| Medium | Line 15 | "The evidence is strongest" ranks an entire research field on the strength of four citations. The papers support limited size and shape correspondences, imitative iconicity, and recurring lexical biases, but they do not supply that comparative ranking. | Narrow the sentence to what the cited papers establish, or add a review that explicitly compares domains of evidence. |
| Low | Lines 79-85 | The references are accurate but omit DOI links, and the Ćwiek entry omits issue 1841. | Add DOI links and the issue number. This improves retrieval; the sources themselves are real. |
| Low | Line 87 | The local-source note is accurate but incomplete. The learning-cluster example comes from the learning chapter; module paraphrase comes from `documents/modules/README.md`; the nonproductive `sileta` and `silero` family is stated canonically in `canon.md`. | Add those three local sources to the note, or replace the prose note with direct file references in endnotes. |
| Low | Line 61 | "Relationships to the five pillars" may imply that every entry must address all five. The schema and protocol require connections only to the pillars that genuinely fit a word. | Change this to "relationships to the relevant pillars" or an equally explicit phrase. |

## External reference ledger

| Work | Existence and metadata | What the source says | Chapter verdict |
|---|---|---|---|
| Edward Sapir, "A study in phonetic symbolism" (1929) | Verified in the [original paper](https://pure.mpg.de/pubman/item/item_2381142_3/component/file_2381141/Sapir_1929a_Study.pdf) and the [Max Planck publication record](https://www.mpi.nl/publications/item2381142/study-phonetic-symbolism). DOI: [10.1037/h0070931](https://doi.org/10.1037/h0070931). The original venue is *Journal of Experimental Psychology* 12(3), 225-239. | Sapir's second experiment used 500 participants, most of them University of Chicago High School students. Four dispersed items contrasted `a` and `i`; preferences for the `a` form as larger ranged roughly from 75 to 96 percent across participant groups. `mal` and `mil`, arbitrarily assigned the meaning table, are his stated example. | Accurate. "Most of them school students," the four contrasts, and the `mal`/`mil` example all check out. The chapter also preserves Sapir's proper limit: the sounds biased a choice after the semantic field had been supplied; they did not reveal a gloss on their own. |
| Aleksandra Ćwiek et al., "The bouba/kiki effect is robust across cultures and writing systems" | Verified in [PubMed](https://pubmed.ncbi.nlm.nih.gov/34775818/) and the [full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8591387/). DOI: [10.1098/rstb.2020.0390](https://doi.org/10.1098/rstb.2020.0390). It appeared online in 2021 and in the journal's 2022 volume 377, issue 1841, article 20200390. Using 2022 is normal and internally consistent. | The final online opportunity sample contained 917 participants associated with 25 languages, nine language families, and ten writing systems. The conservative full-match estimate was 72 percent. Seventeen language groups were reliably above 50 percent; descriptive averages ranged from 100 percent for Swedish to 36 percent for Romanian. Roman-script groups averaged 75 percent and other-script groups 63 percent, but the modeled script effect was weak. | Broadly accurate, with a needed qualification. The effect was strong in the pooled model, not uniform in every language. The chapter's phrase "though its strength varied" gestures toward this, but a numerical sentence would remove the ambiguity. |
| Damián E. Blasi et al., "Sound-meaning association biases evidenced across thousands of languages" (2016) | Verified in the [PNAS article](https://doi.org/10.1073/pnas.1605782113), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27621455/), and an [open Max Planck copy](https://pure.mpg.de/rest/items/item_2344242/component/file_2344241/content). DOI: [10.1073/pnas.1605782113](https://doi.org/10.1073/pnas.1605782113). The chapter's volume, issue, and pages are correct. | After exclusions, the study used 6,447 word lists representing 4,298 languages and 359 lineages. Most lists supplied 28 to 40 basic concepts, while 328 supplied additional items. The reported associations include `n` with nose, `l` with tongue, and high front `i` with small. The authors balanced the tests genealogically, repeated them under two classifications, and screened results across linguistic macroareas. They also corrected for multiple comparisons and word length, then ran a spatial analysis. | Correct in direction, but compressed too tightly. "Nearly two-thirds" accurately describes language coverage of the dataset. It should not be read as the coverage for every concept: the `small` result came from the extended lists and spanned 78 lineages, while the nose and tongue results drew on much broader core coverage. The authors conclude that inheritance and areal dispersal are unlikely explanations; "controlled for" is a serviceable shorthand but stronger than their own methodological caveat about a proper phylogenetic test. |
| Mark Dingemanse et al., "Arbitrariness, iconicity, and systematicity in language" (2015) | Verified in the [Max Planck publication record](https://pure.mpg.de/view/item_2176289), [open paper](https://pure.mpg.de/rest/items/item_2176289/component/file_2213052/content), and [PubMed](https://pubmed.ncbi.nlm.nih.gov/26412098/). DOI: [10.1016/j.tics.2015.07.013](https://doi.org/10.1016/j.tics.2015.07.013). The chapter's authors, year, journal, volume, issue, and pages are correct. | The review distinguishes iconicity, where aspects of form resemble aspects of meaning, from systematicity, where statistical regularities in forms predict usage or function. It also names relative iconicity: relations among multiple forms resemble relations among meanings. The review argues that iconicity can aid word learning and communication, systematicity can aid category learning, and arbitrariness can aid the individuation of meanings. | The learning tradeoff is summarized fairly. The label attached to `sileta` and `silero` is not. One designed pair does not demonstrate a statistical pattern across a word group. |

## Passage-by-passage audit

### Lines 3-7: the color web

The lexicon and compound claims are accurate. `welisha` is the content word for color, and its entry points to `haoni welisha` for voice color or timbre. The compound registry contains `haoni welisha`, `kerou welisha`, and `horathe welisha`, with the stated literal and conventional meanings. The modifier-first analysis matches Phi grammar. The chapter is careful to call the gray and pink readings conventional rather than self-decoding, which agrees with the registry and avoids asking a stone to standardize its wardrobe.

### Line 11: Sapir's size experiment

No correction is needed. Sapir used a 100-pair mixed schedule for the 500-person experiment, with the four `a`/`i` contrasts dispersed among other contrasts to reduce patterned responding. The chapter does not confuse this with his earlier 60-pair experiments. The sample description is accurate: 464 participants were aged 11 through 18, mostly from the University of Chicago High School, with 21 university students, eight other adults, and seven Chinese participants.

One phrasing detail is worth preserving during revision. Sapir assigned each pair a semantic category and asked which form suggested the larger member. The experiment supports a magnitude preference, not the proposition that `mal` independently means large table or that `mil` independently means small table. The chapter already says this correctly in its final two sentences.

### Line 13: the bouba/kiki study

The participant count, language count, writing-system count, auditory presentation, and round/spiky mapping are correct. The title's word "robust" does not mean universal, and the paper explicitly says universal obedience was not its goal. Its main analysis required a participant to match both successive trials congruently and compared that full match with a conservative 50 percent baseline. The pooled posterior mean was 72 percent, with a 95 percent credible interval of 56 to 82 percent.

The present sentence can be read correctly, but it asks "across the whole sample" to do too much. A reader could take it to mean that all 25 groups showed the effect. Seventeen groups had intervals reliably above 50 percent, and three groups had raw descriptive averages below 50 percent. The authors also caution that the online opportunity sample was uneven across languages; 80 percent of participants spoke English as a first or second language. A compact book chapter need not carry every limitation, but it should distinguish a strong pooled tendency from an exceptionless universal.

### Line 13: the global word-list study

The three reported associations are genuine. Nose was associated with alveolar `n` across 334 lineages and four of six adequately covered macroareas. Tongue was associated with `l` across 280 lineages and all six macroareas. Small was associated with high front `i` across 78 lineages and three of five macroareas. The smaller count for small is not a weak result under the authors' test, but it comes from a different coverage tier and should not borrow the apparent reach of the core 40-item list.

The current wording also compresses several methods into "controlled for inheritance and geography." The researchers balanced observations by lineage, used two independent genealogical classifications, required consistent evidence in at least three macroareas, and examined geographic proximity to unrelated languages carrying a signal. Their conclusion is that inheritance and areal spread are unlikely to explain the broad patterns. They also say that an ideal phylogenetic test would require cognate or sound-change data and an evolutionary model that their database did not contain. A more concrete description of the safeguards would be both plainer and harder to overread.

### Line 15: the boundary of the evidence

The boundary is sound: none of these studies establishes Phi's local associations such as nasal groundedness or fricative reflection as human universals. Dingemanse et al. support a wider distinction among imitative iconicity, analogical relations, and statistical patterns. The trouble lies only in the word "strongest." The selected sources do not rank every domain of sound symbolism. "The cited evidence includes" or "These studies establish limited correspondences in" would make the same turn without claiming a literature-wide comparison.

### Lines 17-19: `muila` and the manual's hedge

The `muila` paragraph follows the entry accurately. Its `sound_symbolism` field describes closed lips and deep `u` in `mu`, a separate rising `i`, and flowing `la`. The chapter improves the epistemic boundary by explicitly saying that these are not morphemes. The quotation "Not every word fits the pattern perfectly" appears verbatim in the manual's "Sound as symbol" chapter, followed by its stated claim of intent. No external citation is needed for a transparent account of Phi's own documented practice.

### Lines 23-31: family resemblance

The lexical facts are right. `sileta` means sun, `silero` means star, both begin `si.le`, the sun is one member of the wider class, and `si.le` is not a productive affix. The problem begins when the paragraph says linguists call "this kind of pattern" systematicity. Dingemanse et al. use relative iconicity for an analogical relation among forms and meanings. They reserve systematicity for statistical cues across a group, such as phonological tendencies that help distinguish lexical classes.

Phi may contain systematicity, but this chapter has not measured it. Claims about nasal-heavy semantic neighborhoods, fricative-heavy abstractions, or other sound families would require a declared classification, a lexicon-wide count, and a comparison with an appropriate baseline. The three-word learning cluster `nulae`, `nuwera`, and `whemura` is documented in the learning chapter, but a teaching cluster is not by itself statistical evidence. It can remain as an account of deliberate family resemblance and the risk of confusion.

The review does support the next claim as a general experimental tendency: iconicity helps some word learning and communication, systematic cues can help category learning, and arbitrary distinctiveness helps separate meanings. It does not show that Phi learners receive those benefits from this pair. The chapter's line 31 already exercises the right restraint by waiting for learner evidence before calling the design easy.

### Lines 35-43: transparent composition

These paragraphs agree with the compound registry and with the word-creation protocol. The chapter distinguishes guessability from convention, admits the cost of carrying an inherited image into unrelated contexts, and leaves room for a root when composition becomes cumbersome or misleading. Those are internal design arguments and do not borrow empirical authority from the four external papers.

### Lines 47-55: word space and collision checks

The three-syllable lexical ceiling and four-syllable name exception match `canon.md`, `documents/phonology_rules.md`, and the validator. The stable 376,740 total reproduces from the 14 permitted onsets, five vowels, later hiatus vowels, the ban on repeating a syllable that has an onset, and the three-vowel constraint.

The second number is stale rather than invented. At commit `d5f93aaa5`, the repository contained 1,040 lexical entries and 910 content words. Independent enumeration finds 376,740 legal three-syllable forms, blocks 21,312 forms through exact duplication or character-distance-one proximity to a content word, and leaves exactly 355,428. The current repository contains 1,168 lexical entries and 1,038 content words. The same calculation blocks 29,472 forms and leaves 347,268.

| Vocabulary snapshot | Lexicon entries | Content words | Legal three-syllable forms | Blocked by exact duplication or content-neighbor rule | Available |
|---|---:|---:|---:|---:|---:|
| Commit `d5f93aaa5` | 1,040 | 910 | 376,740 | 21,312 | 355,428 |
| Current audited chapter | 1,168 | 1,038 | 376,740 | 29,472 | 347,268 |

The chapter's conclusion survives. More than 347,000 currently available forms are ample for the project's stated purpose. The exact availability figure is a moving inventory fact, however, and should either be generated or rounded honestly in teaching prose.

The description of the tools is accurate. `validate_examples.py` computes character edit distance, rejects any new content-content pair at distance one, and allows the committed baseline only to shrink. `audit_phonetic_neighbors.py` parses `ph`, `th`, `sh`, and `wh` as units; assigns feature-sensitive substitution costs to vowels and consonants; and sorts close pairs by score, function-word involvement, corpus attestations, and lexical order. Its ABX prompt generator is reproducible from a seed. The solo listening protocol says that a score never renames a word and that repeated confusion from one speaker remains evidence from one speaker. The chapter states each of these limits correctly.

### Lines 59-67: the price of a root and optional modules

The word-creation questions are accurate paraphrases of `documents/development_protocol.md`: existing expression, composition, core or module placement, semantic neighbors, values, and burdens all appear there. The protocol explicitly calls itself a quality checklist rather than a burden-of-proof process and allows coinage because a concept is useful, valued, beautiful, or worth making easy to express. The chapter's less procedural wording preserves that point. One phrase needs tightening: an entry records its relationships to the relevant pillars, not necessarily to all five.

The module paragraph agrees with `documents/modules/README.md`. Modules add vocabulary, not grammar; a speaker may ask for a core paraphrase; and one word may belong to several modules. The closing source note should name the module document because this paragraph depends on it directly.

### Lines 71-75: east as the sun's beginning

`sileta thorui` appears in the compound registry with the literal reading sun's beginning and the conventional reading east. Both words exist with the stated glosses, and modifier-first order is correct. The chapter wisely says that the registry fixes the directional reading. Sunrise is an image behind the convention, not a procedure by which a speaker must calculate a bearing on every day and at every latitude.

## Local source ledger

| Chapter material | Repository source | Verdict |
|---|---|---|
| `welisha`, `haoni welisha`, `kerou welisha`, `horathe welisha` | [`vocabulary/content/color.json`](../vocabulary/content/color.json), [`documents/compounds.md`](../documents/compounds.md), and the entries for voice, stone, and dawn | All forms and readings check out. |
| `muila` sound account | [`vocabulary/content/earth.json`](../vocabulary/content/earth.json) | Faithful paraphrase of the entry. |
| Manual quotation and intended sound-symbolism boundary | [`manual/part2_soul/ch04_philosophy_of_sound_meaning_grammar/02_sound_as_symbol.md`](../manual/part2_soul/ch04_philosophy_of_sound_meaning_grammar/02_sound_as_symbol.md) | Exact quotation; the surrounding argument is represented fairly. |
| `sileta` and `silero` lexical family | [`vocabulary/content/sun.json`](../vocabulary/content/sun.json), [`vocabulary/content/star.json`](../vocabulary/content/star.json), and [`canon.md`](../canon.md) | Meanings and designed resemblance are accurate. Canon supplies the explicit ruling that the shared opening is not a productive affix. |
| `nulae`, `nuwera`, `whemura` learning cluster | [`manual/part2_soul/ch06_philosophy_of_learning/03_patience_with_process.md`](../manual/part2_soul/ch06_philosophy_of_learning/03_patience_with_process.md) | Present verbatim as a recommended learning cluster. This source is missing from the closing note. |
| Three-syllable ceiling and capacity count | [`documents/word_shape_and_external_boundaries.md`](../documents/word_shape_and_external_boundaries.md), [`documents/phonology_rules.md`](../documents/phonology_rules.md), and [`canon.md`](../canon.md) | Structural rule accurate; current availability count stale in the first document. |
| Character and phonetic collision tools | [`scripts/validate_examples.py`](../scripts/validate_examples.py), [`scripts/audit_phonetic_neighbors.py`](../scripts/audit_phonetic_neighbors.py), and [`scripts/README.md`](../scripts/README.md) | Implementation matches the chapter. |
| Solo listening and rename limit | [`documents/listening_audit.md`](../documents/listening_audit.md) | Present and accurately summarized. |
| Word-creation process | [`documents/development_protocol.md`](../documents/development_protocol.md) | The chapter keeps the protocol's meaning without copying its checklist voice. |
| Optional module behavior | [`documents/modules/README.md`](../documents/modules/README.md) | The summary is sound; this source is missing from the closing note. |
| `sileta thorui` | [`documents/compounds.md`](../documents/compounds.md) and entries for sun and beginning | The words, order, literal reading, and registered direction all match. |

## Suggested replacement language

The following passages preserve the chapter's movement while correcting the evidence. They are suggestions, not edits already made.

### Replace the bouba/kiki and Blasi portion of line 13

> Newer and broader tests find other modest correspondences. In an online study published in the journal's 2022 volume, 917 participants associated `bouba` with a round shape and `kiki` with a spiky one. The pooled full-match estimate was 72 percent, and 17 of the 25 language groups were reliably above chance: a broad tendency, not an exceptionless rule (Ćwiek et al. 2022). Blasi and colleagues analyzed 6,447 word lists representing 4,298 languages. Their genealogically balanced and geographically screened tests found recurring associations such as `n` in words for nose and `l` in words for tongue. In the smaller collection of extended lists, high front `i` was associated with small across 78 lineages and three of five adequately covered macroareas (Blasi et al. 2016). Human vocabularies are not wholly arbitrary; certain sounds lean.

### Replace the opening of line 15

> The cited studies establish limited correspondences in size, shape, and basic vocabulary, while the broader review also describes imitative forms. They do not establish that a nasal universally means groundedness, or that a fricative belongs by nature to reflection.

### Replace the terminology paragraph at line 27

> Linguists distinguish several kinds of relation between form and meaning. The kinship of `sileta` and `silero` is closest to relative iconicity: the relation between the two forms echoes a relation between their meanings. Systematicity is different. It is a statistical pattern across a group of words whose forms help predict usage or category, and this pair alone cannot establish one. Natural languages mix both with arbitrariness. Iconic forms can aid word learning and communication; systematic patterns can aid category learning; arbitrary forms help keep meanings individually distinct (Dingemanse et al. 2015). Those are observed tendencies, not yet test results for Phi. A vocabulary in which every relative sounded alike would still make a family reunion difficult. Everyone would answer when one name was called.

### Replace the numerical opening at line 49

> The available space is not small. Under Phi's phonotactic rules, 376,740 legal three-syllable forms can be built. The current lexicon and its character-distance-one gate still leave about 347,000 available, and the precise second figure changes as the lexicon grows. That is enough to settle the fear that Phi will run out of words. It says much less about whether two chosen words will remain distinct across a room, through an accent, or beside a running tap. Combinatorics has excellent hearing under ideal conditions.

## Corrected reference forms

The chapter may keep its present bibliography style and add the retrieval details below.

Blasi, Damián E., Søren Wichmann, Harald Hammarström, Peter F. Stadler, and Morten H. Christiansen. 2016. Sound-meaning association biases evidenced across thousands of languages. *Proceedings of the National Academy of Sciences* 113(39): 10818-10823. https://doi.org/10.1073/pnas.1605782113.

Ćwiek, Aleksandra, Susanne Fuchs, Christoph Draxler, Eva Liina Asu, Dan Dediu, Katri Hiovain, Shigeto Kawahara, Sofia Koutalidis, Manfred Krifka, Pärtel Lippus, Gary Lupyan, Grace E. Oh, Jing Paul, Caterina Petrone, Rachid Ridouane, Sabine Reiter, Nathalie Schümchen, Ádám Szalontai, Özlem Ünal-Logacev, Jochen Zeller, Marcus Perlman, and Bodo Winter. 2022. The bouba/kiki effect is robust across cultures and writing systems. *Philosophical Transactions of the Royal Society B* 377(1841): 20200390. https://doi.org/10.1098/rstb.2020.0390.

Dingemanse, Mark, Damián E. Blasi, Gary Lupyan, Morten H. Christiansen, and Padraic Monaghan. 2015. Arbitrariness, iconicity, and systematicity in language. *Trends in Cognitive Sciences* 19(10): 603-615. https://doi.org/10.1016/j.tics.2015.07.013.

Sapir, Edward. 1929. A study in phonetic symbolism. *Journal of Experimental Psychology* 12(3): 225-239. https://doi.org/10.1037/h0070931.

## Recommended revision order

1. Correct relative iconicity versus systematicity, because that distinction shapes the chapter's central account of the web.
2. Replace the stale 355,428 figure in both the chapter and its repository source, then decide whether the changing count should be generated rather than maintained by hand.
3. Add the numerical qualifications for Ćwiek and separate the broad and extended coverage in Blasi.
4. Narrow the unsupported "strongest" sentence.
5. Add DOI links, issue 1841, and the omitted local sources.

## Bottom line

The chapter has four real external anchors and uses three of them with good restraint. Sapir is clean, Ćwiek needs one numerical qualification, and Blasi needs its two coverage tiers kept apart. Dingemanse exposes the one conceptual tangle: a family resemblance between two Phi words may be deliberate and useful without becoming statistical systematicity. The form-space arithmetic tells a similar story. The large stable total is sound; the smaller inventory total moved because the lexicon did exactly what lexicons do and acquired more words.
