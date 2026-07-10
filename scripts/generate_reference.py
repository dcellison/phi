#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate the Part VII lexicon reference from the vocabulary JSON.

Writes four markdown files under manual/part7_reference/lexicon/:
  - alphabetical.md   every word, A-Z: word, gloss, IPA, part of speech
  - by_domain.md      content words grouped by semantic-domain tag
  - by_module.md      optional module vocabulary grouped by module
  - by_pos.md         all words grouped by part of speech / function class

The vocabulary JSON remains the single source of truth; these files are
GENERATED artifacts. Never edit them by hand — rerun this script after
any vocabulary change:

    python3 scripts/generate_reference.py
"""

import json
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
OUT_DIR = PROJECT_ROOT / "manual" / "part7_reference" / "lexicon"

HEADER = """<!-- GENERATED FILE — do not edit.
     Source of truth: vocabulary/*.json
     Regenerate with: python3 scripts/generate_reference.py -->

"""

MODULE_TITLES = {
    "household-and-daily-life": "Household and Daily Life",
    "medical-and-bodily-care": "Medical and Bodily Care",
    "systems-and-shared-infrastructure": "Systems and Shared Infrastructure",
    "philosophical-reasoning": "Philosophical Reasoning",
    "accessibility-and-participation": "Accessibility and Participation",
    "commons-and-collective-governance": "Commons and Collective Governance",
    "ecological-systems-and-material-life": "Ecological Systems and Material Life",
    "work-craft-and-repair": "Work, Craft, and Repair",
}


def load_entries():
    entries = []
    for path in sorted(VOCABULARY_DIR.rglob("*.json")):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        cls = path.relative_to(VOCABULARY_DIR).parts[0]  # content/function/interjection
        subclass = (
            path.relative_to(VOCABULARY_DIR).parts[1]
            if cls == "function" and len(path.relative_to(VOCABULARY_DIR).parts) > 2
            else cls
        )
        entries.append((d, cls, subclass))
    return entries


def alphabetical(entries):
    lines = [HEADER, "# The Phi Lexicon — Alphabetical\n"]
    lines.append(f"*{len(entries)} words.*\n")
    lines.append("| Word | Gloss | IPA | Part of speech |")
    lines.append("|---|---|---|---|")
    for d, _, _ in sorted(entries, key=lambda e: e[0]["word"]):
        pos = ", ".join(d.get("pos", []))
        lines.append(f"| `{d['word']}` | {d['gloss']} | {d['ipa']} | {pos} |")
    return "\n".join(lines) + "\n"


def by_domain(entries):
    domains = defaultdict(list)
    for d, cls, _ in entries:
        if cls != "content":
            continue
        for tag in d.get("tags", {}):
            domains[tag].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Semantic Domain\n"]
    lines.append(
        "*Content words grouped by domain tag. Words with several tags "
        "appear in each of their domains.*\n"
    )
    for tag in sorted(domains):
        words = sorted(domains[tag], key=lambda d: d["word"])
        lines.append(f"\n## {tag} ({len(words)})\n")
        lines.append("| Word | Gloss | In this domain |")
        lines.append("|---|---|---|")
        for d in words:
            lines.append(f"| `{d['word']}` | {d['gloss']} | {d['tags'][tag]} |")
    return "\n".join(lines) + "\n"


def by_module(entries):
    modules = defaultdict(list)
    for d, cls, _ in entries:
        if cls != "content":
            continue
        for module in d.get("modules", []):
            modules[module].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Optional Module\n"]
    lines.append("*Module vocabulary is ordinary Phi vocabulary with ordinary Phi grammar. These groupings let learners choose specialized fields without treating their terminology as required core study.*\n")
    if not modules:
        lines.append("No module-specific words have been recorded yet.\n")
    for module in sorted(modules, key=lambda item: MODULE_TITLES.get(item, item)):
        words = sorted(modules[module], key=lambda d: d["word"])
        title = MODULE_TITLES.get(module, module.replace("-", " ").title())
        lines.append(f"\n## {title}\n")
        lines.append(f"*{len(words)} module words.*\n")
        lines.append("| Word | Gloss | Part of speech | Concept |")
        lines.append("|---|---|---|---|")
        for d in words:
            pos = ", ".join(d.get("pos", []))
            concept = d.get("concept", "").split(" / ")[0]
            lines.append(f"| `{d['word']}` | {d['gloss']} | {pos} | {concept} |")
    return "\n".join(lines) + "\n"


def by_pos(entries):
    groups = defaultdict(list)
    for d, cls, subclass in entries:
        if cls == "content":
            for p in d.get("pos", ["(unspecified)"]):
                groups[p].append(d)
        else:
            groups[subclass].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Part of Speech\n"]
    lines.append(
        "*Content words appear under every part of speech they can "
        "serve as (Phi's analytic grammar lets many words work as "
        "noun, verb, and adjective). Function words are grouped by "
        "their class.*\n"
    )
    for group in sorted(groups):
        words = sorted(groups[group], key=lambda d: d["word"])
        lines.append(f"\n## {group} ({len(words)})\n")
        lines.append("| Word | Gloss | Concept |")
        lines.append("|---|---|---|")
        for d in words:
            concept = d.get("concept", "").split(" / ")[0]
            lines.append(f"| `{d['word']}` | {d['gloss']} | {concept} |")
    return "\n".join(lines) + "\n"


def main():
    entries = load_entries()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "alphabetical.md").write_text(alphabetical(entries), encoding="utf-8")
    (OUT_DIR / "by_domain.md").write_text(by_domain(entries), encoding="utf-8")
    (OUT_DIR / "by_module.md").write_text(by_module(entries), encoding="utf-8")
    (OUT_DIR / "by_pos.md").write_text(by_pos(entries), encoding="utf-8")
    print(f"Generated 4 reference files from {len(entries)} entries into {OUT_DIR}")


if __name__ == "__main__":
    main()
