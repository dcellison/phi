# Phi semantic domains

Semantic domains make the content lexicon browsable by subject. Each content entry belongs to at least one domain and may belong to several. The field is an object rather than a list because each domain needs a brief reason for this particular word's inclusion.

## Domain catalogue

| Identifier | Use it for |
|---|---|
| `nature` | Organisms, ecosystems, weather, land, water, and ecological relations. |
| `community` | Kinship, social relations, collective life, institutions, and mutual support. |
| `wisdom` | Understanding gained through experience, reflection, learning, or careful judgement. |
| `creation` | Making, building, art, craft, and the transformation of materials. |
| `dialogue` | Speaking, listening, expression, interpretation, and communicative relations. |
| `temporal` | Time, sequence, duration, cycles, and change. |
| `aesthetic` | Beauty, harmony, style, sensory appreciation, and artistic response. |
| `emotion` | Feelings, moods, affective responses, and emotional relations. |
| `physical` | Bodies, sensations, tangible objects, substances, and material qualities. |
| `ritual` | Ceremonies, observances, traditions, and repeated acts that mark shared meaning. |
| `cognition` | Thinking, attention, memory, inference, perception, and other mental processes. |
| `spatial` | Place, position, direction, distance, and movement through space. |
| `activity` | Actions and practices, especially the ordinary work of human life. |

The neighbouring domains are meant to overlap. `wisdom` concerns what a person has come to understand; `cognition` concerns what the mind is doing. `creation` gathers acts that make or transform something, while `activity` also covers walking, waiting, eating, and other acts with no product at the end. A plant may belong to both `nature` and `physical` because it is part of an ecosystem and a tangible living thing.

## Entry form

The keys are the identifiers above. Their values explain why a speaker browsing that domain would reasonably expect to find the word there.

```json
"semantic_domains": {
  "creation": "Life-giving precipitation",
  "nature": "Atmospheric water cycle"
}
```

This is the domain mapping for `pheralu` (rain). The rationales can be short when the relation is plain. They still need to say more than "related to nature" or another sentence that could be pasted into almost any entry.

## Choosing domains

Choose every domain that provides a genuine route to the word, but do not add one merely because a remote association can be invented. A cook looking under `physical` should find heat and texture; the same search should not return every abstract word that can be discussed while standing in a kitchen.

Semantic domains organise retrieval. Pillars record a philosophical relation and answer a different question. A word may sit in the `community` domain because it concerns a public institution, while its pillar rationales explain the particular values at stake in that institution.
