---
name: transmute
version: 1.0.0
description: |
  Transmute a source text into Phi: survey the source and the lexicon
  thoroughly before drafting, favor coining or composing over
  compressing away imagery, and structure the result as validated
  example blocks with a gap log. Use for any new or revised file on
  the texts shelf (pamphlets/*.md rendered to web/texts/), whether a
  whole chapter or a single-line correction.
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

## The three failures this skill guards against

1. **Compressing instead of checking.** An elm became generic `shiro` (tree). A crowded, stinking carriage became a bare "sad heart." A discussion's brisk pace and the Revolution it turned on were dropped entirely. In every case the missing word or construction was already in the lexicon; it had just never been searched for properly.
2. **Trusting a negative search result.** A vocabulary-search script that expected each `vocabulary/**/*.json` file to be a list with an `entries` or `words` key silently returned zero hits for every single query, because each file is actually one JSON object. This nearly produced a false report that Phi lacked words for "brisk," "meeting," "revolution," and "vigorous." All four already existed.
3. **Checking the words and not the grammar.** Every image in News from Nowhere ch. 1 survived steps 1 through 4, and the chapter still under-used Phi's own particle system: modality (`po`, `na`) never appears once in the whole chapter, evidentiality is marked exactly once (`ti`, opening the frame) though the chapter is one long narrated account, discourse adverbs are marked once (`thelao`) though the discussion turns sharply from good-tempered to a shout, and focus (`ko`) and restriction (`li`) never appear at all. None of this was a considered choice; nothing had prompted a check for it.

Everything below is built to catch these three failures before they reach a file.

## 1. Survey the source

- Check the source's copyright status before doing anything else. Public domain: author died more than 70 years ago, or first published before roughly 1930 in the US (verify the exact cutoff year at the time of writing, it moves annually). If public domain, fetch the real text via `WebFetch` rather than working from memory or a half-remembered plot summary; memory of a text is frequently wrong in specific, plot-relevant ways.
- If the source is still under active copyright, do not quote it at length. Work from short, sparing excerpts only, skip the source-quote-line convention in step 6, and say so plainly in the file's own intro paragraph.
- Read the whole relevant passage before drafting a single Phi sentence. Note every specific image, proper noun, time reference, and tonal cue, not just the plot beats.

## 2. Thoroughly consult the current vocabulary. Make no assumptions.

This is the step most likely to be rushed, and rushing it is what caused the near-miss above.

- Search across every file in `vocabulary/**/*.json` for each concept a sentence needs, checking the `gloss`, `description`, and `concept` fields. Each file is a single JSON object, not a list: a script expecting `entries` or `words` wrapper keys will silently return nothing. Sanity-check any script-based search with a direct `grep` for the plain English word before trusting a negative result.
- Search generously: synonyms, related concepts, and a word's opposite (Phi sometimes carves a concept as the negation or opposite of an existing word rather than coining it fresh).
- Check `documents/grammar/*.md` and `documents/taught_patterns.md` for constructions, not just single words: manner descriptors before the verb (P24), stacked adjectives before a noun (P05), possessor-first event-noun chains (P06), date-line time fragments (P25), the optative `su`, the counterfactual `lu he`, the clause-relators (`lao`, `pheo`, `phoe`, `shai`). A missing single word is often not a real gap once the right construction is found.
- A search returning no hits is not evidence a word doesn't exist. Verify the search itself before concluding anything.

## 3. Check, then coin or compose as necessary

Only after step 2 has confirmed a real gap:

- **Compose** when the concept builds cleanly from existing words: noun-noun compounds, adjective plus noun, possessor chains. Precedent: `suro repha` (rope-bridge), `korua thero` (heart-fire, anger), `mawha miona kulo` (no one guides, for a political label canon refuses to grant).
- **Coin without hesitation** when composition would be strained, or when the concept recurs across the text. Vocabulary growth is a stated goal of these transmutations, not a cost to minimize. Run the full Word Creation Protocol from `CLAUDE.md`: conceptual analysis, sound selection matching the concept's feeling, the collision check (`python3 scripts/validate_examples.py neighbors <candidate>`), the hiatus check, pillar alignment, and a semantic-family check.
- Do not default to dropping or generalizing a detail just because coining takes more steps than compression. Ask whether the detail recurs, connects to a pillar, or carries real weight in the scene; if any of those hold, it earns a word rather than a shrug.

## 4. Be as detailed as possible against the source

- Read every sentence of the source against the lexicon now that it has been searched properly. A dense, richly modified source sentence should not automatically collapse into one thin Phi clause; check whether Phi's own grammar, stacked adjectives, manner descriptors, possessor chains, embedded clauses, PP adjuncts, temporal fragments, can carry more of it, and whether it should become two or three Phi sentences instead of one.
- Do not silently drop: settings and place names, time references (a specific hour, "one night," "the day after"), pace and tone words (brisk, vigorous, warm, loud), or any image connected to a Phi pillar (nature, craft, transformation, the gift economy).
- Reserve real dropping for what is genuinely disconnected from Phi: an untranslatable pun, a one-off engineering detail with no thematic weight, a real specific place name with no reusable value.
- Not every source needs to get denser. A spare or aphoristic original (a sutra's negations, a legal article's plain declarations) deserves a spare Phi rendering; compressing an already-terse source is not the same failure as compressing ornate Victorian prose. The rule is "check thoroughly and do not drop content by default," not "make every text longer." Expect the outcome to differ by genre; do not expect the process to.

## 5. Check the particle system, not just the words

Steps 2 through 4 catch a missing word and a dropped image. They do not catch a sentence that names every image correctly and still leaves Phi's grammar idle: no evidential stance, no modal hedge, no discourse connective, a string of bare declaratives where the English carried real nuance. A vocabulary search cannot find this failure, because nothing is missing from the lexicon; the words that exist are simply not being asked to do their job.

Run this checklist against every sentence, not once for the whole passage. Full inventory: `documents/grammar/particle_reference.md`.

- **Modality** (`po` possibility/ability, `na` necessity/obligation, Slot 1): "can," "could," "might," "must," "have to," "insist on," "scarce," "barely" in the English are all modal tells. Mark them; do not let a capacity or an obligation collapse into a bare assertion.
- **Evidentiality** (`hi` witnessed, `ke` inferred, `ti` reported, `ho` assumed, Slot 1): a whole passage framed as secondhand can open with one `ti` and let it carry the frame, but check every clause inside for its own stance too. "It struck him," "he felt," "she knew" are direct-experience clauses even inside a reported frame; the frame's outer evidential does not automatically cover them.
- **Discourse adverbs** (`thelao` therefore, `whekai` however, `sheno` furthermore, `phisu` for example; stand after any Slot 0 particle, before the subject): does this sentence turn against, follow from, add to, or illustrate the one before it? "But," "however," "at last," "so," "also," "for instance" are the English tells.
- **Focus, restriction, addition** (`ko` focus, `li` only/restrictive, `we` also/too, Slot 2): does the English isolate one element ("only," "just"), stress one thing specifically, or add to something already named ("also," "too," "even")?
- **Intensity and comparison** (`ru` very/truly, `mo` more, `mo ko` most, Slot 2): "very," "so," and any comparative or superlative form.
- **Mood** (Slot 0: `wa` question, `no` imperative, `lu`/`lu he` real/unreal conditional, `su` wish, `pi` politeness): check whether a sentence carrying a question, command, wish, or conditional in the English got flattened into a plain declarative in a first pass.

An unmarked assertion is a legitimate claim in Phi, not a gap, so a particle that stays unused after this check is a real choice. A particle that was never considered is not the same thing. Note in the block's Notes what was checked and set aside, the same way a coining decision gets explained, not only what was used.

## 6. Structure the text

For public-domain sources, every example block is four lines inside a fenced code block:

```
<Phi sentence>
<word-by-word gloss, exact lexicon glosses, parenthetical disambiguators dropped>
(<natural English back-translation>)
source: "<the specific clause or sentence of the original this line transmutes>"
```

For still-copyrighted sources, drop the fourth line and say so in the intro.

Each block gets a **Notes:** paragraph explaining the choices in it: what was coined and why, what was composed and why, what canon refuses and how the text describes it instead. The file closes with a **Gap log**: a flat catalog, concept, then the Phi solution, then the reasoning, covering every coinage and composition.

## 7. State the transmutation, don't narrate the drafting

Notes and gap logs state the transmutation's current reasoning. They are never a chronicle of the editing process. Do not write "the first draft dropped X," "a second pass caught Y," "this now returns as," or "was missing until." If a choice corrects an earlier design decision, state what the current choice is and why, not what changed to get there. This is the same standard the project holds PR bodies to: a statement about the thing, not a history of what happened to it.

## 8. Validate, humanize, ship

- Run `python3 scripts/validate_examples.py` standalone before every commit touching the file. Zero errors, zero warnings is the bar.
- Before coining, run `python3 scripts/validate_examples.py neighbors <candidate>`.
- If any vocabulary JSON changed, regenerate: `python3 scripts/generate_reference.py` and `python3 scripts/build_explorer.py`.
- Invoke the actual humanizer skill (the tool call, not a hand-applied summary of its pattern list) on any new or changed prose, intro, notes, gap log, before committing. Never touch the Phi example blocks, gloss lines, or source-quote lines.
- Work on a branch, open a PR, flag judgment calls explicitly in the body, and wait for merge before cleaning up.

## Worked example

Source (public domain, William Morris, *News from Nowhere*, 1890): a single sentence naming a place, a pace, a transformation, and a rising energy among the speakers.

First draft, after step 2 was skipped: one Phi sentence carrying only the reportative frame, with everything else compressed away. Nothing wrong grammatically; everything else simply missing.

After running steps 2 through 4 properly: four Phi sentences. The meeting's place and pace, `lona mua ta shero reshi shareo to nai.` The transformation it turned on, `punoa moreluki wireo philo.` The friends' energy and its topic, `lo melu wireo punoa ki therua haolu.` Every word in all three, `lona`, `reshi`, `moreluki`, `therua`, `shero`, `wireo`, `philo`, was already in the lexicon before the first draft was written. Nothing was coined to fix it. The fix was reading the dictionary properly the first time.

Step 5 catches a different kind of gap in the same chapter. `shareo noeli to manolu. ta miona korua thero ki kapura.` (the discussion stayed warm and good-natured; one grew angry and roared) stands as two adjacent declaratives with no connector between them, though the English marks the turn plainly: "at last." `whekai` (however), opening the second sentence, carries the turn the two bare declaratives left silent. The image was never missing; the grammar carrying its turn was.
