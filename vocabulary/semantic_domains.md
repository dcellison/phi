# Phi semantic domains

Semantic domains make the content lexicon browsable by subject. Each content entry belongs to at least one domain and may belong to several. The field is an object rather than a list because every assignment has to explain why this word belongs on that shelf.

## Domain catalogue

| Identifier | Use it for |
|---|---|
| `nature` | Organisms, ecosystems, weather, land, water, and ecological relations. |
| `physical` | Bodies, sensations, tangible objects, substances, and material qualities. |
| `spatial` | Place, position, direction, distance, and movement through space. |
| `temporal` | Time, sequence, duration, cycles, and change through time. |
| `quantity` | Numerals, counting, amounts, proportions, dimensions, and measurement. |
| `activity` | Actions and practices, including ordinary work with no produced object. |
| `creation` | Making, building, art, craft, and the transformation of materials. |
| `cognition` | Thinking, attention, memory, inference, perception, and other mental processes. |
| `wisdom` | Reflective or practical understanding and judgement shaped by experience or learning. |
| `emotion` | Feelings, moods, affective responses, and emotional relations. |
| `communication` | Speaking, listening, writing, signing, expression, interpretation, and communicative records. |
| `community` | Kinship and social relations, including collective life, institutions, power, conflict, and mutual support. |
| `ethics` | Harm, care, fairness, consent, honesty, responsibility, and judgements about conduct or relationships. |
| `aesthetic` | Beauty, harmony, style, sensory appreciation, and artistic response. |
| `ritual` | Ceremonies, observances, traditions, and repeated acts that mark shared meaning. |

The neighbouring domains overlap, but they do different work. `cognition` concerns what a mind is doing, while `wisdom` concerns understanding or judgement that has grown through reflection, learning, or experience. `ethics` gathers questions of conduct and effect, so a moral judgement no longer needs to borrow `wisdom` merely because it was made carefully.

`activity` includes acts such as walking, waiting, and eating. `creation` is narrower: something is made, built, repaired, or materially transformed. `quantity` contains numbers and directly measurable magnitudes; it does not collect every adjective that happens to admit a degree.

`nature` concerns the living and environmental world, while `physical` concerns bodies, matter, sensation, and material qualities. A plant may belong to both. A colour does not enter `nature` merely because a flower provides a convenient example.

`communication` covers the means and acts by which expression passes between people. `community` covers the relationships and institutions in which people live together, including conflict and unequal power as well as mutual aid.

## Entry form

The keys are the identifiers above. Their values explain why a speaker browsing that domain would reasonably expect to find the word there.

```json
"semantic_domains": {
  "cognition": "attention deliberately directed towards sound",
  "communication": "attentive reception of another person's speech"
}
```

This is the domain mapping for `sheluo` (listen). The rationales are short because the relations are plain, but each one still belongs to this word. "Related to cognition" would explain nothing.

## Choosing domains

Choose a domain when it offers a genuine route to the word itself. An ordinary lexical sense qualifies, including an established extension recorded in the description or usage notes. A handy example or a philosophical consequence does not qualify. Neither does a setting in which the word could merely occur.

The useful test is retrieval. A speaker browsing `communication` should find `sheluo` (listen). The same speaker does not need every adjective that could describe a conversation. Likewise, `nature` should contain rain and soil, not every colour found outdoors.

Domains describe lexical range rather than approval. `community` therefore includes coercion and conflict alongside kinship and cooperation. `wisdom` is not a badge placed on any word Phi regards warmly.

Semantic domains organise retrieval. Pillars record direct philosophical relationships, and modules provide optional specialist learning paths. Those fields may meet in one entry, but none can substitute for another.
