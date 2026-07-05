"""One-off extraction: pull the Phi mode's glyph outlines out of Tengwar
Formal CSUR (writing_systems/fonts/, SIL OFL 1.1) into a committed JSON so
the site build needs no font tooling. Requires fontTools; run manually:

    python3 -m venv /tmp/ftenv && /tmp/ftenv/bin/pip install fonttools
    /tmp/ftenv/bin/python scripts/extract_tengwar_glyphs.py
"""
import json
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "writing_systems" / "fonts" / "TengwarFormalCSUR.ttf"
OUT = ROOT / "writing_systems" / "tengwar_glyphs.json"

# The Phi mode's full inventory: 16 tengwar, 5 above-tehtar, 5 below-tehtar,
# the double pusta (the period), and the pusta (documented calligraphic
# separator, extracted for completeness).
CODEPOINTS = [
    0xE000, 0xE001, 0xE002, 0xE008, 0xE009, 0xE00A, 0xE00B,
    0xE010, 0xE011, 0xE014, 0xE015, 0xE020, 0xE022, 0xE024, 0xE025, 0xE028,
    0xE040, 0xE041, 0xE044, 0xE045, 0xE046, 0xE047, 0xE04A, 0xE04B, 0xE04C, 0xE04D,
    0xE060, 0xE061,
]

font = TTFont(FONT)
cmap = font.getBestCmap()
glyf = font.getGlyphSet()
hmtx = font["hmtx"]

glyphs = {}
for cp in CODEPOINTS:
    name = cmap[cp]
    g = glyf[name]
    sp = SVGPathPen(glyf)
    g.draw(sp)
    bp = BoundsPen(glyf)
    g.draw(bp)
    glyphs[f"{cp:04X}"] = {
        "name": name,
        "path": sp.getCommands(),
        "adv": hmtx[name][0],
        "bbox": list(bp.bounds) if bp.bounds else [0, 0, 0, 0],
    }

out = {
    "source": "Tengwar Formal CSUR 1.1 (freetengwar.sourceforge.net)",
    "license": "SIL Open Font License 1.1 - see writing_systems/fonts/OFL.txt",
    "upem": font["head"].unitsPerEm,
    "ascent": font["hhea"].ascent,
    "descent": font["hhea"].descent,
    "glyphs": glyphs,
    "tweaks": {},
}
OUT.write_text(json.dumps(out, indent=1))
print(f"wrote {OUT.relative_to(ROOT)}: {len(glyphs)} glyphs, upem {out['upem']}")
