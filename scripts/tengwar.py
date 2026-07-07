"""Render romanized Phi as Tengwar SVG, per the Phi mode
(writing_systems/tengwar_mode.md). Pure geometry over the glyph outlines in
writing_systems/tengwar_glyphs.json - no font tooling, no shaping engine, so
the output renders identically in every browser.

Mode decisions encoded here (ruled 2026-07-05): k = calma; word-initial r =
romen, internal r = ore; s = silme nuquerna throughout (every Phi s carries a
tehta, which is what the nuquerna form is for); plain word spacing; the
period is the tengwar double pusta.
"""
import json
import re
from pathlib import Path

_DATA = json.loads((Path(__file__).resolve().parent.parent /
                    "writing_systems" / "tengwar_glyphs.json").read_text())
_G = _DATA["glyphs"]

TENGWA = {"p": "E001", "t": "E000", "k": "E002", "m": "E011", "n": "E010",
          "ph": "E009", "wh": "E00B", "th": "E008", "sh": "E00A",
          "s": "E025", "h": "E028", "w": "E015", "l": "E022"}
R_INITIAL, R_MEDIAL = "E020", "E014"
ABOVE = {"a": "E040", "i": "E044", "e": "E046", "o": "E04A", "u": "E04C"}
BELOW = {"a": "E041", "i": "E045", "e": "E047", "o": "E04B", "u": "E04D"}
DOUBLE_PUSTA = "E061"

_UNIT = re.compile(r"(ph|th|sh|wh|[hklmnprstw])([aeiou]{1,2})")
WORD_GAP = 520
CLEAR = 100


def parse_word(word):
    """Word -> [(tengwa_key, above_key, below_key|None)]; None if not
    parseable as Phi (foreign token, gloss line, etc.)."""
    units, pos = [], 0
    for m in _UNIT.finditer(word):
        if m.start() != pos:
            return None
        onset, vowels = m.group(1), m.group(2)
        if onset == "r":
            base = R_INITIAL if m.start() == 0 else R_MEDIAL
        else:
            base = TENGWA[onset]
        units.append((base, ABOVE[vowels[0]],
                      BELOW[vowels[1]] if len(vowels) > 1 else None))
        pos = m.end()
    return units if units and pos == len(word) else None


def _place(placed, key, x, dx=0.0, dy=0.0):
    g = _G[key]
    bb = g["bbox"]
    placed.append((key, x + dx, dy))
    return [bb[0] + x + dx, bb[1] + dy, bb[2] + x + dx, bb[3] + dy]


def _tehta(placed, key, base_key, x, above):
    """Center the zero-advance tehta over the base glyph's ink, keeping the
    font's own vertical position unless the base's ink collides. `above`
    says which side this tehta belongs on (from the ABOVE/BELOW dicts, not
    inferred from the glyph's own bbox: a font may draw an "above" mark
    with ink that dips slightly below the baseline, which would fool a
    sign-of-bbox check)."""
    base, teh = _G[base_key], _G[key]
    pen = x + base["adv"]
    dx = ((x + (base["bbox"][0] + base["bbox"][2]) / 2)
          - (pen + (teh["bbox"][0] + teh["bbox"][2]) / 2))
    dy = 0.0
    if above:  # lift clear of tall bases
        overlap = base["bbox"][3] + CLEAR - teh["bbox"][1]
        if overlap > 0:
            dy = overlap
    else:      # drop clear of descenders
        overlap = teh["bbox"][3] + CLEAR - base["bbox"][1]
        if overlap > 0:
            dy = -overlap
    return _place(placed, key, pen, dx, dy)


def render_line(line):
    """One Phi line (periods only, lowercase, brackets tolerated) -> SVG
    string, or None if any word fails to parse."""
    placed, boxes, x = [], [], 0.0
    for token in line.split():
        word = token.strip("[]")
        stops = word.count(".")
        word = word.strip(".").strip("[]")
        if word:
            units = parse_word(word)
            if units is None:
                return None
            for base, above, below in units:
                boxes.append(_place(placed, base, x))
                boxes.append(_tehta(placed, above, base, x, above=True))
                if below:
                    boxes.append(_tehta(placed, below, base, x, above=False))
                x += _G[base]["adv"]
            x += WORD_GAP
        for _ in range(stops):
            boxes.append(_place(placed, DOUBLE_PUSTA, x))
            x += _G[DOUBLE_PUSTA]["adv"] + WORD_GAP
    if not placed:
        return None
    xmin = min(b[0] for b in boxes) - 40
    xmax = max(b[2] for b in boxes) + 40
    ymin = min(b[1] for b in boxes) - 40
    ymax = max(b[3] for b in boxes) + 40
    parts = [f'<path transform="translate({gx:.0f} {gy:.0f})" d="{_G[k]["path"]}"/>'
             for k, gx, gy in placed]
    w, h = xmax - xmin, ymax - ymin
    return (f'<svg class="teng-svg" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{xmin:.0f} {-ymax:.0f} {w:.0f} {h:.0f}" '
            f'style="height:{h / _DATA["upem"]:.2f}em" fill="currentColor">'
            f'<g transform="scale(1,-1)">{"".join(parts)}</g></svg>')


def phi_line(line, words):
    """Heuristic: is this (fenced, unescaped) line a Phi line?"""
    toks = [t.strip("[].,") for t in line.split()]
    toks = [t for t in toks if t]
    if len(toks) < 2 or any(t != t.lower() for t in toks):
        return False
    known = sum(1 for t in toks if t in words)
    return known >= max(2, (len(toks) * 4) // 5)
