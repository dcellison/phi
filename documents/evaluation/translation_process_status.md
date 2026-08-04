# Isolated translation certification

This ledger records which Phi translations have completed the isolated process. An earlier fidelity review does not count as certification. The machine-readable register is `project/translation_process_status.json`. The catalogue supplies the standalone works and Gibran selections, while the chapter files supply the present *News from Nowhere* sequence. CI rejects a missing row, an extra row, a stale report, or a certified work whose unit count or digest has changed.

A pending translation may still be accurate and carefully reviewed. Pending means only that its English was not demonstrably derived in a fresh source-blind context after the Phi was frozen. Originals and the Ring Verse refusal are outside this queue because they make a different promise to the reader.

The complete procedure is described in [How a Phi translation is made](../reference/translation_process.md).

## Current state

| State | Documents |
|---|---:|
| Certified | 9 |
| In progress | 0 |
| Pending | 11 |
| Total | 20 |

## Short works

Certified: 8 of 10.

| Document | File | State | Record |
|---|---|---|---|
| lothea thole — The Practice of Love | [metta_sutta.md](../../texts/metta_sutta.md) | Certified | D105; [PR #693](https://github.com/dcellison/phi/pull/693); 36 units |
| sileta kenua wireo moenu lo sherewa: A Solarpunk Manifesto | [solarpunk_manifesto.md](../../texts/solarpunk_manifesto.md) | Certified | D106; [PR #694](https://github.com/dcellison/phi/pull/694); 38 units |
| nitho howeli nela sileta — The North Wind and the Sun | [north_wind_and_sun.md](../../texts/north_wind_and_sun.md) | Certified | D103; [PR #691](https://github.com/dcellison/phi/pull/691); 17 units |
| theula miona — Article 1 of the Universal Declaration of Human Rights | [human_rights_article_one.md](../../texts/human_rights_article_one.md) | Certified | D108; [PR #697](https://github.com/dcellison/phi/pull/697); 2 units |
| ta haluma — The Babel Text | [babel_text.md](../../texts/babel_text.md) | Certified | D109; [PR #698](https://github.com/dcellison/phi/pull/698); 9 units |
| mophira nela lo kalora — Schleicher's Fable | [schleicher_fable.md](../../texts/schleicher_fable.md) | Certified | D107; [PR #696](https://github.com/dcellison/phi/pull/696); 4 units |
| thiku miona lue silero — Selections from The Little Prince | [little_prince_excerpts.md](../../texts/little_prince_excerpts.md) | Certified | D110; [PR #699](https://github.com/dcellison/phi/pull/699); 5 units |
| wuloe wetha tupiwa — The Velveteen Rabbit | [velveteen_rabbit.md](../../texts/velveteen_rabbit.md) | Certified | D111; [PR #700](https://github.com/dcellison/phi/pull/700); 426 units |
| keiro — Selections from the Tao Te Ching | [tao_te_ching.md](../../texts/tao_te_ching.md) | Pending | Awaiting D102 certification. |
| nulo sano korua — The Heart Sutra | [heart_sutra.md](../../texts/heart_sutra.md) | Pending | Awaiting D102 certification. |

## phewo phelui — Kahlil Gibran

Certified: 1 of 4.

| Document | File | State | Record |
|---|---|---|---|
| lothea — On Love | [on_love.md](../../texts/gibran/on_love.md) | Certified | D112; [PR #701](https://github.com/dcellison/phi/pull/701); 33 units |
| phomila — On Children | [on_children.md](../../texts/gibran/on_children.md) | Pending | Awaiting D102 certification. |
| loa — On Giving | [on_giving.md](../../texts/gibran/on_giving.md) | Pending | Awaiting D102 certification. |
| riola — On Work | [on_work.md](../../texts/gibran/on_work.md) | Pending | Awaiting D102 certification. |

## nophi lue mawha lokue — News from Nowhere

Certified: 0 of 6.

| Document | File | State | Record |
|---|---|---|---|
| nophi lue mawha lokue — News from Nowhere, ch. 1: Discussion and Bed | [chapter_01.md](../../texts/news_from_nowhere/chapter_01.md) | Pending | Awaiting D102 certification. |
| nophi lue mawha lokue — News from Nowhere, ch. 2: A Morning Bath | [chapter_02.md](../../texts/news_from_nowhere/chapter_02.md) | Pending | Awaiting D102 certification. |
| nophi lue mawha lokue — News from Nowhere, ch. 3: The Guest House and Breakfast Therein | [chapter_03.md](../../texts/news_from_nowhere/chapter_03.md) | Pending | Awaiting D102 certification. |
| nophi lue mawha lokue — News from Nowhere, ch. 4: A Market by the Way | [chapter_04.md](../../texts/news_from_nowhere/chapter_04.md) | Pending | Awaiting D102 certification. |
| nophi lue mawha lokue — News from Nowhere, ch. 5: Children on the Road | [chapter_05.md](../../texts/news_from_nowhere/chapter_05.md) | Pending | Awaiting D102 certification. |
| nophi lue mawha lokue — News from Nowhere, ch. 6: A Little Shopping | [chapter_06.md](../../texts/news_from_nowhere/chapter_06.md) | Pending | Awaiting D102 certification. |

## Certification records

### lothea thole — The Practice of Love

D105 certified this document in [PR #693](https://github.com/dcellison/phi/pull/693) on 2026-08-02. The freeze contains 36 aligned Phi units, and its `fausboll` citations reconstruct 1,615 normalized source characters exactly. Three affected units were discarded after the first anonymous derivation exposed source-side problems, then derived again in fresh source-blind contexts after repair.

Frozen Phi SHA-256:

```text
73851696237e395421f8dd12b005d8e6bee0332a1654a4734d317679c4c7d7d1
```

Published aligned-layer SHA-256:

```text
4c69caf26388b7dbf757df56722de3af976e9b6f68df2c3001856366a4f1f486
```

### sileta kenua wireo moenu lo sherewa: A Solarpunk Manifesto

D106 certified this document in [PR #694](https://github.com/dcellison/phi/pull/694) on 2026-08-02. The freeze contains 38 aligned Phi units, and its `solarpunk` citations reconstruct 4,538 normalized source characters exactly. Anonymous derivation audits exposed source-side faults; every affected unit was repaired before the final freeze and derived again, with further source-blind passes replacing grouping and naturalness failures.

Frozen Phi SHA-256:

```text
57baf00910adb9e5d0ec9c23ab0d56e2dcc3c023c787f336b279dce9c4b840ee
```

Published aligned-layer SHA-256:

```text
da5fe1c281eb8716b2156db6088f8322edd2be0f132ecb929193233516a36eaf
```

### nitho howeli nela sileta — The North Wind and the Sun

D103 certified this document in [PR #691](https://github.com/dcellison/phi/pull/691) on 2026-08-02. The freeze contains 17 aligned Phi units, and its `aesop` citations reconstruct 1,172 normalized source characters exactly. Two lines rejected during assembly were derived again from anonymous Phi units in a second source-blind context.

Frozen Phi SHA-256:

```text
63fbc9282fe0651f27f18107ad34914e2358be446301e1bdf08f638d9296f470
```

Published aligned-layer SHA-256:

```text
b82be806aaa23c52329448b61f622b39ea96c378df3edd21d73d12b81d314b25
```

### theula miona — Article 1 of the Universal Declaration of Human Rights

D108 certified this document in [PR #697](https://github.com/dcellison/phi/pull/697) on 2026-08-03. The freeze contains 2 aligned Phi units, and its `udhr` citations reconstruct 170 normalized source characters exactly. The first anonymous reading exposed a manner phrase that could attach to either action or obligation-holding. That unit was discarded, repaired with an explicit requirement frame, and derived again in fresh source-blind contexts.

Frozen Phi SHA-256:

```text
1fe727d7a07ead2ac96c2deb2a082f9356d3780c57326f1e9de5ea26bc831fa5
```

Published aligned-layer SHA-256:

```text
5ccab86290265f343c6d9a079f1341b5ad4244852abf3c8c9730dc6a6713e526
```

### ta haluma — The Babel Text

D109 certified this document in [PR #698](https://github.com/dcellison/phi/pull/698) on 2026-08-03. The freeze contains 9 aligned Phi units, and its `kjv` citations reconstruct 1,191 normalized source characters exactly. The source-only pass replaced an anatomical face metaphor. The first anonymous audit then exposed ambiguous relative roles; those Phi units were rebuilt without relative gaps and derived again, while audited readings and a one-unit retry restored every occurrence of surface in English.

Frozen Phi SHA-256:

```text
2cb3d2ccc6b5bb33a1860a6081e45842ee0911a6bfa40637e410185e859da136
```

Published aligned-layer SHA-256:

```text
1adff02c2612b076b0f538afff3adebdf9ca1609f092ccc9875b987770573e32
```

### mophira nela lo kalora — Schleicher's Fable

D107 certified this document in [PR #696](https://github.com/dcellison/phi/pull/696) on 2026-08-03. The freeze contains 4 aligned Phi units, and its `schleicher-en` citations reconstruct 703 normalized source characters exactly. The first anonymous derivation exposed ambiguous horse identity; that unit was repaired and derived again in fresh source-blind contexts while the other three retained their checked outputs under unchanged hashes.

Frozen Phi SHA-256:

```text
dec1e02503f0c9571c4da870a80d67610508efce1d8aa65cbd44d6e9641c3fca
```

Published aligned-layer SHA-256:

```text
774ed454c5d926c7dd45f10d56121cac4f77df54e0fdf73ee2d7a198ea0a4ef3
```

### thiku miona lue silero — Selections from The Little Prince

D110 certified this document in [PR #699](https://github.com/dcellison/phi/pull/699) on 2026-08-03. The freeze contains 5 aligned Phi units, and its `woods` citations reconstruct 238 normalized source characters exactly. The source-only pass repairs subject and adjunct order and makes simplicity an explicit predication. A fresh anonymous context derives all five units, and an independent reader confirms the deterministic responsibility sample without exposing a source-side fault.

Frozen Phi SHA-256:

```text
0cd1f7cd946000b9d6c635a645e90141ada25dacb0443845a912d8470226e3d2
```

Published aligned-layer SHA-256:

```text
91de8f40cf7d5a34898320d9da7a747e70235699ec77b71ae65e1cc62ef07d96
```

### wuloe wetha tupiwa — The Velveteen Rabbit

D111 certified this document in [PR #700](https://github.com/dcellison/phi/pull/700) on 2026-08-03. The freeze contains 426 aligned Phi units, and its `williams` citations reconstruct 20,296 normalized source characters exactly. A fresh anonymous context derived the complete frozen stream. Independent source-blind review exposed further Phi faults; each affected English layer was discarded, and targeted fresh contexts derived and audited every repaired unit before publication.

Frozen Phi SHA-256:

```text
16597a3af79e10b9ff4e66638108da09e4c9fb6bce6ccd4d275ccb4b841c3f59
```

Published aligned-layer SHA-256:

```text
42ab9396fd582eb5a3d6970eaea221f80a6fb5c0707bfd351121095c15e272c5
```

### lothea — On Love

D112 certified this document in [PR #701](https://github.com/dcellison/phi/pull/701) on 2026-08-03. The freeze contains 33 aligned Phi units, and its `gibran` citations reconstruct 2,403 normalized source characters exactly. A fresh anonymous context derives the complete frozen stream. Independent comparison finds two English-layer disagreements and four Phi attachment ambiguities; the affected layers are discarded, the Phi is repaired, and fresh source-blind contexts derive and audit the revised units before publication.

Frozen Phi SHA-256:

```text
7494350b9f12a5a616c046057cf8dffcfc5e9ad8ea54f7e7c35e0f48a85d6125
```

Published aligned-layer SHA-256:

```text
045a51f919a67ea5802aff9445043fac26d566a900098bdbcc9a068f5f24a31a
```

## Maintaining the ledger

Run `python3 scripts/translation_process_status.py --write` after changing a status or adding a translation. Run `python3 scripts/translation_process_status.py --check` before publication. Changing certified Phi invalidates its English. CI will fail until the English has been derived again from a new anonymous packet and the new freeze has its own evidence.
