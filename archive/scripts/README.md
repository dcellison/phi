# Deprecated Scripts

These scripts were quarantined during the 2026-07 canon-repair pass because
they no longer match the repository's data layout and produce **wrong or
misleading results**. They are kept for reference only. Do not run them.

| Script | Why deprecated |
|---|---|
| `check_vocabulary.py` | Expects list-format JSON; all vocabulary files are dict-format. Reports "0 words found". |
| `phicheck` | Wrapper around `check_vocabulary.py`; same failure. |
| `find_available_words.py` | Depends on the broken loader above, so it reports **every** two-syllable form as available — using it would create collisions. Use `validate_examples.py neighbors WORD` instead. |
| `update_available_words.py` | Regenerates the (invalid) output of `find_available_words.py`. |
| `lexicon_tool.py` | Creates a rich DB schema incompatible with the live 3-column `lexicon.db`; `find` crashes with IndexError; `status` looks for files at retired paths. Superseded by `lexicon_tool_simple.py`. |
| `audit_rationales.py` | Requires `conceptual-roots.md` at repo root (now in `archive/`); its root-per-syllable premise was explicitly abandoned (see `archive/recap.md`). |
| `check_word_vocabulary.py` | Expects a `/words/` directory that no longer exists. |
| `check_comm_words.py` | Imports `load_all_words` from `check_vocabulary.py`, which doesn't define it. |
| `calculate_possible_words.py` | Hardcodes stale lexicon counts ("546 words"). |
| `remove_array_brackets.py` | One-time migration for a retired `lexicon/` directory layout. |
| `vocabulary_stats.py` | Expects the retired `/words/` layout. |

## Current tooling

- `scripts/validate_examples.py` — the single validator: lexicon schema +
  phonotactics + syllable arrays + duplicates + documentation example
  checking + `neighbors` collision check for new coinages.
- `scripts/check_duplicates.py` — strict duplicate word/gloss checker.
- `scripts/lexicon_tool_simple.py` — SQLite index over the JSON files
  (JSON remains the source of truth). Now scans `vocabulary/interjection/`
  and permits duplicate glosses.
