# Active text corpus review

This ledger tracks roadmap item SEM-01C: the active Phi corpus is being reread against the complete current lexicon, its module placements, each text's source, and the job the text does for a learner. Files in `archive/` are outside scope. A correction propagated into a pending text does not mark that whole text reviewed.

## Review states

| State | Meaning |
|---|---|
| Reviewed | The Phi passage, source, notes, module choices, learning role, and active dependencies have received the full pass. |
| Preserved | A construction or wording has been examined and deliberately kept. |
| Before-state | A scenario remains unchanged because its earlier limits are part of the evidence it records. |
| Pending | No complete review has been made. A narrow dependency repair may still be recorded beside it. |

## Review method

| Check | Question that decides the disposition |
|---|---|
| Declared method | Is the work identified as a translation or a transmutation before the reader reaches the Phi passage? |
| Source and proposition | In a translation, does every source claim, distinction, image, and relation survive as closely as Phi permits? In a transmutation, is every departure deliberate, visible, and honestly represented by the back-translation? |
| Lexicon semantics | Does every content word fit its full concept and description rather than merely sharing an English gloss? |
| Module vocabulary | Does an optional term say the thought more exactly, or would it only advertise a module and burden this text's intended reader? |
| Composition | Is the existing phrase natural Phi, and does its transparency teach something a dedicated term would hide? |
| Learning role | Does the surrounding material describe honestly what the reader has already learned and what help the text still supplies? |
| Dependencies | Do compound rows, lexicon notes, excerpts, exercises, and repeated complete-text blocks agree with the reviewed passage? |
| Validation | Do the targeted validator, full validator, generated-reference check, and Markdown formatting checks pass after the decisions are applied? |

Module vocabulary is adopted when its meaning earns the place. A transparent base expression remains when it is natural or better suited to the learning path, and a before-state passage stays unchanged when its limitations are evidence.

The shelf uses two methods. A translation remains answerable to the source at every proposition; composition solves lexical differences without granting permission to rewrite the claim. A transmutation may change the source through the language's concepts and commitments, but its freedom is not vagueness. The Phi line must agree with its exact gloss and back-translation; the citation and gap log must show what shifted. Reviewing a transmutation does not turn it into a translation. It clears accidental loss, misleading back-translations, stale vocabulary, and unexamined approximation while leaving defended choices in place.

## Paired review: The North Wind and the Sun

The ground truth is the 1919 *Aesop for Children* text stored at `pamphlets/sources/aesop_for_children.txt`. The close translation uses 106 unique forms; at least 62 do not appear in the preceding primer chapters: 46 content words and 16 non-content forms. The transmutation uses 97 unique forms, with at least 57 unattested in those chapters: 42 content words and 15 non-content forms. Both renderings use base vocabulary throughout. These are attestation counts, not claims about what a learner could infer.

### Close translation

| Area | Finding | Disposition |
|---|---|---|
| Source coverage | The benchmark role requires Aesop's events and moral to survive rather than merely inspire a Phi retelling. | Every source clause has an aligned Phi block, literal back-translation, and exact adjacent citation. The translation precedes the transmutation on the shared page. |
| Quarrel and bluster | Phi has no roots for either term, while `themore` is a reasoned argument and does not fit. | Discussion plus failed agreement forms the quarrel. Heart-fire and loud shouting supply the heat and bluster without creating two narrow roots. |
| Strip and wrap | The transmutation made the winner cause the Traveler's release, which shifted the source's direct removal. Plain `lomare` also lacked the Traveler's agency in wrapping the cloak. | `lue ... wethalu leiro` makes the contestant release the garment from the Traveler. The causative makes the Traveler cause the garment to embrace them closely. |
| Gust and whipping cloth | Quivering was an intentional softening, not a close transfer of the first gust's force. | `teku kema howeli` is a short, strong wind. Passive `wapho` throws the garment's edges around the Traveler's body. |
| Loose cloak and anatomy | `luwi` cannot mean loose, and broad `menoa` alone loses the brow's location. | The Traveler causes the garment to stay `ralu`, free, on their shoulders. The brow is the face above the eyes; cap is the transparent head-garment. |
| Pulling off and throwing down | A single release loses the pull in "pulled off," while `ruemi` replaces the source's abrupt reflexive throw with an ordinary posture. | The garment is pulled from the body and then released. The Traveler throws themself toward the earth into tree-shadow for the stated purpose of escape. |
| Persuasion | `phena haolu` says kind speech but does not say that one person seeks to move another. Phi could state coercion without its communicative counterpart. | New base verb `sharemi` gives Phi persuasion while leaving refusal available. `phena` supplies the kindness that belongs to Aesop's phrase rather than to every act of persuasion. |
| Winning and failing | `thonuki` is technical failure and `thenoi` is quantitative falling short. Neither belongs in a fable's general contest result. | `porua korei`, fulfill purpose, states success against the wager's aim; its negation states failure. The translation repeats Aesop's verdict even where the plot complicates it. |
| Learning role | The fable introduces grammar and vocabulary beyond the graded primer. A second rendering could either support comparison or double the burden without guidance. | The primer sends the learner through the close translation first, then to the transmutation and comparison. Glosses and back-translations are part of the reading method. |

### Transmutation

The companion rendering answers to its own method. Its departures are deliberate, its English follows the Phi rather than repairing it toward Aesop, and the paired comparison now gives each departure a close translation beside it.

| Area | Finding | Disposition |
|---|---|---|
| Back-translation integrity | Several English lines restored source details that the Phi did not contain. `tiripe` became "whipped," `natu` became "tore," and transparent body or clothing terms became cloak, cap, and brow. | The English now follows the Phi literally. Aesop's wording remains on the next line, and the gap log accounts for the distance. |
| Time and manner | `nosa` is the noun "now," but two clauses used it as the adverb "immediately." | Both clauses now use `to reshi` for fast past action. The note teaches the distinction without narrating the correction. |
| Comparative escalation | The Wind blew more strongly, but the old response said that the Traveler also held more strongly. Aesop's relational contrast, tighter against harder, had flattened. | `mo noshi` makes the second grip closer. The two `mo` clauses now differ where the source differs. |
| Traveler's agency | The Sun and Wind agree to act on a stranger who did not join their wager. Gendered English and passive paraphrase then hid several of the Traveler's choices. | Singular they follows Phi's ungendered `shia`. The Traveler holds, opens, releases, wipes, goes away, and lies down in the aligned account. |
| Loose garment and final posture | `luwi` means flexible, not loose. `wapho` means throw, but the reflexive construction made the body sound like an object hurled into shade. | The Traveler stops holding the garment close. `ruemi` gives the final posture, while `lila` marks escape as conscious purpose. |
| The Sun's outcome | Aesop calls the Sun the winner, yet the gentle warmth only loosens the cloak. Escalating heat secures full release and sends the Traveler into shade. | Both outcomes appear. The notes treat the Sun's result as mixed. |
| Moral semantics | `puro` is neutral strength, not violent force, and `theisa` is loudness, not bluster. The former moral blamed two ordinary qualities and claimed that pressure is fruitless even though the plot shows it working. | `keloa haolu` names rough speech and `kawhera` names coercion. Good fruit answers departure instead of victory answering failure. |
| The Wind's motion | Phi gives the cloak a quiver and the Wind a pull. The source has whipping cloth and tearing effort. | The Phi stays as a deliberate softening, but the back-translation no longer borrows the stronger source verbs. |
| Giving light | `phelo` means light in weight, so it cannot carry illumination through an English homonym. | `keru loa`, give brightness, covers shining, beams, and rays as one compositional event. Genuine weight uses of `phelo` are unchanged. |
| Quarrel and argument | `themore` is an argument made of reasons, not a quarrel. Phi has no dedicated root for the source's dispute. | The interaction uses `shareo`; fire and a loud voice preserve its felt manner. Loudness itself receives no moral blame. |
| Effort and failure | `theko` is skilled craft, `riola` is purposeful labor, and `thonuki` reports failure against a technical requirement. None fits the Wind's attempt or Aesop's contest result. | All that the Wind did is `theula rena shia to phoa`. `whuo lureko` judges its immediate result without borrowing a work or systems term. |
| Wager and governance vocabulary | `repora` is a proposal put before a collective process. This exchange needs no institution. | The Sun's spoken agreement uses the optative and `nawo`. The note also identifies the missing party: the Traveler. |
| Active dependencies | The moral appears in two manual chapters, and the fable is the primer's annotated capstone. `keru loa` also reaches the compound registry and other literary texts. | The two manual citations follow the new moral. The capstone still presents the source line and back-translation as part of the reading method. |

The comparison follows all five pillars without demanding an artificial change from each. Solarpunk and preindustrial commitments find the source's material scene already close to them. Art Nouveau changes the pressure of the organic line more than its objects. Secular Buddhist attention moves from rank toward consequence. Peace linguistics produces the widest divergence: translation states Aesop's claim, while transmutation leaves strength and volume neutral and lets the Traveler's departure answer the contest.

No module word is required. Persuasion and coercion belong to ordinary social language, and the other compositions use equally general words. The paired page is still a capstone without asking a new learner to open a specialist lexicon.

## Paired review: Schleicher's fable

The source chain begins with Schleicher's 1868 German rendering in `pamphlets/sources/schleicher_1868.txt`. The controlled English source at `pamphlets/sources/schleicher_1868_english.txt` translates the complete German wording and every explanatory parenthesis, while the German retains Schleicher's square brackets for words absent from his reconstructed Proto-Indo-European text. The close translation uses 63 unique Phi forms; the transmutation uses 60. The first uses Commons `phenori` (ownership), and the second uses `pilora` (exploit), shared by Work and Commons.

### Close translation

| Area | Finding | Disposition |
|---|---|---|
| English ground truth | The common short English rendering omits Schleicher's explanations of shearing, grief, knowledge, comparative suffering, and the sheep making off. | A direct controlled translation from the German preserves all of them and supplies the aligned citation source for both Phi renderings. |
| Constricted heart | `korua se peki` carried the bodily image but silently absorbed the parenthetical grief, while conditional `lu` turned simultaneous seeing into "if." | A duration phrase makes the seeing simultaneous. Intense `nuhe` states the emotional explanation in its own sentence. |
| Great load | Plural large things lost both the singular object and the living bearer under its weight. Technical `takori` and interval-based `ritako` do not fit cargo on a horse. | New base noun `tupeka` names a burden borne by a living being and contrasts with both specialist load terms. |
| The master | Canon refuses *master* as ordinary Phi vocabulary but does not allow translation to erase source power. Current Commons vocabulary can analyze one practical relation inside the title. | The exact title stays in English; `rena lo mophira phenori phelu miona` renders a person who holds ownership of the sheep. The limit is stated plainly. |
| Worse off | `kipona` narrowed a general comparison of condition to pain. Phi still has no generic *bad* or *worse*. | The close translation reverses the comparison: the horses are more `towe`, well, than the sheep. The source's extra emphasis is recorded as a limit. |
| Field and flight | `wemo` followed the common English *plain* rather than German *Feld*, and `rashelo` contradicted its own exclusion of flight from danger. | Existing `kosha` restores the field. New base verb `phesari` names flight; `rato` and fast `pholeni` retain Schleicher's other two motion descriptions. |
| Sheep, wool, and carrying | The entries treated wool as a harmless gift, sheep as a fiber supply, and carrying as willing service. Those meanings prejudged the fable. | `mophira`, `mophi`, and `kolua` now describe the animal, material, and transport neutrally while leaving benefit, harm, and power to their own clauses. |

### Transmutation

The transmutation was written again from the controlled English source. Its source coverage matches the close translation, but each deliberate change now appears in the gap log and in the side-by-side comparison.

| Area | Finding | Disposition |
|---|---|---|
| Driving and power | Neutral causative `ka` made the horses go but could not itself judge consent or method. The earlier notes incorrectly claimed that it did. | The transmutation uses base `kawhera` (coerce) for the horses and optional `pilora` (exploit) for the sheep. Both judgments are supported by the actions that follow. |
| Refusal of the title | Simply replacing *master* with `pilu` both erased the rank and invoked a verb for receptive, mindful taking. | The title disappears from Phi but stays in the citation. Coercion and exploitation expose the relations without turning the human being into a fixed moral identity. |
| Repeated shearing | The German says the sheep no longer have wool and are shorn; habitual repetition is an interpretation rather than an inflection hidden in the source. | The transmutation deliberately adds `ro` and records the amplification. The close translation stays with unmarked passive shearing. |
| Ranking suffering | Schleicher says sheep fare worse than horses, although the animals bear different forms of labor and loss. | `lo phirae tupeka`, different burdens, refuses a common scale without denying either experience. This is the transmutation's clearest secular Buddhist and peace-linguistic change. |
| Ending | The sheep still leaves alone, while the horses stay at work. A repaired ending could easily have invented solidarity or rescue. | Flight is an unresolved response rather than a moral failure or a solution to the scene. |
| Learning role | Two optional power terms could burden an elementary reader, but replacing either with a soft base paraphrase would undo the text's central analysis. | Glosses, back-translations, and the module labels appear on the page. Base paraphrases are available through the ordinary module convention. |

The page gives all five pillars their own material question. The widest changes come from peace linguistics and the secular Buddhist refusal to rank suffering. Solarpunk, Art Nouveau, and preindustrial sections stay anchored to the wagon, fleece, garment, and living bodies.

## Translation review: The Metta Sutta

The ground truth is V. Fausböll's 1881 translation stored at `pamphlets/sources/sutta_nipata_fausboll.txt`. Every cited clause in verses 1 through 10 is represented. This includes the final claim about return to a mother's womb. The text uses two optional roots where ordinary base paraphrase would lose the source's distinction: `thesani`, skill, and `naseru`, obligation.

| Area | Finding | Disposition |
|---|---|---|
| Skill, attainment, and ability | The seeker merely knew a path, attained no state, and was wished fitting rather than able. Three source claims had collapsed into a gentler Phi summary. | Skill is `thesani` in walking toward goodness; `ki noalu kelu` states completed attainment of tranquility; `po phoa` gives actual ability. Nibbana remains visible in the exact adjacent citation as tradition-specific source material. |
| Support and burden | `henoi sano` (knowing enough) replaced easily supported. `phelo` then used the English weight/metaphorical homonym for unburdened even though its entry is strictly about weight. | Easy support is support requiring little labor. Few cares and freedom from burden are stated as few obligations and no heavy obligations. `phelo` is absent. |
| Beings and bodily states | The text claimed Phi had no word for being despite `limoe`, treated joy as an object of `phaelo`, and used fragile for feeble. | The refrain names every `limoe` directly; joy predicates with `nai`; feebleness is having little strength. Great and large remain distinct as `ru whalo` and `whalo`. |
| Family round and social judgment | The family round became taking enough among homes, while reproof became silent perception by the wise. | The practitioner habitually walks among `lumani` and does not wish to take many things. Wise people may explicitly claim that a deed is harmful. The modal retains the possibility, and speech restores the social act in Fausböll's line. |
| Deception, resentment, and enmity | The intransitive `peshu` was given a dative target, and anger, resentment, hatred, and enmity were all left as one undifferentiated heart-fire. | Deception is the instrument by which another is made mistaken. A long-time heart-fire distinguishes lingering resentment and enmity from the unqualified fire of anger and hatred. |
| The mother and her child | The source's mother became a generic parent, the danger to her life became an instrument, and the child's ownness was absent. | `thowia phao` names the birth parent. The relative clause puts the parent's own life in danger and keeps `miso ta lopia`, their own one child; Phi's quantity rule carries "only" without `li`. |
| Cultivation and direction | The source's repeated cultivation became giving or holding love, while "across" widened to an unspecified every place. | `sorila` now governs the loving heart throughout. Above, below, and across are `leo muila`, `phou muila`, and `roa muila`, each with an audible object. |
| Wakefulness and the final verse | Conditional `lu` replaced "as long as," virtue disappeared into a pure-heart image, sensual pleasure lost its greed, and the rebirth claim was omitted for supposed lexical and metaphysical reasons. | `sui waeli` gives duration, the practitioner dedicates themself to the cultivated heart, virtue acts well, perfect vision is complete insight, bodily longing ceases, and `mawha thimu ... so turema` carries the prediction of never returning to a birth parent's belly. |
| Active dependencies | The old refrain and old not-yet-born composition remained in the manual, meditation chapter, compound registry, the born entry, and three particle pamphlets with a stale wish count. | The refrain now uses `limoe`, the registry follows `wea thowia shua` and the central loving-heart compositions, and the teaching prose records the current count of thirty-one wishes. |

The English back-translation is deliberately literal. It lets a reader inspect the Phi without already knowing the language. Where the source still narrows in Phi, the notes name the loss: upright becomes honest, mean becomes harmful, and a womb is a birth parent's belly.

## Paired review: UDHR Article 1

The ground truth is the complete 1948 English Article 1 stored in `pamphlets/sources/udhr_1948.txt`. The close translation and transmutation now share one page. Two source-facing roots do work that composition could not do cleanly: `sherelo` is a normative right that can survive denial, and `sharino` is conscience as moral self-appraisal.

| Area | Close translation | Transmutation |
|---|---|---|
| Birth and equality | A second Phi sentence says that equal worth and rights are held from birth and therefore preserves the scope of the English coordination. | Freedom stays tied to birth, while equality becomes a separate standing universal claim. |
| Dignity and rights | `rolia` supplies inherent worth or dignity; `sherelo` leaves a right sayable before recognition or fulfillment. | Equal worth remains, but rights narrow to recognized `shereni` entitlements. |
| Reason and conscience | Passive `se loa` retains the endowment metaphor. Event-noun `remo` supplies a broad faculty of thought, and `sharino` states conscience directly. | `po remo` gives a capacity to think, while `korua sano` turns conscience into the heart's knowing. |
| Brotherhood and conduct | `lomea phiora` retains a sibling spirit, and reciprocal `wiso` directs the action toward one another. | People act as siblings, and `phena` makes kindness part of the observable conduct. |
| Remaining limits | `remo` is broader than rational faculty, `phiora` is less idiomatic than English "spirit," `lomea` ungenders brotherhood, and `na` is stronger than "should." | The gap log records each deliberate change, including the loss of birth scope on equality and the narrowing from rights to entitlements. |

The five-pillar comparison does not force five rewrites. Solarpunk thought tests whether a right survives institutional denial and whether an entitlement has practical form. Secular Buddhist attention shifts endowed faculties toward conditioned acts in the transmutation. Art Nouveau affects the line and repetition rather than the concepts. Peace linguistics moves the transmutation from prescribed feeling to accountable conduct. Preindustrial wisdom finds kinship and heart-knowing already present, without adding a village or tradition absent from the source.

## Paired review: Babel

The ground truth is KJV Genesis 11:1-9 stored in `pamphlets/sources/kjv_genesis.txt`. The repaired transmutation is intact as one half of the page. The new close translation covers every verse without using its seed-shaped reading of dispersal.

| Area | Close translation | Transmutation |
|---|---|---|
| Source names | Shinar and Babel stay exact beside the Phi. The passage gives the land relation and naming event without assigning adaptations. | Shinar is dropped. Babel becomes `lo haluma`, Many Languages, a semantic place-name made for this retelling. |
| LORD | The KJV title stays beside the Phi. Inside the passage, `karami` identifies the actor's authority. Legitimacy and nature are separate questions. | `muila`, the earth, replaces the source actor and needs no descent. |
| Materials | Brick is clay-stone. The KJV's bitumen becomes thick black oil whose masonry work is making stones one. | Brick stays clay-stone, while bitumen becomes mud and mortar borrows `nolami`, a mental bond. |
| Building | The builders' benefit, the tower's top, and their fear of dispersal survive. | The settlement's scale and upward reach receive more attention than benefit or top; the fear survives. |
| Human possibility | Actions the builders have imagined face no `noraku`, block. | Everything imagined can become for the builders. |
| Confounding | Language is deliberately made unfamiliar so speech from one another cannot be understood. | One language is not enough for the earth and becomes many. |
| Dispersal | Authority sends the people out from the settlement along diverging paths. | The earth uses `thiwera` to scatter people like seed. |
| Ending | The source's final explanation and repeated dispersal close the account. | Two uncited lines call every language a garden and place Phi among them. |

The lexical decision at the center of the pair is restraint. `thiwera` is not an innocent synonym for every scattering: its entry promises seed, breadth, and somewhere to grow. Translation therefore uses caused motion and leaves punishment severe. Transmutation chooses the hopeful word and accepts the change it brings. The five-pillar comparison tests peace linguistics honestly here: refusing violence in Phi cannot mean concealing violence in a source.

## Transmutation review: the original shelf pass

Before selective pairing began, the nine pending transmutations were read from their stated sources before the Phi was judged. Repair was preferred when the narrative or argument already held together. A clean rebuild was reserved for the Ring Verse's central refusal, whose earlier substitute had turned coercion into guidance and imposed binding into mutual bond. No new root was needed; the module vocabulary developed since these texts were written supplied the missing distinctions.

| Work | Source and decision | Material repairs | Pillar disposition |
|---|---|---|---|
| Babel | Complete KJV Genesis 11:1-9; repaired | Earth and sowing remain the chosen transmutation. Notes now describe that choice without claiming Phi is incapable of telling the punitive reading. | Solarpunk and Art Nouveau support the garden coda; preindustrial knowledge supports sowing; Buddhist and peace readings refuse punishment as the only account of diversity. The builders' fear and failed city remain. |
| UDHR Article 1 | Complete 1948 English Article 1; materially rebuilt | Dignity and rights no longer collapse into worth alone. Commons `shereni` adds equal entitlements, `po remo` restores a capacity to think, and kind reciprocal conduct replaces compulsory love. | Peace linguistics leaves feeling free from command while preserving obligation in conduct. Solarpunk supports durable entitlement; Buddhist thought supports equal worth. The aesthetic and preindustrial pillars require no separate change. |
| *The Little Prince* excerpts | Three short Katherine Woods excerpts; repaired | The title describes the small person from the stars while the source keeps prince. The responsibility line now retains the comitative gap required by bonding with another. | Buddhist and peace readings support mutual bond and chosen responsibility. The request and heart-seeing need no ecological or aesthetic rewrite beyond their existing images. |
| *The Prophet* excerpts | Gibran's 1923 text; repaired | The sage-title is presented as a transmutation rather than a lexical incapacity. The tree, seed, and wind express parent-child release without an armory. | Solarpunk and preindustrial practice meet in planting; Art Nouveau favors the bending tree and moving seed; Buddhist and peace readings separate love and parenthood from possession. The citation still shows the source's bow. |
| Tao Te Ching selections | Five chapters from Legge 1891; repaired | Chapter 76 includes the warning about relying on forces: trust in strength alone brings no fruit. Notes distinguish a reframe from an equivalent. | Water, vessel, wind, and yielding give all five pillars material to examine. Peace linguistics changes conquest into fruitlessness without hiding reliance on force; the other chapters retain their quiet, practical images. |
| Heart Sutra | Müller's complete smaller sutra, apart from his own abridgment and colophon; repaired | The opening now names all five aggregates instead of expanding them prematurely to all things. Release is the transmutation of annihilation, and the source term Nirvana stays beside deep peace. | Buddhist analysis governs the work. Peace linguistics shapes release without denying negation. The remaining pillars do not justify added ecological, craft, or decorative imagery. |
| Ring Verse refusal | Tolkien's quoted couplet; central Phi passage rebuilt | Rule becomes an explicit analysis as coercion; bind becomes physical `tiwa` used metaphorically. Guidance and mutual `nolami` no longer sanitize the Ring. | Peace linguistics makes the decisive change by naming constrained choice. Buddhist attention separates acts from permanent moral identities. The other pillars do not soften the source or invent a replacement moral. |
| *The Velveteen Rabbit* | Complete Williams story; repaired | Accessibility names disabled makers directly. Commons names institution and membership. Medical vocabulary distinguishes fever from contamination. Brigand-play becomes coercion-play, pain is not called small, and the child helps rather than single-handedly makes the rabbit Real. | Care, repair, natural transformation, material craft, and the story's organic beauty already engage all five pillars. Peace linguistics chiefly restores agency and names power; it does not remove fever, burning, loss, or grief. |
| *News from Nowhere*, chapters 1-3 | Complete Morris chapters; repaired chapter by chapter | Representation replaces a generic council, the railway wagon stops, mental-health judgments belong to the narrator, commoners' rights use commons entitlement, institutional authority replaces benevolent care, revenge becomes retaliation, and reactionary novels regain their political direction. | Solarpunk and preindustrial commitments are native to Morris's work; Art Nouveau lives in architecture, clothing, and craft. Buddhist attention clarifies the narrator's inference. Peace linguistics names authority and stigma without cleaning the argument, coercion, or social contempt from the story. |

The source citations and gap logs in each pamphlet hold the detailed decisions. The table records why the text remained a transmutation and whether repair or replacement was warranted.

## Literary shelf

| Active text | Method | Status | Note |
|---|---|---|---|
| `pamphlets/north_wind_and_sun.md` | Translation + transmutation | Reviewed | Paired source, back-translation, vocabulary, and five-pillar comparison complete. |
| `pamphlets/metta_sutta.md` | Translation | Reviewed | Full source-fidelity pass complete; two optional roots used where their distinctions matter. |
| `pamphlets/schleicher_fable.md` | Translation + transmutation | Reviewed | Controlled English source, paired renderings, lexical repairs, and five-pillar comparison complete. |
| `pamphlets/babel_text.md` | Translation + transmutation | Reviewed | Complete KJV alignment, translation limits, deliberate Earth and sowing departures, and five-pillar comparison complete. |
| `pamphlets/human_rights_article_one.md` | Translation + transmutation | Reviewed | Paired source alignment, two source-facing roots, translation limits, gap log, and five-pillar comparison complete. |
| `pamphlets/little_prince_excerpts.md` | Transmutation | Reviewed | Three source excerpts checked; the responsibility line gives mutual bonding its required oblique grammar. |
| `pamphlets/prophet_excerpts.md` | Transmutation | Reviewed | Three teachings checked; the planting reframe is deliberate and the gap log names its costs. |
| `pamphlets/tao_te_ching.md` | Transmutation | Reviewed | Five Legge chapters checked; the strength-of-forces warning is restored through an explicit reframe. |
| `pamphlets/heart_sutra.md` | Transmutation | Reviewed | Complete selected source checked; the opening restores all five aggregates. |
| `pamphlets/ring_verse_refusal.md` | Transmutation | Reviewed | Central refusal rebuilt so coercion and imposed tying remain audible. |
| `pamphlets/velveteen_rabbit.md` | Transmutation | Reviewed | Full story and 430 source units checked; module vocabulary repairs disability, fever, institution, and agency. |
| `pamphlets/news_from_nowhere_ch1.md` | Transmutation | Reviewed | Full chapter checked; representation, the stopped train, and source-facing gap log repaired. |
| `pamphlets/news_from_nowhere_ch2.md` | Transmutation | Reviewed | Full chapter checked; money is a concrete misunderstanding and psychiatric stigma stays with the narrator. |
| `pamphlets/news_from_nowhere_ch3.md` | Transmutation | Reviewed | Full chapter checked; Commons and Work vocabulary restore authority, entitlement, retaliation, and political direction. |

The full transmutation shelf has been reviewed. Selective paired work has added close translations where a second rendering exposes Phi's capacity or its limits without displacing the transmutation.
