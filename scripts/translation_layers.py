#!/usr/bin/env python3
"""Extract isolated working views from a literary translation."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


FENCE_RE = re.compile(r"```[^\n]*\n(.*?)\n```", re.S)
SOURCE_RE = re.compile(r"([a-z][a-z0-9-]*):\s*(.+)", re.S)
WORKING_SOURCE_RE = re.compile(r"- `([a-z][a-z0-9-]*)`:\s*(.+)")


@dataclass(frozen=True)
class TranslationUnit:
    phi: str
    sources: tuple[tuple[str, str], ...]


def parse_interlinear_units(markdown: str) -> list[TranslationUnit]:
    units: list[TranslationUnit] = []
    for fence in FENCE_RE.findall(markdown):
        for group in re.split(r"\n[ \t]*\n", fence.strip()):
            lines = [line.strip() for line in group.splitlines()]
            if len(lines) < 4:
                continue
            if not (lines[2].startswith("(") and lines[2].endswith(")")):
                continue

            matches = [SOURCE_RE.fullmatch(line) for line in lines[3:]]
            if not matches or any(match is None for match in matches):
                continue

            sources: list[tuple[str, str]] = []
            for match in matches:
                assert match is not None
                try:
                    witness = json.loads(match.group(2))
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"invalid {match.group(1)} source witness: {match.group(2)}"
                    ) from exc
                if not isinstance(witness, str):
                    raise ValueError(
                        f"{match.group(1)} source witness is not a string"
                    )
                sources.append((match.group(1), witness))
            units.append(TranslationUnit(lines[0], tuple(sources)))
    return units


def parse_source_to_phi_units(markdown: str) -> list[TranslationUnit]:
    units: list[TranslationUnit] = []
    chunks = re.split(r"(?m)^## Unit \d+\s*$", markdown)[1:]
    for chunk in chunks:
        phi_match = re.search(r"(?s)\nPhi:\s*\n+```\n(.*?)\n```", chunk)
        if phi_match is None or "\nSource:\n" not in chunk:
            continue
        source_section = chunk.split("\nSource:\n", 1)[1]
        sources: list[tuple[str, str]] = []
        for line in source_section.splitlines():
            match = WORKING_SOURCE_RE.fullmatch(line.strip())
            if match is None:
                continue
            try:
                witness = json.loads(match.group(2))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"invalid {match.group(1)} source witness: {match.group(2)}"
                ) from exc
            if not isinstance(witness, str):
                raise ValueError(
                    f"{match.group(1)} source witness is not a string"
                )
            sources.append((match.group(1), witness))
        if not sources:
            continue
        units.append(TranslationUnit(phi_match.group(1).strip(), tuple(sources)))
    return units


def parse_units(markdown: str) -> list[TranslationUnit]:
    units = parse_interlinear_units(markdown)
    if units:
        return units
    return parse_source_to_phi_units(markdown)


def phi_digest(units: list[TranslationUnit]) -> str:
    stream = "\n\n".join(unit.phi for unit in units) + "\n"
    return hashlib.sha256(stream.encode("utf-8")).hexdigest()


def source_to_phi_view(path: Path, units: list[TranslationUnit]) -> str:
    parts = [
        "# Source-to-Phi working view",
        "",
        f"Input: `{path.as_posix()}`",
        f"Units: {len(units)}",
        f"Phi SHA-256: `{phi_digest(units)}`",
        "",
        "This view omits glosses, parenthetical English, notes, and limits.",
    ]
    for index, unit in enumerate(units, 1):
        parts.extend(
            [
                "",
                f"## Unit {index:03d}",
                "",
                "Phi:",
                "",
                "```",
                unit.phi,
                "```",
                "",
                "Source:",
            ]
        )
        for label, witness in unit.sources:
            parts.append(f"- `{label}`: {json.dumps(witness, ensure_ascii=False)}")
    return "\n".join(parts) + "\n"


def phi_to_english_view(units: list[TranslationUnit]) -> str:
    parts = [
        "# Phi-only English-derivation packet",
        "",
        f"Units: {len(units)}",
        f"Frozen Phi SHA-256: `{phi_digest(units)}`",
        "",
        "The source, citations, prior English, glosses, notes, and limits are intentionally absent.",
    ]
    for index, unit in enumerate(units, 1):
        parts.extend(
            [
                "",
                f"## Unit {index:03d}",
                "",
                "```",
                unit.phi,
                "```",
            ]
        )
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract an isolated translation phase from a texts Markdown file."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--phase",
        choices=("source-to-phi", "phi-to-english"),
        help="working view to render",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--digest-only",
        action="store_true",
        help="print only the SHA-256 of the aligned Phi stream",
    )
    args = parser.parse_args()

    if args.phase is None and not args.digest_only:
        parser.error("--phase is required unless --digest-only is used")

    units = parse_units(args.path.read_text(encoding="utf-8"))
    if not units:
        parser.error(f"no source-aligned translation units found in {args.path}")

    if args.digest_only:
        rendered = phi_digest(units) + "\n"
    elif args.phase == "source-to-phi":
        rendered = source_to_phi_view(args.path, units)
    else:
        rendered = phi_to_english_view(units)

    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {args.output}: {len(units)} units, {phi_digest(units)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
