# The transmutation process

Transmutation looks like inspiration from the outside, but it is a craft with steps. Here is the process, distilled from the texts that have been transmuted so far.

## Step 1: Sit with the idea

Before touching the dictionary, ask what the sentence is actually *doing*. Not its words — its work. "The aesthetics of solarpunk merge the practical with the beautiful" is doing this work: it claims that two qualities people usually separate belong together. That claim is what must survive. The vocabulary of the original ("aesthetics," "merge") is scaffolding, and scaffolding does not ship.

This step is where mindfulness earns its place in the method. A sentence read hastily gets translated; a sentence sat with gets transmuted.

## Step 2: Find the Phi concepts

Now open the lexicon — but search by *meaning*, not by dictionary headword. Three places to look, in order:

1. **A single word.** Phi's holistic vocabulary often covers with one word what English needs a phrase for: `womu` (house+belonging), `henoi` (enough, as a knowable thing), `thowia` (born — one becomes two).
2. **The compound registry** (`documents/COMPOUNDS.md`). Canonized idioms like `korua thero` (heart-fire: anger) and `remo kire` (thought-shape: a fixed view) are stable parts of the language. Use them before inventing.
3. **A new composition.** If neither exists, compose transparently from existing words — the way `nulae nophi` (sleep-story) makes "dream." If your composition is good, it may deserve a place in the registry.

Only when all three fail is a genuinely new word indicated — and that is a separate, deliberate act (see the Word Creation Protocol), never something done casually in the middle of a text.

## Step 3: Restructure

Phi's shape is not English's shape. As you rebuild:

- **Break complex sentences into parallel simple ones.** Phi prefers a rhythm of short, complete statements over subordinated cascades. One idea per sentence, a period after each — Phi uses no commas.
- **Let the order announce.** Modifier before modified, context before action, clause openers paired with their closers. The sentence should unfold with no surprises at the end except the verb it promised.
- **Use the grammar's own instruments.** The optative `su` does the work of "may…" and "let…". Evidentials mark where knowledge comes from. Headless relatives (`rena … nai`) name whole categories without category nouns.

## Step 4: Check the philosophy

Read the draft against the Five Pillars. Does it quantify what should stay qualitative? Does it accuse where it could observe? Does it borrow a hierarchy the language refuses? The grammar will usually have blocked these already — that is what it is for — but the check is part of the practice.

Where the language *resists* the original — a statistic that will not survive the ternary numbers, a blame the passive declines to assign — pause. The resistance is information. Sometimes the right response is to drop the content (the second case study drops a dollar figure without loss). Sometimes it is to discover what the original was really saying beneath its habits.

## Step 5: Validate

Every Phi word in your text must exist in the lexicon with the meaning you are using. Check the words you are least sure of with the lexicon tools, and if the text will live in the repository, run the validator:

```bash
python3 scripts/validate_examples.py
```

The Metta Sutta transmutation shipped with zero unknown words. Yours should too. A transmutation that uses words the language does not have is not a transmutation — it is a wish.

## The process in one breath

Sit with the idea. Find its Phi concepts — word, compound, or composition. Rebuild in Phi's shape. Listen where the language resists. Verify every word. What remains is the idea, thought in Phi.
