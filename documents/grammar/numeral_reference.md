# Phi Numeral System Reference

This document is the canonical working reference for Phi's ternary numerals, approximation, classifiers, ordinals, arithmetic, and magnitude comparison. The manual's chapter 12 teaches the same system more gradually.

## Scope and design

Phi uses a finite base-three numeral system. Its small digit inventory and grouped forms make large exact counts more linguistically conspicuous than they are in familiar decimal systems. That friction is a design choice: it invites speakers to consider whether an exact count, an estimate, a quantifier, or separately preserved source material best serves the context.

This design does not establish that ternary thought is more natural, that approximate speech is more honest, or that particular numeral words make people mindful, generous, or content. Exact values often support care, safety, accessibility, accountability, trade, science, and faithful reporting. Phi therefore preserves exact information that its internal numerals cannot express as source material outside the Phi passage.

## Learning scope

Numeral learning is divided into four practical layers:

| Layer | Range or skill | Expected use |
|---|---|---|
| Foundation | 0-8 | Learn `mu`, `ta`, `wi`, and compositions with `shao`; recognize and produce them without decimal calculation where possible. |
| Working range | 0-26 | Add `phoi`; sufficient for many ordinary counts and dates. |
| Extended exact range | 27-242 | Add `lau` and `rei`; use when an exact internal Phi count matters. |
| Calculation | arithmetic and comparison | Learn the mandatory `nela` operand boundary and the operation-specific referent rules. |

Conversational competence does not require fast conversion of arbitrary decimal values, memorization of every form through 242, or spoken arithmetic. Ordered recitation is useful, but learners also need shuffled recognition, production from visible quantities, and practice with triad arrangements. Learning time will vary.

## Digits

Phi has three digit words:

| Digit | Value | IPA |
|---|---:|---|
| `mu` | 0 | /ˈmu/ |
| `ta` | 1 | /ˈt̪ä/ |
| `wi` | 2 | /ˈwi/ |

`mu` is the complete numeral for zero. Inside a compound numeral, zero coefficients are omitted rather than pronounced.

```text
ta melu
one friend
(one friend)

wi melu
two friend
(two friends)

mu melu
zero friend
(zero friends)
```

## Scale units

Four scale units name powers of three:

| Scale | Value | Gloss | IPA |
|---|---:|---|---|
| `shao` | 3 | three-group | /ˈʃä.o̞/ |
| `phoi` | 9 | nine-group | /ˈɸo̞.i/ |
| `lau` | 27 | twenty-seven-group | /ˈlä.u/ |
| `rei` | 81 | eighty-one-group | /ˈre̞.i/ |

These forms behave as group nouns in numeral composition. A digit precedes the group it counts, following Phi's modifier-first order.

## Exact composition

An exact positive numeral follows this pattern:

`[ta|wi rei] [ta|wi lau] [ta|wi phoi] [ta|wi shao] [ta|wi]`

Use only the places the value needs. The rules are:

1. Each scale may appear at most once.
2. Scales appear in descending order: `rei`, `lau`, `phoi`, `shao`.
3. Only `ta` or `wi` may count a scale.
4. A zero coefficient is omitted; `mu` does not fill an internal place.
5. A final `ta` or `wi` expresses units.
6. No conjunction appears inside a numeral.
7. Scale units are not recursively counted. `rei` is the highest exact place.

| Value | Phi | Composition |
|---:|---|---|
| 3 | `ta shao` | 1×3 |
| 4 | `ta shao ta` | 1×3 + 1 |
| 5 | `ta shao wi` | 1×3 + 2 |
| 6 | `wi shao` | 2×3 |
| 8 | `wi shao wi` | 2×3 + 2 |
| 9 | `ta phoi` | 1×9 |
| 12 | `ta phoi ta shao` | 1×9 + 1×3 |
| 14 | `ta phoi ta shao wi` | 1×9 + 1×3 + 2 |
| 22 | `wi phoi ta shao ta` | 2×9 + 1×3 + 1 |
| 27 | `ta lau` | 1×27 |
| 82 | `ta rei ta` | 1×81 + 1 |
| 121 | `ta rei ta lau ta phoi ta shao ta` | 1×81 + 1×27 + 1×9 + 1×3 + 1 |
| 242 | `wi rei wi lau wi phoi wi shao wi` | 2×81 + 2×27 + 2×9 + 2×3 + 2 |

Canonical exact Phi numerals therefore cover 0 through 242. Values of 243 and above have no internal Phi numeral. When their exact identity matters, keep the figures, notation, units, or record outside the Phi passage in the surrounding medium. When only magnitude matters, use an approximate scale or quantifier.

## Approximate scale forms

A scale unit without `ta` or `wi` before it denotes an approximate quantity around that scale. Phi defines no numerical rounding interval for these forms; context supplies the useful degree of precision.

```text
shao philo
three-group day
(about three days; a few days)

phoi miona
nine-group person
(about nine people)

lau shiro
twenty-seven-group tree
(trees on the scale of a twenty-seven-group; often "many trees")

rei silero
eighty-one-group star
(stars on the scale of an eighty-one-group; a great many stars)
```

Bare `lau` and `rei` often function pragmatically like *many* and *a great many* or *too many to count for this purpose*. They do not mean that the quantity is literally uncountable. Use an ordinary quantifier when no scale estimate is intended.

Approximation is appropriate when the exact value is unknown or irrelevant. It is not inherently more truthful than precision. A recipe, dose, accessibility specification, safety threshold, allocation, transaction, or evidence report may require an exact internal numeral or an exact source record.

## Quantifiers

Quantifiers precede what they quantify:

| Phi | Meaning |
|---|---|
| `theula` | all, every |
| `sheloi` | many |
| `shelami` | most |
| `soli` | some, several |
| `phina` | few |
| `theli` | each |
| `wheli` | any |
| `mawha` | none |
| `henoi` | enough |
| `wia` | how many |

`henoi` expresses sufficiency, not a numerical result: `henoi sulopa nai.` means “There is enough soup.” What counts as enough depends on the people, purpose, and conditions; the word does not settle that judgment.

`wia` asks for quantity: `wia himo miona so shua.` means “How many people will come?” An answer may be exact, approximate, or quantified, according to what the speaker knows and what the context needs.

## Nature classifiers

Phi has four optional classifiers:

| Classifier | Gloss | Canonical scope |
|---|---|---|
| `himo` | HUM.CLF | people |
| `lipha` | LIFE.CLF | living beings, living parts, and life in waiting |
| `themo` | THING.CLF | detached or crafted physical objects |
| `nophe` | ABST.CLF | concepts, time, events, and non-physical countables |

The order is `[number] [classifier] [noun]`. The classifier is also available after `wia` in a quantity question, but ordinary quantifiers such as `soli`, `sheloi`, and `henoi` modify the noun directly without a classifier:

```text
wi himo melu
two HUM.CLF friend
(two friends, classified as people)

ta shao lipha shiro
one three-group LIFE.CLF tree
(three trees, classified as living beings)
```

The nature-now rule governs the classifier chosen. A living ear takes `lipha`; a carved wooden ear takes `themo`. A storm counted as an event takes `nophe`. Classifiers remain optional in every context: `wi melu` and `wi himo melu` are both complete. Choosing a classifier foregrounds a category and may carry a tone of acknowledgment, but it does not prove that the speaker is mindful or respectful.

## Ordinals

The Slot 2 particle `nu` before a cardinal marks position:

```text
nu ta lopia
ORD one child
(the first child)

nu ta shao philo
ORD one three-group day
(the third day)
```

When position itself is the topic, use the noun `noa`: `lopia mua wi noa nai.` means “The child is in the second position.” All exact ordinal numerals share the cardinal range of 1 through 242; preserve a larger exact position in source material.

## Numerals and plural marking

A numeral or quantifier already marks quantity, so it never combines with plural `lo`.

```text
ta shao lipha shiro
(three trees)

sheloi melu
(many friends)

lo shiro
(trees; unquantified plural)
```

The wider noun-phrase slots remain modifier-first, but quantity strategies are alternatives: use a numeral with an optional classifier, an ordinary quantifier without a classifier, or `lo` for an unquantified plural. A possessor precedes the phrase it owns.

## Arithmetic

Phi narrates integer arithmetic with four operation verbs and one result or equality verb:

| Operation | Phi | Literal frame |
|---|---|---|
| addition | `sholei` | gather |
| subtraction | `leiro` | release |
| multiplication | `welura` | spread |
| division | `phanoi` | portion |
| result or equality | `kelai` | result; equal |

The coordinating conjunction `nela` is the mandatory audible and written boundary between operands:

`[operand 1] nela [operand 2] [operation]. [result] kelai.`

Without `nela`, adjacent operands can be indistinguishable from one compound numeral. For example, `ta shao wi` is the single numeral five, so it cannot also unambiguously mean the operands three and two. `nela` never occurs inside an exact numeral.

```text
wi nela ta shao sholei. ta shao wi kelai.
two COORD one three-group gather. one three-group two equals.
(Two plus three results in five.)

ta phoi nela ta shao leiro. wi shao kelai.
one nine-group COORD one three-group release. two three-group equals.
(Nine minus three results in six.)

ta shao nela wi welura. wi shao kelai.
one three-group COORD two spread. two three-group equals.
(Three multiplied by two results in six.)

ta phoi nela ta shao phanoi. ta shao kelai.
one nine-group COORD one three-group portion. one three-group equals.
(Nine divided by three results in three.)
```

A plain equality uses the same boundary: `ta shao ta nela ta shao ta kelai.` means “Four equals four.” To ask for a result, use `hina kelai`: `ta shao nela wi sholei. hina kelai.` means “Three plus two; what results?”

### Referents in arithmetic

The classifier is always optional, but the referents and dimensions of an operation must make sense:

- Addition and subtraction require commensurable quantities. If nouns or classifiers are stated, both operands and the result name the same kind of quantity.
- In multiplication, the first operand may name the counted thing and the second is a bare factor; the product inherits the first operand's kind.
- In division, the first operand names the total being portioned, the second may name recipients or groups, and the quotient inherits the total's kind. State any remainder separately.

```text
wi lipha powea nela ta shao lipha powea sholei. ta shao wi lipha powea kelai.
two LIFE.CLF egg COORD one three-group LIFE.CLF egg gather. one three-group two LIFE.CLF egg equals.
(Two eggs plus three eggs results in five eggs.)

ta shao themo noru nela wi welura. wi shao themo noru kelai.
one three-group THING.CLF bowl COORD two spread. two three-group THING.CLF bowl equals.
(Three bowls multiplied by two results in six bowls.)
```

Phi currently defines no negative numeral or fractional numeral syntax. Subtraction stated entirely in Phi therefore assumes a nonnegative result, and non-even division uses an integer quotient plus a separately stated remainder. Preserve a negative, fractional, higher-precision, or out-of-range calculation in source material when its exact form matters.

The operation words supply metaphors, not guarantees. `sholei` does not make gathering cooperative, `leiro` does not make loss generous, `welura` does not make growth beneficial, and `phanoi` does not make equal portions just or sufficient. A speaker must state or examine those claims separately.

## Magnitude comparison

`sharoi` means “exceed in magnitude” and `thenoi` means “fall short in magnitude.” Comparison uses the same mandatory operand boundary as arithmetic:

`[quantity 1] nela [quantity 2] [comparison verb]`

```text
ta phoi nela ta shao sharoi.
one nine-group COORD one three-group exceed.
(Nine exceeds three; 9 > 3.)

ta shao nela ta phoi thenoi.
one three-group COORD one nine-group falls-short.
(Three falls short of nine; 3 < 9.)

wa ta shao nela wi shao sharoi.
Q one three-group COORD two three-group exceed.
(Does three exceed six?)
```

Negation expresses inclusive comparisons: `ta shao nela ta shao ma thenoi.` means “Three does not fall short of three; 3 ≥ 3.” Real-world comparisons should state comparable quantities and preserve the relevant measure or criterion when it is not obvious.

These verbs lexically separate magnitude from worth: *exceeds* need not mean *is better*, and *falls short* need not mean *is inadequate*. That distinction does not prevent a speaker or institution from using comparison to rank, shame, or exclude; context and consequences remain open to criticism.

## Cognitive and philosophical claims

Three is within the small range adults can commonly identify without serial counting. Nine, twenty-seven, and eighty-one are not directly perceived as exact quantities in that way. Regular triad arrangements can make their hierarchical grouping visible, but reading those groups is a learned enumeration skill.

Base three is a coherent compositional design but unusual among documented natural numeral systems. A small base does not by itself make a numeral system unlearnable, while unfamiliar grouping, longer number words, operand syntax, and conversion from a familiar base add learning and working-memory demands. Phi treats that cost as acceptable but does not present it as cognitively universal or morally transformative.

The numeral system can make some exact counts longer and some approximate or sufficiency expressions readily available. It cannot by grammar alone cause contentment, sharing, equality, ecological care, or nonviolence. Those are values speakers may pursue through institutions, choices, and explicit discussion. See `documents/design/psychological_violence_of_measurement.md` for the design argument and its evidence boundaries.

## Quick reference

- Digits: `mu` 0, `ta` 1, `wi` 2.
- Scales: `shao` 3, `phoi` 9, `lau` 27, `rei` 81.
- Exact range: 0-242; maximum `wi rei wi lau wi phoi wi shao wi`.
- Exact form: descending scales, `ta` or `wi` before each scale, no repeated scale, omitted zero positions, optional final units.
- Approximate form: bare scale, with no fixed rounding interval.
- Classifiers: `himo` people, `lipha` living, `themo` detached or crafted objects, `nophe` abstract, time, or events; always optional.
- Ordinal: `nu [cardinal]`; position as a noun: `[cardinal] noa`.
- Arithmetic: `[operand 1] nela [operand 2] [operation]. [result] kelai.`
- Comparison: `[quantity 1] nela [quantity 2] sharoi|thenoi.`
- Larger exact values, fractions, negative numbers, units, formulas, and exact technical notation: source material outside the Phi passage.

## Related documentation

- Manual teaching chapter: `manual/part4_grammar/ch12_numbers/`
- Particle inventory: `documents/grammar/particle_reference.md`
- Design argument and evidence boundaries: `documents/design/psychological_violence_of_measurement.md`
- Canonical grammar rulings: `canon.md`
