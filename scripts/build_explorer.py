"""Build the explorer's generated files: web/lexicon.json from the
vocabulary, and web/index.html (the landing page) from kia.md.

Generated output; not committed. Run before serving web/ locally:
    python3 scripts/build_explorer.py
    python3 -m http.server -d web
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["word", "gloss", "ipa", "syllables", "slot", "pos", "concept",
          "description", "sound_symbolism", "grammatical_notes", "pillars", "tags"]

entries = []
for p in sorted((ROOT / "vocabulary").rglob("*.json")):
    d = json.loads(p.read_text())
    e = {k: d[k] for k in FIELDS if k in d}
    e["kind"] = p.parent.name if p.parent.name != "content" else "content"
    entries.append(e)

entries.sort(key=lambda e: e["word"])
out = ROOT / "web" / "lexicon.json"
out.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {out.relative_to(ROOT)}: {len(entries)} entries, {out.stat().st_size // 1024} KB")

# ---- landing page: kia.md rendered to web/index.html ----
import re

def md_to_html(md):
    """Convert kia.md's constrained Markdown (h1/h2, paragraphs,
    blockquotes, hr, bold, italic) to HTML."""
    def inline(s):
        s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        return s
    out = []
    for block in md.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("# "):
            out.append(f"<h1>{inline(block[2:])}</h1>")
        elif block.startswith("## "):
            out.append(f"<h2>{inline(block[3:])}</h2>")
        elif block == "---":
            out.append("<hr>")
        elif block.startswith(">"):
            lines = [inline(l.lstrip("> ")) for l in block.splitlines()]
            out.append("<blockquote>" + "<br>".join(lines) + "</blockquote>")
        else:
            out.append(f"<p>{inline(block)}</p>")
    return "\n".join(out)

kia = (ROOT / "kia.md").read_text()
body = md_to_html(kia)
# the three doors become links: explorer here, primer and manual on GitHub
body = body.replace("<strong>Wander</strong>",
                    '<strong><a href="explore.html">Wander</a></strong>')
body = body.replace("<strong>Begin</strong>",
                    '<strong><a href="https://github.com/dcellison/phi/tree/main/primer">Begin</a></strong>')
body = body.replace("<strong>Verify</strong>",
                    '<strong><a href="https://github.com/dcellison/phi/tree/main/manual">Verify</a></strong>')
landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi — kia</title>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing">
<nav class="topnav"><span class="here">kia</span><a href="explore.html">lexicon</a><a href="https://github.com/dcellison/phi/tree/main/primer">primer</a><a href="https://github.com/dcellison/phi/tree/main/manual">manual</a></nav>
<main>
{body}
<p class="doorlink"><a href="explore.html">Enter the lexicon &rarr;</a></p>
</main>
<footer>
  <p>The lexicon is the single source of truth &mdash; this site is a view over
     <a href="https://github.com/dcellison/phi">the repository</a>. This page is kia.md, rendered.</p>
</footer>
</body>
</html>
"""
(ROOT / "web" / "index.html").write_text(landing)
print(f"wrote web/index.html from kia.md ({len(body.splitlines())} blocks)")
