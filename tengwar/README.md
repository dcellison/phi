# The Phi Tengwar mode

Phi has two current writing modes: romanization and Tengwar. They carry the same words, boundaries, and punctuation. Neither mode adds meaning that the other cannot express.

## Contents

| Path | Purpose |
|---|---|
| [`mode.md`](mode.md) | The current specification: consonants, vowel tehtar, hiatus, spacing, punctuation, and implementation notes. |
| [`glyphs.json`](glyphs.json) | Committed outlines and placement adjustments used by the site renderer. |
| [`fonts/TengwarTelcontar.ttf`](fonts/TengwarTelcontar.ttf) | Tengwar Telcontar 0.08 by Johan Winge, retained as the source font for outline extraction. |

[`scripts/tengwar.py`](../scripts/tengwar.py) renders validated romanized Phi as deterministic inline SVG. [`scripts/extract_tengwar_glyphs.py`](../scripts/extract_tengwar_glyphs.py) is the manual extraction tool that rebuilds `glyphs.json` from the font while preserving hand-tuned placement adjustments. Normal builds use the committed JSON and do not require font tooling.

The speaker-facing [Tengwar pamphlet](../pamphlets/tengwar_mode/) teaches the mode through paired examples. Historical sources and the retired native-glyph studies are preserved under [`archive/writing_systems/`](../archive/writing_systems/); they do not define current Phi.
