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
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
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
        elif block.startswith("|"):
            rows = [r for r in block.splitlines() if r.strip()]
            html = ["<table>"]
            for i, row in enumerate(rows):
                if set(row.replace("|", "").strip()) <= set("-: "):
                    continue
                cells = [inline(c.strip()) for c in row.strip("|").split("|")]
                tag = "th" if i == 0 and len(rows) > 1 and set(rows[1].replace("|","").strip()) <= set("-: ") else "td"
                html.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
            html.append("</table>")
            out.append("".join(html))
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
                    '<strong><a href="primer/index.html">Begin</a></strong>')
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
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="https://github.com/dcellison/phi/tree/main/manual">manual</a></nav>
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

# ---- primer reader: primer/*.md rendered to web/primer/ ----
PRIMER_SRC = ROOT / "primer"
PRIMER_OUT = ROOT / "web" / "primer"
PRIMER_OUT.mkdir(parents=True, exist_ok=True)

def title_of(md):
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "untitled"

NAV_PRIMER = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <span class="here">primer</span> <span class="sep">&middot;</span> <a href="https://github.com/dcellison/phi/tree/main/manual">manual</a></nav>'

def primer_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi primer &mdash; {title}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body class="landing primer">
{NAV_PRIMER}
<main>
{body}
{footer_nav}
</main>
<footer>
  <p>The primer is written in the repository and rendered here at build time &mdash;
     <a href="https://github.com/dcellison/phi/tree/main/primer">the source</a> is the book.</p>
</footer>
</body>
</html>
"""

chapters = sorted(f for f in PRIMER_SRC.glob("*.md") if f.name != "README.md")
titles = {f.name: title_of(f.read_text()) for f in chapters}
for i, f in enumerate(chapters):
    md = f.read_text()
    body = md_to_html(md)
    prev_link = f'<a href="{chapters[i-1].stem}.html">&lsaquo; {titles[chapters[i-1].name]}</a>' if i > 0 else ""
    next_link = f'<a href="{chapters[i+1].stem}.html">{titles[chapters[i+1].name]} &rsaquo;</a>' if i + 1 < len(chapters) else ""
    footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    (PRIMER_OUT / (f.stem + ".html")).write_text(primer_page(body, titles[f.name], footer_nav))

# contents page: the primer README plus a generated reading list
readme_body = md_to_html((PRIMER_SRC / "README.md").read_text())
toc = ["<h2>Read</h2><ol class=\"toc\">"]
for f in chapters:
    toc.append(f'<li><a href="{f.stem}.html">{titles[f.name]}</a></li>')
toc.append("</ol>")
(PRIMER_OUT / "index.html").write_text(primer_page(readme_body + "\n" + "".join(toc), "contents"))
print(f"wrote web/primer/: {len(chapters)} chapters + contents")
