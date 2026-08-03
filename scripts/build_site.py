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

import name_forms
import tengwar

from compound_registry import load_compounds
from content_catalogues import (
    load_pamphlet_catalogue,
    load_text_catalogue,
    load_text_collection_catalogues,
)

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
TEXT_COLLECTION_CATALOGUES = load_text_collection_catalogues(
    ROOT, TEXT_CATALOGUE
)
PAMPHLET_CATALOGUE = load_pamphlet_catalogue(ROOT)
TEXTS = [work for work in TEXT_CATALOGUE if work["kind"] == "short"]
COLLECTIONS = [
    work for work in TEXT_CATALOGUE if work["kind"] == "collection"
]
COLLECTION_TEXTS_BY_PATH = {
    collection["path"]: [
        {
            **work,
            "_repo_path": (
                f'texts/{collection["path"]}/{work["path"]}'
            ),
            "_site_path": (
                f'{collection["path"]}/{Path(work["path"]).stem}.html'
            ),
        }
        for work in TEXT_COLLECTION_CATALOGUES[collection["path"]]
    ]
    for collection in COLLECTIONS
}
COLLECTION_TEXTS = [
    work
    for collection in COLLECTIONS
    for work in COLLECTION_TEXTS_BY_PATH[collection["path"]]
]
BOOKS = [work for work in TEXT_CATALOGUE if work["kind"] == "book"]
if len(BOOKS) != 1:
    raise ValueError("the site renderer currently expects exactly one catalogued book")
NEWS_WORK = BOOKS[0]


def text_repo_path(work):
    """Return the repository path for a short or collected work."""
    return work.get("_repo_path", f'texts/{work["path"]}')


def text_site_path(work):
    """Return the deployed path for a short or collected work."""
    return work.get("_site_path", f'{Path(work["path"]).stem}.html')


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


KIA_SECTION_TITLES = (
    "The grammar has one organizing principle",
    "A dog in three syllables",
    "Punctuation speaks",
    "How do you know?",
    "Some choices are deliberate",
    "The shelf is occupied",
    "Seven doors",
)

KIA_DOORS = (
    ("Walk", "short_road.html"),
    ("Wander", "explore.html"),
    ("Begin", "primer/index.html"),
    ("Verify", "manual/index.html"),
    ("Consider", "book/index.html"),
    ("Read", "texts/index.html"),
    ("Practice", "pamphlets/index.html"),
)


def mark_kia_inline_phi(body):
    """Give source-authored Phi its site treatment, apart from doors."""
    body = re.sub(
        r"<strong>(?!<a\b)(.*?)</strong>",
        r'<strong class="kia-phi">\1</strong>',
        body,
        flags=re.S,
    )
    return re.sub(
        r"<em>([a-z]+)</em>",
        lambda match: (
            f'<em class="kia-phi">{match.group(1)}</em>'
            if match.group(1) in ALL_WORDS
            else match.group(0)
        ),
        body,
    )


def apply_kia_threshold(body):
    """Turn Kia's stable source shape into a welcoming site threshold."""
    parts = re.split(r"(?=<h2>)", body)
    if len(parts) != len(KIA_SECTION_TITLES) + 1:
        raise ValueError(
            "kia threshold expects one opening and seven titled sections"
        )

    opening = re.fullmatch(
        r"<h1>kia</h1>\n"
        r"(?P<greeting><p>.*?</p>)\n"
        r"(?P<statement><p>.*?</p>)\n"
        r"(?P<invitation><p>.*?</p>)",
        parts[0].strip(),
        flags=re.S,
    )
    if opening is None:
        raise ValueError("kia threshold opening shape differs from kia.md")

    section_parts = []
    for expected, section in zip(KIA_SECTION_TITLES, parts[1:]):
        match = re.fullmatch(
            r"<h2>(?P<title>.*?)</h2>\n?(?P<body>.*)",
            section.strip(),
            flags=re.S,
        )
        if match is None or match.group("title") != expected:
            found = match.group("title") if match is not None else "unreadable"
            raise ValueError(
                f"kia threshold expected section {expected!r}, found {found!r}"
            )
        section_parts.append(match.group("body").strip())

    door_source = section_parts.pop()
    if door_source.count("<hr>") != 1:
        raise ValueError("kia threshold expects one divider after the seven doors")
    door_paragraphs, farewell = (
        part.strip() for part in door_source.split("<hr>", 1)
    )
    door_blocks = door_paragraphs.splitlines()
    if len(door_blocks) != len(KIA_DOORS):
        raise ValueError(
            f"kia threshold expects {len(KIA_DOORS)} door paragraphs, "
            f"found {len(door_blocks)}"
        )
    if not re.fullmatch(r"<p>.*?</p>", farewell, flags=re.S):
        raise ValueError("kia threshold expects one closing welcome after the doors")

    door_items = []
    for block, (expected_label, expected_href) in zip(door_blocks, KIA_DOORS):
        paragraph = re.fullmatch(r"<p>(?P<body>.*?)</p>", block, flags=re.S)
        if paragraph is None:
            raise ValueError("kia threshold door is not one paragraph")
        anchor = re.search(
            r'<strong><a href="(?P<href>[^"]+)">(?P<label>[^<]+)</a></strong>',
            paragraph.group("body"),
        )
        if (
            anchor is None
            or anchor.group("label") != expected_label
            or anchor.group("href") != expected_href
        ):
            raise ValueError(
                f"kia threshold door differs for {expected_label!r}"
            )
        copy = (
            paragraph.group("body")[:anchor.start()]
            + f'<strong class="kia-door-name">{expected_label}</strong>'
            + paragraph.group("body")[anchor.end():]
        )
        door_items.append(
            '<li class="kia-door-item">'
            f'<a class="kia-door" href="{expected_href}">'
            f'<span class="kia-door-copy">{copy}</span>'
            '<span class="kia-door-arrow" aria-hidden="true">&rarr;</span>'
            "</a></li>"
        )

    hero_hand = tengwar.render_line("kia.")
    farewell_hand = tengwar.render_line("kia. whelani.")
    if hero_hand is None or farewell_hand is None:
        raise ValueError("kia threshold Tengwar greeting did not render")

    encounters = []
    for number, (title, section_body) in enumerate(
        zip(KIA_SECTION_TITLES[:-1], section_parts),
        start=1,
    ):
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        encounters.append(
            f'<section class="kia-encounter" id="{slug}">'
            '<header class="kia-section-header">'
            f'<span class="kia-section-number" aria-hidden="true">{number:02}</span>'
            f"<h2>{title}</h2>"
            "</header>"
            f'<div class="kia-section-copy">{section_body}</div>'
            "</section>"
        )

    page = (
        '<article class="kia-threshold-work">'
        '<header class="kia-hero">'
        '<div class="kia-hero-frame">'
        '<p class="kia-hero-label">Phi</p>'
        f'<div class="kia-hero-hand" aria-hidden="true">{hero_hand}</div>'
        "<h1>kia</h1>"
        f'<div class="kia-hero-greeting">{opening.group("greeting")}</div>'
        "</div>"
        "</header>"
        '<div class="kia-opening">'
        f'{opening.group("statement")}{opening.group("invitation")}'
        "</div>"
        + "".join(encounters)
        + '<section class="kia-doors-section" id="seven-doors">'
        '<header class="kia-section-header">'
        '<span class="kia-section-number" aria-hidden="true">07</span>'
        "<h2>Seven doors</h2>"
        "</header>"
        '<nav class="kia-doors" aria-label="Ways into Phi">'
        f'<ol class="kia-door-list">{"".join(door_items)}</ol>'
        "</nav>"
        "</section>"
        '<aside class="kia-farewell" aria-label="Welcome in Phi">'
        f'<div class="kia-farewell-hand" aria-hidden="true">{farewell_hand}</div>'
        f"{farewell}"
        "</aside>"
        "</article>"
    )
    return mark_kia_inline_phi(page)


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
body = apply_kia_threshold(body)
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
<body class="landing kia-threshold-page">
<nav class="topnav"><span class="here">kia</span> <span class="sep">&middot;</span> <a href="short_road.html">walk</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="book/index.html">book</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
{body}
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
print(
    "wrote build/site/index.html from kia.md "
    f"({len(KIA_SECTION_TITLES) - 1} encounters, {len(KIA_DOORS)} doors)"
)

# ---- colophon: colophon.md rendered after the manual treatment is loaded ----

def colophon_page(body):
    """Render the root colophon with the same treatment as its manual copy."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="How Phi is made: the designer, the instrument, and the rules between them.">
<title>Phi — colophon</title>
<script src="theme.js"></script>
<link rel="stylesheet" href="style.css">
</head>
<body class="landing primer manual-editorial manual-reference-page manual-makers-mark-page manual-maker-note-variant">
<nav class="topnav"><a href="index.html">kia</a> <span class="sep">&middot;</span> <a href="short_road.html">walk</a> <span class="sep">&middot;</span> <a href="primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="book/index.html">book</a> <span class="sep">&middot;</span> <a href="manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>
<main>
<article class="manual-work">{body}</article>
</main>
<footer>
  <p>Signed at the end, in the old way. This page is colophon.md, rendered from
     <a href="https://github.com/dcellison/phi">the repository</a>.</p>
</footer>
</body>
</html>
"""

# ---- the short road: short_road.md rendered to build/site/short_road.html ----

SHORT_ROAD_SECTION_TITLES = (
    "Let the vowels finish",
    "One organizing principle",
    "Thirty-five particles keep their places",
    "The question stands where the answer will",
    "Count in threes",
    "The day follows the sky",
    "The question with nothing to count",
    "Meanings can stay in view",
    "A name announces itself",
    "Three relationships to a text",
    "Where the choices come from",
    "The door",
)


def style_short_road_examples(body):
    """Turn the Short Road's fenced triples into interlinear figures."""
    group_count = 0

    def replace_fence(match):
        nonlocal group_count
        figures = []
        groups = re.split(r"\n\s*\n", match.group(1).strip())
        for group in groups:
            lines = group.splitlines()
            if len(lines) != 3:
                raise ValueError(
                    "short road examples must contain Phi, gloss, and translation"
                )
            source = html_module.unescape(lines[0]).strip()
            if not tengwar.phi_line(source, ALL_WORDS):
                raise ValueError(
                    f"short road example is not valid-looking Phi: {source!r}"
                )
            if not lines[2].startswith("(") or not lines[2].endswith(")"):
                raise ValueError(
                    f"short road translation lacks parentheses: {source!r}"
                )
            group_count += 1
            figures.append(
                '<figure class="walk-example">'
                f'<div class="walk-phi-line">{lines[0]}</div>'
                f'<div class="walk-gloss-line">{lines[1]}</div>'
                f"<figcaption>{lines[2][1:-1]}</figcaption>"
                "</figure>"
            )
        if len(figures) == 1:
            return figures[0]
        return '<div class="walk-example-set">' + "".join(figures) + "</div>"

    body, fence_count = re.subn(
        r"<pre>(.*?)</pre>",
        replace_fence,
        body,
        flags=re.S,
    )
    return body, fence_count, group_count


def mark_short_road_inline_phi(body):
    """Mark the Short Road's source-authored inline Phi."""
    code_count = body.count("<code>")
    strong_count = body.count("<strong>")
    if code_count != 40 or strong_count != 4:
        raise ValueError(
            "short road inline Phi shape differs: "
            f"expected 40 code spans and 4 strong spans, found {code_count} "
            f"and {strong_count}"
        )
    body = body.replace("<code>", '<code class="walk-phi">')
    return re.sub(
        r"<strong>(.*?)</strong>",
        r'<strong class="walk-phi">\1</strong>',
        body,
        flags=re.S,
    )


def apply_short_road_walk(body):
    """Turn the Short Road's stable source shape into one continuous route."""
    parts = re.split(r"(?=<h2>)", body)
    if len(parts) != len(SHORT_ROAD_SECTION_TITLES) + 1:
        raise ValueError(
            "short road expects one opening and twelve titled sections"
        )

    opening = re.fullmatch(
        r"<h1>The short road</h1>\n(?P<lede><p>.*?</p>)",
        parts[0].strip(),
        flags=re.S,
    )
    if opening is None:
        raise ValueError("short road opening shape differs from short_road.md")

    sections = []
    for expected, section in zip(SHORT_ROAD_SECTION_TITLES, parts[1:]):
        match = re.fullmatch(
            r"<h2>(?P<title>.*?)</h2>\n?(?P<body>.*)",
            section.strip(),
            flags=re.S,
        )
        if match is None or match.group("title") != expected:
            found = match.group("title") if match is not None else "unreadable"
            raise ValueError(
                f"short road expected section {expected!r}, found {found!r}"
            )
        sections.append((expected, match.group("body").strip()))

    styled_sections = []
    fence_total = 0
    group_total = 0
    for title, section_body in sections:
        section_body, fence_count, group_count = style_short_road_examples(
            section_body
        )
        fence_total += fence_count
        group_total += group_count
        styled_sections.append((title, section_body))

    if fence_total != 9 or group_total != 13:
        raise ValueError(
            "short road example shape differs: "
            f"expected 9 fences and 13 groups, found {fence_total} and "
            f"{group_total}"
        )

    closing_hand = tengwar.render_line("pi no shua.")
    if closing_hand is None:
        raise ValueError("short road closing invitation did not render in Tengwar")
    closing = (
        '<figure class="walk-closing-invitation">'
        f'<div class="walk-closing-hand" aria-hidden="true">{closing_hand}</div>'
        '<div class="walk-closing-phi">pi no shua.</div>'
        '<div class="walk-closing-gloss">POL IMP come.</div>'
        "<figcaption>Please, come.</figcaption>"
        "</figure>"
    )
    last_title, last_body = styled_sections[-1]
    last_body, closing_count = re.subn(
        r"<p><strong>pi no shua\.</strong>\n"
        r"POL IMP come\.\n"
        r"\(Please, come\.\)</p>$",
        closing,
        last_body,
        flags=re.S,
    )
    if closing_count != 1:
        raise ValueError("short road closing invitation shape differs")
    styled_sections[-1] = (last_title, last_body)

    route_items = []
    stage_html = []
    total = len(SHORT_ROAD_SECTION_TITLES)
    for number, (title, section_body) in enumerate(styled_sections, start=1):
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        safe_title = html_module.escape(title, quote=True)
        route_items.append(
            "<li>"
            f'<a href="#{slug}" aria-label="Stop {number}: {safe_title}">'
            f'<span aria-hidden="true">{number:02}</span>'
            "</a></li>"
        )
        position_class = (
            " walk-stage-first" if number == 1
            else " walk-stage-last" if number == total
            else ""
        )
        stage_html.append(
            f'<section class="walk-stage{position_class}" id="{slug}">'
            '<div class="walk-stage-marker" aria-hidden="true">'
            f"<span>{number:02}</span>"
            "</div>"
            '<div class="walk-stage-copy">'
            f"<h2>{title}</h2>{section_body}"
            "</div>"
            "</section>"
        )

    page = (
        '<article class="walk-work">'
        '<header class="walk-header">'
        '<p class="walk-kicker"><span>12 stops</span>'
        '<span class="walk-kicker-sep" aria-hidden="true">/</span>'
        "<span>about 20 minutes</span></p>"
        '<div class="walk-title-row">'
        "<h1>The short road</h1>"
        '<div class="walk-route-motif" aria-hidden="true"></div>'
        "</div>"
        f'<div class="walk-lede">{opening.group("lede")}</div>'
        "</header>"
        '<nav class="walk-route-map" aria-label="The short road, twelve stops">'
        f'<ol>{"".join(route_items)}</ol>'
        "</nav>"
        + "".join(stage_html)
        + "</article>"
    )
    return mark_short_road_inline_phi(page)


short_road_body = md_to_html((ROOT / "short_road.md").read_text())
short_road_body = apply_short_road_walk(short_road_body)
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
<body class="landing primer short-road-page">
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
print(
    "wrote build/site/short_road.html from short_road.md "
    f"({len(SHORT_ROAD_SECTION_TITLES)} stops, 13 examples)"
)

# ---- primer reader: primer/*.md rendered to build/site/primer/ ----

TEXT_SITE_PATHS = {
    text_repo_path(work): text_site_path(work)
    for work in [*TEXTS, *COLLECTION_TEXTS]
}
TEXT_SITE_PATHS.update(
    {
        f'texts/{collection["path"]}': f'{collection["path"]}/index.html'
        for collection in COLLECTIONS
    }
)
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
    name_indices = name_forms.marked_atom_indices(words)
    return bool(words) and all(
        word in ALL_WORDS
        or (index in name_indices and not name_forms.form_errors(word))
        for index, word in enumerate(words)
    )


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
        headers = re.findall(r"<th>(.*?)</th>", rows[0], re.S)
        if len(headers) != 4:
            raise ValueError("Appendix A gloss table requires four columns")
        visible_headers = headers[:3]
        plain_headers = [
            html_module.unescape(re.sub(r"<[^>]+>", "", header))
            for header in visible_headers
        ]
        out = [
            '<div class="manual-table-wrap manual-table-dense '
            'manual-gloss-table-wrap">',
            '<table class="manual-reference-table gloss-table">',
        ]
        out.append(
            "<tr>"
            + "".join(
                f'<th scope="col">{header}</th>'
                for header in visible_headers
            )
            + "</tr>"
        )
        for row in rows[1:]:
            cells = re.findall(r"<td>(.*?)</td>", row, re.S)
            if len(cells) != 4:
                raise ValueError("Appendix A gloss table has an uneven row")
            first = (
                f'{cells[0]} <span class="glossmark" '
                'aria-hidden="true">&#9432;</span>'
                f'<span class="gloss-pop">{cells[3]}</span>'
            )
            visible_cells = [first, cells[1], cells[2]]
            out.append(
                '<tr class="gloss-row" tabindex="0">'
                + "".join(
                    '<td data-label="'
                    + html_module.escape(plain_headers[index], quote=True)
                    + '"><span class="manual-table-value">'
                    + cell
                    + "</span></td>"
                    for index, cell in enumerate(visible_cells)
                )
                + "</tr>"
            )
        out.extend(("</table>", "</div>"))
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
    elif f.name == "31_capstone.md":
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

def manual_page(
    body,
    title,
    footer_nav="",
    editorial_kind=None,
    editorial_motif=None,
    editorial_variant=None,
):
    body_class = "landing primer"
    main_body = body
    if editorial_kind is not None:
        body_class += (
            f" manual-editorial manual-{editorial_kind}-page"
        )
        if editorial_motif is not None:
            motif_class = editorial_motif.replace("_", "-")
            body_class += f" manual-{motif_class}-page"
        if editorial_variant is not None:
            variant_class = editorial_variant.replace("_", "-")
            body_class += f" manual-{variant_class}-variant"
        main_body = f'<article class="manual-work">{body}</article>'
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
<body class="{body_class}">
{NAV_MANUAL}
<main>
{main_body}
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


def manual_editorial_group(repo_path):
    """Map a rendered manual source to its motif and coverage group."""
    parts = Path(repo_path).parts
    if len(parts) >= 3 and parts[0] == "manual":
        return parts[1]
    if parts == ("colophon.md",):
        return "colophon"
    raise ValueError(f"unknown manual editorial group: {repo_path}")


def manual_editorial_chapter(repo_path):
    """Return the numbered chapter directory for a teaching page."""
    parts = Path(repo_path).parts
    if (
        len(parts) >= 4
        and parts[0] == "manual"
        and re.fullmatch(r"ch\d+_[a-z0-9_]+", parts[2])
    ):
        return parts[2]
    return None


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


def markdown_table_shapes(source):
    """Return each Markdown table's column and data-row counts."""
    blocks = []
    current = []
    for line in source.splitlines() + [""]:
        if line.startswith("|"):
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    inventory = []
    for block in blocks:
        if (
            len(block) < 2
            or not set(block[1].replace("|", "").strip()) <= set("-: ")
        ):
            raise ValueError("manual editorial table lacks a separator row")
        headers = [cell.strip() for cell in block[0].strip("|").split("|")]
        inventory.append((len(headers), len(block) - 2))
    return inventory


def manual_structural_signature(source):
    """Describe the block structure a manual treatment depends on."""
    fences = [
        block.strip("\n").splitlines()
        for block in re.findall(r"```[a-z]*\n(.*?)```", source, flags=re.S)
    ]
    bare = re.sub(r"```[a-z]*\n.*?```", "", source, flags=re.S)
    headings = [
        len(mark)
        for mark in re.findall(r"^(#{1,6}) .+$", bare, flags=re.M)
    ]
    blocks = [block.strip() for block in bare.split("\n\n") if block.strip()]
    quote_shapes = [
        sum(line.startswith(">") for line in block.splitlines())
        for block in blocks
        if block.startswith(">")
    ]
    unordered_shapes = [
        sum(bool(re.match(r"^[-*] ", line)) for line in block.splitlines())
        for block in blocks
        if re.match(r"^[-*] ", block)
    ]
    ordered_shapes = [
        sum(bool(re.match(r"^\d+\. ", line)) for line in block.splitlines())
        for block in blocks
        if re.match(r"^\d+\. ", block)
    ]

    def joined(values, formatter=str):
        return ",".join(formatter(value) for value in values) or "-"

    return ";".join(
        (
            "h" + joined(headings),
            "t" + joined(
                markdown_table_shapes(bare),
                lambda shape: f"{shape[0]}x{shape[1]}",
            ),
            "f" + joined([len(block) for block in fences]),
            "q" + joined(quote_shapes),
            "u" + joined(unordered_shapes),
            "o" + joined(ordered_shapes),
            "r" + str(len(re.findall(r"^---$", bare, flags=re.M))),
        )
    )


def load_manual_editorial():
    """Load treated manual groups and pin each page's block structure."""
    config_path = SITE_SRC / "manual_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if set(config) != {"complete_groups", "groups", "chapters", "pages"}:
        raise ValueError(
            "site/manual_editorial.json requires complete_groups, groups, "
            "chapters, and pages"
        )
    complete_groups = config["complete_groups"]
    groups = config["groups"]
    chapters = config["chapters"]
    pages = config["pages"]
    if (
        not isinstance(complete_groups, list)
        or len(complete_groups) != len(set(complete_groups))
        or not isinstance(groups, dict)
        or not isinstance(chapters, dict)
        or not isinstance(pages, dict)
        or not pages
    ):
        raise ValueError(
            "manual editorial coverage, groups, chapters, and pages "
            "must be valid collections"
        )
    allowed_motifs = {
        "first_light",
        "living_heart",
        "spoken_sound",
        "ordered_layers",
        "woven_thoughts",
        "lived_practice",
        "open_reference",
        "indexed_notes",
        "makers_mark",
    }
    for group_key, group in groups.items():
        if (
            not re.fullmatch(
                r"(?:part\d+_[a-z0-9_]+|appendices|colophon)",
                group_key,
            )
            or not isinstance(group, dict)
            or set(group) != {"motif", "title", "summary"}
            or group["motif"] not in allowed_motifs
            or not isinstance(group["title"], str)
            or not group["title"].strip()
            or not isinstance(group["summary"], str)
            or not group["summary"].strip()
        ):
            raise ValueError(f"invalid manual editorial group: {group_key}")
    if any(group not in groups for group in complete_groups):
        raise ValueError("every complete manual group requires group metadata")

    rendered_paths = {
        path.relative_to(ROOT).as_posix()
        for _, _, path in sections
    }
    expected_chapters = {
        chapter
        for repo_path in rendered_paths
        if (chapter := manual_editorial_chapter(repo_path)) is not None
    }
    if set(chapters) != expected_chapters:
        raise ValueError(
            "manual editorial chapters differ from the rendered manual: "
            + ", ".join(sorted(set(chapters) ^ expected_chapters))
        )
    chapter_numbers = []
    for chapter_key, chapter_title in chapters.items():
        chapter_match = re.fullmatch(r"ch(\d+)_[a-z0-9_]+", chapter_key)
        if (
            chapter_match is None
            or not isinstance(chapter_title, str)
            or not chapter_title.strip()
        ):
            raise ValueError(f"invalid manual editorial chapter: {chapter_key}")
        chapter_numbers.append(int(chapter_match.group(1)))
    if sorted(chapter_numbers) != list(range(1, len(chapters) + 1)):
        raise ValueError("manual editorial chapter numbers must be contiguous")
    outline = (MANUAL_SRC / "outline.md").read_text(encoding="utf-8")
    outline_parts = re.findall(
        r"^## Part ([IVX]+): (.+)$",
        outline,
        flags=re.M,
    )
    numbered_groups = sorted(
        (
            int(re.fullmatch(r"part(\d+)_[a-z0-9_]+", group_key).group(1)),
            group,
        )
        for group_key, group in groups.items()
        if group_key.startswith("part")
    )
    roman_parts = ("I", "II", "III", "IV", "V", "VI", "VII")
    expected_outline_parts = [
        (roman_parts[number - 1], group["title"])
        for number, group in numbered_groups
    ]
    if outline_parts != expected_outline_parts:
        raise ValueError("manual outline part titles differ from editorial metadata")
    outline_chapters = [
        (int(number), title)
        for number, title in re.findall(
            r"^- Chapter (\d+): (.+)$",
            outline,
            flags=re.M,
        )
    ]
    expected_outline_chapters = sorted(
        (
            int(re.fullmatch(r"ch(\d+)_[a-z0-9_]+", chapter_key).group(1)),
            chapter_title,
        )
        for chapter_key, chapter_title in chapters.items()
    )
    if outline_chapters != expected_outline_chapters:
        raise ValueError(
            "manual outline chapter titles differ from editorial metadata"
        )

    configured_paths = set(pages)
    if not configured_paths <= rendered_paths:
        raise ValueError(
            "manual editorial pages include files outside the rendered manual: "
            + ", ".join(sorted(configured_paths - rendered_paths))
        )
    expected_complete = {
        repo_path
        for repo_path in rendered_paths
        if manual_editorial_group(repo_path) in complete_groups
    }
    missing = expected_complete - configured_paths
    if missing:
        raise ValueError(
            "complete manual groups have untreated pages: "
            + ", ".join(sorted(missing))
        )

    for repo_path, treatment in pages.items():
        source_path = ROOT / repo_path
        group_key = manual_editorial_group(repo_path)
        if (
            group_key not in groups
            or not source_path.is_file()
            or not isinstance(treatment, dict)
        ):
            raise ValueError(f"invalid manual editorial source: {repo_path}")
        variant = treatment.get("variant")
        required = {"shape", "variant"}
        if variant == "ordered_reference":
            required.add("pattern")
        if variant == "glossary":
            required.add("definition_count")
        optional = {"table_headers"}
        treatment_keys = set(treatment)
        if (
            not required <= treatment_keys
            or not treatment_keys <= required | optional
        ):
            raise ValueError(
                f"manual editorial treatment for {repo_path} requires "
                + ", ".join(sorted(required))
                + " and permits table_headers"
            )
        if variant not in {
            "standard",
            "conversation",
            "ordered_reference",
            "directory",
            "module_guide",
            "glossary",
            "appendix",
            "maker_note",
        }:
            raise ValueError(f"unknown manual editorial variant: {variant}")
        source = source_path.read_text(encoding="utf-8")
        table_headers = treatment.get("table_headers")
        if table_headers is not None and (
            not isinstance(table_headers, list)
            or not table_headers
            or any(
                not isinstance(header, str) or not header.strip()
                for header in table_headers
            )
        ):
            raise ValueError(
                f"manual editorial table headers are invalid: {repo_path}"
            )
        if variant == "glossary" and (
            not isinstance(treatment["definition_count"], int)
            or treatment["definition_count"] < 1
        ):
            raise ValueError(
                f"manual editorial glossary count is invalid: {repo_path}"
            )
        if treatment["shape"] != manual_structural_signature(source):
            raise ValueError(
                f"manual editorial source structure changed: {repo_path}"
            )
        if variant == "ordered_reference" and source.count(
            f'**{treatment["pattern"]}**'
        ) != 1:
            raise ValueError(
                f"manual editorial pattern changed or is ambiguous: {repo_path}"
            )
        if variant == "conversation" and source.count("\n---\n") != 2:
            raise ValueError(
                f"manual editorial conversation boundaries changed: {repo_path}"
            )
    return groups, chapters, pages


def manual_motif(name):
    """Return the restrained Lucide motif for a manual part."""
    # Lucide outlines; the deployed site carries the project's ISC notice.
    motifs = {
        "first_light": (
            """
    <path d="M12 2v8"/>
    <path d="m4.93 10.93 1.41 1.41"/>
    <path d="M2 18h2"/>
    <path d="M20 18h2"/>
    <path d="m19.07 10.93-1.41 1.41"/>
    <path d="M22 22H2"/>
    <path d="m8 6 4-4 4 4"/>
    <path d="M16 18a4 4 0 0 0-8 0"/>""",
            """
    <path d="M7 20h8"/>
    <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
    <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5 0-4.6-.7-1.1-.8-1.8-2.2-2.3-3.7 2-.4 3.5 0 4.6.7z"/>
    <path d="M14.1 6a7 7 0 0 0-1.9 2.8c1.7.3 3.1 0 4.1-.7 1-.7 1.6-1.9 2-3.3-1.8-.3-3.2 0-4.2.7z"/>""",
        ),
        "living_heart": (
            """
    <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>""",
            """
    <path d="M7 20h8"/>
    <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
    <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5 0-4.6-.7-1.1-.8-1.8-2.2-2.3-3.7 2-.4 3.5 0 4.6.7z"/>
    <path d="M14.1 6a7 7 0 0 0-1.9 2.8c1.7.3 3.1 0 4.1-.7 1-.7 1.6-1.9 2-3.3-1.8-.3-3.2 0-4.2.7z"/>""",
        ),
        "spoken_sound": (
            """
    <path d="M2 10v3"/>
    <path d="M6 6v11"/>
    <path d="M10 3v18"/>
    <path d="M14 8v7"/>
    <path d="M18 5v13"/>
    <path d="M22 10v3"/>""",
            """
    <path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 7-6 7-6 10a2.5 2.5 0 0 1-5 0"/>
    <path d="M6 8.5A6.5 6.5 0 0 0 12.5 15"/>
    <path d="M11 8.5a2 2 0 1 1 4 0c0 2-2 3-2 3"/>""",
        ),
        "ordered_layers": (
            """
    <path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/>
    <path d="m22 12.5-9.17 4.17a2 2 0 0 1-1.66 0L2 12.5"/>
    <path d="m22 17.5-9.17 4.17a2 2 0 0 1-1.66 0L2 17.5"/>""",
            """
    <line x1="10" x2="21" y1="6" y2="6"/>
    <line x1="10" x2="21" y1="12" y2="12"/>
    <line x1="10" x2="21" y1="18" y2="18"/>
    <path d="M4 6h1v4"/>
    <path d="M4 10h2"/>
    <path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1"/>""",
        ),
        "woven_thoughts": (
            """
    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>""",
            """
    <path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 1-2 2 2 2 0 0 1 2 2v5c0 1.1.9 2 2 2h1"/>
    <path d="M16 21h1a2 2 0 0 0 2-2v-5c0-1.1.9-2 2-2a2 2 0 0 1-2-2V5a2 2 0 0 0-2-2h-1"/>""",
        ),
        "lived_practice": (
            """
    <circle cx="12" cy="12" r="10"/>
    <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>""",
            """
    <path d="M7 20h8"/>
    <path d="M10 20c5.5-2.5.8-6.4 3-10"/>
    <path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5 0-4.6-.7-1.1-.8-1.8-2.2-2.3-3.7 2-.4 3.5 0 4.6.7z"/>
    <path d="M14.1 6a7 7 0 0 0-1.9 2.8c1.7.3 3.1 0 4.1-.7 1-.7 1.6-1.9 2-3.3-1.8-.3-3.2 0-4.2.7z"/>""",
        ),
        "open_reference": (
            """
    <path d="M12 7v14"/>
    <path d="M3 18a1 1 0 0 1-1-1V5a2 2 0 0 1 2-2h5a3 3 0 0 1 3 3v15a3 3 0 0 0-3-3Z"/>
    <path d="M21 18a1 1 0 0 0 1-1V5a2 2 0 0 0-2-2h-5a3 3 0 0 0-3 3v15a3 3 0 0 1 3-3Z"/>""",
            """
    <path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>""",
        ),
        "indexed_notes": (
            """
    <path d="M20 7h-3a2 2 0 0 1-2-2V2"/>
    <path d="M15 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6Z"/>
    <path d="M9 13h6"/>
    <path d="M9 17h6"/>
    <path d="M9 9h1"/>""",
            """
    <path d="M21 12h-8"/>
    <path d="M21 6H8"/>
    <path d="M21 18h-8"/>
    <path d="M3 6h1v4"/>
    <path d="M3 10h4"/>
    <path d="M3 18h6"/>
    <path d="M3 14h1v4"/>""",
        ),
        "makers_mark": (
            """
    <path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/>
    <line x1="16" x2="2" y1="8" y2="22"/>
    <line x1="17.5" x2="9" y1="15" y2="15"/>""",
            """
    <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>""",
        ),
    }
    if name not in motifs:
        raise ValueError(f"unknown manual motif: {name}")
    first, second = motifs[name]
    return (
        f'<div class="manual-page-motif manual-motif-{name}" '
        'aria-hidden="true">'
        f'<svg viewBox="0 0 24 24" focusable="false">{first}</svg>'
        f'<svg viewBox="0 0 24 24" focusable="false">{second}</svg>'
        "</div>"
    )


def manual_heading_id(title):
    """Make a stable local anchor from a configured manual heading."""
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def mark_manual_inline_phi(body):
    """Give current Phi in strong spans the shared inline treatment."""
    def mark_strong(match):
        if not is_current_phi(match.group(1)):
            return match.group(0)
        return (
            f'<code class="phi-inline" lang="art-x-phi">'
            f"{match.group(1)}</code>"
        )

    return re.sub(r"<strong>([^<]+)</strong>", mark_strong, body)


def mark_manual_repo_paths(body):
    """Mark repository paths without shrinking ordinary inline code."""
    def mark_path(match):
        value = html_module.unescape(match.group(1))
        root_path = re.fullmatch(
            r"/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*/?",
            value,
        )
        relative_path = re.fullmatch(
            r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+/?",
            value,
        )
        if root_path is None and relative_path is None:
            return match.group(0)
        return f'<code class="manual-repo-path">{match.group(1)}</code>'

    return re.sub(r"<code>([^<]+)</code>", mark_path, body)


def style_manual_tables(body, title, table_headers=None):
    """Add responsive labels while preserving every rendered table cell."""
    tables = re.findall(r"<table>.*?</table>", body, flags=re.S)
    table_headers_used = False
    for table_number, table in enumerate(tables, start=1):
        rows = re.findall(r"<tr>(.*?)</tr>", table, flags=re.S)
        if not rows:
            raise ValueError(
                f"manual editorial table {table_number} has no rows: {title}"
            )
        headers = re.findall(r"<th>(.*?)</th>", rows[0], flags=re.S)
        data_rows = rows[1:]
        if not headers:
            first_row_cells = re.findall(
                r"<td>(.*?)</td>", rows[0], flags=re.S
            )
            if (
                table_headers is None
                or table_number != 1
                or not first_row_cells
                or len(first_row_cells) != len(table_headers)
            ):
                raise ValueError(
                    f"manual editorial table {table_number} has no header: "
                    f"{title} ({rows[0]})"
                )
            headers = [
                html_module.escape(header) for header in table_headers
            ]
            data_rows = rows
            table_headers_used = True
        plain_headers = [
            html_module.unescape(re.sub(r"<[^>]+>", "", header))
            for header in headers
        ]
        rebuilt = ['<table class="manual-reference-table">']
        rebuilt.append(
            "<tr>"
            + "".join(f'<th scope="col">{header}</th>' for header in headers)
            + "</tr>"
        )
        for row in data_rows:
            cells = re.findall(r"<td>(.*?)</td>", row, flags=re.S)
            if len(cells) != len(headers):
                raise ValueError(
                    f"manual editorial table {table_number} has uneven rows: "
                    f"{title}"
                )
            rebuilt.append(
                "<tr>"
                + "".join(
                    '<td data-label="'
                    + html_module.escape(plain_headers[index], quote=True)
                    + '"><span class="manual-table-value">'
                    + cell
                    + "</span></td>"
                    for index, cell in enumerate(cells)
                )
                + "</tr>"
            )
        rebuilt.append("</table>")
        classes = ["manual-table-wrap"]
        if len(rows) - 1 > 6:
            classes.append("manual-table-dense")
        if len(headers) == 2:
            classes.append("manual-table-pair")
        if len(headers) > 3:
            classes.append("manual-table-wide")
        replacement = (
            f'<div class="{" ".join(classes)}">'
            + "".join(rebuilt)
            + "</div>"
        )
        body = body.replace(table, replacement, 1)
    if table_headers is not None and not table_headers_used:
        raise ValueError(
            f"manual editorial table headers have no headerless table: {title}"
        )
    return body


def style_manual_examples(body):
    """Render interlinear fences and retain other preformatted material."""
    blocks = re.findall(r"<pre>(.*?)</pre>", body, flags=re.S)
    for block in blocks:
        groups = [
            group.splitlines()
            for group in re.split(r"\n\s*\n", block.strip())
        ]
        interlinear = []
        for lines in groups:
            plain_lines = [html_module.unescape(line) for line in lines]
            if (
                len(lines) not in {3, 4}
                or not is_current_phi_passage(plain_lines[0])
            ):
                interlinear = []
                break
            source_line = (
                f'\n  <p class="manual-example-source">{lines[3]}</p>'
                if len(lines) == 4
                else ""
            )
            interlinear.append(f"""
<figure class="manual-example" aria-label="Interlinear example">
  <p class="manual-example-phi" lang="art-x-phi">{lines[0]}</p>
  <p class="manual-example-gloss">{lines[1]}</p>
  <figcaption>{lines[2]}</figcaption>{source_line}
</figure>""")
        if len(interlinear) == 1:
            replacement = interlinear[0]
        elif interlinear:
            replacement = (
                '<div class="manual-example-set" role="group" '
                'aria-label="Interlinear examples">'
                + "".join(interlinear)
                + "</div>"
            )
        elif re.fullmatch(r"\[[^\]]+\](?: [A-Z][A-Z ]*)+", block.strip()):
            replacement = (
                '<div class="manual-syntax-formula" '
                'aria-label="Syntax formula"><code>'
                + block.strip()
                + "</code></div>"
            )
        else:
            replacement = f'<pre class="manual-code-sample">{block}</pre>'
        body = body.replace(f"<pre>{block}</pre>", replacement, 1)
    return body


def style_manual_glossary(body, definition_count):
    """Turn Appendix A's prose definitions into a compact reference grid."""
    pattern = re.compile(
        r"<p><strong>([^<]+)</strong>: (.*?)</p>",
        flags=re.S,
    )
    definitions = list(pattern.finditer(body))
    if len(definitions) != definition_count:
        raise ValueError(
            "manual editorial glossary definition count changed "
            f"({len(definitions)} found, {definition_count} expected)"
        )
    between = body[definitions[0].start():definitions[-1].end()]
    if pattern.sub("", between).strip():
        raise ValueError("manual editorial glossary definitions are not contiguous")
    entries = "".join(
        '<div class="manual-glossary-entry">'
        f"<dt>{match.group(1)}</dt>"
        f"<dd>{match.group(2)}</dd>"
        "</div>"
        for match in definitions
    )
    glossary = (
        '<dl class="manual-glossary" aria-label="Linguistic terms">'
        + entries
        + "</dl>"
    )
    return (
        body[:definitions[0].start()]
        + glossary
        + body[definitions[-1].end():]
    )


def style_manual_dialogue(body):
    """Lift the Part I road conversation into speaker rows."""
    match = re.search(r"<hr>\n(.*?)\n<hr>", body, flags=re.S)
    if match is None or body.count("<hr>") != 2:
        raise ValueError("manual editorial conversation boundaries changed")
    paragraphs = re.findall(r"<p>(.*?)</p>", match.group(1), flags=re.S)
    if len(paragraphs) < 2 or len(paragraphs) % 2:
        raise ValueError("manual editorial conversation turns changed")
    turns = []
    for index in range(0, len(paragraphs), 2):
        spoken = re.fullmatch(
            r"<strong>([A-Z]):</strong>\s*(.+)",
            paragraphs[index],
            flags=re.S,
        )
        translation = re.fullmatch(
            r"<em>(.*?)</em>",
            paragraphs[index + 1],
            flags=re.S,
        )
        if spoken is None or translation is None:
            raise ValueError("manual editorial conversation row changed")
        phi = spoken.group(2)
        plain_phi = html_module.unescape(re.sub(r"<[^>]+>", "", phi))
        if not is_current_phi_passage(plain_phi):
            raise ValueError("manual editorial conversation contains non-Phi")
        turns.append(
            '<div class="manual-dialogue-turn">'
            f'<span class="manual-dialogue-speaker">{spoken.group(1)}</span>'
            '<div class="manual-dialogue-copy">'
            f'<p class="manual-dialogue-phi" lang="art-x-phi">{phi}</p>'
            f'<p class="manual-dialogue-english">{translation.group(1)}</p>'
            "</div></div>"
        )
    replacement = (
        '<figure class="manual-dialogue" aria-label="Conversation">'
        + "".join(turns)
        + "</figure>"
    )
    return body[:match.start()] + replacement + body[match.end():]


def style_manual_pattern(body, pattern):
    """Turn the configured noun-phrase formula into an ordered reference row."""
    pattern_html = html_module.escape(pattern)
    source = f"<p><strong>{pattern_html}</strong></p>"
    if body.count(source) != 1:
        raise ValueError("manual editorial canonical pattern changed")
    labels = re.findall(r"\[([^\]]+)\]", pattern)
    items = "".join(
        f'<li><span class="manual-pattern-number" aria-hidden="true">'
        f"{index:02d}</span> "
        f"<span>{html_module.escape(label)}</span></li>"
        for index, label in enumerate(labels, start=1)
    )
    replacement = (
        '<div class="manual-pattern" role="group" '
        'aria-label="Canonical noun phrase order">'
        f'<ol class="manual-pattern-list">{items}</ol>'
        "</div>"
    )
    return body.replace(source, replacement, 1)


def manual_header_context(
    group_key,
    chapter_key,
    chapter_label,
    section_number,
    section_total,
):
    """Build orientation labels for teaching, reference, and back matter."""
    part_match = re.fullmatch(r"part(\d+)_[a-z0-9_]+", group_key)
    if part_match is not None:
        part_number = int(part_match.group(1))
        roman_parts = ("I", "II", "III", "IV", "V", "VI", "VII")
        if not 1 <= part_number <= len(roman_parts):
            raise ValueError("manual editorial part number is outside the manual")
        meta = (
            f"<span>Part {roman_parts[part_number - 1]}</span>"
            f"<span>{html_module.escape(MANUAL_GROUPS[group_key]['title'])}</span>"
        )
        if chapter_key is not None:
            chapter_number = int(
                re.fullmatch(r"ch(\d+)_[a-z0-9_]+", chapter_key).group(1)
            )
            detail = (
                f"Chapter {chapter_number} "
                '<span aria-hidden="true">&middot;</span> '
                f"{html_module.escape(MANUAL_CHAPTERS[chapter_key])}"
            )
            position = f"Section {section_number} of {section_total}"
        elif part_number == 7 and chapter_label is None:
            detail = "Reference desk"
            position = f"Reference {section_number} of {section_total}"
        elif part_number == 7 and chapter_label == "Domain Modules":
            detail = "Domain modules"
            position = f"Module {section_number} of {section_total}"
        else:
            raise ValueError(
                "manual editorial numbered part has an invalid chapter label"
            )
        return meta, detail, position
    if group_key == "appendices" and chapter_label is None:
        return (
            "<span>Back matter</span><span>Appendices</span>",
            "Reference notes",
            f"Appendix {section_number} of {section_total}",
        )
    if group_key == "colophon" and chapter_label is None:
        return (
            "<span>Back matter</span><span>Colophon</span>",
            "Maker's note",
            "Final page",
        )
    raise ValueError("manual editorial page has an invalid reading-order label")


def apply_manual_editorial(
    body,
    treatment,
    chapter_label,
    section_number,
    section_total,
    motif,
    title,
    group_key,
    chapter_key,
):
    """Apply the manual reference treatment to one structurally pinned page."""
    title_html = html_module.escape(title, quote=False)
    title_tags = [
        match.group(0)
        for match in re.finditer(r"<h([12])>(.*?)</h\1>", body, flags=re.S)
        if html_module.unescape(
            re.sub(r"<[^>]+>", "", match.group(2))
        ) == title
    ]
    if len(title_tags) != 1:
        raise ValueError(
            f"manual editorial title is missing or ambiguous: {title}"
        )
    body = body.replace(title_tags[0], "", 1)
    if treatment["variant"] == "conversation":
        body = style_manual_dialogue(body)
    body = mark_inline_phi(body)
    body = mark_manual_inline_phi(body)
    body = mark_manual_repo_paths(body)
    if treatment["variant"] == "glossary":
        body = style_manual_glossary(
            body,
            treatment["definition_count"],
        )
    body = style_manual_tables(body, title, treatment.get("table_headers"))
    body = style_manual_examples(body)
    if treatment["variant"] == "ordered_reference":
        body = style_manual_pattern(body, treatment["pattern"])

    section_headings = []
    used_ids = set()

    def style_h2(match):
        heading_html = match.group(1)
        heading = html_module.unescape(re.sub(r"<[^>]+>", "", heading_html))
        heading_id = manual_heading_id(heading)
        if not heading_id or heading_id in used_ids:
            raise ValueError(
                f"manual editorial section anchor is invalid: {heading}"
            )
        used_ids.add(heading_id)
        number = len(section_headings) + 1
        step = re.fullmatch(r"Step (\d+):\s*(.+)", heading_html, flags=re.S)
        is_exercise = bool(re.match(r"Exercise \d+:", heading))
        section_headings.append(
            {
                "html": heading_html,
                "id": heading_id,
                "title": heading,
                "exercise": is_exercise,
            }
        )
        exercise_class = " manual-exercise-title" if is_exercise else ""
        if step is not None:
            return (
                f'<h2 class="manual-section-title manual-step-title" '
                f'id="{heading_id}">'
                '<span class="manual-step-number" aria-hidden="true">'
                f'<small>Step</small>{int(step.group(1)):02d}</span> '
                f"<span>{step.group(2)}</span></h2>"
            )
        return (
            f'<h2 class="manual-section-title{exercise_class}" '
            f'id="{heading_id}">'
            f'<span class="manual-section-number" aria-hidden="true">'
            f"{number:02d}</span> "
            f"<span>{heading_html}</span></h2>"
        )

    body = re.sub(r"<h2>(.*?)</h2>", style_h2, body, flags=re.S)

    subsection_ids = set()

    def style_h3(match):
        heading_html = match.group(1)
        heading = html_module.unescape(re.sub(r"<[^>]+>", "", heading_html))
        base = "sub-" + manual_heading_id(heading)
        heading_id = base
        suffix = 2
        while heading_id in subsection_ids or heading_id in used_ids:
            heading_id = f"{base}-{suffix}"
            suffix += 1
        subsection_ids.add(heading_id)
        return (
            f'<h3 class="manual-subsection-title" id="{heading_id}">'
            f"{heading_html}</h3>"
        )

    body = re.sub(r"<h3>(.*?)</h3>", style_h3, body, flags=re.S)

    first_section = body.find('<h2 class="manual-section-title')
    opening_end = first_section if first_section >= 0 else len(body)
    opening = body[:opening_end]
    opening, lede_count = re.subn(
        r"<p>",
        '<p class="manual-page-lede">',
        opening,
        count=1,
    )
    if lede_count == 0 and first_section >= 0 and not opening.strip():
        opening = ""
    elif lede_count != 1:
        raise ValueError(
            f"manual editorial page requires an opening paragraph: {title}"
        )
    if opening:
        opening = f'<div class="manual-page-opening">{opening}</div>'

    sections_html = []
    if first_section >= 0:
        rest = body[first_section:]
        section_matches = list(
            re.finditer(
                r'<h2 class="manual-section-title[^"]*" '
                r'id="([^"]+)">.*?</h2>',
                rest,
                flags=re.S,
            )
        )
        if len(section_matches) != len(section_headings):
            raise ValueError(
                f"manual editorial section wrapping changed: {title} "
                f"({len(section_matches)} rendered, "
                f"{len(section_headings)} inventoried; "
                f"{re.findall(r'<h2[^>]*>', rest)})"
            )
        for index, match in enumerate(section_matches):
            end = (
                section_matches[index + 1].start()
                if index + 1 < len(section_matches)
                else len(rest)
            )
            exercise_class = (
                " manual-exercise-section"
                if section_headings[index]["exercise"]
                else ""
            )
            sections_html.append(
                f'<section class="manual-reference-section{exercise_class}" '
                f'aria-labelledby="{match.group(1)}">'
                + rest[match.start():end]
                + "</section>"
            )
    else:
        opening = (
            '<div class="manual-unsectioned-copy">'
            + opening
            + "</div>"
        )

    meta_labels, detail_label, position_label = manual_header_context(
        group_key,
        chapter_key,
        chapter_label,
        section_number,
        section_total,
    )
    title_words = re.findall(r"[A-Za-z]+", title)
    longest_title_word = max(map(len, title_words)) if title_words else 0
    if longest_title_word >= 12:
        title_class = ' class="manual-title-very-long"'
    elif longest_title_word >= 10 or (
        longest_title_word >= 9 and len(title) >= 16
    ):
        title_class = ' class="manual-title-long"'
    else:
        title_class = ""
    map_items = "".join(
        f'<li><a href="#{heading["id"]}">'
        f'<span class="manual-map-number" aria-hidden="true">'
        f"{index:02d}</span> "
        f'<span class="manual-map-title">{heading["html"]}</span>'
        "</a></li>"
        for index, heading in enumerate(section_headings, start=1)
    )
    header = f"""
<header class="manual-page-header">
  <div class="manual-header-meta">
    <p><span class="manual-shelf-label">Phi manual</span>{meta_labels}</p>
    <p>{position_label}</p>
  </div>
  <div class="manual-title-row">
    <div>
      <p class="manual-chapter-label">{detail_label}</p>
      <h1{title_class}>{title_html}</h1>
    </div>
    {manual_motif(motif)}
  </div>
</header>"""
    section_map = (
        f"""
<nav class="manual-page-map" aria-label="On this page">
  <p>On this page</p>
  <ol>{map_items}</ol>
</nav>"""
        if len(section_headings) >= 2
        else ""
    )
    return header + opening + section_map + "".join(sections_html)


def manual_editorial_navigation(previous, following):
    """Give an editorial manual page labelled previous and next links."""
    previous_link = (
        f'<a class="manual-nav-page manual-nav-previous" '
        f'href="{previous["href"]}"><span>Previous</span>'
        f'<strong>{html_module.escape(previous["title"])}</strong></a>'
        if previous
        else '<span class="manual-nav-page"></span>'
    )
    next_link = (
        f'<a class="manual-nav-page manual-nav-next" '
        f'href="{following["href"]}"><span>Next</span>'
        f'<strong>{html_module.escape(following["title"])}</strong></a>'
        if following
        else '<span class="manual-nav-page"></span>'
    )
    return (
        '<nav class="chapnav manual-page-nav" aria-label="Manual pages">'
        f'{previous_link}<a class="manual-nav-contents" '
        f'href="index.html">Manual contents</a>{next_link}</nav>'
    )


def manual_contents(entries):
    """Build the manual catalogue from its verified reading order."""
    roman_parts = ("I", "II", "III", "IV", "V", "VI", "VII")
    part_keys = [
        key
        for key in MANUAL_GROUPS
        if re.fullmatch(r"part\d+_[a-z0-9_]+", key)
    ]
    part_numbers = [
        int(re.fullmatch(r"part(\d+)_[a-z0-9_]+", key).group(1))
        for key in part_keys
    ]
    if part_numbers != list(range(1, 8)):
        raise ValueError("manual contents require Parts I through VII in order")

    indexed_entries = []
    seen_hrefs = set()
    for index, (part, chapter, source, title) in enumerate(entries, start=1):
        repo_path = source.relative_to(ROOT).as_posix()
        href = slug(source)
        if href in seen_hrefs:
            raise ValueError(f"manual contents repeat a page: {href}")
        seen_hrefs.add(href)
        indexed_entries.append(
            {
                "index": index,
                "part": part,
                "chapter_label": chapter,
                "title": title,
                "href": href,
                "group": manual_editorial_group(repo_path),
                "chapter": manual_editorial_chapter(repo_path),
            }
        )
    if len(indexed_entries) != len(MANUAL_EDITORIAL):
        raise ValueError(
            "manual contents and editorial catalogue have different page counts"
        )

    def entry_list(items):
        return (
            '<ol class="manual-index-readings">'
            + "".join(
                f'<li><a href="{item["href"]}">'
                '<span class="manual-index-reading-number" aria-hidden="true">'
                f'{item["index"]:03d}</span>'
                '<span class="manual-index-reading-title">'
                f'{html_module.escape(item["title"])}</span>'
                '<span class="manual-index-arrow" aria-hidden="true">'
                "&rsaquo;</span></a></li>"
                for item in items
            )
            + "</ol>"
        )

    def chapter_block(chapter_key, items, label=None):
        if not items:
            raise ValueError("manual contents chapter cannot be empty")
        if chapter_key is not None:
            match = re.fullmatch(r"ch(\d+)_[a-z0-9_]+", chapter_key)
            number = int(match.group(1))
            heading = (
                f"<span>Chapter {number}</span>"
                f"<strong>{html_module.escape(MANUAL_CHAPTERS[chapter_key])}</strong>"
            )
        elif label is not None:
            heading = f"<strong>{html_module.escape(label)}</strong>"
        else:
            raise ValueError("manual contents reference group requires a label")
        return (
            '<section class="manual-index-chapter">'
            f"<h3>{heading}</h3>{entry_list(items)}</section>"
        )

    jump_links = "".join(
        f'<a href="#part-{roman.lower()}"><span>Part {roman}</span>'
        f'{html_module.escape(MANUAL_GROUPS[group_key]["title"])}</a>'
        for roman, group_key in zip(roman_parts, part_keys)
    )
    jump_links += (
        '<a href="#back-matter"><span>After Part VII</span>Back matter</a>'
    )

    part_sections = []
    for roman, group_key in zip(roman_parts, part_keys):
        group = MANUAL_GROUPS[group_key]
        group_entries = [
            item for item in indexed_entries if item["group"] == group_key
        ]
        if not group_entries:
            raise ValueError(f"manual contents group is empty: {group_key}")
        if group_key != "part7_reference":
            chapter_keys = []
            for item in group_entries:
                if item["chapter"] not in chapter_keys:
                    chapter_keys.append(item["chapter"])
            if None in chapter_keys:
                raise ValueError(
                    f"manual teaching part has an unnumbered page: {group_key}"
                )
            blocks = [
                chapter_block(
                    chapter_key,
                    [
                        item
                        for item in group_entries
                        if item["chapter"] == chapter_key
                    ],
                )
                for chapter_key in chapter_keys
            ]
        else:
            reference_entries = [
                item
                for item in group_entries
                if item["chapter_label"] is None
            ]
            module_entries = [
                item
                for item in group_entries
                if item["chapter_label"] == "Domain Modules"
            ]
            if len(reference_entries) + len(module_entries) != len(group_entries):
                raise ValueError("manual reference contents have an unknown group")
            blocks = [
                chapter_block(None, reference_entries, "Reference desk"),
                chapter_block(None, module_entries, "Domain modules"),
            ]
        part_sections.append(
            f'<section class="manual-index-part" id="part-{roman.lower()}">'
            '<header class="manual-index-part-header"><div>'
            f'<p class="manual-index-part-label">Part {roman} '
            '<span aria-hidden="true">&middot;</span> '
            f'{len(group_entries)} readings</p>'
            f"<h2>{html_module.escape(group['title'])}</h2>"
            f"<p>{html_module.escape(group['summary'])}</p></div>"
            f'{manual_motif(group["motif"])}</header>'
            '<div class="manual-index-chapters">'
            + "".join(blocks)
            + "</div></section>"
        )

    appendix_entries = [
        item for item in indexed_entries if item["group"] == "appendices"
    ]
    colophon_entries = [
        item for item in indexed_entries if item["group"] == "colophon"
    ]
    if len(appendix_entries) != 3 or len(colophon_entries) != 1:
        raise ValueError("manual contents require three appendices and one colophon")
    back_matter = (
        '<section class="manual-index-part manual-index-back-matter" '
        'id="back-matter"><header class="manual-index-part-header"><div>'
        '<p class="manual-index-part-label">After Part VII '
        '<span aria-hidden="true">&middot;</span> 4 readings</p>'
        '<h2>Back matter</h2><p>'
        + html_module.escape(MANUAL_GROUPS["appendices"]["summary"])
        + " "
        + html_module.escape(MANUAL_GROUPS["colophon"]["summary"])
        + "</p></div>"
        + manual_motif(MANUAL_GROUPS["appendices"]["motif"])
        + '</header><div class="manual-index-chapters">'
        + chapter_block(None, appendix_entries, "Reference notes")
        + chapter_block(None, colophon_entries, "Maker's note")
        + "</div></section>"
    )

    header = (
        '<header class="manual-index-header"><div class="manual-index-meta">'
        '<p><span>Phi manual</span><span>Contents</span></p>'
        '<p>Working reference</p></div>'
        '<div class="manual-index-title-row"><h1>The Phi manual</h1>'
        + manual_motif("ordered_layers")
        + '<p class="manual-index-lede">The '
        '<a href="../primer/index.html">primer</a> teaches Phi through one '
        "household's day. The manual lays the language out in full. Begin at "
        '<a href="#part-i">First light</a>, or enter wherever a question has '
        'brought you. Every page returns here, and the '
        '<a href="../explore.html">lexicon</a> keeps every word close by.</p>'
        '</div><p class="manual-index-counts" aria-label="Manual extent">'
        "<span><strong>7</strong> parts</span>"
        f"<span><strong>{len(MANUAL_CHAPTERS)}</strong> chapters</span>"
        f"<span><strong>{len(indexed_entries)}</strong> readings</span></p>"
        "</header>"
    )
    return (
        header
        + '<nav class="manual-index-jump" aria-label="Manual parts">'
        + jump_links
        + "</nav>"
        + "".join(part_sections)
        + back_matter
    )


MANUAL_GROUPS, MANUAL_CHAPTERS, MANUAL_EDITORIAL = load_manual_editorial()


sec_titles = [title_of(f.read_text()) for _, _, f in sections]
colophon_manual_body = None
for i, (part, ch, f) in enumerate(sections):
    source = f.read_text()
    repo_path = f.relative_to(ROOT).as_posix()
    treatment = MANUAL_EDITORIAL.get(repo_path)
    body = md_to_html(source)
    if f.name == "appendix_a_glossary.md":
        body = add_gloss_popovers(body)
    editorial_kind = None
    if treatment is None:
        crumb_bits = [part] + ([ch] if ch else [])
        crumb = '<p class="crumb">' + " &mdash; ".join(crumb_bits) + "</p>"
        body = crumb + body
    else:
        group_key = manual_editorial_group(repo_path)
        chapter_key = manual_editorial_chapter(repo_path)
        motif = MANUAL_GROUPS[group_key]["motif"]
        chapter_sections = [
            item
            for item in sections
            if item[0] == part and item[1] == ch
        ]
        chapter_paths = [item[2] for item in chapter_sections]
        body = apply_manual_editorial(
            body,
            treatment,
            ch,
            chapter_paths.index(f) + 1,
            len(chapter_paths),
            motif,
            sec_titles[i],
            group_key,
            chapter_key,
        )
        editorial_kind = "reference"
    prev_link = f'<a href="{slug(sections[i-1][2])}">&lsaquo; {sec_titles[i-1]}</a>' if i > 0 else ""
    next_link = f'<a href="{slug(sections[i+1][2])}">{sec_titles[i+1]} &rsaquo;</a>' if i + 1 < len(sections) else ""
    if treatment is None:
        footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">contents</a>{next_link}</div>'
    else:
        previous = (
            {"href": slug(sections[i - 1][2]), "title": sec_titles[i - 1]}
            if i > 0
            else None
        )
        following = (
            {"href": slug(sections[i + 1][2]), "title": sec_titles[i + 1]}
            if i + 1 < len(sections)
            else None
        )
        footer_nav = manual_editorial_navigation(previous, following)
    linked_body = link_manual_pages(link_text_citations(body), f)
    if f == colo:
        colophon_manual_body = linked_body
    (MANUAL_OUT / slug(f)).write_text(
        manual_page(
            linked_body,
            sec_titles[i],
            footer_nav,
            editorial_kind=editorial_kind,
            editorial_motif=motif if treatment is not None else None,
            editorial_variant=(
                treatment["variant"] if treatment is not None else None
            ),
        )
    )

if colophon_manual_body is None:
    raise ValueError("the manual colophon did not receive its treatment")
(BUILD_SITE / "colophon.html").write_text(colophon_page(colophon_manual_body))
print("wrote build/site/colophon.html from colophon.md")

# contents page generated from the same verified reading order
contents_entries = [
    (part, chapter, source, sec_titles[index])
    for index, (part, chapter, source) in enumerate(sections)
]
(MANUAL_OUT / "index.html").write_text(
    manual_page(
        manual_contents(contents_entries),
        "contents",
        editorial_kind="contents",
        editorial_motif="ordered_layers",
        editorial_variant="contents",
    )
)
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


BOOK_INDEX_PARTS = (
    {
        "roman": "I",
        "title": "The case",
        "chapters": (1, 2, 3),
        "description": (
            "Phi walks into a hurried public world, declines several of its "
            "habits, and takes its place among the older invented languages."
        ),
    },
    {
        "roman": "II",
        "title": "The language as argument",
        "chapters": (4, 5, 6, 7, 8),
        "description": (
            "Five chapters look inside Phi. They follow a sentence's machinery "
            "and the pull between words, then ask what the language refuses, "
            "whether literature can precede speakers, and how the work is done."
        ),
    },
    {
        "roman": "III",
        "title": "What it can honestly do now",
        "chapters": (9, 10, 11),
        "description": (
            "Phi's claims now meet the evidence: what serious leisure can do, "
            "the distance offered by a learned tongue, and how far language "
            "may shape thought."
        ),
    },
    {
        "roman": "IV",
        "title": "If it catches on",
        "chapters": (12, 13, 14),
        "description": (
            "Last, the book asks what happens outside its own covers: whether "
            "solarpunk communities might use Phi, what escapes when words "
            "travel alone, and what evidence a future community would owe "
            "itself."
        ),
    },
)


def book_index_icon(kind):
    """Return a restrained Lucide outline for the book contents."""
    # Lucide outlines; the deployed site carries the project's ISC notice.
    icons = {
        "book": (
            '<path d="M12 7v14"/>'
            '<path d="M3 18a1 1 0 0 1-1-1V5a2 2 0 0 1 2-2h5'
            'a3 3 0 0 1 3 3v15a3 3 0 0 0-3-3Z"/>'
            '<path d="M21 18a1 1 0 0 0 1-1V5a2 2 0 0 0-2-2h-5'
            'a3 3 0 0 0-3 3v15a3 3 0 0 1 3-3Z"/>'
        ),
        "waves": (
            '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5s2.5 2 '
            '5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>'
            '<path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 '
            '5-2s2.5 2 5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>'
            '<path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 '
            '5-2s2.5 2 5 2 2.5-2 5-2c1.3 0 1.9.5 2.5 1"/>'
        ),
        "door": (
            '<path d="M11 20H2"/>'
            '<path d="M11 4.56v16.16a1 1 0 0 0 1.24.97L19 20'
            'V5.56a2 2 0 0 0-1.52-1.94l-4-1A2 2 0 0 0 11 4.56Z"/>'
            '<path d="M11 4H8a2 2 0 0 0-2 2v14"/>'
            '<path d="M14 12h.01"/><path d="M22 20h-3"/>'
        ),
        "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    }
    if kind not in icons:
        raise ValueError(f"unknown book-index icon: {kind}")
    return (
        f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" '
        f'stroke="currentColor" stroke-linecap="round" '
        f'stroke-linejoin="round" stroke-width="1.5" focusable="false" '
        f'aria-hidden="true">{icons[kind]}</svg>'
    )


def book_index_expected_label(chapter, title):
    """Return the README label required for one published book file."""
    if chapter.stem == "00_the_boatman":
        return f"Opening: {title}"
    if chapter.stem == "15_the_door":
        return f"Close: {title}"
    if chapter.stem == "bibliography":
        return title
    number_match = re.match(r"([0-9]{2})_", chapter.stem)
    if number_match is None:
        raise ValueError(f"book chapter lacks a two-digit prefix: {chapter.name}")
    return f"Chapter {int(number_match.group(1))}: {title}"


def book_contents(body, chapters, titles):
    """Turn the book README into a checked map of its argument."""
    match = re.fullmatch(
        r"<h1>(?P<title>.*?)</h1>\n"
        r"(?P<intro>(?:<p>.*?</p>\n){4})"
        r"<h2>Read the current chapters</h2>\n"
        r"<ul>(?P<items>.*?)</ul>\n"
        r"(?P<closing><p>.*?</p>)",
        body.strip(),
        flags=re.S,
    )
    if match is None:
        raise ValueError("book README shape differs from the contents treatment")

    intro = re.findall(r"<p>.*?</p>", match.group("intro"), flags=re.S)
    if len(intro) != 4:
        raise ValueError("book README must have four opening paragraphs")
    opening_match = re.fullmatch(
        r"<p>(?P<lede>.+?\.) (?P<continuation>.+)</p>",
        intro[0],
        flags=re.S,
    )
    if opening_match is None:
        raise ValueError("book README opening must contain a two-sentence lead")
    lede = f"<p>{opening_match.group('lede')}</p>"
    continuation = f"<p>{opening_match.group('continuation')}</p>"

    found_items = re.findall(
        r'<li><a href="(?P<href>[^"]+)">(?P<label>.*?)</a></li>',
        match.group("items"),
        flags=re.S,
    )
    rebuilt_items = "".join(
        f'<li><a href="{href}">{label}</a></li>'
        for href, label in found_items
    )
    if rebuilt_items != match.group("items"):
        raise ValueError("book README chapter list contains unexpected markup")

    expected_items = [
        (
            f"{chapter.stem}.html",
            book_index_expected_label(chapter, titles[chapter.name]),
        )
        for chapter in chapters
    ]
    normalized_items = [
        (href, html_module.unescape(label))
        for href, label in found_items
    ]
    if normalized_items != expected_items:
        raise ValueError(
            "book README chapter list differs from the published chapter files"
        )

    numbered = {
        int(chapter.stem[:2]): chapter
        for chapter in chapters
        if re.match(r"^[0-9]{2}_", chapter.stem)
    }
    if set(numbered) != set(range(16)):
        raise ValueError("book contents expects numbered files 00 through 15")
    bibliography = next(
        (chapter for chapter in chapters if chapter.stem == "bibliography"),
        None,
    )
    if bibliography is None or len(chapters) != 17:
        raise ValueError("book contents expects sixteen readings and a bibliography")

    part_numbers = tuple(
        number
        for part in BOOK_INDEX_PARTS
        for number in part["chapters"]
    )
    if part_numbers != tuple(range(1, 15)):
        raise ValueError("book contents parts must cover chapters 1 through 14")

    part_jumps = []
    part_sections = []
    for part in BOOK_INDEX_PARTS:
        part_id = f"part-{part['roman'].lower()}"
        part_jumps.append(
            "<li>"
            f'<a href="#{part_id}">'
            f'<span>Part {part["roman"]}</span>'
            f"<strong>{html_module.escape(part['title'])}</strong>"
            "</a></li>"
        )
        chapter_rows = []
        for number in part["chapters"]:
            chapter = numbered[number]
            chapter_title = html_module.escape(titles[chapter.name])
            chapter_rows.append(
                '<li class="book-index-chapter">'
                f'<a href="{chapter.stem}.html">'
                f'<span class="book-index-chapter-number">{number:02d}</span>'
                '<span class="book-index-chapter-copy">'
                f'<span class="book-index-chapter-label">Chapter {number}</span>'
                f"<strong>{chapter_title}</strong>"
                "</span>"
                f'<span class="book-index-arrow">{book_index_icon("arrow")}</span>'
                "</a></li>"
            )
        part_sections.append(
            f'<section class="book-index-part book-index-part-{part["roman"].lower()}" '
            f'id="{part_id}" aria-labelledby="{part_id}-heading">'
            '<header class="book-index-part-header">'
            f'<p class="book-index-part-number">Part {part["roman"]}</p>'
            f'<h2 id="{part_id}-heading">'
            f'{html_module.escape(part["title"])}</h2>'
            f'<p>{html_module.escape(part["description"])}</p>'
            "</header>"
            f'<ol class="book-index-chapters">{"".join(chapter_rows)}</ol>'
            "</section>"
        )

    opening = numbered[0]
    closing = numbered[15]
    return (
        '<article class="book-index-work">'
        '<header class="book-index-header">'
        '<div class="book-index-meta">'
        '<p><span>Complete</span><span aria-hidden="true">·</span>'
        "<span>17 readings</span></p>"
        "<p>Why Phi is made this way</p>"
        "</div>"
        '<div class="book-index-title-row">'
        f"<h1>{match.group('title')}</h1>"
        '<div class="book-index-motif" aria-hidden="true">'
        f'{book_index_icon("book")}{book_index_icon("waves")}'
        "</div>"
        "</div>"
        f'<div class="book-index-lede">{lede}</div>'
        '<div class="book-index-premise">'
        f"{continuation}{intro[1]}{intro[2]}"
        "</div>"
        '<div class="book-index-status">'
        '<p class="book-index-status-count"><strong>14</strong> chapters</p>'
        f"{intro[3]}"
        "</div>"
        "</header>"
        '<div class="book-index-reader-anchor" data-reader-home></div>'
        '<nav class="book-index-map" aria-label="The book in four parts">'
        f'<ol>{"".join(part_jumps)}</ol>'
        "</nav>"
        '<section class="book-index-opening" aria-labelledby="book-opening-heading">'
        f'<a href="{opening.stem}.html">'
        '<span class="book-index-bookend-icon">'
        f'{book_index_icon("waves")}</span>'
        '<span class="book-index-bookend-copy">'
        '<span>Begin at the river</span>'
        f'<strong id="book-opening-heading">'
        f'{html_module.escape(titles[opening.name])}</strong>'
        "</span>"
        f'<span class="book-index-arrow">{book_index_icon("arrow")}</span>'
        "</a></section>"
        + "".join(part_sections)
        + '<section class="book-index-ending" aria-labelledby="book-ending-heading">'
        '<div class="book-index-closing">'
        f'<a href="{closing.stem}.html">'
        '<span class="book-index-bookend-icon">'
        f'{book_index_icon("door")}</span>'
        '<span class="book-index-bookend-copy">'
        '<span>Close</span>'
        f'<strong id="book-ending-heading">'
        f'{html_module.escape(titles[closing.name])}</strong>'
        "</span>"
        f'<span class="book-index-arrow">{book_index_icon("arrow")}</span>'
        "</a>"
        f"{match.group('closing')}"
        "</div>"
        f'<a class="book-index-bibliography" href="{bibliography.stem}.html">'
        '<span>Notes gathered at the end</span>'
        f"<strong>{html_module.escape(titles[bibliography.name])}</strong>"
        f'<span class="book-index-arrow">{book_index_icon("arrow")}</span>'
        "</a>"
        "</section>"
        "</article>"
    )


def book_page(body, title, footer_nav="", editorial=False, contents=False):
    if contents:
        body_class = "landing primer book-contents-page"
    else:
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
(BOOK_OUT / "index.html").write_text(
    book_page(
        book_contents(book_readme, book_chapters, book_titles),
        "contents",
        contents=True,
    )
)
print(f"wrote build/site/book/: {len(book_chapters)} chapters + contents")

# ---- the texts: translations, originals, and refusals rendered to build/site/texts/ ----

PHI_WORDS = {e["word"] for e in entries}

TEXT_MOTIFS = {
    "heart_radiance",
    "wind_sun",
    "people_equal",
    "dwelling_garden",
    "wool_journey",
    "water_open",
    "lotus_circle",
    "sun_sprout",
    "words_seed",
    "ring_refusal",
    "star_bond",
    "rabbit_heart",
    "window_water",
    "river_home",
}


def split_text_editorial_title(source_title, phi_title, repo_path):
    """Separate a validated Phi title from its English display title."""
    if not source_title.startswith(phi_title):
        raise ValueError(
            f"texts editorial title does not begin with its Phi title: {repo_path}"
        )
    title_tail = source_title[len(phi_title):]
    if title_tail.startswith(" — "):
        return phi_title, title_tail[3:]
    if title_tail.startswith(": "):
        return phi_title, title_tail[2:]
    raise ValueError(
        f"texts editorial title has no supported separator: {repo_path}"
    )


def load_texts_editorial():
    """Load opt-in literary treatments and reject stale source assumptions."""
    config_path = SITE_SRC / "texts_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or set(config) != {"pages"}:
        raise ValueError("site/texts_editorial.json must contain one 'pages' object")
    pages = config["pages"]
    if not isinstance(pages, dict):
        raise ValueError("site/texts_editorial.json pages must be an object")

    catalogued = {
        text_repo_path(work): work
        for work in [*TEXTS, *COLLECTION_TEXTS]
    }
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
            "translation": set(),
            "refusal": set(),
            "original": {
                "dialogue_blocks",
                "dialogue_speakers",
                "dialogue_actions",
                "ledger_rows",
            },
            "essay": {
                "argument_blocks",
                "argument_passages",
                "ledger_rows",
            },
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
        expected_method = {
            "translation": "Translation",
            "refusal": "Refusal",
            "original": "Original",
            "essay": "Original",
        }[form]
        if work["method"] != expected_method:
            raise ValueError(
                f"texts editorial source has incompatible method: {repo_path}"
            )

        source = (ROOT / repo_path).read_text(encoding="utf-8")
        source_title = title_of(source)
        if source_title != work["title"]:
            raise ValueError(
                f"texts editorial title differs from the catalogue: {repo_path}"
            )
        phi_title = treatment["phi_title"]
        _, english_title = split_text_editorial_title(
            source_title,
            phi_title,
            repo_path,
        )
        if (
            not is_current_phi(phi_title)
            or not english_title.strip()
        ):
            raise ValueError(f"invalid texts editorial Phi title: {repo_path}")

        sections = treatment["sections"]
        source_sections = re.findall(r"^## (.+)$", source, flags=re.M)
        section_fields = {"title", "kind"}
        section_kinds = {
            "translation",
            "translation_detail",
            "refusal",
            "complete",
            "apparatus",
            "context",
            "dialogue",
            "essay",
            "record",
            "pillars",
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
            "refusal": ["context", "refusal", "apparatus"],
            "original": ["dialogue", "record", "record", "pillars"],
            "essay": ["essay", "record", "record", "pillars"],
        }
        if form in expected_kinds and major_kinds != expected_kinds[form]:
            raise ValueError(
                f"texts editorial sections have the wrong order for {form}: "
                f"{repo_path}"
            )
        if form == "translation":
            first_complete = (
                major_kinds.index("complete")
                if "complete" in major_kinds
                else -1
            )
            if (
                first_complete < 1
                or any(
                    kind != "translation"
                    for kind in major_kinds[:first_complete]
                )
                or major_kinds[first_complete + 1:] == []
                or any(
                    kind != "apparatus"
                    for kind in major_kinds[first_complete + 1:]
                )
            ):
                raise ValueError(
                    "translation-only editorial sections must contain one or "
                    f"more translations, one complete reading, and apparatus: {repo_path}"
                )
        if form == "original":
            if any(
                treatment[field] != 0
                for field in (
                    "interlinear_blocks",
                    "interlinear_stanzas",
                    "source_free_blocks",
                    "source_free_stanzas",
                    "complete_readings",
                    "notes",
                    "pillar_sections",
                    "inner_dividers",
                )
            ):
                raise ValueError(
                    f"original editorial treatment has incompatible shared counts: "
                    f"{repo_path}"
                )
            speakers = treatment["dialogue_speakers"]
            if (
                not isinstance(treatment["dialogue_blocks"], int)
                or treatment["dialogue_blocks"] < 1
                or not isinstance(treatment["dialogue_actions"], int)
                or treatment["dialogue_actions"] < 0
                or not isinstance(speakers, dict)
                or len(speakers) < 2
                or any(
                    not re.fullmatch(r"[A-Z]", label)
                    or not isinstance(speaker, dict)
                    or set(speaker) != {"name", "turns"}
                    or not isinstance(speaker["name"], str)
                    or not re.fullmatch(r"[a-z]+", speaker["name"])
                    or not isinstance(speaker["turns"], int)
                    or speaker["turns"] < 1
                    for label, speaker in speakers.items()
                )
                or not isinstance(treatment["ledger_rows"], list)
                or len(
                    {speaker["name"] for speaker in speakers.values()}
                ) != len(speakers)
                or len(treatment["ledger_rows"]) != treatment["tables"]
                or any(
                    not isinstance(row_count, int) or row_count < 1
                    for row_count in treatment["ledger_rows"]
                )
            ):
                raise ValueError(
                    f"invalid original editorial structure: {repo_path}"
                )
        if form == "essay":
            if any(
                treatment[field] != 0
                for field in (
                    "interlinear_blocks",
                    "interlinear_stanzas",
                    "source_free_blocks",
                    "source_free_stanzas",
                    "complete_readings",
                    "notes",
                    "pillar_sections",
                    "inner_dividers",
                )
            ):
                raise ValueError(
                    f"essay editorial treatment has incompatible shared counts: "
                    f"{repo_path}"
                )
            if (
                not isinstance(treatment["argument_blocks"], int)
                or treatment["argument_blocks"] < 1
                or not isinstance(treatment["argument_passages"], int)
                or treatment["argument_passages"] < treatment["argument_blocks"]
                or not isinstance(treatment["ledger_rows"], list)
                or len(treatment["ledger_rows"]) != treatment["tables"]
                or any(
                    not isinstance(row_count, int) or row_count < 1
                    for row_count in treatment["ledger_rows"]
                )
            ):
                raise ValueError(
                    f"invalid essay editorial structure: {repo_path}"
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


def split_news_chapter_title(source_title, phi_title, english_title, repo_path):
    """Separate one validated book chapter heading into its number and title."""
    prefix = f"{phi_title} — {english_title}, ch. "
    if not source_title.startswith(prefix):
        raise ValueError(f"News from Nowhere chapter title differs: {repo_path}")
    match = re.fullmatch(r"([0-9]+): (.+)", source_title[len(prefix):])
    if match is None:
        raise ValueError(f"News from Nowhere chapter title is malformed: {repo_path}")
    return int(match.group(1)), match.group(2)


def load_news_editorial():
    """Load the book treatment and pin every current chapter to its source."""
    config_path = SITE_SRC / "news_from_nowhere_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or set(config) != {"book"}:
        raise ValueError(
            "site/news_from_nowhere_editorial.json must contain one 'book' object"
        )
    book = config["book"]
    book_fields = {
        "path",
        "phi_title",
        "english_title",
        "motif",
        "total_chapters",
        "chapters",
    }
    if not isinstance(book, dict) or set(book) != book_fields:
        raise ValueError(
            "News from Nowhere editorial book requires "
            f"{', '.join(sorted(book_fields))}"
        )

    repo_path = f"texts/{NEWS_WORK['path']}"
    phi_title = book["phi_title"]
    english_title = book["english_title"]
    if (
        book["path"] != repo_path
        or NEWS_WORK["method"] != "Book in progress"
        or not isinstance(phi_title, str)
        or not is_current_phi(phi_title)
        or not isinstance(english_title, str)
        or not english_title.strip()
        or book["motif"] not in TEXT_MOTIFS
    ):
        raise ValueError("News from Nowhere editorial identity differs from the shelf")
    catalogue_phi, catalogue_english = split_text_editorial_title(
        NEWS_WORK["title"],
        phi_title,
        repo_path,
    )
    if catalogue_phi != phi_title or catalogue_english != english_title:
        raise ValueError("News from Nowhere editorial title differs from the catalogue")

    total_chapters = book["total_chapters"]
    chapters = book["chapters"]
    book_dir = ROOT / repo_path
    chapter_files = sorted(path.name for path in book_dir.glob("chapter_*.md"))
    if (
        not isinstance(total_chapters, int)
        or total_chapters < 1
        or not isinstance(chapters, list)
        or not chapters
        or len(chapters) > total_chapters
        or [chapter.get("file") for chapter in chapters] != chapter_files
    ):
        raise ValueError("News from Nowhere editorial chapter sequence differs")

    chapter_fields = {
        "file",
        "number",
        "title",
        "method",
        "summary",
        "movements",
        "apparatus",
        "opening_paragraphs",
        "interlinear_blocks",
        "interlinear_stanzas",
        "notes",
        "tables",
        "ledger_rows",
        "inner_dividers",
    }
    movement_fields = {"level", "title"}
    count_fields = (
        "opening_paragraphs",
        "interlinear_blocks",
        "interlinear_stanzas",
        "notes",
        "tables",
        "inner_dividers",
    )
    for expected_number, chapter in enumerate(chapters, 1):
        if not isinstance(chapter, dict) or set(chapter) != chapter_fields:
            raise ValueError(
                "News from Nowhere editorial chapter requires "
                f"{', '.join(sorted(chapter_fields))}"
            )
        filename = chapter["file"]
        movements = chapter["movements"]
        if (
            chapter["number"] != expected_number
            or filename != f"chapter_{expected_number:02d}.md"
            or not isinstance(chapter["title"], str)
            or not chapter["title"].strip()
            or chapter["method"] not in {"Translation", "Transmutation"}
            or not isinstance(chapter["summary"], str)
            or not chapter["summary"].strip()
            or not isinstance(movements, list)
            or not movements
            or any(
                not isinstance(movement, dict)
                or set(movement) != movement_fields
                or movement["level"] not in {2, 3}
                or not isinstance(movement["title"], str)
                or not movement["title"].strip()
                for movement in movements
            )
            or len({movement["title"] for movement in movements}) != len(movements)
            or not isinstance(chapter["apparatus"], str)
            or not chapter["apparatus"].strip()
            or chapter["apparatus"] in {
                movement["title"] for movement in movements
            }
            or any(
                not isinstance(chapter[field], int) or chapter[field] < 0
                for field in count_fields
            )
            or not isinstance(chapter["ledger_rows"], list)
            or len(chapter["ledger_rows"]) != chapter["tables"]
            or any(
                not isinstance(row_count, int) or row_count < 1
                for row_count in chapter["ledger_rows"]
            )
        ):
            raise ValueError(
                f"invalid News from Nowhere editorial chapter: {filename}"
            )

        source_path = book_dir / filename
        source = source_path.read_text(encoding="utf-8")
        source_number, source_chapter_title = split_news_chapter_title(
            title_of(source),
            phi_title,
            english_title,
            source_path.relative_to(ROOT).as_posix(),
        )
        source_headings = [
            (len(marks), title)
            for marks, title in re.findall(
                r"^(#{2,3}) (.+)$",
                source,
                flags=re.M,
            )
        ]
        expected_headings = [
            (movement["level"], movement["title"])
            for movement in movements
        ] + [(2, chapter["apparatus"])]
        source_labels = re.findall(
            r"^([a-z][a-z0-9-]*):",
            source,
            flags=re.M,
        )
        if (
            source_number != expected_number
            or source_chapter_title != chapter["title"]
            or source_headings != expected_headings
            or len(source_labels) != chapter["interlinear_stanzas"]
            or any(label != "morris" for label in source_labels)
            or len(re.findall(r"^---$", source, flags=re.M))
            != chapter["inner_dividers"] + 1
        ):
            raise ValueError(
                f"News from Nowhere editorial source differs: {filename}"
            )
    return book


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
    heart = """
    <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3.33.82-4.5 2.09C10.83 3.82 9.26 3 7.5 3A5.5 5.5 0 0 0 2 8.5C2 10.79 3.51 12.54 5 14l7 7Z"/>"""
    lotus = """
    <path d="M12 5a3 3 0 1 1 3 3m-3-3a3 3 0 1 0-3 3m3-3v1M9 8a3 3 0 1 0 3 3M9 8h1m5 0a3 3 0 1 1-3 3m3-3h-1m-2 3v-1"/>
    <circle cx="12" cy="8" r="2"/>
    <path d="M12 10v12"/>
    <path d="M12 22c4.2 0 7-1.667 7-5-4.2 0-7 1.667-7 5Z"/>
    <path d="M12 22c-4.2 0-7-1.667-7-5 4.2 0 7 1.667 7 5Z"/>"""
    ban = """
    <circle cx="12" cy="12" r="10"/>
    <path d="M4.929 4.929 19.07 19.071"/>"""
    star = """
    <path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>"""
    link = """
    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>"""
    rabbit = """
    <path d="M13 16a3 3 0 0 1 2.24 5"/>
    <path d="M18 12h.01"/>
    <path d="M18 21h-8a4 4 0 0 1-4-4 7 7 0 0 1 7-7h.2L9.6 6.4a1 1 0 1 1 2.8-2.8L15.8 7h.2c3.3 0 6 2.7 6 6v1a2 2 0 0 1-2 2h-1a3 3 0 0 0-3 3"/>
    <path d="M20 8.54V4a2 2 0 1 0-4 0v3"/>
    <path d="M7.612 12.524a3 3 0 1 0-1.6 4.3"/>"""
    window = """
    <rect width="18" height="18" x="3" y="3" rx="2"/>
    <path d="M3 9h18"/>
    <path d="M9 21V9"/>"""
    droplet = """
    <path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>"""
    motifs = {
        "heart_radiance": (heart, circle),
        "wind_sun": (wind, sun),
        "people_equal": (people, equal),
        "dwelling_garden": (dwelling, sprout),
        "wool_journey": (waves, journey),
        "water_open": (waves, circle),
        "lotus_circle": (circle, lotus),
        "sun_sprout": (sun, sprout),
        "words_seed": (words, sprout),
        "ring_refusal": (circle, ban),
        "star_bond": (star, link),
        "rabbit_heart": (rabbit, heart),
        "window_water": (window, droplet),
        "river_home": (waves, dwelling),
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
    """Return the Lucide mark for one editorial section kind."""
    paths = {
        "translation": (
            '<path d="M21 6H3"/><path d="M15 12H3"/>'
            '<path d="M17 18H3"/>'
        ),
        "refusal": (
            '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2'
            'c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/>'
            '<path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>'
        ),
        "collection_detail": (
            '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>'
            '<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
        ),
        "complete": (
            '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>'
            '<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
        ),
        "apparatus": (
            '<path d="M9 6h11"/><path d="M9 12h11"/><path d="M9 18h11"/>'
            '<path d="M5 6h.01"/><path d="M5 12h.01"/><path d="M5 18h.01"/>'
        ),
        "context": (
            '<circle cx="11" cy="11" r="8"/>'
            '<path d="m21 21-4.3-4.3"/>'
        ),
        "dialogue": (
            '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29'
            'a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092'
            ' 10 10 0 1 0-4.777-4.719"/>'
            '<path d="M8 12h.01"/><path d="M12 12h.01"/>'
            '<path d="M16 12h.01"/>'
        ),
        "essay": (
            '<path d="M4 4h9a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/>'
            '<path d="M20 4h-4a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h5z"/>'
            '<path d="M7 9h5"/><path d="M7 13h4"/>'
        ),
        "record": (
            '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/>'
            '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6'
            'a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>'
            '<path d="M12 11h4"/><path d="M12 16h4"/>'
            '<path d="M8 11h.01"/><path d="M8 16h.01"/>'
        ),
        "pillars": (
            '<path d="M12 5a3 3 0 1 1 3 3m-3-3a3 3 0 1 0-3 3m3-3v1'
            'M9 8a3 3 0 1 0 3 3M9 8h1m5 0a3 3 0 1 1-3 3m3-3h-1'
            'm-2 3v-1"/>'
            '<circle cx="12" cy="8" r="2"/><path d="M12 10v12"/>'
            '<path d="M12 22c4.2 0 7-1.667 7-5-4.2 0-7 1.667-7 5Z"/>'
            '<path d="M12 22c-4.2 0-7-1.667-7-5 4.2 0 7 1.667 7 5Z"/>'
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
    automatic_forms = {"translation", "refusal", "original", "essay"}
    if treatment["form"] in automatic_forms:
        map_items = [
            {
                "label": (
                    section["title"].split(" — ", 1)[1]
                    if (
                        treatment["form"] == "refusal"
                        and " — " in section["title"]
                        and is_current_phi(section["title"].split(" — ", 1)[0])
                    )
                    else section["title"]
                ),
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


def style_original_dialogue(body, repo_path, treatment):
    """Render and verify the exact speaker turns in an original Phi dialogue."""
    speakers = treatment["dialogue_speakers"]
    speaker_names = {speaker["name"] for speaker in speakers.values()}
    speaker_counts = {label: 0 for label in speakers}
    block_count = 0
    action_count = 0

    def is_original_phi(value):
        text = html_module.unescape(value).strip()
        if not re.fullmatch(r"[a-z]+(?:[ .]+[a-z]+)*[.]?", text):
            return False
        words = re.findall(r"[a-z]+", text)
        return bool(words) and all(
            word in ALL_WORDS or word in speaker_names
            for word in words
        )

    def render_reading(phi, gloss, literal):
        return (
            '<div class="text-dialogue-body">'
            f'<p class="text-phi-line" lang="art-x-phi">{phi}</p>'
            '<p class="text-gloss-line">'
            '<span class="visually-hidden">Word-by-word gloss: </span>'
            f"{gloss}</p>"
            '<div class="text-dialogue-close-reading">'
            '<p class="text-literal-line">'
            '<span class="visually-hidden">Close English reading: </span>'
            f"{literal}</p>"
            "</div>"
            "</div>"
        )

    def convert(match):
        nonlocal action_count, block_count
        raw = match.group(1).strip()
        groups = re.split(r"\n[ \t]*\n", raw)
        rendered = []
        for group in groups:
            lines = [line.strip() for line in group.splitlines()]
            if (
                len(lines) != 3
                or not lines[2].startswith("(")
                or not lines[2].endswith(")")
            ):
                first_line = lines[0][:80] if lines else "(empty)"
                raise ValueError(
                    f"unrecognized original dialogue turn in {repo_path}: "
                    f"{first_line}"
                )
            speaker_match = re.fullmatch(r"([A-Z]):\s+(.+)", lines[0])
            if speaker_match is not None:
                label, phi = speaker_match.groups()
                if label not in speakers or not is_original_phi(phi):
                    raise ValueError(
                        f"invalid original dialogue speaker turn in {repo_path}: "
                        f"{lines[0][:80]}"
                    )
                speaker = speakers[label]
                speaker_counts[label] += 1
                rendered.append(
                    '<div class="text-dialogue-turn text-dialogue-speaker-turn" '
                    f'data-speaker="{html_module.escape(label, quote=True)}" '
                    f'role="group" '
                    f'aria-label="{html_module.escape(speaker["name"], quote=True)} '
                    'speaks">'
                    '<div class="text-dialogue-who">'
                    '<span class="text-dialogue-initial" aria-hidden="true">'
                    f"{html_module.escape(label)}</span>"
                    '<span class="text-dialogue-name" lang="art-x-phi">'
                    f'{html_module.escape(speaker["name"])}</span>'
                    "</div>"
                    f"{render_reading(phi, lines[1], lines[2])}"
                    "</div>"
                )
            else:
                if re.match(r"[A-Z]:", lines[0]) or not is_original_phi(lines[0]):
                    raise ValueError(
                        f"invalid original dialogue action in {repo_path}: "
                        f"{lines[0][:80]}"
                    )
                action_count += 1
                rendered.append(
                    '<div class="text-dialogue-turn text-dialogue-action" '
                    'role="group" aria-label="Scene action">'
                    '<div class="text-dialogue-who">'
                    '<span class="text-dialogue-scene">scene</span>'
                    "</div>"
                    f"{render_reading(lines[0], lines[1], lines[2])}"
                    "</div>"
                )
        block_count += 1
        return (
            '<div class="text-dialogue" aria-label="Original Phi dialogue">'
            + "".join(rendered)
            + "</div>"
        )

    body = re.sub(r"<pre>(.*?)</pre>", convert, body, flags=re.S)
    if block_count != treatment["dialogue_blocks"]:
        raise ValueError(
            f"texts editorial dialogue block count differs in {repo_path}: "
            f"expected {treatment['dialogue_blocks']}, found {block_count}"
        )
    if action_count != treatment["dialogue_actions"]:
        raise ValueError(
            f"texts editorial dialogue action count differs in {repo_path}: "
            f"expected {treatment['dialogue_actions']}, found {action_count}"
        )
    expected_counts = {
        label: speaker["turns"]
        for label, speaker in speakers.items()
    }
    if speaker_counts != expected_counts:
        raise ValueError(
            f"texts editorial dialogue speaker counts differ in {repo_path}: "
            f"expected {expected_counts}, found {speaker_counts}"
        )
    if "<pre>" in body:
        raise ValueError(f"editorial text left an untreated fence in {repo_path}")
    return body


def style_original_essay(body, repo_path, treatment):
    """Render and verify the passages of an original Phi essay.

    An essay argues in one voice, so its fence holds plain three-line
    passages with no speaker column: the Phi, its gloss, and the close
    English reading."""
    block_count = 0
    passage_count = 0

    def convert(match):
        nonlocal block_count, passage_count
        raw = match.group(1).strip()
        rendered = []
        for group in re.split(r"\n[ \t]*\n", raw):
            lines = [line.strip() for line in group.splitlines()]
            if (
                len(lines) != 3
                or not lines[2].startswith("(")
                or not lines[2].endswith(")")
            ):
                first_line = lines[0][:80] if lines else "(empty)"
                raise ValueError(
                    f"unrecognized original essay passage in {repo_path}: "
                    f"{first_line}"
                )
            passage_count += 1
            rendered.append(
                '<div class="text-essay-passage" role="group" '
                f'aria-label="Passage {passage_count}">'
                f'<p class="text-phi-line" lang="art-x-phi">{lines[0]}</p>'
                '<p class="text-gloss-line">'
                '<span class="visually-hidden">Word-by-word gloss: </span>'
                f"{lines[1]}</p>"
                '<div class="text-essay-close-reading">'
                '<p class="text-literal-line">'
                '<span class="visually-hidden">Close English reading: </span>'
                f"{lines[2]}</p>"
                "</div>"
                "</div>"
            )
        block_count += 1
        return (
            '<div class="text-essay" aria-label="Original Phi essay">'
            + "".join(rendered)
            + "</div>"
        )

    body = re.sub(r"<pre>(.*?)</pre>", convert, body, flags=re.S)
    if block_count != treatment["argument_blocks"]:
        raise ValueError(
            f"texts editorial essay block count differs in {repo_path}: "
            f"expected {treatment['argument_blocks']}, found {block_count}"
        )
    if passage_count != treatment["argument_passages"]:
        raise ValueError(
            f"texts editorial essay passage count differs in {repo_path}: "
            f"expected {treatment['argument_passages']}, found {passage_count}"
        )
    if "<pre>" in body:
        raise ValueError(f"editorial text left an untreated fence in {repo_path}")
    return body


def style_text_fences(body, repo_path, treatment):
    """Turn a literary work's exact fences into readings and interlinear rows."""
    counts = {
        "interlinear_blocks": 0,
        "interlinear_stanzas": 0,
        "source_free_blocks": 0,
        "source_free_stanzas": 0,
        "complete_readings": 0,
    }

    def source_witness(serialized):
        try:
            witness = json.loads(serialized)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"invalid quoted source witness in {repo_path}: {serialized}"
            ) from exc
        if not isinstance(witness, str):
            raise ValueError(
                f"source witness is not text in {repo_path}: {serialized}"
            )
        return witness

    def stanza(phi, gloss, literal, source_name=None, source_lines=None):
        source = ""
        class_name = "text-stanza"
        if source_name is not None:
            source_copy = "<br>".join(source_lines)
            source = (
                '<p class="text-source-line">'
                f'<span class="text-source-name">{source_name}:</span> '
                f"<span>{source_copy}</span></p>"
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
            if len(lines) < 4:
                parsed = []
                break
            source_matches = [
                re.fullmatch(
                    r"([a-z][a-z0-9-]*):\s*(.+)",
                    line,
                    flags=re.S,
                )
                for line in lines[3:]
            ]
            if (
                not is_text_phi_passage(lines[0])
                or not lines[2].startswith("(")
                or not lines[2].endswith(")")
                or any(source_match is None for source_match in source_matches)
                or len({source_match.group(1) for source_match in source_matches}) != 1
            ):
                parsed = []
                break
            parsed.append(
                (
                    lines[0],
                    lines[1],
                    lines[2],
                    source_matches[0].group(1),
                    tuple(
                        source_witness(source_match.group(2))
                        for source_match in source_matches
                    ),
                )
            )

        if parsed:
            counts["interlinear_blocks"] += 1
            counts["interlinear_stanzas"] += len(parsed)
            stanzas = [
                stanza(phi, gloss, literal, source_name, source_lines)
                for phi, gloss, literal, source_name, source_lines in parsed
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

        reading_groups = [
            [line.strip() for line in group.splitlines() if line.strip()]
            for group in groups
            if group.strip()
        ]
        if reading_groups and all(
            lines and all(is_text_phi_passage(line) for line in lines)
            for lines in reading_groups
        ):
            counts["complete_readings"] += 1
            rendered_groups = []
            line_index = 0
            for lines in reading_groups:
                rendered_lines = []
                for reading in lines:
                    class_name = (
                        "text-reading-line text-reading-title"
                        if line_index == 0
                        else "text-reading-line"
                    )
                    rendered_lines.append(
                        f'<p class="{class_name}" lang="art-x-phi">{reading}</p>'
                    )
                    line_index += 1
                rendered_groups.append(
                    '<div class="text-reading-stanza">'
                    + "".join(rendered_lines)
                    + "</div>"
                )
            return (
                '<section class="text-complete-reading" '
                'aria-label="Complete Phi reading">'
                + "".join(rendered_groups)
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
    row_counts = []

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
        row_counts.append(len(rows) - 1)
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
    if "ledger_rows" in treatment and row_counts != treatment["ledger_rows"]:
        raise ValueError(
            f"texts editorial table row counts differ in {repo_path}: "
            f"expected {treatment['ledger_rows']}, found {row_counts}"
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
        classes = []
        verse = re.fullmatch(r"Verse ([0-9]+): (.+)", plain)
        proposition = re.fullmatch(r"([0-9]+)\. (.+)", plain)
        if verse is not None:
            kind = "text-scene-heading"
            classes.extend(("text-numbered-heading", "text-verse-heading"))
            title = (
                '<span class="text-heading-number">'
                f'{int(verse.group(1)):02d}</span>'
                '<span class="text-heading-label">'
                f'{html_module.escape(verse.group(2))}</span>'
            )
        elif proposition is not None:
            kind = "text-scene-heading"
            classes.extend(("text-numbered-heading", "text-proposition-heading"))
            title = (
                '<span class="text-heading-number">'
                f'{int(proposition.group(1)):02d}</span>'
                '<span class="text-heading-label">'
                f'{html_module.escape(proposition.group(2))}</span>'
            )
        elif plain.startswith("Complete "):
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
        class_names = " ".join((kind, *classes))
        return f'<h3 class="{class_names}">{title}</h3>'

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


def text_method_heading(title, kind, form, sequence_number=None):
    """Build a major method heading with its nonverbal mark."""
    kind_class = kind.replace("_", "-")
    heading = html_module.escape(title)
    if form == "refusal" and " — " in title:
        phi, english = title.split(" — ", 1)
        if is_current_phi(phi):
            heading = (
                '<span class="text-heading-copy">'
                f'<span class="text-subheading-phi" lang="art-x-phi">'
                f'{html_module.escape(phi)}</span>'
                f'<span class="text-subheading-english">'
                f'{html_module.escape(english)}</span>'
                "</span>"
            )
    lead = (
        '<span class="text-section-number" aria-hidden="true">'
        f"{sequence_number:02d}</span>"
        if sequence_number is not None
        else text_section_icon(kind)
    )
    return (
        f'<h2 class="text-method-heading text-{kind_class}-heading" '
        f'id="{text_heading_slug(title)}">'
        f"{lead}"
        f"{heading}"
        "</h2>"
    )


def apply_text_editorial(body, source, repo_path, treatment):
    """Apply an editorial treatment to one validated literary work."""
    source_title = title_of(source)
    phi_title, english_title = split_text_editorial_title(
        source_title,
        treatment["phi_title"],
        repo_path,
    )
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
    if treatment["form"] == "translation":
        method_label = '<span>Translation</span>'
    elif treatment["form"] == "refusal":
        method_label = '<span>Refusal</span>'
    else:
        method_label = '<span>Original</span>'
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

    opening_boundary = (
        r"(?=<h2>)"
        if treatment["form"] in {"original", "essay"}
        else r"<hr>"
    )
    opening_pattern = re.compile(
        r"(</header>)\s*((?:<p>.*?</p>\s*)+)" + opening_boundary,
        flags=re.S,
    )
    opening = opening_pattern.search(body)
    if opening is None:
        raise ValueError(f"editorial text opening differs in {repo_path}")
    opening_paragraphs = re.findall(
        r"<p>(.*?)</p>",
        opening.group(2),
        flags=re.S,
    )
    opening_paragraphs = [
        (
            fully_emphasized.group(1)
            if (
                fully_emphasized := re.fullmatch(
                    r"<em>(.*?)</em>",
                    paragraph,
                    flags=re.S,
                )
            )
            else re.sub(r"</?em>", "", paragraph)
        )
        for paragraph in opening_paragraphs
    ]
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
        original = f'<h2>{html_module.escape(section["title"], quote=False)}</h2>'
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
    refusal_total = sum(
        section["kind"] == "refusal"
        for section in major_sections
    )
    refusal_index = 0
    for section in major_sections:
        title = section["title"]
        kind = section["kind"]
        sequence_number = None
        if kind == "refusal":
            refusal_index += 1
            if treatment["form"] == "refusal" and refusal_total > 1:
                sequence_number = refusal_index
        original = f"<h2>{html_module.escape(title, quote=False)}</h2>"
        if body.count(original) != 1:
            raise ValueError(
                f"editorial text section heading differs in {repo_path}: {title}"
            )
        marker = text_method_heading(
            title,
            kind,
            treatment["form"],
            sequence_number,
        )
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
        if kind in {"translation", "refusal"}:
            class_name = f"text-rendering text-{kind}"
        elif kind == "context":
            class_name = "text-context"
        elif kind == "complete":
            class_name = "text-complete-section"
        elif kind == "apparatus":
            class_name = "text-apparatus"
        elif kind == "dialogue":
            class_name = "text-dialogue-section"
        elif kind == "essay":
            class_name = "text-essay-section"
        elif kind == "record":
            class_name = "text-record-section"
        elif kind == "pillars":
            class_name = "text-pillars-section"
        else:
            raise ValueError(f"unhandled texts editorial section kind: {kind}")
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
    if treatment["form"] == "original":
        body = style_original_dialogue(body, repo_path, treatment)
    elif treatment["form"] == "essay":
        body = style_original_essay(body, repo_path, treatment)
    else:
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
NEWS_EDITORIAL = load_news_editorial()

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
                    out.append(
                        '<span class="teng-dual" aria-hidden="true">'
                        f"{rendered}</span>"
                    )
            out.append(line)
        return "<pre>" + "\n".join(out) + "</pre>"
    return re.sub(r"<pre>(.*?)</pre>", do_pre, html, flags=re.S)

TEXTS_OUT = BUILD_SITE / "texts"
prepare_html_output(TEXTS_OUT)


def texts_nav(depth):
    root_prefix = "../" * depth
    texts_index = "index.html" if depth == 1 else "../index.html"
    return f'<nav class="topnav"><a href="{root_prefix}index.html">kia</a> <span class="sep">&middot;</span> <a href="{root_prefix}short_road.html">walk</a> <span class="sep">&middot;</span> <a href="{root_prefix}primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="{root_prefix}book/index.html">book</a> <span class="sep">&middot;</span> <a href="{root_prefix}manual/index.html">manual</a> <span class="sep">&middot;</span> <a href="{root_prefix}pamphlets/index.html">pamphlets</a> <span class="sep">&middot;</span> <a class="here" href="{texts_index}">texts</a> <span class="sep">&middot;</span> <a href="{root_prefix}explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'


def texts_page(
    body,
    title,
    depth=1,
    footer_nav=None,
    editorial_kind=None,
    editorial_motif=None,
):
    root_prefix = "../" * depth
    texts_index = "index.html" if depth == 1 else "../index.html"
    if footer_nav is None:
        footer_nav = f'<div class="chapnav"><a href="{texts_index}">all texts</a></div>'
    body_class = "landing primer"
    content = f"{body}\n{footer_nav}"
    if editorial_kind is not None:
        body_class += f" text-editorial text-{editorial_kind}-page"
        if editorial_motif is not None:
            motif_class = editorial_motif.replace("_", "-")
            body_class += f" text-{motif_class}-page"
        content = f'<article class="text-work">\n{body}\n{footer_nav}\n</article>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Phi literature in translation, original composition, and refusal, from the Metta Sutta to News from Nowhere.">
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
  <p>Each work identifies its relationship to a source. Source witnesses, where a work has one, live with the texts in <a href="https://github.com/dcellison/phi/tree/main/texts">the repository</a>. The site renders them at build time.
     The <a href="{root_prefix}colophon.html">colophon</a> records how Phi is made.</p>
</footer>
</body>
</html>
"""


def text_work_nav(works, index, index_label="All texts", item_noun="work"):
    """Build previous, contents, and next navigation for a work sequence."""
    links = []
    if index > 0:
        previous = works[index - 1]
        links.append(
            f'<a class="text-work-prev" href="{Path(previous["path"]).stem}.html">'
            f'<span class="text-nav-direction">&lsaquo; Previous {item_noun}</span>'
            f'<span class="text-nav-title">{html_module.escape(previous["title"])}</span>'
            "</a>"
        )
    else:
        links.append('<span class="text-work-nav-space" aria-hidden="true"></span>')
    links.append(
        '<a class="text-work-index" href="index.html">'
        f"{html_module.escape(index_label)}</a>"
    )
    if index + 1 < len(works):
        following = works[index + 1]
        links.append(
            f'<a class="text-work-next" href="{Path(following["path"]).stem}.html">'
            f'<span class="text-nav-direction">Next {item_noun} &rsaquo;</span>'
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
    editorial_motif = None
    if treatment is not None:
        rendered = apply_text_editorial(
            rendered,
            md,
            repo_path,
            treatment,
        )
        footer_nav = text_work_nav(TEXTS, work_index)
        editorial_kind = treatment["form"]
        editorial_motif = treatment["motif"]
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
            editorial_motif=editorial_motif,
        )
    )

def news_link_arrow():
    """Return the Lucide arrow used by book and chapter links."""
    return (
        '<span class="news-link-arrow" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" focusable="false">'
        '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'
        "</svg></span>"
    )


def split_news_movement_title(title):
    """Separate a movement's optional Phi title from its English title."""
    if " — " in title:
        phi_title, english_title = title.split(" — ", 1)
        if is_current_phi(phi_title) and english_title.strip():
            return phi_title, english_title
    return None, title


def news_chapter_map(chapter):
    """Build a complete movement map for one book chapter."""
    items = []
    for index, movement in enumerate(chapter["movements"], 1):
        phi_title, english_title = split_news_movement_title(movement["title"])
        phi = (
            f'<span class="news-map-phi" lang="art-x-phi">'
            f"{html_module.escape(phi_title)}</span>"
            if phi_title is not None
            else ""
        )
        items.append(
            "<li>"
            f'<a href="#{text_heading_slug(movement["title"])}">'
            f'<span class="news-map-number">{index:02d}</span>'
            '<span class="news-map-copy">'
            f"{phi}"
            f'<span class="news-map-title">{html_module.escape(english_title)}</span>'
            "</span>"
            "</a></li>"
        )
    return (
        '<nav class="news-chapter-map" aria-label="In this chapter">'
        '<p class="news-chapter-map-label">In this chapter</p>'
        f'<ol>{"".join(items)}</ol>'
        "</nav>"
    )


def news_movement_heading(movement, sequence_number):
    """Build a numbered chapter movement heading without changing its level."""
    title = movement["title"]
    phi_title, english_title = split_news_movement_title(title)
    phi = (
        f'<span class="news-movement-phi" lang="art-x-phi">'
        f"{html_module.escape(phi_title)}</span>"
        if phi_title is not None
        else ""
    )
    level = movement["level"]
    return (
        f'<h{level} class="news-movement-heading" '
        f'id="{text_heading_slug(title)}">'
        f'<span class="news-movement-number" aria-hidden="true">'
        f"{sequence_number:02d}</span>"
        '<span class="news-movement-copy">'
        f"{phi}"
        f'<span class="news-movement-english">'
        f"{html_module.escape(english_title)}</span>"
        f"</span></h{level}>"
    )


def news_chapter_nav(chapters, index):
    """Build chapter navigation with the adjacent titles in view."""
    links = []
    if index > 0:
        previous = chapters[index - 1]
        links.append(
            f'<a class="news-chapter-prev" '
            f'href="{Path(previous["file"]).stem}.html">'
            '<span class="news-nav-direction">&lsaquo; Previous chapter</span>'
            f'<span class="news-nav-title">{html_module.escape(previous["title"])}</span>'
            "</a>"
        )
    else:
        links.append('<span class="news-nav-space" aria-hidden="true"></span>')
    links.append('<a class="news-chapter-contents" href="index.html">Book contents</a>')
    if index + 1 < len(chapters):
        following = chapters[index + 1]
        links.append(
            f'<a class="news-chapter-next" '
            f'href="{Path(following["file"]).stem}.html">'
            '<span class="news-nav-direction">Next chapter &rsaquo;</span>'
            f'<span class="news-nav-title">{html_module.escape(following["title"])}</span>'
            "</a>"
        )
    else:
        links.append('<span class="news-nav-space" aria-hidden="true"></span>')
    return (
        '<nav class="chapnav news-chapter-nav" aria-label="Book navigation">'
        + "".join(links)
        + "</nav>"
    )


def apply_news_chapter_editorial(body, source, chapter, book):
    """Render one complete chapter and reject any source-shape drift."""
    repo_path = f'{book["path"]}/{chapter["file"]}'
    source_title = title_of(source)
    source_number, source_chapter_title = split_news_chapter_title(
        source_title,
        book["phi_title"],
        book["english_title"],
        repo_path,
    )
    heading = re.search(r"<h1>(.*?)</h1>", body, flags=re.S)
    if (
        heading is None
        or html_module.unescape(heading.group(1)) != source_title
        or source_number != chapter["number"]
        or source_chapter_title != chapter["title"]
    ):
        raise ValueError(f"News from Nowhere chapter heading differs: {repo_path}")
    tengwar_title = tengwar.render_line(book["phi_title"])
    if tengwar_title is None:
        raise ValueError("News from Nowhere title cannot render in Tengwar")
    title_class = (
        " news-chapter-title-long"
        if len(chapter["title"]) > 30
        else ""
    )
    header = f"""
<header class="news-chapter-header">
  <div class="news-chapter-meta">
    <p class="news-book-kicker"><a href="index.html">{html_module.escape(book["english_title"])}</a></p>
    <p class="news-chapter-position"><span>{html_module.escape(chapter["method"])}</span><span>Chapter {chapter["number"]:02d} of {book["total_chapters"]:02d}</span></p>
  </div>
  <div class="news-chapter-title-row">
    <div class="news-chapter-title-copy">
      <p class="text-phi-title" lang="art-x-phi">{html_module.escape(book["phi_title"])}</p>
      <h1 class="news-chapter-title{title_class}">{html_module.escape(chapter["title"])}</h1>
    </div>
    {texts_motif(book["motif"])}
  </div>
  <div class="text-title-tengwar" aria-hidden="true">{tengwar_title}</div>
</header>""".strip()
    body = body[:heading.start()] + header + body[heading.end():]

    opening = re.search(
        r"(</header>)\s*((?:<p>.*?</p>\s*)+)<hr>",
        body,
        flags=re.S,
    )
    if opening is None:
        raise ValueError(f"News from Nowhere chapter opening differs: {repo_path}")
    opening_paragraphs = re.findall(
        r"<p>(.*?)</p>",
        opening.group(2),
        flags=re.S,
    )
    opening_paragraphs = [
        (
            emphasized.group(1)
            if (
                emphasized := re.fullmatch(
                    r"<em>(.*?)</em>",
                    paragraph,
                    flags=re.S,
                )
            )
            else re.sub(r"</?em>", "", paragraph)
        )
        for paragraph in opening_paragraphs
    ]
    if len(opening_paragraphs) != chapter["opening_paragraphs"]:
        raise ValueError(
            f"News from Nowhere opening paragraph count differs in {repo_path}: "
            f"expected {chapter['opening_paragraphs']}, "
            f"found {len(opening_paragraphs)}"
        )
    reader_notes = "".join(
        f'<p class="text-reader-note">{paragraph}</p>'
        for paragraph in opening_paragraphs[1:]
    )
    rendered_opening = (
        f"{opening.group(1)}"
        '<section class="news-chapter-opening">'
        '<div class="news-chapter-intro-copy">'
        f'<p class="text-work-lede">{opening_paragraphs[0]}</p>'
        f'<div class="text-reader-notes">{reader_notes}</div>'
        "</div>"
        f"{news_chapter_map(chapter)}"
        "</section>"
    )
    body = body[:opening.start()] + rendered_opening + body[opening.end():]

    section_specs = [
        {
            "kind": "movement",
            "level": movement["level"],
            "title": movement["title"],
            "marker": news_movement_heading(movement, index),
        }
        for index, movement in enumerate(chapter["movements"], 1)
    ]
    section_specs.append(
        {
            "kind": "apparatus",
            "level": 2,
            "title": chapter["apparatus"],
            "marker": text_method_heading(
                chapter["apparatus"],
                "apparatus",
                "news",
            ),
        }
    )
    for section in section_specs:
        original = (
            f'<h{section["level"]}>'
            f'{html_module.escape(section["title"], quote=False)}'
            f'</h{section["level"]}>'
        )
        if body.count(original) != 1:
            raise ValueError(
                f"News from Nowhere section heading differs in {repo_path}: "
                f"{section['title']}"
            )
        body = body.replace(original, section["marker"])

    if body.count("<hr>") != chapter["inner_dividers"]:
        raise ValueError(
            f"News from Nowhere divider count differs in {repo_path}: "
            f"expected {chapter['inner_dividers']}, found {body.count('<hr>')}"
        )
    positions = [body.index(section["marker"]) for section in section_specs]
    prefix = body[:positions[0]]
    rendered_sections = []
    removed_dividers = 0
    for index, section_spec in enumerate(section_specs):
        end = positions[index + 1] if index + 1 < len(positions) else len(body)
        section = body[positions[index]:end]
        section, removed = re.subn(r"\s*<hr>\s*$", "", section)
        removed_dividers += removed
        if section_spec["kind"] == "movement":
            level_class = f'news-movement-level-{section_spec["level"]}'
            rendered_sections.append(
                f'<section class="news-movement {level_class}">{section}</section>'
            )
        else:
            rendered_sections.append(
                f'<section class="text-apparatus news-apparatus">{section}</section>'
            )
    body = prefix + "".join(rendered_sections)
    if removed_dividers != chapter["inner_dividers"] or "<hr>" in body:
        raise ValueError(f"News from Nowhere left an untreated divider in {repo_path}")

    fence_treatment = {
        "interlinear_blocks": chapter["interlinear_blocks"],
        "interlinear_stanzas": chapter["interlinear_stanzas"],
        "source_free_blocks": 0,
        "source_free_stanzas": 0,
        "complete_readings": 0,
    }
    body = style_text_fences(body, repo_path, fence_treatment)
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
    if note_count != chapter["notes"]:
        raise ValueError(
            f"News from Nowhere note count differs in {repo_path}: "
            f"expected {chapter['notes']}, found {note_count}"
        )
    body = style_text_tables(body, repo_path, chapter)
    body = body.replace(r"\<code>", "<code>").replace(r"\</code>", "</code>")
    return mark_text_inline_phi(body)


def news_book_index(readme_source, book):
    """Build the book's landing page from its README and strict chapter data."""
    body = md_to_html(readme_source)
    body = re.sub(
        r'href="(chapter_[0-9]+)\.md"',
        r'href="\1.html"',
        body,
    )
    body = body.replace(
        'href="source.txt"',
        'href="https://github.com/dcellison/phi/blob/main/texts/news_from_nowhere/source.txt"',
    )
    match = re.fullmatch(
        r"<h1><em>(.*?)</em></h1>\s*"
        r"<p>(.*?)</p>\s*"
        r"<h2>Chapters</h2>\s*"
        r"<table>(.*?)</table>",
        body.strip(),
        flags=re.S,
    )
    if match is None or html_module.unescape(match.group(1)) != book["english_title"]:
        raise ValueError("News from Nowhere README structure differs")
    rows = re.findall(r"<tr>(.*?)</tr>", match.group(3), flags=re.S)
    if not rows:
        raise ValueError("News from Nowhere README has no chapter table")
    headers = re.findall(r"<th>(.*?)</th>", rows[0], flags=re.S)
    if headers != ["Chapter", "Title", "Text"]:
        raise ValueError("News from Nowhere README chapter headers differ")
    if len(rows) - 1 != len(book["chapters"]):
        raise ValueError("News from Nowhere README chapter count differs")
    for row, chapter in zip(rows[1:], book["chapters"]):
        cells = re.findall(r"<td>(.*?)</td>", row, flags=re.S)
        expected_link = (
            f'<a href="{Path(chapter["file"]).stem}.html">'
            f'Read chapter {chapter["number"]}</a>'
        )
        if cells != [
            str(chapter["number"]),
            chapter["title"],
            expected_link,
        ]:
            raise ValueError(
                f'News from Nowhere README row differs: {chapter["file"]}'
            )

    tengwar_title = tengwar.render_line(book["phi_title"])
    if tengwar_title is None:
        raise ValueError("News from Nowhere title cannot render in Tengwar")
    available = len(book["chapters"])
    chapter_rows = []
    for chapter in book["chapters"]:
        movement_noun = "movement" if len(chapter["movements"]) == 1 else "movements"
        passage_noun = (
            "passage" if chapter["interlinear_stanzas"] == 1 else "passages"
        )
        chapter_rows.append(
            '<li class="news-book-chapter">'
            f'<a href="{Path(chapter["file"]).stem}.html">'
            f'<span class="news-book-chapter-number">'
            f'{chapter["number"]:02d}</span>'
            '<div class="news-book-chapter-copy">'
            f'<p class="news-book-chapter-label">Chapter '
            f'{chapter["number"]:02d}</p>'
            f'<h3>{html_module.escape(chapter["title"])}</h3>'
            f'<p class="news-book-chapter-summary">'
            f'{html_module.escape(chapter["summary"])}</p>'
            "</div>"
            '<div class="news-book-chapter-meta">'
            f'<p>{len(chapter["movements"]):02d} {movement_noun}</p>'
            f'<p>{chapter["interlinear_stanzas"]:03d} {passage_noun}</p>'
            "</div>"
            f"{news_link_arrow()}"
            "</a></li>"
        )
    return (
        '<header class="news-book-header">'
        '<div class="news-book-meta">'
        '<p class="text-shelf-label">Phi texts</p>'
        '<p class="news-book-method">Work in progress</p>'
        "</div>"
        '<div class="news-book-title-row">'
        '<div class="news-book-title-copy">'
        f'<p class="text-phi-title" lang="art-x-phi">'
        f'{html_module.escape(book["phi_title"])}</p>'
        f'<h1>{html_module.escape(book["english_title"])}</h1>'
        '<p class="news-book-author">William Morris</p>'
        "</div>"
        f'{texts_motif(book["motif"])}'
        "</div>"
        f'<div class="text-title-tengwar" aria-hidden="true">{tengwar_title}</div>'
        "</header>"
        '<section class="news-book-opening" data-reader-home>'
        f'<p class="news-book-lede">{match.group(2)}</p>'
        "</section>"
        '<section class="news-book-status" aria-labelledby="news-book-status-heading">'
        '<div class="news-book-status-copy">'
        '<p class="news-book-status-label" id="news-book-status-heading">'
        "Book in progress</p>"
        f'<p class="news-book-status-count"><strong>{available:02d}</strong> '
        f'<span>of {book["total_chapters"]:02d} chapters</span></p>'
        "</div>"
        f'<progress max="{book["total_chapters"]}" value="{available}">'
        f'{available} of {book["total_chapters"]} chapters</progress>'
        "</section>"
        '<section class="news-book-catalogue" '
        'aria-labelledby="news-book-catalogue-heading">'
        '<header class="news-book-section-heading">'
        '<p class="news-book-section-label">Reading sequence</p>'
        '<h2 id="news-book-catalogue-heading">Chapters available</h2>'
        "</header>"
        f'<ol class="news-book-chapter-list">{"".join(chapter_rows)}</ol>'
        "</section>"
    )


NEWS_SRC = ROOT / "texts" / NEWS_WORK["path"]
NEWS_OUT = TEXTS_OUT / NEWS_WORK["path"]
prepare_html_output(NEWS_OUT)
news_chapters = [
    NEWS_SRC / chapter["file"]
    for chapter in NEWS_EDITORIAL["chapters"]
]
for chapter_index, (chapter_path, chapter) in enumerate(
    zip(news_chapters, NEWS_EDITORIAL["chapters"])
):
    chapter_source = chapter_path.read_text(encoding="utf-8")
    rendered = apply_news_chapter_editorial(
        md_to_html(chapter_source),
        chapter_source,
        chapter,
        NEWS_EDITORIAL,
    )
    chapter_nav = news_chapter_nav(NEWS_EDITORIAL["chapters"], chapter_index)
    page_title = (
        f'{NEWS_EDITORIAL["english_title"]}, chapter '
        f'{chapter["number"]}: {chapter["title"]}'
    )
    (NEWS_OUT / f"{chapter_path.stem}.html").write_text(
        texts_page(
            rendered,
            page_title,
            depth=2,
            footer_nav=chapter_nav,
            editorial_kind="news-chapter",
            editorial_motif=NEWS_EDITORIAL["motif"],
        )
    )

news_index = news_book_index(
    (NEWS_SRC / "README.md").read_text(encoding="utf-8"),
    NEWS_EDITORIAL,
)
news_index_nav = (
    '<nav class="chapnav news-book-footer-nav" aria-label="Text navigation">'
    '<a href="../index.html">All texts</a></nav>'
)
(NEWS_OUT / "index.html").write_text(
    texts_page(
        news_index,
        NEWS_EDITORIAL["english_title"],
        depth=2,
        footer_nav=news_index_nav,
        editorial_kind="news-book",
        editorial_motif=NEWS_EDITORIAL["motif"],
    )
)

TEXT_CONTENTS_METHODS = (
    {
        "method": "Translation",
        "label": "Translation",
        "kind": "translation",
        "icon": "translation",
        "description": (
            "Translation answers to the source's claims and distinctions. "
            "It shows what Phi can carry when the source sets the terms."
        ),
    },
    {
        "method": "Refusal",
        "label": "Refusal",
        "kind": "refusal",
        "icon": "refusal",
        "description": (
            "A refusal answers a source without claiming to translate it. "
            "The source remains visible beside Phi's answer."
        ),
    },
    {
        "method": "Original",
        "label": "Original work",
        "kind": "original",
        "icon": "dialogue",
        "description": (
            "Original work begins in Phi. English follows as a close reading "
            "rather than governing the sentence."
        ),
    },
)


def split_catalogued_text_title(work):
    """Separate and verify the Phi and English parts of a catalogue title."""
    repo_path = text_repo_path(work)
    treatment = TEXT_EDITORIAL_PAGES.get(repo_path)
    if treatment is not None:
        return split_text_editorial_title(
            work["title"],
            treatment["phi_title"],
            repo_path,
        )
    for separator in (" — ", ": "):
        if separator not in work["title"]:
            continue
        phi_title, english_title = work["title"].split(separator, 1)
        if is_current_phi(phi_title) and english_title.strip():
            return phi_title, english_title
    raise ValueError(f"text catalogue title has no verified Phi opening: {repo_path}")


def text_contents_title(work):
    """Split one catalogue title into its romanized Phi and English halves."""
    return split_catalogued_text_title(work)


def text_contents_arrow():
    """Return the decorative Lucide arrow used at the end of a work link."""
    return (
        '<span class="text-index-arrow" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" focusable="false">'
        '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'
        "</svg></span>"
    )


def text_collection_index(readme_source, collection, works):
    """Build one author-collection landing page from its README and catalogue."""
    collection_path = collection["path"]
    collection_method = {
        "Translation": "Translations",
        "Refusal": "Refusals",
        "Original": "Original Phi works",
    }[collection["method"]]
    body = md_to_html(readme_source)
    body = re.sub(
        r'href="([a-z0-9_]+)\.md"',
        r'href="\1.html"',
        body,
    )
    body = re.sub(
        r'href="sources/([^"]+)"',
        (
            'href="https://github.com/dcellison/phi/blob/main/'
            f'texts/{collection_path}/sources/\\1"'
        ),
        body,
    )
    match = re.fullmatch(
        r"<h1><em>(.*?)</em></h1>\s*"
        r"<p>(.*?)</p>\s*"
        r"<h2>Selections</h2>\s*"
        r"<table>(.*?)</table>",
        body.strip(),
        flags=re.S,
    )
    phi_title, english_title = text_contents_title(collection)
    if (
        match is None
        or html_module.unescape(match.group(1)) != english_title
    ):
        raise ValueError(
            f"text collection README structure differs: {collection_path}"
        )
    lede = mark_text_inline_phi(f"<p>{match.group(2)}</p>")
    lede_match = re.fullmatch(r"<p>(.*?)</p>", lede, flags=re.S)
    if lede_match is None:
        raise ValueError(
            f"text collection README lede differs: {collection_path}"
        )
    rows = re.findall(r"<tr>(.*?)</tr>", match.group(3), flags=re.S)
    if not rows:
        raise ValueError(
            f"text collection README has no work table: {collection_path}"
        )
    headers = re.findall(r"<th>(.*?)</th>", rows[0], flags=re.S)
    if headers != ["Selection", "Source", "Method", "Text"]:
        raise ValueError(
            f"text collection README headers differ: {collection_path}"
        )
    if len(rows) - 1 != len(works):
        raise ValueError(
            f"text collection README work count differs: {collection_path}"
        )
    for row, work in zip(rows[1:], works):
        cells = re.findall(r"<td>(.*?)</td>", row, flags=re.S)
        _, work_english = text_contents_title(work)
        if len(cells) != 4:
            raise ValueError(
                f"text collection README row differs: {text_repo_path(work)}"
            )
        link = re.fullmatch(
            rf'<a href="{re.escape(Path(work["path"]).stem)}\.html">'
            r"[^<]+</a>",
            cells[3],
        )
        if (
            cells[0] != html_module.escape(work_english, quote=False)
            or cells[1] != html_module.escape(work["source"], quote=False)
            or cells[2] != html_module.escape(work["method"], quote=False)
            or link is None
        ):
            raise ValueError(
                f"text collection README row differs: {text_repo_path(work)}"
            )

    tengwar_title = tengwar.render_line(phi_title)
    if tengwar_title is None:
        raise ValueError(
            f"text collection title cannot render in Tengwar: {collection_path}"
        )
    work_rows = []
    for index, work in enumerate(works, 1):
        work_phi, work_english = text_contents_title(work)
        work_rows.append(
            '<li class="news-book-chapter author-collection-work">'
            f'<a href="{Path(work["path"]).stem}.html">'
            f'<span class="news-book-chapter-number">{index:02d}</span>'
            '<div class="news-book-chapter-copy">'
            f'<p class="news-book-chapter-label">Selection {index:02d}</p>'
            f'<p class="author-collection-work-phi" lang="art-x-phi">'
            f"{html_module.escape(work_phi)}</p>"
            f"<h3>{html_module.escape(work_english)}</h3>"
            f'<p class="news-book-chapter-summary">'
            f'{html_module.escape(work["summary"])}</p>'
            "</div>"
            '<div class="news-book-chapter-meta">'
            f'<p>{html_module.escape(work["source"])}</p>'
            f'<p>{html_module.escape(work["method"])}</p>'
            "</div>"
            f"{news_link_arrow()}"
            "</a></li>"
        )
    work_noun = "selection" if len(works) == 1 else "selections"
    return (
        '<header class="news-book-header author-collection-header">'
        '<div class="news-book-meta">'
        '<p class="text-shelf-label">Phi texts</p>'
        '<p class="news-book-method">Author collection</p>'
        "</div>"
        '<div class="news-book-title-row">'
        '<div class="news-book-title-copy">'
        f'<p class="text-phi-title" lang="art-x-phi">'
        f"{html_module.escape(phi_title)}</p>"
        f"<h1>{html_module.escape(english_title)}</h1>"
        f'<p class="news-book-author">{collection_method}</p>'
        "</div>"
        f'{texts_motif("words_seed")}'
        "</div>"
        f'<div class="text-title-tengwar" aria-hidden="true">{tengwar_title}</div>'
        "</header>"
        '<section class="news-book-opening author-collection-opening" '
        'data-reader-home>'
        f'<p class="news-book-lede">{lede_match.group(1)}</p>'
        "</section>"
        '<section class="news-book-catalogue author-collection-catalogue" '
        'aria-labelledby="author-collection-catalogue-heading">'
        '<header class="news-book-section-heading">'
        '<p class="news-book-section-label">By source work</p>'
        '<h2 id="author-collection-catalogue-heading">Selections available</h2>'
        f'<p class="author-collection-count">{len(works):02d} {work_noun}</p>'
        "</header>"
        f'<ol class="news-book-chapter-list">{"".join(work_rows)}</ol>'
        "</section>"
    )


for collection in COLLECTIONS:
    collection_path = collection["path"]
    collection_source = ROOT / "texts" / collection_path
    collection_output = TEXTS_OUT / collection_path
    prepare_html_output(collection_output)
    collection_works = COLLECTION_TEXTS_BY_PATH[collection_path]
    _, collection_english = text_contents_title(collection)
    for work_index, work in enumerate(collection_works):
        source = collection_source / work["path"]
        md = source.read_text(encoding="utf-8")
        repo_path = text_repo_path(work)
        treatment = TEXT_EDITORIAL_PAGES.get(repo_path)
        if treatment is None:
            raise ValueError(
                f"collection work has no editorial treatment: {repo_path}"
            )
        rendered = apply_text_editorial(
            md_to_html(md),
            md,
            repo_path,
            treatment,
        )
        footer_nav = text_work_nav(
            collection_works,
            work_index,
            f"{collection_english} contents",
            "selection",
        )
        (collection_output / f"{source.stem}.html").write_text(
            texts_page(
                rendered,
                work["title"],
                depth=2,
                footer_nav=footer_nav,
                editorial_kind=treatment["form"],
                editorial_motif=treatment["motif"],
            )
        )
    collection_index = text_collection_index(
        (collection_source / "README.md").read_text(encoding="utf-8"),
        collection,
        collection_works,
    )
    collection_footer = (
        '<nav class="chapnav news-book-footer-nav" '
        'aria-label="Text navigation">'
        '<a href="../index.html">All texts</a></nav>'
    )
    (collection_output / "index.html").write_text(
        texts_page(
            collection_index,
            collection_english,
            depth=2,
            footer_nav=collection_footer,
            editorial_kind="author-collection",
            editorial_motif="words_seed",
        )
    )


def text_contents_page(news_chapter_count):
    """Build the catalogue-driven entrance to the literary shelf."""
    expected_editorial = {
        text_repo_path(work)
        for work in [*TEXTS, *COLLECTION_TEXTS]
    }
    if set(TEXT_EDITORIAL_PAGES) != expected_editorial:
        raise ValueError(
            "texts contents require one editorial treatment for every short work"
        )
    method_specs = {
        spec["method"]: spec
        for spec in TEXT_CONTENTS_METHODS
    }
    all_works = [*TEXTS, *COLLECTION_TEXTS, NEWS_WORK]
    if any(
        work["method"] not in method_specs
        for work in [*TEXTS, *COLLECTION_TEXTS]
    ):
        raise ValueError("texts contents contain an unknown catalogue method")

    method_key = []
    for spec in TEXT_CONTENTS_METHODS:
        count = sum(work["method"] == spec["method"] for work in all_works)
        if count == 0:
            continue
        noun = "work" if count == 1 else "works"
        method_key.append(
            f'<article class="text-index-method text-index-method-{spec["kind"]}">'
            "<header>"
            f'{text_section_icon(spec["icon"])}'
            "<div>"
            f'<h3>{html_module.escape(spec["label"])}</h3>'
            f'<p class="text-index-method-count">{count:02d} {noun}</p>'
            "</div>"
            "</header>"
            f'<p>{html_module.escape(spec["description"])}</p>'
            "</article>"
        )

    work_rows = []
    for index, work in enumerate(TEXTS, 1):
        spec = method_specs[work["method"]]
        phi_title, english_title = text_contents_title(work)
        href = f"{Path(work['path']).stem}.html"
        work_rows.append(
            f'<li class="text-index-entry text-index-entry-{spec["kind"]}">'
            f'<a href="{href}">'
            f'<span class="text-index-number">{index:02d}</span>'
            '<div class="text-index-copy">'
            f'<p class="text-index-phi-title" lang="art-x-phi">'
            f"{html_module.escape(phi_title)}</p>"
            f'<h3>{html_module.escape(english_title)}</h3>'
            f'<p class="text-index-summary">{html_module.escape(work["summary"])}</p>'
            "</div>"
            '<div class="text-index-entry-meta">'
            f'<p class="text-index-entry-method">{html_module.escape(spec["label"])}</p>'
            "</div>"
            f"{text_contents_arrow()}"
            "</a></li>"
        )

    collection_rows = []
    for collection in COLLECTIONS:
        phi_title, english_title = text_contents_title(collection)
        available = len(COLLECTION_TEXTS_BY_PATH[collection["path"]])
        work_noun = "selection" if available == 1 else "selections"
        collection_rows.append(
            '<li class="text-index-collection">'
            f'<a href="{collection["path"]}/index.html">'
            '<span class="text-index-book-mark" aria-hidden="true">'
            f'{text_section_icon("collection_detail")}</span>'
            '<div class="text-index-copy">'
            f'<p class="text-index-phi-title" lang="art-x-phi">'
            f"{html_module.escape(phi_title)}</p>"
            f"<h3>{html_module.escape(english_title)}</h3>"
            f'<p class="text-index-summary">'
            f'{html_module.escape(collection["summary"])}</p>'
            "</div>"
            '<div class="text-index-entry-meta">'
            '<p class="text-index-entry-method">Author collection</p>'
            f'<p class="text-index-book-progress">{available:02d} '
            f"{work_noun} available</p>"
            "</div>"
            f"{text_contents_arrow()}"
            "</a></li>"
        )
    collection_noun = "collection" if len(COLLECTIONS) == 1 else "collections"
    collection_section = (
        '<section class="text-index-collections" '
        'aria-labelledby="text-index-collections-heading">'
        '<header class="text-index-section-heading">'
        "<div>"
        '<p class="text-index-section-label">Grouped by writer</p>'
        '<h2 id="text-index-collections-heading">Author collections</h2>'
        "</div>"
        f'<p class="text-index-section-count">{len(COLLECTIONS):02d} '
        f"{collection_noun}</p>"
        "</header>"
        f'<ol class="text-index-collection-list">{"".join(collection_rows)}</ol>'
        "</section>"
    )

    news_phi, news_english = text_contents_title(NEWS_WORK)
    chapter_noun = "chapter" if news_chapter_count == 1 else "chapters"
    book_entry = (
        '<section class="text-index-book" aria-labelledby="text-index-book-heading">'
        '<header class="text-index-section-heading">'
        '<div>'
        '<p class="text-index-section-label">Book in progress</p>'
        '<h2 id="text-index-book-heading">Book-length work</h2>'
        "</div>"
        '<p class="text-index-section-count">01 work</p>'
        "</header>"
        f'<a href="{NEWS_WORK["path"]}/index.html">'
        '<span class="text-index-book-mark" aria-hidden="true">'
        f'{text_section_icon("complete")}</span>'
        '<div class="text-index-copy">'
        f'<p class="text-index-phi-title" lang="art-x-phi">'
        f"{html_module.escape(news_phi)}</p>"
        f"<h3>{html_module.escape(news_english)}</h3>"
        f'<p class="text-index-summary">'
        f'{html_module.escape(NEWS_WORK["summary"])}</p>'
        "</div>"
        '<div class="text-index-entry-meta">'
        '<p class="text-index-entry-method">Book in progress</p>'
        f'<p class="text-index-book-progress">{news_chapter_count:02d} '
        f"{chapter_noun} available</p>"
        "</div>"
        f"{text_contents_arrow()}"
        "</a></section>"
    )

    return (
        '<header class="text-index-header">'
        '<div class="text-work-meta">'
        '<p class="text-shelf-label">Phi texts</p>'
        f'<p class="text-index-count">{len(all_works):02d} works</p>'
        "</div>"
        '<div class="text-index-title-row">'
        "<h1>The texts</h1>"
        '<p class="text-index-lede">This shelf holds work written in Phi and '
        "work brought into it. Each page says what it owes to a source. A "
        "translation carries its source, original work begins in Phi, and a "
        "refusal answers a source without calling itself a translation.</p>"
        f'{texts_motif("words_seed")}'
        "</div>"
        "</header>"
        '<section class="text-index-methods" '
        'aria-labelledby="text-index-methods-heading">'
        '<h2 id="text-index-methods-heading">How the shelf relates to sources</h2>'
        f'<div class="text-index-method-grid">{"".join(method_key)}</div>'
        "</section>"
        '<section class="text-index-catalogue" '
        'aria-labelledby="text-index-catalogue-heading">'
        '<header class="text-index-section-heading">'
        "<div>"
        '<p class="text-index-section-label">Catalogue order</p>'
        '<h2 id="text-index-catalogue-heading">Short works</h2>'
        "</div>"
        f'<p class="text-index-section-count">{len(TEXTS):02d} works</p>'
        "</header>"
        f'<ol class="text-index-list">{"".join(work_rows)}</ol>'
        "</section>"
        f"{collection_section}"
        f"{book_entry}"
    )


(TEXTS_OUT / "index.html").write_text(
    texts_page(
        text_contents_page(len(news_chapters)),
        "contents",
        footer_nav="",
        editorial_kind="contents",
    )
)
print(
    "wrote build/site/texts/: "
    f"{len(TEXTS) + len(COLLECTION_TEXTS) + len(BOOKS)} works, "
    f"{len(COLLECTIONS)} author collection, "
    f"{len(news_chapters)} News from Nowhere chapters + contents"
)

# ---- the pamphlets: deep-dive companions rendered to build/site/pamphlets/ ----
PAMPH_OUT = BUILD_SITE / "pamphlets"
prepare_html_output(PAMPH_OUT)
NAV_PAMPH = '<nav class="topnav"><a href="../index.html">kia</a> <span class="sep">&middot;</span> <a href="../short_road.html">walk</a> <span class="sep">&middot;</span> <a href="../primer/index.html">primer</a> <span class="sep">&middot;</span> <a href="../book/index.html">book</a> <span class="sep">&middot;</span> <a href="../manual/index.html">manual</a> <span class="sep">&middot;</span> <a class="here" href="index.html">pamphlets</a> <span class="sep">&middot;</span> <a href="../texts/index.html">texts</a> <span class="sep">&middot;</span> <a href="../explore.html">lexicon</a> <button class="themetoggle" aria-label="toggle light and dark" title="light / dark">&#9681;</button></nav>'


def pamphlet_ordered_list_starts(source):
    """Return the first number of each Markdown ordered-list block."""
    starts = []
    in_fence = False
    in_list = False
    previous_blank = True
    for line in source.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            in_list = False
            previous_blank = False
            continue
        match = None if in_fence else re.match(r"^(\d+)\. ", line)
        if match is not None and (in_list or previous_blank):
            if not in_list:
                starts.append(int(match.group(1)))
            in_list = True
        else:
            in_list = False
        previous_blank = not line.strip()
    return starts


def pamphlet_structural_signature(source):
    """Pin workbook structure and visible exercise numbering."""
    starts = pamphlet_ordered_list_starts(source)
    return (
        manual_structural_signature(source)
        + ";s"
        + (",".join(map(str, starts)) if starts else "-")
    )


def pamphlet_default_section_level(variant):
    """Choose the section level used by the compact workbook sources."""
    if variant in {"opening", "reference", "examples"}:
        return 0
    if variant in {"exercises", "answers"}:
        return 2
    return 3


def load_pamphlet_editorial():
    """Load opt-in pamphlet treatments and verify complete workbook coverage."""
    config_path = SITE_SRC / "pamphlet_editorial.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if set(config) != {"complete_pamphlets", "pamphlets", "pages"}:
        raise ValueError(
            "site/pamphlet_editorial.json requires complete_pamphlets, "
            "pamphlets, and pages"
        )
    complete = config["complete_pamphlets"]
    pamphlets = config["pamphlets"]
    pages = config["pages"]
    if (
        not isinstance(complete, list)
        or len(complete) != len(set(complete))
        or not isinstance(pamphlets, dict)
        or set(pamphlets) != set(complete)
        or not isinstance(pages, dict)
        or not pages
    ):
        raise ValueError("pamphlet editorial coverage must be complete and unique")

    catalogue_directories = {
        pamphlet["directory"] for pamphlet in PAMPHLET_CATALOGUE
    }
    if not set(complete) <= catalogue_directories:
        raise ValueError("pamphlet editorial coverage names an unknown pamphlet")
    for directory, metadata in pamphlets.items():
        if (
            not re.fullmatch(r"[a-z0-9_]+", directory)
            or not isinstance(metadata, dict)
            or set(metadata) != {"motif"}
            or metadata["motif"]
            not in {
                "ordered_slots",
                "clause_links",
                "event_views",
                "source_routes",
                "participant_reference",
                "noun_phrase",
                "name_designation",
                "source_beside",
                "audible_boundaries",
                "written_hands",
                "ternary_scale",
            }
        ):
            raise ValueError(
                f"invalid pamphlet editorial metadata: {directory}"
            )

    expected_paths = {
        path.relative_to(ROOT).as_posix()
        for directory in complete
        for path in sorted((ROOT / "pamphlets" / directory).glob("*.md"))
    }
    if set(pages) != expected_paths:
        raise ValueError(
            "pamphlet editorial pages differ from complete coverage: "
            + ", ".join(sorted(set(pages) ^ expected_paths))
        )
    allowed_variants = {
        "opening",
        "lesson",
        "stack",
        "tables",
        "scenario",
        "errors",
        "exercises",
        "answers",
        "appendix",
        "reference",
        "examples",
    }
    for repo_path, treatment in pages.items():
        path = ROOT / repo_path
        source = path.read_text(encoding="utf-8") if path.is_file() else ""
        treatment_fields = set(treatment) if isinstance(treatment, dict) else set()
        default_section_level = (
            pamphlet_default_section_level(treatment.get("variant"))
            if isinstance(treatment, dict)
            else None
        )
        section_level = (
            treatment.get("section_level", default_section_level)
            if isinstance(treatment, dict)
            else None
        )
        if (
            not path.is_file()
            or not isinstance(treatment, dict)
            or treatment_fields
            not in (
                {"shape", "variant"},
                {"section_level", "shape", "variant"},
            )
            or treatment["variant"] not in allowed_variants
            or section_level
            not in (
                {0}
                if treatment["variant"] in {"opening", "reference"}
                else {0, 2, 3}
            )
            or (
                section_level == 0
                and treatment["variant"] != "opening"
                and re.search(r"^#{2,6} ", source, flags=re.M)
            )
            or treatment["shape"]
            != pamphlet_structural_signature(source)
        ):
            raise ValueError(
                f"invalid pamphlet editorial treatment: {repo_path}"
            )
    for directory in complete:
        directory_pages = sorted(
            repo_path
            for repo_path in pages
            if Path(repo_path).parts[1] == directory
        )
        if (
            not directory_pages
            or Path(directory_pages[0]).name != "00_title.md"
            or pages[directory_pages[0]]["variant"] != "opening"
            or sum(
                treatment["variant"] == "opening"
                for repo_path, treatment in pages.items()
                if Path(repo_path).parts[1] == directory
            )
            != 1
        ):
            raise ValueError(
                f"pamphlet editorial opening is invalid: {directory}"
            )
    return pamphlets, pages


def pamphlet_motif(name):
    """Return the CSS-painted Lucide motif anchor for a workbook."""
    if name not in {
        "ordered_slots",
        "clause_links",
        "event_views",
        "source_routes",
        "participant_reference",
        "noun_phrase",
        "name_designation",
        "source_beside",
        "audible_boundaries",
        "written_hands",
        "ternary_scale",
    }:
        raise ValueError(f"unknown pamphlet motif: {name}")
    return '<div class="pamphlet-page-motif" aria-hidden="true"></div>'


def pamphlet_display_title(title, index):
    """Separate a workbook page's small label from its display title."""
    if index == 0:
        return "Workbook", title
    part_match = re.fullmatch(r"Part (\d+): (.+)", title)
    if part_match is not None:
        if int(part_match.group(1)) != index:
            raise ValueError(f"pamphlet part number differs from order: {title}")
        return f"Part {index}", part_match.group(2)
    appendix_match = re.fullmatch(r"Appendix: (.+)", title)
    if appendix_match is not None:
        return "Appendix", appendix_match.group(1)
    return f"Part {index}", title


def pamphlet_contents_label(title, index):
    """Return the source contents wording expected for a workbook page."""
    if index == 0:
        return title
    part_match = re.fullmatch(r"Part \d+: (.+)", title)
    if part_match is not None:
        label = part_match.group(1)
        parenthetical_particle = re.fullmatch(r"(.+) \(([a-z]+)\)", label)
        if parenthetical_particle is not None:
            return (
                f"{parenthetical_particle.group(1)}: "
                f"{parenthetical_particle.group(2)}"
            )
        return label
    if title.startswith("Appendix: "):
        return title
    return title


def pamphlet_reading_rail(directory, paths, titles, current):
    """Give every workbook page a compact route to every other page."""
    links = []
    for index, (path, title) in enumerate(zip(paths, titles)):
        label, display_title = pamphlet_display_title(title, index)
        accessible_title = (
            f"{label}: {display_title}" if label != "Workbook" else display_title
        )
        current_attributes = (
            ' class="current" aria-current="page"' if index == current else ""
        )
        href = f"{directory}__{path.stem}.html"
        accessible_label = (
            f"Page {index + 1} of {len(paths)}: {accessible_title}"
        )
        links.append(
            f'<a href="{href}"{current_attributes} '
            f'data-page="{index:02d}" '
            f'aria-label="{html_module.escape(accessible_label, quote=True)}" '
            f'title="{html_module.escape(accessible_title, quote=True)}"></a>'
        )
    return (
        '<nav class="pamphlet-reading-rail pager" '
        'aria-label="Workbook pages">'
        + "".join(links)
        + "</nav>"
    )


def validate_pamphlet_reader_fallback(header, rail, title, page_count):
    """Keep decorative and compact UI out of simplified article text."""
    if "<svg" in header.lower():
        raise ValueError("pamphlet header contains extractable decorative SVG")
    rail_text = html_module.unescape(
        re.sub(r"<[^>]+>", "", rail)
    ).strip()
    labels = re.findall(
        r'<a [^>]*aria-label="Page \d+ of \d+: [^"]+"',
        rail,
    )
    if rail_text or len(labels) != page_count:
        raise ValueError(
            "pamphlet rail is not safe for simplified reading mode"
        )
    meta_match = re.search(
        r'<div class="pamphlet-header-meta"><p>(.*?)</p>',
        header,
        flags=re.S,
    )
    if meta_match is None:
        raise ValueError("pamphlet header metadata is missing")
    meta_text = html_module.unescape(
        re.sub(r"<[^>]+>", "", meta_match.group(1))
    )
    meta_text = " ".join(meta_text.split())
    if meta_text != f"Phi practice \N{MIDDLE DOT} {title}":
        raise ValueError("pamphlet header metadata needs literal separators")


def mark_pamphlet_inline_phi(body):
    """Mark current Phi in prose, lists, and table cells."""
    def mark_container(match):
        return re.sub(
            r"<code>([^<]+)</code>",
            lambda code: (
                '<code class="phi-inline" lang="art-x-phi">'
                f"{code.group(1)}</code>"
                if is_current_phi(code.group(1))
                else code.group(0)
            ),
            match.group(0),
        )

    return re.sub(
        r"<(?:p|li|td)(?: [^>]*)?>.*?</(?:p|li|td)>",
        mark_container,
        body,
        flags=re.S,
    )


def style_pamphlet_tables(body, title):
    """Use the responsive reference-table machinery with workbook classes."""
    return rename_manual_editorial_classes(style_manual_tables(body, title))


def style_pamphlet_examples(body):
    """Use the interlinear parser with workbook-specific presentation."""
    return rename_manual_editorial_classes(style_manual_examples(body))


def style_pamphlet_ternary_drills(body, title):
    """Turn bare numeral drills into readable correspondence and recital grids."""
    pair_count = 0
    recital_count = 0

    def style_block(match):
        nonlocal pair_count, recital_count
        block = match.group(1)
        lines = [line for line in block.splitlines() if line.strip()]
        pairs = [
            re.fullmatch(r"(.+?)\s{2,}\N{EM DASH}\s+(\d+)", line)
            for line in lines
        ]
        if lines and all(pair is not None for pair in pairs):
            if not all(is_current_phi(pair.group(1)) for pair in pairs):
                raise ValueError(
                    f"ternary correspondence drill contains non-Phi: {title}"
                )
            pair_count += 1
            rows = "".join(
                "<div>"
                f'<dt><code lang="art-x-phi">{pair.group(1)}</code></dt>'
                f"<dd>{pair.group(2)}</dd>"
                "</div>"
                for pair in pairs
            )
            return (
                '<dl class="pamphlet-number-drill" '
                'aria-label="Phi numeral recognition drill">'
                f"{rows}</dl>"
            )
        if len(lines) >= 2 and all(is_current_phi(line) for line in lines):
            recital_count += 1
            entries = "".join(
                f'<code lang="art-x-phi">{line}</code>' for line in lines
            )
            return (
                '<div class="pamphlet-number-recital" role="group" '
                'aria-label="Phi numeral reading drill">'
                f"{entries}</div>"
            )
        return match.group(0)

    body = re.sub(r"<pre>(.*?)</pre>", style_block, body, flags=re.S)
    expected_pairs = 1 if title == "Part 1: Counting in threes" else 0
    expected_recitals = 1 if title == "Part 2: Climbing the scale" else 0
    if pair_count != expected_pairs or recital_count != expected_recitals:
        raise ValueError(
            f"ternary numeral drill count changed: {title} "
            f"({pair_count} correspondences, {recital_count} recitals)"
        )
    return body


def style_pamphlet_ternary_worked_numbers(body, title):
    """Set worked decompositions apart without changing their explanation."""
    body, count = re.subn(
        r"<p><strong>Worked:</strong>\s*(.*?)</p>",
        r'<div class="pamphlet-worked-number">'
        r"<p><span>Worked</span>\1</p></div>",
        body,
        flags=re.S,
    )
    expected = 2 if title == "Part 2: Climbing the scale" else 0
    if count != expected:
        raise ValueError(
            f"ternary worked-example count changed: {title} ({count})"
        )
    return body


def style_pamphlet_ternary_dialogue_examples(body, title):
    """Keep the market's spoken exchange inside the interlinear treatment."""
    count = 0

    def style_block(match):
        nonlocal count
        block = match.group(1)
        groups = [
            group.splitlines()
            for group in re.split(r"\n\s*\n", block.strip())
        ]
        if not any(
            lines and f" {chr(0x2014)} " in lines[0]
            for lines in groups
        ):
            return match.group(0)
        figures = []
        for lines in groups:
            if len(lines) != 3:
                raise ValueError(
                    f"ternary dialogue example has the wrong depth: {title}"
                )
            phi_parts = [
                html_module.unescape(part)
                for part in lines[0].split(f" {chr(0x2014)} ")
            ]
            if not all(is_current_phi_passage(part) for part in phi_parts):
                raise ValueError(
                    f"ternary dialogue example contains non-Phi: {title}"
                )
            dialogue_class = (
                " pamphlet-dialogue-example"
                if len(phi_parts) > 1
                else ""
            )
            figures.append(
                f'<figure class="pamphlet-example{dialogue_class}" '
                'aria-label="Interlinear example">'
                f'<p class="pamphlet-example-phi" lang="art-x-phi">'
                f"{lines[0]}</p>"
                f'<p class="pamphlet-example-gloss">{lines[1]}</p>'
                f"<figcaption>{lines[2]}</figcaption>"
                "</figure>"
            )
        count += 1
        return (
            '<div class="pamphlet-example-set" role="group" '
            'aria-label="Interlinear examples">'
            + "".join(figures)
            + "</div>"
        )

    body = re.sub(r"<pre>(.*?)</pre>", style_block, body, flags=re.S)
    expected = 1 if title == "Part 7: Market day" else 0
    if count != expected:
        raise ValueError(
            f"ternary dialogue-example count changed: {title} ({count})"
        )
    return body


def style_pamphlet_ternary_answer_parts(body, title):
    """Restore inline answer labels as real divisions in the answer key."""
    if title != "Part 9: Exercises":
        return body
    if body.count("<h2>Answer key</h2>") != 1:
        raise ValueError("ternary exercises need one answer key")
    before_key, after_key = body.split("<h2>Answer key</h2>")
    pattern = re.compile(
        r"<p><strong>(Part [A-F](?:, deferred from Part \d+)?)\."
        r"</strong>\s*(.*?)</p>",
        flags=re.S,
    )
    labels = [match.group(1) for match in pattern.finditer(after_key)]
    expected = [
        "Part A",
        "Part B",
        "Part B, deferred from Part 2",
        "Part C",
        "Part C, deferred from Part 3",
        "Part D",
        "Part E",
        "Part E, deferred from Part 4",
        "Part E, deferred from Part 6",
        "Part F",
    ]
    if labels != expected:
        raise ValueError(
            f"ternary answer divisions changed: {labels!r}"
        )
    after_key = pattern.sub(
        lambda match: (
            f"<h3>{match.group(1)}</h3><p>{match.group(2).strip()}</p>"
        ),
        after_key,
    )
    if re.search(r"<strong>Part [A-F]", after_key):
        raise ValueError("ternary answer division remained inline")
    return before_key + "<h2>Answer key</h2>" + after_key


def style_pamphlet_dual_examples(body, title):
    """Give paired Tengwar and romanized examples semantic reading layers."""
    blocks = re.findall(r"<pre>(.*?)</pre>", body, flags=re.S)
    for block in blocks:
        groups = [
            group.splitlines()
            for group in re.split(r"\n\s*\n", block.strip())
        ]
        interlinear = []
        for lines in groups:
            if not lines:
                raise ValueError(
                    f"Tengwar pamphlet has an empty example group: {title}"
                )
            tengwar_match = re.fullmatch(
                r'<span class="teng-dual" aria-hidden="true">'
                r"(.*?)</span>",
                lines[0],
                flags=re.S,
            )
            source_lines = lines[1:]
            plain_lines = [
                html_module.unescape(line) for line in source_lines
            ]
            if (
                tengwar_match is None
                or len(source_lines) not in {2, 3, 4}
                or not is_current_phi_passage(plain_lines[0])
            ):
                raise ValueError(
                    f"Tengwar pamphlet example cannot be paired: {title}"
                )
            caption = (
                f"\n  <figcaption>{source_lines[2]}</figcaption>"
                if len(source_lines) >= 3
                else ""
            )
            source_line = (
                f'\n  <p class="pamphlet-example-source">'
                f"{source_lines[3]}</p>"
                if len(source_lines) == 4
                else ""
            )
            interlinear.append(f"""
<figure class="pamphlet-example pamphlet-dual-example" aria-label="Tengwar and romanized interlinear example">
  <div class="pamphlet-example-tengwar" aria-hidden="true">{tengwar_match.group(1)}</div>
  <p class="pamphlet-example-phi" lang="art-x-phi">{source_lines[0]}</p>
  <p class="pamphlet-example-gloss">{source_lines[1]}</p>{caption}{source_line}
</figure>""")
        if len(interlinear) == 1:
            replacement = interlinear[0]
        else:
            replacement = (
                '<div class="pamphlet-example-set '
                'pamphlet-dual-example-set" role="group" '
                'aria-label="Tengwar and romanized interlinear examples">'
                + "".join(interlinear)
                + "</div>"
            )
        body = body.replace(f"<pre>{block}</pre>", replacement, 1)
    if "<pre>" in body:
        raise ValueError(
            f"Tengwar pamphlet left an unpaired code block: {title}"
        )
    return body


def rename_manual_editorial_classes(body):
    """Rename shared renderer classes without touching prose or code samples."""
    return re.sub(
        r'class="([^"]*)"',
        lambda match: (
            'class="'
            + " ".join(
                (
                    class_name.replace("manual-", "pamphlet-", 1)
                    if class_name.startswith("manual-")
                    else class_name
                )
                for class_name in match.group(1).split()
            )
            + '"'
        ),
        body,
    )


def apply_pamphlet_ordered_starts(body, source, title):
    """Keep the source numbering when Markdown begins a list above one."""
    starts = pamphlet_ordered_list_starts(source)
    rendered = list(re.finditer(r"<ol>", body))
    if len(rendered) != len(starts):
        raise ValueError(
            f"pamphlet ordered-list count changed in {title} "
            f"({len(rendered)} rendered, {len(starts)} in source)"
        )
    start_iter = iter(starts)
    return re.sub(
        r"<ol>",
        lambda _match: (
            "<ol>"
            if (start := next(start_iter)) == 1
            else f'<ol start="{start}">'
        ),
        body,
    )


def pamphlet_section_heading(title, variant, section_number):
    """Build a workbook heading with an earned label."""
    prefix_match = re.fullmatch(r"(Table \d+|Error \d+|Part [A-F]): (.+)", title)
    if prefix_match is not None:
        label, display_title = prefix_match.groups()
    elif letter_match := re.fullmatch(r"([A-F])\. (.+)", title):
        label = f"Part {letter_match.group(1)}"
        display_title = letter_match.group(2)
    elif title.startswith("Practice: "):
        label = "Practice"
        display_title = title.removeprefix("Practice: ")
    elif title == "Answer key":
        label = "Check your work"
        display_title = title
    elif variant == "appendix":
        label = "Reference"
        display_title = title
    else:
        label = f"{section_number:02d}"
        display_title = title
    heading_id = manual_heading_id(title)
    if not heading_id:
        raise ValueError(f"pamphlet section lacks a stable anchor: {title}")
    heading = (
        f'<h2 class="pamphlet-section-title" id="{heading_id}">'
        f'<span>{html_module.escape(label)}</span>'
        f"{display_title}</h2>"
    )
    return heading_id, heading


def style_pamphlet_sections(body, variant, heading_level):
    """Wrap the page's primary workbook sections without changing their text."""
    pattern = re.compile(
        rf"<h{heading_level}>(.*?)</h{heading_level}>",
        flags=re.S,
    )
    matches = list(pattern.finditer(body))
    if not matches:
        raise ValueError(f"pamphlet {variant} page has no primary sections")
    result = [body[:matches[0].start()]]
    seen_ids = set()
    answer_section = False
    for index, match in enumerate(matches, start=1):
        end = matches[index].start() if index < len(matches) else len(body)
        title = html_module.unescape(re.sub(r"<[^>]+>", "", match.group(1)))
        heading_id, heading = pamphlet_section_heading(title, variant, index)
        if heading_id in seen_ids:
            raise ValueError(f"pamphlet section anchor repeats: {title}")
        seen_ids.add(heading_id)
        classes = ["pamphlet-section"]
        if title.startswith("Practice: "):
            classes.append("pamphlet-practice-section")
        if variant == "tables" and title.startswith("Table "):
            classes.append("pamphlet-table-section")
        if variant == "errors":
            classes.append("pamphlet-error-section")
        if variant == "exercises":
            answer_section = answer_section or title == "Answer key"
            classes.append(
                "pamphlet-answer-section"
                if answer_section
                else "pamphlet-exercise-section"
            )
        if variant == "answers":
            classes.append("pamphlet-reasoning-section")
        if variant == "appendix":
            classes.append("pamphlet-appendix-section")
        content = body[match.end():end]
        if variant == "exercises" and answer_section:
            content = re.sub(
                r"<h3>(Part [A-Z](?:(?::|,) .*?)?)</h3>",
                r'<h3 class="pamphlet-answer-part">'
                r"<span>Answers</span>\1</h3>",
                content,
            )
            content = re.sub(
                r"<p><strong>(Part [A-Z])\.</strong></p>",
                r'<h3 class="pamphlet-answer-part">'
                r"<span>Answers</span>\1</h3>",
                content,
            )
        result.append(
            f'<section class="{" ".join(classes)}" '
            f'aria-labelledby="{heading_id}">{heading}{content}</section>'
        )
    return "".join(result)


def style_pamphlet_answer_glosses(body):
    """Separate Phi and gloss lines in legacy interlinear answer items."""
    gloss_marker = re.compile(
        r"(?:^| )(?:[123]SG|PL|PST|FUT|NEG|REL|"
        r"[A-Z]+(?:\.[A-Z]+)+)(?: |$)"
    )

    def split_item(match):
        phi, gloss = match.groups()
        plain_gloss = html_module.unescape(gloss).strip()
        if gloss_marker.search(plain_gloss) is None:
            return match.group(0)
        return (
            '<li class="pamphlet-answer-interlinear">'
            f'<span class="pamphlet-answer-phi">{phi}</span>'
            f'<span class="pamphlet-answer-gloss">{gloss.strip()}</span>'
            "</li>"
        )

    return re.sub(
        r'<section class="[^"]*\bpamphlet-answer-section\b[^"]*"'
        r"[^>]*>.*?</section>",
        lambda section: re.sub(
            r'<li>(<code class="phi-inline"[^>]*>.*?</code>)\s+'
            r"([^<]+)</li>",
            split_item,
            section.group(0),
        ),
        body,
        flags=re.S,
    )


def style_pamphlet_answer_runs(body):
    """Restore answer items collapsed onto one Markdown source line."""
    single_item_list = re.compile(
        r"<ol(?P<attrs>[^>]*)><li>"
        r"(?P<content>(?:(?!</?li(?:\s|>)).)*)"
        r"</li></ol>",
        flags=re.S,
    )
    numbered_boundary = re.compile(r"\s(?P<number>\d+)\.\s+")

    def split_run(match):
        attributes = match.group("attrs")
        content = match.group("content")
        start_match = re.search(r'\bstart="(\d+)"', attributes)
        first_number = int(start_match.group(1)) if start_match else 1
        boundaries = list(numbered_boundary.finditer(content))
        numbers = [int(boundary.group("number")) for boundary in boundaries]
        if numbers != list(
            range(first_number + 1, first_number + 1 + len(numbers))
        ):
            return match.group(0)
        items = []
        item_start = 0
        for boundary in boundaries:
            items.append(content[item_start:boundary.start()].strip())
            item_start = boundary.end()
        items.append(content[item_start:].strip())
        if len(items) < 2 or any(not item for item in items):
            return match.group(0)
        return (
            f'<ol{attributes} class="pamphlet-answer-run">'
            + "".join(f"<li>{item}</li>" for item in items)
            + "</ol>"
        )

    return re.sub(
        r'<section class="[^"]*\bpamphlet-answer-section\b[^"]*"'
        r"[^>]*>.*?</section>",
        lambda section: single_item_list.sub(split_run, section.group(0)),
        body,
        flags=re.S,
    )


def style_pamphlet_bold_exercise_parts(body, title):
    """Restore bold exercise labels as sections when the source uses them."""
    prompt_pattern = re.compile(
        r"<p><strong>Part ([A-Z]): ([^<]+?)([.?!])</strong>"
        r"\s*(.*?)</p>",
        flags=re.S,
    )
    prompt_matches = list(prompt_pattern.finditer(body))
    if not prompt_matches:
        return body
    if body.count("<h2>Answer key</h2>") != 1:
        raise ValueError(
            f"bold-part exercises need one answer key: {title}"
        )
    before_key, after_key = body.split("<h2>Answer key</h2>")
    prompt_matches = list(prompt_pattern.finditer(before_key))
    prompt_letters = [match.group(1) for match in prompt_matches]
    expected_prompts = [
        chr(code)
        for code in range(ord("A"), ord("A") + len(prompt_letters))
    ]
    if prompt_letters != expected_prompts:
        raise ValueError(
            f"bold exercise parts are not consecutive: {title}"
        )

    def prompt_section(match):
        detail = match.group(4).strip()
        paragraph = f"<p>{detail}</p>" if detail else ""
        terminal = match.group(3) if match.group(3) != "." else ""
        return (
            f"<h2>Part {match.group(1)}: "
            f"{match.group(2)}{terminal}</h2>"
            f"{paragraph}"
        )

    before_key = prompt_pattern.sub(prompt_section, before_key)
    answer_pattern = re.compile(
        r"<p><strong>Part ([A-Z])\.</strong>\s*(.*?)</p>",
        flags=re.S,
    )
    answer_matches = list(answer_pattern.finditer(after_key))
    answer_letters = [match.group(1) for match in answer_matches]
    if answer_letters != prompt_letters[:len(answer_letters)]:
        raise ValueError(
            f"bold answer parts do not match their exercises: {title}"
        )

    def answer_section(match):
        detail = match.group(2).strip()
        paragraph = f"<p>{detail}</p>" if detail else ""
        return f"<h3>Part {match.group(1)}</h3>{paragraph}"

    after_key = answer_pattern.sub(answer_section, after_key)
    return before_key + "<h2>Answer key</h2>" + after_key


def style_pamphlet_opening(body, directory, paths, titles):
    """Turn the source opening into a linked workbook map."""
    subtitle_match = re.search(r"<h2>(.*?)</h2>", body, flags=re.S)
    if subtitle_match is None:
        raise ValueError("pamphlet opening lacks its subtitle")
    subtitle = subtitle_match.group(1)
    body = body[:subtitle_match.start()] + body[subtitle_match.end():]
    contents_match = re.search(
        r"<hr>\s*<p><strong>Contents:</strong></p>\s*"
        r"<ol>(.*?)</ol>\s*<hr>",
        body,
        flags=re.S,
    )
    if contents_match is None:
        raise ValueError("pamphlet opening contents boundaries changed")
    source_items = re.findall(
        r"<li>(.*?)</li>",
        contents_match.group(1),
        flags=re.S,
    )
    expected_items = [
        pamphlet_contents_label(title, index)
        for index, title in enumerate(titles)
        if index > 0
    ]
    plain_items = [
        html_module.unescape(re.sub(r"<[^>]+>", "", item))
        for item in source_items
    ]
    if plain_items != expected_items:
        raise ValueError(
            f"pamphlet opening contents differ from its live pages: {directory}; "
            f"source={plain_items!r}; pages={expected_items!r}"
        )
    linked_items = "".join(
        f'<li><a href="{directory}__{path.stem}.html">'
        f'<span>{index:02d}</span> '
        f"{html_module.escape(label)}</a></li>"
        for index, (path, label) in enumerate(
            zip(paths[1:], expected_items),
            start=1,
        )
    )
    contents = (
        '<nav class="pamphlet-contents" aria-label="Workbook contents">'
        '<p>Workbook map</p><ol>'
        + linked_items
        + "</ol></nav>"
    )
    body = (
        body[:contents_match.start()]
        + contents
        + body[contents_match.end():]
    )
    body, outcome_count = re.subn(
        r"<p>(By the end of this pamphlet, you will"
        r"(?: be able to)?:)</p>\s*"
        r"(<ul>.*?</ul>)",
        r'<div class="pamphlet-outcomes"><p>\1</p>\2</div>',
        body,
        count=1,
        flags=re.S,
    )
    if (
        "By the end of this pamphlet, you will" in body
        and outcome_count != 1
    ):
        raise ValueError("pamphlet opening outcome boundary changed")
    body = re.sub(
        r"<p><em>(.*?)</em></p>\s*$",
        r'<p class="pamphlet-closing-note">\1</p>',
        body,
        count=1,
        flags=re.S,
    )
    return subtitle, body


def apply_pamphlet_editorial(
    body,
    source,
    treatment,
    pamphlet,
    paths,
    titles,
    index,
):
    """Apply the workbook treatment to one structurally pinned page."""
    title = titles[index]
    title_tags = [
        match.group(0)
        for match in re.finditer(r"<h1>(.*?)</h1>", body, flags=re.S)
        if html_module.unescape(
            re.sub(r"<[^>]+>", "", match.group(1))
        )
        == title
    ]
    if len(title_tags) != 1:
        raise ValueError(
            f"pamphlet editorial title is missing or ambiguous: {title}"
        )
    body = body.replace(title_tags[0], "", 1)
    label, display_title = pamphlet_display_title(title, index)
    subtitle = None
    if treatment["variant"] == "opening":
        subtitle, body = style_pamphlet_opening(
            body,
            pamphlet["directory"],
            paths,
            titles,
        )

    body = mark_pamphlet_inline_phi(body)
    body = mark_manual_inline_phi(body)
    body = style_pamphlet_tables(body, title)
    motif = PAMPHLET_GROUPS[pamphlet["directory"]]["motif"]
    if motif == "ternary_scale":
        body = style_pamphlet_ternary_drills(body, title)
        body = style_pamphlet_ternary_worked_numbers(body, title)
        body = style_pamphlet_ternary_dialogue_examples(body, title)
    body = (
        style_pamphlet_dual_examples(body, title)
        if pamphlet["dual_script"]
        else style_pamphlet_examples(body)
    )
    body = apply_pamphlet_ordered_starts(body, source, title)
    if treatment["variant"] == "exercises":
        answer_key_count = body.count("<h1>Answer key</h1>")
        if answer_key_count > 1:
            raise ValueError("pamphlet exercises have multiple answer keys")
        if answer_key_count == 1:
            before_key, after_key = body.split("<h1>Answer key</h1>")
            after_key = re.sub(
                r"<h2>(Part [A-Z](?:: .*?)?)</h2>",
                r"<h3>\1</h3>",
                after_key,
            )
            body = before_key + "<h2>Answer key</h2>" + after_key
        if pamphlet["dual_script"]:
            body = style_pamphlet_bold_exercise_parts(body, title)
        if motif == "ternary_scale":
            body = style_pamphlet_ternary_answer_parts(body, title)
    if treatment["variant"] == "reference":
        if (
            not body.lstrip().startswith(
                '<div class="pamphlet-table-wrap'
            )
            or body.count("<p>") != 1
        ):
            raise ValueError(
                "pamphlet reference page needs a table and one closing note"
            )
        body = re.sub(
            r"<p>",
            '<p class="pamphlet-closing-note">',
            body,
            count=1,
        )
    elif treatment["variant"] != "answers":
        body = re.sub(
            r"<p>",
            '<p class="pamphlet-page-lede">',
            body,
            count=1,
        )
    if treatment["variant"] != "opening":
        section_level = treatment.get(
            "section_level",
            pamphlet_default_section_level(treatment["variant"]),
        )
        if section_level:
            body = style_pamphlet_sections(
                body,
                treatment["variant"],
                section_level,
            )
        if treatment["variant"] == "exercises":
            body = style_pamphlet_answer_glosses(body)
            body = style_pamphlet_answer_runs(body)

    position = f"Reading {index + 1} of {len(paths)}"
    subtitle_html = (
        f'<p class="pamphlet-subtitle">{subtitle}</p>'
        if subtitle is not None
        else ""
    )
    progress = (index + 1) * 100 / len(paths)
    header = (
        '<header class="pamphlet-page-header">'
        '<div class="pamphlet-header-meta"><p>'
        '<span class="pamphlet-shelf-label">Phi practice</span> '
        '<span class="pamphlet-meta-separator" aria-hidden="true">'
        '&middot;</span> '
        f'<span>{html_module.escape(pamphlet["title"])}</span></p>'
        f"<p>{position}</p></div>"
        '<div class="pamphlet-title-row"><div>'
        f'<p class="pamphlet-page-label">{html_module.escape(label)}</p>'
        f"<h1>{html_module.escape(display_title)}</h1></div>"
        f"{pamphlet_motif(motif)}{subtitle_html}</div>"
        '<div class="pamphlet-progress" aria-hidden="true">'
        f'<span style="width:{progress:.3f}%"></span></div>'
        "</header>"
    )
    rail = pamphlet_reading_rail(
        pamphlet["directory"],
        paths,
        titles,
        index,
    )
    validate_pamphlet_reader_fallback(
        header,
        rail,
        pamphlet["title"],
        len(paths),
    )
    return header + rail + body


def pamphlet_editorial_navigation(previous, following):
    """Give a workbook page labelled previous and next links."""
    previous_link = (
        f'<a class="pamphlet-nav-page pamphlet-nav-previous" '
        f'href="{previous["href"]}"><span>Previous</span> '
        f'<strong>{html_module.escape(previous["title"])}</strong></a>'
        if previous
        else '<span class="pamphlet-nav-page"></span>'
    )
    next_link = (
        f'<a class="pamphlet-nav-page pamphlet-nav-next" '
        f'href="{following["href"]}"><span>Next</span> '
        f'<strong>{html_module.escape(following["title"])}</strong></a>'
        if following
        else '<span class="pamphlet-nav-page"></span>'
    )
    return (
        '<nav class="chapnav pamphlet-page-nav" aria-label="Workbook pages">'
        f'{previous_link} <a class="pamphlet-nav-contents" '
        f'href="index.html">All pamphlets</a> {next_link}</nav>'
    )


PAMPHLET_MOTIF_LABELS = {
    "ordered_slots": "Particle system",
    "clause_links": "Clause work",
    "event_views": "Time and view",
    "source_routes": "Claimed source",
    "participant_reference": "Participant reference",
    "noun_phrase": "Noun phrase",
    "name_designation": "Naming",
    "source_beside": "Source boundary",
    "audible_boundaries": "Speech and writing",
    "written_hands": "Writing system",
    "ternary_scale": "Number",
}


def pamphlet_contents_arrow():
    """Return the decorative Lucide arrow used by a workbook link."""
    return (
        '<span class="pamphlet-index-arrow" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" '
        'stroke="currentColor" stroke-linecap="round" '
        'stroke-linejoin="round" stroke-width="1.5" focusable="false">'
        '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'
        "</svg></span>"
    )


def pamphlet_contents_page(entries):
    """Build the catalogue-driven entrance to the workbook shelf."""
    if not entries:
        raise ValueError("pamphlet contents require at least one workbook")
    directories = [entry["directory"] for entry in entries]
    if (
        len(directories) != len(set(directories))
        or set(directories) != set(PAMPHLET_GROUPS)
    ):
        raise ValueError(
            "pamphlet contents and editorial catalogue differ"
        )
    motifs = {entry["motif"] for entry in entries}
    if not motifs <= set(PAMPHLET_MOTIF_LABELS):
        raise ValueError("pamphlet contents contain an unknown motif")
    if any(entry["page_count"] < 1 for entry in entries):
        raise ValueError("pamphlet contents contain an empty workbook")

    rows = []
    for entry in entries:
        page_count = entry["page_count"]
        page_noun = "reading" if page_count == 1 else "readings"
        motif_class = entry["motif"].replace("_", "-")
        rows.append(
            f'<li class="pamphlet-index-entry '
            f'pamphlet-{motif_class}-page">'
            f'<a href="{entry["href"]}">'
            '<div class="pamphlet-index-copy">'
            '<p class="pamphlet-index-entry-meta">'
            f'{html_module.escape(PAMPHLET_MOTIF_LABELS[entry["motif"]])}'
            ' <span aria-hidden="true">&middot;</span> '
            f"{page_count} {page_noun}</p>"
            f'<h3>{html_module.escape(entry["title"])}</h3>'
            f'<p class="pamphlet-index-summary">'
            f'{html_module.escape(entry["summary"])}</p></div>'
            f'{pamphlet_motif(entry["motif"])}'
            f"{pamphlet_contents_arrow()}</a></li>"
        )

    total_pages = sum(entry["page_count"] for entry in entries)
    return (
        '<header class="pamphlet-index-header">'
        '<div class="pamphlet-index-meta">'
        '<p><span>Phi practice</span> <span>Contents</span></p>'
        '<p>Workbooks for use</p></div>'
        '<div class="pamphlet-index-title-row">'
        '<h1>The pamphlets</h1>'
        '<div class="pamphlet-index-mark" aria-hidden="true"></div>'
        '<p class="pamphlet-index-lede">The manual gives Phi\'s grammar '
        "its full account. These workbooks spend more time with the places "
        "where an example on its own is not quite enough. Read one straight "
        "through, or keep it open beside the manual with a pencil nearby.</p>"
        "</div>"
        '<p class="pamphlet-index-counts" aria-label="Pamphlet shelf extent">'
        f"<span><strong>{len(entries)}</strong> workbooks</span> "
        f"<span><strong>{total_pages}</strong> readings</span></p>"
        "</header>"
        '<section class="pamphlet-index-catalogue" '
        'aria-labelledby="pamphlet-index-catalogue-heading">'
        '<header class="pamphlet-index-section-heading"><div>'
        '<p class="pamphlet-index-section-label">Catalogue order</p>'
        '<h2 id="pamphlet-index-catalogue-heading">Choose a workbook</h2>'
        "</div>"
        f'<p class="pamphlet-index-section-count">{len(entries):02d} '
        "on the shelf</p></header>"
        f'<ol class="pamphlet-index-list">{"".join(rows)}</ol>'
        "</section>"
    )


PAMPHLET_GROUPS, PAMPHLET_EDITORIAL = load_pamphlet_editorial()


def pamphlet_page(
    body,
    title,
    footer_nav="",
    editorial_variant=None,
    editorial_motif=None,
):
    body_class = "landing primer"
    main_body = body
    if editorial_variant is not None:
        body_class += " pamphlet-editorial"
        variant_class = editorial_variant.replace("_", "-")
        body_class += f" pamphlet-{variant_class}-page"
        if editorial_motif is not None:
            motif_class = editorial_motif.replace("_", "-")
            body_class += f" pamphlet-{motif_class}-page"
        main_body = f'<article class="pamphlet-work">{body}</article>'
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
<body class="{body_class}">
{NAV_PAMPH}
<main>
{main_body}
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
pamph_pages = 0
pamphlet_index_entries = []
for pamphlet in PAMPHLETS:
    dirname = pamphlet["directory"]
    title = pamphlet["title"]
    pfiles = sorted((ROOT / "pamphlets" / dirname).glob("*.md"))
    ptitles = [title_of(f.read_text()) for f in pfiles]
    dual = pamphlet["dual_script"]
    for i, f in enumerate(pfiles):
        source = f.read_text()
        repo_path = f.relative_to(ROOT).as_posix()
        treatment = PAMPHLET_EDITORIAL.get(repo_path)
        html = md_to_html(source)
        body = tengwarize_dual(html) if dual else html
        if treatment is None:
            prev_link = f'<a href="{dirname}__{pfiles[i-1].stem}.html">&lsaquo; {ptitles[i-1]}</a>' if i > 0 else ""
            next_link = f'<a href="{dirname}__{pfiles[i+1].stem}.html">{ptitles[i+1]} &rsaquo;</a>' if i + 1 < len(pfiles) else ""
            footer_nav = f'<div class="chapnav">{prev_link}<a href="index.html">all pamphlets</a>{next_link}</div>'
        else:
            body = apply_pamphlet_editorial(
                body,
                source,
                treatment,
                pamphlet,
                pfiles,
                ptitles,
                i,
            )
            previous = (
                {
                    "href": f"{dirname}__{pfiles[i - 1].stem}.html",
                    "title": ptitles[i - 1],
                }
                if i > 0
                else None
            )
            following = (
                {
                    "href": f"{dirname}__{pfiles[i + 1].stem}.html",
                    "title": ptitles[i + 1],
                }
                if i + 1 < len(pfiles)
                else None
            )
            footer_nav = pamphlet_editorial_navigation(previous, following)
        linked_body = link_text_citations(body)
        (PAMPH_OUT / f"{dirname}__{f.stem}.html").write_text(
            pamphlet_page(
                linked_body,
                ptitles[i],
                footer_nav,
                editorial_variant=(
                    treatment["variant"] if treatment is not None else None
                ),
                editorial_motif=(
                    PAMPHLET_GROUPS[dirname]["motif"]
                    if treatment is not None
                    else None
                ),
            )
        )
        pamph_pages += 1
    pamphlet_index_entries.append(
        {
            **pamphlet,
            "href": f"{dirname}__{pfiles[0].stem}.html",
            "motif": PAMPHLET_GROUPS[dirname]["motif"],
            "page_count": len(pfiles),
        }
    )
(PAMPH_OUT / "index.html").write_text(
    pamphlet_page(
        pamphlet_contents_page(pamphlet_index_entries),
        "contents",
        editorial_variant="contents",
    )
)
print(f"wrote build/site/pamphlets/: {pamph_pages} pages + contents")
