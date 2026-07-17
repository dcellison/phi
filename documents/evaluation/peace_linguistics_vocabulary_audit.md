# Peace Linguistics Vocabulary Audit

**Audit date:** 17 July 2026

**Follow-up completed:** 17 July 2026

## Purpose and conclusion

This audit asks whether Phi's current vocabulary makes violence, domination, humiliation, or combat-shaped thought ordinary in the language. It covers all 1,221 current lexicon entries and excludes `archive/`. The result is mostly reassuring. No entry gives Phi a direct root for generic conflict, organised violence, a violent role, or a weapon. Phi is much more at home with consent, care, accountability, and repair.

The audit found one recent lexical concern. `patore`, glossed *hit*, entered the base vocabulary on 17 July 2026 in commit `6ef76685`, merged through PR #404. It never entered authored Phi or a registered compound. Its nonviolent uses divide cleanly among forceful contact, displacement, damage, injury, and rhythmic hand contact, so the broad root is retired rather than narrowed.

Most of the trouble found by the audit lay in older English lexicon prose. A small group described reasoning through victory, defeat, attack, or defence, while several craft entries still spoke of masters and servants. The follow-up migration has replaced those frames without changing a Phi root.

## Standard used

Peace linguistics treats language choice as an ethical act within a relationship. Francisco Gomes de Matos's chapter ["Planning uses of Peace Linguistics in second language education"](https://doi.org/10.1515/9783110518269-016) places human dignity, communicative responsibility, and anticipation of harmful effects at the centre of that practice. His earlier account of [peace-promoting vocabulary](https://www.humiliationstudies.org/news-old/archives/000304.html) gives practical weight to apology, comfort, gentleness, tact, cooperation, mediation, reconciliation, trust, and empathy.

The Global Center for Nonkilling's [*Nonkilling Linguistics*](https://nonkilling.org/pdf/nklinguistics.pdf) goes further. It argues for a vocabulary of peace rather than war, calls for the replacement of combat metaphors such as wars on social problems, and asks how violent vocabulary can be refused. It also warns language teachers not to turn peace education into censorship. That warning matters for natural languages and their speakers. Phi presents a different design question because its author deliberately chooses which distinctions receive easy, unmarked roots. A refusal here does not erase a person's testimony. Exact source wording remains available beside Phi, and Phi can still describe injury, coercion, danger, responsibility, and repair.

Phi's own standard is stronger and more specific. `canon.md` calls the language a practice of mindful and compassionate speech. The language guide says that core vocabulary resists normalising violence and domination while outside source material preserves testimony and critique. The development protocol adds the necessary safeguard: a refusal must not obstruct care, identity, consent, safety, testimony, or philosophical examination.

This produces a workable boundary. Phi can name a harmful effect or expose the mechanism that caused it. It does not need an ordinary root that makes the violent act, weapon, enemy role, or dominating office feel like one more neutral item in the room.

## Method

The repository contains 1,221 lexicon entries: 1,091 content words, 110 function words, and 20 interjections. I searched every string field in every current vocabulary JSON file: glosses, search terms, descriptions, usage notes, examples, semantic domains, sound symbolism, and pillar notes. The first pass looked for direct violent and domination vocabulary. A second pass looked for ordinary physical actions that can be used violently. A third examined pejorative person labels, combat metaphors, command and hierarchy language, and terms used to report coercion or institutional harm.

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

The governance terms pass for the same reason. Before the follow-up migration, `nashaku` contained a peace-linguistics note calling it a "neutral enforcement word." The revised entry now identifies enforcement as action under claimed authority, requires the actor and method to remain visible, and uses `kawhera` when power or threat narrows practical choice.

## History of the flagged vocabulary

| Entry or cluster | Introduction and later history | Finding |
|---|---|---|
| `patore` hit, `lerasu` cruel, `tisharu` puncture | Added together in commit `6ef76685` on 17 July 2026 and merged through PR #404 | `patore` is retired after the separate ruling below. The other two name ethical conduct and an ordinary physical process. |
| `kawhera` coerce and `whepelo` retaliate | Added to Commons in commit `d479c6c1` on 10 July, promoted to base vocabulary in `194b2bcd` on 12 July, and migrated to the target prose contract in `b44aebae` on 16 July | Keep. Their move to base made consent and institutional reprisal easier to discuss across domains; it did not broaden either word into a generic violence verb. |
| Commons power terms | `karami`, `nasholu`, `nashaku`, `norulo`, and `phenori` entered with the Commons module in `d479c6c1` | Keep in the module. Their definitions treat authority and ownership as claims that can be contested. |
| `tiwa` tie and `kawepa` catch | Added in the owner-approved core verb batch `c413061f` on 4 July | Kept and tightened. `tiwa` now requires consent or coercion to be stated when a person is restrained; `kawepa` focuses on physical interception and support rather than social capture. |

## Resolved lexical ruling

### 1. Inventory

Before retirement, `patore` appeared in ten tracked files. One was its lexicon entry, three were generated manual lexicon pages, and one was the generated readable decision register. The remaining five were project history, decision, coverage, and evaluation records. There was no independent use to translate or preserve.

### 2. Existing-vocabulary test

The stone example needs contact and manner, both already present:

```
kerou tomae kema palo.
stone floor strong touch.
(The stone touches the floor forcefully.)
```

If the contact drives something away, `pesa` (push) states that movement. If it worsens an object's condition, `pukeri` (damage) states the result; bodily injury is `kaworu`. When the stone fell before contact, `lepa` names that movement. Each choice tells the listener more than a general impact verb did.

Applause also composes without that root:

```
miona wi manuwe roe telui wiso palo.
person two hand INS rhythm RECP touch.
(A person's two hands touch each other in rhythm.)
```

The surrounding clause can then use `woraka` (appreciate), `pharuki` (celebrate), or `nomela` (encourage). This leaves room for a gathering that offers the same response through another gesture.

### 3. Decision

Retire `patore`. Its legitimate uses do not form one Phi concept that earns the unmarked extension to deliberate interpersonal hitting. Forceful contact remains easy to say, while movement and consequence stay available as their own claims.

### 4. Migration

The canonical entry is removed and `patore` is added to the short retired-form list, which prevents lexical reassignment while leaving the form eligible as an onym. `CV-HIT-01` now records the declined root, `CV-HIT-02` records the compositional result, and `CV-APPLAUSE-01` carries the rhythmic hand-contact expression. Generated lexicon references are rebuilt from the smaller inventory. D030 remains an accurate record of introduction; D033 records its partial supersession.

## Resolved prose rulings

### `tiwa` (tie) and `kawepa` (catch)

These older verbs have legitimate daily uses, but their former prose reached close to captivity. `tiwa` listed a person among the things that may be tied. `kawepa` said that catching brought a moving person or thing under immediate control. Neither root means capture or imprisonment, and `tiwa` has been used deliberately in the Ring Verse refusal to make imposed physical fastening uncomfortable rather than relational.

Both words remain. Cordwork stays at the centre of `tiwa`, with consent or coercion part of the account when a person is physically restrained. `kawepa` describes meeting a moving body or object to stop or support its motion; custody and confinement require separate claims.

### `thema` (guardian)

The inherited entry described people who could not protect themselves, then surrounded guardianship with heroic and martial scenery. Its replacement defines guardianship as entrusted protective care, limits the role's authority, and leaves the protected person's agency explicit. `shorupo` is now the act of protection, while `theluo` covers stewardship of shared resources and community life.

## Combat and hierarchy in the English prose

At the time of audit, twenty-seven entries contained at least one direct combat or violence word somewhere in their English fields. Fourteen used such a word literally to establish a useful boundary. `arm` and `knife`, for example, state that their Phi senses do not include weapons. `brave`, `courage`, and `bold` separate difficult truthful action from aggression. `peace` has to mention violence in order to define the condition. Those references still do honest semantic work.

The remaining thirteen used combat language as metaphor, inherited scenery, or an unnecessary contrast. Their roots were not the problem. Their prose has now been replaced.

| Area | Entries | Earlier framing removed |
|---|---|---|
| Philosophical reasoning | `claim`, `contradict`, `counterexample`, `dialogue`, `refute`, `retract` | A claim is defended, a counterexample defeats or targets it, speakers become enemies, dialogue rejects victory, refutation becomes attack, and revision becomes defeat. Claims can instead be supported, tested, found incompatible, revised, or shown false. |
| Nature and physical description | `fish`, `sail`, `water`, `height`, `storm` | Fish and sails fight forces, water is unconquered, high ground belongs to defence, and weather is violent. The physical actions are already available without importing combat. |
| Roles and values | `guardian`, `truth` | The guardian is explained against weapons and warriors, while truth becomes a weapon that should instead be a bridge. Direct definitions would carry both entries more cleanly. |

Hierarchy entered another legacy cluster. `apprentice`, `mentor`, and `student` referred to masters or master craftspeople; `guild` and `workshop` repeated the same frame. `scribe` was called a servant. `steward` rejected masters but still used the term as its contrast. The revised entries now speak of experienced practitioners and learners, along with recorders and accountable caretakers. Authority, membership, and consent are stated where they matter.

Several old `sound_symbolism` fields elsewhere in the lexicon still reach automatically for striking, force, command, and binding. The entries in this audit's repair set now use embodied phonesthetics. Their descriptions follow lip, tongue, and breath through closure and release. The broader legacy vocabulary prose audit should apply the same standard.

## Decision register repair

`CV-CONFLICT-01` was the most serious finding because it could have produced future coinage. The open candidate asked which words for conflict, violence, fighting, attack, defence, hunting, and killing belonged in the base language or a possible module. That was not a cautious prompt. It was an invitation to cross the boundary.

This audit records the candidate as declined. Modules are not a side door for violent vocabulary. Phi will continue to report harm and the power relations around it, then speak directly about protection, responsibility, redress, and repair. Exact violent terminology remains with its source when fidelity requires it. Generic violent acts and roles do not receive ordinary Phi roots merely because a coverage list noticed their absence.

The machine-checked register now closes `CV-HIT-02` with the compositional result and records the former root as declined under `CV-HIT-01`. The ritual-and-play batch is closed as well: its applause expression no longer depends on a general impact verb.

The neighbouring `CV-AIM-01` remains open, but its wording now asks only about physical alignment in craft or measurement. It no longer proposes a general target noun. Direction, orientation, intention, and purpose should continue to carry the abstract work unless an embodied practice reveals a narrower need.

## Admission test for future vocabulary

1. Ask what ordinary use the proposed root makes easy. A daily, caring, ecological, medical, or craft use may justify a physical word even when harm is possible.
2. Reject a proposal whose semantic centre is a weapon, enemy role, attack, violent contest, hunt, killing act, captivity, or dominating office.
3. Admit a harm-reporting word only when it improves consent, care, warning, testimony, accountability, or repair. Its definition should expose the mechanism or effect and should not turn a person into a fixed harmful kind.
4. Keep exact source terms outside Phi when the source wording is itself the fact being preserved. Translation and description may still state what happened.
5. Check every English field for combat metaphors. A peaceful root taught through attack, victory, conquest, or defence still carries the unwanted frame into the language's habits.

## Follow-up completed

1. `tiwa`, `kawepa`, `thema`, and `nashaku` now state their physical or institutional scope directly. Their entries also make agency, consent, and coercion visible.
2. The thirteen combat-metaphor entries now describe logical relations and physical properties without importing victory or martial scenery. Their accounts of weather, care, and truth are direct as well.
3. The seven hierarchy entries now define learning, craft association, record-keeping, and stewardship without master or servant framing.

Phi has not quietly acquired a vocabulary of war. Its one new general impact verb had no corpus life and is now retired. This follow-up also clears the old metaphors identified by the audit; the wider prose migration remains responsible for finding the same habits elsewhere.
