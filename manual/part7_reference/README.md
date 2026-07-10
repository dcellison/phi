# Part VII: Reference

| File | What it is |
|---|---|
| `quick_reference_grammar.md` | The whole grammar on one page |
| `lexicon/alphabetical.md` | Every word A–Z — **generated** |
| `lexicon/by_domain.md` | Content words by semantic domain — **generated** |
| `lexicon/by_module.md` | Optional vocabulary grouped by domain module — **generated** |
| `lexicon/by_pos.md` | All words by part of speech — **generated** |
| `modules/` | Speaker-facing explanations and usage guides for optional domain vocabulary |
| `sample_texts.md` | Dialogues, a poem, and the guide to the texts shelf |

The four lexicon files are generated from `vocabulary/*.json` (the single source of truth) and must never be edited by hand. After any vocabulary change:

```bash
python3 scripts/generate_reference.py
```

How Phi is written is chapter 8 §6: the romanization, the Tengwar mode, and the reserved glyph mode. The Tengwar mode is taught glyph by glyph in `pamphlets/tengwar_mode/`, whose pages render every line in both scripts.
