# The manner placement study (2026-07-06)

The evidence behind the *Manner is a descriptor before the verb* ruling in `/canon.md`. Phi's content lexicon has never contained an adverb — yet the corpus modified verbs anyway, using ordinary descriptors in preverbal position, and it did so in two different orders relative to the Slot 1 block. No manual section taught the pattern; the two orders shipped in published texts. This study collected every attestation and the ruling picked one order.

## The attestations

| source | line | order | reading |
|---|---|---|---|
| complementizers pamphlet §5 | `sholo to shena haolu` | [Slot 1] [descriptor] [verb] | said calmly (manner) |
| complementizers pamphlet §3 | `to reshi wepu` | [Slot 1] [descriptor] [verb] | moved fast (manner) |
| Velveteen Rabbit | `thia ma phelora nila` | [Slot 1] [descriptor] [verb] | see you as unbeautiful (depictive) |
| Schleicher fable | `reshi to kolua` | [descriptor] [Slot 1] [verb] | carried swiftly (manner) |
| Velveteen Rabbit | `sheru to nila` | [descriptor] [Slot 1] [verb] | looked slowly (manner) |
| horse.json (entry example) | `kalora reshi rashelo` | no Slot 1 present | runs fast (manner) |

Three of five particle-bearing attestations already placed the descriptor inside the Slot 1 block.

## The ruling and why

**[Slot 1] [descriptor] [verb]** — the descriptor stands immediately before the verb, and the ranked particle block stands before the whole. Two grounds:

1. **The phrase-shape symmetry.** The noun phrase is function words, then descriptors, then the head (`ha phelora thepalu`, this beautiful garden). The winning order gives the verb phrase the identical shape (`to reshi kolua`, carried swiftly). One shape for both phrase types is the deeper consistency; the modifier-first principle is satisfied either way, so the symmetry decides.
2. **The corpus majority.** Three attestations to two, including the only depictive.

The two nonconforming lines (Schleicher fable, Velveteen Rabbit) were realigned in the same PR, gloss lines included. The entry example in horse.json carries no Slot 1 particle and conforms as written. Existing documentation needed no amendment: every description of Slot 1 says "before the verb", which remains true — the ruling only fixes what may stand between them.

Taught in manual ch12 §4 (Describing the action: manner); the ruling lives in `/canon.md`.
