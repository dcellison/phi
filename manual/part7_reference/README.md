# Part VII: Reference

| File | What it is |
|---|---|
| `quick_reference_grammar.md` | The whole grammar on one page |
| `lexicon/alphabetical.md` | Every word A–Z — **generated** |
| `lexicon/by_domain.md` | Content words by semantic domain — **generated** |
| `lexicon/by_pos.md` | All words by part of speech — **generated** |
| `sample_texts.md` | Dialogues, a poem, and the first complete text |

The three lexicon files are generated from `vocabulary/*.json` (the
single source of truth) and must never be edited by hand. After any
vocabulary change:

```bash
python3 scripts/generate_reference.py
```

The writing-system section planned in the outline is omitted: the
Mayan-inspired glyph proposal (`documents/writing-system/`) has not
been developed into a usable script. Phi is currently written in its
romanization.
