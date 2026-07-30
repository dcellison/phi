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

Source-based work on the shelf uses two methods. A translation remains answerable to the source at every proposition; composition solves lexical differences without granting permission to rewrite the claim. A transmutation may change the source through the language's concepts and commitments, but its freedom is not vagueness. The Phi line must agree with its exact gloss and back-translation; the citation and gap log must show what shifted. Reviewing a transmutation does not turn it into a translation. It clears accidental loss, misleading back-translations, stale vocabulary, and unexamined approximation while leaving defended choices in place.

## Modifier-first purpose migration

D054 applies the same order to every purpose construction on the reviewed shelf: `[lila purpose clause] [main clause]`. Twelve retained attestations required reversal. This count includes the complete-text copies below their aligned examples. Their propositions and source citations remain unchanged. The Solarpunk Manifesto and the shelf's other existing purpose-first clauses already had the canonical order.

| Text | Active attestations changed | Result |
|---|---:|---|
| Babel | 2 | Intended communicative loss now precedes the act that changes one shared language into different languages. |
| *News from Nowhere*, chapter 2 | 2 | Helping precedes the offered hand; catching fish precedes the journey upriver. |
| *News from Nowhere*, chapter 3 | 2 | Listening precedes the posture behind the narrator; seeing the departure precedes arrival at the porch. |
| *The North Wind and the Sun* | 2 | Escape precedes the move into shade in the detailed translation and its complete copy. |
| *The Prophet, On Children* | 2 | Becoming like the children and the flight of the living straight things precede the actions directed towards those ends. |
| *Tao Te Ching* selections | 2 | Shaping the room precedes cutting its door and windows. |

## Translation review: The North Wind and the Sun

The ground truth is the 1919 *Aesop for Children* text stored at `texts/sources/aesop_for_children.txt`. The translation aligns every source clause with Phi, an exact gloss, a literal back-translation, and the adjacent Aesop wording. Its continuous reading has the same Phi sentence stream as the detailed blocks, and its vocabulary is entirely base.

| Area | Finding | Disposition |
|---|---|---|
| Source coverage | The benchmark must carry Aesop's events and moral rather than merely borrow the scene. | Every source clause appears once in the aligned reading. The complete Phi block and limits table make the work usable both as a sound sample and as a fidelity test. |
| Quarrel and bluster | Phi has no dedicated roots for either term. | Discussion plus failed agreement forms the quarrel; heart-fire and loud shouting supply its felt manner without turning `themore`, reasoned argument, into a dispute. |
| Clothing and weather | Cloak, cap, gust, whipping cloth, wrapping, and loose hanging require several ordinary relations. | Garment and head-garment remain transparent. A short strong wind, passive throwing of the cloth edges, close embrace, opening, and freedom preserve the physical sequence. |
| Bodily action | The source distinguishes forehead, forceful pulling, flight, and a reflexive throw towards the ground. | Base `komeri`, `natu`, `phesari`, and `wapho` keep those actions distinct. The back-translation does not borrow Aesop's stronger verbs where Phi says less. |
| Persuasion and outcome | Kind speech alone does not say that one person tries to move another; technical failure does not fit the wager. | Base `sharemi` names persuasion while leaving refusal available. Fulfilling a stated purpose and not fulfilling it carry Aesop's win and fail. |
| Completed-vocabulary retrofit | Older phrases walked around try, forehead, and flee. | Base `mesatu`, `komeri`, and `phesari` now state the source distinctions directly. Warmth, intense heat, and giving brightness remain separate. |
| Learning role | The fable reaches beyond the graded primer. | The capstone leads through the annotated blocks, then the complete reading and limits table. Glosses and back-translations remain part of the bridge. |

No module word is required. Weather, clothing, bodily action, persuasion, and coercion all belong to ordinary speech.

## Translation review: Schleicher's fable

The source chain begins with Schleicher's 1868 German rendering in `texts/sources/schleicher_1868.txt`. The controlled English witness in `texts/sources/schleicher_1868_english.txt` preserves every explanation and parenthesis, while the German retains Schleicher's square brackets for words absent from his reconstructed Proto-Indo-European text. The ordered citations reconstruct that controlled witness exactly.

| Area | Finding | Disposition |
|---|---|---|
| English ground truth | The common short English rendering omits shearing, grief, knowledge, comparative suffering, and the sheep making off. | The controlled translation from the German supplies the complete aligned witness. |
| Constricted heart | The German gives both a bodily image and its emotional explanation. | Phi states the squeezed heart and intense sadness separately, during the act of seeing. |
| Load and bodily burden | Physical heaviness alone loses the living bearer. | `tumoa` describes the wagon's weight; base `tupeka` names the burden carried by a horse. |
| Shearing | Generic cutting did not identify removal of a fleece from its living bearer. | Shared Ecological and Work `mophiku` names shearing at both source occurrences and keeps the sheep as patient. |
| The master | Phi has no ordinary person-role for *master*, but translation cannot erase the source relation. | The title stays in English. Commons `phenori` identifies a person who holds ownership of the sheep inside the Phi sentence. |
| Worse off | Phi has no generic *bad* or *worse*. | The comparison reverses: the horses are more `towe`, well, than the sheep. The limits table records the source's extra emphasis. |
| Final motion | Schleicher offers turned aside, escaped, and made off as descriptions of one departure. | Phi coordinates a turn towards the field with quick flight into it rather than making the sheep leave three times. |
| Source reconstruction | The horses' quotation and final parenthetical descriptions must remain complete. | The citation stream includes the closing quotation mark and reconstructs the stored witness exactly. |

The translation uses shared `mophiku` and Commons `phenori`. No other optional term makes the source more exact.

## Translation review: The Metta Sutta

The ground truth is V. Fausböll's 1881 translation stored at `texts/sources/sutta_nipata_fausboll.txt`. Every cited clause in verses 1 through 10 is represented, including the final claim about return to a mother's womb. The translation uses the full lexicon where the distinction fits: existing `thesani`, `naseru`, and `sharino` now stand beside `serathi`, `taleri`, and `wurashi`.

| Area | Finding | Disposition |
|---|---|---|
| Opening structure, attainment, and ability | The seeker merely knew a path, attained no state, and was wished fitting rather than able. A later repair overcorrected by imposing a universal duty to do everything that required action. | `ha thena` points forward to the source's list. `thesani` supplies skill in `welao sheraki`, `noalu ki kelu` states completed attainment of tranquility, and `po phoa` gives actual ability. Nibbana remains visible in the exact adjacent citation as tradition-specific source material. |
| Support and burden | `henoi sano` (knowing enough) replaced easily supported. `phelo` then used the English weight/metaphorical homonym for unburdened even though its entry is strictly about weight. | Easy support is support requiring little labor. Few cares narrow to obligations, while `whuo tupeka` says directly that the person is without a burden. `phelo` is absent. |
| Uprightness and conscientiousness | `wero` narrowed uprightness to freedom from knowing deception, while `thesa` reduced conscientiousness to generic care. | `serathi` names ethical integrity. Conscientiousness remains transparent as careful attention to one's own `sharino`, keeping the inward faculty and the present act visible. |
| Beings and bodily states | The text claimed Phi had no word for being, later used `limoe` as if it included people without marked distance, treated joy as an object of `phaelo`, and used fragile for feeble. | `theula miona nela theula limoe` explicitly coordinates every person with every other creature. Joy predicates with `nai`; base `huwa` names the feeble as weak. Great and large remain distinct as `ru whalo` and `whalo`. |
| Family round and social judgment | The family round became taking enough among homes, while a later repair called craving ordinary want and turned reproof into a claim about harm. | A `whau` clause places the habitual walk among families around the instruction not to act from `wurashi`, craving. Other wise people may directly `shane` that a deed is unfitting, preserving the addressee and possibility of reproof. |
| Deception, resentment, and enmity | The intransitive `peshu` was given a dative target, and anger, resentment, hatred, and enmity were all left as one undifferentiated heart-fire. | Deception is the instrument by which another is made mistaken. A long-time heart-fire distinguishes lingering resentment and enmity from the unqualified fire of anger and hatred. |
| The mother and her child | The source's mother became a generic parent, the danger to her life became an instrument, and the child's ownness was absent. | `thowia phao` names the birth parent. One proposition puts the parent's own life in danger; `sui ha pukea` keeps the protection within that danger, and `miso ta lopia` keeps their own one child. Phi's quantity rule carries "only" without `li`. |
| Cultivation, direction, and obstruction | The source's repeated cultivation became giving or holding love, "across" was rendered as around, and derived English strengthened clear to unobstructed. | `sorila` governs the loving heart throughout. Above, below, and across are `leo muila`, `phou muila`, and `thue muila`; `noraku ma` says that the heart is not blocked. |
| Wakefulness and the final verse | Conditional `lu` replaced "as long as," virtue disappeared into a pure-heart image, sensual pleasure lost its greed, and the rebirth claim was omitted for supposed lexical and metaphysical reasons. A later repair still made virtue one good act and pleasure bodily joy. | `sui theula waeli thimu` gives the full waking span. `taleri` names virtue, `sholu sorai` names complete insight, and `lo morae nirelo wurashi shena ka nai` calms craving for sensory pleasures. `mawha thimu ... so turema` carries the prediction of never returning to a birth parent's belly. |
| Active dependencies | The old refrain and old not-yet-born composition remained in the manual, meditation chapter, compound registry, the born entry, and three particle pamphlets with a stale wish count. | The refrain now uses `limoe`, the registry follows `wea thowia shua` and the central loving-heart compositions, and the teaching prose records the current count of thirty-one wishes. |

The English back-translation is deliberately literal. It lets a reader inspect the Phi without already knowing the language. The remaining material losses are stated directly: "mean" becomes contextually unfitting, anger and hatred share the settled heart-fire image, duration distinguishes resentment and enmity, mother becomes birth parent, and womb becomes a birth parent's belly.

### Current lexical rulings

The translation led to four roots. The remaining compositions fit Fausböll better than extra English-shaped labels.

| Question | Disposition | Reason |
|---|---|---|
| Upright and virtuous | Add `serathi` and `taleri` | Integrity and virtue are useful philosophical qualities with different questions: fidelity to an ethical commitment, and ethical excellence under stated reasons. Honesty and one good act no longer stand in for them. |
| Pleasure | Add base `nirelo` | Joy, liking, amusement, and contentment do not name an experience's agreeable quality. Ordinary food, touch, music, and rest make pleasure a base distinction. |
| Greediness and craving | Add `wurashi` to Philosophical Reasoning and Medical and Bodily Care | `rinu` leaves force open and `wilao` remains neutral. Craving is pressure towards satisfaction that is hard to set aside; its first-person care use must not label or diagnose the person. |
| Conscientious, non-arrogant, and reprove | Preserve transparent clauses | Careful attention to one's conscience, not seeing oneself above others, and direct telling by wise people keep the relations visible. `lerasu` would strengthen "mean" into cruelty, so `theali ma` stays with an explicit gap note. |
| Womb and birth parent | Preserve `thowia phao mokura` | `mokura` makes the bodily location concrete without pretending that belly and womb are identical. Reproductive anatomy has its own recorded return conditions and should not be settled by one traditional source. |
| Inclusive beings | Preserve `theula miona nela theula limoe` | The composition includes people without asking the normally nonhuman `limoe` to absorb them. The wider generic-organism question remains under `CV-LIFE-01`. |

## Translation review: UDHR Article 1

The ground truth is the complete 1948 English Article 1 stored in `texts/sources/udhr_1948.txt`. Three aligned units preserve both source sentences. Four optional roots keep distinctions the declaration needs: `sherelo` is a normative right that can survive denial, `remori` is reason as a faculty, `sharino` is conscience as moral self-appraisal, and `naseru` states the final obligation.

| Area | Finding | Disposition |
|---|---|---|
| Birth and equality | English coordinates freedom and equality under birth. | A second Phi sentence repeats the birth scope over equal dignity and rights. |
| Dignity and rights | Recognition cannot be allowed to create the right it acknowledges. | `rolia` supplies inherent worth or dignity; `sherelo` keeps a right sayable under denial. |
| Reason and conscience | Event-noun `remo` names thinking, not the endowed faculty in the source. | `remori` names the fallible faculty for weighing reasons. `sharino` names moral self-appraisal, and passive `se loa` preserves endowment without inventing a giver. |
| Brotherhood | Phi has no universal male class. | `lomea phiora` retains sibling spirit while necessarily removing grammatical gender. |
| Conduct and modality | Bare necessity would overstate English *should*. | Reciprocal `wiso` directs conduct towards one another, while `naseru phelu` presents a held obligation under the declaration's ethical source. |
| Learning paths | The source draws distinctions from more than one optional domain. | Philosophical Reasoning supplies right, reason, and conscience; Commons supplies obligation. The page's limits table names the remaining distance. |

## Translation review: Babel

The ground truth is KJV Genesis 11:1-9 stored in `texts/sources/kjv_genesis.txt`. The translation follows all nine verses in order. Commons `karami` and Work `noraku` and `torali` are the optional roots that the source needs; every other pressure resolves through base composition or an adjacent source identity.

| Area | Finding | Disposition |
|---|---|---|
| Source names | Shinar and Babel have no accepted Phi adaptations. | The land relation and naming event appear in Phi, while the exact names remain in their source lines. |
| LORD | The title is outside Phi, but the source actor cannot disappear. | `whu karami phelu limoe` describes a nonhuman story creature who holds authority without settling its legitimacy or nature. |
| Brick, mortar, city, and tower | Wall and oil were too broad for recurring built distinctions. | Clay-stone and thick black oil describe brick and bitumen. `whalo silawo` gives the city a human-scale form, while Work `torali` names the tower directly. |
| Renown and feared dispersal | The builders seek public recognition and build to avoid scattering. | A wish to be known by many people carries renown. Purpose-first order places the feared result before the building intended to prevent it. |
| Descent and descendants | The source gives downward motion and lineage without naming ordinary children. | Travel from sky to earth carries descent; descendants of people carry the genealogical relation. |
| Confounding | A changed language alone does not state the intended communicative loss. | Phi states one shared language becoming different languages, then gives failed reciprocal understanding as the purpose. |
| Dispersal | The KJV presents punishment, not sowing. | Authority remains the actor, `thiwera` reports scattering, and no seed comparison changes the event's force. |
| Coverage | Every KJV clause must belong to one aligned unit. | The ordered citations reconstruct Genesis 11:1-9 exactly, and the continuous Phi reading matches the detailed blocks. |

## Translation review: Heart Sutra

The ground truth is F. Max Müller's 1894 Smaller Pragñâ-pâramitâ-hridaya-sûtra stored in `texts/sources/buddhist_mahayana_texts_1894.txt`. The translation follows the complete printed text and its colophon without reconstructing lists Müller abbreviates. Philosophical `remole`, concept, is its only optional root.

| Area | Finding | Disposition |
|---|---|---|
| Names and titles | Avalokiteshvara, Sariputra, and tradition-specific terms have no accepted Phi forms. | Exact identities remain in the source lines. Phi carries reverence, direct address, awakening, and the practical descriptions around them. |
| Five Skandhas | The source names five gatherings and later distinguishes perception, conception, and mind. | The ternary count appears at first mention. `morae`, `remole`, and event-noun `remo` keep the later categories apart. |
| Form and emptiness | The equation reverses itself explicitly. | Event-noun `kire` and quality-noun `whemoa` appear in both directions rather than relying on one symmetric paraphrase. |
| Contradictory qualities | Faultless and not faultless, then not imperfect and not perfect, must all survive. | Error is absent and present. A nested headless relative preserves the double negative before completeness is denied. |
| Absence chain | Müller abbreviates parts of the doctrinal lists. | Phi follows the printed abbreviation and does not invent what the English witness omits. |
| Consciousness and fear | The source moves from annihilated envelopment to freedom and enjoyment of final Nirvana. | `waeli`, caused ending, `ralu`, and `nirelo` preserve that sequence while the limits table keeps Nirvana outside an exhaustive Phi equation. |
| Verse and crossing | The verse makes rank claims and the mantra implies one traveller. | `melira` receives the source's two comparisons. Wisdom is addressed, `thia` carries the traveller, and `kerime` gives the crossing a shore. |
| Literal English | Back-translation must not restore force absent from the Phi. | Uttered remains uttered rather than proclaimed, and edge remains edge rather than far shore. The source line retains the stronger wording. |

## Translation review: The Prophet, On Children

The ground truth is the complete On Children teaching in Kahlil Gibran's 1923 *The Prophet*, stored in `texts/gibran/sources/the_prophet.txt`. The translation begins with the request for the teaching and follows all 18 source units through the stable bow. Its derived English states only what the Phi contains, and its continuous reading has the same Phi sentence stream as the detailed blocks. Commons `phenori` (ownership) and Household `phemiru` (visit) remain its two optional roots.

| Area | Translation decision |
|---|---|
| Speakers and child relation | `miona` and `phirae miona` preserve the turn change without inventing gender; `phomila` appears on both sides of the opening denial. |
| Life and living | Noun `lioru` is personified as Life, while the source alone supplies capitalization and theological presence. |
| Belonging | Offspring stand outside the parent's `phenori`, ownership, rather than merely outside a physical grasp. |
| Cause and contrast | `whekai`, `shai`, and `thelao` restore contrast, concession, and the repeated conclusion-reason relation in Phi's required order. |
| Effort and future | `meloa` restores striving, negated `mesatu` restores attempted conformity, and `phemiru` restores the visit to tomorrow's house. |
| Archery and agency | Cord, flexibility, straightness, sharpness, flight, sending, and an approached marker describe the bow, arrow, archer, and target without adding permanent archery roots. The sender's strength and intended speed and distance remain explicit. |
| Final parallel | `senao keiro` makes the same manner of love explicit for the flying object and stable tool. |

Existing vocabulary is enough. Base `lopia` names the baby by life stage, while `phomila` keeps descent apart from childhood. The `lioru`, `liona`, `lima` family separates life, living, and being alive. Physical and relational descriptions carry the archery scene, and Gibran's cited English keeps each named object visible.

### Post-migration contextual retrofit

The repaired translation corrects a structural problem older vocabulary migration did not expose: several English possessives, conjunctions, and causal relations had survived only in the derived English. It also restores the framing request and makes the archery descriptions answer to the source more closely.

| Question | Disposition | Reason |
|---|---|---|
| Woman, babe, and he | Add the complete framing exchange with `miona`, `lopia`, and `phirae miona` | Phi does not assign gender classes. A person holds a very young child, and a different person answers, preserving the speaker change without making the two neutral pronouns ambiguous. |
| Possessor order | Replace every singular `lo thia phomila` with possessor-first `thia lo phomila` | `lo thia` is the plural second-person pronoun, not plural offspring possessed by singular you. The corrected order follows the noun-phrase template and the offspring entry's own example. |
| Love, thought, and plural thought | Add `thia` before love and thoughts and explicit `lo` before plural thoughts | The old derived English said "your" where the Phi named no possessor. The repaired Phi now carries every possessive and the source's plural thought. |
| Contrast, concession, and reason | Add `whekai` and `shai`; move each reason before its conclusion and connect it with `thelao` | Through-versus-from, with-yet-not-owned, and Gibran's repeated "For" clauses are semantic relations rather than punctuation. Phi retains them in modifier-first order. |
| Child as life stage and offspring by descent | Replace `lopia` with `phomila` | `lopia` is a person in childhood. Gibran's sons and daughters are direct offspring and need not still be children by age. |
| Life | Replace personified `liona` with `lioru` | `lioru` is the condition and course that Gibran personifies as Life; `liona` names living as an activity. |
| Striving, seeking, trying, and intending | Preserve `meloa` for strive; replace `thueli` with negated `mesatu` for seek not | Gibran first asks for sustained effort towards likeness, then warns the parent against trying to make the offspring alike. |
| Belonging and ownership | Preserve `phenori` | Gibran's belong means being possessed. Base `wema` concerns felt fit within a place, community, or relationship and does not name ownership. |
| Tomorrow's house and visiting | Preserve `wireo womu` and `phemiru` | Gibran's tomorrow is a future beyond the parent's reach, while Household `phemiru` gives the visit a bounded stay. |
| Bow, arrow, archer, and target | Replace source-invented wood and vague tool use with cord, flexibility, straightness, sharpness, explicit sending, and an approached marker | `sepho` follows Gibran's sent forth without adding the applied release of `wapho`, throw. |
| Final comparison | Add `senao keiro` | Additive `we` alone said also but did not carry the source's "even as ... so" relation. |
| Active dependencies | Update the translation, its continuous reading, the review record, and phonetic-neighbour attestations | The repaired Phi lines recur nowhere else in the active corpus. Gibran's stored source, shelf links, and registered compounds remain unchanged. |

## Translation review: The Prophet, On Work

The ground truth is the complete On Work teaching in Kahlil Gibran's 1923 *The Prophet*, stored in `texts/gibran/sources/the_prophet.txt`. The translation follows all 32 source units in order, its citation stream reconstructs the stored source exactly, and the continuous reading has the same Phi sentence stream as the detailed blocks.

| Question | Translation decision |
|---|---|
| Modifier scope | Instrumental `roe phaeli` makes tenderness the manner of sowing rather than a property of the seeds. |
| Source degree and force | `mo ko nulo` restores the inmost secret, `kema pilu` restores forceful capture of the rainbow, and caused cessation of audibility restores the worker's role in muffling. |
| Curse and misfortune | A burden arising from harmful speech stays distinct from harmful luck. Gibran's exact curse remains in the source line. |
| Proud submission | The procession accepts the endless path's guidance with pride. The source preserves the force that the relational description does not. |
| Distaste and grudge | Absence of liking replaces two incorrect uses of strong `kophinu`, disgust. The limits table states what remains. |
| Human worth | Comparative dignity follows Gibran's hierarchy and rebuttal without treating physical size as greatness. |

No new root is needed. `CV-AFFECT-10` records distaste and reluctance through preference, desire, and refusal clauses; `CV-POWER-01` keeps guidance, authority, coercion, and administrative presentation separate; `CV-SACRED-03` leaves the claimed mechanism of a curse with its religious or cultural source. The page adds no module membership, registered compound, or grammar.

## Translation review: The Prophet, On Giving

The ground truth is the complete On Giving teaching in Kahlil Gibran's 1923 *The Prophet*, stored in `texts/gibran/sources/the_prophet.txt`. The translation follows all 33 source units from the rich man's request to the earth as mother and God as father. Its citation stream preserves the source order without ellipsis, and the continuous reading has the same Phi sentence stream as its detailed blocks. The work adds `parelu`, deserve, and `thaweno`, reward, as optional roots with four module memberships.

| Question | Translation decision |
|---|---|
| Complete source boundary | All 33 source propositions and images receive a Phi unit, including the dog, well, coffer, myrtle, orchard, ocean, opened chest, witness, yoke, and wings. |
| Possessions and fear | Commons `phenori` names ownership; the careful dog hides bones in pathless sand while following people to a sacred place. Fear remains identified with need and thirst as Gibran claims. |
| Motive, pain, and virtue | Recognition, hidden desire, joy, pain, virtue, fragrance, and divine action each receive their own relation. `thaweno` preserves Gibran's reward rather than changing it into a gift. |
| Request and unasked giving | A polite whole-clause question supplies the request; `whuo ha haolu` then states giving without that speech. |
| Deservingness and worth | `parelu` carries every desert claim while `rolia` keeps naked worth distinct. The orchard, pasture, days, nights, ocean, stream, cup, courage, confidence, generosity, and opened chest remain. |
| Myrtle, baptism, God, and holy city | Exact identities stay in Gibran's citations. Phi describes a shrub releasing a pleasant smell, a sacred water ceremony, a sacred spirit, and a sacred place. |
| Giver and witness | Life gives to Life while the human giver is a person who observes. |
| Gratitude, debt, and wings | Receivers take up no weight of gratitude, rise with the giver on gifts as wings, and avoid doubting the giver's divine parentage through overattention to debt. |

The two new roots are source-led but not source-specific. A council can dispute whether someone `parelu` redress, and a workshop can describe a `thaweno` promised after an act. Myrtle, baptism, God, pilgrimage, inheritance, and Gibran's metaphysical personification remain exact source identities beside material Phi descriptions. No registered compound or grammar is added.

## Translation review: The Prophet, On Love

The ground truth is the complete On Love teaching in Kahlil Gibran's 1923 *The Prophet*, stored in `texts/gibran/sources/the_prophet.txt`. The translation follows all 35 source units in order, its citation stream reconstructs the 2,403-character normalized source passage exactly, and the continuous reading has the same Phi sentence stream as its detailed blocks.

| Question | Translation decision |
|---|---|
| Inclination and bodily state | Base `ratenu` restores steepness without making a slope fast. Base `salenu` directly names the unclothed result of threshing. |
| Existing direct vocabulary | `theisa`, `sheraki`, `henoi`, `rinu`, `nowae`, `thaeso`, `phimei`, `melira`, and `phanoi` replace physical-size words and older detours. |
| Worth and deservingness | `parelu` states that love finds its own guidance deserved; `rolia` no longer becomes a condition love tests. |
| Yielding | The listener accepts love when its wings enfold them, preserving Gibran's instruction without importing a generic submission root. |
| Crown, crucifixion, and grain-floor | The crown, tied wood, passive holding until death, pruning, threshing, sifting, grinding, folding, pressure, and sacred fire remain materially explicit. Their specialised or violent English identities stay in the citations. |
| Fragment of Life's heart | Event/result-noun `phanoi` makes the lover a small portion of Life's heart through the stated knowledge. |
| Fear and emotional wholeness | The seasonless world and incomplete laughter and tears remain as Gibran judges them. |
| Devotional close | Blessing, thanks, a song of appreciation, and intense joy describe the acts and state while prayer, praise, and ecstasy remain exact in the source. |
| Grammar and derived English | Present tense returns to the grain-floor sequence; active `phelu` keeps love as the holder; `tei` takes the event noun "your death"; reason frames precede their subjects; `shia` remains gender-neutral in English. |

The pass changed 19 of 35 units and added two base roots, with no module membership, registered compound, function word, or grammar. `CV-GRAIN-01` and `CV-DEVOTION-01` preserve the compositional decisions around grain work, prayer, and praise; existing decisions continue to keep following and kneading compositional, pruning deferred, deservingness direct, and violence-centred roots declined.

## Translation review: Tao Te Ching selections

The ground truth is James Legge's complete chapters 8, 11, 17, 63, and 76 from his 1891 *Tao Teh King*, stored in `texts/sources/tao_teh_king_1891.txt`. All 51 units align in order, their citations consume the selected source without an uncited word between them, and the continuous Phi reading has the same sentence stream as the detailed blocks.

| Area | Finding | Disposition |
|---|---|---|
| Water and six excellences | The opening moves from water's low place through residence, mind, association, governance, affairs, and movement. | Each relation remains in the translation. `kowanu` names governance, while deep stillness and association with virtuous people keep their own clauses. |
| Wheel and useful emptiness | Legge names spokes, nave, and axle as parts of one geometry. | `monaki` and the geometry carry the spokes, one centre carries the nave, and a straight strong thing sits beside Legge's axle. `ponu tholu` keeps an opening apart from a door panel. |
| Political relation | Chapter 17 distinguishes barely seen authority, praise, irresolution, reticence, and completed work. | `karami`, spoken appreciation, observed lack of confidence, speaking little, and completed undertakings preserve those distinctions without adding a ruler class. |
| Easy and difficult | Phi has no generic easy adjective. | `kethua` names difficulty and its negation supplies the easier side. Careless commitment replaces the false weight reading of a light promise. |
| Recompense | The source states a general response rather than a command to the reader. | A person gives kindness to someone who acts harmfully towards them. The limits table records the accounting sense Phi leaves behind. |
| Life and death | Dryness, completed withering, softness, weakness, rigidity, and strength remain separate. | `lioru` names life, `kurathi` names dry, and perfective `kureno` presents withering as complete. |
| Force and conquest | The source links reliance on force with failure to conquer. | Phi preserves the reliance and failed purpose while Legge's line alone supplies the military body and conquest. |
| Tree cutter | The final comparison names a role Phi does not lexicalize. | A person who cuts trees chooses the broad trunk. The source keeps *feller* exact. |

Thirteen optional roots carry source distinctions across Commons, Philosophical Reasoning, Accessibility, Systems, Ecological, Work, and Household. No new root is needed.

## Translation review: A Solarpunk Manifesto

The ground truth is the complete licensed English witness stored in `texts/sources/solarpunk_manifesto.txt`. Its five opening paragraphs and 22 numbered propositions, with proposition 18 divided into its seven listed sources and proposition 22 divided into its colon and four claims, make 38 aligned units. The ordered `solarpunk:` citations reconstruct that witness exactly. The detailed and continuous Phi passages have the same 1,127-token stream, and every derived-English line reports only what its Phi contains. The translation uses 244 unique forms, 33 of them optional roots.

| Module | Unique roots used |
|---|---:|
| Accessibility and Participation | 7 |
| Commons and Collective Governance | 11 |
| Ecological Systems and Material Life | 11 |
| Household and Daily Life | 2 |
| Medical and Bodily Care | 1 |
| Philosophical Reasoning | 1 |
| Systems and Shared Infrastructure | 11 |
| Work, Craft, and Repair | 10 |

### Full source-fidelity pass

The pass changes seventeen aligned units without altering a source citation. It repairs several clauses whose notes had been carrying source meaning absent from the Phi, removes two semantic substitutions, and makes the derived English literal again. No root is added. Capitalism, decolonialism, Jugaad, the named genres, and the named schools of art and urbanism remain analytic or source-bound because each is wider than an honest one-word Phi substitute.

| Question | Disposition | Reason |
|---|---|---|
| Complete source and parallel readings | Preserve all 38 citations; keep the continuous Phi stream identical to the annotated stream | The page remains a translation rather than a selection. The source witness can be reconstructed in order, and the continuous reading cannot drift from the analysed blocks. |
| Seeking an answer and embodying it | Use `mesatu`, attempt, for the search; state a self-sustaining society, arrival in the future, and living the way | Earlier intention language claimed a mental state rather than an effort. The repaired passage carries the civilization's sustainability, the motion endpoint, and embodiment in the Phi rather than in its note. |
| Earthy and solid aesthetics | Replace intense hardness with `patoku muralo`, solid material | Solidity is a material state. `kethua` made the aesthetic hard in intensity or effort, which was not the source contrast. |
| Calamity and struggles | Make damage and pain come upon the shared Earth in ongoing aspect | The earlier line made Earth hold abstract dangers. The repaired line keeps present turmoil while refusing to decorate calamity as a storm. |
| Real and false scarcity or abundance | State fair allocation and sharing under true conditions, then refuse support for each false claim | General advocacy for accuracy did not express the economic claim. The two counterfactual cases now appear in Phi. |
| Thoughtful provocation and achievable proposals | Replace optional `whakeru`, objection, with a thoughtful thing that makes people think; give the proposals an explicit purpose clause | Provocation need not be an objection. A separate modifier-first purpose sentence keeps the destination visible without obscuring the relative clause. |
| Valuable perspective and possible future | Give the new way of seeing a separate worth claim; keep the culture and future explicit; use potential `shua` | The former noun string did not license its relative structure, and its final line treated possibility as a property of a future rather than something that may come. |
| Smart cities and smart citizenry | Set large settlements with device-control systems against their system-literate members, then passively choose the members | Understanding alone did not express "in favor of." The contrast now includes the preference while retaining the source's exact wordplay beside it. |
| Entertainment and activism | Replace joyful play with a story's possible pleasantness, followed by advocacy | A story may entertain without itself playing. The contrast now joins an audience-facing effect to a political use. |
| Local energy grids and cultural agency | Use established `thewaki sekaru phaliso`; repeat `ha moenu` before loving Earth | Electricity transfer defines the grid here. The explicit culture subject prevents the preceding plural systems from becoming the lover. |
| Sex, gender, and sexual identity | Replace the invented "soul name" with bodies, self-description, love, and partnership | The source categories remain exact in English. Phi stays inclusive without pretending that its analytic list preserves every distinction communities make. |
| Humanity achieving social evolution | Make all people cause society to evolve; apply comparative `mo losha` to both compassion and acceptance | Potential evolution by itself removed humanity's agency. The comparison now reaches both qualities named in the source. |
| Mash-up and the seven aesthetic sources | Replace promised harmony with neutral inclusion; split bicycle wheels from quantity; name present infrastructure as community-support systems; make backend components hidden | A mash-up need not harmonize. The split bicycle clauses obey the quantity tier, while the other repairs restore the defining relations of existing infrastructure and backend design. |
| Slow destruction and learned use of science | Stop causing slow damage to Earth; state that people learned a way to act wisely with evidence-and-testing knowledge | The earlier Phi made Earth slowly die and merely held knowledge wisely. The repaired clauses preserve human action, learning, and use. |
| Final possibility | Replace result-taking `kelu` without a result with potential `shua`, come | The closing line now says that the future can enter the present rather than leaving a result predicate incomplete. |
| Optional module vocabulary | Use 33 optional roots with 54 memberships across all eight modules | Each specialist root carries a distinction active in the manifesto. The removal of `whakeru` and addition of `sekaru` change the distribution without changing the optional-root total. |
| Source boundaries and deliberate compositions | Preserve Solarpunk, the named genres, economic and political labels, Art Nouveau, Hayao Miyazaki, Jugaad, the 1800s, New Urbanism, and New Pedestrianism in the adjacent source lines | The Phi phrases expose the relation each term contributes to this manifesto. None pretends to exhaust the source identity, history, or theory. |
| Active dependencies | Update the annotated blocks, continuous translation, limits table, review ledger, and phonetic-neighbor attestations | The source citations remain byte-for-byte unchanged. The revised annotated and continuous Phi passages contain the same sentence sequence. |

## Translation review: The Little Prince excerpts

The page translates three short passages from Katherine Woods's 1943 translation: the sheep request, the fox's secret, and the responsibility that follows taming. A compact source file stores the three quoted excerpts so citation validation can test every `woods:` line. The title and five interlinear units contain seven complete assertions and use 40 unique forms.

### Source-led rebuild

The page was translated afresh rather than repaired around its former relational reframe. Each Phi assertion was checked against Woods's wording, its exact gloss, and its derived English. The result preserves taming as taming, records the narrower and wider meanings that do not align exactly, and adds no root.

| Question | Disposition | Reason |
|---|---|---|
| Source witness | Store the three quoted excerpts and register `woods:` citations | Every reproduced source fragment now has an exact local witness. The page does not claim coverage beyond those three passages. |
| Draw me a sheep | Preserve `pi no wei mia ta mophira kire` | Polite imperative `pi no` carries the courtesy, `wei mia` names the recipient, and `kire` has an established drawing sense while retaining shape as its exact gloss. |
| And now; simple secret | Add `sheno nosa`; turn the apposition into a second complete identity clause | `sheno` preserves the additive opening and `nosa` its present turn. Phi does not ask the colon alone to carry an incomplete clause. |
| See rightly | Preserve `miona li roe korua po theali nila` | Restrictive `li` remains on the heart as instrument, and `theali` makes the seeing fitting for its purpose rather than asserting infallible perception. |
| Invisible to the eye | Preserve `whu noetha nai roe mirae se po ma nila` | The essential thing remains the subject. Singular eye and passive potential negation preserve Woods's proposition. |
| What you have tamed | Use `whu thia woenu ki ka kelu nolika` | Perfective causative becoming states that the listener made an animal tame. The explicit animal narrows Woods's open relative but gives the Phi relative clause an audible boundary. |
| Forever and responsibility | Use `naseru pa phelu`, then restate the held obligation under `theula thimu` | Inchoative holding preserves the beginning of responsibility, while the second sentence gives it unbounded duration. `naseru` states an obligation under the fox's teaching without adding the willing acceptance built into `thonai`. |
| Title and rank | Preserve `thiku miona lue silero` beside the source title | The English keeps Prince exact. Phi describes the small person from the stars without creating a general rank word. |
| Optional module vocabulary | Use shared Commons and Work `naseru` | Responsibility as obligation is the specialist distinction the final excerpt needs. All other forms remain base or function vocabulary. |
| Active dependencies | Update the page, source registry, catalogue, renderer contract, teaching references, review ledger, progress records, and phonetic-neighbour attestations | The detailed and continuous Phi streams must remain identical, and every Woods fragment must match the compact witness. |

## Transmutation review: the Ring Verse refusal

The page quotes Tolkien's inscription and answers it with four Phi lines rather than promising a translation. Its title and passage use 17 unique forms, all from base or function vocabulary. The first shelf rebuild correctly separated coercion and physical tying from guidance and mutual bond, but it widened the contextual **them** to all people. The stricter pass repairs that referent without softening the refusal.

### Post-migration contextual retrofit

The first retrofit left the four Phi lines unchanged. It brought the surrounding explanation into line with the completed Commons vocabulary and corrected one old account of `meipa`, seat.

| Question | Disposition | Reason |
|---|---|---|
| Rule and dominion | Preserve `kawhera`; distinguish `nasholu` in the explanation | `nasholu` is a social prescription. Tolkien's verb makes one being dominate others. `kawhera` identifies the practical choice that power closes without inventing a neutral dominion verb. |
| Authority, enforcement, and control | Do not insert `karami`, `nashaku`, or `ketora` | A holder may exercise `karami` within a social scope, but the noun leaves legitimacy open. `nashaku` acts in relation to a rule or decision. Systems `ketora` adjusts a technical process and says nothing about authority over people. Any of the three would tidy the Ring's act into the wrong kind of relation. |
| Binding and mutual bond | Preserve metaphorical `tiwa` and reject `nolami` | `tiwa` keeps the image bodily through fastening with a flexible line. `nolami` belongs to participants who form or sustain a mutual connection. The Ring imposes restraint; it does not enter a relationship. |
| Ring and darkness | Preserve `thumai sorui` and quality-noun `nuelo` | Finger-circle is the registered ordinary composition for a ring. Under the regular adjective rule, `nuelo` also covers darkness as a noun. Neither expression hides a source distinction or needs a specialist root. |
| Throne and seat | Keep throne in the source; correct the account of `meipa` | `meipa` is an object or prepared place made for sitting and may be reserved or exalted. It is audibly related to `meilo`, sit, but it is not that verb with a place suffix. Raising a seat does not give its occupant an unmarked dominion role. |
| Optional module vocabulary | Use none in the Phi lines | Commons vocabulary improves the analysis, not the transmutation. The verse's coercion, finding, bringing, darkness, and physical restraint are already expressible in ordinary Phi. |
| Source and active dependencies | Preserve Tolkien's quotation and synchronize the two repeated Phi lines | The source remains outside Phi byte-for-byte. The first and fourth lines recur in book chapter 2; the former chapter 6 duplication is no longer present. Canon's stale claim that the refusal uses `kulo`, `theluo`, and `nolami` also requires correction. |

### Full source-fidelity pass

The stricter pass changes all four Phi lines because their shared target was too broad. It keeps the quoted inscription unchanged, identifies the people reached through the other Rings, restores the source's alternation between **all** and **them**, and states openly that Phi has changed four infinitive purposes into present accusations.

| Question | Disposition | Reason |
|---|---|---|
| Scope of the source witness | Keep the short inscription as the only quotation; discuss the surrounding stanza without reproducing it | The quoted words suffice for the refusal. The other Rings establish the antecedent, while lord and throne belong to the surrounding source context rather than to the quoted inscription. |
| All and them | Use `theula whu phirae thumai sorui wenuha miona` in the first and third lines, then `lo shia` in the second and fourth | The old `theula miona` meant every person, a claim the source does not make. The headed relative follows dominion through the other Rings to everyone wearing a different finger-ring. The pronoun retains that set where the source says **them**. |
| Purpose and accusation | Preserve the deliberate move from infinitive purpose to unmarked present clauses and record it in the introduction and gap log | A translation would present what the One Ring is for. This refusal instead accuses it of coercing, finding, bringing, and tying. The grammatical shift belongs to the transmutation and must not pass as accidental equivalence. |
| Rule, authority, and dominion | Preserve `kawhera`; keep `nasholu`, `nashaku`, `karami`, `kulo`, and `theluo` in the analysis | None of the neighbouring social relations means dominion. `kawhera` names the closing of practical choice without granting the Ring a legitimate role. |
| Bind and bond | Preserve metaphorical `tiwa`; reject `nolami` | The physical tie remains an uncomfortable image of imposed restraint. A mutual bond would reverse the relation at the heart of the refusal. |
| Optional module vocabulary | Use none | All 16 passage forms are base or function vocabulary. The relative clause needs no wearer role, specialist title, or new root. |
| Active dependencies | Update the page, canon, book chapters 2 and 7, catalogue summary, sample-text description, review ledger, vocabulary decision register, progress records, and phonetic-neighbour attestations | The source quotation remains byte-for-byte unchanged. Book chapter 2 repeats the first and fourth Phi lines, while chapter 7 states the form count and describes the gap log. |

The refusal remains narrower than silence. Peace linguistics leaves the domination exposed while testimony stays possible. The Ring remains an instrument of coercion and imposed tying, not an office the lexicon makes clean.

## Translation review: The Velveteen Rabbit

The complete Williams story is now a translation with 429 exact source fragments across 427 aligned Phi stanzas. The citation stream reconstructs the stored story exactly and in order. Optional vocabulary enters through six modules, with Household vocabulary doing most of that work.

### Post-migration contextual retrofit

Forty-six aligned units changed in the earlier retrofit. The source lines remained byte-for-byte unchanged. Most repairs replaced an old paraphrase that had become inaccurate after the base lexicon grew; a smaller set let module vocabulary name familiar objects in the nursery and sickroom. At that stage, the story kept its declared changes around rank, coercion, gendered kinship, military source language, clock time, and the Child's share in making the rabbit Real.

| Question | Disposition | Reason |
|---|---|---|
| Searching and finding | Use `sheraki` for Nana's candle search and the rabbit's unsuccessful search for the Fairy; keep `hekawi` where something is found | `hekawi` records discovery and does not contain a search. The old notes claimed otherwise, which made success appear in two source moments where Williams gives none. |
| Age and wear | Use `serao` for age and `rohemi` for wear from handling | Williams often says both "old" and "shabby." The revised clauses can now preserve both. The Skin Horse's lesson, the threadbare coat, the Fairy's worn toys, and the shabby nose all concern wear rather than age alone. |
| Love, liking, eagerness, and excitement | Use `kaeli` for liking and `rashowe` for excitement; preserve `lothea` and `therua` where love or readiness is meant | The child grows to like the bed and likes the rabbit comfortable. The wild rabbit dislikes dancing. None of those is love. Excitement also has its own glad energy, while eagerness prepares for a wanted act. |
| Bodily qualities and sensations | Use `welua`, `kiparu`, `kathoru`, `sukaro`, `wiloru`, `tiphori`, and `sikoru` | Fragility, joints, the jaw beneath the chin, intense heat, dizziness, body-wide tingling, and an itch no longer need phrases that blur their physical distinctions. The back-translations show where Phi still narrows Williams's wording. |
| Ordinary household objects | Use Household `komalu`, `wethamo`, `lirupa`, and `phelasi` for pillow, blanket, sack, and shelf | These are ordinary within the module's learning path and exact in this nursery. Base `koma nuwera`, head-bed, remains a valid core paraphrase for a pillow; the direct module word does not retire it. |
| Material and household work | Use `liru`, shared `whemori`, shared `riporu`, and `tupeka` | Plush is fabric, not necessarily wool. The sack holds rubbish, the gardener has tasks, and searching for a missing china dog is a burden rather than physically heavy craft. |
| Conversation, preparation, planning, and commitment | Use `thorelu`, `thilonu`, `winora`, and `seru` | The rabbit misses ordinary talks with the Skin Horse. The seaside arrangements were prepared, the rabbit planned his future games, and the gardener promised a future course on which the household relied. |
| Difficulty, scent, boredom, and attention | Use negated `kethua`, fitting `theali`, `moshaki`, and `theonu` | Easy is not the English homonym *simple*, and a scent is fitting rather than accurate. The sickroom is boring because nothing can be done. The excited child scarcely attends to the new rabbit rather than losing the ability to think. |
| Loneliness and commonplace status | Use settled `sonu nuhe`; replace the misuse of `siloma` with a second ordinary sentence | Loneliness composes from aloneness and sadness. Phi still has no useful core adjective for "commonplace," so the other toys make the rabbit feel small and leave him merely one toy among them. |
| Picture-books and transparent compounds | Use `kire shelu`; preserve the other compounds that still teach | A picture is a made shape, not necessarily a coloured one. Compounds for velveteen, sawdust, the mainspring, pearls, the wheelbarrow, and the story's other material images remain expressive rather than obsolete. |
| Optional module reach | Use 13 distinct roots with 18 memberships across six modules | Commons contributes `punoki` and `wemari`; Ecological contributes `hisophi` and `whemori`; Household contributes seven roots; Medical contributes `hisophi` and `suloru`; Systems contributes `nurako`; Work contributes `hisophi`, `kolai`, `riporu`, and `whemori`. No Philosophical or Accessibility root is forced into the story. |
| Source boundaries and peace linguistics | Preserve the exact Williams witness and the established transmutation choices | The citation still contains soldiers, Government, brigands, burning, illness, and grief. Phi names disability, institution, coercion-play, fever, and contamination without erasing the source events or turning pain into a moral lesson. |
| Active dependencies | Update the story notes, gap account, review ledger, and progress records | All 430 source lines remain unchanged. The revised Phi, exact glosses, and English back-translations pass the targeted example validator. |

### Full source-fidelity pass

The stricter fidelity pass changed 69 of the 427 Phi stanzas and added base `tinemu` (ant). The source witness then reconstructed Williams's complete stored story exactly and in order. The count fell from 430 citation fragments to 429 because the question "What is REAL?" and its following scene-setting tail returned to their one original sentence; the aligned stanza count fell from 428 to 427 with it.

| Question | Disposition | Reason |
|---|---|---|
| Williams witness | Remove the Timothy and tear ellipses, remove the Timothy overlap, restore dialogue quotation marks, and reunite the reversed "What is REAL?" sentence | Every source character now appears once and in source order. Timothy's joints, the three-part tear sentence, and the relation between the Rabbit's question and its setting no longer depend on editorial punctuation or repetition. |
| Full-sentence grammar | Repair all 22 baseline parser diagnostics | Obligation follows the quality it scopes, quantity and degree particles precede Slot 1, complement content precedes its predicate stack, quoted material reaches a licensed speech verb, and direct thought no longer borrows a quotation frame. The targeted sentence validator reports no errors. |
| Claims, models, and roles | Use `sherewa`, optional `reteru`, headed `kiparu`, and ordinary role descriptions | Mechanical toys claim they are Real. The cloth rabbit can deny being a model, Timothy retains his joints, and Williams keeps Nana, soldiers, Government, and Fairy in the adjacent source. |
| Worth, care, and bodily change | Use `rolia` and `sone`; retain pain and wear as separate facts | The Skin Horse says loose joints and a worn coat do not alter worth. Later clauses state what the Rabbit values and how little he values other people's view, rather than treating care as an absent thought or declaring bodily change small. |
| Specific material and motion | Restore the railway device, brown sweet almonds, unspecified seasons, dragging, mud over the whole body, rubbing, sudden onset, a neck stretch, a nose wrinkle, folded ears, the berry thicket, lifting, dingy velveteen, sideways jumps, and round eyes | Each item had either disappeared from Phi, been weakened in derived English, or been assigned a neighbouring word with a different centre. Existing base and module vocabulary carries all but the ant. |
| Ant | Add base `tinemu` and use it at all three appearances | The recurring animals are part of the story's visual thread. Generic `nireku` flattened that thread and made the notes claim, incorrectly, that the species did no later work. |
| Speech and thought | Route shouted quotations through instrumental `kapura`, keep direct thoughts outside `sha ... sho`, and restore the wild rabbit's two source questions | Speech frames now close on `haolu`. The Rabbit's cries remain cries, while thoughts remain thoughts and the derived English no longer invents a third question. |
| Source-detail boundaries | Keep exact engine, chocolate almond, raspberry, sateen, shawl, pearl, emerald, crab, and role identities in Williams | Phi describes the visible material, use, colour, shape, or relation when that helps. One literary witness does not turn each English or cultural label into a reusable root. |
| Optional module reach | Use 14 roots with 19 memberships across six modules | Household contributes six roots and shares `whemori`; Ecological contributes `reteru`, `hisophi`, and `whemori`; Systems shares `reteru` and contributes `nurako`; Commons contributes `punoki` and `wemari`; Medical contributes `hisophi` and `suloru`; Work contributes `hisophi`, `kolai`, and `whemori`. No optional word enters merely to raise the count. |
| Active dependencies | Update the story, vocabulary, decision register, generated references, shelf renderer count, review ledger, roadmap, handoff, and phonetic-neighbour attestations | The new root passes the lexical ceiling, character and phonetic collision checks, retired-form check, and English-homonym review. The complete Phi, gloss, back-translation, and source structure remains machine-checked. |

### Translation conversion

D081 changes 29 aligned stanzas and presents the work solely as a translation. It also adds a continuous Phi reading assembled from the same 427 units. No source fragment, lexicon entry, module membership, registered compound, or grammatical rule changes.

| Question | Disposition | Reason |
|---|---|---|
| Splendour and charm | Use `ru mioru` and record the narrower result | Beautiful preserves the favourable appearance without inventing radiance. The limits table states that Phi does not distinguish the source's splendour from its charm. |
| Expense and price | Describe toys that require more things in exchange | The relation behind greater expense remains explicit without adding money or price vocabulary. Williams keeps the compact economic category. |
| Pretence | Use `peshu` for knowingly false claims | The mechanical toys and Timothy no longer merely claim their status. The Phi states the source's pretence without creating a separate verb for social performance. |
| Soldiers and Government | Describe disabled makers who belong to a group acting through force, and an institution of society's governance | Disability, organised force, membership, institution, society, and governance remain in Phi. The exact military role and capitalised political identity remain in Williams rather than becoming ordinary Phi titles. |
| Love, play, pain, handling, and Real | Restore play as the excluded purpose, endurance through pain, careful gentle keeping, and permanent Real state | The earlier rendering replaced Williams's claims with guidance by pain, caregiving, and inherent worth. The translation now follows the Skin Horse's actual lesson without calling pain small, deserved, or spiritually useful. |
| Nana, hatred, and brigands | Use nursery authority, dislike with heart-fire, and coercion-play | The source's power and aversion remain visible. Phi does not coin ruler, hatred, brigand, or combat-centred roots for one story. |
| Time, tea, colour, and bodily action | Restore the first night and later nights, tea as a meal, rubbed-away pink, low-voiced grumbling, a forceful foot-noise, and joy in using hind legs | These details were expressible in current Phi and no longer needed approximation. Exact clock duration and calendar names stay in Williams. |
| Scope and comparison | Restore ceasing to be Real, anything in the world, the unchanged strength of love, a warm deep jungle, and a flower needing no change | The revised clauses carry distinctions that the earlier back-translations had supplied more fully than the Phi. Tropical and perfect remain narrower descriptive renderings named in the limits table. |
| Complete reading and source witness | Keep the continuous reading identical to the detailed units and retain all 429 source fragments in order | Readers can hear the story without the apparatus, while every interpretive decision remains inspectable against Williams. |
| Vocabulary boundary | Add no root | Existing base and module vocabulary can carry the story. Expense, military service, government, hatred, brigandage, exact time, named products, and gem identities remain transparent descriptions or source-bound terms where Phi's philosophy does not support a general lexical root. |
| Active dependencies | Update the story, catalogue, teaching references, shelf renderer contract, review ledger, progress records, handoff, and phonetic-neighbour attestations | Targeted validation checks the Phi, exact glosses, continuous reading, citations, and source reconstruction before full repository validation. |

## Transmutation review: News from Nowhere, chapter 1

Morris's first chapter has 85 aligned source units. The revised Phi uses 232 unique forms. Six optional roots enter through four modules: Commons and Collective Governance, Household and Daily Life, Philosophical Reasoning, and Systems and Shared Infrastructure. The chapter needs those distinctions, but it still does most of its work in base vocabulary.

### Post-migration contextual retrofit

Twenty-nine aligned units change. Every `morris:` line remains byte-for-byte unchanged. The repairs are concentrated where the earlier rendering had stretched a familiar root beyond its present meaning or worked around a distinction that the completed lexicon can now state directly.

| Question | Disposition | Reason |
|---|---|---|
| Views, membership, and authority | Use `phelu` for holding a view, Commons `wemari` for alliance membership, and Commons `karami` for authority | `shalori` represents people or groups, not thoughts. The man belongs to the alliance without becoming a council officer, while the Anarchist position is rendered as a wish that no individual hold authority in society. |
| Claims, attempts, volume, and arguments | Use `sherewa`, `mesatu`, `ru theisa kapura`, and Philosophical `themore` | Friends put forward claims, participants attempt to speak together, the outburst is explicitly very loud, and the narrator later turns over arguments rather than generic thoughts. Each source act keeps its own strength. |
| Noise, farewell, and coerced travel | Use `mosha`, quoted `pao`, and `kawhera` | Noise and quiet occupy periods. A spoken goodbye is no longer inferred from `pholeni`, depart. Morris's claim that civilisation forced railway travel into habit is named as coercion before the consequence and custom are stated. |
| Discontent, sadness, and disgust | Use negated `nuloe`, `korua nuhe`, and `kophinu`; preserve `wipha` for the later bodily restlessness that falls away | The carriage mood, sadness, disgust with oneself, and inability to settle are related in the scene but not interchangeable in Phi. |
| Winter, room heat, cloud-flecks, and shabby wear | Use `shila`, Household `tholupi`, `piloe`, and `rohemi` | Winter no longer depends on a frost-season paraphrase. A heated room, scattered cloud-spots, and a worn suburb no longer borrow the meanings of warmth, light physical weight, or age. |
| Observation, river motion, waking, and enjoyment | Use `somela`, `tiripe`, `nowae`, `waeli`, and `kaeli` | Morris asks the man to note the river, distinguishes glitter from swirl, wakes him twice, calls him wide awake, and lets him begin to enjoy the condition before the tale amuses him. The revised forms preserve those steps. |
| Ease and structural simplicity | Use negated `kethua` and retain `siloma` for uncomplicated structure | The closing claim is that first-person telling will not be very difficult and will feel more natural. English *easy* no longer pulls `siloma` away from its actual centre. |
| Transparent compositions and source boundaries | Preserve `suro repha`, `pelowa muila`, `nurako lokue`, the underground-railway relative clause, and source-only London names and exact measures | These expressions remain clear Phi rather than obsolete detours. The Thames, Chiswick Eyot, the suburb category, a five-minute walk, and clock hours remain exact in Morris's adjacent witness. |
| Optional module reach | Use six roots with six memberships across four modules | Commons contributes `shalimo`, `wemari`, and `karami`; Household contributes `tholupi`; Philosophical contributes `themore`; Systems contributes `nurako`. No other module is imported merely to increase coverage. |
| Active dependencies | Update the chapter notes, review ledger, progress records, handoff, and phonetic-neighbour attestations | All 85 source units retain their exact Morris lines. Chapters 2 and 3 carry the river, name, and authority choices forward in their own completed passes. |

## Transmutation review: News from Nowhere, chapter 2

Morris's second chapter has 241 aligned source units. The revised Phi uses 361 unique forms. Five optional roots enter with seven memberships across four modules: Accessibility and Participation, Household and Daily Life, Systems and Shared Infrastructure, and Work, Craft, and Repair. The room, meals, and limits of work earn that vocabulary; the rest of the chapter remains largely in the base language.

### Post-migration contextual retrofit

Fifty-seven aligned units change. Every `morris:` line remains byte-for-byte unchanged. The longer count reflects the chapter's length and its accumulation of small distinctions. Searching does not promise discovery. The bugle also parts company with the flute, to the probable relief of both.

| Question | Disposition | Reason |
|---|---|---|
| Waking, sleep, and relief | Use `nowae`, `tupeka`, and `meraho` | Waking receives its direct verb, sleep can be the burden the narrator cannot shake, and fresh air brings relief without requiring a falling-weight paraphrase. |
| Awareness and bodily sensation | Use `selua` and `wiloru`; retain `waeli` for the wider waking state | Awareness of the place, dizziness, and full consciousness are distinct claims. The narrator's clear mind remains a further sentence. |
| Search, material, form, and wear | Use `sheraki`, `teshilo`, `luwae`, `phiro`, and `rohemi` | Eyes search without guaranteeing discovery, and Bright is still looking for work rather than finding it. The clasp is steel, the bridges have graceful and elegant form, and exposed stone weathers without being declared damaged. |
| River life and landscape | Give `kawepa` its salmon object, use `thelomi` for the lake, and retain `pilomu` for Morris's tree label | `kawepa` reports the net meeting the moving fish and leaves what follows to another clause. Lake need not borrow pond, while the sycamore entry deliberately leaves exact species to the source or local name. |
| Tide and service | Use `lunisa` through the river scene and `pheloma` for the work done for another person | Flood, ebb, the boat held against the tide, and Dick's guess now keep the tidal cycle in view. Both speakers describe the ferrying as service rather than reducing it to a particular act of help. |
| Difficulty and simplicity | Use negated `kethua` for easy passage or escape and positive `kethua` for troublesome custom and hard acceptance; retain `siloma` for the garment's simple construction | English *easy* no longer pulls simplicity into effort. The one remaining `siloma` describes structure, which is its proper work. |
| Guidance, workload, and ordinary acts | Keep `kulo` as an action with participants visible, use `pushali` for work beyond present capacity, `pilewa` for the clasp's making, and `rohi` for rubbing hands | The proposal is to guide a person, not to transform into an abstract guidance. Overload leaves the work meaningful. `pilewa` names the crafted piece, and rubbing differs physically from wiping. |
| Rooms, blankets, and meals | Use Household `tholupi`, `wethamo`, and `nurome` | The hot interior is a room, bedclothes are blankets, and breakfast or dinner is a meal rather than food in general. These are ordinary details, which is precisely why the Household module has them. |
| Industrial and musical source detail | Compose the missing riveting and hammering sounds; replace `phui` with `thiku shioli howeli haoni keli` | Metal fastening and hammer contact restore Morris's vanished works. The bugle remains exact in the source line while Phi describes a small silver wind-voice device rather than falsely calling it a flute. |
| Measures, names, and transparent compositions | Add `pai` to the century estimate; preserve exact 2003, London names, `kerou loriphi`, `whelina sholei`, `halemu womu`, and all three `ne` names in their established roles | The narrator needs an approximate elapsed duration, while Morris's exact date stays outside Phi. Stone rainbows, grass-gathering, and the remembering-house still reveal useful relations. |
| Optional module reach | Use five roots with seven memberships across four modules | Household contributes `tholupi`, `wethamo`, and `nurome`; Work contributes `kolai` and shares `pushali`, whose Accessibility and Systems memberships reflect the same capacity distinction. No module enters for decoration. |
| Active dependencies | Update the chapter notes, review ledger, coverage record, roadmap, handoff, and phonetic-neighbour attestations | All 241 source units retain their exact Morris lines. Chapter 3 inherits the river, name, work, and source-boundary choices and completes the literary shelf. |

## Transmutation review: News from Nowhere, chapter 3

Morris's third chapter has 245 aligned source units. The revised Phi uses 406 unique forms. Fourteen optional roots enter with 15 memberships across five modules: Accessibility and Participation, Commons and Collective Governance, Ecological Systems and Material Life, Household and Daily Life, and Work, Craft, and Repair. Breakfast and the weaver's trade give those words honest work; most of the hall still speaks in base Phi.

### Post-migration contextual retrofit

Forty-six aligned units change, and every `morris:` line remains byte-for-byte unchanged. A breakfast becomes a meal, a listener listens, and the mechanical weaver finally gets a loom. The pass coins no new root.

| Question | Disposition | Reason |
|---|---|---|
| Recognition, rooms, texture, and material | Use `miratu`, Household `tholupi`, `wuloe`, and `muralo` | The narrator recognizes the frieze, arches lead into rooms, fresco lies on physically soft clay, and material no longer borrows the general noun for thing. |
| Clothing, age, and health | Use `tholua`, retain `siloma`, and use `wolu` | The dress keeps an ancient form and a later simple form without inventing the numbered century in Phi. Health is an inferred bodily condition rather than a report that the hosts feel well now. |
| Breakfast, size, and quality | Use Household `nurome`, base `ponalu`, and Work `kirero`; retain `nuora` for the food | The occasion is a meal, while the roses differ in the two respects Morris states. Food remains what is cooked and placed on the table. |
| Anxiety, reasons, truth, and responses | Use `weshoru`, `remotha`, `theloa`, and `lonae` | Anxiety need not borrow fear, a literary reason is still a reason, truth is a noun in the guarded lie, and answering is a return turn rather than hearing or giving words. |
| Forest scale and listening | Replace physical `whalo` with `sheloi` houses and use `sheluo` | Morris's clearing is great because many houses were removed. The nearby host comes to listen, an attended act, rather than merely receiving sound. |
| Awareness, search, and bodily detail | Use `selua`, `sheraki`, `meraku`, `meshoi`, `phimei`, and `kiparu` | The weaver is almost aware of his breach, compliments are sought without being found in advance, and brain, cheek, lip, and wrist keep their source distinctions. |
| Craft, interest, skill, and steel | Use `theko`, `mewali`, Work `weloa` and `thesani`, and `teshilo` | The weaver discusses a craft that interests the narrator, works at a mechanical loom, admits little hand skill, and leaves iron out of Dick's steel. |
| Greatness, dignity, and friendship | Use intensifier `ru`, `thunoa`, and established `phirae melu` | Great beauty is intense beauty rather than physically large beauty. Gold looks dignified, while his friends are special in the same phrasing chapter 2 established. |
| Notice and handiness | Use `morae` and Accessibility `kelasu` | The carriage catches the narrator's notice and proves handy in use. Low weight remains a separate quality under `phelo`. |
| Transparent compositions | Keep stone rainbows, the fire-blowing device, the gray horse, the old oar-man, and the description of lead by inferred weight | These phrases remain more revealing than a narrow label. The exact metal and vanished occupations stay available in Morris's adjacent witness. |
| Optional module reach | Use 14 roots with 15 memberships across five modules | Accessibility contributes `kelasu`; Commons contributes six roots; Ecological contributes `telo`; Household contributes `nurome` and `tholupi`; Work contributes five roots and shares `telo`. No module is added merely to raise the count. |
| Source boundaries and peace linguistics | Preserve Morris's exact dates, places, gendered sorting, armor, and fighting language beside the established transmutation choices | Phi reports authority, harm, retaliation, and guardianship without cleaning the narrator's politics or importing martial vocabulary for the golden coat. |
| Active dependencies | Update the chapter notes, review ledger, progress records, handoff, and phonetic-neighbour attestations | All 245 source units retain their exact Morris lines. The literary retrofit is complete, and the drafted-book review now carries its method and vocabulary forward. |

## Contextual review: the drafted Phi book

The drafted book comprises its cold open, chapters 1 through 7, and chapter 11. Eighteen fenced Phi examples appear across six of those files, with inline forms carrying the language through the others. Sixteen blocks remain exact, including the three Babel passages quoted in chapter 7. Two in the cold open change: service receives its direct word, and Dick's full answer now carries the tide into the Phi quotation.

### Post-migration contextual retrofit

The review keeps the garment-and-hand composition, changes no source quotation, and coins no root. Its largest repair is explanatory. `wia` can ask about a count or an amount, so Dick's difficulty is the missing referent supplied by a vanished payment custom, not a grammatical demand that everything become countable. Later chapters also shed three claims inherited from the old lexicon schema: sound symbolism and pillar rationales are optional, while articulatory notes do the required physical work.

| Question | Disposition | Reason |
|---|---|---|
| Service and help | Replace `naphe` with `pheloma` in the quoted expectation and both dependent novel units | Morris names service, and Phi already distinguishes work done for another person's use from help offered to a particular activity. The narrator's assumption remains marked by `ho`. |
| Quantity and the missing object | Describe `wia` as a quantity gap for counts or amounts | A numeral, estimate, quantifier, or unknown answer may fill the gap. The bare question becomes puzzling because the narrator assumes a payment custom that Dick does not share. |
| The tide | Add the complete reply with `lunisa` and carry the same root through the dependent river scene | The joke lands on Dick's guess. Showing only his failure to understand left out the answer on which the cold open depends. |
| Translation and transmutation | Name the method accurately and remove the claim that Phi produced Morris's joke without prompting | Morris supplied the misunderstanding. Phi changes its wording under a declared transmutation and exposes the missing economic expectation without claiming authorship of the joke. |
| Transparent composition | Retain `muo wethalu manuwe sepho` for putting a hand into the garment | Phi has no pocket noun, and the composition preserves the physical act without pretending that the whole garment is a pocket. |
| Lexicon prose contract | Replace chapter 5's retired `muila` symbolism and chapter 6's claim that names lack two supposedly required optional fields | `muila` now demonstrates articulatory description without a symbolic tale; `nuwera` supplies a genuine optional mnemonic through its audible kinship with `nulae`. A productive name lacks shared lexical definition and classification without being deficient in optional symbolism or philosophy. |
| Preserved chapters and examples | Leave chapters 1, 3, 4, 7, and 11 unchanged; preserve every non-cold-open block in chapters 2, 4, 6, 7, and 11 | Chapters 1 and 3 contain no Phi sentence requiring retrofit. Chapter 7 copies three validated Babel passages exactly, and the remaining examples already agree with their literary or manual sources and the completed lexicon. |
| Optional module reach | Add no optional root | The cold open's argument belongs to base vocabulary and grammar. Existing module vocabulary in later teaching examples remains where its subject needs it; no term enters merely to display the modules. |
| Active dependencies | Update chapter 2, the treatment, review ledger, progress records, handoff, and phonetic-neighbour attestations | All Morris lines remain exact, and every drafted Phi book chapter is current through chapter 7. Resume the manual-led remainder of SEM-09D before drafting chapter 8. |

## Transmutation review

The two transmuted works on the shelf were read from their stated sources before the Phi was judged. Repair was preferred when the narrative or argument already held together. A clean rebuild was reserved for the Ring Verse's central refusal, whose earlier substitute had turned coercion into guidance and imposed binding into mutual bond. No new root was needed; the completed module vocabulary supplied the missing distinctions.

| Work | Source and decision | Material repairs | Pillar disposition |
|---|---|---|---|
| Ring Verse refusal | Tolkien's quoted inscription; central Phi passage rebuilt and fidelity-repaired | Rule becomes an explicit analysis as coercion; bind becomes physical `tiwa` used metaphorically. The repaired referent follows the other Rings to their wearers instead of widening **them** to all people. | Peace linguistics makes the decisive change by naming constrained choice. Buddhist attention separates acts from permanent moral identities. The other pillars do not soften the source or invent a replacement moral. |
| *News from Nowhere*, chapters 1-3 | Complete Morris chapters; repaired chapter by chapter | Chapter 1 separates views, membership, and authority. Chapter 2 gives waking, bodily sensation, household detail, work capacity, and the river their completed distinctions. Chapter 3 adds direct rooms, meals, body parts, responses, and craft while retaining commoners' entitlement and the political direction of reactionary novels. | Solarpunk and preindustrial commitments are native to Morris's work; Art Nouveau lives in architecture, clothing, and craft. Buddhist attention clarifies the narrator's inference. Peace linguistics names authority and stigma without cleaning the argument, coercion, or social contempt from the story. |

The source citations and gap logs in each work hold the detailed decisions. The table records why each text remains a transmutation and whether repair or replacement was warranted.

## Phi-first review: When care becomes coercion

Phi is the source for all 39 dialogue units: 34 spoken turns and five narrative actions. The review therefore begins with the Phi propositions and their sequence, then asks whether each gloss and English reading follows them. There is no outside source to restore and no licence to repair an English sentence by changing a coherent Phi thought.

| Area | Finding | Disposition |
|---|---|---|
| Modifier-first order | telari's perfective drinking clause placed `phialu` after Slot 1. | Move the object before `ki milau`. The strict parser now accepts all 39 units. |
| Question structure | `sua hina theama kanu` placed two gap-words in one clause. The intended question is about agency rather than an open pair of unknowns. | Ask `sua mia theama kanu`, "Who chooses my care?" This preserves the argument and obeys the one-gap rule. |
| Retraction | sanuwe described themself as mistaken, then used rephrasing to deny a conclusion. That did not explicitly perform the retraction recorded by the proposition ledger. | Use base `kanelu` for the error and `nosheku` for retraction of the conclusion. The later care claim remains distinct from required departure. |
| Consent withdrawal | `naweri` made withdrawal sound like refusal of consent itself. Current vocabulary keeps refusal and the ending of an ongoing relation separate. | Apply cessative `te` to `lesawi`. telari can end consent to the carrying, and sanuwe must acknowledge that event. |
| Derived English | Two readings collapsed `mua ha womu` into bare "here," while the opening and proposition ledger strengthened `neri` from cool to cooler. | Restore "this home" in both readings and keep the community room cool. No English line now adds a comparison or removes an explicit place. |
| Argument structure | The bodily reports support a safety concern, not the necessity of departure. Consciousness, understanding, and ability to respond support telari's present choice without becoming a universal capacity test. | Keep the unresolved no-prior-consent case. The dialogue reaches a practical boundary rather than a general authority rule. |
| Module reach and coinage | Eight optional roots carry 13 memberships across Household, Medical, Systems, Philosophical Reasoning, Commons, Ecological, and Work. Base bodily language remains preferable to clinical classification in a conversation between friends. | Keep every optional term in its earned role and add no root. The needed repairs use existing base vocabulary and grammar. |
| Validator reach | Fenced Phi above an all-lowercase gloss escaped the Markdown sentence detector. That hid the two-gap question. | Treat a parenthetical line after a gloss as evidence of an interlinear block and add a regression fixture with two gap-words. The expanded scan adds 210 active examples; none of the other newly visible examples fails. |

## Phi-first review: The thing holds its mending

Phi is the source for all 31 essay units and their 67 complete assertions. The review tests each proposition and the argument it enters before comparing the exact gloss and derived English. The wall has no outside witness to restore, so a coherent Phi claim remains primary even when an English phrase would be easier to preserve.

| Area | Finding | Disposition |
|---|---|---|
| Surface relation | Three passages placed walkers generally at the wall's surface with `mua`, although the essay claims direct surface contact. | Use `nia moru leko` for the cat and the habitual walkers. The wall remains their supporting surface rather than merely their location. |
| Restoration path | The restoration clause used `kau`, whose destination is reached, while both `talome` and the derived English leave the earlier shape as a direction. | Replace it with `wea`. Restoration moves towards the selected past shape without claiming exact arrival or making that shape essential. |
| Function and deliberate action | `phoa` names a deliberate act or deed. It cannot name the operation by which a wall remains a garden boundary. | Use shared Systems and Work `kelitho` for the wall's function, the function criterion, and the narrowed thesis. |
| Break and identity | The old revision made complete physical break decide that mending had ended and a new thing had been made. That contradicted the essay's own claim that sameness depends on a chosen criterion. | Let `pukate` settle loss of wholeness only. The break does not choose between `whori` and `pilewa`; the thesis now survives only where the thing's function remains. |
| Derived framing | The opening and the Pre-industrial reading introduced a household, gathered fallen stones, evening, and night beyond the Phi account. | Keep the parent, stone repair, present day, and cat. The English framing now grows from the Phi scene without becoming a second source. |
| Argument structure | Material, function, and use as a place support different identity claims. The wall supplies none of their criteria, while its worth remains inherent under `rolia`. | Preserve the unresolved chooser. Accurate claims can still disagree about which criterion governs, and the essay does not turn that disagreement into a loss of worth. |
| Module reach and coinage | Four optional roots carry six memberships across Philosophical Reasoning, Commons, Systems, and Work. The only missing precision was already available as `kelitho`. | Use each optional distinction where the argument needs it and add no root. General repair, material, place, worth, and choice language remains base vocabulary. |

## Phi-first review: When a report is enough

Phi is the source for all 31 essay units and their 64 complete assertions. The review tests the report's grammatical source, each later proposition, the argument joining them, and then the exact gloss and derived English. The bridge has no outside witness; the revised essay must therefore remain coherent in Phi before its English account can explain what it did.

| Area | Finding | Disposition |
|---|---|---|
| Reportative syntax | The title and nine passages treated Slot 1 `ti` as a modifier making `sherewa` into a noun phrase for a reported claim. This produced 42 strict-parser diagnostics, including arguments after Slot 1 and two evidentials in one clause. | Put `ti` on the finite bridge predicate `ki ti pukate`. Use event-noun `shane` for the report, and let every later assertion mark its own source. The strict parser now accepts all 31 units. |
| Motion valency | The liar objection gave intransitive `roke` a direct object, although moving another person requires causative voice. | Add `ka` before modal `po`. The objection now states that the deceiver can cause another person to move. |
| Reciprocal syntax | Two comparisons used object pronoun `wiso` as though it meant English "as each other." | Remove it. Coordinated subjects take `senao ma nai` directly; `wiso` remains the object of a mutual action. |
| Source and truth | The old alternatives were truth and lying, which made an unverified error into intentional deception. It also let both the telling and later action appear to change a claim's truth. | Contrast `shewo` with base `phelira`, mistaken. State that neither a telling nor acting makes the claim true; reserve `peshu` for the objection in which someone knowingly repeats a false report. |
| Illumination | `shero nuko` made the night black as a color when the walk depends on low light. | Use base `nuelo`, dark. The scene now states the condition that makes inspection difficult. |
| Lexical scope | `kupe` describes deliberate concealment through position or cover. It was stretched to say that the language did not hide an evidential distinction. | Use `lilea`: explicit source marking clarifies the difference between telling and seeing. |
| Inspection and evidence | Going to look was described as converting a reported claim into a witnessed claim. Evidential sources do not convert, and current optional vocabulary already provides `nilaki` for systematic inspection. | Let inspection supply new `thesori`. The later `hi nila` is a separate direct perception, while the bridge proposition remains reportative when the speaker repeats that route. |
| Reversibility and argument | The essay called a walk reversible, then admitted that its time cannot return. The contradiction made `tulawe` carry the argument by violating its own definition. | Use `whu tulawe ma nai` for the kind of injury at issue and `po phelu` to keep its occurrence possible rather than certain. Explicitly retain the walk's lost time. The report supplies a contextual reason rather than a costless or universal rule. |
| Obligation and burden | The old revision denied universal action but did not say what survived, and its final parent assignment did not explain why that person owed repeated walks. | Distinguish `remotha`, Commons and Work `naseru`, and `kanu`: the report gives a reason, creates no obligation, and leaves inspection chosen. Base `tupeka` and shared `ritako` make cumulative burden and its needed boundary visible. |
| Derived framing | The opening and pillar table added a river, an hour's walk, shoes, and later month and year spans that the Phi never stated. The exact clock unit also contradicted Phi's measurement refusal. | Keep the friend, dusk, bridge, dark distance, morning crossing, and bodily walk. Every reader-facing frame now grows from the Phi argument without becoming a second source. |
| Module reach and coinage | Five optional roots carry ten memberships across Philosophical Reasoning, Systems, Work, Accessibility, Household, and Commons. The missing distinctions were already present in the completed module set. | Use `whamoi`, `nilaki`, `whakeru`, `naseru`, and `ritako` in their earned roles and add no root. |

## Phi-first review: Worth does not require a valuer

Phi is the source for all 33 essay units and their 62 complete assertions. The review begins with the branch, follows the argument through its retraction, and then checks every gloss, derived reading, vocabulary claim, and pillar account against what the Phi actually says. The essay has no outside witness; the language can record a normative commitment without turning its own syntax into evidence that the commitment is true.

| Area | Finding | Disposition |
|---|---|---|
| Sentence structure | The old text contained two `lu` conditions before one consequence, placed negation before a predicative complement and causative voice, and gave intransitive `roke` a direct object. | Rebuild the affected reasoning rather than preserving its faulty inference. All 33 revised units pass the strict sentence parser. |
| Dative and accuracy | The essay called `thena wei sua rolia phelu` ungrammatical because `rolia` lacked a holder slot. `wei` is a clause-level recipient or beneficiary and remains legal there. It also called questions `telua`, although accuracy compares a representation with its reference. | Keep both dative questions grammatical. Use `theali` for the fitting inquiry and state that asking the second question does not define worth. The semantic contrast comes from `thaemo` and `rolia`, not from a syntactic ban. |
| Time and derived framing | The opening supplied two summers, a blocked path, a spoiled view, an underside, and a split end that the Phi never stated. The present claim that nobody saw the branch also conflicted with the later observed scene. | Put the two summers and the later direct observation into Phi. Keep the garden edge, moss on the branch's surface, and insects within it; remove the other English-only details. |
| Change and nonhuman minds | The branch twice failed to change before it decomposed, while the essay denied insect thought and valuation without evidence. Neither claim was needed. | Let the branch's worth remain when human attention changes. Frame insect valuation as an embedded unknown and leave their minds open. |
| Ecological relations | `whemori` and `kelasu` were treated as properties located solely in a person's activity or in the person. Waste instead depends on an activity or system, usability relates a thing to a user and purpose, and seeing insects does not by itself establish habitat. | Use possible waste under one garden method, possible insect habitat, resource under one purpose, decomposition, and possible nutrient release. Remove `kelasu`, whose accessibility distinction did no work here. |
| Challenge and retraction | Relational waste and usability were called a counterexample to the claim that worth resides in a thing. They were an analogy and objection, not a scoped case falsifying a universal claim. The text then said the counterexample did not refute the claim before narrowing it anyway. | Use `whakeru` for the objection and `whekate` for its actual force. Retract the locative thesis explicitly with `nosheku`, then state the smaller claim separately. |
| Creation and cessation | The argument inferred that worth would end when valuing ended if valuing made worth. `pilewa` makes bowls and other results that may outlast their making, so the inference was invalid in Phi as well as in logic. | Drop the inference. A child's worth surviving withdrawn approval and a person's worth surviving unproductive labor become supporting reasons rather than a purported proof. |
| Authorship and shared wording | Generic people were said to have made Phi, and one word for child and branch worth was treated first as making them different and later as refusing to distinguish them. | Let the essay's first-person author own the lexical choice. A child and a branch both hold worth, while causative negation states that one word does not make two things the same. |
| Obligation and attention | `mawha miona ... na` tried to express absence of obligation through necessity, contrary to canon's freedom construction. The final intransitive motion clause also denied that language moved the speaker towards care. | Use `lila ... ralu nai` for freedom from required tending or protection. The branch's worth creates no obligation but gives the speaker a reason to attend, and that reason requires no particular act. |
| Module reach and coinage | Nine optional roots carry fifteen memberships across Philosophical Reasoning, Ecological, Household, Medical, Commons, and Work. Current vocabulary supplies every needed distinction. | Keep `kirothe`, `natheri`, `whakeru`, `whekate`, `morume`, `menuro`, `lurepa`, `whemori`, and `naseru`; add no root. |

## Literary shelf

| Active text | Method | Status | Note |
|---|---|---|---|
| `texts/care_and_coercion.md` | Original | Reviewed | All 39 Phi-source units, exact glosses, derived readings, proposition structure, optional terms, and five-pillar claims have received a Phi-first review; retraction and consent withdrawal now remain distinct. |
| `texts/the_mended_wall.md` | Original | Reviewed | All 31 Phi-source units, exact glosses, derived readings, proposition structure, optional terms, and five-pillar claims have received a Phi-first review; function and wholeness no longer collapse into doing and identity. |
| `texts/the_report_at_dusk.md` | Original | Reviewed | All 31 Phi-source units, exact glosses, derived readings, proposition structure, optional terms, and five-pillar claims have received a Phi-first review; `ti` now marks finite propositions, and reason no longer collapses into truth or obligation. |
| `texts/the_worth_of_a_fallen_branch.md` | Original | Reviewed | All 33 Phi-source units, exact glosses, derived readings, proposition structure, optional terms, and five-pillar claims have received a Phi-first review; lexical commitment no longer masquerades as grammatical proof. |
| `texts/north_wind_and_sun.md` | Translation | Reviewed | Complete Aesop alignment, literal back-translation, continuous reading, and translation limits complete. |
| `texts/metta_sutta.md` | Translation | Reviewed | Full source-fidelity pass complete; two optional roots used where their distinctions matter. |
| `texts/solarpunk_manifesto.md` | Translation | Reviewed | The 38-unit fidelity pass changes 17 units, aligns a 244-form Phi reading with the complete licensed witness, and uses 33 optional roots across all eight modules without altering a source line. |
| `texts/schleicher_fable.md` | Translation | Reviewed | D074 adds direct shearing, removes a quoted fragment, restores cessative possession, treats the final glosses as one motion, and makes the citation stream reconstruct the stored source body exactly. |
| `texts/babel_text.md` | Translation | Reviewed | Complete KJV alignment, continuous reading, and translation limits complete. |
| `texts/human_rights_article_one.md` | Translation | Reviewed | Exact rights, reason, conscience, held obligation, source alignment, and translation limits complete. |
| `texts/little_prince_excerpts.md` | Translation | Reviewed | Five interlinear units and seven assertions align with the three stored Woods excerpts. The 40-form rendering preserves the current turn, passive invisibility, taming, and obligation while recording Phi's narrower animal head. |
| `texts/gibran/on_love.md` | Translation | Reviewed | The complete 35-unit citation stream reconstructs the 2,403-character source passage exactly. The fidelity pass changes 19 units and adds base `ratenu` and `salenu`. |
| `texts/gibran/on_children.md` | Translation | Reviewed | All 18 source units align, the continuous reading matches the detailed blocks, and the limits table records Phi's material treatment of the archery scene. |
| `texts/gibran/on_giving.md` | Translation | Reviewed | All 33 source units align. D075 adds direct deservingness and reward while preserving exact source identities beside material descriptions. |
| `texts/gibran/on_work.md` | Translation | Reviewed | All 32 source units align exactly, and the limits table records the distinctions that remain with Gibran's wording. |
| `texts/tao_te_ching.md` | Translation | Reviewed | All 51 Legge units align in order, and the continuous reading follows every proposition in the detailed translation. |
| `texts/heart_sutra.md` | Translation | Reviewed | All 34 Müller units align in order, and the translation preserves every printed proposition in the selected witness. |
| `texts/ring_verse_refusal.md` | Transmutation | Reviewed | The 17-form base-only refusal keeps Tolkien's inscription exact, narrows its affected people to wearers of the other Rings, and records the deliberate change from purpose to accusation. |
| `texts/velveteen_rabbit.md` | Translation | Reviewed | The 429 exact Williams fragments align across 427 Phi stanzas and reconstruct the stored story in order. D081 changes 29 stanzas, adds a matching continuous reading, and records the remaining descriptive limits without adding vocabulary. |
| `texts/news_from_nowhere/chapter_01.md` | Transmutation | Reviewed | The 85-unit post-migration pass changes 29 units and uses six optional roots across four modules without altering Morris's source lines. |
| `texts/news_from_nowhere/chapter_02.md` | Transmutation | Reviewed | The 241-unit post-migration pass changes 57 units and uses five optional roots with seven memberships across four modules without altering Morris's source lines. |
| `texts/news_from_nowhere/chapter_03.md` | Transmutation | Reviewed | The 245-unit post-migration pass changes 46 units and uses 14 optional roots with 15 memberships across five modules without altering Morris's source lines. |

Every current translation, transmutation, and original has received the review appropriate to its declared method. The six formerly paired works, the Little Prince excerpts, and The Velveteen Rabbit now stand as translations only. All four original Phi works have received Phi-first reviews. The Phi book and SEM-09D retrofit are complete.
