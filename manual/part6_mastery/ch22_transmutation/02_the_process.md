# The transmutation process

Transmutation looks like inspiration from the outside, but it is a craft with steps. Here is the process, distilled from the texts that have been transmuted so far.

## Step 1: Sit with the idea

Before touching the dictionary, ask what the sentence is actually *doing*. Not its words: its work. "The aesthetics of solarpunk merge the practical with the beautiful" is doing this work: it claims that two qualities people usually separate belong together. That claim is what must survive. The vocabulary of the original ("aesthetics," "merge") is scaffolding, and scaffolding does not ship.

This step is where the methods separate. A translator asks which details make the source's claim exact. A transmuter decides which underlying work to carry and which source details may change. Both decisions require patience.

## Step 2: Find the Phi concepts

Now open the lexicon, but search by *meaning*, not by dictionary headword. Three places to look, in order:

1. **A single word.** Phi's holistic vocabulary often covers with one word what English needs a phrase for: `womu` (house+belonging), `henoi` (enough, as a knowable thing), `thowia` (born, one becomes two).
2. **The compound registry** (`documents/reference/compounds.md`). Canonized idioms like `korua thero` (heart-fire: anger) and `remo kire` (thought-shape: a fixed view) are stable parts of the language. Use them before inventing.
3. **A new composition.** If neither exists, compose transparently from existing words, the way `nulae nophi` (sleep-story) makes "dream." If your composition is good, it may deserve a place in the registry.

Once those places have been checked, choose honestly between composition and coinage. A transmutation also has the option to reframe, which its gap log records. Coinage follows the Word Creation Protocol and is settled before the passage is finished rather than improvised inside a sentence.

## Step 3: Restructure

Phi's shape is not English's shape. As you rebuild:

- **Break complex sentences into parallel simple ones.** Phi prefers a rhythm of short, complete statements over subordinated cascades. One idea per sentence, a period after each: Phi uses no commas.
- **Let the order announce.** Modifier before modified, context before action, clause openers paired with their closers. The sentence should unfold with no surprises at the end except the verb it promised.
- **Use the grammar's own instruments.** The optative `su` does the work of "may…" and "let…". Evidentials mark where knowledge comes from. Headless relatives (`rena … nai`) name whole categories without category nouns.

## Step 4: Check the philosophy

Read the draft against the Five Pillars. Does it quantify what should stay qualitative? Does it accuse where it could observe? Does it borrow a hierarchy the language refuses? The grammar will usually have blocked these already (that is what it is for), but the check is part of the practice.

Where the language *resists* the original (an exact statistic that needs a source record, a blame the passive declines to assign), pause. The resistance is information, not permission to erase relevant content. Sometimes a Phi summary can omit a detail while the source record preserves it; sometimes the detail is essential and must remain beside the passage. Sometimes the resistance reveals what the original was doing beneath its habits.

## Step 5: Validate

Every Phi word in your text must exist in the lexicon with the meaning you are using. Check the words you are least sure of with the lexicon tools, and if the text will live in the repository, run the validator:

```bash
python3 scripts/validate_examples.py
```

The Metta Sutta translation contains no unknown forms. A transmutation has the same obligation: every Phi word in it must exist. Otherwise the passage is a wish for vocabulary, not a finished text.

## The five moves

Inside steps 2 through 4, the same five moves recur: the repertoire the shelf's texts were built with. The Tao Te Ching text (`texts/tao_te_ching.md`) names them inline as a worked guide; here is the repertoire itself, each move with the shelf's clearest demonstrations.

**The refusal.** When Phi cannot rebuild a line directly, ask what the line's virtue or mechanism looks like in Phi's own economy. *Contend* became takes-nothing and *leader* became the one-who-guides (Tao Te Ching); *master* became the separate acts of coercion and exploitation (Schleicher's fable); the Ring Verse's refusal became its text. If the source wording itself matters, preserve it outside the Phi passage rather than presenting transmutation as quotation.

**The reframe.** Replace the source's imagery with imagery Phi already owns, at the same depth. The archer, bow, and arrows became the wind, the tree, and living seeds (The Prophet); the felled tree became the tree in the great wind (Tao Te Ching); the scattering of Babel became a sowing (the Babel text).

**The carve.** When several Phi words cover one English word, the lexicon's carve notes decide: that is what they are for. The Tao is `keiro`, not `ruela`, because the carve separates the guiding way from the walked ground; calm, peaceful, and tranquil each have their own territory.

**The grammar-led choice.** Let a ruling shape the sentence, and trust the push. *Belong* must go through `phelu` (The Prophet: the possession ruling made the verse truer); *Real* turned out to be the habitual `ro` (The Velveteen Rabbit); *useful* became the possibility particle `po` (Tao Te Ching: emptiness opens rather than adds).

**Composition.** Build the missing abstraction from the rules instead of coining: quality-nouns make the soft and the hard, event-nouns make life and death, `mu thena` counts honest emptiness (Tao Te Ching); a dream was always a sleep-story.

Coinage is one of the tools, not a penalty for exhausting the others. When a concept deserves its own root, leave the draft, follow the Word Creation Protocol, and return with a valid word. A shelf text may reach the end without a coin; that is evidence that composition did the work, not a target every text must meet.

## The process in one breath

Sit with the idea. Find its Phi concepts: word, compound, or composition. Rebuild in Phi's shape. Listen where the language resists. Verify every word. What remains is the idea, thought in Phi.
