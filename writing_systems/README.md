# The writing-systems studio

Phi's romanization is one mode of writing the language among peers — canon's Letters ruling (2026-07-05) made that structural: a mark may carry meaning only if every mode can carry it. This folder is where the other modes live while they grow. Nothing here is canon; the lexicon, grammar references, and manual outrank everything in this directory, and the validator does not scan it (recovered material deliberately preserves era vocabulary that is no longer current).

## Contents

| File | What it is |
|---|---|
| `tengwar_mode.md` | The Phi Tengwar mode — full specification recovered from the 2021 LaTeX manual and decoded from its CSUR codepoints, with a modernization agenda |
| `mayan_glyph_mode.md` | The Mayan-inspired glyph block exploration, un-parked from the archive, with corrections noted against current canon |
| `recovered/tengwar.tex` | Raw recovered source: the Tengwar chapter of the 2021 manual (commit `fde058a`, `old/latex/source/`) |
| `recovered/orthography.tex` | Raw recovered source: the 2021 orthography chapter (same provenance) |
| `recovered/tengwar-telcontar.css` | The Obsidian snippet that rendered Tengwar in the original vault (commit `fde058a^`, `.obsidian/snippets/`) |

## Provenance

The Tengwar/LaTeX manual was built in the 2021 "plath" era and retired when the project moved to markdown — it sits in the abandoned-direction ledger of `archive/LANGUAGE_ARCHAEOLOGY_REPORT.md`. The sources were recovered from git history on 2026-07-05; the compiled `manual.pdf` and the Tengwar Telcontar font binaries were left in history rather than re-committed (recovery commands are in `tengwar_mode.md` §Tooling). The Mayan exploration was written later and parked in `archive/writing-system/` until this folder opened.

## Ground rules for development here

Everything must survive mode-invariance: the three modes (romanization, Tengwar, glyph blocks) must carry exactly the same information — no capitals anywhere, the period as the only punctuation, everything else spoken (`wa`, `shola…sholo`, `kona`, the closers, `ne`). When a mode's design question needs a language-level ruling, it goes to canon like any other settled decision. When a mode matures enough to write a shelf text, it graduates toward the manual.
