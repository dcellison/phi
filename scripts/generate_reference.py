#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate the Part VII lexicon reference from the vocabulary JSON.

Writes three markdown files under manual/part7_reference/lexicon/:
  - alphabetical.md   every word, A-Z: word, gloss, IPA, part of speech
  - by_domain.md      content words grouped by semantic-domain tag
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
    (OUT_DIR / "by_pos.md").write_text(by_pos(entries), encoding="utf-8")
    print(f"Generated 3 reference files from {len(entries)} entries into {OUT_DIR}")


if __name__ == "__main__":
    main()
