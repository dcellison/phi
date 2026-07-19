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

The ground truth is the 1919 *Aesop for Children* text stored at `texts/sources/aesop_for_children.txt`. The close translation uses 104 unique forms and the transmutation uses 98. Both still reach well beyond the preceding graded chapters, so the glosses and back-translations remain part of the reading method. Both renderings use base vocabulary throughout.

### Close translation

| Area | Finding | Disposition |
|---|---|---|
| Source coverage | The benchmark role requires Aesop's events and moral to survive rather than merely inspire a Phi retelling. | Every source clause has an aligned Phi block, literal back-translation, and exact adjacent citation. The translation precedes the transmutation on the shared page. |
| Quarrel and bluster | Phi has no roots for either term, while `themore` is a reasoned argument and does not fit. | Discussion plus failed agreement forms the quarrel. Heart-fire and loud shouting supply the heat and bluster without creating two narrow roots. |
| Strip and wrap | The transmutation made the winner cause the Traveler's release, which shifted the source's direct removal. Plain `lomare` also lacked the Traveler's agency in wrapping the cloak. | `lue ... wethalu leiro` makes the contestant release the garment from the Traveler. The causative makes the Traveler cause the garment to embrace them closely. |
| Gust and whipping cloth | Quivering was an intentional softening, not a close transfer of the first gust's force. | `teku kema howeli` is a short, strong wind. Passive `wapho` throws the garment's edges around the Traveler's body. |
| Loose cloak and anatomy | `luwi` cannot mean loose, and broad `menoa` loses the brow's location. | The Traveler causes the garment to stay `ralu`, free, on their shoulders. Base `komeri` now names the forehead directly; cap remains the transparent head-garment. |
| Pulling off and throwing down | A single release loses the pull in "pulled off," while `ruemi` replaces the source's abrupt reflexive throw with an ordinary posture. | The garment is pulled from the body and then released. The Traveler flees (`phesari`) from the burning brightness and throws themself toward the earth into tree-shadow. |
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
| Effort and failure | `theko` is skilled craft, `riola` is purposeful labor, and `thonuki` reports failure against a technical requirement. None fits the Wind's attempt or Aesop's contest result. | The event noun `mesatu` now names the Wind's attempts without turning them into labour. `whuo lureko` judges their immediate result without borrowing a systems term. |
| Wager and governance vocabulary | `repora` is a proposal put before a collective process. This exchange needs no institution. | The Sun's spoken agreement uses the optative and `nawo`. The note also identifies the missing party: the Traveler. |
| Active dependencies | The moral appears in two manual chapters, and the fable is the primer's annotated capstone. `keru loa` also reaches the compound registry and other literary texts. | The two manual citations follow the new moral. The capstone still presents the source line and back-translation as part of the reading method. |

The comparison follows all five pillars without demanding an artificial change from each. Solarpunk and preindustrial commitments find the source's material scene already close to them. Art Nouveau changes the pressure of the organic line more than its objects. Secular Buddhist attention moves from rank toward consequence. Peace linguistics produces the widest divergence: translation states Aesop's claim, while transmutation leaves strength and volume neutral and lets the Traveler's departure answer the contest.

No module word is required. Persuasion and coercion belong to ordinary social language, and the other compositions use equally general words. The paired page is still a capstone without asking a new learner to open a specialist lexicon.

### Post-migration contextual retrofit

Three old detours can now give way to direct base words in both renderings. Each replacement restores a source detail without changing the translation's fidelity or the transmutation's answer to Aesop. The remaining compositions stay because they still say the right thing.

| Question | Disposition | Reason |
|---|---|---|
| Effort and attempt | Replace generic `theula rena shia to phoa` with `shia theula mesatu` | The older phrase said only "all that it did." The event noun of base `mesatu` now says "all its attempts" and leaves completion and success open until `whuo lureko` reports the fruit. |
| Brow | Replace the descriptive location and broad `menoa` with `komeri` | Forehead is an ordinary bodily landmark in the source and in daily speech. The direct base noun is both shorter and more exact. |
| Escape from the Sun | Replace `phei ... wepu`, go away from, with `lue ... phesari` | The Traveler now flees the burning brightness. `phesari` carries the danger or constraint that plain motion left unspoken. The close translation still throws the body down; the transmutation still uses an ordinary lying posture. |
| Warmth, heat, and illumination | Preserve `sulae`, `sukaro`, and `keru loa` | The pleasant warmth is moderate, the later bodily heat is intense, and the registered expression "give brightness" presents a shining source. `sumeri` would turn the scene into a temperature parameter, while `keruma` concerns received illumination as a condition. |
| Garment, pulling, and damage | Preserve `wethalu`, `lomare`, `ralu`, and `natu` | Head-garment remains a useful transparent composition, the cloak's embrace keeps wrapping embodied, and Aesop's "tore at" reports forceful pulling without proving that the cloth was damaged. `tawemi` and `pukeri` would change those claims. |
| Optional module vocabulary | Use none | The fable's weather, clothing, bodily actions, persuasion, and coercion all belong to ordinary speech. No optional root improves either rendering. |

## Paired review: Schleicher's fable

The source chain begins with Schleicher's 1868 German rendering in `texts/sources/schleicher_1868.txt`. The controlled English source at `texts/sources/schleicher_1868_english.txt` translates the complete German wording and every explanatory parenthesis, while the German retains Schleicher's square brackets for words absent from his reconstructed Proto-Indo-European text. The close translation uses 63 unique Phi forms; the transmutation uses 60. The first uses Commons `phenori` (ownership), and the second uses `pilora` (exploit), shared by Work and Commons.

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

### Post-migration contextual retrofit

The post-migration pass checked every content phrase against the completed lexicon. Neither Phi rendering needs a change. The existing roots keep source distinctions that newer words would blur, and the transparent clauses still expose relations that a broader label would hide.

| Question | Disposition | Reason |
|---|---|---|
| Physical weight and burden | Preserve `tumoa` and `tupeka` | `tumoa` gives the wagon the source's heavy judgement. `tupeka` keeps the living bearer inside the great load; newer `pamolu` would identify weight as a magnitude but lose the burden as an object carried by the horse. |
| Heartfelt grief | Preserve intense `nuhe` | Schleicher's parenthesis describes immediate heartfelt distress without an identified loss. `nuhemi` is continuing grief after loss, so it would narrow the source more than `ru nuhe phaelo`. |
| Warmth, shearing, and bodily consequence | Preserve `sulae`, passive `kati`, and the surrounding clauses | The garment is warm, not hot. The source establishes cutting and missing wool but does not separately establish damage, cruelty, or an act of covering. `sukaro`, `pukeri`, `lerasu`, and `tawemi` would add those claims rather than replace a workaround. |
| Animal objects of power verbs | Repair the lexicon prose; preserve the Phi | The target entries for `kawhera` and `pilora` had narrowed their objects to people even though the transmutation validly applies coercion to horses and exploitation to sheep. D053 restores animals to both ranges and adds examples without changing a form or gloss. |
| Optional module vocabulary | Preserve `phenori` and `pilora` only | Commons `phenori` supplies the practical ownership relation required by the close translation. Shared Work and Commons `pilora` supplies the transmutation's analysis. No other optional term makes either rendering more faithful or natural. |

## Translation review: The Metta Sutta

The ground truth is V. Fausböll's 1881 translation stored at `texts/sources/sutta_nipata_fausboll.txt`. Every cited clause in verses 1 through 10 is represented. The final claim about return to a mother's womb is there too. The complete Phi text uses 124 unique forms. Two are optional roots whose distinctions a base paraphrase would lose: `thesani`, skill, and `naseru`, obligation.

| Area | Finding | Disposition |
|---|---|---|
| Skill, attainment, and ability | The seeker merely knew a path, attained no state, and was wished fitting rather than able. Three source claims had collapsed into a gentler Phi summary. | Skill is `thesani` in `welao sheraki`, the search for goodness. `ki noalu kelu` states completed attainment of tranquility, while `po phoa` gives actual ability. Nibbana remains visible in the exact adjacent citation as tradition-specific source material. |
| Support and burden | `henoi sano` (knowing enough) replaced easily supported. `phelo` then used the English weight/metaphorical homonym for unburdened even though its entry is strictly about weight. | Easy support is support requiring little labor. Few cares narrow to obligations, while `whuo tupeka` says directly that the person is without a burden. `phelo` is absent. |
| Beings and bodily states | The text claimed Phi had no word for being despite `limoe`, treated joy as an object of `phaelo`, and used fragile for feeble. | The refrain names every `limoe` directly; joy predicates with `nai`; base `huwa` names the feeble as weak. Great and large remain distinct as `ru whalo` and `whalo`. |
| Family round and social judgment | The family round became taking enough among homes, while reproof became silent perception by the wise. | The practitioner habitually walks among `lumani` and does not want to take many things. Base `rinu` gives ordinary desire; unlike `pula`, it does not cast the desired outcome as a welcome one. Wise people may explicitly claim that a deed is harmful; the modal retains the possibility, and speech restores the social act in Fausböll's line. |
| Deception, resentment, and enmity | The intransitive `peshu` was given a dative target, and anger, resentment, hatred, and enmity were all left as one undifferentiated heart-fire. | Deception is the instrument by which another is made mistaken. A long-time heart-fire distinguishes lingering resentment and enmity from the unqualified fire of anger and hatred. |
| The mother and her child | The source's mother became a generic parent, the danger to her life became an instrument, and the child's ownness was absent. | `thowia phao` names the birth parent. The relative clause puts the parent's own life in danger and keeps `miso ta lopia`, their own one child; Phi's quantity rule carries "only" without `li`. |
| Cultivation and direction | The source's repeated cultivation became giving or holding love, while "across" widened to an unspecified every place. | `sorila` now governs the loving heart throughout. Above, below, and across are `leo muila`, `phou muila`, and `roa muila`, each with an audible object. |
| Wakefulness and the final verse | Conditional `lu` replaced "as long as," virtue disappeared into a pure-heart image, sensual pleasure lost its greed, and the rebirth claim was omitted for supposed lexical and metaphysical reasons. | `sui waeli` gives duration, the practitioner dedicates themself to the cultivated heart, virtue acts well, perfect vision is complete insight, bodily longing ceases, and `mawha thimu ... so turema` carries the prediction of never returning to a birth parent's belly. |
| Active dependencies | The old refrain and old not-yet-born composition remained in the manual, meditation chapter, compound registry, the born entry, and three particle pamphlets with a stale wish count. | The refrain now uses `limoe`, the registry follows `wea thowia shua` and the central loving-heart compositions, and the teaching prose records the current count of thirty-one wishes. |

The English back-translation is deliberately literal. It lets a reader inspect the Phi without already knowing the language. Where the source still narrows in Phi, the notes name the loss: upright becomes honest, mean becomes harmful, and a womb is a birth parent's belly.

### Post-migration contextual retrofit

Four old detours have direct base vocabulary. The other compositions still fit Fausböll better than their apparent single-word alternatives.

| Question | Disposition | Reason |
|---|---|---|
| Seeking good | Replace `wea welao thalo` with `welao sheraki` | The old line walked toward goodness. `sheraki` names the search itself without claiming that goodness has been found, while optional `thesani` supplies the learned skill named by the source. |
| Unburdened | Replace `whuo tumoa naseru` with `whuo tupeka` | `tupeka` is a burden borne by a living being. It suits this personal freedom better than a heavy obligation, and it remains distinct from technical load, workload, and physical weight. |
| Greediness on the family round | Replace `pula` with `rinu` | `pula` presents an outcome the person would welcome. `rinu` is ordinary wanting, while `mena ... meno` holds the complete action of taking many things among the families. That action carries the excess present in this scene. |
| Feeble and strong | Replace `phina puro phelu` with `huwa` | Direct `huwa` and `kema` give the source's weak-strong contrast. `welua` still means readily damaged, not weak in capacity. |
| Upright, conscientious, and mean | Preserve `wero`, `thesa`, and `peloma` | `sharino` names conscience as an inward faculty, not conscientious conduct. `sherelo` names a normative right, not uprightness. `lerasu` would strengthen "mean" into cruelty. The existing words state honest, careful, and harmful, and the gap log keeps their limits visible. |
| Womb and birth parent | Preserve `thowia phao mokura` | `mokura` makes the bodily location concrete without pretending that belly and womb are identical. Reproductive anatomy has its own recorded return conditions and should not be settled by one traditional source. |
| Optional module vocabulary | Preserve `thesani` and `naseru` only | Base words would blur practical skill and obligation here. No other optional root improves the translation. |

## Paired review: UDHR Article 1

The ground truth is the complete 1948 English Article 1 stored in `texts/sources/udhr_1948.txt`. The close translation uses 23 unique forms. Its two source-facing optional roots do work that composition could not do cleanly: `sherelo` is a normative right that can survive denial, and `sharino` is conscience as moral self-appraisal. The 21-form transmutation uses one optional root, Commons `shereni`, for recognised entitlement.

| Area | Close translation | Transmutation |
|---|---|---|
| Birth and equality | A second Phi sentence says that equal worth and rights are held from birth and therefore preserves the scope of the English coordination. | Freedom stays tied to birth, while equality becomes a separate standing universal claim. |
| Dignity and rights | `rolia` supplies inherent worth or dignity; `sherelo` leaves a right sayable before recognition or fulfillment. | Equal worth remains, but rights narrow to recognized `shereni` entitlements. |
| Reason and conscience | Passive `se loa` retains the endowment metaphor. Event-noun `remo` supplies thinking as an activity, which leaves the faculty itself unnamed. `sharino` states conscience directly. | `po remo` gives a capacity to think, while `korua sano` turns conscience into the heart's knowing. |
| Brotherhood and conduct | `lomea phiora` retains a sibling spirit, and reciprocal `wiso` directs the action toward one another. | People act as siblings, and `phena` makes kindness part of the observable conduct. |
| Remaining limits | `remo` is broader than rational faculty, `phiora` is less idiomatic than English "spirit," `lomea` ungenders brotherhood, and `na` is stronger than "should." | The gap log records each deliberate change, including the loss of birth scope on equality and the narrowing from rights to entitlements. |

The five-pillar comparison does not force five rewrites. Solarpunk thought tests whether a right survives institutional denial and whether an entitlement has practical form. Secular Buddhist attention shifts endowed faculties toward conditioned acts in the transmutation. Art Nouveau affects the line and repetition rather than the concepts. Peace linguistics moves the transmutation from prescribed feeling to accountable conduct. Preindustrial wisdom finds kinship and heart-knowing already present, without adding a village or tradition absent from the source.

### Post-migration contextual retrofit

The full lexicon gives neither rendering a better Phi line. Their direct roots and transparent phrases still fit Article 1; the apparent alternatives answer different questions. One English note changes: `remo` supplies thinking as an activity, not a dedicated faculty of reason.

| Question | Disposition | Reason |
|---|---|---|
| Freedom, equality, and dignity | Preserve `ralu thowia` and `kolo rolia` | `ralu` leaves a course open from constraint, `kolo` supplies equal standing, and `rolia` belongs to every person without being earned. `thunoa` concerns dignified conduct or treatment and cannot replace inherent dignity here. |
| Reason | Preserve event-noun `remo` and its recorded limit | Thinking is closer to the source's faculty than `remotha`, one stated ground for accepting a claim or choice. `kethira` names inference and `themore` an argument; neither supplies a general faculty. |
| Rights and entitlements | Preserve `sherelo` in translation and `shereni` in transmutation | The declaration needs a right that can still be said when an institution denies it. The transmutation deliberately asks whether a social order has recognised the claim and made it usable. |
| Conscience and heart-knowing | Preserve `sharino` in translation and `korua sano` in transmutation | `sharino` is the source's inward moral self-appraisal. The heart's knowing is a deliberate Phi reframing, while `naremu` is guilt felt after an act or omission rather than a moral faculty. |
| Brotherhood and kinship | Preserve `lomea phiora` and `phea lomea` | The sibling noun keeps the source's specific kin relation without a universal male class. Wider `thaluni`, kin, would make the image less exact. |
| Conduct and modality | Preserve reciprocal `wiso`, necessity `na`, and transmuted `phena` | `wiso` gives action toward one another. The stronger force of `na` remains visible in both gap logs, while kindness belongs only to the transmutation. |
| Optional module vocabulary | Preserve close `sherelo` and `sharino`, and transmuted `shereni` | Each of these three distinctions is needed here. No other optional root improves either rendering. |

## Paired review: Babel

The ground truth is KJV Genesis 11:1-9 stored in `texts/sources/kjv_genesis.txt`. The close translation uses 83 unique forms and two optional roots: Commons `karami` (authority) and Work `noraku` (blocked). The 70-form transmutation uses base vocabulary throughout. The close rendering remains answerable to all nine verses, while the transmutation marks its departures openly. Neither needs another root.

| Area | Close translation | Transmutation |
|---|---|---|
| Source names | Shinar and Babel stay exact beside the Phi. The passage gives the land relation and naming event without assigning adaptations. | Shinar is dropped. Babel becomes `lo haluma`, Many Languages, a semantic place-name made for this retelling. |
| LORD | The KJV title stays beside the Phi. Inside the passage, `karami` identifies the actor's authority. Legitimacy and nature are separate questions. | `muila`, the earth, replaces the source actor and needs no descent. |
| Materials | Brick is the registered clay-stone. The KJV's bitumen becomes thick black oil and connects the clay-stones. | Brick stays clay-stone, while bitumen becomes mud that connects the pieces. |
| Building | The builders' benefit, the tower's high edge, their wish for a known name, and their fear of dispersal survive. | The settlement's scale and upward reach receive more attention than benefit or top; the known name and fear survive. |
| Human possibility | Actions the builders have imagined face no `noraku`, block. | The builders begin in the present moment and can do everything they have imagined doing. |
| Confounding | Language is deliberately made unfamiliar so speech from one another cannot be understood. | One language is not enough for the earth and becomes many. |
| Dispersal | Authority uses `thiwera` to scatter the people from the settlement across the earth. | The earth uses the same verb, compares the people to seed, and follows the comparison into gardens. |
| Ending | The source's final explanation and repeated dispersal close the account. | Two uncited lines call every language a garden and place Phi among them. |

`thiwera` stays neutral in both passages. It describes broadcast scattering and has an audible kinship with `thinoe`, seed, but it does not make every scattering innocent. Authority is the subject in the translation, and no seed comparison appears, so the punishment remains severe. The transmutation adds that comparison and follows it into gardens. This is the peace-linguistic test: refusing violence in Phi cannot mean concealing violence in a source.

### Post-migration contextual retrofit

The completed lexicon exposes several semantic shortcuts and an omitted source claim, all repairable with existing words. The table also records why several transparent expressions remain.

| Question | Disposition | Reason |
|---|---|---|
| Brick and ceramic | Preserve registered `mueri kerou` | `mueri kerou`, clay-stone, is Phi's established brick expression and already includes clay hardened for a stone's work. `mueta` names the wider ceramic material class; it would not identify a brick's form or use by itself. |
| Mortar and bond | Replace material `nolami` and the make-one clause with `lorea` | `nolami` is a mutual bond between beings, not the physical English homonym. In the close translation, bitumen is material that connects clay-stones. In the transmutation, mud connects them directly. |
| Tower top | Replace close `koma` with `raelu shuna` | The source asks how high the tower's top may reach. A high edge states that relation without extending the anatomical head into an object part. The transmutation's tall wall reaching the sky remains its deliberate simplification. |
| Name and renown | Replace `nomei pilewa` and `nomei whalo kelu` with passive `sano` | The builders want recognition, not a newly manufactured identifier or a physically large name. "May our name be known" carries the source idiom's ambition in ordinary Phi. |
| Beginning and imagined action | Preserve close `noraku`; repair the transmutation with `pa phoa`, `nosa`, and `po phoa` | `noraku` keeps the source's negative prediction and its blocked action. The transmutation now restores "begin" and "now," then makes its affirmative turn through actions the builders can do. Bare `kelu` was incomplete because becoming requires a stated result. |
| Scattering and sowing | Replace close caused going with direct `thiwera`; preserve transmuted `phea lo thinoe` | The same neutral verb can report punitive dispersal and seed-shaped sowing. Authority and the absence of comparison keep the translation severe; seed and garden make the transmutation's ethical departure visible. Direct `thophe` would lose the source's repeated scattering. |
| Face of the earth | Preserve `muila menoa` | The KJV itself offers the bodily image, and both renderings make that metaphor explicit. Replacing it with `muila leko`, earth's surface, would be denotationally tidy but would discard an image that the transmutation later answers with seed and garden. |
| City, people, and source identities | Preserve `whalo silawo`, close `theula miona ta nai`, transmuted `ta punoa`, and the external Shinar, Babel, and LORD forms | The settlement expression follows the standing city decision. The close version keeps the source's unity claim, while the transmutation interprets it as one society. Exact names and the refused title remain visible beside Phi rather than entering through invented adaptations. |
| Optional module vocabulary | Preserve close `karami` and `noraku` only | Authority is the practical relation needed to carry LORD inside the translation, and blocked action fits the source prediction. No optional root improves the transmutation. |
| Active dependencies | Preserve the registered brick row; no repeated Phi excerpt changes elsewhere | The compound registry already defines `mueri kerou` through Babel's material contrast. Searches of the active corpus find the revised sentences only on the paired page, including its complete translation block. |

## Paired review: Heart Sutra

The ground truth is F. Max Müller's 1894 Smaller Pragñâ-pâramitâ-hridaya-sûtra stored in `texts/sources/buddhist_mahayana_texts_1894.txt`. The close translation uses 98 unique Phi forms and one optional root, Philosophical `remole` (concept). The 79-form transmutation uses base vocabulary throughout. The close rendering follows the complete printed text and its colophon, but does not reconstruct the lists Müller abbreviates with "till we come to." Names and tradition-specific terms remain in the adjacent source lines when no accepted form or exhaustive equivalent exists.

| Area | Close translation | Transmutation |
|---|---|---|
| Five Skandhas | The ternary count appears at first mention, where each Skandha is a gathering. Later, event-noun `morae` keeps perception distinct from conception and knowledge. | The category list has five entries but never announces its count or gathered character. `phaelo` deliberately turns perception towards felt experience. |
| Address and identity | Exact names occur in cited English. Passive `nelu` carries venerable, and `kona miona` carries the otherwise lost vocative. | A deep-seeing epithet replaces Avalokiteshvara; the listener receives no address. |
| Equation | Deixis and focus reproduce "here" and "indeed." Two comparison clauses preserve the reversal. | Coordination makes non-difference mutual in one sentence. |
| Absence chain | Before the abbreviation, the Phi zeroes knowing, its absence, and the end of both. | The transmutation passes directly from the senses to decay and death. |
| Consciousness and fear | Quality-noun `waeli` forms the enclosure. Its caused ending leads to explicit freedom with `ralu`. | `remo kire` places the walker among constructions of thought; release opens the way out. |
| Verse and crossing | `melira`, song or poem, receives both rank claims. The addressed wisdom completes every movement to a literal shore. | The same noun carries fewer claims, and an optative opens the crossing first to us and then to everyone. |
| Ending | Only Müller's citation carries Svaha; a Phi sentence carries the colophon. | `shea shua`, peace comes, answers Svaha and closes the spoken text. |

No new root is needed. Philosophical `remole`, concept, separates conception from mind. Base `nelu` restores reverence, `morae` distinguishes perception from feeling, and `melira` gives the verse a work made for the voice. `waeli`, `ralu`, `helui`, and `kerime` supply consciousness, freedom, change, and shore. The central boundary is textual: this is a translation of Müller's English, not a fresh adjudication of Sanskrit doctrine. The close version can therefore carry annihilation and superiority while the transmutation releases thought-shapes and invites company. Neither choice is disguised as a limit in Phi.

### Post-migration contextual retrofit

Five choices on the paired page no longer survive the current word entries. Each has a base answer. The remaining compositions still fit Müller's wording or the transmutation's declared departure better than their apparent alternatives.

| Question | Disposition | Reason |
|---|---|---|
| Venerable and dignified | Replace close `thunoa` with passive `nelu` | `thunoa` describes self-possessed conduct or treatment that accords dignity. Müller's venerable instead reports high regard, which `nelu`, revere, preserves without assigning a rank or office. |
| Perception and feeling | Replace close event-noun `phaelo` with `morae`; preserve transmuted `phaelo` | `morae` is perception through one or more bodily channels, which fits Müller's printed term. `phaelo` reports felt sensation or emotion. The transmutation chooses that inward experience deliberately as one of its five ordinary bundles. |
| Imperfection and quantitative shortfall | Replace `ma thenoi` with completeness asserted before it is denied in both renderings | `thenoi` compares a tested quantity with a required reference and needs Phi's `nela` construction. It cannot mean imperfect without such a comparison. Phi has no metaphysical imperfect quality, so Müller's not-imperfect becomes `sholu`, complete, before the next sentence denies completeness. The translation limit and transmutation gap log keep that narrowing visible. |
| Verse, poem, and greatness | Replace close `phelui sena` and transmuted event-noun `meliho` with `melira`; replace `whalo` with `ru welao` and close `ru nulo` | `melira` already covers a song or poem shaped for the voice. `meliho` names the act of singing, while word-pattern is needlessly generic. `whalo` concerns physical size or broad scope, not the importance hidden inside the English homonym "great." Very good and very deep knowing state the two judgements directly. |
| Form and formation | Preserve event-noun `kire` | `kire` names a thing's shape or form. `norelu` centres separate parts or material acquiring an organised structure, which would turn Müller's form into a process of formation. |
| Faultlessness, purity, and technical fault | Preserve `shiloa` and its stated limit | `kiphira` is a technical fault in a component or relation and explicitly leaves moral fault elsewhere. It cannot answer Müller's metaphysical pair. Purity remains an approximation, with its loss named beside the translation. |
| Ignorance, destruction, and obtaining | Preserve `sano whemoa`, `lumae`, and `pilu` | Knowledge's emptiness, an ending, and active taking expose Phi's available relations without coining Buddhist technical vocabulary. Dissolution, breakage, and release answer different material or relational events. Müller's exact doctrine stays visible in the source lines and limits table. |
| Consciousness, freedom, release, and change | Preserve close `waeli` and `ralu`; preserve transmuted `remo kire` and `leiro`; replace transmuted event-noun `kelu` with `helui` | The close rendering follows consciousness as subjective experience and the resulting freedom from fear. The transmutation makes its ethical turn openly by releasing thought-shapes instead of disguising annihilation as a direct equivalent. `kelu` is becoming, while Müller's change already has the direct base verb `helui`. |
| Names, sacred terms, and optional vocabulary | Preserve adjacent source forms and close `remole` only | Avalokiteshvara, Sariputra, Prajnaparamita, Nirvana, and Svaha keep their source identities beside the Phi. `remole` earns its Philosophical module place because conception must remain distinct from mind. No other optional root improves either rendering. |
| Active dependencies | Update the paired page and phonetic-neighbour attestations only | The changed Phi sentences recur in the page's complete translation block but nowhere else in the active corpus. The source file, shelf links, and registered compounds remain unchanged. |

## Paired review: The Prophet, On Children

The ground truth is the complete On Children teaching in Kahlil Gibran's 1923 *The Prophet*, stored in `texts/sources/the_prophet.txt`. The established excerpt begins with Gibran's first paradox rather than the woman's request for the teaching. Its close translation covers every proposition from that line through the stable bow in 72 unique Phi forms. Its optional roots are Commons `phenori` (ownership) and Household `phemiru` (visit). The 49-form transmutation uses base vocabulary throughout.

| Area | Close translation | Transmutation |
|---|---|---|
| Child relation | `phomila` appears on both sides of the opening denial; Gibran's sons and daughters become offspring. | The second `phomila` becomes `thena`, thing, so the ownership reading arrives immediately. |
| Life and living | Noun `lioru` is personified as Life. | Life remains `lioru`, while adjective `lima` makes the transmuted seeds alive. |
| Belonging | Offspring stand outside the parent's `phenori`, ownership. | The parent does not `phelu`, hold, them. |
| Effort and future | `meloa` restores striving, negated `mesatu` restores the attempted conformity, and `phemiru` restores the visit to tomorrow's house. | Becoming and presence state the same boundaries with fewer distinctions. |
| Archery | Bow, arrow, and archer receive material descriptions from cord, flexible wood, sharpness, flight, and tool use. | Tree, seed, and wind replace the weapon system. |
| Agency | The archer sees a purpose marker and uses strength so the arrows fly fast and far. | Wind carries seeds toward tomorrow without a chosen target. |
| Final parallel | The one who uses the tool loves the flying arrow and stable bow. | Life loves the flying seed and standing tree. |

Existing vocabulary is enough. Base `phomila` keeps descent apart from the childhood stage, and the `lioru`, `liona`, `lima` family separates life, living, and being alive. Commons `phenori` makes the social ownership claim exact, while Household `phemiru` distinguishes visiting the future house from merely being there. One metaphor does not need permanent archery roots: material descriptions carry the objects, and Gibran's cited English identifies them. Close translation states the weapon image without endorsing it; transmutation can remove the target without pretending the source had none.

### Post-migration contextual retrofit

Three distinctions alter the paired section. Several newer or newly clarified words look tempting at first and fail once Gibran's relation is read closely.

| Question | Disposition | Reason |
|---|---|---|
| Child as life stage and offspring by descent | Replace `lopia` with `phomila` in both renderings | `lopia` is a person in childhood. Gibran's sons and daughters are direct offspring and need not still be children by age. `phomila` keeps that relation without turning descent into possession. |
| Life, living, and being alive | Replace personified `liona` with `lioru`; replace transmuted `liona thinoe` with `lima thinoe` | `lioru` is the condition and course that Gibran personifies as Life. `liona` names living as an activity, while the seed in the transmutation simply has the quality `lima`, alive. |
| Striving, seeking, trying, and intending | Preserve close `meloa` for strive; replace close `thueli` with negated `mesatu` for seek not | Gibran's first verb asks for effort sustained towards likeness, which is the centre of `meloa`. He then warns the parent against trying to make the offspring alike. `mesatu` states that action more closely than intention, while `sheraki` would mean searching for someone, something, a place, or an answer. |
| Belonging, ownership, and holding | Preserve close `phenori` and transmuted `phelu` | Gibran's belong means being possessed. Base `wema` concerns felt fit within a place, community, or relationship and explicitly never means ownership. The translation names the social claim; the transmutation answers it with the body's grasp. |
| Tomorrow's house and visiting | Preserve `wireo womu`, close `phemiru`, and transmuted distant presence | Gibran's tomorrow is a future beyond the parent's reach, not the following day. Household `phemiru` gives the close version a bounded stay at that home, while the transmutation keeps its plainer refusal of presence. |
| Bow, arrow, archer, and target | Preserve the close material descriptions and the transmuted tree, seed, and wind | `sepho` follows Gibran's sent forth without adding the applied release of `wapho`, throw. Cord, flexible wood, sharpness, flight, tool use, and a purpose marker reconstruct the source image without placing reusable weapon terms in Phi. The transmutation still removes aimed parenthood openly. |
| Active dependencies | Update the paired page, its continuous translation, the shared gap log, and phonetic-neighbour attestations | The repaired lines recur nowhere else in the active corpus. Gibran's stored source, its quoted lines, shelf links, and registered compounds remain unchanged. |

## Paired review: Tao Te Ching selections

The ground truth is James Legge's complete chapters 8, 11, 17, 63, and 76 from his 1891 *Tao Teh King*, stored in `texts/sources/tao_teh_king_1891.txt`. The close translation covers every proposition in 161 unique Phi forms, eleven of them optional. The transmutation uses 102 unique forms, all from the base vocabulary. It remains a selected reading: chapters 17 and 76 cite every source proposition, while chapters 8, 11, and 63 leave material behind.

| Learning path | Optional roots in the close translation |
|---|---|
| Commons and Collective Governance | `karami` (authority), `kowanu` (governance) |
| Accessibility and Participation | `kelasu` (usable) |
| Systems and Shared Infrastructure; Work, Craft, and Repair | `kelitho` (function) |
| Ecological Systems and Material Life; Systems and Shared Infrastructure | `mirela` (state), `pherami` (depend) |
| Ecological Systems and Material Life; Systems and Shared Infrastructure; Work, Craft, and Repair | `monaki` (component) |
| Work, Craft, and Repair | `pokera` (competent), `rinoka` (project) |
| Philosophical Reasoning | `themore` (argument) |
| Household and Daily Life | `tholupi` (room) |

| Area | Close translation | Transmutation |
|---|---|---|
| Water and contention | Water does not intend another place, and people dislike the low place it occupies. | Water helps everything and takes nothing. |
| Useful emptiness | Thirty wooden wheel components meet at an open center before pot and room repeat the dependency. | The wheel is omitted; possibility under `po` carries the pot, door, and window. |
| Political relation | Chapter 8 names governance; chapter 17 describes people who hold `karami`, authority, in society. | The rulers become people who guide. |
| Easy and difficult | `kethua` names difficult affairs and its negation supplies the easier state. | The promises, flavors, preparation, and difficulty chain stay outside the selection. |
| Dry and withered | At death plants are dry and have withered. | The selected plant line now says both as well. |
| Death and life | Rigidity and strength come with death; softness and weakness come with `lioru`, life. | The qualities remain companions of death and life. |
| Force and conquest | A person trusts the strength of their own people who act through force, then fails to fulfill the purpose Legge names as conquest. | Trust in strength brings no fruit. |
| Feller and wind | A broad tree is chosen by a tree cutter. | A rigid tree falls in wind while a flexible tree stays. |

No new root is needed. The pass replaces five older detours and corrects one noun choice. Commons `kowanu` now names government as a continuing arrangement for collective decisions. `monaki` calls the spokes functional parts, while their path through the wheel supplies their shape. Base `kethua` states difficulty directly, `kureno` restores withering, and `lioru` keeps life apart from the activity of living. Other gaps stay on the page as descriptions or source material: nave is one center, axle is a support rod, Tao keeps Legge's adjacent wording, and conquest stays named in the source citation. Translation does not hide people acting through force or the feller. Transmutation may refuse their direction after the source appears beside it.

### Post-migration contextual retrofit

Six distinctions alter the paired page. Several other candidates fail on meaning or would erase a declared transmutation choice.

| Question | Disposition | Reason |
|---|---|---|
| Government, governance, authority, and guidance | Replace close event-noun `punoa kulo` with Commons `punoa kowanu`; preserve close `karami` and transmuted `kulo` | Chapter 8 concerns the arrangement by which a society makes and carries out decisions, which is the center of `kowanu`. Chapter 17 needs the power relation itself, so `karami` remains. The transmutation deliberately turns rulers into guides; importing the translation's authority would undo that reframe. |
| Spokes, pieces, and components | Replace close classifier phrase `themo wolea` with `wolea monaki` | A spoke is not merely an arbitrary piece of wood. `monaki` identifies it by its function in the wheel, while the path from rim to center still supplies its geometry. Phi continues to lack dedicated spoke, nave, and axle roots. |
| Difficulty, perseverance, lightness, and burden | Replace chapter 63's difficulty chain with base `kethua` and its negation; preserve `meloa` elsewhere and the first `tupeka` | `kethua` explicitly covers a task or condition demanding substantial effort. `meloa` is the chosen act of continuing despite difficulty, not difficulty itself, while `phelo` concerns physical lightness or low intensity. The earlier `tupeka` remains right where Legge describes trouble as a felt burden. |
| Drying, ceased growth, and withering | Replace close `te thuroa` and add perfective `kureno` to both renderings | Ceasing to grow was only an observable edge of Legge's withered. Base `kureno` now names the plant process itself, and perfective `ki` presents it as complete at the time of death. `kurathi` remains because the source separately says dry. |
| Life, living, and death | Replace event-noun `liona` with `lioru` in both renderings; preserve event-noun `lumeo` | `lioru` is life as a condition and course, which is the relation Legge names. `liona` would make the quality a companion of living as an activity. Phi's event-noun rule already gives `lumeo`, die, its noun use death. |
| Concomitants and companions | Replace close `melu` with `nua ... shua`, come with; preserve transmuted `melu` | The close version no longer turns an abstract association into friendship. The transmutation may keep death's and life's companions as a literary personification, provided the comparison names the change. |
| Small, large, and English "great" | Preserve `thiku` and `whalo` throughout | Chapter 63 compares magnitude, number, and the scope of undertakings. Current `whalo` covers overall amount and broad scope, so this is not the importance homonym that required repair in the Heart Sutra. `sone`, value, would alter Laozi's paradox. |
| Brittle, fragile, and hard | Preserve `welua` for brittle | `welua` names susceptibility to damage, which is the useful contrast with living softness here. Adding `kethua` would assert resistance to indentation and still would not create a dedicated brittle quality. |
| Tao, virtue, praise, wheel parts, conquest, and feller | Preserve the stated limits and adjacent Legge lines | `keiro` is the selected ordinary way, good people do not acquire a doctrinal virtue, honor does not guarantee spoken praise, and the wheel's exact craft terms remain descriptive. Conquest and the feller stay audible in the close source without entering Phi's reusable peace vocabulary. |
| Optional module vocabulary | Preserve the close version's eleven optional roots and the transmutation's base-only path | Every optional root in the translation carries a distinction used by Legge's argument or material example. None improves the transmutation enough to outweigh its selected, ordinary register. |
| Active dependencies | Update the paired page, its continuous close block, the shared notes, and phonetic-neighbor attestations only | The changed Phi sentences recur nowhere else in the active corpus. Legge's stored source, its quoted lines, shelf links, and registered compounds remain unchanged. |

## Translation review: A Solarpunk Manifesto

The ground truth is the complete licensed English witness stored in `texts/sources/solarpunk_manifesto.txt`. Its five opening paragraphs, 22 propositions, and seven-part aesthetic list make 38 aligned units. The Phi translation uses 238 unique forms, 33 of them optional roots. This is the shelf's broadest module test because the manifesto speaks directly to Phi's first intended community audience; a specialist word still has to earn its sentence, but it need not apologize for being there.

| Module | Unique roots used |
|---|---:|
| Accessibility and Participation | 7 |
| Commons and Collective Governance | 12 |
| Ecological Systems and Material Life | 10 |
| Household and Daily Life | 2 |
| Medical and Bodily Care | 1 |
| Philosophical Reasoning | 2 |
| Systems and Shared Infrastructure | 10 |
| Work, Craft, and Repair | 10 |

### Post-migration contextual retrofit

The retrofit changes seventeen aligned units. It adopts later words where they restore a source distinction and removes several module terms from jobs their completed definitions do not permit. The remaining analytic phrases stay because capitalism, decolonialism, Jugaad, and the named schools of art and urbanism are wider than any honest Phi substitute.

| Question | Disposition | Reason |
|---|---|---|
| Fashion, aesthetics, and visible style | Replace `wetha kire` and two broad beauty phrases with base `senalu` | Fashion concerns characteristic choices across cloth and dress, not the act of shaping cloth. Aesthetics joins those choices across works; `mioru` remains where the manifesto actually judges beauty. |
| General solutions and medical remedy | Replace three uses of Medical `heloa` with `keiro`, way | `heloa` answers an ailment or discomfort. The manifesto's ecological and social solutions become practical ways, and the following clauses state what each way must accomplish. |
| Trying, wanting, and enthusiasm | Use base `mesatu`, `rinu`, and `rashowe` | Proposition 1 claims an attempt, proposition 14 claims a desire to oppose three futures, and proposition 4 names energetic enthusiasm. Practice, direct refusal, and joy-giving character each changed the source relation. |
| Fossil energy and replacement | Replace the fossil energy's ceased function with ceased passive supply | Energy does not perform a component's operation under `kelitho`. Ending its supply beside the supply of non-polluting energy makes the replacement relation audible. |
| One right tactic | Replace `telua`, accurate, with `theali`, fitting | Accuracy compares a representation with its reference. A tactic fits a purpose and circumstances, which is why several communities may choose differently without one factual description being wrong. |
| Generativity and technical capacity | Replace `kealo henora` with event-noun `kealo`, creation | Systems `henora` is a conditioned limit on what a system can hold, process, or deliver. Creation carries generativity without treating human or cultural ability as a technical parameter. |
| Politics, smart cities, corporations, and autonomous systems | Use Commons `kowanu` for politics; confine `ketora` to device-control and self-control systems; use `punoa karami` for corporate social power | Governance is still narrower than politics, and that limit remains stated. Technical control belongs to processes and variables. Institutions exercise authority over society; autonomous systems regulate themselves and then separately have to function. |
| Energy grids | Replace general energy networks with `thewaki kenua phaliso`, electrical-energy networks | The infrastructure reading of grid is electrical here. `thewaki` keeps electricity distinct from energy while the source retains its broader wording. |
| Ability and disability | Replace person-modifying `henora` with base `sowelu miona`, disabled people | Human ability is not system capacity. Disability can be named directly without turning it into sickness or assigning a universal scale of ability. The source line keeps its exact list of categories. |
| Fear, conditions of life, and overlord rank | Replace two technical states with a fear-causing path and better living; replace spatial `leo` with `muila karami`, authority over Earth | `mirela` gathers selected system conditions, and `leo` marks physical height. The revised clauses preserve the fear people feel, the way people live, and the social authority renounced by the source. |
| Final qualities | Replace Work `kirero` with `sherewa`, claims | The closing list contains four propositions, not one evaluation of a work against criteria. A spoken claim supplies the colon that Phi cannot leave silent. |
| Source boundaries and deliberate compositions | Preserve Solarpunk, the named genres, economic and political labels, Art Nouveau, Hayao Miyazaki, Jugaad, the 1800s, New Urbanism, and New Pedestrianism in the adjacent source lines | The Phi phrases expose the relation each term contributes to this manifesto. None pretends to exhaust the source identity, history, or theory. |
| Active dependencies | Update the annotated blocks, continuous translation, limits table, review ledger, and phonetic-neighbor attestations | The source citations remain byte-for-byte unchanged. The revised annotated and continuous Phi passages contain the same sentence sequence. |

## Transmutation review: The Little Prince excerpts

The page holds three short passages from Katherine Woods's 1943 translation: the sheep request, the fox's secret, and the responsibility that follows a bond. Copyright keeps the English to those quoted excerpts rather than a stored source witness. The Phi title and passages use 35 unique forms, all from base vocabulary. That modest reach suits the page: its work happens in ordinary words whose relations have to be exact.

### Post-migration contextual retrofit

Two changes are enough. One separates the English homonyms *plain* and *simple*; the other lets Phi's aspect agree with Woods's present perfect. The title, heart metaphor, and mutual bond remain deliberate transmutations rather than unfinished translations.

| Question | Disposition | Reason |
|---|---|---|
| Simple and plain | Replace `ru mueli kupela` with `ru siloma kupela` | `mueli` describes something without ornament. Woods calls the secret simple, and `siloma` gives its thought an uncomplicated arrangement without turning simplicity into an aesthetic judgement. |
| Have tamed | Replace past `to nolami` with perfective `ki nolami` | The bond is complete at the present reference time and grounds the responsibility that begins now. Simple past located it earlier but did not preserve Woods's present result. |
| Drawing the sheep | Preserve `kire` | The verb shapes material or line, and its current definition uses a pencil giving a sheep its drawn outline as the concrete case. A narrower art-form root would work against Phi's established account of a work through its making. |
| Heart, eyes, and seeing | Preserve `korua`, `mirae`, `nila`, and manner `theali` | The source turns on visual language and then denies the eye access to what matters. General `morae`, sense, would blur that contrast; `shelomu`, understand, would explain the metaphor instead of speaking it. |
| Taming and mutual bond | Preserve `nolami` with its comitative gap | The fox explains taming through created ties, and this transmutation accepts that explanation. `woenu` describes an animal accustomed to human presence or handling. It would move the sentence back towards tameness just where the transmutation chooses a mutual relation. |
| Responsibility, accountability, and obligation | Preserve base `thonai` | The speaker willingly takes up care for a relation. Optional `lothoni` requires answerability under review, while `naseru` names a requirement that may be imposed or disputed. Neither belongs in the fox's gift. |
| Title and rank | Preserve `thiku miona lue silero` beside the source title | The English keeps Prince exact. Phi describes the small person from the stars and declines to turn rank into a reusable role word. |
| Optional module vocabulary | Use none | The excerpts concern an ordinary request, perception, relationship, and care. The specialist distinctions considered above would change their centre rather than sharpen it. |
| Active dependencies | Update the excerpt page, review ledger, progress records, and phonetic-neighbor attestations | The three Woods quotations and the shared title remain unchanged. Neither revised Phi phrase recurs in another active passage. |

## Transmutation review: the Ring Verse refusal

The page quotes Tolkien's couplet and answers it with four Phi lines rather than promising a close translation. Its title and passage use 12 unique forms, all from base or function vocabulary. The lines remain exactly as rebuilt during the original shelf review: the Ring coerces, finds, brings, and physically ties all people. The completed Commons vocabulary changes the explanation around them, because Phi can now distinguish a social rule, enforcement, and authority from dominion without granting the Ring any of those narrower relations.

### Post-migration contextual retrofit

Nothing in the Phi needs repair. The later lexicon explains the choice more precisely and exposes one old account of `meipa`, seat, that no longer agrees with its entry.

| Question | Disposition | Reason |
|---|---|---|
| Rule and dominion | Preserve `kawhera`; distinguish `nasholu` in the explanation | `nasholu` is a social prescription. Tolkien's verb makes one being dominate others. `kawhera` identifies the practical choice that power closes without inventing a neutral dominion verb. |
| Authority, enforcement, and control | Do not insert `karami`, `nashaku`, or `ketora` | A holder may exercise `karami` within a social scope, but the noun leaves legitimacy open. `nashaku` acts in relation to a rule or decision. Systems `ketora` adjusts a technical process and says nothing about authority over people. Any of the three would tidy the Ring's act into the wrong kind of relation. |
| Binding and mutual bond | Preserve metaphorical `tiwa` and reject `nolami` | `tiwa` keeps the image bodily through fastening with a flexible line. `nolami` belongs to participants who form or sustain a mutual connection. The Ring imposes restraint; it does not enter a relationship. |
| Ring and darkness | Preserve `thumai sorui` and quality-noun `nuelo` | Finger-circle is the registered ordinary composition for a ring. Under the regular adjective rule, `nuelo` also covers darkness as a noun. Neither expression hides a source distinction or needs a specialist root. |
| Throne and seat | Keep throne in the source; correct the account of `meipa` | `meipa` is an object or prepared place made for sitting and may be reserved or exalted. It is audibly related to `meilo`, sit, but it is not that verb with a place suffix. Raising a seat does not give its occupant an unmarked dominion role. |
| Optional module vocabulary | Use none in the Phi lines | Commons vocabulary improves the analysis, not the transmutation. The verse's coercion, finding, bringing, darkness, and physical restraint are already expressible in ordinary Phi. |
| Source and active dependencies | Preserve Tolkien's quotation and every repeated Phi line; remove one stale canon claim | The source remains outside Phi byte-for-byte. The first and fourth lines recur in book chapter 2, and the first recurs in chapter 6; none needs repair. Canon incorrectly said that the present refusal used an older `kulo` line, so that historical assertion is removed without changing the verb-primary ruling. |

The refusal remains narrower than silence. Peace linguistics leaves the domination exposed while testimony stays possible. The Ring remains an act of coercion and imposed tying, not an office the lexicon makes clean.

## Transmutation review: The Velveteen Rabbit

The complete Williams story remains a transmutation with 430 aligned source units. Its revised Phi uses 407 unique forms. Thirteen optional roots have 18 memberships across six modules. Household vocabulary does most of the new work, as one might reasonably expect from a rabbit who spends so much of the story in a nursery.

### Post-migration contextual retrofit

Forty-six aligned units change. The source lines remain byte-for-byte unchanged. Most repairs replace an old paraphrase that had become inaccurate after the base lexicon grew; a smaller set lets module vocabulary name familiar objects in the nursery and sickroom. The story keeps its declared changes around rank, coercion, gendered kinship, military source language, clock time, and the Child's share in making the rabbit Real.

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

## Transmutation review: the original shelf pass

Before selective pairing began, the nine pending transmutations were read from their stated sources before the Phi was judged. Repair was preferred when the narrative or argument already held together. A clean rebuild was reserved for the Ring Verse's central refusal, whose earlier substitute had turned coercion into guidance and imposed binding into mutual bond. No new root was needed; the module vocabulary developed since these texts were written supplied the missing distinctions.

| Work | Source and decision | Material repairs | Pillar disposition |
|---|---|---|---|
| Babel | Complete KJV Genesis 11:1-9; repaired | Earth and sowing remain the chosen transmutation. Notes now describe that choice without claiming Phi is incapable of telling the punitive reading. | Solarpunk and Art Nouveau support the garden coda; preindustrial knowledge supports sowing; Buddhist and peace readings refuse punishment as the only account of diversity. The builders' fear and failed city remain. |
| UDHR Article 1 | Complete 1948 English Article 1; materially rebuilt | Dignity and rights no longer collapse into worth alone. Commons `shereni` adds equal entitlements, `po remo` restores a capacity to think, and kind reciprocal conduct replaces compulsory love. | Peace linguistics leaves feeling free from command while preserving obligation in conduct. Solarpunk supports durable entitlement; Buddhist thought supports equal worth. The aesthetic and preindustrial pillars require no separate change. |
| *The Little Prince* excerpts | Three short Katherine Woods excerpts; repaired and current | The title describes the small person from the stars while the source keeps prince. Simple no longer borrows the English homonym *plain*, and perfective aspect makes the bond's result current. | Buddhist and peace readings support mutual bond and chosen responsibility. The request and heart-seeing need no ecological or aesthetic rewrite beyond their existing images. |
| *The Prophet* excerpts | Gibran's 1923 text; repaired transmutations, with On Children paired | The sage-title is presented as a transmutation rather than a lexical incapacity. The tree, seed, and wind express parent-child release without an armory. | Solarpunk and preindustrial practice meet in planting; Art Nouveau favors the bending tree and moving seed; Buddhist and peace readings separate love and parenthood from possession. The paired translation reconstructs the source's bow in Phi. |
| Tao Te Ching selections | Five chapters from Legge 1891; repaired transmutation, now paired | Chapter 76 includes the warning about relying on forces: trust in strength alone brings no fruit. The close translation includes the complete chapters. | Water, vessel, wind, and yielding give all five pillars material to examine. Peace linguistics changes conquest into fruitlessness in the transmutation while the paired translation keeps reliance on force and the feller visible. |
| Heart Sutra | Müller's complete smaller sutra; repaired transmutation with omissions logged | The opening names all five aggregates instead of expanding them prematurely to all things. The printed knowledge and ignorance sequence is intentionally absent. Release is the transmutation of annihilation, and Müller's Nirvana appears beside deep peace. | Buddhist analysis governs the work. Peace linguistics shapes release without denying negation. The remaining pillars do not justify added ecological, craft, or decorative imagery. |
| Ring Verse refusal | Tolkien's quoted couplet; central Phi passage rebuilt | Rule becomes an explicit analysis as coercion; bind becomes physical `tiwa` used metaphorically. Guidance and mutual `nolami` no longer sanitize the Ring. | Peace linguistics makes the decisive change by naming constrained choice. Buddhist attention separates acts from permanent moral identities. The other pillars do not soften the source or invent a replacement moral. |
| *The Velveteen Rabbit* | Complete Williams story; repaired and current | The post-migration pass changes 46 units, separates search from finding and wear from age, and uses 13 optional roots across six modules. Brigand-play remains coercion-play, pain is not called small, and the child helps rather than single-handedly makes the rabbit Real. | Care, repair, natural transformation, material craft, and the story's organic beauty already engage all five pillars. Peace linguistics chiefly restores agency and names power; it does not remove fever, burning, loss, or grief. |
| *News from Nowhere*, chapters 1-3 | Complete Morris chapters; repaired chapter by chapter | Chapter 1 separates views, membership, and authority. Chapter 2 gives waking, bodily sensation, household detail, work capacity, and the river their completed distinctions. Chapter 3 adds direct rooms, meals, body parts, responses, and craft while retaining commoners' entitlement and the political direction of reactionary novels. | Solarpunk and preindustrial commitments are native to Morris's work; Art Nouveau lives in architecture, clothing, and craft. Buddhist attention clarifies the narrator's inference. Peace linguistics names authority and stigma without cleaning the argument, coercion, or social contempt from the story. |

The source citations and gap logs in each pamphlet hold the detailed decisions. The table records why the text remained a transmutation and whether repair or replacement was warranted.

## Literary shelf

| Active text | Method | Status | Note |
|---|---|---|---|
| `texts/north_wind_and_sun.md` | Translation + transmutation | Reviewed | Paired source, back-translation, vocabulary, and five-pillar comparison complete. |
| `texts/metta_sutta.md` | Translation | Reviewed | Full source-fidelity pass complete; two optional roots used where their distinctions matter. |
| `texts/solarpunk_manifesto.md` | Translation | Reviewed | The 238-form post-migration retrofit uses all eight modules while keeping political and cultural source terms exact beside transparent Phi analyses. |
| `texts/schleicher_fable.md` | Translation + transmutation | Reviewed | The post-migration retrofit preserves both renderings and repairs the supporting animal range of `kawhera` and `pilora`. |
| `texts/babel_text.md` | Translation + transmutation | Reviewed | Complete KJV alignment, translation limits, deliberate Earth and sowing departures, and five-pillar comparison complete. |
| `texts/human_rights_article_one.md` | Translation + transmutation | Reviewed | Paired source alignment, two source-facing roots, translation limits, gap log, and five-pillar comparison complete. |
| `texts/little_prince_excerpts.md` | Transmutation | Reviewed | The 35-form base-vocabulary work corrects the secret's quality and source aspect without giving up the mutual bond. |
| `texts/prophet_excerpts.md` | Translation + transmutation | Reviewed | Three transmuted teachings checked; On Children now has complete source alignment, translation limits, and a five-pillar comparison. |
| `texts/tao_te_ching.md` | Translation + transmutation | Reviewed | Five complete Legge chapters, translation limits, selected transmutation, and five-pillar comparison complete. |
| `texts/heart_sutra.md` | Translation + transmutation | Reviewed | Complete Müller alignment, translation limits, explicit transmutation omissions, and five-pillar comparison complete. |
| `texts/ring_verse_refusal.md` | Transmutation | Reviewed | The 12-form base-only refusal survives the post-migration pass; completed Commons terms sharpen the account without entering the four lines. |
| `texts/velveteen_rabbit.md` | Transmutation | Reviewed | The 430-unit post-migration pass changes 46 units and uses 13 optional roots across six modules without altering Williams's source lines. |
| `texts/news_from_nowhere/chapter_01.md` | Transmutation | Reviewed | The 85-unit post-migration pass changes 29 units and uses six optional roots across four modules without altering Morris's source lines. |
| `texts/news_from_nowhere/chapter_02.md` | Transmutation | Reviewed | The 241-unit post-migration pass changes 57 units and uses five optional roots with seven memberships across four modules without altering Morris's source lines. |
| `texts/news_from_nowhere/chapter_03.md` | Transmutation | Reviewed | The 245-unit post-migration pass changes 46 units and uses 14 optional roots with 15 memberships across five modules without altering Morris's source lines. |

The full transmutation shelf has received its original review and its post-migration contextual retrofit. Selective paired work has added close translations where a second rendering exposes Phi's capacity or its limits without displacing the transmutation. The drafted Phi book is current through chapter 7, including the dependent tide and service lines in *News from Nowhere* chapter 2 and the three exact Babel passages used to examine the literary method. Resume the manual-led remainder of SEM-09D before chapter 8.
