# Minimal-Pair Collision Audit

*Generated 2026-07-03 on branch `consistency/canon-repair`, lexicon at
795 entries. Method: exact edit-distance-1 comparison across all
content words (substitution, insertion, or deletion of one letter).*

## Headline numbers

- **831 content-word pairs** differ by a single letter.
- The distance-1 graph is a small world: one connected cluster chains
  418 words together. The chain itself is not the problem — a dense
  CV-syllable space guarantees it — but individual pairs within it
  vary enormously in risk.

## Risk model

A minimal pair is dangerous in proportion to:
1. **Semantic proximity** — words usable in the same sentence slot about
   the same topic (confusion goes undetected);
2. **Opposition** — antonyms/converses, where confusion *inverts* the
   meaning;
3. **Frequency** — basic vocabulary is used and misread most.

By this model, most of the 831 pairs are harmless (`tomi` pot / `tomi`-
adjacent `teli` bell will never be confused in context). A small set is
genuinely hazardous.

## High-risk pairs (recoining candidates — owner decision required)

| Pair | Glosses | Why dangerous | Suggested action |
|---|---|---|---|
| `thelo` / `theloa` | **lie / truth** | Direct antonyms, one letter apart; a dropped final `-a` inverts a sentence's meaning entirely | Recoin one — highest priority |
| `theloi` / `thenoi` | **exceeds / falls-short** | The two magnitude-comparison verbs are opposites differing in one letter (`l`/`n`), used in identical frames (`X Y theloi`) | Recoin one |
| `shomela` / `shonela` | **teach / learn** | Converse pair (`m`/`n`, the two most confusable nasals), same semantic field, same frames | Recoin one |
| `nai` / `tai` | **be / have** | The two most fundamental verbs in the language | Consider carefully — both are deeply embedded in examples; if kept, document explicitly |
| `melu` / `telu` | **friend / partner** | Same semantic field (close human relationships), same slot | Moderate priority |
| `phaelo` / `phaelu` | **feel / peaceful** | Different POS but co-occur in emotion sentences (`mia phaelu phaelo`) | Low — POS position usually disambiguates |
| `howela` / `nowela` | **receive / exchange** | Same gift-economy field | Low–moderate |
| `lorika` / `lorima` | **blood / build** | Different fields; visually close | Low |

## Structural observations

- The `-elV-/-olV-` neighborhood (kela/keli/kelo/kelu/kolo/kolu/kulo…)
  remains the densest region. New coinages should avoid it entirely;
  the collision policy in CLAUDE.md (Step 2) now enforces a
  same-class distance-1 rejection via
  `scripts/validate_examples.py neighbors`.
- Function words tolerate distance-1 within closed classes (sua/kua,
  mua/mue) because slot position disambiguates — no action needed.
- **`whia` (without) vs `wia` (how many)** differ only in /ʍ/ vs /w/ —
  the very contrast the CV-only particle rule was created to avoid
  (commit f862c47). Both are function words in pre-nominal position,
  so position does NOT disambiguate. Worth an owner decision alongside
  the pairs above.
- The new direction pair `lawe`/`kuri` demonstrates the opposite-pair
  standard: zero shared letters. `thelo`/`theloa` and
  `shomela`/`shonela` predate that standard.

## Resolution (2026-07-03, Word Batch 2 — owner-approved)

All five flagged hazards were resolved:

| Old | New | Notes |
|---|---|---|
| `thelo` (lie) | **`peshu`** | zero-collision form |
| `theloi` (exceeds) | **`sharoi`** | kills both theloi~thenoi and theloi~theloa |
| `shomela` (teach) | **`thumela`** | th- wisdom family; 4 letters from shonela (learn) |
| `tai` (have) | **retired** | possession folded into `phelu` (hold/have/keep) |
| `whia` (without) | **`whuo`** | ends the /ʍ/-vs-/w/ pair with `wia` |

Remaining moderate pairs (`melu`/`telu`, `howela`/`nowela`,
`phaelo`/`phaelu`) stand as acceptable, protected going forward by the
coining policy in CLAUDE.md Step 2.
