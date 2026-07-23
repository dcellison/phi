# The Phi Tengwar mode

Write `lothea` in romanization and it occupies six letters. Write the same word in Tengwar and it occupies two tengwar. The first carries `l` with `o` above it. The second carries `th` with `e` above and the separate `a` below. Nothing has been abbreviated: the mode has simply gathered each consonant and the vowel or vowels that follow it into one written unit.

Phi has two current writing modes, romanization and Tengwar. They carry the same words, word boundaries, and period. Capitalization does not exist in either mode, and Tengwar adds no grammatical distinction of its own.

## Reading a unit

Each tengwa is read in this order:

1. the consonant;
2. the vowel above it;
3. the vowel below it, if present.

Phi words always begin with a consonant, so an initial vowel carrier is never needed. No legal Phi word places more than two vowels together, so the above and below positions can hold every permitted sequence. A vowel below a tengwa is therefore not silent ornament: it is the second vowel in hiatus.

## Consonant tengwar

| Romanization | Tengwa | CSUR codepoint | Tengwar Telcontar keypress |
|---|---|---|---|
| `p` | parma | `U+E001` | `p` |
| `t` | tinco | `U+E000` | `t` |
| `k` | calma | `U+E002` | `c` |
| `m` | malta | `U+E011` | `m` |
| `n` | númen | `U+E010` | `n` |
| `r` at the start of a word | rómen | `U+E020` | `r` |
| `r` inside a word | órë | `U+E014` | `shift-r` |
| `ph` | formen | `U+E009` | `shift-p` |
| `th` | thúlë | `U+E008` | `shift-t` |
| `sh` | harma | `U+E00A` | `shift-c` |
| `wh` | hwesta | `U+E00B` | `shift-k` |
| `s` | silmë nuquerna | `U+E025` | `shift-s` |
| `h` | hyarmen | `U+E028` | `h` |
| `w` | vala | `U+E015` | `w` |
| `l` | lambë | `U+E022` | `l` |

The choice between rómen and órë follows position, not pronunciation. An `r` at the beginning of a word is rómen; any later `r` is órë. A speaker may tap or trill either one without changing the spelling.

The working mode uses silmë nuquerna for every `s`. Every Phi syllable is open, so every `s` must carry a vowel tehta; the reversed form leaves that tehta room. Plain silmë (`U+E024`, keypress `s`) remains available as a calligraphic alternative.

## Vowel tehtar

| Vowel | Above form | Below form | Tengwar Telcontar keypresses |
|---|---|---|---|
| `a` | `U+E040` | `U+E041` | `a` / `option-a` |
| `e` | `U+E046` | `U+E047` | `e` / `option-e` |
| `i` | `U+E044` | `U+E045` | `i` / `option-i` |
| `o` | `U+E04A` | `U+E04B` | `o` / `option-o` |
| `u` | `U+E04C` | `U+E04D` | `u` / `option-u` |

These keypresses follow the [Free Tengwar Font Project keyboard layout](https://freetengwar.sourceforge.net/keylayouts.html) on macOS. On Windows, the layout uses `ctrl-alt` in place of `option`. The above form is the first vowel after a consonant. The below form is used only for the second vowel of a hiatus pair.

## A worked word

`lothea` divides as `lo.the.a`.

| Tengwa | Marks | Reading |
|---|---|---|
| lambë | `o` above | `lo` |
| thúlë | `e` above, `a` below | `the.a` |

The reader sees two written units and hears three syllables. The `a` below thúlë makes the hiatus visible without adding a carrier.

## Spacing and punctuation

Words normally take plain spaces. A writer may instead use the raised dot `⸱` (`U+2E31`) as a calligraphic word separator. It carries no distinction that an ordinary space lacks.

The period is written as the Tengwar double pusta (`U+E061`). Phi has no other visible punctuation. Questions, quotation boundaries, direct address, and other relations remain spoken words in both writing modes.

## Source material

The mode renders grammatical Phi, including productive Phi-form names introduced by `ne`. Foreign wording, source-script names, exact records, identifiers, and other unassimilated source material remain outside the Phi passage and retain their own script.

## Implementation

| Path | Role |
|---|---|
| [`glyphs.json`](glyphs.json) | The 28 committed outlines, advances, bounding boxes, and placement adjustments used at build time. |
| [`fonts/TengwarTelcontar.ttf`](fonts/TengwarTelcontar.ttf) | The GPL-licensed [Tengwar Telcontar 0.08](https://freetengwar.sourceforge.net/tengtelc.html) source font by Johan Winge. |
| [`scripts/tengwar.py`](../scripts/tengwar.py) | The renderer that parses validated romanized Phi and assembles self-contained SVG. |
| [`scripts/extract_tengwar_glyphs.py`](../scripts/extract_tengwar_glyphs.py) | The manual extraction tool used when the committed outline data must be rebuilt. |

The renderer uses plain word spacing, silmë nuquerna throughout, and the positional rómen/órë rule. It draws from `glyphs.json`, so ordinary builds need neither the font nor a shaping engine. The site shows paired Tengwar and romanized lines in the [Tengwar pamphlet](../pamphlets/tengwar_mode/); other shelves remain in romanization.
