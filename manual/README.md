# Phi manual

The manual is Phi's complete teaching and reference work. Read it from First light, or leave it open when a particle, sound, or clause refuses to come to mind. The website builds its contents from the live files and keeps all 139 readings in one sequence.

## Reading order

| Part | Focus | Chapters | Source |
|---|---|---:|---|
| I | First light | 1-2 | `part1_first_light/` |
| II | The soul of Phi | 3-6 | `part2_soul/` |
| III | Phonology | 7-8 | `part3_phonology/` |
| IV | Grammar | 9-16 | `part4_grammar/` |
| V | Complex structures | 17-20 | `part5_complex/` |
| VI | Mastery | 21-23 | `part6_mastery/` |
| VII | Reference | - | `part7_reference/` |
| Back matter | Appendices and colophon | - | `appendices/` and `/colophon.md` |

[`outline.md`](outline.md) maps the parts and chapters. Each reading takes its title from its own Markdown heading. The root colophon closes the manual's reading order and also supplies the site's footer-linked colophon.

## Authority

The manual teaches Phi, but it does not outrank [`/canon.md`](../canon.md) or the canonical JSON under [`/vocabulary/`](../vocabulary/). Current grammar references live under [`/documents/grammar/`](../documents/grammar/). When two documents disagree, the authority order in canon settles the matter.

Part VII's lexicon listings and compound registry are generated views. Edit the vocabulary JSON or [`documents/reference/compounds.md`](../documents/reference/compounds.md), then rebuild the references:

```bash
python3 scripts/generate_reference.py
```

## Checks

Validate the language examples and rebuild the reader from the repository root:

```bash
python3 scripts/validate_examples.py --paths manual
python3 scripts/build_site.py
```
