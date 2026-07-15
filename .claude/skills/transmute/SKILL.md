---
name: transmute
version: 1.0.0
description: |
  Transmute a source text into Phi: survey the source and the lexicon
  thoroughly before drafting, use Phi's grammar and vocabulary to
  their fullest to recreate the source's full intent, and favor
  coining or composing over compressing away imagery or settling for
  a near-word. Structure the result as validated example blocks with
  a gap log. Use for any new or revised file on the texts shelf
  (texts/*.md and texts/news_from_nowhere/*.md, rendered under build/site/texts/), whether a whole chapter or
  a single-line correction.
compatibility: phi-repo (Claude Code)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebFetch
  - AskUserQuestion
---

# Transmute: turning a source text into Phi

This skill exists because the first pass at News from Nowhere ch. 1 got the process wrong twice: once by compressing the original's imagery away by default, and once by trusting a vocabulary search that silently returned nothing when the words it was looking for were sitting in the lexicon the whole time. Both failures are avoidable if the steps below are followed in order, every time, including for a one-line fix.

## The governing principle

Phi is designed for full expressive parity with any natural language: it can specify anything other human languages can specify, given a deep enough search of its vocabulary, its compound registry, and its grammar. A transmutation takes full advantage of all three. The target is the source's full intent, its images, its stance, its irony, its pace, and its force, not a paraphrase of its plot. When a rendering comes out flat or generic, treat that as evidence of an incomplete search, never as a limit of the language: dig deeper before compressing, generalizing, or substituting a near-word, and reach for coining only once the search has genuinely been exhausted.

## The ten failures this skill guards against

1. **Compressing instead of checking.** An elm became generic `shiro` (tree). A crowded, stinking carriage became a bare "sad heart." A discussion's brisk pace and the Revolution it turned on were dropped entirely. In every case the missing word or construction was already in the lexicon; it had just never been searched for properly.
2. **Trusting a negative search result.** A vocabulary-search script that expected each file under the three entry directories to be a list with an `entries` or `words` key silently returned zero hits for every single query, because each entry file is actually one JSON object. This nearly produced a false report that Phi lacked words for "brisk," "meeting," "revolution," and "vigorous." All four already existed.
3. **Checking the words and not the grammar.** Every image in News from Nowhere ch. 1 survived steps 1 through 4, and the chapter still under-used Phi's own particle system: modality (`po`, `na`) never appears once in the whole chapter, evidentiality is marked exactly once (`ti`, opening the frame) though the chapter is one long narrated account, discourse adverbs are marked once (`thelao`) though the discussion turns sharply from good-tempered to a shout, and focus (`ko`) and restriction (`li`) never appear at all. None of this was a considered choice; nothing had prompted a check for it.
4. **Fetching fragments instead of the full text.** Asking a summarizing fetch tool for isolated, pre-guessed passages ("find the text between X and Y") requires already knowing the right boundaries, and the summarizing model can silently clip its own quotes to fit an output limit, returning something that looks verbatim but is not. Retrieving the complete source once and reading it directly caught a real error a fragmentary approach had missed: a brevity Morris states twice (a habitual mood, and separately a habitual temper, each described as passing quickly) had collapsed into one sentence that attached the wrong quality to the wrong thing.
5. **Letting a citation claim more than its own unit translates.** Two adjacent two-word sentences (`kohura ki nai`, `maeli ki nai`) shared one long, ellipsis-truncated citation instead of each getting the precise clause it translates, and a separate unit citing pure state ("he was alone," no verb of motion) carried the citation "took his way home by himself," attributing movement to a sentence that has none. The translation itself was complete; the citations made it look like the transmutation had dropped most of the sentence, because each excerpt promised far more than its own two or three words delivered. Daniel caught this by reading the shipped block, not by checking the source.
6. **Merging two actions into one clause by attaching a manner word to the nearest verb instead of the right one.** "Having said good-night very amicably, took his way home" became `shia ... to noeli wepu`, "he went home, amicably," attaching `noeli` (warm) to `wepu` (go) instead of to the parting that was actually amicable. Nothing was dropped from the word search; the sentence just claimed something the source never says, that the journey itself was amicable, while the real amicable act had no verb of its own at all. Daniel: "One does not travel amicably. He said good-night amicably." This is compression wearing a different shape: not a missing word, but two distinct actions sharing one clause because the manner slot was sitting right there.
7. **Letting the back-translation drift from what the Phi word actually says, in either direction.** `shia ki kapura.` was glossed `(He shouted.)`, though `kapura`'s own lexicon entry defines it as a cry "with sudden force, the voice breaking past its ordinary bounds," stronger than plain loudness, chosen specifically to carry "roaring out very loud." Daniel: "Please be more descriptive from now on. 'he shouted' isn't even close to 'and finished by roaring out very loud'." But the very next fix, in the same pass, overcorrected the other way: `shia mena lo miona tawimo nai meno haolu` (he said the others were foolish, `haolu` a plain, contentless verb of speech) got glossed `(He damned the rest of them as fools.)`, inventing a contempt the Phi does not contain to match Morris's "damning." Daniel: "You can't just pretend the Phi has words in it that it doesn't!! ... You are destroying the information from the Phi!" The real fix composed `thiku nila` (small-see, already in the lexicon as the compound for shame inflicted from outside) as its own sentence, giving the damning an actual Phi verb instead of dressing up the gloss of a verb that doesn't mean that. The test is the same in both directions: open the Phi word's own lexicon entry before writing the parenthetical English, and let the back-translation say exactly as much as that entry supports, no less and no more. If the source seems to need more than the current Phi carries, that is a signal to search, compose, or coin (see step 2 and 3), never to let the English gloss quietly say something the Phi sentence does not.
8. **Settling for a flat rendering or a near-word on the assumption that Phi cannot say the thing.** "Finished by roaring out very loud" seemed to have no tool for "finished by" (no cessative fit, no discourse adverb fit) until `shareo lumae` (the discussion's end) composed it as a plain locative adjunct, reusing `lumae`, a word already doing separate work in the same chapter inside `sileta lumae` (the sun's end, west). "Damning all the rest for fools" was first rendered with `haolu` (speak), a plain verb with no contempt in it, when `thiku nila` (small-see) already stood in the compound registry as the act of contempt, named in `shame.json` as shame's own cousin. An amicable good-night had no verb of its own until `pholeni` (depart) turned out to bundle "the farewell spoken" into its own definition. "A man whom he knows very well indeed" was cut as unreachable until the pre-nominal relative clause carried it cleanly (`rena melu ru sano miona`). In every case the exact tool was already in the language before the question was asked; the gap was in the searching. Daniel, after the last of these: "ALWAYS use Phi's grammar to its fullest. That's the whole idea of the language! It can specify anything other human languages can specify. You just need to dig deep enough." A lazy substitution is not a smaller version of the right answer; it is a wrong answer that hides a findable right one.
9. **Writing the grammar in the source language's order.** Ten units across one chapter put a relator after its object (`shalimo mua`, `womu mua`, `luphore kau`) though canon, the preposition reference, and every other text in the corpus put every preposition before its object, and an eleventh instance sat inside `pothu`'s own lexicon entry, coined during the same drafting: the error travels with the drafting hand into whatever it touches. Two more sentences left `ro` (HAB) floating before the predicate noun phrase (`shia ro teku korua nupira to nai`) instead of inside Slot 1 (`to ro nai`), while a third sentence in the same section placed its cluster correctly (that sentence's habitual later proved to belong outside the cluster entirely; failure 10 tells that story). The vocabulary search was thorough, every image survived, the citations were precise, and the sentences were still wrong. No search catches this failure, because nothing is missing; the words are simply standing where English would put them. Word order is verified by reading each drafted sentence back against the grammar references (step 6), and the validator's postposed-preposition net catches only the mechanically detectable slice, a preposition followed by a Slot 1 particle or standing sentence-final.

10. **Stacking an aspect onto a causative cluster when the aspect belongs to the caused event.** "The means of travelling which civilisation has forced upon us like a habit" became `punoa roe nurako lo miona to ro ka wepu`, one causative clause with `ro` (HAB) riding in its Slot 1 cluster, back-translated "(Civilization habitually forces people to travel by railway.)" Daniel: "Civilization does nothing habitually. It forces people to habitually travel by railway." A Slot 1 cluster has one scope, its own clause's event, and under `ka` that event is the causing (canon reads modals on `ka` the same way), so the habit sat on the forcing no matter what the back-translation wished. The repair gives the caused event its own clause and lets a word carry the repetition: `punoa roe nurako lo miona to ka wepu. ha wepu keno to kelu.` (society made people go by railway; this going became a custom). The tell is an adverb that reads naturally on either verb of the English: wherever it lands there, check which event the Phi's structure actually modifies, because failure 6's lesson (manner attached to the nearest verb instead of the right one) applies to aspect too, and the cluster's compactness hides the wrong reading better than a manner slot ever did.

Everything below is built to catch these ten failures before they reach a file.

## 1. Survey the source

- Check the source's copyright status before doing anything else. Public domain: author died more than 70 years ago, or first published before roughly 1930 in the US (verify the exact cutoff year at the time of writing, it moves annually). If public domain, retrieve the complete source text and work from that directly, not from a sequence of prompted excerpts. For a plain-text edition (Project Gutenberg's `.txt` files, for instance), `curl` the raw file to the scratchpad and read it with the `Read` tool; this returns the exact text with no summarizing intermediary. Reserve `WebFetch` for sources with no plain-text form, and even then ask it to return a whole chapter or section verbatim rather than a targeted excerpt. Never work from memory or a half-remembered plot summary; memory of a text is frequently wrong in specific, plot-relevant ways.
- If the source is still under active copyright, do not quote it at length. Work from short, sparing excerpts only, skip the source-quote-line convention in step 7, and say so plainly in the file's own intro paragraph.
- Read the whole relevant passage before drafting a single Phi sentence. Note every specific image, proper noun, time reference, and tonal cue, not just the plot beats.

## 2. Thoroughly consult the current vocabulary. Make no assumptions.

This is the step most likely to be rushed, and rushing it is what caused the near-miss above.

- Search the JSON entries under `vocabulary/content/`, `vocabulary/function/`, and `vocabulary/interjection/` for each concept a sentence needs, checking the `gloss`, `description`, and `concept` fields. Each entry file is one JSON object rather than a list; a script expecting `entries` or `words` wrapper keys will silently return nothing. Sanity-check any script-based search with a direct `grep` for the plain English word before trusting a negative result.
- Search generously: synonyms, related concepts, and a word's opposite (Phi sometimes carves a concept as the negation or opposite of an existing word rather than coining it fresh).
- Read the full `description` fields of near-hits, not just their glosses. A word's definition often bundles exactly the act a sentence needs: `pholeni` (depart) carries "the farewell spoken" in its own entry, so an amicable good-night already has its verb.
- Check whether a word already at work elsewhere in the text or corpus carries a second image that extends here: `lumae` (end) names the sun's end (`sileta lumae`, west) and equally the discussion's end (`shareo lumae`, "finished by"). A word spent on one image is not used up; its other senses stay available, and reusing one weaves the text tighter.
- Check `documents/reference/compounds.md` before concluding an act or quality has no word: the compound registry already holds many of them (`thiku nila`, small-see, contempt; `korua thero`, heart-fire, anger).
- Check `documents/grammar/*.md` and `documents/reference/taught_patterns.md` for constructions, not just single words: manner descriptors before the verb (P24), stacked adjectives before a noun (P05), possessor-first event-noun chains (P06), date-line time fragments (P25), the optative `su`, the counterfactual `lu he`, the clause-relators (`lao`, `pheo`, `phoe`, `shai`), embedded content questions (a gap-word like `hina`, `sua`, `kua` standing where the answer goes, no `wela`/`welo` needed, manual ch19 "Embedded content questions"). A missing single word is often not a real gap once the right construction is found.
- A search returning no hits is not evidence a word doesn't exist. Verify the search itself before concluding anything.

## 3. Check, then coin or compose as necessary

Only after step 2 has confirmed a real gap:

- **Compose** when the concept builds cleanly from existing words: noun-noun compounds, adjective plus noun, possessor chains. Precedent: `suro repha` (rope-bridge), `korua thero` (heart-fire, anger), `mawha miona kulo` (no one guides, for a political label canon refuses to grant).
- **Register what the text canonizes.** When a composition becomes a stable idiom rather than a one-off phrase (it recurs, or the text's notes present it as the language's way of saying the thing), add its row to `documents/reference/compounds.md` in the same PR and regenerate (step 9); the registry feeds the Part VII compound reference and the explorer, so an unregistered idiom is invisible to every other speaker. A free descriptive phrase used once earns no row.
- **Coin without hesitation** when composition would be strained, or when the concept recurs across the text. Vocabulary growth is a stated goal of these transmutations, not a cost to minimize. Run the full Word Creation Protocol from `CLAUDE.md`: conceptual analysis, sound selection matching the concept's feeling, the collision check (`python3 scripts/validate_examples.py neighbors <candidate>`), the hiatus check, pillar alignment, and a semantic-family check.
- Do not default to dropping or generalizing a detail just because coining takes more steps than compression. Ask whether the detail recurs, connects to a pillar, or carries real weight in the scene; if any of those hold, it earns a word rather than a shrug.
- **Named species get a middle test, not an automatic coin.** A tree, plant, or animal named in the source earns a coined word when the species recurs in the text or corpus, carries an image the scene turns on, or belongs to the daily round a speaker community would name. A species mentioned once, inside a list, doing texture rather than image-work, is generalized (`whalo shiro`, great trees) or composed descriptively instead. The elm passes this test (a recurring, dwelt-on image); a passing botanical mention does not. When coining a species whose common name differs across English dialects, gloss it by the name most widely known.

## 4. Be as detailed as possible against the source

- Read every sentence of the source against the lexicon now that it has been searched properly. A dense, richly modified source sentence should not automatically collapse into one thin Phi clause; check whether Phi's own grammar, stacked adjectives, manner descriptors, possessor chains, embedded clauses, PP adjuncts, temporal fragments, can carry more of it, and whether it should become two or three Phi sentences instead of one.
- When a source sentence describes two distinct actions (a parting and a journey, a greeting and a departure, a feeling and a subsequent act), give each its own clause and its own verb rather than merging them into one, even when a single dense sentence would be grammatical. Before attaching a manner word to a verb, confirm that verb is the actual action the manner describes, not just the nearest verb in the same sentence: travel has no temperature, so an amicable good-night does not make an amicable journey.
- Do not silently drop: settings and place names, time references (a specific hour, "one night," "the day after"), pace and tone words (brisk, vigorous, warm, loud), or any image connected to a Phi pillar (nature, craft, transformation, the gift economy).
- Reserve real dropping for what is genuinely disconnected from Phi: an untranslatable pun, a one-off engineering detail with no thematic weight, a real specific place name with no reusable value.
- Not every source needs to get denser. A spare or aphoristic original (a sutra's negations, a legal article's plain declarations) deserves a spare Phi rendering; compressing an already-terse source is not the same failure as compressing ornate Victorian prose. The rule is "check thoroughly and do not drop content by default," not "make every text longer." Expect the outcome to differ by genre; do not expect the process to.

## 5. Check the particle system, not just the words

Steps 2 through 4 catch a missing word and a dropped image. They do not catch a sentence that names every image correctly and still leaves Phi's grammar idle: no evidential stance, no modal hedge, no discourse connective, a string of bare declaratives where the English carried real nuance. A vocabulary search cannot find this failure, because nothing is missing from the lexicon; the words that exist are simply not being asked to do their job.

Run this checklist against every sentence, not once for the whole passage. Full inventory: `documents/grammar/particle_reference.md`.

- **Modality** (`po` possibility/ability, `na` necessity/obligation, Slot 1): "can," "could," "might," "must," "would," "have to," "insist on," "scarce," "barely" in the English are all modal tells. `po` on a future verb turns a bare prediction into an offered possibility (manual ch15 §3, "Speculation"): "what would happen" is `hina so po kelu`, not a flat future. Mark them; do not let a capacity, an obligation, or a hedge collapse into a bare assertion.
- **Evidentiality** (`hi` witnessed, `ke` inferred, `ti` reported, `ho` assumed, Slot 1): a whole passage framed as secondhand can open with one `ti` and let it carry the frame, but check every clause inside for its own stance too. "It struck him," "he felt," "she knew" are direct-experience clauses even inside a reported frame; the frame's outer evidential does not automatically cover them.
- **Discourse adverbs** (`thelao` therefore, `whekai` however, `sheno` furthermore, `phisu` for example; stand after any Slot 0 particle, before the subject): does this sentence turn against, follow from, add to, or illustrate the one before it? "But," "however," "at last," "so," "also," "for instance" are the English tells.
- **Focus, restriction, addition** (`ko` focus, `li` only/restrictive, `we` also/too, Slot 2): does the English isolate one element ("only," "just"), stress one thing specifically, or add to something already named ("also," "too," "even")?
- **Intensity and comparison** (`ru` very/truly, `mo` more, `mo ko` most, Slot 2): "very," "so," and any comparative or superlative form.
- **Mood** (Slot 0: `wa` question, `no` imperative, `lu`/`lu he` real/unreal conditional, `su` wish, `pi` politeness): check whether a sentence carrying a question, command, wish, or conditional in the English got flattened into a plain declarative in a first pass.

An unmarked assertion is a legitimate claim in Phi, not a gap, so a particle that stays unused after this check is a real choice. A particle that was never considered is not the same thing. Note in the block's Notes what was checked and set aside, the same way a coining decision gets explained, not only what was used.

## 6. Read each sentence back in grammar order

Steps 2 through 5 decide what each sentence says. This step checks how it stands. English habit is strong enough to survive a thorough vocabulary search: the words come out right and the order comes out English. Read every drafted sentence back against this list, one clause at a time, before it goes near a file.

- **SOV, with adjuncts between subject and object**: S PP O V, circumstances announced before the thing acted on (canon's adjunct-order bullet).
- **Every preposition precedes its object**, always: `mua shalimo`, never `shalimo mua`. Nested relators are legal in that same order (`wei leo waero`, to the sky above). The one licensed surface exception is the oblique relative, where the object is gapped and the preposition stands directly before the verb phrase (`rena mia mua to thalo shelira`).
- **The Slot 1 cluster attaches to the verb**, in canon order (Tense > Aspect > Voice > Evidentiality > Modality > Negation): `to ro nai`, `to si nai`, `to ki ka kelu`. No aspect particle floats earlier in the sentence; if a particle is not immediately in front of the verb with its cluster, it is in the wrong place.
- **Manner runs [Slot 1][descriptor][verb]** (`to ru noeli pholeni`), and a predicate stands before the Slot 1 cluster and `nai` (`shero mioru to nai`).
- **Discourse adverbs stand after any Slot 0 particle, before the subject**; possessors precede the possessed; quantifiers and numerals precede their nouns; a `rena` clause precedes its head.

The validator now nets the mechanically detectable slice of this (a preposition followed by a Slot 1 particle, or standing sentence-final), but the net is deliberately narrow: a postposed relator followed by a plain noun reads the same as a well-formed phrase, so this read-back is the real check, every sentence, every time.

## 7. Structure the text

For public-domain sources, every example block is four lines inside a fenced code block:

```
<Phi sentence>
<word-by-word gloss, exact lexicon glosses, parenthetical disambiguators dropped>
(<natural English back-translation>)
source: "<the specific clause or sentence of the original this line transmutes>"
```

For still-copyrighted sources, drop the fourth line and say so in the intro.

**The excerpt must represent the transmutation, not the neighborhood it came from.** Cite exactly the clause the Phi sentence translates, no more. Two units never share the same citation, even when they split one English sentence between them, and citations never overlap: if one unit's citation ends mid-sentence, the next unit's citation picks up exactly where it left off, not a few words earlier. Before finalizing a block, reread each citation next to only its own Phi line and ask whether the citation promises anything the Phi sentence does not actually say (a verb of motion the sentence lacks, an image a neighboring unit carries instead); an inflated or borrowed citation makes a complete translation look like a compressed one, and a shared or truncated-with-ellipsis citation is close to always a sign that the original sentence should have been split at its own clause boundary instead.

**The back-translation must say exactly what the Phi word says, neither less nor more.** A word chosen or coined specifically for its intensity (`kapura` over `haolu`, `wipha` over a plain "sad") has that intensity written into its own lexicon entry; read that entry before writing the parenthetical English line, and let the back-translation show what the word actually means, not just its one-line gloss. "He shouted" is a defensible gloss of `kapura` and still a bad back-translation, because the word was chosen to carry "roaring out very loud" and the English fell short of it. But do not overcorrect: a generic verb like `haolu` (speak) never earns a back-translation borrowed from a stronger English word ("damned," "declared," "condemned") just because the source sentence is forceful. If the Phi genuinely falls short of the source, that is a real gap to close with a better composition or a new word (steps 2 and 3), not something to paper over in the English gloss. Check every back-translation in a block against the lexicon entry of its own Phi words, the same way citations get checked against their Phi lines: does the English carry exactly as much force, specificity, or feeling as those words actually define, no more and no less.

Each block gets a **Notes:** paragraph explaining the choices in it: what was coined and why, what was composed and why, what canon refuses and how the text describes it instead. The file closes with a **Gap log**: a flat catalog, concept, then the Phi solution, then the reasoning, covering every coinage and composition.

## 8. State the transmutation, don't narrate the drafting

Notes and gap logs state the transmutation's current reasoning. They are never a chronicle of the editing process. Do not write "the first draft dropped X," "a second pass caught Y," "this now returns as," or "was missing until." If a choice corrects an earlier design decision, state what the current choice is and why, not what changed to get there. This is the same standard the project holds PR bodies to: a statement about the thing, not a history of what happened to it.

## 9. Validate, humanize, ship

- Run `python3 scripts/validate_examples.py` standalone before every commit touching the file. Zero errors, zero warnings is the bar.
- Reread every citation in the block against only its own Phi line (see the check in step 7); the validator does not catch a shared, overlapping, or inflated citation, so this is a manual pass every time, not a one-off fix for whichever unit prompted it.
- Reread every back-translation against the lexicon entry of its own Phi words, not just its citation (see the check in step 7); a back-translation can be a technically correct gloss and still flatten a word chosen for its intensity, or claim a stronger meaning than a plain word actually has, and the validator has no way to catch either direction.
- Reread every sentence in grammar order (step 6); the validator's postposed-preposition net is narrow by design and the Slot 1 check only sees adjacent runs, so neither replaces the read-back.
- Before coining, run `python3 scripts/validate_examples.py neighbors <candidate>`.
- If any vocabulary JSON or `documents/reference/compounds.md` changed, regenerate: `python3 scripts/generate_reference.py` and `python3 scripts/build_site.py`.
- Invoke the actual humanizer skill (the tool call, not a hand-applied summary of its pattern list) on any new or changed prose, intro, notes, gap log, before committing. Never touch the Phi example blocks, gloss lines, or source-quote lines.
- Work on a branch, open a PR, flag judgment calls explicitly in the body, and wait for merge before cleaning up.

## Worked example

Source (public domain, William Morris, *News from Nowhere*, 1890): a single sentence naming a place, a pace, a transformation, and a rising energy among the speakers.

First draft, after step 2 was skipped: one Phi sentence carrying only the reportative frame, with everything else compressed away. Nothing wrong grammatically; everything else simply missing.

After running steps 2 through 4 properly: four Phi sentences. The meeting's place and pace, `mua lona ta shero reshi shareo to nai.` The transformation it turned on, `punoa moluki wireo philo.` The friends' energy and its topic, `lo melu wireo punoa ki therua haolu.` Every word in all three, `lona`, `reshi`, `moluki`, `therua`, `shero`, `wireo`, `philo`, was already in the lexicon before the first draft was written. Nothing was coined to fix it. The fix was reading the dictionary properly the first time.

Step 5 catches a different kind of gap in the same chapter. `shareo noeli to manolu. ta miona korua thero ki kapura.` (the discussion stayed warm and good-natured; one grew angry and roared) stands as two adjacent declaratives with no connector between them, though the English marks the turn plainly: "at last." `whekai` (however), opening the second sentence, carries the turn the two bare declaratives left silent. The image was never missing; the grammar carrying its turn was.

A fresh run of the whole opening sentence ("as to what would happen on the Morrow of the Revolution") turned up a case where an entire clause, not just a connector, had gone missing: the shipped text kept the date (`punoa moluki wireo philo`) and dropped the question anchored to it. "Would" is a modality tell; following it to `po`'s speculation usage led to the embedded-content-question construction (a gap-word needs no complementizer), and composing the two gave `punoa moluki wireo philo hina so po kelu.` (on the morrow of society's transformation, what might happen), no coining required. Steps 1 through 4 had already passed this sentence; nothing was flagged as missing because nothing was missing from the lexicon, only from the grammar actually asked to carry the sentence's own uncertainty.
