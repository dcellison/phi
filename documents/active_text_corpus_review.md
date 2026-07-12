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

## Transmutation review: The North Wind and the Sun

The ground truth is the 1919 *Aesop for Children* text stored at `pamphlets/sources/aesop_for_children.txt`. The reviewed Phi passage uses 97 unique forms, all from base vocabulary. At least 57 of those forms do not appear anywhere in the preceding primer chapters: 42 are content words and 15 are non-content forms. This is an attestation count, not a claim about how many a learner could infer.

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

Solarpunk and preindustrial values meet in the material scene: a traveler walks through weather, relies on cloth, and finds a roadside tree. Art Nouveau is present in the organic line of wind, sun, fruit, and shadow rather than an added ornament. The secular Buddhist pillar appears in release and in the refusal to freeze anger into identity. Peace linguistics changes the moral most. The text names coercion while leaving strength and loudness neutral. The Traveler's departure answers the contest.

No module word is required. `kawhera` belongs to base vocabulary because coercion can occur in any domain, and every other revised form is equally general. The fable can remain a capstone without asking a new learner to open a specialist lexicon.

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

## Literary shelf

| Active text | Method | Status | Note |
|---|---|---|---|
| `pamphlets/north_wind_and_sun.md` | Transmutation | Reviewed | Full source, back-translation, and value pass complete. |
| `pamphlets/metta_sutta.md` | Translation | Reviewed | Full source-fidelity pass complete; two optional roots used where their distinctions matter. |
| `pamphlets/schleicher_fable.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/babel_text.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/human_rights_article_one.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/little_prince_excerpts.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/prophet_excerpts.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/tao_te_ching.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/heart_sutra.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/ring_verse_refusal.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/velveteen_rabbit.md` | Transmutation | Pending | The shine-compound dependency is repaired; the story is not otherwise reviewed. |
| `pamphlets/news_from_nowhere_ch1.md` | Transmutation | Pending | Complete review not begun. |
| `pamphlets/news_from_nowhere_ch2.md` | Transmutation | Pending | One illumination line is repaired with the shine compound; the chapter is not otherwise reviewed. |
| `pamphlets/news_from_nowhere_ch3.md` | Transmutation | Pending | Complete review not begun. |

The next text begins at its source and declared method. A translation earns every narrowing; a transmutation earns every change.
