# Citation audit for the current book chapters

## Purpose and scope

This is a source audit, not a revision of the chapters. It covers every formal reference in the four chapter files currently under `book/`, checks the existence and authorship of each work, follows the one external link printed in the references, compares the chapter's claims with the cited findings, and checks the chapters' internal references against the Phi repository. No fabricated publication or falsely attributed author was found. That good bibliographic result does not make every use of the sources sound: several passages draw conclusions broader or more causal than the cited work permits.

The four chapter files contain 39 formal references: one in [The boatman](00_the_boatman.md), twelve in [The hurried tongue](01_the_hurried_tongue.md), one in [What a refusal is](02_what_a_refusal_is.md), and twenty-five in [The lens, not the cage](11_the_lens_not_the_cage.md). `treatment.md` is a planning document rather than a chapter, so its abbreviated research receipts are outside this audit. They will need a separate bibliography check if they enter the book's prose.

## Summary

| Chapter | Formal references | Bibliographic result | Main work still needed |
|---|---:|---|---|
| The boatman | 1 | Genuine work, author, and publication history | Identify the quoted edition consistently |
| The hurried tongue | 12 | All genuine; one subtitle is incomplete | Correct one chronology error, cite Slow Food, and narrow several empirical claims |
| What a refusal is | 1 | Genuine work and author; internal Phi receipts also exist | Replace two unsupported historical superlatives with defensible wording |
| The lens, not the cage | 25 | All genuine | Add two omitted original sources, remove one mismatched citation, and qualify several contested or universal claims |

## 00: The boatman

### Formal reference

| Reference | Identity check | Use in the chapter |
|---|---|---|
| William Morris, *News from Nowhere; or, An Epoch of Rest* | Verified | The quoted dialogue agrees with the book text, and the author and title are correct. The entry combines the 1890 serialization with the 1891 revised book edition without choosing which edition it cites. |

Morris's novel was serialized in *Commonweal* in 1890 and first published in book form by Reeves & Turner in 1891. The chapter says that its passages follow the book text, so the reference should lead with the 1891 edition and mention the serialization in a note. The [William Morris Gallery](https://www.wmgallery.org.uk/%3A/object/news-from-nowhere/) and the [William Morris Archive](https://morrisarchive.lib.uiowa.edu/serialization-of-news-from-nowhere-in-commonweal) confirm that sequence. The quoted wording also appears in the [public *Commonweal* text](https://www.marxists.org/archive/morris/works/1890/commonweal/nowhere_commonweal.htm).

A suitable replacement entry would be:

> Morris, William. 1891. *News from Nowhere; or, An Epoch of Rest*. London: Reeves & Turner. First serialized in *Commonweal* in 1890. The passages above follow the book text.

The local source text contains the quoted exchange, and the corresponding Phi rendering is present in `texts/news_from_nowhere/chapter_02.md`. The shelf pointer is therefore valid.

## 01: The hurried tongue

### Reference ledger

| Reference | Identity check | Use in the chapter |
|---|---|---|
| Allcott, Braghieri, Eichmeyer, and Gentzkow 2020 | Verified: authors, title, journal, volume, issue, and pages | The experiment is described recognizably, but its result is generalized beyond the selected Facebook users and election period studied. |
| Brady, Wills, Jost, Tucker, and Van Bavel 2017 | Verified: authors, title, journal, volume, issue, and pages | The chapter changes an observational association into causation and treats moral-emotional language as if it meant only blame and outrage. |
| Crockett 2017 | Verified: author, title, journal, volume, and pages | Fairly identified as a conceptual framework rather than a dataset. |
| Freeman 2009 | Verified: author, title, publisher, and year | The reference is correct, but the prose mistakenly places the 2009 book in the same year as a 2010 manifesto. |
| Honoré 2004 | Verified: author, book, publisher, and year | The printed subtitle is incomplete. The discussion of `tempo giusto` and the movement's relationship with technology is consistent with the book. |
| Jaidka, Zhou, and Lelkes 2019 | Verified: authors, title, journal, volume, issue, and pages | The findings are recognizable, but the natural experiment was not a randomized clean test or a panel of the same people. |
| Köhler, David, and Blumtritt 2010 | Verified: authors, title, date, and official site | The summary of the manifesto is fair. The printed root-domain link works but should point to the English manifesto itself. |
| Lorenz-Spreen, Mønsted, Hövel, and Lehmann 2019 | Verified: authors, title, journal, article number, and year | The Twitter figures are correct, but the chapter claims more uniformity across datasets than the study reports. |
| Newport 2019 | Verified: author, title, publisher, and year | Correctly used as an argument and source of vocabulary, not as empirical evidence. |
| Odell 2019 | Verified: author, title, publisher, and year | Correctly used as an argument and source of vocabulary, not as empirical evidence. |
| Rathje, Van Bavel, and van der Linden 2021 | Verified: authors, title, journal, volume, issue, and article number | The numerical summary is accurate, but the conclusion is extended from selected American political accounts to English sentences in general. |
| Vosoughi, Roy, and Aral 2018 | Verified: authors, title, journal, volume, issue, and pages | The numerical summary is accurate for the Twitter dataset. The chapter turns that bounded result into a claim about truth in general. |

### Bibliographic and historical corrections

The complete title of Honoré's book is *In Praise of Slowness: How a Worldwide Movement Is Challenging the Cult of Speed*. The current entry omits "How a Worldwide Movement Is." The [WorldCat record](https://search.worldcat.org/title/In-praise-of-slowness-%3A-how-a-worldwide-movement-is-challenging-the-cult-of-speed/oclc/55495224) and the [Publishers Weekly record](https://www.publishersweekly.com/9780060545789) agree on the full title.

The sentence beginning "The same year brought the argument to the inbox" follows the 2010 Slow Media Manifesto but introduces Freeman's 2009 book. Either "The previous year" or a transition without a relative date would repair the chronology. The [Scribner record](https://www.simonandschuster.com/books/The-Tyranny-of-E-mail/John-Freeman/9781416588122) confirms the 2009 publication date.

The Slow Media reference should use the exact [English manifesto page](https://en.slow-media.net/manifesto) rather than `slow-media.net`, and should include an access date if the book's chosen citation style requires one. The link resolves and the listed authors are correct.

The Slow Food paragraph has no reference. The 1986 protest near the Spanish Steps and the 1989 founding by representatives from fifteen countries are documented in [Slow Food's history](https://www.slowfood.com/our-history/). The paragraph then gathers the "good, clean, and fair" formulation, the Ark of Taste, and the university under "from the start," although these belong to later stages of the movement. Slow Food's [account of its present values](https://www.slowfood.com/about-us/) can support the philosophy, but the chronology needs to distinguish the founding from later institutions.

### Empirical claims that need narrower wording

The opening thought experiment says the accusatory sentence will travel farther and that its advantage can be estimated from its wording alone. Brady et al. studied 563,312 messages about gun control, same-sex marriage, and climate change. Each additional moral-emotional word was associated with roughly twenty percent more diffusion, especially within ideological groups. The design was observational. It did not show that a word caused the increase, and it did not measure whether anyone was persuaded. "Moral-emotional language" is also wider than "the vocabulary of blame and outrage." The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/28652356/) gives the study's scope and result.

Rathje et al. analyzed 2,730,215 posts from news organizations and members of the United States Congress on Facebook and Twitter. The reported twofold difference and 67 percent increase in the odds of sharing are accurate within that corpus. "The single most shareable thing an English sentence can currently do" converts a result about selected political accounts, platforms, and tested predictors into a universal statement about English. The [full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8256037/) supports a narrower conclusion about out-group language in online political communication.

Vosoughi et al. did study about 126,000 stories spread by roughly three million people, and it found that false stories traveled farther, faster, deeper, and more broadly on Twitter. The 70 percent and six-times figures are accurate. "Truth simply takes longer to move" should retain its Twitter qualification rather than becoming a general law of communication. The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29590045/) confirms the study's figures and scope.

Crockett's account is handled more carefully. The chapter explicitly calls it a framework rather than a dataset, which is correct. The paper discusses reduced personal costs, greater exposure to outrage-provoking material, and reinforcement through online feedback. The [Nature Human Behaviour article](https://www.nature.com/articles/s41562-017-0213-3) supports that characterization.

Lorenz-Spreen et al. compared collective attention across Twitter, Google Books, Google Trends, movie ticket sales, Reddit, and Wikipedia. The reported decline in a top Twitter hashtag's average residence from 17.5 hours in 2013 to 11.9 hours in 2016 is correct. "The pattern repeated everywhere the data reached" is too absolute, since the paper discusses differences and limits among the systems. "The whole culture's conversational metabolism runs hotter" is the chapter's interpretation rather than the authors' result. The [Nature Communications article](https://www.nature.com/articles/s41467-019-09311-w) should remain attached to the measured changes.

Jaidka et al. analyzed 358,242 replies to American politicians across Twitter's change from 140 to 280 characters. The estimates of less incivility and more politeness and constructiveness are accurately reported, as is the longer decline in empathy and respect. "The same platform, the same people" is not accurate because this was a corpus of replies rather than a panel following the same users, and "clean test" suggests experimental control the discontinuous time-series design did not have. The [Journal of Communication article](https://academic.oup.com/joc/article/69/4/345/5547032) supports a more careful description as a natural experiment.

Allcott et al. randomized 2,743 recruited Facebook users and studied four weeks of deactivation before the 2018 midterm election. The paper reports more offline activity and socializing, less factual news knowledge, lower policy-issue polarization, a gain of about 0.09 standard deviations in subjective wellbeing, and lower Facebook use afterward. The chapter should say "policy-issue polarization" rather than political polarization without qualification. The claim that the ordinary dose of a fast medium "costs something" reaches beyond selected users willing to participate, one platform, and one political period. The [American Economic Review article](https://www.aeaweb.org/articles?id=10.1257/aer.20190658) supports the bounded experimental claim.

The synthesis in the paragraph beginning "The diffusion studies found the advantage of heat" repeats these expansions. The studies found associations within particular corpora, not an inherent advantage residing in words themselves. The character-limit study does not establish the general rule "change the form and the conduct changes with it." The Facebook experiment did not show that a user has "nowhere slower to stand" inside the medium. These sentences can remain the author's argument if they are marked as an inference rather than presented as three empirical findings.

## 02: What a refusal is

### Formal and internal references

| Reference | Identity check | Use in the chapter |
|---|---|---|
| J. R. R. Tolkien, *The Lord of the Rings* | Verified: author, work, London publisher, and 1954-1955 publication sequence | The Ring Verse is a proper source for the discussion. A volume and page would make the location reproducible. |

George Allen & Unwin is the publisher's usual printed style. The current "George Allen and Unwin" is recognizable but should be normalized. The [Tolkien bibliography](https://forodrim.org/bibliography/tbchron.html) confirms the three-volume publication sequence, and [WorldCat](https://search.worldcat.org/title/1487587) confirms the work and publisher.

The chapter's internal receipts are present. `texts/ring_verse_refusal.md` contains the cited refusal and the displayed Phi lines. `documents/psychological_violence_of_measurement.md` exists. The named canon rulings, the examples `ruela wi philo thalo nai.` and `lo mia wiso wisola.`, and the cited vocabulary forms all exist in the repository with the meanings the chapter gives them.

### Unsupported historical claims

"The oldest custom in language invention" is not established by the Tolkien reference and is probably not provable. "A familiar custom among language creators" would preserve the point without inventing priority.

The chapter elsewhere describes people waiting "the way people waited for most of human history." That is a broad historical claim without a source. It can either be sourced from scholarship on time discipline or rewritten as a limited contrast with clock-scheduled waiting.

## 11: The lens, not the cage

### Reference ledger

| Reference | Identity check | Use in the chapter |
|---|---|---|
| Boroditsky 2001 | Verified: author, title, journal, volume, and pages | Correctly identified as the original Mandarin-time result; the replication history needs more exact language. |
| Boroditsky and Gaby 2010 | Verified: authors, title, journal, volume, and pages | The east-west card layouts and orientation effect are accurately reported; broader claims about the community exceed this task. |
| Boroditsky, Fuhrman, and McCormick 2011 | Verified: authors, title, journal, volume, and pages | Supports a weaker and task-dependent difference between English and Mandarin temporal representations. |
| Chen 2007 | Verified: author, title, journal, volume, and pages | Properly cited as a failed replication and challenge to the original metaphor-frequency premise. |
| Frank, Everett, Fedorenko, and Gibson 2008 | Verified: authors, title, journal, volume, and pages | The visible matching and memory-dependent failures are reported accurately. The field-wide conclusion later drawn from them needs restraint. |
| Fuhrman and Boroditsky 2010 | Verified: authors, title, journal, volume, and pages | Misapplied: the study concerns English and Hebrew writing direction, not Mandarin vertical time. |
| Gordon 2004 | Verified: author, title, journal, volume, and pages | Fairly presented as the earlier Pirahã result, though the "no words, no numbers, no thought" formula is a later caricature rather than Gordon's literal conclusion. |
| January and Kako 2007 | Verified: authors, title, journal, volume, and pages | Properly cited among failed replications; "three independent laboratories" is less exact than "three published follow-up papers." |
| Levinson, Kita, Haun, and Rasch 2002 | Verified: authors, title, journal, volume, and pages | The reply and dispute are represented fairly, though "the flip does not happen" should remain attributed to the authors. |
| Li and Gleitman 2002 | Verified: authors, title, journal, volume, and pages | The landmark manipulation and ecological interpretation are represented fairly. |
| Malotki 1983 | Verified: author, title, publisher, and year | Supports the extensive account of Hopi temporal expression, not the separate historical claim about the extent of Whorf's informant base. |
| McWhorter 2014 | Verified: author, title, publisher, and year | Used for recognizable arguments, but page or chapter citations are needed for the detailed summary. |
| Mickan, Schiefke, and Stefanowitsch 2014 | Verified: authors, title, publication, volume, and pages | Properly cited as a failed direct replication of the bridge-description experiment. |
| Papafragou, Li, Choi, and Han 2007 | Verified: authors, title, journal, volume, and pages | The Korean child-development result is summarized fairly. |
| Pinker 1994 | Verified: author, title, publisher, and year | Used for recognizable arguments, but page or chapter citations are needed for the detailed summary. |
| Pullum 1991 | Verified: author, title, publisher, and year | The chapter follows Pullum's account, but later specialist scholarship complicates that account. |
| Regier and Kay 2009 | Verified: authors, title, journal, volume, and pages | A genuine review with the stated thesis; part of its lateralized-color evidence was later challenged, as the chapter notes. |
| Roberts, Winters, and Chen 2015 | Verified: authors, title, journal, volume, issue, and article number | Correctly challenges the savings-rate claim, but the chapter describes the correction too absolutely. |
| Samuel, Cole, and Eacott 2019 | Verified: authors, title, journal, volume, and pages | The systematic review and its cautious conclusion are represented fairly. |
| Slobin 1996 | Verified: author, chapter title, book, editors, and pages | The description of "thinking for speaking" is broadly accurate. |
| Tosun, Vaid, and Geraci 2013 | Verified: authors, title, journal, volume, and pages | The Turkish source-memory findings and bilingual carryover are represented accurately. |
| Tse and Altarriba 2008 | Verified: authors, title, journal, volume, and pages | Properly cited as evidence against the original Mandarin-time result. |
| Ünal and Papafragou 2018 | Verified: authors, chapter title, handbook, editor, and pages | The universalist conclusion is represented fairly. |
| Winawer et al. 2007 | Verified: all six authors, title, journal, volume, and pages | The Russian color result and verbal-interference finding are accurate. The citation cannot establish that this is the field's "most famous replicable result." |
| Witzel and Gegenfurtner 2011 | Verified: authors, title, journal, volume, issue, and article number | The replication series and failure to find lateralization are represented fairly; the conclusion should remain scoped to that series. |

### Missing original sources

The gendered-bridges paragraph discusses the 2003 experiment but omits it from the references. The full entry is:

> Boroditsky, Lera, Lauren A. Schmidt, and Webb Phillips. 2003. "Sex, Syntax, and Semantics." In *Language in Mind: Advances in the Study of Language and Thought*, edited by Dedre Gentner and Susan Goldin-Meadow, 61-79. Cambridge, MA: MIT Press.

The [publication record](https://philpapers.org/rec/BORSSA-3) confirms the authors, title, editors, and pages. The chapter says that the experiment "was never published in a peer-reviewed journal." That is literally true but leaves the impression that it was never published in a scholarly venue. It appeared, with limited methodological detail, in an edited MIT Press volume. The later [Mickan, Schiefke, and Stefanowitsch paper](https://stefanowitsch.de/anatol/files/p/mickanetal2014_kls.pdf) and the [Samuel, Cole, and Eacott systematic review](https://repository.essex.ac.uk/25035/) support the cautious conclusion about the result.

The savings-rate paragraph names Keith Chen's 2013 study but omits it from the references. The full entry is:

> Chen, M. Keith. 2013. "The Effect of Language on Economic Behavior: Evidence from Savings Rates, Health Behaviors, and Retirement Assets." *American Economic Review* 103(2): 690-731. https://doi.org/10.1257/aer.103.2.690.

The [American Economic Review article](https://pubs.aeaweb.org/doi/10.1257/aer.103.2.690) is the original source. Roberts, Winters, and Chen found that language family and cultural descent weakened the reported association and made it nonsignificant under strict tests, while some other specifications retained it. "Dissolves most of the correlation" is a possible reading of part of the analysis, not a complete account of the paper's findings. The [PLoS ONE article](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0132145) should be described in those terms.

### Source mismatch and replication wording

The Mandarin-time paragraph should remove Fuhrman and Boroditsky 2010 from the support for vertical Mandarin time. That paper compares English and Hebrew speakers and finds that writing direction is associated with horizontal temporal layout. Its [official abstract](https://pubmed.ncbi.nlm.nih.gov/21564254/) does not discuss Mandarin vertical representations. Boroditsky, Fuhrman, and McCormick 2011 does supply the relevant later evidence; its [PubMed record](https://pubmed.ncbi.nlm.nih.gov/21030013/) reports horizontal and vertical differences between English and Mandarin speakers.

"Three independent laboratories then failed to reproduce the result" should become "three published follow-up papers challenged or failed to reproduce the result" unless the chapter adds an affiliation-level demonstration of laboratory independence. January and Kako report multiple failed attempts within one research program, which is not the same unit of evidence as multiple independent laboratories. Their [paper](https://ruccs.rutgers.edu/images/personal-karin-stromswold/publications/January2007.pdf), together with [Chen's record](https://philpapers.org/rec/CHEDCA-2) and [Tse and Altarriba's record](https://philpapers.org/rec/TSEEAL), supports the narrower wording.

### Historical claims that need sources or qualification

Malotki's *Hopi Time* is real and extensive. It shows that Hopi has abundant ways to express temporal relations. It does not by itself establish the chapter's account of Whorf relying substantially on interviews with one Hopi speaker in New York. Recent scholarship describes Whorf's long work with Ernest Naquayouma but also records a 1938 Hopi field trip and other materials. The chapter needs a separate history-of-scholarship citation and less categorical wording. A relevant modern source is the University of Chicago Press article ["Whorf's Hopi Fieldwork"](https://www.journals.uchicago.edu/doi/10.1086/732457).

The snow paragraph accurately recounts Pullum's argument but treats it as the settled end of the matter. Later work by specialists in Inuit and Yupik languages argues that Boas was illustrating morphological structure rather than offering a final count and that these languages do have substantial, culturally useful snow and ice vocabularies. The popular claim of a magical fixed number remains unsound, but "Boas mentioned four roots and retellings did the rest" is too tidy. Krupnik and Müller-Wille's [historical and linguistic review](https://gwern.net/doc/psychology/linguistics/2010-krupnik.pdf) gives the needed correction. Outside historical titles and quotations, the book should prefer a specific community or language name over the dated cover term in Pullum's title.

Boroditsky and Gaby's card task supports east-west temporal layouts and the way participants' orientation maps onto those layouts. It does not by itself prove that the community uses absolute directions "for everything, at every scale" or establish the unsourced description "famously good." Those may be defensible with ethnographic and spatial-language sources, but they should not be charged to the card experiment. The [publication record](https://research.monash.edu/en/publications/remembrances-of-times-east-absolute-spatial-representations-of-ti/) describes the study's actual task and conclusion.

The color section reports Winawer et al.'s central findings accurately: Russian speakers were faster across the relevant lexical boundary, and verbal interference removed the advantage. "The most famous replicable result" is a reputation and replication claim that the original paper cannot support. The chapter can call it a widely discussed result or cite a review of subsequent replications. The [original PNAS article](https://doi.org/10.1073/pnas.0701644104) establishes the experiment itself. Witzel and Gegenfurtner tested ten versions of a lateralized category effect with 230 observers and did not reproduce the lateralization; their [Journal of Vision paper](https://doi.org/10.1167/11.12.16) supports a scoped statement about those tests rather than every possible replication.

The Pirahã discussion tracks Frank et al. closely. Visible one-to-one matching was exact, while tasks requiring memory or transformation produced approximate responses, and the smallest quantity expression could still be used at six. Calling number words "a cognitive technology" follows the paper's title and argument. "The authors' conclusion has become the field's" is a separate consensus claim and needs a review source or softer wording. The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/18547557/) supports the experimental details.

The spatial-frame exchange between Li and Gleitman and Levinson et al. is real and fairly presented as a dispute about linguistic causation and testing ecology. The statement that English speakers' landmark-dependent flip "does not happen under matched conditions" should stay attributed to Levinson's group rather than appearing as a settled finding. The [Li and Gleitman record](https://peggyli.scholars.harvard.edu/publications/turning-tables-language-and-spatial-reasoning) and the [Levinson et al. record](https://mpipsyl.disco.mpg.de/Record/PuRe.item_57830) document both sides.

### Constructed-language history

The Loglan paragraph needs direct citations for both its history and its claim that the planned experiment never ran. James Cooke Brown did begin Loglan in 1955 and introduce it in *Scientific American* in 1960. The Lojban fork and the intellectual-property dispute are also documented. The [original *Scientific American* article](https://www.scientificamerican.com/article/loglan/), the [official Lojban history](https://lojban.org/static/whatis.html), and the [Lojban account of the dispute](https://www.lojban.org/static/publications/loglan.html.out) support those points. None of these sources plainly establishes every part of "The experiment never ran. Not once" or the causal claim that community disputes consumed the decades required for it. The official history says that a small number of people temporarily reached conversational ability and that attempts to obtain research funding failed. The chapter should cite a source specifically addressing the proposed experiment or narrow the verdict to the absence of a published controlled test found in the project record.

The Láadan paragraph also needs a precise source. Suzette Haden Elgin's [account of Láadan](https://laadanlanguage.com/articles/articles-by-suzette/about-laadan/) confirms that work began in 1982 and connects the language with *Native Tongue*. Her [Láadan FAQ](https://laadanlanguage.com/articles/articles-by-suzette/laadan-faq/) supplies further first-person context. The ten-year adoption test and Elgin's reported verdict appear in secondary accounts, but the chapter says she "published the verdict herself" without identifying the publication. That sentence requires a title and page or a more cautious attribution.

The Toki Pona paragraph has no citation. The [official site](https://www.tokipona.org/) confirms the language's 2001 creation and living international community. It does not support the exclusivity of "the one small philosophical language with a living community," and other philosophical constructed languages also have active communities. Claims about testimony of gentler attention and the community's methodological care need named sources. The safest revision would describe Toki Pona as one living philosophical-language community and cite particular surveys, essays, or statements for any reported cognitive experiences.

The paragraph concluding that the clean constructed-language experiment has never been run turns three examples into a universal history. "The reason is always the same" and "Every built language that set out to test the mind lost its speakers first" require a systematic survey that the chapter does not cite. Loglan's record, Láadan's limited adoption, and Toki Pona's lack of a controlled cognitive study can support a more modest observation: the examples examined here have not produced the fluent comparative populations required for the proposed experiments.

### General statements about the field

The chapter's central position is defensible when phrased as a cautious reading of this evidence: language can affect attention, memory, categorization, and spatial habits under particular tasks, while strong claims about languages imprisoning their speakers' thought have not held up. The present references do not support the universal formulations "rejected by essentially everyone," "every surviving effect is bounded," or "the strongest grammar-to-cognition claim currently on the market." A current handbook or systematic review of linguistic relativity should support any claim about consensus across the field.

Pinker and McWhorter are genuine sources for the skeptical arguments attributed to them, but the paragraphs give detailed reconstructions without page references. Add chapter or page citations, especially for Pinker's distinction between thought and inner speech and McWhorter's Bulgarian evidentiality example. Their books can establish their arguments; they cannot establish by themselves that the field accepts those arguments.

The evidentiality section is otherwise careful. Tosun, Vaid, and Geraci found memory differences associated with Turkish direct and indirect evidential marking, including an effect among late bilinguals working in English. Papafragou et al. found that children's nonlinguistic source reasoning followed its own developmental course despite evidential morphology, and Ünal and Papafragou argue that evidential concepts are not created by grammar. The [Tosun article](https://www.sciencedirect.com/science/article/abs/pii/S0749596X13000235), [Papafragou record](https://pubmed.ncbi.nlm.nih.gov/16707120/), and [Ünal and Papafragou chapter](https://academic.oup.com/edited-volume/38177/chapter-abstract/333047784) support that balanced account. "The strongest grammar-to-cognition claim currently on the market" should still be replaced by a direct description of the result.

Slobin's "thinking for speaking" is accurately invoked as a claim about what speakers attend to while formulating speech rather than a prison around possible thought. The [book-chapter record](https://mpipsyl.disco.mpg.de/Record/MPIPL_cat.PL0070326) confirms the citation and pages.

## Revision order

1. Correct the Honoré subtitle, Freeman chronology, Morris edition, Tolkien publisher style, and Slow Media URL. These are direct bibliographic repairs.
2. Add the original Boroditsky, Schmidt, and Phillips 2003 and Chen 2013 references. Remove Fuhrman and Boroditsky 2010 from the Mandarin-vertical claim.
3. Add sources for Slow Food, Whorf's research history, Loglan, Láadan, and Toki Pona. Remove or qualify any sentence for which no adequate source can be found.
4. Revise causal and universal wording in the social-media chapter. Preserve the reported numbers while keeping each conclusion within the population, platform, task, and design studied.
5. Revise Chapter 11's consensus claims, superlatives, and constructed-language generalizations. Where the book is making its own synthesis, label it as an inference rather than making the cited authors appear to have reached it.
6. Add page or chapter locators for the extended treatments of Pinker, McWhorter, Tolkien, and any other book-length source quoted or closely paraphrased.
7. Recheck every revised sentence against the linked primary source before considering the audit resolved. The bibliographic entries are real; the remaining work is mostly about keeping the prose as exact as the evidence.
