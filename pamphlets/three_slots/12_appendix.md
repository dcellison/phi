# Appendix: the complete inventory

Thirty-five particles — the whole grammar, one page.

### Slot 0 — the frame (first, or absent)

| Particle | Gloss | Duty |
|---|---|---|
| `wa` | Q | announces a yes/no question |
| `no` | IMP | announces a request or gentle command |
| `lu` | COND | announces a condition; consequence follows as its own sentence |
| `he` | IRR | irrealis — exists only as `lu he`, the counterfactual |
| `su` | OPT | announces a wish; claims nothing, demands nothing |
| `pi` | POL | politeness — the outermost frame, always first |

### Slot 1 — the stack (before the verb, ranked, one per rank)

**Tense > Aspect > Voice > Evidentiality > Modality > Negation**

| Rank | Particle | Gloss | Duty |
|---|---|---|---|
| tense | `to` | PST | past; unmarked is present |
| tense | `so` | FUT | future |
| aspect | `ki` | PFV | complete at the tense's reference time (`ki` have, `to ki` had, `so ki` will have) |
| aspect | `si` | IPFV | ongoing, mid-flow — never habit |
| aspect | `pa` | INCH | beginning |
| aspect | `te` | CESS | ending — the language's only *stop* |
| aspect | `ro` | HAB | habitual, characteristic — the pattern |
| voice | `se` | PASS | the receiver speaks; agent optional |
| voice | `ka` | CAUS | the second author on the record; pairs only as `se ka` |
| evid. | `hi` | DIR | witnessed — the claim, never the default |
| evid. | `ke` | INFER | inferred from evidence |
| evid. | `ti` | REP | received from another |
| evid. | `ho` | ASSUM | assumed from pattern |
| modal | `po` | POT | possible, able; `po ma` cannot |
| modal | `na` | NEC | necessary; `na ma` must not; `ka na` must make |
| neg. | `ma` | NEG | last, against the verb; `ka ma` denies the causation |

### Slot 2 — the word's dress (immediately before its word, nesting wider-first)

**`we`/`li` > `ha`/`ra` > `lo`/numerals > `ko` > `ru`/`mo` > word**

| Particle | Gloss | Duty |
|---|---|---|
| `we` | ALSO | adds an echo across sentences |
| `li` | RESTR | the fence: identity only, never quantity |
| `ha` | PROX | this; also a locative predicate with `nai` |
| `ra` | DIST | that; likewise |
| `lo` | PL | unquantified plural; never beside a numeral |
| `nu` | ORD | position, before its numeral |
| `ko` | FOC | the pointing finger; with `mo` makes the superlative |
| `ru` | INTS | intensity, on the word it touches |
| `mo` | CMPR | more; `mo ko` most; `sheo` carries the *than* |
| `ne` | NAME | the spoken capital (Pamphlet 5) |
| `sa` | HON.RESPECT | announced respect |
| `ni` | HON.INTIM | announced closeness |
| `le` | HON.ROLE | announced regard for a role |

### The ruled readings, one line each

- One per rank; the single pairing is `se ka`, in that order.
- `po ma` cannot · `na ma` must not · `ka ma` causation denied · need-not is the freedom periphrasis.
- `ki` completes at the reference time tense sets.
- `si` mid-flow only; `ro` habit only; the border is one question wide.
- An unmarked sentence claims no source; every silence in the system is a meaning.
- Politeness first; one speech-act per sentence; `kona` is not a frame but its own utterance.
- Slot 2 nests wider-first; one discourse relation per phrase.

### Cross-references

- Doctrine: manual ch11 (the backbone, all six sections); ch15 (tense and aspect); ch16 (voice, possibility, negation); ch17 (evidentiality); `documents/grammar/particle_reference.md` (the full inventory with examples).
- Canon: the seven particle rulings — unmarked-claims-no-source, the `si`/`ro` carve, compositional `ki`, one per rank, `ka` is voice, the `li` fence, Slot 2 nests — plus the Slot 1 order and modal negation rulings they complete.
- Sibling pamphlets: 3 (evidentiality, whole); 5 (`ne` and the honorifics); 6 (`su` at text scale); 7 (`wa`, `kona`, and the marks that are words).
- The enforcement: `scripts/validate_examples.py` checks order and one-per-rank mechanically, corpus-wide, since the July audit.
