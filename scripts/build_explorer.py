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

# ---- tengwar word dictionary: every word pre-rendered for the teacher ----
import sys as _sys
_sys.path.insert(0, str(ROOT / "scripts"))
import tengwar as _tengwar
tw = {e["word"]: _tengwar.render_line(e["word"]) for e in entries}
period = _tengwar.render_line(".")
if period:
    tw["."] = period
tw_out = ROOT / "web" / "tengwar_words.json"
tw_out.write_text(json.dumps(tw, ensure_ascii=False, separators=(",", ":")))
print(f"wrote web/tengwar_words.json: {len(tw)} renderings, {tw_out.stat().st_size // 1024} KB")

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
# the three doors become links: explorer here, primer and manual on GitHub
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
<meta name="description" content="Phi is a constructed language built to slow you down: one grammar rule, sounds you cannot rush, and a shelf of literature that includes the Ring Verse it refused to translate.">
<meta property="og:title" content="Phi — a language built to slow you down">
<meta property="og:description" content="One grammar rule, no irregulars, sounds you cannot rush — and no words for lord, throne, or rule. Nine hundred words, a primer, a manual, and literature already on the shelf.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dcellison.github.io/phi/">
<title>Phi — kia</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing">
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="teacher.html">teacher</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
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

def link_text_citations(html):
    """Repo-path citations of the texts become on-site links (pages
    using this all live one directory below web/)."""
    for stem in ("metta_sutta", "north_wind_and_sun", "human_rights_article_one", "babel_text", "ring_verse_refusal", "schleicher_fable", "little_prince_excerpts", "velveteen_rabbit"):
        html = html.replace(f"<code>pamphlets/{stem}.md</code>",
                            f'<a href="../texts/{stem}.html"><code>pamphlets/{stem}.md</code></a>')
        html = html.replace(f'href="../pamphlets/{stem}.md"',
                            f'href="../texts/{stem}.html"')
    return html

PRIMER_SRC = ROOT / "primer"
PRIMER_OUT = ROOT / "web" / "primer"
PRIMER_OUT.mkdir(parents=True, exist_ok=True)

def title_of(md):
    for line in md.splitlines():
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    for line in md.splitlines():
        if line.startswith("## "):
            return re.sub(r"[*`]", "", line[3:]).strip()
    return "untitled"

NAV_PRIMER = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a class="here" href="index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../teacher.html">teacher</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def primer_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The Phi primer: learn a language built to slow you down, one household chapter at a time.">
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

NAV_MANUAL = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a class="here" href="index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../teacher.html">teacher</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def manual_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The Phi manual: the complete reference for a constructed language with one grammatical rule and no irregular anything.">
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

# ---- the texts: transmuted literature rendered to web/texts/ ----
import tengwar

PHI_WORDS = {e["word"] for e in entries}

def tengwarize(html):
    """Inside each <pre> of a text page, give every Phi line a Tengwar
    rendering alongside the romanization; the tengtoggle switches them."""
    def do_pre(m):
        out = []
        for line in m.group(1).split("\n"):
            svg = None
            if tengwar.phi_line(line.strip(), PHI_WORDS):
                svg = tengwar.render_line(line.strip())
            if svg:
                out.append(f'<span class="rom">{line}</span><span class="teng">{svg}</span>')
            else:
                out.append(line)
        return "<pre>" + "\n".join(out) + "</pre>"
    return re.sub(r"<pre>(.*?)</pre>", do_pre, html, flags=re.S)

TEXTS_OUT = ROOT / "web" / "texts"
TEXTS_OUT.mkdir(parents=True, exist_ok=True)
NAV_TEXTS = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a class="here" href="index.html">texts</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../teacher.html">teacher</a> <button class="tengtoggle" aria-label="toggle tengwar script" title="tengwar / roman">tengwar</button> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def texts_page(body, title):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi's literature: eight transmutations, from the Metta Sutta to The Velveteen Rabbit — and the Ring Verse, refused.">
<title>Phi texts &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../tengwar.js"></script>
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
    ("metta_sutta", "lothea thole \u2014 The Practice of Love", "The first text ever written in Phi: the Metta Sutta, the loving-kindness meditation, rebuilt from the language's own concepts. Where the language's heart is."),
    ("north_wind_and_sun", "nitho howeli nela sorae \u2014 The North Wind and the Sun", "Phi's first story: the fable told in a thousand languages to show what each sounds like. The primer's capstone sends its readers here."),
    ("human_rights_article_one", "theula miona \u2014 Article 1 of the Universal Declaration of Human Rights", "The most-translated document in history, in the language that needed no new words to say it \u2014 and no gendered ones to exclude with."),
    ("babel_text", "ta haoluma \u2014 the Babel text", "The conlang community's handshake, done the Phi way: the scattering as sowing, every language a garden \u2014 and the first time Phi names its own kind."),
    ("ring_verse_refusal", "naweri \u2014 the Ring Verse, refused", "The one entry on this shelf that is not a translation: what a language without domination vocabulary cannot say \u2014 and the hearth-poem that comes out when it tries."),
    ("schleicher_fable", "mophira nela lo kalora \u2014 Schleicher's fable", "The historical linguists' test-text since 1868. Phi's telling keeps the sting and withholds one word: the master, who can only be described as the one who takes."),
    ("little_prince_excerpts", "thiku miona lue silero \u2014 from The Little Prince", "Three excerpts, zero new words \u2014 and two transmutations that see through the original: the prince who was never a rank, and the taming that was always a bond."),
    ("velveteen_rabbit", "wuloe wetha tupiwa \u2014 The Velveteen Rabbit", "The longest transmutation: a full story in eight scenes, two coins, and the discovery that Real was the habitual aspect all along."),
]
for stem, title, blurb in TEXTS:
    md = (ROOT / "pamphlets" / f"{stem}.md").read_text()
    (TEXTS_OUT / f"{stem}.html").write_text(texts_page(tengwarize(md_to_html(md)), title))

toc = ["<h1>The texts</h1>",
       "<p>Phi's literature so far. Each is a transmutation &mdash; not a translation word for word, but the idea rebuilt from Phi's own concepts, with notes recording every adaptation the language asked for.</p>"]
for stem, title, blurb in TEXTS:
    toc.append(f'<h2><a href="{stem}.html">{title}</a></h2><p>{blurb}</p>')
toc.append("<hr><p><em>More transmutations are coming; the shelf is built to grow.</em></p>")
(TEXTS_OUT / "index.html").write_text(texts_page("\n".join(toc), "contents"))
print(f"wrote web/texts/: {len(TEXTS)} texts + contents")

# ---- the pamphlets: deep-dive companions rendered to web/pamphlets/ ----
PAMPH_OUT = ROOT / "web" / "pamphlets"
PAMPH_OUT.mkdir(parents=True, exist_ok=True)
NAV_PAMPH = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a class="here" href="index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../teacher.html">teacher</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def pamphlet_page(body, title, footer_nav=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Deep-dive practice companions to the Phi manual, from relative clauses to the punctuation you can hear — each explained patiently, with exercises and answer keys.">
<title>Phi pamphlets &mdash; {title}</title>
<script src="../theme.js"></script>
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
     the manual wins. Written in <a href="https://github.com/dcellison/phi/tree/main/pamphlets">the repository</a>, rendered at build time.</p>
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
    ("metta_companion", "Reading lothea thole: a companion to the first text",
     "The Metta Sutta walked verse by verse — one must, nineteen mays, and the verse where the wishing stops. The optative engine, the headless refrain, the three compounds read as observations, and the recitation the text was always for."),
    ("spoken_punctuation", "Punctuation you can hear",
     "Phi writes one mark and says the rest: wa the question mark, shola and sholo the quotation marks, kona the comma of address, ne the capital of a name — and the dictation test that page-bound punctuation cannot pass."),
    ("three_slots", "The three slots",
     "The whole grammar is thirty-five small words that never change: the frame, the stack, and the word's dress, drilled to reflex — with the interaction tables, the ruled readings, and the evening question where every particle costs what it claims."),
]
toc = ["<h1>The pamphlets</h1>",
       "<p>Focused deep-dives: extended explanation and abundant practice for the features learners find hardest. Each is a companion to the manual, not a rival — read one straight through, or keep it open beside the exercises.</p>"]
pamph_pages = 0
for dirname, title, blurb in PAMPHLETS:
    pfiles = sorted((ROOT / "pamphlets" / dirname).glob("*.md"))
    ptitles = [title_of(f.read_text()) for f in pfiles]
    for i, f in enumerate(pfiles):
        body = md_to_html(f.read_text())
        prev_link = f'<a href="{dirname}__{pfiles[i-1].stem}.html">&lsaquo; {ptitles[i-1]}</a>' if i > 0 else ""
        next_link = f'<a href="{dirname}__{pfiles[i+1].stem}.html">{ptitles[i+1]} &rsaquo;</a>' if i + 1 < len(pfiles) else ""
        footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">all pamphlets</a>{next_link}</div>'
        (PAMPH_OUT / f"{dirname}__{f.stem}.html").write_text(pamphlet_page(link_text_citations(body), ptitles[i], footer_nav))
        pamph_pages += 1
    toc.append(f'<h2><a href="{dirname}__{pfiles[0].stem}.html">{title}</a></h2><p>{blurb}</p>')
toc.append("<hr><p><em>More pamphlets are coming; the shelf is built to grow.</em></p>")
(PAMPH_OUT / "index.html").write_text(pamphlet_page("\n".join(toc), "contents"))
print(f"wrote web/pamphlets/: {pamph_pages} pages + contents")
