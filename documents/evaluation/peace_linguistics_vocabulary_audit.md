# Peace Linguistics Vocabulary Audit

**Audit date:** 17 July 2026

## Purpose and conclusion

This audit asks whether Phi's current vocabulary makes violence, domination, humiliation, or combat-shaped thought ordinary in the language. It covers all 1,222 current lexicon entries and excludes `archive/`. The result is mostly reassuring. No entry gives Phi a direct root for generic conflict, organised violence, a violent role, or a weapon. Phi is much more at home with consent, care, accountability, and repair.

One recent word does need a fresh ruling. `patore`, glossed *hit*, entered the base vocabulary on 17 July 2026 in commit `6ef76685`, merged through PR #404. It is defined as a brief forceful impact whose intent and harm remain open. That is careful semantics, but its broad range also gives Phi an unmarked verb for one person hitting another. I cannot clear it merely because its example is a stone striking a floor. My recommendation is to review `patore` in a separate breaking-change decision and retire the broad sense unless its nonviolent uses justify the cost. If it stays, its centre should be physical impact, with deliberate interpersonal blows kept outside the unmarked sense.

The larger weakness is in English lexicon prose, especially older entries. A small group describes reasoning through victory, defeat, attack, or defence, and several inherited craft entries still speak of masters and servants. Those words are not Phi roots, but they teach speakers how Phi's concepts are imagined. They belong in the legacy prose migration, where they can be removed without changing the lexicon.

## Standard used

Peace linguistics treats language choice as an ethical act within a relationship. Francisco Gomes de Matos's chapter ["Planning uses of Peace Linguistics in second language education"](https://doi.org/10.1515/9783110518269-016) places human dignity, communicative responsibility, and anticipation of harmful effects at the centre of that practice. His earlier account of [peace-promoting vocabulary](https://www.humiliationstudies.org/news-old/archives/000304.html) gives practical weight to apology, comfort, gentleness, tact, cooperation, mediation, reconciliation, trust, and empathy.

The Global Center for Nonkilling's [*Nonkilling Linguistics*](https://nonkilling.org/pdf/nklinguistics.pdf) goes further. It argues for a vocabulary of peace rather than war, calls for the replacement of combat metaphors such as wars on social problems, and asks how violent vocabulary can be refused. It also warns language teachers not to turn peace education into censorship. That warning matters for natural languages and their speakers. Phi presents a different design question because its author deliberately chooses which distinctions receive easy, unmarked roots. A refusal here does not erase a person's testimony. Exact source wording remains available beside Phi, and Phi can still describe injury, coercion, danger, responsibility, and repair.

Phi's own standard is stronger and more specific. `canon.md` calls the language a practice of mindful and compassionate speech. The language guide says that core vocabulary resists normalising violence and domination while outside source material preserves testimony and critique. The development protocol adds the necessary safeguard: a refusal must not obstruct care, identity, consent, safety, testimony, or philosophical examination.

This produces a workable boundary. Phi can name a harmful effect or expose the mechanism that caused it. It does not need an ordinary root that makes the violent act, weapon, enemy role, or dominating office feel like one more neutral item in the room.

## Method

The repository contains 1,222 lexicon entries: 1,092 content words, 110 function words, and 20 interjections. I searched every string field in every current vocabulary JSON file: glosses, search terms, descriptions, usage notes, examples, semantic domains, sound symbolism, and pillar notes. The first pass looked for direct violent and domination vocabulary. A second pass looked for ordinary physical actions that can be used violently. A third examined pejorative person labels, combat metaphors, command and hierarchy language, and terms used to report coercion or institutional harm.

Every flagged entry then received a manual semantic reading. Git history supplied the introduction date and later scope changes for the words most likely to have entered through the recent coverage work. Generated references were not counted as independent lexical evidence because they repeat the canonical JSON.

## Lexical findings

| Class | Current examples | Assessment |
|---|---|---|
| Direct violence, war, and enmity | No current glosses for conflict, attack, fight, battle, war, weapon, kill, murder, enemy, defence, combat, hunt, slaughter, violence, aggression, conquest, victory, warrior, capture, or captivity | Correctly absent. The refusal now covers generic conflict and direct roots centred on violent acts, weapons, enemies, and war. |
| Harm, condition, and consequence | `pukea` danger, `peloma` harmful, `pukeri` damage, `kaworu` injury, `kipona` pain, `lumeo` die | Keep. These words let a speaker warn, seek care, describe an event, and discuss responsibility without creating a verb for killing or attack. |
| Harmful conduct and power | `kawhera` coerce, `whepelo` retaliate, `lerasu` cruel, `pilora` exploit, `pharomu` exclude, `wheparu` discriminate | Keep. Their definitions expose actors, effects, power relations, and evidence. They make testimony and accountability possible instead of supplying attractive or euphemistic language for the conduct. |
| Institutional claims | `karami` authority, `nasholu` rule, `nashaku` enforce, `norulo` jurisdiction, `phenori` ownership | Keep in their modules. Each word separates a claimed power from legitimacy, consent, justice, or care. They permit examination of institutions without granting those institutions moral standing. |
| Technical control | `ketora` control | Keep. Its definition is confined to technical processes and explicitly excludes control over people. |
| Ordinary tools and material acts | `kati` cut, `katiru` knife, `tisharu` puncture, `wapho` throw, `pesa` push, `natu` pull, `pukate` break, `thape` burn, `toka` hammer, `kirato` lock | Keep. Their ordinary centres are cooking, craft, movement, fire, repair, and household boundaries. A harmful use of a tool does not turn its ordinary tool name into weapon vocabulary. |
| Negative judgement and difficult feeling | `peshu` lie, `tawimo` foolish, `nupira` shame | Keep with their present boundaries. `peshu` requires known falsehood and intent to mislead. `tawimo` belongs first to an act or choice and rejects use as a contemptuous class label. `nupira` names the person's felt experience rather than endorsing humiliation. |
| Peace-promoting practice | `lesawi` consent, `naweri` refuse, `molawi` cooperate, `shorupo` protect, `shiroka` repair, `helolu` redress, `warosha` reconcile, `ruesha` compassionate | Keep and continue teaching prominently. Peace linguistics needs more than the absence of weapons. Phi already has a substantial constructive vocabulary for agency, care, and response after harm. |

The distinction between harm-reporting words and violence-normalising words is not cosmetic. Without `kawhera`, polite coercion becomes harder to expose. Without `whepelo`, an institution can present reprisal as an unrelated inconvenience. Without `kaworu`, a person loses a direct way to report bodily injury. These words earn their place because they make power and effect more visible.

The governance terms pass for the same reason, although `nashaku` contains one sentence that should change during prose migration. Its peace-linguistics note calls it a "neutral enforcement word." The entry itself does not treat enforcement as neutral, and neither should the note. The useful claim is that an explicit verb reveals the enforcing actor and method.

## History of the flagged vocabulary

| Entry or cluster | Introduction and later history | Finding |
|---|---|---|
| `patore` hit, `lerasu` cruel, `tisharu` puncture | Added together in commit `6ef76685` on 17 July 2026 and merged through PR #404 | Only `patore` needs a new peace-linguistic ruling. The other two name ethical conduct and an ordinary physical process. |
| `kawhera` coerce and `whepelo` retaliate | Added to Commons in commit `d479c6c1` on 10 July, promoted to base vocabulary in `194b2bcd` on 12 July, and migrated to the target prose contract in `b44aebae` on 16 July | Keep. Their move to base made consent and institutional reprisal easier to discuss across domains; it did not broaden either word into a generic violence verb. |
| Commons power terms | `karami`, `nasholu`, `nashaku`, `norulo`, and `phenori` entered with the Commons module in `d479c6c1` | Keep in the module. Their definitions treat authority and ownership as claims that can be contested. |
| `tiwa` tie and `kawepa` catch | Added in the owner-approved core verb batch `c413061f` on 4 July | Keep, then tighten their person-directed wording during prose migration. They predate the recent recovery batch. |

## Entries requiring a later ruling

### `patore` (hit)

`patore` is the only root introduced in the 17 July batch that sits directly on the peace-linguistic boundary. The same commit added `lerasu` (cruel) and `tisharu` (puncture), but those words have clearer work. Cruelty is an ethical judgement about avoidable suffering, while puncture covers needles, thorns, and drills. `patore` covers a falling stone, a swinging tool, or a moving hand. Its `strike` search term makes the broader invitation plain.

The word may still prove defensible as a neutral impact verb for accidents, craft, and hand contact in applause. The present record does not settle that question. A separate ruling should compare those uses with transparent expressions built from `palo` (touch), an explicit manner, and the actual result. Until then, `patore` should be treated as under review rather than as proof that general violence vocabulary belongs in Phi.

### `tiwa` (tie) and `kawepa` (catch)

These older verbs have legitimate daily uses, but their prose reaches close to captivity. `tiwa` currently lists a person among the things that may be tied. `kawepa` says that catching brings a moving person or thing under immediate control. Neither root means capture or imprisonment, and `tiwa` has been used deliberately in the Ring Verse refusal to make imposed physical fastening uncomfortable rather than relational.

Both words should remain. During their prose migration, `tiwa` should keep cordwork at its centre and make consent or coercion explicit when a person is physically restrained. `kawepa` should describe stopping or supporting motion without borrowing the social sense of capturing a person. That repair would protect the useful physical meanings without pretending that restraint cannot be reported.

### `thema` (guardian)

The root is usable, but its inherited entry does not speak in Phi's present voice. It describes people who cannot protect themselves, then builds a heroic contrast among wisdom, weapons, walls, strength, force, and a warrior archetype. The result is paternalistic even while trying to reject violence. A later target-schema migration should define the actual relationship, who recognises it, and the protected person's agency. The martial scenery can go.

## Combat and hierarchy in the English prose

Twenty-seven entries contain at least one direct combat or violence word somewhere in their English fields. Fourteen use such a word literally to establish a useful boundary. `arm` and `knife`, for example, state that their Phi senses do not include weapons. `brave`, `courage`, and `bold` separate difficult truthful action from aggression. `peace` has to mention violence in order to define the condition. Those references are doing honest semantic work.

Thirteen entries use combat language as metaphor, inherited scenery, or an unnecessary contrast. Their roots are not the problem. Their prose is.

| Area | Entries | Current framing to remove |
|---|---|---|
| Philosophical reasoning | `claim`, `contradict`, `counterexample`, `dialogue`, `refute`, `retract` | A claim is defended, a counterexample defeats or targets it, speakers become enemies, dialogue rejects victory, refutation becomes attack, and revision becomes defeat. Claims can instead be supported, tested, found incompatible, revised, or shown false. |
| Nature and physical description | `fish`, `sail`, `water`, `height`, `storm` | Fish and sails fight forces, water is unconquered, high ground belongs to defence, and weather is violent. The physical actions are already available without importing combat. |
| Roles and values | `guardian`, `truth` | The guardian is explained against weapons and warriors, while truth becomes a weapon that should instead be a bridge. Direct definitions would carry both entries more cleanly. |

Hierarchy enters another legacy cluster. `apprentice`, `guild`, `mentor`, `student`, and `workshop` refer to masters or master craftspeople. `scribe` is called a servant. `steward` rejects masters but still uses the term as its contrast. Phi has already refused a master role in its own vocabulary. These inherited English fields should speak instead of experienced craftspeople, learners, recorders, and caretakers, with authority and consent stated where they matter.

Several old `sound_symbolism` fields also reach automatically for striking, force, command, and binding. Most describe the feel of stops or tools rather than violence, so they do not change a word's meaning. They still belong in the planned legacy vocabulary prose audit. Embodied phonesthetics can describe the mouth without making every firm consonant throw a punch.

## Decision register repair

`CV-CONFLICT-01` was the most serious finding because it could have produced future coinage. The open candidate asked which words for conflict, violence, fighting, attack, defence, hunting, and killing belonged in the base language or a possible module. That was not a cautious prompt. It was an invitation to cross the boundary.

This audit records the candidate as declined. Modules are not a side door for violent vocabulary. Phi will continue to report harm and the power relations around it, then speak directly about protection, responsibility, redress, and repair. Exact violent terminology remains with its source when fidelity requires it. Generic violent acts and roles do not receive ordinary Phi roots merely because a coverage list noticed their absence.

The machine-checked register now carries `CV-HIT-02` as well. It records the open question about `patore` in both the contact-and-force and ritual-and-play batches, so the present applause construction cannot make the broader retention question disappear.

The neighbouring `CV-AIM-01` remains open, but its wording now asks only about physical alignment in craft or measurement. It no longer proposes a general target noun. Direction, orientation, intention, and purpose should continue to carry the abstract work unless an embodied practice reveals a narrower need.

## Admission test for future vocabulary

1. Ask what ordinary use the proposed root makes easy. A daily, caring, ecological, medical, or craft use may justify a physical word even when harm is possible.
2. Reject a proposal whose semantic centre is a weapon, enemy role, attack, violent contest, hunt, killing act, captivity, or dominating office.
3. Admit a harm-reporting word only when it improves consent, care, warning, testimony, accountability, or repair. Its definition should expose the mechanism or effect and should not turn a person into a fixed harmful kind.
4. Keep exact source terms outside Phi when the source wording is itself the fact being preserved. Translation and description may still state what happened.
5. Check every English field for combat metaphors. A peaceful root taught through attack, victory, conquest, or defence still carries the unwanted frame into the language's habits.

## Recommended order of follow-up

The next decision should be `CV-HIT-02`, since `patore` is recent and changes the base lexicon. After that, the target-schema migration can tighten `tiwa`, `kawepa`, `thema`, and the note for `nashaku`. The thirteen combat-metaphor entries and seven hierarchy entries fit naturally into the wider legacy vocabulary prose audit already planned. No other current root requires retirement on the evidence found here.

Phi has not quietly acquired a vocabulary of war. It did, however, leave one new force verb at the threshold and several old metaphors in the furniture. The threshold now has a marker. The furniture can be moved without rebuilding the house.
