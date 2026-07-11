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

import name_forms

_DATA = json.loads((Path(__file__).resolve().parent.parent /
                    "writing_systems" / "tengwar_glyphs.json").read_text())
_G = _DATA["glyphs"]

# Manual per-base-glyph position corrections, keyed by the base tengwa's
# codepoint, then "above"/"below", each a {"dx": x, "dy": y} offset added
# on top of the plain bbox placement in _tehta() (positive dx is right,
# positive dy is up, both in font design units, upem 2048). A slot may
# also carry a "by_vowel" dict, keyed by the tehta's own codepoint (e.g.
# "E04A" for o-above), overriding dx/dy for that one vowel; vowels not
# listed fall back to the slot's own dx/dy. This exists because vowels
# differ enough in size and shape that one offset per base letter can't
# fit all of them: o (a wide diagonal swoosh) needs far more vertical
# clearance from an ascender's hook than a (a compact diamond cluster)
# does, and forcing them to share a height either buries o in the hook
# or floats a way off above the letter. Empty entries just mean the
# plain placement hasn't been checked against a reference yet, not that
# it's known correct. Add one at a time, informed by an actual rendered
# comparison - see writing_systems/tengwar_mode.md and
# [[tengwar-telcontar-swap]] in memory for the story of why this exists
# (automated per-glyph shape analysis was tried and abandoned: it kept
# finding a new letter shape it got wrong) and for th specifically, the
# standing correction: center it above the hump, not the mast, then
# nudge right by roughly the stem's own width so it clears the stem
# instead of sitting on top of it.
TWEAKS = _DATA.get("tweaks", {})

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
    """Center the zero-advance tehta over the base glyph's bbox, and set
    its height clear of the base's own bbox top/bottom. `above` says which
    side this tehta belongs on (from the ABOVE/BELOW dicts, not inferred
    from the glyph's own bbox, which a font's isolated-mark design can
    leave meaningless as an absolute position, e.g. this font's tehtar all
    carry a native y-position left over from sitting inside a composite
    with a display circle - see extract_tengwar_glyphs.py).

    This is deliberately plain bbox math with no per-glyph shape analysis:
    an earlier attempt to derive placement from each base's actual stem/
    bow geometry kept finding a new letter shape it got wrong (overlapping
    the very stem it was trying to clear, for one). Letters whose bbox
    isn't a good proxy for where a tehta should sit (mainly the ones with
    a decorative ascender or descender well beyond their own body) get a
    manual correction from TWEAKS instead of an automated one; see there
    for how to add one and what's already been dialed in."""
    base, teh = _G[base_key], _G[key]
    pen = x + base["adv"]
    dx = ((x + (base["bbox"][0] + base["bbox"][2]) / 2)
          - (pen + (teh["bbox"][0] + teh["bbox"][2]) / 2))
    dy = (base["bbox"][3] + CLEAR - teh["bbox"][1] if above
          else base["bbox"][1] - CLEAR - teh["bbox"][3])
    slot = TWEAKS.get(base_key, {}).get("above" if above else "below")
    if slot:
        tweak = slot.get("by_vowel", {}).get(key, slot)
        dx += tweak.get("dx", 0)
        dy += tweak.get("dy", 0)
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
    name_indices = name_forms.marked_atom_indices(toks)
    known = sum(
        1 for index, token in enumerate(toks)
        if token in words
        or (index in name_indices and not name_forms.form_errors(token))
    )
    return known >= max(2, (len(toks) * 4) // 5)
