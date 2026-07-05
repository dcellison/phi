# The Phi Tengwar mode

Recovered 2026-07-05 from git history: the 2021 manual's `tengwar.tex` and `orthography.tex` (extracted from commit `fde058a`, paths `old/latex/source/`), decoded from the ConScript Unicode Registry codepoints embedded in the source. This is design material, not canon — the mode predates parts of current Phi, and the modernization agenda at the end lists every known gap. The raw recovered sources sit in `recovered/`.

## The mode in brief

Phi is written in its own Tengwar mode — the Phi mode — with two deliberate departures from the classical modes. First, a modified r-rule (below). Second, and defining: **no vowel carriers, ever**. Where a word carries two vowels in hiatus, the first tehta sits above the preceding consonant's tengwa and the second tehta sits below the same tengwa. Each tengwa is read: consonant, then the vowel above, then the vowel below.

Two facts of Phi phonology make this mode airtight, and neither was true of Quenya. Every Phi word begins with a consonant, so no word ever needs a carrier at its head. And the three-vowel constraint means no more than two vowels ever stand in sequence, so above-plus-below always suffices — one tengwa can carry everything the phonology allows to follow its consonant. The script and the sound rules agree perfectly; the mode is not an adaptation so much as a fit.

The result is remarkably compact. Six-letter *lothea* takes two tengwar. Particles and pronouns are almost always a single tengwa with tehtar. The digraphs ph, th, sh, wh — two letters each in romanization — are one tengwa each.

## Consonant tengwar

| Grapheme | Tengwa | CSUR codepoint | Keypress |
|---|---|---|---|
| p | parma | U+E001 | p |
| t | tinco | U+E000 | t |
| m | malta | U+E011 | m |
| n | númen | U+E010 | n |
| r (word-initial, trilled [r]) | rómen | U+E020 | r |
| r (word-internal, tapped [ɾ]) | órë | U+E014 | shift-r |
| ph | formen | U+E009 | shift-p |
| wh | hwesta | U+E00B | shift-k |
| th | thúlë | U+E008 | shift-t |
| s | silmë | U+E024 | s |
| s (alternate) | silmë nuquerna | U+E025 | shift-s |
| sh | harma | U+E00A | shift-c |
| h | hyarmen | U+E028 | h |
| w | vala | U+E015 | w |
| l | lambë | U+E022 | l |

Two rules govern the doubled rows. The two silmë forms are the writer's choice: whichever form sits more comfortably under the word's tehtar — the classical Quenya convention, kept. The two r forms are not a choice: word-initial r is always the trill and always rómen; word-internal r is always the tap and always órë. (The classical modes split rómen/órë by pre-vocalic versus final position; the Phi mode repurposes the pair for its trill/tap allophony.)

## Vowel tehtar

| Grapheme | Above form (first vowel) | Below form (second vowel) | Keypress |
|---|---|---|---|
| a | U+E040 | U+E041 | a / option-a |
| e | U+E046 | U+E047 | e / option-e |
| i | U+E044 | U+E045 | i / option-i |
| o | U+E04A | U+E04B | o / option-o |
| u | U+E04C | U+E04D | u / option-u |

Keypresses are for the Tengwar Telcontar keyboard layout on macOS; Windows uses ctrl-alt in place of option. The above form marks a vowel read directly after the consonant; the below form marks the hiatus vowel that follows it.

## The hiatus rule, worked

*lothea* = lo·the·a, and in the mode:

| Tengwa | Carries | Reads |
|---|---|---|
| lambë (E022) | o above (E04A) | lo |
| thúlë (E008) | e above (E046), a below (E041) | the·a |

Two tengwar, six letters, and the hiatus is visible: the reader sees the a hanging below thúlë and knows it is its own syllable — the below position *is* the hiatus mark. The same works for any pair: *lohau* is lambë(o) + hyarmen(a above, u below). Nothing is ever ambiguous, because the phonology guarantees the reading order exhausts the possibilities.

## Punctuation and spacing

| Romanization | Tengwar form | Keypress |
|---|---|---|
| space | ⸱ word separator (U+2E31) | , |
| period | tengwar double-dot (rendered from :) | shift-, |

The original manual also mentions optional word markers for clarity in long multisyllabic words. Note the fit with the 2026 punctuation ruling (canon: the period is Phi's only visible punctuation): the mode adds no punctuation romanization lacks — the separator is the Tengwar *form of the space*, and the double-dot is the form of the period. Mode-invariance holds: both modes carry exactly the same information.

## Decoded examples from the original manual

The 2021 source embeds three specimens, recovered codepoint by codepoint:

1. *lothea* — lambë(o) thúlë(e, a-below). As above.
2. *mia thi lothea* ("I love you," informal) — malta(i, a-below) · thúlë(i) · lambë(o) thúlë(e, a-below). Note the 2021 grammar: second person was *thi*; today it is *thia*, one more below-tehta.
3. The "formal" variant *si mia na thi te lothea* used the era's part-of-speech marking particles (*si*, *na*, *te* as noun/verb markers). That grammar is long gone — *si*, *na*, and *te* now mean IPFV, necessity, and cessative — so this specimen is purely historical.

## Tooling

The font is Tengwar Telcontar (freetengwar.sourceforge.net), a Unicode/Graphite font using the CSUR tengwar block; correct rendering needs a Graphite-aware application. The same project provides the keyboard layout the keypress columns assume. An Obsidian CSS snippet (`.tengwar` class) is in `recovered/`. Binaries were deliberately not re-committed; recover them from history at will:

```
git show fde058a:old/latex/fonts/tengtelc.ttf  > tengtelc.ttf
git show fde058a:old/latex/fonts/tengtelcb.ttf > tengtelcb.ttf
git show fde058a:old/latex/source/manual.pdf   > manual.pdf
```

## Modernization rulings (settled 2026-07-05)

The 2021 mode met current Phi, and Daniel ruled on every gap:

1. **k = calma (U+E002)** — the classical [k], keeping quessë free.
2. **u-initial hiatus pairs** (*lue*, *mua*, *muila*, *nuola* …) are confirmed mechanical: u above, second vowel below; the 2021 pair table is superseded by the general rule.
3. **The r-rule stays positional in writing**: word-initial r is always rómen, internal r always órë — the written mode is stricter than the free trill/tap variation `documents/phonetics.md` allows in speech.
4. **Plain spacing between words.** The ⸱ separator remains a documented calligraphic option; the site renders bare space. The double pusta remains the period.
5. **The silmë choice is resolved by structure**: every Phi s carries a tehta (all syllables are open), so the rendered mode uses silmë nuquerna throughout — plain silmë remains for calligraphy.

## The renderer

The full-corpus test (old agenda item 5) is live: every Phi line on the texts shelf is rendered to Tengwar at build time and the shelf's `tengwar` toggle switches scripts. The pipeline is pure geometry — no shaping engine, so it is identical in every browser:

- `writing_systems/fonts/` — Tengwar Formal CSUR 1.1, vendored under its SIL OFL 1.1 license (see `OFL.txt`).
- `scripts/extract_tengwar_glyphs.py` — one-off: pulls the mode's 28 glyph outlines, advances, and boxes into `writing_systems/tengwar_glyphs.json` (committed, so CI needs no font tooling).
- `scripts/tengwar.py` — parses romanized Phi into (tengwa, above, below) units per this mode and assembles self-contained SVG (`currentColor` fill, so the theme toggle applies).
- `scripts/build_explorer.py` — wraps each Phi line in the texts as romanization plus SVG; `web/tengwar.js` remembers the reader's choice.
