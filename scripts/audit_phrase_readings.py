#!/usr/bin/env python3
"""Report how many structural readings Phi's sentences admit.

Every sentence in the lexicon's examples and the active Markdown is parsed
and its readings counted by ``phi_readings``. A reading is one way of
dividing a clause into subject, adjuncts, object, and manner, together with
one choice of where each dependent clause ends. The counter has no verb
valency and no meanings, so the figures are an upper bound on structural
choice and say nothing about how often a reader goes wrong.

Two counts are given. The conservative count lets only nouns, pronouns, and
names end a phrase freely. The full count also lets an adjective (quality
noun) or a verb (event noun) head a phrase with modifiers of its own.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys

from phi_readings import ReadingCounter
from phi_sentence_validator import Lexicon, PROJECT_ROOT
import validate_sentences

GROUPS = (
    ("Translations", "texts/"),
    ("Original compositions", "texts/"),
    ("Manual", "manual/"),
    ("Pamphlets", "pamphlets/"),
    ("Primer", "primer/"),
    ("Book", "book/"),
    ("Dictionary examples", "vocabulary/"),
    ("Other documents", ""),
)


def original_works() -> frozenset[str]:
    catalogue = json.loads((PROJECT_ROOT / "texts" / "catalogue.json").read_text(encoding="utf-8"))
    return frozenset(
        "texts/" + work["path"]
        for work in catalogue.get("works", [])
        if work.get("method", "").lower().startswith("original")
    )


def group_of(path: str, originals: frozenset[str]) -> str:
    if path.startswith("texts/"):
        return "Original compositions" if path in originals else "Translations"
    for name, prefix in GROUPS[2:-1]:
        if path.startswith(prefix):
            return name
    return "Other documents"


def collect(paths: list[str] | None, openers: frozenset[str] = frozenset()):
    lexicon = Lexicon.load()
    counter = ReadingCounter(lexicon, openers=openers)
    sources = []
    if not paths:
        sources.extend(validate_sentences.iter_lexicon_examples(PROJECT_ROOT))
    sources.extend(
        validate_sentences.iter_markdown_examples(
            PROJECT_ROOT, lexicon, paths or validate_sentences.ACTIVE_DOC_ROOTS
        )
    )
    seen = set()
    rows = []
    for source in sources:
        path = source.label.split(":", 1)[0]
        parts = counter.analyse_sentences(source.text, allow_fragments=source.allow_fragments)
        if parts is None:
            continue
        for part in parts:
            key = (path, part.text)
            if key in seen:
                continue
            seen.add(key)
            rows.append((path, part))
    return rows


def percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.0f}%" if whole else "-"


def render(rows, top: int) -> str:
    originals = original_works()
    by_group = defaultdict(list)
    by_file = defaultdict(list)
    for path, part in rows:
        by_group[group_of(path, originals)].append(part)
        by_file[path].append(part)

    lines = ["# Phrase-reading audit", ""]
    lines += [
        "| Corpus | Sentences | More than one reading | Four or more | "
        "More than one, full count | Outside canonical order | Not modelled |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    order = [name for name, _ in GROUPS]
    for name in order:
        parts = by_group.get(name)
        if not parts:
            continue
        total = len(parts)
        many = sum(1 for p in parts if p.conservative > 1)
        four = sum(1 for p in parts if p.conservative >= 4)
        wide = sum(1 for p in parts if p.full > 1)
        relaxed = sum(1 for p in parts if any(c.relaxed for c in p.clauses))
        missed = sum(1 for p in parts if p.unmodelled)
        lines.append(
            f"| {name} | {total} | {many} ({percent(many, total)}) | "
            f"{four} ({percent(four, total)}) | {wide} ({percent(wide, total)}) | "
            f"{relaxed} ({percent(relaxed, total)}) | {missed} ({percent(missed, total)}) |"
        )

    seam_counts: Counter[str] = Counter()
    ambiguous_clauses = 0
    join_counts: Counter[str] = Counter()
    join_total: Counter[str] = Counter()
    for _, part in rows:
        for clause in part.clauses:
            if clause.conservative > 1 and clause.seams:
                ambiguous_clauses += 1
                seam_counts.update(clause.seams)
        for join in part.joins:
            join_total[join.kind] += 1
            if join.alternatives > 1:
                join_counts[join.kind] += 1

    lines += ["", "## Where the open seams are", ""]
    lines.append(
        f"Clauses with more than one division, conservative count: {ambiguous_clauses}. "
        "A clause may show several kinds."
    )
    lines += ["", "| Kind of seam | Clauses |", "|---|---:|"]
    for kind, count in seam_counts.most_common():
        lines.append(f"| {kind} | {count} |")
    lines += ["", "| Dependent clause | With more than one possible end | Of |", "|---|---:|---:|"]
    for kind in ("adverbial", "relative"):
        lines.append(f"| {kind} | {join_counts[kind]} | {join_total[kind]} |")

    lines += ["", "## By text", "", "| File | Sentences | More than one reading | Full count |", "|---|---:|---:|---:|"]
    for path in sorted(by_file):
        if not path.startswith("texts/"):
            continue
        parts = by_file[path]
        total = len(parts)
        many = sum(1 for p in parts if p.conservative > 1)
        wide = sum(1 for p in parts if p.full > 1)
        lines.append(
            f"| `{path}` | {total} | {many} ({percent(many, total)}) | "
            f"{wide} ({percent(wide, total)}) |"
        )

    lines += ["", f"## The {top} sentences with the most readings", ""]
    ranked = sorted(rows, key=lambda row: (-row[1].conservative, row[0], row[1].text))[:top]
    for path, part in ranked:
        lines.append(f"- {part.conservative} readings, `{path}`: `{part.text}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paths", nargs="+", help="active Markdown paths; default is everything")
    parser.add_argument("--sentence", help="count one literal Phi sentence and show its divisions")
    parser.add_argument("--output", type=Path, help="write the report here")
    parser.add_argument("--top", type=int, default=20, help="how many sentences to list")
    parser.add_argument(
        "--openers",
        nargs="+",
        default=[],
        help="what-if: count as though these Slot 2 words always began a new phrase",
    )
    args = parser.parse_args()

    if args.sentence is not None:
        counter = ReadingCounter(openers=frozenset(args.openers))
        parts = counter.analyse_sentences(args.sentence)
        if parts is None:
            print("The sentence does not parse.")
            return 1
        for part in parts:
            print(f"{part.text}")
            print(f"  readings: {part.conservative} conservative, {part.full} full")
            for join in part.joins:
                print(
                    f"  {join.kind} clause opened by '{join.opener}': "
                    f"{join.alternatives} possible end(s)"
                )
            for clause in part.clauses:
                if clause.conservative < 2:
                    continue
                print(f"  clause: {clause.text}")
                for division in clause.divisions:
                    print(f"    {division}")
                if clause.seams:
                    print(f"    open seams: {', '.join(clause.seams)}")
        return 0

    text = render(collect(args.paths, frozenset(args.openers)), args.top)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
