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
    """Convert the repo's constrained Markdown (headings, paragraphs,
    blockquotes, tables, lists, fenced code, hr, inline marks) to HTML."""
    # fenced code blocks survive as-is: lift them out before splitting
    fences = []
    def lift(m):
        inner = m.group(1).strip("\n")
        inner = inner.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        fences.append(f"<pre>{inner}</pre>")
        return f"\x00FENCE{len(fences)-1}\x00"
    md = re.sub(r"```[a-z]*\n(.*?)```", lift, md, flags=re.S)
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
        elif block.startswith("### "):
            out.append(f"<h3>{inline(block[4:])}</h3>")
        elif block.startswith("## "):
            out.append(f"<h2>{inline(block[3:])}</h2>")
        elif block == "---":
            out.append("<hr>")
        elif block.startswith("\x00FENCE"):
            out.append(fences[int(block.strip("\x00").replace("FENCE", ""))])
        elif re.match(r"^[-*] ", block):
            items = re.split(r"\n(?=[-*] )", block)
            out.append("<ul>" + "".join(f"<li>{inline(i[2:].strip())}</li>" for i in items) + "</ul>")
        elif re.match(r"^\d+\. ", block):
            items = re.split(r"\n(?=\d+\. )", block)
            out.append("<ol>" + "".join(f"<li>{inline(re.sub(r'^[0-9]+[.] ', chr(39)+chr(39), i).strip() if False else re.sub(r'^\d+\. ', '', i).strip())}</li>" for i in items) + "</ol>")
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
            text = "\n".join(l.lstrip("> ") for l in block.splitlines())
            out.append("<blockquote>" + inline(text).replace("\n", "<br>") + "</blockquote>")
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
                    '<strong><a href="manual/index.html">Verify</a></strong>')
body = body.replace("<strong>Read</strong>",
                    '<strong><a href="texts/index.html">Read</a></strong>')
landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi — kia</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing">
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
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
            return re.sub(r"[*`]", "", line[2:]).strip()
    return "untitled"

NAV_PRIMER = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <span class="here">primer</span> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def primer_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi primer &mdash; {title}</title>
<script src="../theme.js"></script>
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

# ---- manual reader: manual/**.md rendered to web/manual/ ----
MANUAL_SRC = ROOT / "manual"
MANUAL_OUT = ROOT / "web" / "manual"
MANUAL_OUT.mkdir(parents=True, exist_ok=True)

def pretty(name, kind):
    m = re.match(r"(?:part|ch|appendix_)?(\w+?)_(.*)", name) if kind != "part" else re.match(r"part(\d+)_(.*)", name)
    if kind == "part":
        num, rest = re.match(r"part(\d+)_(.*)", name).groups()
        return f"Part {num} \u00b7 " + rest.replace("_", " ")
    if kind == "chapter":
        mm = re.match(r"ch(\d+)_(.*)", name)
        if mm:
            return f"Chapter {int(mm.group(1))} \u00b7 " + mm.group(2).replace("_", " ")
        return name.replace("_", " ")
    return name.replace("_", " ")

NAV_MANUAL = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <span class="here">manual</span> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def manual_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi manual &mdash; {title}</title>
<script src="../theme.js"></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="landing primer">
{NAV_MANUAL}
<main>
{body}
{footer_nav}
</main>
<footer>
  <p>The manual is written in the repository and rendered here at build time &mdash;
     <a href="https://github.com/dcellison/phi/tree/main/manual">the source</a> is the reference.</p>
</footer>
</body>
</html>
"""

# reading order: numbered parts, then appendices, then the reference
# extras; exclude working docs and the lexicon reference (the explorer
# covers it)
sections = []  # (group_label, chapter_label, path)
part_dirs = sorted(d for d in MANUAL_SRC.iterdir() if d.is_dir() and d.name.startswith("part"))
for d in part_dirs:
    label = pretty(d.name, "part")
    if d.name == "part7_reference":
        for f in sorted(d.glob("*.md")):
            sections.append((label, None, f))
        continue
    for ch in sorted(x for x in d.iterdir() if x.is_dir()):
        ch_label = pretty(ch.name, "chapter")
        for f in sorted(ch.glob("*.md")):
            sections.append((label, ch_label, f))
app = MANUAL_SRC / "appendices"
if app.is_dir():
    for f in sorted(app.glob("*.md")):
        sections.append(("Appendices", None, f))

def slug(path):
    rel = path.relative_to(MANUAL_SRC)
    return str(rel.with_suffix("")).replace("/", "__") + ".html"

sec_titles = [title_of(f.read_text()) for _, _, f in sections]
for i, (part, ch, f) in enumerate(sections):
    crumb_bits = [part] + ([ch] if ch else [])
    crumb = '<p class="crumb">' + " &mdash; ".join(crumb_bits) + "</p>"
    body = crumb + md_to_html(f.read_text())
    prev_link = f'<a href="{slug(sections[i-1][2])}">&lsaquo; {sec_titles[i-1]}</a>' if i > 0 else ""
    next_link = f'<a href="{slug(sections[i+1][2])}">{sec_titles[i+1]} &rsaquo;</a>' if i + 1 < len(sections) else ""
    footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    (MANUAL_OUT / slug(f)).write_text(manual_page(body, sec_titles[i], footer_nav))

# contents page grouped by part and chapter
toc = ["<h1>The Phi manual</h1>",
       "<p>The complete reference, rendered from the repository. Read it in order or dip in anywhere; the primer is the gentler road, and the lexicon holds every word.</p>"]
cur_part = cur_ch = None
open_list = False
for i, (part, ch, f) in enumerate(sections):
    if part != cur_part:
        if open_list: toc.append("</ol>"); open_list = False
        toc.append(f"<h2>{part}</h2>"); cur_part, cur_ch = part, None
    if ch != cur_ch and ch is not None:
        if open_list: toc.append("</ol>"); open_list = False
        toc.append(f"<h3 class=\"toc-ch\">{ch}</h3>"); cur_ch = ch
    if not open_list:
        toc.append("<ol class=\"toc\">"); open_list = True
    toc.append(f'<li><a href="{slug(f)}">{sec_titles[i]}</a></li>')
if open_list: toc.append("</ol>")
(MANUAL_OUT / "index.html").write_text(manual_page("\n".join(toc), "contents"))
print(f"wrote web/manual/: {len(sections)} sections + contents")

# ---- the texts: transmuted literature rendered to web/texts/ ----
TEXTS_OUT = ROOT / "web" / "texts"
TEXTS_OUT.mkdir(parents=True, exist_ok=True)
NAV_TEXTS = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <span class="here">texts</span> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def texts_page(body, title):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phi texts &mdash; {title}</title>
<script src="../theme.js"></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="landing primer">
{NAV_TEXTS}
<main>
{body}
<div class="chapnav"><a href="index.html">all texts</a></div>
</main>
<footer>
  <p>Transmutations, not translations: each text is rebuilt from Phi's own
     concepts. Written in <a href="https://github.com/dcellison/phi/tree/main/pamphlets">the repository</a>, rendered at build time.</p>
</footer>
</body>
</html>
"""

TEXTS = [
    ("metta_sutta", "The Metta Sutta", "The first text ever written in Phi: the loving-kindness meditation, rebuilt from the language's own concepts. Where the language's heart is."),
    ("north_wind_and_sun", "The North Wind and the Sun", "Phi's first story: the fable told in a thousand languages to show what each sounds like. The primer's capstone sends its readers here."),
]
for stem, title, blurb in TEXTS:
    md = (ROOT / "pamphlets" / f"{stem}.md").read_text()
    (TEXTS_OUT / f"{stem}.html").write_text(texts_page(md_to_html(md), title))

toc = ["<h1>The texts</h1>",
       "<p>Phi's literature so far. Each is a transmutation &mdash; not a translation word for word, but the idea rebuilt from Phi's own concepts, with notes recording every adaptation the language asked for.</p>"]
for stem, title, blurb in TEXTS:
    toc.append(f'<h2><a href="{stem}.html">{title}</a></h2><p>{blurb}</p>')
toc.append("<hr><p><em>More transmutations are coming; the shelf is built to grow.</em></p>")
(TEXTS_OUT / "index.html").write_text(texts_page("\n".join(toc), "contents"))
print(f"wrote web/texts/: {len(TEXTS)} texts + contents")
