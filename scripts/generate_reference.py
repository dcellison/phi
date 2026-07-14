#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate the Part VII lexicon reference from the vocabulary JSON,
and the Part VII compound reference from the compound registry.

Writes four markdown files under manual/part7_reference/lexicon/:
  - alphabetical.md   every word, A-Z: word, gloss, IPA, part of speech
  - by_domain.md      content words grouped by semantic domain
  - by_module.md      optional module vocabulary grouped by module
  - by_pos.md         all words grouped by part of speech / function class

and one under manual/part7_reference/:
  - compounds.md      every canonized compound idiom, from documents/reference/compounds.md

The vocabulary JSON and the compound registry remain the single sources
of truth; these files are GENERATED artifacts. Never edit them by hand —
rerun this script after any vocabulary or registry change:

    python3 scripts/generate_reference.py
"""

import json
from collections import defaultdict
from pathlib import Path

from compound_registry import load_compounds

PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
VOCABULARY_ENTRY_DIRS = tuple(
    VOCABULARY_DIR / name for name in ("content", "function", "interjection")
)
OUT_DIR = PROJECT_ROOT / "manual" / "part7_reference" / "lexicon"
COMPOUNDS_OUT = PROJECT_ROOT / "manual" / "part7_reference" / "compounds.md"

HEADER = """<!-- GENERATED FILE — do not edit.
     Source of truth: vocabulary entry JSON
     Regenerate with: python3 scripts/generate_reference.py -->

"""

COMPOUNDS_HEADER = """<!-- GENERATED FILE — do not edit.
     Source of truth: documents/reference/compounds.md
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
    paths = sorted(
        path
        for directory in VOCABULARY_ENTRY_DIRS
        for path in directory.rglob("*.json")
    )
    for path in paths:
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
        pos = d.get("pos", "")
        lines.append(f"| `{d['word']}` | {d['gloss']} | {d['ipa']} | {pos} |")
    return "\n".join(lines) + "\n"


def by_domain(entries):
    domains = defaultdict(list)
    for d, cls, _ in entries:
        if cls != "content":
            continue
        for domain in d.get("semantic_domains", {}):
            domains[domain].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Semantic Domain\n"]
    lines.append(
        "*Content words grouped by semantic domain. Words in several domains "
        "appear under each one.*\n"
    )
    for domain in sorted(domains):
        words = sorted(domains[domain], key=lambda d: d["word"])
        lines.append(f"\n## {domain} ({len(words)})\n")
        lines.append("| Word | Gloss | In this domain |")
        lines.append("|---|---|---|")
        for d in words:
            rationale = d["semantic_domains"][domain]
            lines.append(f"| `{d['word']}` | {d['gloss']} | {rationale} |")
    return "\n".join(lines) + "\n"


def by_module(entries):
    modules = defaultdict(list)
    for d, cls, _ in entries:
        if cls != "content":
            continue
        for module in d.get("modules", []):
            modules[module].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Optional Module\n"]
    lines.append("*Module vocabulary is ordinary Phi vocabulary with ordinary Phi grammar. These groupings let learners choose specialized fields without treating their terminology as required core study. A word with several module classifications appears in every learning path where it belongs.*\n")
    if not modules:
        lines.append("No module-specific words have been recorded yet.\n")
    for module in sorted(modules, key=lambda item: MODULE_TITLES.get(item, item)):
        words = sorted(modules[module], key=lambda d: d["word"])
        title = MODULE_TITLES.get(module, module.replace("-", " ").title())
        lines.append(f"\n## {title}\n")
        lines.append(f"*{len(words)} words in this learning path.*\n")
        lines.append("| Word | Gloss | Part of speech |")
        lines.append("|---|---|---|")
        for d in words:
            pos = d.get("pos", "")
            lines.append(f"| `{d['word']}` | {d['gloss']} | {pos} |")
    return "\n".join(lines) + "\n"


def by_pos(entries):
    groups = defaultdict(list)
    for d, cls, subclass in entries:
        if cls == "content":
            groups[d.get("pos", "(unspecified)")].append(d)
        else:
            groups[subclass].append(d)
    lines = [HEADER, "# The Phi Lexicon — By Part of Speech\n"]
    lines.append(
        "*Content words appear under their listed lexical class. A "
        "rule-supplied event or quality noun does not add another class "
        "to the entry. Function words are grouped by grammatical class.*\n"
    )
    for group in sorted(groups):
        words = sorted(groups[group], key=lambda d: d["word"])
        lines.append(f"\n## {group} ({len(words)})\n")
        lines.append("| Word | Gloss |")
        lines.append("|---|---|")
        for d in words:
            lines.append(f"| `{d['word']}` | {d['gloss']} |")
    return "\n".join(lines) + "\n"


def compounds_reference(compounds):
    lines = [COMPOUNDS_HEADER, "# The Compound Registry\n"]
    lines.append(f"*{len(compounds)} canonized compounds.*\n")
    lines.append("Canonized compound idioms are multi-word expressions whose meaning is a stable part of the language, not one-off improvisations. Each stays compositional because the composition itself carries the insight a coined label would hide.\n")
    lines.append("Reach for these before composing fresh, and before proposing a new word: registry first, then free composition, then, deliberately and by the protocol, a coinage. Every word inside a compound is an ordinary lexicon word; the explorer shows each compound on its member words' entries.\n")
    section = None
    for c in compounds:
        if c["section"] != section:
            section = c["section"]
            lines.append(f"\n## {section}\n")
            lines.append("| Compound | Literal | Meaning | Why compositional |")
            lines.append("|---|---|---|---|")
        lines.append(f"| `{c['compound']}` | {c['literal']} | {c['meaning']} | {c['why']} |")
    return "\n".join(lines) + "\n"


def main():
    entries = load_entries()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "alphabetical.md").write_text(alphabetical(entries), encoding="utf-8")
    (OUT_DIR / "by_domain.md").write_text(by_domain(entries), encoding="utf-8")
    (OUT_DIR / "by_module.md").write_text(by_module(entries), encoding="utf-8")
    (OUT_DIR / "by_pos.md").write_text(by_pos(entries), encoding="utf-8")
    compounds = load_compounds()
    COMPOUNDS_OUT.write_text(compounds_reference(compounds), encoding="utf-8")
    print(f"Generated 4 reference files from {len(entries)} entries into {OUT_DIR}")
    print(f"Generated {COMPOUNDS_OUT.relative_to(PROJECT_ROOT)} from {len(compounds)} registry rows")


if __name__ == "__main__":
    main()
