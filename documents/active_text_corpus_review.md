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

## Literary shelf

| Active text | Status | Note |
|---|---|---|
| `pamphlets/north_wind_and_sun.md` | Reviewed | Pilot complete. |
| `pamphlets/metta_sutta.md` | Pending | Complete review not begun. |
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
