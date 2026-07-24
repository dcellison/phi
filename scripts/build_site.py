"""Build the complete Phi website under build/site.

Maintained website assets live under site/. Generated output is not committed.
Run before serving the site locally:
    python3 scripts/build_site.py
    python3 -m http.server -d build/site
"""
import html as html_module
import json
import re
import shutil
from pathlib import Path

from compound_registry import load_compounds
from content_catalogues import load_pamphlet_catalogue, load_text_catalogue

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = ROOT / "site"
BUILD_SITE = ROOT / "build" / "site"
VOCABULARY_DIR = ROOT / "vocabulary"
VOCABULARY_ENTRY_DIRS = tuple(
    VOCABULARY_DIR / name for name in ("content", "function", "interjection")
)
SCHEMA = json.loads((VOCABULARY_DIR / "schema.json").read_text(encoding="utf-8"))
FIELDS = list(SCHEMA["properties"])
TEXT_CATALOGUE = load_text_catalogue(ROOT)
PAMPHLET_CATALOGUE = load_pamphlet_catalogue(ROOT)
TEXTS = [work for work in TEXT_CATALOGUE if work["kind"] == "short"]
BOOKS = [work for work in TEXT_CATALOGUE if work["kind"] == "book"]
if len(BOOKS) != 1:
    raise ValueError("the site renderer currently expects exactly one catalogued book")
NEWS_WORK = BOOKS[0]


def prepare_site_output():
    """Create a clean deployment tree and copy maintained site assets into it."""
    if BUILD_SITE.exists():
        shutil.rmtree(BUILD_SITE)
    BUILD_SITE.mkdir(parents=True)
    for name in ("app.js", "explore.html", "reader.js", "style.css", "theme.js"):
        shutil.copy2(SITE_SRC / name, BUILD_SITE / name)
    shutil.copytree(SITE_SRC / "fonts", BUILD_SITE / "fonts")
    shutil.copytree(SITE_SRC / "icons", BUILD_SITE / "icons")


def prepare_html_output(path):
    """Create a generated HTML directory and remove obsolete pages."""
    path.mkdir(parents=True, exist_ok=True)
    for generated in path.glob("*.html"):
        generated.unlink()


prepare_site_output()


entries = []
entry_paths = sorted(
    path
    for directory in VOCABULARY_ENTRY_DIRS
    for path in directory.rglob("*.json")
)
for p in entry_paths:
    d = json.loads(p.read_text())
    e = {k: d[k] for k in FIELDS if k in d}
    e["kind"] = p.parent.name if p.parent.name != "content" else "content"
    entries.append(e)

entries.sort(key=lambda e: e["word"])
out = BUILD_SITE / "lexicon.json"
out.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {out.relative_to(ROOT)}: {len(entries)} entries, {out.stat().st_size // 1024} KB")

# ---- compound registry: documents/reference/compounds.md to build/site/compounds.json ----
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
comp_out = BUILD_SITE / "compounds.json"
comp_out.write_text(json.dumps(compounds, ensure_ascii=False, separators=(",", ":")))
print(f"wrote {comp_out.relative_to(ROOT)}: {len(compounds)} compounds")

# ---- landing page: kia.md rendered to build/site/index.html ----

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
body = body.replace("<strong>Consider</strong>",
                    '<strong><a href="book/index.html">Consider</a></strong>')
body = body.replace("<strong>Read</strong>",
                    '<strong><a href="texts/index.html">Read</a></strong>')
body = body.replace("<strong>Practice</strong>",
                    '<strong><a href="pamphlets/index.html">Practice</a></strong>')
landing = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi is a philosophical constructed language for practising mindful and compassionate speech.">
<meta property="og:title" content="Phi: a language for mindful and compassionate speech">
<meta property="og:description" content="A modifier-first organizing principle, regular forms, clear source boundaries, more than a thousand words, a primer, a manual, and literature already on the shelf.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dcellison.github.io/phi/">
<title>Phi — kia</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing">
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="short_road.html">walk</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="book/index.html">book</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
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
(BUILD_SITE / "index.html").write_text(landing)
print(f"wrote build/site/index.html from kia.md ({len(body.splitlines())} blocks)")

# ---- colophon: colophon.md rendered to build/site/colophon.html ----

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
<nav class="topnav"><a href="index.html">kia</a> <span class="sep">&middot;</span> <a href="short_road.html">walk</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="book/index.html">book</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
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
(BUILD_SITE / "colophon.html").write_text(colophon_page)
print("wrote build/site/colophon.html from colophon.md")

# ---- the short road: short_road.md rendered to build/site/short_road.html ----

short_road_body = md_to_html((ROOT / "short_road.md").read_text())
short_road_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A twenty-minute walk through Phi, from its first open vowel and modifier-first grammar to the choices its text shelf puts into practice.">
<title>Phi — the short road</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing primer">
<nav class="topnav"><a href="index.html">kia</a> <span class="sep">&middot;</span> <a class="here" href="short_road.html">walk</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="book/index.html">book</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
{short_road_body}
</main>
<footer>
  <p>A twenty-minute walk from Phi's first open vowel to its text shelf. This page is short_road.md, rendered from
     <a href="https://github.com/dcellison/phi">the repository</a>.
     The <a href="colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""
(BUILD_SITE / "short_road.html").write_text(short_road_page)
print("wrote build/site/short_road.html from short_road.md")

# ---- primer reader: primer/*.md rendered to build/site/primer/ ----

TEXT_SITE_PATHS = {
    f"texts/{work['path']}": f"{Path(work['path']).stem}.html"
    for work in TEXT_CATALOGUE
    if work["kind"] == "short"
}
for chapter in sorted(
    (ROOT / "texts" / NEWS_WORK["path"]).glob("chapter_*.md")
):
    repo_path = chapter.relative_to(ROOT).as_posix()
    TEXT_SITE_PATHS[repo_path] = f"news_from_nowhere/{chapter.stem}.html"


def link_text_citations(html):
    """Repo-path citations of the texts become on-site links (pages
    using this all live one directory below the deployed site root)."""
    for repo_path, site_path in TEXT_SITE_PATHS.items():
        site_href = f"../texts/{site_path}"
        html = html.replace(
            f"<code>{repo_path}</code>",
            f'<a href="{site_href}"><code>{repo_path}</code></a>',
        )
        html = re.sub(
            rf'href="(?:\.\./)+{re.escape(repo_path)}"',
            f'href="{site_href}"',
            html,
        )
    html = re.sub(
        r'href="\.\./lexicon/by_module\.md#([a-z0-9-]+)"',
        lambda match: f'href="../explore.html?module={match.group(1)}"',
        html,
    )
    html = html.replace(
        "<code>documents/reference/compounds.md</code>",
        '<a href="../manual/part7_reference__compounds.html"><code>documents/reference/compounds.md</code></a>',
    )
    return html


PHI_INLINE_FORM = re.compile(
    r"[a-z]+(?:(?:[.]? | [.]{3} | … )[a-z]+)*[.]?"
)


def is_current_phi(value):
    """Return whether a short rendered string consists only of current Phi."""
    text = html_module.unescape(value).strip()
    if not PHI_INLINE_FORM.fullmatch(text):
        return False
    words = re.findall(r"[a-z]+", text)
    return bool(words) and all(word in ALL_WORDS for word in words)


def is_current_phi_passage(value):
    """Return whether a punctuated passage contains only current Phi forms."""
    text = html_module.unescape(value).strip()
    if not re.fullmatch(r"[a-z]+(?:[ .]+[a-z]+)*[.]?", text):
        return False
    words = re.findall(r"[a-z]+", text)
    return bool(words) and all(word in ALL_WORDS for word in words)


def mark_inline_phi(body):
    """Identify backticked Phi in prose without styling paths or labels."""
    def mark_code(match):
        if not is_current_phi(match.group(1)):
            return match.group(0)
        return f'<code class="phi-inline">{match.group(1)}</code>'

    def mark_paragraph(match):
        return re.sub(r"<code>([^<]+)</code>", mark_code, match.group(0))

    return re.sub(r"<p(?: [^>]*)?>.*?</p>", mark_paragraph, body, flags=re.S)


def mark_primer_inline_fragment(fragment):
    """Lift intentional Phi mentions from one primer prose fragment."""
    def mark_strong(strong_match):
        if not is_current_phi(strong_match.group(1)):
            return strong_match.group(0)
        return f'<code class="phi-inline">{strong_match.group(1)}</code>'

    fragment = re.sub(r"<strong>([^<]+)</strong>", mark_strong, fragment)

    def mark_em(em_match):
        if not is_current_phi(em_match.group(1)):
            return em_match.group(0)
        return f'<code class="phi-inline">{em_match.group(1)}</code>'

    fragment = re.sub(r"<em>([^<]+)</em>", mark_em, fragment)

    def mark_em_bridge(bridge_match):
        value = bridge_match.group(2)
        punctuation = ""
        if value.endswith((".", ",", ":", ";", "?", "!")):
            value, punctuation = value[:-1], value[-1]
        if not is_current_phi(value):
            return bridge_match.group(0)
        return (
            "</em>"
            + bridge_match.group(1)
            + f'<code class="phi-inline">{value}</code>'
            + punctuation
            + bridge_match.group(3)
            + "<em>"
        )

    return re.sub(
        r"</em>(\s+)([^<>]+?)(\s*)<em>",
        mark_em_bridge,
        fragment,
    )


def mark_primer_inline_phi(body):
    """Lift the primer's emphasized inline Phi into the shared chip style."""
    return re.sub(
        r"<p(?: [^>]*)?>.*?</p>",
        lambda match: mark_primer_inline_fragment(match.group(0)),
        body,
        flags=re.S,
    )


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
PRIMER_OUT = BUILD_SITE / "primer"
prepare_html_output(PRIMER_OUT)


def title_of(md):
    for line in md.splitlines():
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    for line in md.splitlines():
        if line.startswith("## "):
            return re.sub(r"[*`]", "", line[3:]).strip()
    return "untitled"


def load_primer_editorial():
    """Load the complete primer treatment and reject gaps or stale entries."""
    config_path = SITE_SRC / "primer_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if set(config) != {"total_chapters", "parts", "pages"}:
        raise ValueError(
            "site/primer_editorial.json requires total_chapters, parts, and pages"
        )
    total = config["total_chapters"]
    if not isinstance(total, int) or total < 1:
        raise ValueError("primer editorial total_chapters must be positive")
    parts = config["parts"]
    if not isinstance(parts, list) or not parts:
        raise ValueError("primer editorial parts must be a non-empty list")
    expected_first = 1
    for part in parts:
        if not isinstance(part, dict) or set(part) != {
            "first",
            "last",
            "label",
            "motif",
        }:
            raise ValueError(
                "each primer editorial part requires first, last, label, and motif"
            )
        if (
            not isinstance(part["first"], int)
            or not isinstance(part["last"], int)
            or part["first"] != expected_first
            or part["last"] < part["first"]
            or part["last"] > total
        ):
            raise ValueError("primer editorial part ranges must be contiguous")
        if not isinstance(part["label"], str) or not part["label"].strip():
            raise ValueError("primer editorial part labels must be non-empty")
        if part["motif"] not in {"household", "seasons", "gathering", "story"}:
            raise ValueError(
                f"unknown primer editorial motif: {part['motif']}"
            )
        expected_first = part["last"] + 1
    if expected_first != total + 1:
        raise ValueError("primer editorial parts must cover every chapter")

    pages = config.get("pages")
    if not isinstance(pages, dict):
        raise ValueError("primer editorial pages must be an object")
    expected_pages = {
        path.relative_to(ROOT).as_posix()
        for path in PRIMER_SRC.glob("[0-9][0-9]_*.md")
        if 1 <= int(path.name[:2]) <= total
    }
    if set(pages) != expected_pages:
        missing = sorted(expected_pages - set(pages))
        extra = sorted(set(pages) - expected_pages)
        raise ValueError(
            f"primer editorial page inventory differs: missing={missing}, extra={extra}"
        )
    resolved = {}
    for repo_path, treatment in pages.items():
        source_path = ROOT / repo_path
        if (
            not repo_path.startswith("primer/")
            or not source_path.is_file()
            or not isinstance(treatment, dict)
        ):
            raise ValueError(f"invalid primer editorial source: {repo_path}")
        if set(treatment) != {"story_title", "manual_source"}:
            raise ValueError(
                f"primer editorial treatment for {repo_path} requires "
                "manual_source and story_title"
            )
        if (
            not isinstance(treatment["story_title"], str)
            or not treatment["story_title"].strip()
        ):
            raise ValueError(
                f"primer editorial story_title for {repo_path} must be non-empty"
            )
        chapter_match = re.match(r"primer/([0-9]+)_", repo_path)
        if chapter_match is None:
            raise ValueError(f"primer editorial chapter is not numbered: {repo_path}")
        chapter = int(chapter_match.group(1))
        part = next(
            (
                candidate
                for candidate in parts
                if candidate["first"] <= chapter <= candidate["last"]
            ),
            None,
        )
        if part is None:
            raise ValueError(f"primer editorial chapter has no part: {repo_path}")
        manual_source = treatment["manual_source"]
        if (
            not isinstance(manual_source, str)
            or not manual_source.startswith("manual/")
            or not (ROOT / manual_source).is_file()
        ):
            raise ValueError(
                f"invalid primer editorial manual reference for {repo_path}"
            )
        resolved[repo_path] = {
            "part": part["label"],
            "story_title": treatment["story_title"],
            "progress": {"current": chapter, "total": total},
            "motif": part["motif"],
            "manual_source": manual_source,
        }
    return total, parts, resolved


def primer_motif(name):
    """Return one of the restrained motifs used across the primer."""
    # Lucide outlines; the deployed site carries the project's ISC notice.
    icons = {
        "household": (
            """
    <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
    <path d="M3 10a2 2 0 0 1 .71-1.53l7-6a2 2 0 0 1 2.58 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>""",
            """
    <path d="M7 20h8"/>
    <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
    <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5 0-4.6-.7-1.1-.8-1.8-2.2-2.3-3.7 2-.4 3.5 0 4.6.7z"/>
    <path d="M14.1 6a7 7 0 0 0-1.9 2.8c1.7.3 3.1 0 4.1-.7 1-.7 1.6-1.9 2-3.3-1.8-.3-3.2 0-4.2.7z"/>""",
        ),
        "seasons": (
            """
    <circle cx="12" cy="12" r="4"/>
    <path d="M12 2v2"/><path d="M12 20v2"/>
    <path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/>
    <path d="M2 12h2"/><path d="M20 12h2"/>
    <path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>""",
            """
    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
    <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>""",
        ),
        "gathering": (
            """
    <path d="M18 21a8 8 0 0 0-16 0"/>
    <circle cx="10" cy="8" r="5"/>
    <path d="M22 20c0-3.37-2-6.5-4-8a5 5 0 0 0-.45-8.3"/>""",
            """
    <path d="M12 5a3 3 0 1 1 3 3m-3-3a3 3 0 1 0-3 3m3-3v1M9 8a3 3 0 1 0 3 3M9 8h1m5 0a3 3 0 1 1-3 3m3-3h-1m-2 3v-1"/>
    <circle cx="12" cy="8" r="2"/>
    <path d="M12 10v12"/>
    <path d="M12 22c4.2 0 7-1.667 7-5-4.2 0-7 1.667-7 5Z"/>
    <path d="M12 22c-4.2 0-7-1.667-7-5 4.2 0 7 1.667 7 5Z"/>""",
        ),
        "story": (
            """
    <path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>""",
            """
    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
    <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>""",
        ),
        "capstone": (
            """
    <path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719"/>""",
            """
    <path d="M12 5v16"/>
    <path d="M20.001 19A2 2 0 0 0 22 17V5a2 2 0 0 0-1.999-2L16 3.002A5 5 0 0 0 12 5a5 5 0 0 0-4-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 1.999 2H8a5 5 0 0 1 4 2 5 5 0 0 1 4-2z"/>""",
        ),
        "breath": (
            """
    <path d="M12.8 19.6A2 2 0 1 0 14 16H2"/>
    <path d="M17.5 8a2.5 2.5 0 1 1 2 4H2"/>
    <path d="M9.8 4.4A2 2 0 1 1 11 8H2"/>""",
            """
    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>
    <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>""",
        ),
        "contents": (
            """
    <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
    <path d="M3 10a2 2 0 0 1 .71-1.53l7-6a2 2 0 0 1 2.58 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>""",
            """
    <path d="M12 5v16"/>
    <path d="M20.001 19A2 2 0 0 0 22 17V5a2 2 0 0 0-1.999-2L16 3.002A5 5 0 0 0 12 5a5 5 0 0 0-4-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 1.999 2H8a5 5 0 0 1 4 2 5 5 0 0 1 4-2z"/>""",
        ),
    }
    if name not in icons:
        raise ValueError(f"unknown primer motif: {name}")
    rendered = "".join(
        f'<svg viewBox="0 0 24 24" focusable="false">{icon}</svg>'
        for icon in icons[name]
    )
    return (
        f'<div class="primer-part-motif primer-motif-{name}" '
        f'aria-hidden="true">{rendered}</div>'
    )


def style_primer_blockquotes(body):
    """Distinguish Phi reading lines and speaker turns in a primer chapter."""
    def style_quote(match):
        lines = [
            line.strip()
            for line in match.group(1).split("<br>")
            if line.strip()
        ]
        parsed = []
        has_turn = False
        for line in lines:
            turn = re.fullmatch(
                r"([a-z]+):\s*<strong>(.*?)</strong>(?:\s*(.*))?",
                line,
                flags=re.S,
            )
            if (
                turn is not None
                and turn.group(1) in ALL_WORDS
                and is_current_phi(turn.group(2))
            ):
                parsed.append(
                    ("turn", turn.group(1), turn.group(2), turn.group(3))
                )
                has_turn = True
                continue
            reading = re.fullmatch(
                r"<strong>(.*?)</strong>(?:\s*(.*))?",
                line,
                flags=re.S,
            )
            if reading is not None and is_current_phi(reading.group(1)):
                parsed.append(
                    ("reading", None, reading.group(1), reading.group(2))
                )
                continue
            return match.group(0)

        if not has_turn:
            readings = []
            for _, _, utterance, note_html in parsed:
                note = (
                    '<span class="primer-reading-note">'
                    f"{mark_primer_inline_fragment(note_html)}</span>"
                    if note_html
                    else ""
                )
                readings.append(
                    '<span class="primer-reading-line">'
                    f'<span class="primer-phi-line">{utterance}</span>'
                    f"{note}</span>"
                )
            return (
                '<blockquote class="primer-reading" aria-label="Phi passage">'
                + "".join(readings)
                + "</blockquote>"
            )

        turns = []
        for kind, speaker, utterance, note_html in parsed:
            note = (
                '<span class="primer-dialogue-note">'
                f"{mark_primer_inline_fragment(note_html)}</span>"
                if note_html
                else ""
            )
            if kind == "turn":
                turns.append(
                    '<span class="primer-dialogue-line">'
                    f'<span class="primer-speaker">{speaker}</span>'
                    '<span class="primer-dialogue-copy">'
                    f'<span class="primer-utterance">{utterance}</span>'
                    f"{note}</span>"
                    "</span>"
                )
            else:
                turns.append(
                    '<span class="primer-dialogue-line primer-narration-line">'
                    '<span class="primer-dialogue-copy">'
                    f'<span class="primer-utterance">{utterance}</span>'
                    f"{note}</span>"
                    "</span>"
                )
        return (
            '<blockquote class="primer-dialogue" aria-label="Phi dialogue">'
            + "".join(turns)
            + "</blockquote>"
        )

    return re.sub(r"<blockquote>(.*?)</blockquote>", style_quote, body, flags=re.S)


def apply_primer_editorial(body, source, repo_path, treatment):
    """Add the opt-in reader treatment for one primer chapter."""
    progress = treatment["progress"]
    heading = re.search(r"<h1>(.*?)</h1>", body, flags=re.S)
    if heading is None:
        raise ValueError(f"editorial primer source has no heading: {repo_path}")
    heading_parts = heading.group(1).split(" · ", 1)
    if (
        len(heading_parts) != 2
        or not heading_parts[0].isdigit()
        or int(heading_parts[0]) != progress["current"]
    ):
        raise ValueError(
            f"editorial primer heading does not match progress: {repo_path}"
        )
    ratio = 100 * progress["current"] / progress["total"]
    header = f"""
<header class="primer-chapter-header">
  <div class="primer-chapter-meta">
    <p class="primer-part">{html_module.escape(treatment["part"])}</p>
    <p class="primer-progress-label">Chapter {progress["current"]} of {progress["total"]}</p>
  </div>
  <div class="primer-title-row">
    <div>
      <h1><span class="primer-chapter-number">{heading_parts[0]}</span><span class="primer-title-divider" aria-hidden="true">·</span><span class="primer-chapter-word">{heading_parts[1]}</span></h1>
      <p class="primer-story-title">{html_module.escape(treatment["story_title"])}</p>
    </div>
    {primer_motif(treatment["motif"])}
  </div>
  <div class="primer-progress" role="progressbar" aria-label="Chapter {progress["current"]} of {progress["total"]}" aria-valuemin="1" aria-valuemax="{progress["total"]}" aria-valuenow="{progress["current"]}">
    <span style="width: {ratio:.4f}%"></span>
  </div>
</header>""".strip()
    body = body[:heading.start()] + header + body[heading.end():]

    header_end = body.index("</header>") + len("</header>")
    opening = body[header_end:]
    opening, lede_count = re.subn(
        r"<p>(.*?)</p>",
        r'<p class="primer-chapter-lede">\1</p>',
        opening,
        count=1,
        flags=re.S,
    )
    if lede_count != 1:
        raise ValueError(f"editorial primer source has no lede: {repo_path}")
    body = body[:header_end] + opening
    body = mark_inline_phi(mark_primer_inline_phi(body))

    body, scene_count = re.subn(
        r"<h2>([IVXLCDM]+)</h2>",
        (
            '<h2 class="primer-scene-title">'
            '<span class="primer-scene-label">Scene</span>'
            r'<span class="primer-scene-number">\1</span>'
            "</h2>"
        ),
        body,
    )
    if scene_count == 0:
        raise ValueError(f"editorial primer source has no scenes: {repo_path}")
    body = style_primer_blockquotes(body)

    body, ledger_count = re.subn(
        (
            r"<table>(?=<tr><th>new word</th><th>say it</th>"
            r"<th>it means</th></tr>)"
        ),
        '<table class="primer-word-ledger">',
        body,
    )
    if ledger_count == 0:
        raise ValueError(f"editorial primer source has no word ledger: {repo_path}")
    body = re.sub(
        r"(</table>)\n<p>",
        r'\1\n<p class="primer-scene-note">',
        body,
    )

    manual_label = "The machinery, when you want it:"
    if source.count(manual_label) != 1 or body.count(manual_label) != 1:
        raise ValueError(
            f"editorial manual reference must occur once in {repo_path}"
        )
    manual_source = Path(treatment["manual_source"]).relative_to("manual")
    manual_href = (
        "../manual/"
        + str(manual_source.with_suffix("")).replace("/", "__")
        + ".html"
    )
    body = body.replace(
        manual_label,
        f'<a class="primer-manual-link" href="{manual_href}">{manual_label}</a>',
    )
    if body.count("<hr>") != 1:
        raise ValueError(
            f"editorial primer source must have one closing rule: {repo_path}"
        )
    chapter_body, closing = body.split("<hr>", 1)
    return (
        chapter_body
        + '<aside class="primer-closing-note">\n'
        + closing.strip()
        + "\n</aside>"
    )


def primer_special_header(
    eyebrow,
    progress_label,
    title,
    story_title,
    motif,
    progress=None,
):
    """Build a primer header for contents, prelude, or capstone pages."""
    progress_html = ""
    if progress is not None:
        progress_html = f"""
  <div class="primer-progress" aria-hidden="true">
    <span style="width: {progress:.4f}%"></span>
  </div>"""
    return f"""
<header class="primer-chapter-header primer-special-header">
  <div class="primer-chapter-meta">
    <p class="primer-part">{html_module.escape(eyebrow)}</p>
    <p class="primer-progress-label">{html_module.escape(progress_label)}</p>
  </div>
  <div class="primer-title-row">
    <div>
      <h1><span class="primer-chapter-word">{html_module.escape(title)}</span></h1>
      <p class="primer-story-title">{html_module.escape(story_title)}</p>
    </div>
    {primer_motif(motif)}
  </div>{progress_html}
</header>""".strip()


def apply_primer_prelude(body, repo_path):
    """Give the pronunciation prelude the primer's reference-page treatment."""
    heading = "<h1>Before you begin: the sounds</h1>"
    if body.count(heading) != 1:
        raise ValueError(f"primer prelude heading changed: {repo_path}")
    header = primer_special_header(
        "Prelude",
        "Before chapter 1",
        "Before you begin",
        "The sounds",
        "breath",
    )
    body = body.replace(heading, header)
    header_end = body.index("</header>") + len("</header>")
    opening = body[header_end:]
    opening, lede_count = re.subn(
        r"<p>(.*?)</p>",
        r'<p class="primer-chapter-lede">\1</p>',
        opening,
        count=1,
        flags=re.S,
    )
    if lede_count != 1:
        raise ValueError(f"primer prelude has no lede: {repo_path}")
    body = body[:header_end] + opening
    body, section_count = re.subn(
        r"<h2>(.*?)</h2>",
        r'<h2 class="primer-reference-title">\1</h2>',
        body,
    )
    if section_count != 5:
        raise ValueError(
            f"primer prelude requires five reference sections: {repo_path}"
        )
    body, table_count = re.subn(
        r"<table>",
        '<table class="primer-sound-table">',
        body,
    )
    if table_count != 2:
        raise ValueError(f"primer prelude requires two sound tables: {repo_path}")
    body = mark_inline_phi(mark_primer_inline_phi(body))
    closing = (
        "<p>Now turn the page. From here on, the language will teach you "
        "itself.</p>"
    )
    if body.count(closing) != 1:
        raise ValueError(f"primer prelude closing changed: {repo_path}")
    return body.replace(
        closing,
        f'<aside class="primer-threshold-note">{closing}</aside>',
    )


def apply_primer_capstone(body, repo_path):
    """Give the capstone a bridge-page treatment without changing its source."""
    heading = "<h1>Capstone · the fable</h1>"
    if body.count(heading) != 1:
        raise ValueError(f"primer capstone heading changed: {repo_path}")
    header = primer_special_header(
        "Capstone",
        "After chapter 24",
        "The fable",
        "A bridge to the texts",
        "capstone",
        progress=100,
    )
    body = body.replace(heading, header)
    header_end = body.index("</header>") + len("</header>")
    opening = body[header_end:]
    opening, lede_count = re.subn(
        r"<p>(.*?)</p>",
        r'<p class="primer-chapter-lede">\1</p>',
        opening,
        count=1,
        flags=re.S,
    )
    if lede_count != 1:
        raise ValueError(f"primer capstone has no lede: {repo_path}")
    body = body[:header_end] + opening
    body, section_count = re.subn(
        r"<h2>(.*?)</h2>",
        r'<h2 class="primer-reference-title">\1</h2>',
        body,
    )
    if section_count != 1:
        raise ValueError(f"primer capstone requires one road section: {repo_path}")
    if body.count("<hr>") != 1:
        raise ValueError(f"primer capstone requires one closing rule: {repo_path}")
    chapter_body, closing = body.split("<hr>", 1)
    chapter_body = mark_inline_phi(mark_primer_inline_phi(chapter_body))
    section_at = chapter_body.index(
        '<h2 class="primer-reference-title">After the fable</h2>'
    )
    prefix, roads = chapter_body[:section_at], chapter_body[section_at:]
    road_index = 0

    def style_road(match):
        nonlocal road_index
        road_index += 1
        road_class = (
            "primer-road-intro" if road_index == 1 else "primer-capstone-road"
        )
        return f'<p class="{road_class}">{match.group(1)}</p>'

    roads = re.sub(r"<p>(.*?)</p>", style_road, roads, flags=re.S)
    if road_index != 4:
        raise ValueError(f"primer capstone requires three roads: {repo_path}")
    chapter_body = prefix + roads
    manual_label = "The manual"
    if chapter_body.count(manual_label) != 1:
        raise ValueError(f"primer capstone manual pointer changed: {repo_path}")
    chapter_body = chapter_body.replace(
        manual_label,
        '<a class="primer-manual-link" href="../manual/index.html">'
        f"{manual_label}</a>",
    )
    closing_match = re.fullmatch(
        r"\s*<p><em>(.*?)</em></p>\s*<p><em>(.*?)</em></p>\s*",
        closing,
        flags=re.S,
    )
    if (
        closing_match is None
        or not is_current_phi_passage(closing_match.group(1))
    ):
        raise ValueError(f"primer capstone farewell changed: {repo_path}")
    return (
        chapter_body
        + '<aside class="primer-capstone-farewell">'
        + '<blockquote class="primer-reading" aria-label="Phi passage">'
        + '<span class="primer-reading-line">'
        + f'<span class="primer-phi-line">{closing_match.group(1)}</span>'
        + "</span></blockquote>"
        + f'<p>{closing_match.group(2)}</p>'
        + "</aside>"
    )


def apply_primer_contents(body):
    """Shape the primer contents as a four-part reading ladder."""
    heading = "<h1>The Phi Primer</h1>"
    if body.count(heading) != 1:
        raise ValueError("primer contents heading changed")
    header = primer_special_header(
        "Primer",
        "Contents",
        "The Phi Primer",
        "Twenty-four chapters in four parts",
        "contents",
    )
    body = body.replace(heading, header)
    header_end = body.index("</header>") + len("</header>")
    opening = body[header_end:]
    opening, lede_count = re.subn(
        r"<p>(.*?)</p>",
        r'<p class="primer-chapter-lede">\1</p>',
        opening,
        count=1,
        flags=re.S,
    )
    if lede_count != 1:
        raise ValueError("primer contents has no lede")
    body = body[:header_end] + opening
    body, section_count = re.subn(
        r"<h2>(.*?)</h2>",
        r'<h2 class="primer-reference-title">\1</h2>',
        body,
    )
    if section_count != 4:
        raise ValueError("primer contents requires four named sections")

    ladder_index = 0

    def style_ladder(match):
        nonlocal ladder_index
        ladder_index += 1
        configured_label = PRIMER_EDITORIAL_PARTS[ladder_index - 1][
            "label"
        ].split(" · ", 1)
        if configured_label != [match.group(1), match.group(2)]:
            raise ValueError(
                "primer contents part label does not match editorial configuration"
            )
        rows = re.findall(
            r"<tr><td><a [^>]*>([0-9]+)</a></td><td>.*?</td>"
            r"<td>(.*?)</td></tr>",
            match.group(3),
            flags=re.S,
        )
        for chapter_text, story_title in rows:
            chapter = int(chapter_text)
            treatment = next(
                (
                    candidate
                    for candidate in PRIMER_EDITORIAL_PAGES.values()
                    if candidate["progress"]["current"] == chapter
                ),
                None,
            )
            if (
                treatment is None
                or treatment["story_title"]
                != html_module.unescape(re.sub(r"<[^>]+>", "", story_title))
            ):
                raise ValueError(
                    f"primer contents story title differs for chapter {chapter}"
                )
        return (
            f'<section class="primer-ladder-part primer-ladder-part-{ladder_index}">'
            '<h3>'
            f'<span class="primer-ladder-number">{match.group(1)}</span>'
            f'<span>{match.group(2)}</span>'
            "</h3>"
            f'<table class="primer-ladder">{match.group(3)}</table>'
            "</section>"
        )

    body = re.sub(
        r"<p><strong>(Part [IV]+): ([^<]+)</strong></p>\n"
        r"<table>(.*?)</table>",
        style_ladder,
        body,
        flags=re.S,
    )
    if ladder_index != len(PRIMER_EDITORIAL_PARTS):
        raise ValueError("primer contents ladder does not match configured parts")
    first_part = body.index('<section class="primer-ladder-part')
    last_part = body.rindex("</section>") + len("</section>")
    body = (
        body[:first_part]
        + '<div class="primer-ladder-grid">'
        + body[first_part:last_part]
        + "</div>"
        + body[last_part:]
    )
    body, capstone_count = re.subn(
        r"<p><strong>Capstone</strong>: (.*?)</p>",
        r'<p class="primer-contents-capstone"><strong>Capstone</strong>: \1</p>',
        body,
        flags=re.S,
    )
    if capstone_count != 1:
        raise ValueError("primer contents capstone pointer changed")
    body = mark_inline_phi(mark_primer_inline_phi(body))
    body, status_count = re.subn(
        (
            r'(<h2 class="primer-reference-title">Status</h2>)\n'
            r"<p>(.*?)</p>"
        ),
        r'\1\n<p class="primer-status-note">\2</p>',
        body,
        flags=re.S,
    )
    if status_count != 1:
        raise ValueError("primer contents status note changed")
    body, start_count = re.subn(
        r"<p>Start with (.*?)</p>",
        r'<p class="primer-start-note">Start with \1</p>',
        body,
        flags=re.S,
    )
    if start_count != 1:
        raise ValueError("primer contents start note changed")
    return body


(
    PRIMER_EDITORIAL_TOTAL,
    PRIMER_EDITORIAL_PARTS,
    PRIMER_EDITORIAL_PAGES,
) = load_primer_editorial()


NAV_PRIMER = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">walk</a> <span class="sep">&middot;</span> <a class="here" href="index.html">primer</a> <span class="sep">&middot;</span> <a href="../book/index.html">book</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

def primer_page(body, title, footer_nav="", editorial_kind=None):
    body_class = "landing primer"
    content = f"{body}\n{footer_nav}"
    if editorial_kind is not None:
        body_class += f" primer-editorial primer-{editorial_kind}-page"
        content = (
            f'<article class="primer-chapter primer-{editorial_kind}">\n'
            f"{body}\n{footer_nav}\n</article>"
        )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The Phi primer: learn a language for mindful and compassionate speech, one household chapter at a time.">
<title>Phi primer &mdash; {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="{body_class}">
{NAV_PRIMER}
<main>
{content}
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
    repo_path = f.relative_to(ROOT).as_posix()
    treatment = PRIMER_EDITORIAL_PAGES.get(repo_path)
    if treatment is not None:
        body = apply_primer_editorial(body, md, repo_path, treatment)
        editorial_kind = "lesson"
    elif f.name == "00_before_you_begin.md":
        body = apply_primer_prelude(body, repo_path)
        editorial_kind = "prelude"
    elif f.name == "25_capstone.md":
        body = apply_primer_capstone(body, repo_path)
        editorial_kind = "capstone"
    else:
        raise ValueError(f"primer page has no editorial treatment: {repo_path}")
    prev_link = f'<a href="{chapters[i-1].stem}.html">&lsaquo; {titles[chapters[i-1].name]}</a>' if i > 0 else ""
    next_link = f'<a href="{chapters[i+1].stem}.html">{titles[chapters[i+1].name]} &rsaquo;</a>' if i + 1 < len(chapters) else ""
    footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    (PRIMER_OUT / (f.stem + ".html")).write_text(
        primer_page(
            link_text_citations(body),
            titles[f.name],
            footer_nav,
            editorial_kind=editorial_kind,
        )
    )

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
readme_body = link_text_citations(readme_body) + "\n" + start_end
readme_body = apply_primer_contents(readme_body)
(PRIMER_OUT / "index.html").write_text(
    primer_page(readme_body, "contents", editorial_kind="contents")
)
print(f"wrote build/site/primer/: {len(chapters)} chapters + contents")

# ---- manual reader: manual/**.md rendered to build/site/manual/ ----
MANUAL_SRC = ROOT / "manual"
MANUAL_OUT = BUILD_SITE / "manual"
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

NAV_MANUAL = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">walk</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../book/index.html">book</a> <span class="sep">&middot;</span> <a class="here" href="index.html">manual</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

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


MANUAL_SITE_PATHS = {path.resolve(): slug(path) for _, _, path in sections}
MODULE_LEXICON = (MANUAL_SRC / "part7_reference" / "lexicon" / "by_module.md").resolve()


def link_manual_pages(html, source):
    """Point relative manual Markdown links at their flattened site pages."""
    def rewrite(match):
        href = match.group(1)
        path, separator, fragment = href.partition("#")
        target = (source.parent / path).resolve()
        if target == MODULE_LEXICON:
            suffix = f"?module={fragment}" if separator else ""
            return f'href="../explore.html{suffix}"'
        site_path = MANUAL_SITE_PATHS.get(target)
        if site_path:
            suffix = f"#{fragment}" if separator else ""
            return f'href="{site_path}{suffix}"'
        return match.group(0)

    return re.sub(r'href="([^"]+\.md(?:#[^"]*)?)"', rewrite, html)


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
    linked_body = link_manual_pages(link_text_citations(body), f)
    (MANUAL_OUT / slug(f)).write_text(manual_page(linked_body, sec_titles[i], footer_nav))

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
print(f"wrote build/site/manual/: {len(sections)} sections + contents")

# ---- the Phi book: available chapters rendered as a work in progress ----
BOOK_SRC = ROOT / "book"
BOOK_OUT = BUILD_SITE / "book"
prepare_html_output(BOOK_OUT)
NAV_BOOK = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">walk</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a class="here" href="index.html">book</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="../pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'


def load_editorial_pages():
    """Load opt-in editorial treatments and reject stale source paths."""
    config_path = SITE_SRC / "editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    pages = config.get("pages")
    if set(config) != {"pages"} or not isinstance(pages, dict):
        raise ValueError("site/editorial.json must contain one 'pages' object")
    for repo_path, treatment in pages.items():
        source_path = ROOT / repo_path
        if not source_path.is_file():
            raise ValueError(f"editorial source does not exist: {repo_path}")
        if not isinstance(treatment, dict):
            raise ValueError(
                f"editorial treatment for {repo_path} must be an object"
            )
        fields = set(treatment)
        if "pull_quotes" not in fields or not fields <= {"eyebrow", "pull_quotes"}:
            raise ValueError(
                f"editorial treatment for {repo_path} requires 'pull_quotes' "
                "and permits an optional 'eyebrow'"
            )
        quotes = treatment["pull_quotes"]
        if not isinstance(quotes, list) or not quotes or any(
            not isinstance(quote, str) or not quote.strip() for quote in quotes
        ):
            raise ValueError(
                f"editorial pull_quotes for {repo_path} must be a non-empty string list"
            )
        if len(quotes) != len(set(quotes)):
            raise ValueError(f"editorial pull_quotes repeat in {repo_path}")
        eyebrow = treatment.get("eyebrow")
        if eyebrow is not None and (
            not isinstance(eyebrow, str) or not eyebrow.strip()
        ):
            raise ValueError(
                f"editorial eyebrow for {repo_path} must be a non-empty string"
            )
    return pages


def mark_drop_cap(paragraph):
    """Wrap the first visible letter while preserving it for assistive tools."""
    in_tag = False
    in_entity = False
    for index, char in enumerate(paragraph):
        if char == "<" and not in_entity:
            in_tag = True
        elif char == ">" and in_tag:
            in_tag = False
        elif char == "&" and not in_tag:
            in_entity = True
        elif char == ";" and in_entity:
            in_entity = False
        elif not in_tag and not in_entity and char.isalpha():
            return (
                paragraph[:index]
                + f'<span class="drop-cap">{char}</span>'
                + paragraph[index + 1:]
            )
    raise ValueError("editorial opening paragraph has no visible letter")


def apply_book_editorial(body, source, repo_path, treatment):
    """Generate the chapter furniture named in site/editorial.json."""
    chapter_match = re.match(r"book/([0-9]+)_", repo_path)
    if not chapter_match:
        raise ValueError(f"editorial book path lacks a chapter number: {repo_path}")
    chapter_number = int(chapter_match.group(1))
    eyebrow = treatment.get("eyebrow", f"Chapter {chapter_number}")
    body, heading_count = re.subn(
        r"(<h1>.*?</h1>)",
        rf'<p class="chapter-eyebrow">{html_module.escape(eyebrow)}</p>\n\1',
        body,
        count=1,
        flags=re.S,
    )
    if heading_count != 1:
        raise ValueError(f"editorial source must have one level-one heading: {repo_path}")

    lede_match = re.search(r"<p>(.*?)</p>", body, flags=re.S)
    if lede_match is None:
        raise ValueError(f"editorial source has no opening paragraph: {repo_path}")
    marked_lede = mark_drop_cap(lede_match.group(1))
    body = (
        body[:lede_match.start()]
        + f'<p class="chapter-lede">{marked_lede}</p>'
        + body[lede_match.end():]
    )
    body = mark_inline_phi(body)

    paragraph_matches = list(re.finditer(r"<p>.*?</p>", body, flags=re.S))
    contexts = {}
    for quote in treatment["pull_quotes"]:
        if source.count(quote) != 1:
            raise ValueError(
                f"editorial pull quote must occur exactly once in {repo_path}: {quote!r}"
            )
        escaped_quote = html_module.escape(quote, quote=False)
        containing = [
            match for match in paragraph_matches
            if escaped_quote in match.group(0)
        ]
        if len(containing) != 1:
            raise ValueError(
                f"editorial pull quote did not survive rendering in {repo_path}: {quote!r}"
            )
        aside = (
            '<aside class="chapter-pullquote" aria-hidden="true">'
            f"<p>{escaped_quote}</p></aside>\n"
        )
        paragraph = containing[0]
        contexts.setdefault((paragraph.start(), paragraph.end()), []).append(aside)
    for (start, end), asides in sorted(contexts.items(), reverse=True):
        context = (
            '<div class="pullquote-context">\n'
            + "".join(asides)
            + body[start:end]
            + "\n</div>"
        )
        body = body[:start] + context + body[end:]
    return body


EDITORIAL_PAGES = load_editorial_pages()


def book_page(body, title, footer_nav="", editorial=False):
    body_class = "landing primer book-editorial" if editorial else "landing primer"
    content = (
        f'<article class="chapter-copy">\n{body}\n{footer_nav}\n</article>'
        if editorial else f"{body}\n{footer_nav}"
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The book about why Phi was made this way and what the evidence permits it to claim.">
<title>Phi book: {title}</title>
<script src="../theme.js"></script>
<script src="../reader.js" defer></script>
<link rel="stylesheet" href="../style.css">
</head>
<body class="{body_class}">
{NAV_BOOK}
<main>
{content}
</main>
<footer>
  <p>The book was written in public. Its source chapters live in
     <a href="https://github.com/dcellison/phi/tree/main/book">the repository</a>, and the site renders them at build time.
     The <a href="../colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""


book_chapters = sorted(BOOK_SRC.glob("[0-9][0-9]_*.md")) + [p for p in [BOOK_SRC / "bibliography.md"] if p.exists()]
book_titles = {chapter.name: title_of(chapter.read_text()) for chapter in book_chapters}
for i, chapter in enumerate(book_chapters):
    source = chapter.read_text()
    repo_path = chapter.relative_to(ROOT).as_posix()
    treatment = EDITORIAL_PAGES.get(repo_path)
    body = link_text_citations(md_to_html(source))
    if treatment is not None:
        body = apply_book_editorial(body, source, repo_path, treatment)
    prev_link = (
        f'<a href="{book_chapters[i - 1].stem}.html">'
        f'&lsaquo; {book_titles[book_chapters[i - 1].name]}</a>'
        if i > 0 else ""
    )
    next_link = (
        f'<a href="{book_chapters[i + 1].stem}.html">'
        f'{book_titles[book_chapters[i + 1].name]} &rsaquo;</a>'
        if i + 1 < len(book_chapters) else ""
    )
    chapter_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    (BOOK_OUT / f"{chapter.stem}.html").write_text(
        book_page(
            body,
            book_titles[chapter.name],
            chapter_nav,
            editorial=treatment is not None,
        )
    )

book_readme = md_to_html((BOOK_SRC / "README.md").read_text())
book_readme = re.sub(
    r'href="([0-9][0-9]_[a-z0-9_]+|bibliography)\.md"',
    r'href="\1.html"',
    book_readme,
)
(BOOK_OUT / "index.html").write_text(book_page(book_readme, "contents"))
print(f"wrote build/site/book/: {len(book_chapters)} chapters + contents")

# ---- the texts: translated, transmuted, and original literature rendered to build/site/texts/ ----
import tengwar

PHI_WORDS = {e["word"] for e in entries}

TEXT_MOTIFS = {
    "wind_sun",
    "people_equal",
    "dwelling_garden",
    "wool_journey",
    "water_open",
    "lotus_circle",
    "words_seed",
}


def load_texts_editorial():
    """Load opt-in literary treatments and reject stale source assumptions."""
    config_path = SITE_SRC / "texts_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or set(config) != {"pages"}:
        raise ValueError("site/texts_editorial.json must contain one 'pages' object")
    pages = config["pages"]
    if not isinstance(pages, dict):
        raise ValueError("site/texts_editorial.json pages must be an object")

    catalogued = {f"texts/{work['path']}": work for work in TEXTS}
    resolved = {}
    shared_required = {
        "form",
        "phi_title",
        "motif",
        "sections",
        "opening_paragraphs",
        "interlinear_blocks",
        "interlinear_stanzas",
        "source_free_blocks",
        "source_free_stanzas",
        "complete_readings",
        "notes",
        "tables",
        "pillar_sections",
        "inner_dividers",
    }
    for repo_path, treatment in pages.items():
        if (
            repo_path not in catalogued
            or not (ROOT / repo_path).is_file()
            or not isinstance(treatment, dict)
        ):
            raise ValueError(f"invalid texts editorial source: {repo_path}")
        form = treatment.get("form")
        form_fields = {
            "paired": set(),
            "collection": {"reading_map"},
        }
        if form not in form_fields:
            raise ValueError(f"unknown texts editorial form: {form}")
        required = shared_required | form_fields[form]
        if set(treatment) != required:
            raise ValueError(
                f"texts editorial treatment for {repo_path} requires "
                f"{', '.join(sorted(required))}"
            )
        if treatment["motif"] not in TEXT_MOTIFS:
            raise ValueError(f"unknown texts editorial motif: {treatment['motif']}")
        work = catalogued[repo_path]
        if work["method"] != "Translation + transmutation":
            raise ValueError(
                f"paired texts editorial source has incompatible method: {repo_path}"
            )

        source = (ROOT / repo_path).read_text(encoding="utf-8")
        source_title = title_of(source)
        if source_title != work["title"] or " — " not in source_title:
            raise ValueError(
                f"texts editorial title differs from the catalogue: {repo_path}"
            )
        phi_title, english_title = source_title.split(" — ", 1)
        if (
            treatment["phi_title"] != phi_title
            or not is_current_phi(phi_title)
            or not english_title.strip()
        ):
            raise ValueError(f"invalid texts editorial Phi title: {repo_path}")

        sections = treatment["sections"]
        source_sections = re.findall(r"^## (.+)$", source, flags=re.M)
        section_fields = {"title", "kind"}
        section_kinds = {
            "translation",
            "translation_detail",
            "transmutation",
            "comparison",
            "collection_detail",
        }
        if (
            not isinstance(sections, list)
            or not sections
            or any(
                not isinstance(section, dict)
                or set(section) != section_fields
                or not isinstance(section["title"], str)
                or not section["title"]
                or section["kind"] not in section_kinds
                for section in sections
            )
            or len({section["title"] for section in sections}) != len(sections)
            or [section["title"] for section in sections] != source_sections
        ):
            raise ValueError(
                f"texts editorial sections differ from the source: {repo_path}"
            )
        major_sections = [
            section for section in sections
            if section["kind"] != "translation_detail"
        ]
        major_kinds = [section["kind"] for section in major_sections]
        expected_kinds = {
            "paired": ["translation", "transmutation", "comparison"],
            "collection": [
                "transmutation",
                "translation",
                "transmutation",
                "comparison",
                "transmutation",
                "collection_detail",
            ],
        }
        if major_kinds != expected_kinds[form]:
            raise ValueError(
                f"texts editorial sections have the wrong order for {form}: "
                f"{repo_path}"
            )
        if form == "collection":
            reading_map = treatment["reading_map"]
            reading_map_fields = {"label", "method", "target"}
            section_titles = {section["title"] for section in sections}
            if (
                not isinstance(reading_map, list)
                or len(reading_map) < 2
                or any(
                    not isinstance(item, dict)
                    or set(item) != reading_map_fields
                    or any(
                        not isinstance(item[field], str) or not item[field]
                        for field in reading_map_fields
                    )
                    or item["target"] not in section_titles
                    for item in reading_map
                )
                or len({item["label"] for item in reading_map}) != len(reading_map)
                or len({item["target"] for item in reading_map}) != len(reading_map)
            ):
                raise ValueError(
                    f"texts editorial reading map differs from the source: "
                    f"{repo_path}"
                )
        for field in (
            "opening_paragraphs",
            "interlinear_blocks",
            "interlinear_stanzas",
            "source_free_blocks",
            "source_free_stanzas",
            "complete_readings",
            "notes",
            "tables",
            "pillar_sections",
            "inner_dividers",
        ):
            if not isinstance(treatment[field], int) or treatment[field] < 0:
                raise ValueError(
                    f"texts editorial {field} must be a non-negative integer: "
                    f"{repo_path}"
                )
        resolved[repo_path] = {**treatment, "work": work}
    return resolved


def texts_motif(name):
    """Return the restrained Lucide motif for an editorial text."""
    # Lucide outlines; the deployed site carries the project's ISC notice.
    wind = """
    <path d="M12.8 19.6A2 2 0 1 0 14 16H2"/>
    <path d="M17.5 8a2.5 2.5 0 1 1 2 4H2"/>
    <path d="M9.8 4.4A2 2 0 1 1 11 8H2"/>"""
    sun = """
    <circle cx="12" cy="12" r="4"/>
    <path d="M12 2v2"/><path d="M12 20v2"/>
    <path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/>
    <path d="M2 12h2"/><path d="M20 12h2"/>
    <path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>"""
    people = """
    <path d="M18 21a8 8 0 0 0-16 0"/>
    <circle cx="10" cy="8" r="5"/>
    <path d="M22 20c0-3.37-2-6.5-4-8a5 5 0 0 0-.45-8.3"/>"""
    equal = """
    <path d="M5 9h14"/>
    <path d="M5 15h14"/>"""
    dwelling = """
    <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/>
    <path d="M3 10a2 2 0 0 1 .71-1.53l7-6a2 2 0 0 1 2.58 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>"""
    sprout = """
    <path d="M7 20h8"/>
    <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
    <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5 0-4.6-.7-1.1-.8-1.8-2.2-2.3-3.7 2-.4 3.5 0 4.6.7z"/>
    <path d="M14.1 6a7 7 0 0 0-1.9 2.8c1.7.3 3.1 0 4.1-.7 1-.7 1.6-1.9 2-3.3-1.8-.3-3.2 0-4.2.7z"/>"""
    words = """
    <path d="M21 15a4 4 0 0 1-4 4H8l-5 3V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4z"/>
    <path d="M8 8h8"/><path d="M8 12h5"/>"""
    waves = """
    <path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5s2.5 2 5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>
    <path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>
    <path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>"""
    journey = """
    <path d="M18 8l4 4-4 4"/>
    <path d="M2 12h20"/>"""
    circle = """
    <circle cx="12" cy="12" r="9"/>"""
    lotus = """
    <path d="M12 5a3 3 0 1 1 3 3m-3-3a3 3 0 1 0-3 3m3-3v1M9 8a3 3 0 1 0 3 3M9 8h1m5 0a3 3 0 1 1-3 3m3-3h-1m-2 3v-1"/>
    <circle cx="12" cy="8" r="2"/>
    <path d="M12 10v12"/>
    <path d="M12 22c4.2 0 7-1.667 7-5-4.2 0-7 1.667-7 5Z"/>
    <path d="M12 22c-4.2 0-7-1.667-7-5 4.2 0 7 1.667 7 5Z"/>"""
    motifs = {
        "wind_sun": (wind, sun),
        "people_equal": (people, equal),
        "dwelling_garden": (dwelling, sprout),
        "wool_journey": (waves, journey),
        "water_open": (waves, circle),
        "lotus_circle": (circle, lotus),
        "words_seed": (words, sprout),
    }
    if name not in motifs:
        raise ValueError(f"unknown texts motif: {name}")
    first, second = motifs[name]
    return (
        f'<div class="text-work-motif text-work-motif-{name}" aria-hidden="true">'
        f'<svg viewBox="0 0 24 24" focusable="false">{first}</svg>'
        f'<svg viewBox="0 0 24 24" focusable="false">{second}</svg>'
        "</div>"
    )


def text_section_icon(kind):
    """Return a Lucide mark for a translation, transmutation, or comparison."""
    paths = {
        "translation": (
            '<path d="M21 6H3"/><path d="M15 12H3"/>'
            '<path d="M17 18H3"/>'
        ),
        "transmutation": (
            '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2'
            'c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>'
            '<path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
        ),
        "comparison": (
            '<path d="M8 3 4 7l4 4"/><path d="M4 7h16"/>'
            '<path d="m16 21 4-4-4-4"/><path d="M20 17H4"/>'
        ),
        "collection_detail": (
            '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>'
            '<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
        ),
    }
    if kind not in paths:
        raise ValueError(f"unknown texts section kind: {kind}")
    return (
        '<span class="text-section-icon" aria-hidden="true">'
        f'<svg viewBox="0 0 24 24" focusable="false">{paths[kind]}</svg>'
        "</span>"
    )


def text_heading_slug(title):
    """Make a stable fragment identifier from one validated section title."""
    return re.sub(
        r"[^a-z0-9]+",
        "-",
        html_module.unescape(re.sub(r"<[^>]+>", "", title)).lower(),
    ).strip("-")


def text_reading_map(treatment):
    """Build the reading map shown before a treated literary work."""
    if treatment["form"] == "paired":
        map_items = [
            {
                "label": section["title"],
                "method": None,
                "target": section["title"],
            }
            for section in treatment["sections"]
            if section["kind"] != "translation_detail"
        ]
    else:
        map_items = treatment["reading_map"]
    links = []
    for index, item in enumerate(map_items, 1):
        method = ""
        if item["method"] is not None:
            method = (
                '<span class="text-map-method">'
                f'{html_module.escape(item["method"])}</span>'
            )
        links.append(
            "<li>"
            f'<a href="#{text_heading_slug(item["target"])}">'
            f'<span class="text-map-number">{index:02d}</span>'
            '<span class="text-map-copy">'
            f'<span class="text-map-title">{html_module.escape(item["label"])}</span>'
            f"{method}</span>"
            "</a></li>"
        )
    return (
        '<nav class="text-reading-map" aria-label="In this text">'
        '<p class="text-reading-map-label">In this text</p>'
        f'<ol>{"".join(links)}</ol>'
        "</nav>"
    )


def is_text_phi_passage(value):
    """Accept current Phi plus the square brackets used to expose clause shape."""
    text = html_module.unescape(value).strip()
    depth = 0
    for character in text:
        if character == "[":
            depth += 1
        elif character == "]":
            depth -= 1
            if depth < 0:
                return False
    if depth != 0:
        return False
    unbracketed = re.sub(r"\s+", " ", text.replace("[", "").replace("]", ""))
    return is_current_phi_passage(unbracketed)


def style_text_fences(body, repo_path, treatment):
    """Turn a paired work's exact fences into readings and interlinear rows."""
    counts = {
        "interlinear_blocks": 0,
        "interlinear_stanzas": 0,
        "source_free_blocks": 0,
        "source_free_stanzas": 0,
        "complete_readings": 0,
    }

    def stanza(phi, gloss, literal, source_name=None, source_line=None):
        source = ""
        class_name = "text-stanza"
        if source_name is not None:
            source = (
                '<p class="text-source-line">'
                f'<span class="text-source-name">{source_name}:</span> '
                f"<span>{source_line}</span></p>"
            )
        else:
            class_name += " text-stanza-source-free"
        return (
            f'<figure class="{class_name}">'
            '<div class="text-stanza-language">'
            f'<p class="text-phi-line" lang="art-x-phi">{phi}</p>'
            '<p class="text-gloss-line">'
            '<span class="visually-hidden">Word-by-word gloss: </span>'
            f"{gloss}</p>"
            "</div>"
            "<figcaption>"
            '<p class="text-literal-line">'
            '<span class="visually-hidden">Literal English: </span>'
            f"{literal}</p>"
            f"{source}"
            "</figcaption>"
            "</figure>"
        )

    def convert(match):
        raw = match.group(1).strip()
        groups = re.split(r"\n[ \t]*\n", raw)
        parsed = []
        for group in groups:
            lines = [line.strip() for line in group.splitlines()]
            if len(lines) != 4:
                parsed = []
                break
            source_match = re.fullmatch(
                r"([a-z][a-z0-9-]*):\s*(.+)",
                lines[3],
                flags=re.S,
            )
            if (
                not is_text_phi_passage(lines[0])
                or not lines[2].startswith("(")
                or not lines[2].endswith(")")
                or source_match is None
            ):
                parsed = []
                break
            parsed.append(
                (lines[0], lines[1], lines[2], source_match.group(1), source_match.group(2))
            )

        if parsed:
            counts["interlinear_blocks"] += 1
            counts["interlinear_stanzas"] += len(parsed)
            stanzas = [
                stanza(phi, gloss, literal, source_name, source_line)
                for phi, gloss, literal, source_name, source_line in parsed
            ]
            return (
                '<div class="text-interlinear" aria-label="Interlinear passage">'
                + "".join(stanzas)
                + "</div>"
            )

        source_free = []
        for group in groups:
            lines = [line.strip() for line in group.splitlines()]
            if (
                len(lines) != 3
                or not is_text_phi_passage(lines[0])
                or not lines[2].startswith("(")
                or not lines[2].endswith(")")
            ):
                source_free = []
                break
            source_free.append((lines[0], lines[1], lines[2]))
        if source_free:
            counts["source_free_blocks"] += 1
            counts["source_free_stanzas"] += len(source_free)
            stanzas = [
                stanza(phi, gloss, literal)
                for phi, gloss, literal in source_free
            ]
            return (
                '<div class="text-interlinear text-interlinear-source-free" '
                'aria-label="Phi passage without a source line">'
                + "".join(stanzas)
                + "</div>"
            )

        readings = [group.strip() for group in groups if group.strip()]
        if readings and all(
            "\n" not in reading and is_text_phi_passage(reading)
            for reading in readings
        ):
            counts["complete_readings"] += 1
            lines = []
            for index, reading in enumerate(readings):
                class_name = (
                    "text-reading-line text-reading-title"
                    if index == 0
                    else "text-reading-line"
                )
                lines.append(
                    f'<p class="{class_name}" lang="art-x-phi">{reading}</p>'
                )
            return (
                '<section class="text-complete-reading" '
                'aria-label="Complete Phi reading">'
                + "".join(lines)
                + "</section>"
            )

        first_line = raw.splitlines()[0][:80] if raw else "(empty)"
        raise ValueError(
            f"unrecognized editorial text fence in {repo_path}: {first_line}"
        )

    body = re.sub(r"<pre>(.*?)</pre>", convert, body, flags=re.S)
    for field, actual in counts.items():
        if actual != treatment[field]:
            raise ValueError(
                f"texts editorial {field} differs in {repo_path}: "
                f"expected {treatment[field]}, found {actual}"
            )
    if "<pre>" in body:
        raise ValueError(f"editorial text left an untreated fence in {repo_path}")
    return body


def style_text_tables(body, repo_path, treatment):
    """Give each literary table labels that remain useful on phones."""
    count = 0

    def convert(match):
        nonlocal count
        rows = re.findall(r"<tr>(.*?)</tr>", match.group(1), flags=re.S)
        if not rows:
            raise ValueError(f"empty editorial text table in {repo_path}")
        headers = tuple(re.findall(r"<th>(.*?)</th>", rows[0], flags=re.S))
        plain_headers = [
            html_module.unescape(re.sub(r"<[^>]+>", "", header)).strip()
            for header in headers
        ]
        if (
            not 2 <= len(headers) <= 4
            or any(not header for header in plain_headers)
            or len(set(plain_headers)) != len(plain_headers)
        ):
            raise ValueError(
                f"unrecognized editorial text table in {repo_path}: {headers}"
            )
        rebuilt = ["<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>"]
        for row in rows[1:]:
            cells = re.findall(r"<td>(.*?)</td>", row, flags=re.S)
            if len(cells) != len(headers):
                raise ValueError(f"uneven editorial text table in {repo_path}")
            rendered_cells = []
            for header, cell in zip(headers, cells):
                label = html_module.escape(
                    html_module.unescape(re.sub(r"<[^>]+>", "", header)),
                    quote=True,
                )
                rendered_cells.append(f'<td data-label="{label}">{cell}</td>')
            rebuilt.append("<tr>" + "".join(rendered_cells) + "</tr>")
        count += 1
        width_class = (
            "text-ledger-wide" if len(headers) == 4 else "text-ledger-compact"
        )
        return (
            '<div class="text-ledger-wrap">'
            f'<table class="text-ledger {width_class}">'
            + "".join(rebuilt)
            + "</table></div>"
        )

    body = re.sub(r"<table>(.*?)</table>", convert, body, flags=re.S)
    if count != treatment["tables"]:
        raise ValueError(
            f"texts editorial table count differs in {repo_path}: "
            f"expected {treatment['tables']}, found {count}"
        )
    return body


def style_text_subheadings(body):
    """Mark scenes, readings, ledgers, and pillar reflections distinctly."""
    pillars = {
        "Solarpunk values",
        "Secular Buddhist philosophy",
        "Art Nouveau aesthetics",
        "Peace linguistics",
        "Pre-industrial wisdom",
    }

    def convert(match):
        title = match.group(1)
        plain = html_module.unescape(re.sub(r"<[^>]+>", "", title))
        if plain.startswith("Complete "):
            kind = "text-reading-heading"
        elif "limits" in plain.lower() or "gap log" in plain.lower():
            kind = "text-ledger-heading"
        elif plain in pillars:
            kind = "text-pillar-heading"
        else:
            kind = "text-scene-heading"
        if " — " in title:
            phi, english = title.split(" — ", 1)
            if is_current_phi(phi):
                title = (
                    f'<span class="text-subheading-phi" lang="art-x-phi">{phi}</span>'
                    '<span class="visually-hidden">, </span>'
                    f'<span class="text-subheading-english">{english}</span>'
                )
        return f'<h3 class="{kind}">{title}</h3>'

    return re.sub(r"<h3>(.*?)</h3>", convert, body, flags=re.S)


def mark_text_inline_phi(body):
    """Apply the shared inline treatment in literary prose and ledgers."""
    def mark_fragment(match):
        fragment = match.group(0)

        def mark_code(code_match):
            if not is_current_phi(code_match.group(1)):
                return code_match.group(0)
            return f'<code class="phi-inline">{code_match.group(1)}</code>'

        return re.sub(r"<code>([^<]+)</code>", mark_code, fragment)

    return re.sub(
        r"<(?:p|td|li)(?: [^>]*)?>.*?</(?:p|td|li)>",
        mark_fragment,
        body,
        flags=re.S,
    )


def group_text_pillars(body, repo_path, treatment):
    """Pair each five-pillar heading with the reflection that belongs to it."""
    body, count = re.subn(
        (
            r'(<h3 class="text-pillar-heading">.*?</h3>)\s*'
            r"(<p>.*?</p>)"
        ),
        r'<section class="text-pillar-reflection">\1\2</section>',
        body,
        flags=re.S,
    )
    if count != treatment["pillar_sections"]:
        raise ValueError(
            f"texts editorial pillar count differs in {repo_path}: "
            f"expected {treatment['pillar_sections']}, found {count}"
        )
    return body


def text_method_heading(title, kind, form):
    """Build a major method heading with its nonverbal mark."""
    kind_class = kind.replace("_", "-")
    heading = html_module.escape(title)
    if form == "collection" and kind != "collection_detail" and ": " in title:
        teaching, method = title.split(": ", 1)
        heading = (
            '<span class="text-heading-copy">'
            f'<span class="text-teaching-name">{html_module.escape(teaching)}</span>'
            '<span class="visually-hidden">: </span>'
            f'<span class="text-rendering-kind">{html_module.escape(method)}</span>'
            "</span>"
        )
    return (
        f'<h2 class="text-method-heading text-{kind_class}-heading" '
        f'id="{text_heading_slug(title)}">'
        f"{text_section_icon(kind)}"
        f"{heading}"
        "</h2>"
    )


def apply_text_editorial(body, source, repo_path, treatment):
    """Apply the anthology treatment to one validated literary work."""
    source_title = title_of(source)
    phi_title, english_title = source_title.split(" — ", 1)
    heading = re.search(r"<h1>(.*?)</h1>", body, flags=re.S)
    if heading is None or html_module.unescape(heading.group(1)) != source_title:
        raise ValueError(f"editorial text has no matching heading: {repo_path}")
    tengwar_title = tengwar.render_line(phi_title)
    if tengwar_title is None:
        raise ValueError(f"editorial text title cannot render in Tengwar: {repo_path}")
    title_class = (
        ' class="text-work-title-long"'
        if len(english_title) > 44
        else ""
    )
    if treatment["form"] == "paired":
        method_label = (
            '<span>Translation</span><span aria-hidden="true">+</span>'
            '<span>transmutation</span>'
        )
    else:
        method_label = (
            '<span>Transmutations</span><span aria-hidden="true">+</span>'
            '<span>paired teaching</span>'
        )
    header = f"""
<header class="text-work-header">
  <div class="text-work-meta">
    <p class="text-shelf-label">Phi texts</p>
    <p class="text-work-method">{method_label}</p>
  </div>
  <div class="text-work-title-row">
    <div class="text-work-title-copy">
      <p class="text-phi-title" lang="art-x-phi">{html_module.escape(phi_title)}</p>
      <h1{title_class}>{html_module.escape(english_title)}</h1>
    </div>
    {texts_motif(treatment["motif"])}
  </div>
  <div class="text-title-tengwar" aria-hidden="true">{tengwar_title}</div>
</header>""".strip()
    body = body[:heading.start()] + header + body[heading.end():]

    opening_pattern = re.compile(
        r"(</header>)\s*((?:<p><em>.*?</em></p>\s*)+)<hr>",
        flags=re.S,
    )
    opening = opening_pattern.search(body)
    if opening is None:
        raise ValueError(f"editorial text opening differs in {repo_path}")
    opening_paragraphs = re.findall(
        r"<p><em>(.*?)</em></p>",
        opening.group(2),
        flags=re.S,
    )
    if len(opening_paragraphs) != treatment["opening_paragraphs"]:
        raise ValueError(
            f"texts editorial opening paragraph count differs in {repo_path}: "
            f"expected {treatment['opening_paragraphs']}, "
            f"found {len(opening_paragraphs)}"
        )
    reader_notes = "".join(
        f'<p class="text-reader-note">{paragraph}</p>'
        for paragraph in opening_paragraphs[1:]
    )
    rendered_opening = (
        f"{opening.group(1)}"
        '<section class="text-work-opening">'
        f'<p class="text-work-lede">{opening_paragraphs[0]}</p>'
        f'<div class="text-reader-notes">{reader_notes}</div>'
        f'{text_reading_map(treatment)}'
        "</section>"
    )
    body = body[:opening.start()] + rendered_opening + body[opening.end():]

    for section in treatment["sections"]:
        if section["kind"] != "translation_detail":
            continue
        original = f'<h2>{html_module.escape(section["title"])}</h2>'
        if body.count(original) != 1:
            raise ValueError(
                f"editorial text section heading differs in {repo_path}: "
                f"{section['title']}"
            )
        body = body.replace(
            original,
            f'<h3>{html_module.escape(section["title"])}</h3>',
        )

    major_sections = [
        section for section in treatment["sections"]
        if section["kind"] != "translation_detail"
    ]
    markers = []
    for section in major_sections:
        title = section["title"]
        kind = section["kind"]
        original = f"<h2>{html_module.escape(title)}</h2>"
        if body.count(original) != 1:
            raise ValueError(
                f"editorial text section heading differs in {repo_path}: {title}"
            )
        marker = text_method_heading(title, kind, treatment["form"])
        body = body.replace(original, marker)
        markers.append(marker)

    positions = [body.index(marker) for marker in markers]
    prefix = body[:positions[0]]
    sections = []
    for index, section_spec in enumerate(major_sections):
        kind = section_spec["kind"]
        end = positions[index + 1] if index + 1 < len(positions) else len(body)
        section = body[positions[index]:end]
        section = re.sub(r"\s*<hr>\s*$", "", section)
        if kind in {"translation", "transmutation"}:
            class_name = f"text-rendering text-{kind}"
        elif kind == "comparison":
            class_name = "text-comparison"
        else:
            class_name = "text-collection-detail"
        sections.append(f'<section class="{class_name}">{section}</section>')
    body = prefix + "".join(sections)
    if body.count("<hr>") != treatment["inner_dividers"]:
        raise ValueError(
            f"texts editorial inner divider count differs in {repo_path}: "
            f"expected {treatment['inner_dividers']}, found {body.count('<hr>')}"
        )
    body = body.replace(
        "<hr>",
        '<div class="text-inner-divider" aria-hidden="true"></div>',
    )

    body = style_text_subheadings(body)
    body = style_text_fences(body, repo_path, treatment)
    body, note_count = re.subn(
        r"<p><strong>Notes:</strong>\s*(.*?)</p>",
        (
            '<aside class="text-notes">'
            '<p><span class="text-notes-label">Notes:</span> '
            r"\1</p></aside>"
        ),
        body,
        flags=re.S,
    )
    if note_count != treatment["notes"]:
        raise ValueError(
            f"texts editorial note count differs in {repo_path}: "
            f"expected {treatment['notes']}, found {note_count}"
        )
    body = style_text_tables(body, repo_path, treatment)
    body = group_text_pillars(body, repo_path, treatment)
    body = mark_text_inline_phi(body)
    return body


TEXT_EDITORIAL_PAGES = load_texts_editorial()

# Every headword's Tengwar hand, as compact placement data over one shared
# glyph dictionary rather than a full SVG per word: the explorer assembles
# the same markup render_line() produces, and the coordinates ship already
# rounded so the browser does string work only.
teng_words = {}
teng_glyph_keys = set()
for headword in sorted(PHI_WORDS):
    laid = tengwar.layout_line(headword)
    if laid is None:
        continue
    placed, (txmin, tymin, txmax, tymax) = laid
    tw, th = txmax - txmin, tymax - tymin
    teng_words[headword] = {
        "p": [[key, int(f"{gx:.0f}"), int(f"{gy:.0f}")] for key, gx, gy in placed],
        "vb": [int(f"{txmin:.0f}"), int(f"{-tymax:.0f}"), int(f"{tw:.0f}"), int(f"{th:.0f}")],
        "em": f"{th / tengwar.UPEM:.2f}",
    }
    teng_glyph_keys.update(key for key, _, _ in placed)
teng_out = BUILD_SITE / "tengwar_words.json"
teng_out.write_text(json.dumps(
    {"glyphs": {key: tengwar.glyph_path(key) for key in sorted(teng_glyph_keys)},
     "words": teng_words},
    ensure_ascii=False, separators=(",", ":")))
print(f"wrote {teng_out.relative_to(ROOT)}: {len(teng_words)} words, {teng_out.stat().st_size // 1024} KB")

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

TEXTS_OUT = BUILD_SITE / "texts"
prepare_html_output(TEXTS_OUT)


def texts_nav(depth):
    root_prefix = "../" * depth
    texts_index = "index.html" if depth == 1 else "../index.html"
    return f'<nav class="topnav"><a href="{root_prefix}index.html">kia</a> <span class="sep">&middot;</span> <a href="{root_prefix}short_road.html">walk</a> <span class="sep">&middot;</span> <a href="{root_prefix}primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="{root_prefix}book/index.html">book</a> <span class="sep">&middot;</span> <a href="{root_prefix}manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="{root_prefix}pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a class="here" href="{texts_index}">texts</a> <span class="sep">&middot;</span> <a href="{root_prefix}explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'


def texts_page(body, title, depth=1, footer_nav=None, editorial_kind=None):
    root_prefix = "../" * depth
    texts_index = "index.html" if depth == 1 else "../index.html"
    if footer_nav is None:
        footer_nav = f'<div class="chapnav"><a href="{texts_index}">all texts</a></div>'
    body_class = "landing primer"
    content = f"{body}\n{footer_nav}"
    if editorial_kind is not None:
        body_class += f" text-editorial text-{editorial_kind}-page"
        content = f'<article class="text-work">\n{body}\n{footer_nav}\n</article>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi literature in close translation, transmutation, and original composition, from the Metta Sutta to News from Nowhere.">
<title>Phi texts &mdash; {title}</title>
<script src="{root_prefix}theme.js"></script>
<script src="{root_prefix}reader.js" defer></script>
<link rel="stylesheet" href="{root_prefix}style.css">
</head>
<body class="{body_class}">
{texts_nav(depth)}
<main>
{content}
</main>
<footer>
  <p>Each work identifies itself as a translation, transmutation, or original Phi composition. Source witnesses, where a work has one, live with the texts in <a href="https://github.com/dcellison/phi/tree/main/texts">the repository</a>. The site renders them at build time.
     The <a href="{root_prefix}colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""


def text_work_nav(index):
    """Build previous, shelf, and next navigation for an editorial work."""
    links = []
    if index > 0:
        previous = TEXTS[index - 1]
        links.append(
            f'<a class="text-work-prev" href="{Path(previous["path"]).stem}.html">'
            '<span class="text-nav-direction">&lsaquo; Previous work</span>'
            f'<span class="text-nav-title">{html_module.escape(previous["title"])}</span>'
            "</a>"
        )
    else:
        links.append('<span class="text-work-nav-space" aria-hidden="true"></span>')
    links.append('<a class="text-work-index" href="index.html">All texts</a>')
    if index + 1 < len(TEXTS):
        following = TEXTS[index + 1]
        links.append(
            f'<a class="text-work-next" href="{Path(following["path"]).stem}.html">'
            '<span class="text-nav-direction">Next work &rsaquo;</span>'
            f'<span class="text-nav-title">{html_module.escape(following["title"])}</span>'
            "</a>"
        )
    else:
        links.append('<span class="text-work-nav-space" aria-hidden="true"></span>')
    return '<nav class="chapnav text-work-nav" aria-label="Text navigation">' + "".join(links) + "</nav>"


for work_index, work in enumerate(TEXTS):
    source = ROOT / "texts" / work["path"]
    stem = source.stem
    md = source.read_text()
    repo_path = source.relative_to(ROOT).as_posix()
    treatment = TEXT_EDITORIAL_PAGES.get(repo_path)
    rendered = md_to_html(md)
    footer_nav = None
    editorial_kind = None
    if treatment is not None:
        rendered = apply_text_editorial(
            rendered,
            md,
            repo_path,
            treatment,
        )
        footer_nav = text_work_nav(work_index)
        editorial_kind = treatment["form"]
    else:
        rendered = rendered.replace(
            "</h1>",
            f'</h1>\n<p class="text-method">{work["method"]}</p>',
            1,
        )
    (TEXTS_OUT / f"{stem}.html").write_text(
        texts_page(
            rendered,
            work["title"],
            footer_nav=footer_nav,
            editorial_kind=editorial_kind,
        )
    )

NEWS_SRC = ROOT / "texts" / NEWS_WORK["path"]
NEWS_OUT = TEXTS_OUT / NEWS_WORK["path"]
prepare_html_output(NEWS_OUT)
news_chapters = sorted(NEWS_SRC.glob("chapter_*.md"))
for i, chapter in enumerate(news_chapters):
    chapter_number = int(chapter.stem.split("_")[1])
    chapter_title = title_of(chapter.read_text())
    rendered = md_to_html(chapter.read_text()).replace(
        "</h1>", f'</h1>\n<p class="text-method">{NEWS_WORK["method"]}</p>', 1
    )
    prev_number = (
        int(news_chapters[i - 1].stem.split("_")[1]) if i > 0 else None
    )
    next_number = (
        int(news_chapters[i + 1].stem.split("_")[1])
        if i + 1 < len(news_chapters)
        else None
    )
    prev_link = (
        f'<a href="{news_chapters[i - 1].stem}.html">'
        f'&lsaquo; Chapter {prev_number}</a>'
        if prev_number is not None else ""
    )
    next_link = (
        f'<a href="{news_chapters[i + 1].stem}.html">'
        f'Chapter {next_number} &rsaquo;</a>'
        if next_number is not None else ""
    )
    chapter_nav = f'<div class="chapnav">{prev_link}<a href="index.html">book contents</a>{next_link}</div>'
    (NEWS_OUT / f"{chapter.stem}.html").write_text(
        texts_page(rendered, chapter_title, depth=2, footer_nav=chapter_nav)
    )

news_readme = md_to_html((NEWS_SRC / "README.md").read_text())
news_readme = news_readme.replace(
    "</h1>", f'</h1>\n<p class="text-method">{NEWS_WORK["method"]}</p>', 1
)
news_readme = re.sub(
    r'href="(chapter_[0-9]+)\.md"', r'href="\1.html"', news_readme
)
news_readme = news_readme.replace(
    'href="source.txt"',
    'href="https://github.com/dcellison/phi/blob/main/texts/news_from_nowhere/source.txt"',
)
(NEWS_OUT / "index.html").write_text(
    texts_page(news_readme, "News from Nowhere", depth=2)
)

toc = ["<h1>The texts</h1>",
       "<p>The Metta Sutta contains all ten verses of its source. The North Wind, Schleicher, and Article 1 pages put a close translation before a transmutation. Babel, the Heart Sutra, and five Tao chapters apply the same order to longer pieces. On Children pairs one teaching within The Prophet's three-part page. The shelf's first original work begins in a hot room, where care meets a refusal and the argument has to remain with both.</p>",
       "<p>A close translation answers to the source's claims and distinctions in natural Phi. Its purpose here is practical: to show that Phi can handle any source on its own terms and produce a close analogue, even when Phi would tell it differently. Every rendering says what it owes the source.</p>",
       "<p>Transmutation is Phi's preferred method for inherited material because it gives the source room to change as Phi understands it. The five pillars and Phi's own habits of thought shape the result, while the source stays in view. Seven works put translation and transmutation side by side so a reader can see what changed and why.</p>",
       "<p>Original work puts Phi first. English follows closely, and a proposition record tracks challenges, revisions, and questions left open. The block needs no fourth source line.</p>"]
for work in TEXTS:
    stem = Path(work["path"]).stem
    toc.append(f'<h2><a href="{stem}.html">{work["title"]}</a></h2><p class="text-method">{work["method"]}</p><p>{work["summary"]}</p>')
news_toc_title = NEWS_WORK["title"].replace("—", "&mdash;")
toc.append(f'<h2><a href="{NEWS_WORK["path"]}/index.html">{news_toc_title}</a></h2><p class="text-method">{NEWS_WORK["method"]}</p><p>{NEWS_WORK["summary"]}</p>')
toc.append("<hr><p><em>More texts are coming; the shelf is built to grow.</em></p>")
(TEXTS_OUT / "index.html").write_text(texts_page("\n".join(toc), "contents", footer_nav=""))
print(f"wrote build/site/texts/: {len(TEXT_CATALOGUE)} works, {len(news_chapters)} News from Nowhere chapters + contents")

# ---- the pamphlets: deep-dive companions rendered to build/site/pamphlets/ ----
PAMPH_OUT = BUILD_SITE / "pamphlets"
prepare_html_output(PAMPH_OUT)
NAV_PAMPH = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">walk</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../book/index.html">book</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a class="here" href="index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'

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

PAMPHLETS = PAMPHLET_CATALOGUE
toc = ["<h1>The pamphlets</h1>",
       "<p>Focused deep-dives: extended explanation and abundant practice for the features learners find hardest. Each is a companion to the manual, not a rival — read one straight through, or keep it open beside the exercises.</p>"]
pamph_pages = 0
for pamphlet in PAMPHLETS:
    dirname = pamphlet["directory"]
    title = pamphlet["title"]
    blurb = pamphlet["summary"]
    pfiles = sorted((ROOT / "pamphlets" / dirname).glob("*.md"))
    ptitles = [title_of(f.read_text()) for f in pfiles]
    dual = pamphlet["dual_script"]
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
print(f"wrote build/site/pamphlets/: {pamph_pages} pages + contents")
