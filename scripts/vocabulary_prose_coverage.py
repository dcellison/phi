#!/usr/bin/env python3
"""Measure progress from the legacy lexicon prose shape to the target contract."""

import json
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
REPORT_FILE = (
    PROJECT_ROOT / "documents" / "validation" / "vocabulary_prose_coverage.json"
)

TARGET_FIELDS = ("articulatory_notes", "examples")
LEGACY_FIELDS = ("concept", "grammatical_notes")
COUNTED_FIELDS = (
    "articulatory_notes",
    "examples",
    "search_terms",
    "usage_notes",
    "sound_symbolism",
    "pillars",
    "concept",
    "grammatical_notes",
)
STATES = ("legacy", "partial", "dual", "target")


def entry_state(entry):
    """Classify one entry by which old and target prose fields it carries."""
    target_count = sum(field in entry for field in TARGET_FIELDS)
    has_legacy = any(field in entry for field in LEGACY_FIELDS)
    if target_count == 0:
        return "legacy"
    if target_count < len(TARGET_FIELDS):
        return "partial"
    return "dual" if has_legacy else "target"


def load_entries(root=PROJECT_ROOT):
    """Return ``(kind, entry)`` pairs from all three lexicon directories."""
    vocabulary = root / "vocabulary"
    entries = []
    for kind in ("content", "function", "interjection"):
        for path in sorted((vocabulary / kind).rglob("*.json")):
            entries.append((kind, json.loads(path.read_text(encoding="utf-8"))))
    return entries


def state_counts(entries):
    counts = Counter(entry_state(entry) for _kind, entry in entries)
    return {state: counts[state] for state in STATES}


def build_report(entries):
    """Build the stable report committed as migration evidence."""
    entries = list(entries)
    by_kind = {}
    for kind in ("content", "function", "interjection"):
        selected = [pair for pair in entries if pair[0] == kind]
        by_kind[kind] = {
            "total": len(selected),
            "states": state_counts(selected),
        }
    return {
        "contract": "lexicon-prose-v1",
        "total": len(entries),
        "states": state_counts(entries),
        "by_kind": by_kind,
        "fields": {
            field: sum(field in entry for _kind, entry in entries)
            for field in COUNTED_FIELDS
        },
    }


def render_report(report):
    return json.dumps(report, indent=2, ensure_ascii=False) + "\n"


def main():
    report = build_report(load_entries())
    REPORT_FILE.write_text(render_report(report), encoding="utf-8")
    print(
        f"wrote {REPORT_FILE.relative_to(PROJECT_ROOT)}: "
        f"{report['total']} entries"
    )


if __name__ == "__main__":
    main()
