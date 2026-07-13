"""Build the explorer's generated files: web/lexicon.json from the
vocabulary, and web/index.html (the landing page) from kia.md.

Generated output; not committed. Run before serving web/ locally:
    python3 scripts/build_explorer.py
    python3 -m http.server -d web
"""
import html as html_module
import json
import re
from pathlib import Path

from compound_registry import load_compounds

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["word", "gloss", "ipa", "syllables", "slot", "pos", "concept",
          "description", "sound_symbolism", "grammatical_notes", "pillars", "tags",
          "modules"]


def prepare_html_output(path):
    """Create a generated HTML directory and remove obsolete pages."""
    path.mkdir(parents=True, exist_ok=True)
    for generated in path.glob("*.html"):
        generated.unlink()


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

# ---- compound registry: documents/compounds.md to web/compounds.json ----
ALL_WORDS = {e["word"] for e in entries}
CELL_MD = re.compile(r"`([^`]+)`|\*([^*]+)\*")

def cell_html(text):
    """A registry cell as safe HTML: backticked Phi becomes a .phi span
    (clickable when it is one lexicon word), *emphasis* becomes <em>."""
    def sub(m):
        if m.group(1) is not None:
            tok = html_module.escape(m.group(1))
            link = f' data-w="{tok}" role="link" tabindex="0"' if m.group(1) in ALL_WORDS else ""
            return f'<span class="phi"{link}>{tok}</span>'
        return f"<em>{html_module.escape(m.group(2))}</em>"
    parts, last = [], 0
    for m in CELL_MD.finditer(text):
        parts.append(html_module.escape(text[last:m.start()]))
        parts.append(sub(m))
        last = m.end()
    parts.append(html_module.escape(text[last:]))
    return "".join(parts)

compounds = [
    {"compound": c["compound"], "tokens": c["tokens"], "literal": c["literal"],
     "meaning": c["meaning"], "section": c["section"], "why_html": cell_html(c["why"])}
    for c in load_compounds()
]
comp_out = ROOT / "web" / "compounds.json"
comp_out.write_text(json.dumps(compounds, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {comp_out.relative_to(ROOT)}: {len(compounds)} compounds")

# ---- landing page: kia.md rendered to web/index.html ----

def md_to_html(md):
    """Convert the repo's constrained Markdown (headings, paragraphs,
    blockquotes, tables, lists, fenced code, hr, inline marks) to HTML."""
    # fenced code blocks survive as-is: lift them out before splitting
    fences = []
    def lift(m):
        inner = m.group(1).strip("\n")
        inner = "\n".join(
            html_module.escape(line, quote=False) for line in inner.splitlines()
        )
        fences.append(f"<pre>{inner}</pre>")
        return f"\x00FENCE{len(fences)-1}\x00"
    md = re.sub(r"```[a-z]*\n(.*?)```", lift, md, flags=re.S)
    # a fence may butt against following prose with a single newline;
    # give each placeholder its own block so both halves render
    md = re.sub(r"(\x00FENCE\d+\x00)", r"\n\n\1\n\n", md)
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
# the doors become links
body = body.replace("<strong>Walk</strong>",
                    '<strong><a href="short_road.html">Walk</a></strong>')
body = body.replace("<strong>Wander</strong>",
                    '<strong><a href="explore.html">Wander</a></strong>')
body = body.replace("<strong>Begin</strong>",
                    '<strong><a href="primer/index.html">Begin</a></strong>')
body = body.replace("<strong>Verify</strong>",
                    '<strong><a href="manual/index.html">Verify</a></strong>')
body = body.replace("<strong>Read</strong>",
                    '<strong><a href="texts/index.html">Read</a></strong>')
body = body.replace("<strong>Practice</strong>",
                    '<strong><a href="pamphlets/index.html">Practice</a></strong>')
landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi is a philosophical constructed language organized by modifier-first grammar and an unhurried practice of communication.">
<meta property="og:title" content="Phi — a language built to slow you down">
<meta property="og:description" content="A modifier-first organizing principle, regular forms, clear source boundaries, more than a thousand words, a primer, a manual, and literature already on the shelf.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dcellison.github.io/phi/">
<title>Phi — kia</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing">
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="short_road.html">short road</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
{body}
<p class="doorlink"><a href="explore.html">Enter the lexicon &rarr;</a></p>
</main>
<footer>
  <p>The lexicon is the single source of truth &mdash; this site is a view over
     <a href="https://github.com/dcellison/phi">the repository</a>. This page is kia.md, rendered.
     The <a href="colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""
(ROOT / "web" / "index.html").write_text(landing)
print(f"wrote web/index.html from kia.md ({len(body.splitlines())} blocks)")

# ---- colophon: colophon.md rendered to web/colophon.html ----

colophon_body = md_to_html((ROOT / "colophon.md").read_text())
colophon_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="How Phi is made: the designer, the instrument, and the rules between them.">
<title>Phi — colophon</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="topnav"><a href="index.html">kia</a> <span class="sep">&middot;</span> <a href="short_road.html">short road</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
{colophon_body}
</main>
<footer>
  <p>Signed at the end, in the old way. This page is colophon.md, rendered from
     <a href="https://github.com/dcellison/phi">the repository</a>.</p>
</footer>
</body>
</html>
"""
(ROOT / "web" / "colophon.html").write_text(colophon_page)
print("wrote web/colophon.html from colophon.md")

# ---- the short road: short_road.md rendered to web/short_road.html ----

short_road_body = md_to_html((ROOT / "short_road.md").read_text())
short_road_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The whole of Phi at walking pace: one rule, thirty-five particles, ternary numbers, the sun's clock, and a shelf of literature, in twenty minutes.">
<title>Phi — the short road</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="topnav"><a href="index.html">kia</a> <span class="sep">&middot;</span> <a class="here" href="short_road.html">short road</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
{short_road_body}
</main>
<footer>
  <p>The whole language at walking pace. This page is short_road.md, rendered from
     <a href="https://github.com/dcellison/phi">the repository</a>.
     The <a href="colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""
(ROOT / "web" / "short_road.html").write_text(short_road_page)
print("wrote web/short_road.html from short_road.md")

# ---- primer reader: primer/*.md rendered to web/primer/ ----

def link_text_citations(html):
    """Repo-path citations of the texts become on-site links (pages
    using this all live one directory below web/)."""
    for stem in ("metta_sutta", "north_wind_and_sun", "human_rights_article_one", "babel_text", "ring_verse_refusal", "schleicher_fable", "little_prince_excerpts", "velveteen_rabbit"):
        html = html.replace(f"<code>pamphlets/{stem}.md</code>",
                            f'<a href="../texts/{stem}.html"><code>pamphlets/{stem}.md</code></a>')
        html = html.replace(f'href="../pamphlets/{stem}.md"',
                            f'href="../texts/{stem}.html"')
    html = re.sub(
        r'href="\.\./lexicon/by_module\.md#([a-z0-9-]+)"',
        lambda match: f'href="../explore.html?module={match.group(1)}"',
        html,
    )
    html = html.replace(
        "<code>documents/compounds.md</code>",
        '<a href="../manual/part7_reference__compounds.html"><code>documents/compounds.md</code></a>',
    )
    return html

def add_gloss_popovers(html):
    """Appendix A's Leipzig table carries a fourth column of longer
    explanations; lift it into each row so a click or hover reveals it
    without widening the visible table."""
    def do_table(m):
        table = m.group(0)
        rows = re.findall(r"<tr>(.*?)</tr>", table, re.S)
        if not rows or "Explanation" not in rows[0]:
            return table
        out = ["<table class=\"gloss-table\">"]
        out.append("<tr>" + "".join(f"<th>{c}</th>" for c in
                    re.findall(r"<th>(.*?)</th>", rows[0], re.S)[:3]) + "</tr>")
        for row in rows[1:]:
            cells = re.findall(r"<td>(.*?)</td>", row, re.S)
            first = (f'{cells[0]} <span class="glossmark" aria-hidden="true">&#9432;</span>'
                     f'<span class="gloss-pop">{cells[3]}</span>')
            out.append(f'<tr class="gloss-row" tabindex="0">'
                        f'<td>{first}</td><td>{cells[1]}</td><td>{cells[2]}</td></tr>')
        out.append("</table>")
        return "".join(out)
    return re.sub(r"<table>.*?</table>", do_table, html, flags=re.S)

PRIMER_SRC = ROOT / "primer"
PRIMER_OUT = ROOT / "web" / "primer"
prepare_html_output(PRIMER_OUT)

def title_of(md):
    for line in md.splitlines():
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    for line in md.splitlines():
        if line.startswith("## "):
            return re.sub(r"[*`]", "", line[3:]).strip()
    return "untitled"

NAV_PRIMER = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">short road</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a class="here" href="index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def primer_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The Phi primer: learn a language built to slow you down, one household chapter at a time.">
<title>Phi primer &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
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
     <a href="https://github.com/dcellison/phi/tree/main/primer">the source</a> is the book.
     The <a href="../colophon.html">colophon</a> records how Phi is made.</p>
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
    (PRIMER_OUT / (f.stem + ".html")).write_text(primer_page(link_text_citations(body), titles[f.name], footer_nav))

# contents page: the primer README plus a generated reading list
readme_body = md_to_html((PRIMER_SRC / "README.md").read_text())
# link the ladder tables' chapter numbers to their pages
for f in chapters:
    mm = re.match(r"(\d+)_", f.stem)
    if mm:
        n = int(mm.group(1))
        readme_body = readme_body.replace(
            f"<tr><td>{n}</td>",
            f'<tr><td><a href="{f.stem}.html">{n}</a></td>')
start_end = (f'<p>Start with <a href="{chapters[0].stem}.html">{titles[chapters[0].name]}</a>; '
             f'the ladder above links every chapter; end with <a href="{chapters[-1].stem}.html">the capstone</a>.</p>')
(PRIMER_OUT / "index.html").write_text(primer_page(link_text_citations(readme_body) + "\n" + start_end, "contents"))
print(f"wrote web/primer/: {len(chapters)} chapters + contents")

# ---- manual reader: manual/**.md rendered to web/manual/ ----
MANUAL_SRC = ROOT / "manual"
MANUAL_OUT = ROOT / "web" / "manual"
prepare_html_output(MANUAL_OUT)

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

NAV_MANUAL = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">short road</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a class="here" href="index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def manual_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The Phi manual: the complete reference for a philosophical constructed language organized by one modifier-first principle.">
<title>Phi manual &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
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
     <a href="https://github.com/dcellison/phi/tree/main/manual">the source</a> is the reference.
     The <a href="../colophon.html">colophon</a> records how Phi is made.</p>
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
        modules = d / "modules"
        if modules.is_dir():
            for f in sorted(modules.glob("*.md")):
                sections.append((label, "Domain Modules", f))
        continue
    for ch in sorted(x for x in d.iterdir() if x.is_dir()):
        ch_label = pretty(ch.name, "chapter")
        for f in sorted(ch.glob("*.md")):
            sections.append((label, ch_label, f))
app = MANUAL_SRC / "appendices"
if app.is_dir():
    for f in sorted(app.glob("*.md")):
        sections.append(("Appendices", None, f))
# back matter: the colophon signs the book, rendered from the root file
colo = ROOT / "colophon.md"
if colo.exists():
    sections.append(("Colophon", None, colo))

def slug(path):
    if MANUAL_SRC not in path.parents:
        return path.stem + ".html"
    rel = path.relative_to(MANUAL_SRC)
    return str(rel.with_suffix("")).replace("/", "__") + ".html"

sec_titles = [title_of(f.read_text()) for _, _, f in sections]
for i, (part, ch, f) in enumerate(sections):
    crumb_bits = [part] + ([ch] if ch else [])
    crumb = '<p class="crumb">' + " &mdash; ".join(crumb_bits) + "</p>"
    body = crumb + md_to_html(f.read_text())
    if f.name == "appendix_a_glossary.md":
        body = add_gloss_popovers(body)
    prev_link = f'<a href="{slug(sections[i-1][2])}">&lsaquo; {sec_titles[i-1]}</a>' if i > 0 else ""
    next_link = f'<a href="{slug(sections[i+1][2])}">{sec_titles[i+1]} &rsaquo;</a>' if i + 1 < len(sections) else ""
    footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    (MANUAL_OUT / slug(f)).write_text(manual_page(link_text_citations(body), sec_titles[i], footer_nav))

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

# ---- the texts: translated and transmuted literature rendered to web/texts/ ----
import tengwar

PHI_WORDS = {e["word"] for e in entries}

def tengwarize_dual(html):
    """For the tengwar_mode pamphlet: every Phi line gets its Tengwar
    rendering on its own line directly above the romanization, both always
    visible, so a reader can correlate the two hands without toggling
    between them."""
    def do_pre(m):
        out = []
        for line in m.group(1).split("\n"):
            source = html_module.unescape(line).strip()
            if tengwar.phi_line(source, PHI_WORDS):
                rendered = tengwar.render_line(source)
                if rendered:
                    out.append(f'<span class="teng-dual">{rendered}</span>')
            out.append(line)
        return "<pre>" + "\n".join(out) + "</pre>"
    return re.sub(r"<pre>(.*?)</pre>", do_pre, html, flags=re.S)

TEXTS_OUT = ROOT / "web" / "texts"
prepare_html_output(TEXTS_OUT)
NAV_TEXTS = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">short road</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a class="here" href="index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def texts_page(body, title):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi's literature in close translation and transmutation, from the Metta Sutta to News from Nowhere and the Ring Verse refusal.">
<title>Phi texts &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="landing primer">
{NAV_TEXTS}
<main>
{body}
<div class="chapnav"><a href="index.html">all texts</a></div>
</main>
<footer>
  <p>Each rendering identifies itself as a translation or a transmutation. The source files live in <a href="https://github.com/dcellison/phi/tree/main/pamphlets">the repository</a>, and the site renders them at build time.
     The <a href="../colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""

TEXTS = [
    ("metta_sutta", "lothea thole \u2014 The Practice of Love", "The first text written in Phi: the Metta Sutta followed through all ten verses, with each source claim and image given a place in the language."),
    ("north_wind_and_sun", "nitho howeli nela sileta \u2014 The North Wind and the Sun", "One familiar fable in two Phi renderings: a close translation for hearing the language, followed by a transmutation and a comparison through the five pillars."),
    ("human_rights_article_one", "theula miona \u2014 Article 1 of the Universal Declaration of Human Rights", "Article 1 in two Phi renderings: a close translation preserves rights and conscience, then a transmutation turns toward recognized entitlement and reciprocal kind conduct."),
    ("babel_text", "ta haluma \u2014 the Babel text", "Genesis 11:1-9 in two Phi renderings: a close translation preserves confounding and forced dispersal, while the transmutation reads scattering as sowing and every language as a garden."),
    ("ring_verse_refusal", "naweri \u2014 the Ring Verse, refused", "A refusal that names coercion and imposed tying while declining to make ruler or lord ordinary Phi roles."),
    ("schleicher_fable", "mophira nela lo kalora \u2014 Schleicher's fable", "Schleicher's 1868 test text in two Phi renderings: a close translation retains the master claim, while a transmutation names coercion and exploitation without granting the title."),
    ("little_prince_excerpts", "thiku miona lue silero \u2014 from The Little Prince", "Three excerpts in which the source title keeps its prince, the Phi title describes a small person from the stars, and taming becomes mutual bond."),
    ("velveteen_rabbit", "wuloe wetha tupiwa \u2014 The Velveteen Rabbit", "Williams's full story, with Real learned through love and the hard scenes of disability, fever, contamination, coercion, burning, and return stated plainly."),
    ("prophet_excerpts", "phewo phelui \u2014 from The Prophet", "Three selected teachings by Gibran. On Children appears in two forms: the close translation retains the bow and arrow, while the transmutation gives their motion to a tree and its wind-carried seed."),
    ("tao_te_ching", "keiro \u2014 from the Tao Te Ching", "Five Legge chapters on water, useful emptiness, unnoticed guidance, small beginnings, and yielding strength. The text includes the warning about trusting force."),
    ("heart_sutra", "nulo sano korua \u2014 the Heart Sutra", "The smaller Heart Sutra in Müller's 1894 English, rendered twice in Phi: completed crossing in the translation and a communal wish in the transmutation."),
    ("news_from_nowhere_ch1", "nophi lue mawha lokue \u2014 News from Nowhere, ch. 1", "Morris's political argument, railway journey, winter walk, sleepless reckoning, and first-person handoff, carried under an opening reportative frame."),
    ("news_from_nowhere_ch2", "nophi lue mawha lokue \u2014 News from Nowhere, ch. 2", "The first morning beside a clear river, with salmon nets, a bridge on stone rainbows, and a failed attempt to pay for a service."),
    ("news_from_nowhere_ch3", "nophi lue mawha lokue \u2014 News from Nowhere, ch. 3", "Breakfast in the Guest House, followed by bread, roses, forest history, commons entitlement, handwork, mathematics, and the arrival of Gold."),
]

TEXT_METHODS = {
    "metta_sutta": "Translation",
    "north_wind_and_sun": "Translation + transmutation",
    "human_rights_article_one": "Translation + transmutation",
    "babel_text": "Translation + transmutation",
    "ring_verse_refusal": "Transmutation",
    "schleicher_fable": "Translation + transmutation",
    "little_prince_excerpts": "Transmutation",
    "velveteen_rabbit": "Transmutation",
    "prophet_excerpts": "Translation + transmutation",
    "tao_te_ching": "Transmutation",
    "heart_sutra": "Translation + transmutation",
    "news_from_nowhere_ch1": "Transmutation",
    "news_from_nowhere_ch2": "Transmutation",
    "news_from_nowhere_ch3": "Transmutation",
}


def text_method(stem):
    return TEXT_METHODS[stem]


for stem, title, blurb in TEXTS:
    md = (ROOT / "pamphlets" / f"{stem}.md").read_text()
    method = text_method(stem)
    rendered = md_to_html(md).replace("</h1>", f'</h1>\n<p class="text-method">{method}</p>', 1)
    (TEXTS_OUT / f"{stem}.html").write_text(texts_page(rendered, title))

toc = ["<h1>The texts</h1>",
       "<p>The Metta Sutta contains all ten verses of its source. The North Wind, Schleicher, and Article 1 pages put a close translation before a transmutation. Babel and the Heart Sutra apply the same order to longer pieces. On Children pairs one teaching within The Prophet's three-part page; each paired text then shows where the methods part.</p>",
       "<p>A close translation answers to the source's claims and distinctions in natural Phi. Its purpose here is practical: to show that Phi can handle any source on its own terms and produce a close analogue, even when Phi would tell it differently. Every rendering says what it owes the source.</p>",
       "<p>Transmutation is Phi's preferred method because it gives the source room to change as Phi understands it. The five pillars and Phi's own habits of thought shape the result, while the source stays in view. This is how transmutation preserves the heart of Phi. Six works put both methods side by side so a reader can see what changed and why.</p>"]
for stem, title, blurb in TEXTS:
    toc.append(f'<h2><a href="{stem}.html">{title}</a></h2><p class="text-method">{text_method(stem)}</p><p>{blurb}</p>')
toc.append("<hr><p><em>More texts are coming; the shelf is built to grow.</em></p>")
(TEXTS_OUT / "index.html").write_text(texts_page("\n".join(toc), "contents"))
print(f"wrote web/texts/: {len(TEXTS)} texts + contents")

# ---- the pamphlets: deep-dive companions rendered to web/pamphlets/ ----
PAMPH_OUT = ROOT / "web" / "pamphlets"
prepare_html_output(PAMPH_OUT)
NAV_PAMPH = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">short road</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a class="here" href="index.html">pamphlets</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def pamphlet_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Deep-dive practice companions to the Phi manual, from relative clauses to the punctuation you can hear — each explained patiently, with exercises and answer keys.">
<title>Phi pamphlets &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="landing primer">
{NAV_PAMPH}
<main>
{body}
{footer_nav}
</main>
<footer>
  <p>The pamphlets are deep-dive companions to the manual &mdash; where they disagree,
     the manual wins. Written in <a href="https://github.com/dcellison/phi/tree/main/pamphlets">the repository</a>, rendered at build time.
     The <a href="../colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""

PAMPHLETS = [
    ("relative_clauses", "Relative clauses in Phi",
     "The whole description before the noun: pre-nominal relative clauses from first principles to nested patterns, the errors English pulls you toward, and exercises with a full answer key."),
    ("complementizers", "Complementizers and embedded clauses in Phi",
     "Thoughts within thoughts: the three opener–closer pairs — statements, questions, quotations — why the closers exist, and enough practice to make them reflex."),
    ("evidentiality", "Evidentiality in Phi",
     "Four particles for how you know — witnessed, inferred, told, assumed — drilled from the snake at the well to the honest journal. Phi does not ask you to be certain; it asks you to be exact about how you are not."),
    ("ternary_numerals", "Counting in Phi: the ternary numerals and the four natures",
     "Three number-words, four group-words, four kinds of being — counting drilled to reflex, and then the harder skill: the honest about, where the sentence gets shorter as it gets truer."),
    ("naming", "How Phi names people",
     "A name is a word someone carries: ne the spoken capital, kona the raised hand, three honorifics that announce relationship rather than rank — and the family register, where a name at rest is proof of presence."),
    ("spoken_punctuation", "Punctuation you can hear",
     "Core Phi writes one mark and lexicalizes the rest: wa the question, shola and sholo the quotation boundary, kona the address, ne the name, and a dictation practice whose limits are stated explicitly."),
    ("source_material", "Source material beside Phi",
     "How Phi uses vocabulary, transparent expressions, modules, and productive names while exact records, scripts, notation, testimony, and quotations remain in their own medium."),
    ("three_slots", "The three slots",
     "The whole grammar is thirty-five small words that never change: the frame, the stack, and the word's dress, drilled to reflex — with the interaction tables, the ruled readings, and the evening question where every particle costs what it claims."),
    ("tengwar_mode", "How Phi is written in Tengwar",
     "A second hand for the same language: the fifteen consonant tengwar, the vowel tehtar that ride above and below them, and the one true invention — a hiatus rule that needs no vowel carrier at all, because Phi's own sound rules never leave it needing one."),
]
toc = ["<h1>The pamphlets</h1>",
       "<p>Focused deep-dives: extended explanation and abundant practice for the features learners find hardest. Each is a companion to the manual, not a rival — read one straight through, or keep it open beside the exercises.</p>"]
pamph_pages = 0
for dirname, title, blurb in PAMPHLETS:
    pfiles = sorted((ROOT / "pamphlets" / dirname).glob("*.md"))
    ptitles = [title_of(f.read_text()) for f in pfiles]
    dual = dirname == "tengwar_mode"
    for i, f in enumerate(pfiles):
        html = md_to_html(f.read_text())
        body = tengwarize_dual(html) if dual else html
        prev_link = f'<a href="{dirname}__{pfiles[i-1].stem}.html">&lsaquo; {ptitles[i-1]}</a>' if i > 0 else ""
        next_link = f'<a href="{dirname}__{pfiles[i+1].stem}.html">{ptitles[i+1]} &rsaquo;</a>' if i + 1 < len(pfiles) else ""
        footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">all pamphlets</a>{next_link}</div>'
        (PAMPH_OUT / f"{dirname}__{f.stem}.html").write_text(pamphlet_page(link_text_citations(body), ptitles[i], footer_nav))
        pamph_pages += 1
    toc.append(f'<h2><a href="{dirname}__{pfiles[0].stem}.html">{title}</a></h2><p>{blurb}</p>')
toc.append("<hr><p><em>More pamphlets are coming; the shelf is built to grow.</em></p>")
(PAMPH_OUT / "index.html").write_text(pamphlet_page("\n".join(toc), "contents"))
print(f"wrote web/pamphlets/: {pamph_pages} pages + contents")
