# Part VII: Reference

| File | What it is |
|---|---|
| `quick_reference_grammar.md` | The whole grammar on one page |
| `compounds.md` | Every canonized compound idiom and why it stays compositional (**generated**) |
| `lexicon/alphabetical.md` | Every word from A to Z (**generated**) |
| `lexicon/by_domain.md` | Content words by semantic domain (**generated**) |
| `lexicon/by_module.md` | Optional vocabulary grouped by domain module (**generated**) |
| `lexicon/by_pos.md` | All words by part of speech (**generated**) |
| `modules/` | Speaker-facing explanations and usage guides for optional domain vocabulary |
| `sample_texts.md` | Dialogues, a poem, and the guide to the texts shelf |

The four lexicon files are generated from the entry JSON under `vocabulary/`, and `compounds.md` comes from `documents/reference/compounds.md`. These five files are views of their source material and should not be edited by hand. After any vocabulary or registry change:

```bash
python3 scripts/generate_reference.py
```

How Phi is written is chapter 8 §6: the romanization, the Tengwar mode, and the reserved glyph mode. The Tengwar mode is taught glyph by glyph in `pamphlets/tengwar_mode/`, whose pages render every line in both scripts.
