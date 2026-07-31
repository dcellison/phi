# Phi website source

This directory holds the maintained assets for Phi's website: the lexicon explorer shell, styles, browser scripts, fonts, and the editorial configuration that gives each shelf its design. It contains no generated pages or data.

The site builder copies these assets to `build/site/`, renders the repository's Markdown shelves there, and generates the lexicon and compound data. The complete deployment tree is ignored by Git.

Local preview:

```bash
python3 scripts/build_site.py
python3 -m http.server -d build/site
```

Then open http://localhost:8000. GitHub Pages builds and deploys the same directory on every push to `main` through `.github/workflows/pages.yml`.

## Editorial configuration

Six JSON files here decide how each shelf is rendered. The Markdown sources stay plain, with no front matter and no layout markers in the prose, so everything the renderer needs to know about a page's shape is recorded in one of these files instead.

| File | What it treats | Coverage |
|---|---|---|
| `primer_editorial.json` | the primer's 30 lessons, grouped into parts | total, every chapter from 1 to `total_chapters` |
| `manual_editorial.json` | 145 pages of the manual, including the colophon | total within each group named in `complete_groups` |
| `pamphlet_editorial.json` | 155 workbook pages across 14 pamphlets | total within each directory named in `complete_pamphlets`, opening at `00_title.md` |
| `texts_editorial.json` | 16 works on the texts shelf | opt in, and every key must be a catalogued work |
| `news_from_nowhere_editorial.json` | the novel, chapter by chapter | total, every `chapter_*.md` file numbered from 1 |
| `editorial.json` | 16 book pages | opt in, one or more `pull_quotes` and an optional `eyebrow` |

Each loader runs at the top of its shelf's build and raises on the first disagreement it finds, so a config that has drifted from its sources stops the build with a named path and a stated reason. Nothing degrades quietly. A page that silently lost its treatment would look broken to a reader and fine in the build log, and that is the failure these checks exist to prevent. Read the message before assuming the source is at fault, because the config is usually the half that went stale.

### Agreement with files outside this directory

Several of these checks reach outside this directory, which is what makes the failures surprising the first time.

| Config | Checked against | What has to agree |
|---|---|---|
| `primer_editorial.json` | `primer/README.md` | part labels, every story title, and the number of ladder tables |
| `manual_editorial.json` | `manual/outline.md` | part titles, chapter titles, and chapter numbers running from 1 without gaps |
| `texts_editorial.json` | `texts/catalogue.json` | the work's title, and a `form` compatible with its catalogued method |
| `news_from_nowhere_editorial.json` | `texts/catalogue.json` and `texts/news_from_nowhere/` | book title, each chapter's method, and the exact sequence of chapter filenames |
| `pamphlet_editorial.json` | `pamphlets/catalogue.json` | every complete pamphlet names a catalogued directory |

So renaming a primer story or reordering a manual part is never a one-file edit. The contents page, the config, and the source all move together or the build says so.

### Closed vocabularies

Every `motif` names a drawing the script already holds, and every `variant` names a layout it already knows how to build. The primer has four motifs (household, seasons, gathering, story), the manual nine, the pamphlets eleven, and the texts shelf fourteen. Manual pages choose from eight variants, pamphlet pages from eleven, and each texts entry declares one of six forms, which then decides the rest of its required fields. Reuse an existing value where one fits. Adding a motif means new artwork in `scripts/build_site.py` and matching rules in `style.css`, so it is a design decision rather than a configuration change.

### Structural signatures

Manual and pamphlet entries carry a `shape` string that pins the page's block structure: how many headings sit at each level, how large each table is, how long each fenced block runs, and what shape its quotes, lists, and rules have. Pamphlets append the start number of every ordered list, which keeps visible exercise numbering from drifting when a workbook is edited.

Change a page's structure and the build stops without reporting the new value. A manual page at least says that its source structure changed. A pamphlet page reports only an invalid treatment, because the shape check shares one condition with the variant and section level, so suspect the shape first. Either way, recompute the string and paste it in. `scripts/build_site.py` has no main guard and runs the whole build on import, so lift the four functions out of the module rather than importing it:

```bash
python3 - <<'PY'
import ast, re
src = open("scripts/build_site.py").read()
wanted = {"markdown_table_shapes", "manual_structural_signature",
          "pamphlet_ordered_list_starts", "pamphlet_structural_signature"}
ns = {"re": re}
for node in ast.parse(src).body:
    if isinstance(node, ast.FunctionDef) and node.name in wanted:
        exec(compile(ast.Module([node], []), "<sig>", "exec"), ns)
page = "pamphlets/three_slots/03_slot_1_tense_aspect.md"
print(ns["pamphlet_structural_signature"](open(page).read()))
PY
```

Use `manual_structural_signature` for a manual page and `pamphlet_structural_signature` for a workbook page.

The texts and news configs work differently. They declare counts the renderer verifies as it goes: how many opening paragraphs a page has, how many interlinear blocks and notes, how many tables and inner dividers. Those errors print what was expected beside what was found, so they need no recipe.

### Primer pages outside the numbered range

The prelude, `00_before_you_begin.md`, and the capstone, `31_capstone.md`, sit outside `total_chapters` on purpose and take their own treatments, dispatched by filename in the build script. That is why the capstone can be numbered above the last chapter. Renumbering or renaming either page fails the build with a report that a primer page has no editorial treatment, so the arrangement is odd to look at but not fragile.

Update a config in the same commit as the source it describes. The build catches the drift either way, but it picks the moment.
