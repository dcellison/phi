# Appendix: the complete inventory

Phi has thirty-five particles. They are one part of its grammar, gathered here by scope.

### Slot 0: utterance frame

| Particle | Gloss | Function |
|---|---|---|
| `wa` | Q | marks a yes/no question |
| `no` | IMP | marks a directive, interpreted in context as a request or command |
| `lu` | COND | marks a realis condition; the consequence follows as its own sentence |
| `he` | IRR | follows `lu` to make an irrealis or counterfactual condition |
| `su` | OPT | marks a wish, hope, blessing, or prayer |
| `pi` | POL | marks a polite stance |

The documented combined forms are `pi wa`, `pi no`, and `lu he`. Other multiple Slot 0 sequences are not licensed. `kona` is an extra-clausal vocative, not a particle.

### Slot 1: verb phrase

**Tense > Aspect > Voice > Evidentiality > Modality > Negation**

| Rank | Particle | Gloss | Function |
|---|---|---|---|
| tense | `to` | PST | past; present is unmarked |
| tense | `so` | FUT | future |
| aspect | `ki` | PFV | complete at the reference time |
| aspect | `si` | IPFV | ongoing or in progress |
| aspect | `pa` | INCH | beginning |
| aspect | `te` | CESS | ending |
| aspect | `ro` | HAB | recurring or characteristic pattern |
| voice | `se` | PASS | patient as subject, actor unstated |
| voice | `ka` | CAUS | causer added, original actor placed in the object sequence |
| evidentiality | `hi` | DIR | direct perception claimed as source |
| evidentiality | `ke` | INFER | inference from case-specific evidence claimed as source |
| evidentiality | `ti` | REP | a received report claimed as source |
| evidentiality | `ho` | ASSUM | assumption or supposition claimed as source |
| modality | `po` | POT | possibility or ability; `po ma` means cannot |
| modality | `na` | NEC | necessity or obligation; `na ma` means must not |
| negation | `ma` | NEG | negates the verb phrase and follows every other rank |

Each rank permits one particle. The sole same-rank pair is `se ka`, in that order. `ka ma` denies causation without asserting or denying the caused event. Need not takes the corresponding freedom construction, such as `thia lila wepu ralu nai.`

### Slot 2: constituent

**`we` / `li` > `ha` / `ra` > `lo` / numeral > `ko` > `ru` / `mo` > word**

| Particle | Gloss | Function |
|---|---|---|
| `we` | ALSO | adds a constituent to what discourse has established |
| `li` | RESTR | restricts identity, not quantity |
| `ha` | PROX | marks proximal reference; with `nai`, may predicate here |
| `ra` | DIST | marks distal reference; with `nai`, may predicate there |
| `lo` | PL | marks unquantified plurality; replaced by a numeral or quantifier |
| `nu` | ORD | makes the following numeral ordinal |
| `ko` | FOC | selects a constituent for contrast or correction |
| `ru` | INTS | increases the degree of a quality or action |
| `mo` | CMPR | forms a comparative; `mo ko` forms a superlative |
| `ne` | NAME | introduces a name atom |
| `sa` | HON.RESPECT | marks respect toward a named bearer |
| `ni` | HON.INTIM | marks personal closeness toward a named bearer |
| `le` | HON.ROLE | marks regard for a named bearer's community role |

`we` and `li` do not stack on one phrase. The local fixed orders are `mo ko`, `nu` before its numeral, and `ne` before an honorific.

### Narrow readings of absence

- No Slot 0 particle gives an ordinary declarative assertion.
- No tense particle gives present time.
- No aspect particle selects an aspectual view.
- No evidential names a source.
- No modal marks possibility, ability, necessity, or obligation.
- No `ma` leaves the predicate affirmative rather than negated.

### Working sentence template

**[Slot 0] [Subject] [Adjuncts] [Slot 2 + Object] [Slot 1] [Manner] [Verb]**

Every modifier precedes what it modifies. Empty positions disappear; the remaining elements keep their relative order.

### Cross-references

- Manual chapter 9 introduces the whole system and combines the three scopes.
- Manual chapter 14 develops tense and aspect.
- Manual chapter 15 develops passive voice, causative voice, modality, and negation.
- Manual chapter 16 develops evidentiality.
- The evidentiality, naming, and spoken-punctuation pamphlets provide extended practice in their respective areas.
- `python3 scripts/validate_examples.py --paths pamphlets/three_slots --show-warnings` checks examples, particle order, and one-per-rank structure.
