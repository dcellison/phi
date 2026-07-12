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
| Source and proposition | Does the Phi passage preserve the source's relevant claim, image, event, or deliberate transformation without presenting a transmutation as a quotation? |
| Lexicon semantics | Does every content word fit its full concept and description rather than merely sharing an English gloss? |
| Module vocabulary | Does an optional term say the thought more exactly, or would it only advertise a module and burden this text's intended reader? |
| Composition | Is the existing phrase natural Phi, and does its transparency teach something a dedicated term would hide? |
| Learning role | Does the surrounding material describe honestly what the reader has already learned and what help the text still supplies? |
| Dependencies | Do compound rows, lexicon notes, excerpts, exercises, and repeated complete-text blocks agree with the reviewed passage? |
| Validation | Do the targeted validator, full validator, generated-reference check, and Markdown formatting checks pass after the decisions are applied? |

Module vocabulary is adopted when its meaning earns the place. A transparent base expression remains when it is natural or better suited to the learning path, and a before-state passage stays unchanged when its limitations are evidence.

## Pilot: The North Wind and the Sun

The ground truth is the 1919 *Aesop for Children* text stored at `pamphlets/sources/aesop_for_children.txt`. The reviewed Phi passage uses 96 unique forms, all from base vocabulary. At least 56 of those forms do not appear anywhere in the preceding primer chapters: 42 are content words and 14 are non-content forms. This is an attestation count, not a claim about how many a learner could infer.

| Area | Finding | Disposition |
|---|---|---|
| Giving light | `phelo` means light in weight. The phrase `phelo loa` depended on the English homonym and did not compose in Phi. Other illumination uses hid behind tense or intervening descriptors. | `keru` now carries brightness, and `keru loa`, give brightness, is the registered compound. Exact gloss lines use `bright`; genuine weight and unburdened uses of `phelo` remain. |
| Pale color and lightning | One Morris line used weight-light `phelo` for pale green, though the color chapter composes pale hues with `whilo` (white). The `pheluka` (lightning) entry also claimed a false derivation from `phelo`. | `whilo liro` now carries pale green. The atomic lightning form remains, while its entry describes the storm flash directly and accounts for `phe`, stressed `lu`, and final `ka`. |
| The Wind's efforts | `theko` is skilled craft, while `riola` is purposeful labor that contributes beyond the self. Neither suits an attempt to tear away a cloak. | `theula rena shia to phoa`, all that he did, now carries the line. It stays in base vocabulary and moves closer to Aesop's "all his efforts." |
| Quarrel and argument | `themore` names premises organized for a conclusion and explicitly excludes quarrels. `shareo` keeps the interaction while fire and loud voice preserve its heat. | `shareo` stays, and the note makes the contrast explicit. |
| Wager and proposal | `repora` places a possible collective action into consideration. The Sun's optative invitation and `nawo` already carry this small exchange without importing a governance register. | The wager remains spoken agreement. |
| Test and failure | `somaki` is a defined evidence-gathering procedure. `thonuki` is failure to perform a required technical function. The contest is not a test procedure, and the moral is not a technical failure report. | The parallel attempts and fruit metaphor stay; the note explains why the technical failure verb does not belong in the moral. |
| Canon claims | No current canon ruling refuses quarrel, win, or generic fail vocabulary as a class. The earlier notes attributed lexical absence to canon without support. | The notes now describe the actual lexical boundaries without claiming a canon ruling. |
| Primer capstone | The fable contains comparison, causation, passive voice, the optative, unfamiliar relators, and unfamiliar vocabulary. Calling it unassisted made the learner responsible for a curricular gap. | The capstone is now an annotated bridge whose glosses and back-translations belong to the reading method. |
| Active dependencies | The semantic family reaches primer lessons, manual prose, evidentiality exercises, *The Velveteen Rabbit*, *News from Nowhere*, `kia.md`, the compound registry, and several lexicon entries. The blow entry also described a fable line that no longer existed. | The family is repaired, and the blow note cites the current comparative line. These narrow repairs do not count as complete reviews of the other texts. |

The Phi passage adds no module vocabulary. That result is useful: this review is a semantic audit, not a tour arranged to show off the new modules. The larger lexicon can sharpen a text by confirming that an older composition is still the right one.

## Review: The Metta Sutta

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

| Active text | Status | Note |
|---|---|---|
| `pamphlets/north_wind_and_sun.md` | Reviewed | Pilot complete. |
| `pamphlets/metta_sutta.md` | Reviewed | Full source-fidelity pass complete; two optional roots used where their distinctions matter. |
| `pamphlets/schleicher_fable.md` | Pending | Complete review not begun. |
| `pamphlets/babel_text.md` | Pending | Complete review not begun. |
| `pamphlets/human_rights_article_one.md` | Pending | Complete review not begun. |
| `pamphlets/little_prince_excerpts.md` | Pending | Complete review not begun. |
| `pamphlets/prophet_excerpts.md` | Pending | Complete review not begun. |
| `pamphlets/tao_te_ching.md` | Pending | Complete review not begun. |
| `pamphlets/heart_sutra.md` | Pending | Complete review not begun. |
| `pamphlets/ring_verse_refusal.md` | Pending | Complete review not begun. |
| `pamphlets/velveteen_rabbit.md` | Pending | The shine-compound dependency is repaired; the story is not otherwise reviewed. |
| `pamphlets/news_from_nowhere_ch1.md` | Pending | Complete review not begun. |
| `pamphlets/news_from_nowhere_ch2.md` | Pending | One illumination line is repaired with the shine compound; the chapter is not otherwise reviewed. |
| `pamphlets/news_from_nowhere_ch3.md` | Pending | Complete review not begun. |

The next text begins at its source, then earns every change line by line.
