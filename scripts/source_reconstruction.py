#!/usr/bin/env python3
"""Verify ordered translation citations against independent source witnesses."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from translation_layers import parse_interlinear_units


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_FILE = ROOT / "project" / "source_reconstruction_manifest.json"
FORMAT = "phi-source-reconstruction-v1"
NORMALIZATION = "gutenberg-wrapped-prose-v1"
LABEL_RE = re.compile(r"[a-z][a-z0-9-]*")
DOCUMENT_FIELDS = {
    "translation",
    "source",
    "citation_label",
    "selection",
    "normalization",
}
SELECTION_FIELDS = {"start_after", "end_before"}
MANIFEST_FIELDS = {"format", "required_translation_globs", "documents"}


@dataclass(frozen=True)
class ReconstructionResult:
    translation: str
    citation_count: int
    normalized_characters: int


def load_manifest(path: Path = MANIFEST_FILE):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_gutenberg_prose(text: str) -> str:
    """Undo Project Gutenberg line wrapping and collapse layout whitespace."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"^\[Illustration: [^\]]+\][ \t]*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"-\n(?=[A-Za-z])", "-", text)
    return " ".join(text.split())


def repository_file(root: Path, value, role: str) -> tuple[Path | None, str | None]:
    if not isinstance(value, str) or not value:
        return None, f"{role} must be a non-empty repository-relative path"
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        return None, f"{role} must stay inside the repository: {value!r}"
    root = root.resolve()
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None, f"{role} must stay inside the repository: {value!r}"
    if not candidate.is_file():
        return None, f"{role} does not exist: {value}"
    return candidate, None


def marker_match(text: str, marker: str):
    pattern = re.compile(rf"^{re.escape(marker)}$", re.M)
    return list(pattern.finditer(text))


def select_source(
    text: str, selection: dict, context: str
) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    if not isinstance(selection, dict):
        return None, [f"{context}: selection must be an object"]
    missing = sorted(SELECTION_FIELDS - set(selection))
    extra = sorted(set(selection) - SELECTION_FIELDS)
    if missing:
        errors.append(f"{context}: selection is missing {', '.join(missing)}")
    if extra:
        errors.append(f"{context}: selection has unknown fields: {', '.join(extra)}")
    if errors:
        return None, errors

    start_marker = selection["start_after"]
    end_marker = selection["end_before"]
    if not isinstance(start_marker, str) or not start_marker:
        errors.append(f"{context}: start_after must be a non-empty string")
    if not isinstance(end_marker, str) or not end_marker:
        errors.append(f"{context}: end_before must be a non-empty string")
    if errors:
        return None, errors

    starts = marker_match(text, start_marker)
    ends = marker_match(text, end_marker)
    if len(starts) != 1:
        errors.append(
            f"{context}: start marker must occur once, found {len(starts)}: {start_marker!r}"
        )
    if len(ends) != 1:
        errors.append(
            f"{context}: end marker must occur once, found {len(ends)}: {end_marker!r}"
        )
    if errors:
        return None, errors
    if starts[0].end() >= ends[0].start():
        return None, [f"{context}: source markers are reversed or overlap"]
    return text[starts[0].end():ends[0].start()], []


def excerpt(text: str, limit: int = 96) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def contains_span(stream: str, span: str) -> bool:
    if not span:
        return False
    return (
        stream == span
        or stream.startswith(span + " ")
        or stream.endswith(" " + span)
        or f" {span} " in stream
    )


def reconstruction_error(
    expected: str, fragments: list[str], context: str
) -> str | None:
    cursor = 0
    for index, fragment in enumerate(fragments):
        separator = "" if index == 0 else " "
        piece = separator + fragment
        if expected.startswith(piece, cursor):
            cursor += len(piece)
            continue

        citation_number = index + 1
        later_citations = " ".join(fragments[index + 1:])
        if fragment in fragments[:index]:
            return (
                f"{context}: duplicated source span at citation {citation_number}: "
                f"{excerpt(fragment)!r}"
            )

        forward = expected.find(piece, cursor + 1)
        if forward != -1:
            skipped = expected[cursor:forward].strip()
            if contains_span(later_citations, skipped):
                return (
                    f"{context}: reordered source spans at citation {citation_number}: "
                    f"expected {excerpt(skipped)!r} before {excerpt(fragment)!r}"
                )
            return (
                f"{context}: missing source span before citation {citation_number}: "
                f"{excerpt(skipped)!r}"
            )

        prior = expected.rfind(piece, 0, cursor)
        if prior != -1:
            return (
                f"{context}: reordered source span at citation {citation_number}: "
                f"{excerpt(fragment)!r} belongs before the current position"
            )

        expected_near = expected[cursor:cursor + max(len(piece), 48)].strip()
        return (
            f"{context}: altered source text at citation {citation_number}: "
            f"expected near {excerpt(expected_near)!r}, found {excerpt(fragment)!r}"
        )

    if cursor < len(expected):
        return f"{context}: missing trailing source span: {excerpt(expected[cursor:])!r}"
    return None


def check_manifest(data, root: Path = ROOT) -> tuple[list[ReconstructionResult], list[str]]:
    results: list[ReconstructionResult] = []
    errors: list[str] = []
    if not isinstance(data, dict):
        return results, ["source reconstruction manifest must be an object"]
    missing_manifest_fields = sorted(MANIFEST_FIELDS - set(data))
    extra_manifest_fields = sorted(set(data) - MANIFEST_FIELDS)
    if missing_manifest_fields:
        errors.append(
            "manifest is missing fields: " + ", ".join(missing_manifest_fields)
        )
    if extra_manifest_fields:
        errors.append(
            "manifest has unknown fields: " + ", ".join(extra_manifest_fields)
        )
    if data.get("format") != FORMAT:
        errors.append(f"format must be {FORMAT!r}")
    required_globs = data.get("required_translation_globs")
    required_translations: set[str] = set()
    if not isinstance(required_globs, list) or not required_globs:
        errors.append("required_translation_globs must be a non-empty list")
    else:
        for pattern in required_globs:
            if not isinstance(pattern, str) or not pattern:
                errors.append("every required translation glob must be a non-empty string")
                continue
            relative_pattern = Path(pattern)
            if relative_pattern.is_absolute() or ".." in relative_pattern.parts:
                errors.append(
                    f"required translation glob must stay inside the repository: {pattern!r}"
                )
                continue
            matches = sorted(path for path in root.glob(pattern) if path.is_file())
            if not matches:
                errors.append(f"required translation glob matches no files: {pattern!r}")
                continue
            for match in matches:
                resolved = match.resolve()
                try:
                    relative = resolved.relative_to(root.resolve()).as_posix()
                except ValueError:
                    errors.append(
                        f"required translation glob leaves the repository: {pattern!r}"
                    )
                    continue
                required_translations.add(relative)
    documents = data.get("documents")
    if not isinstance(documents, list) or not documents:
        return results, [*errors, "documents must be a non-empty list"]

    translations: list[str] = []
    for index, document in enumerate(documents, start=1):
        context = f"manifest document {index}"
        if not isinstance(document, dict):
            errors.append(f"{context}: entry must be an object")
            continue
        translation_value = document.get("translation")
        if isinstance(translation_value, str) and translation_value:
            context = translation_value
            translations.append(translation_value)

        missing = sorted(DOCUMENT_FIELDS - set(document))
        extra = sorted(set(document) - DOCUMENT_FIELDS)
        if missing:
            errors.append(f"{context}: missing fields: {', '.join(missing)}")
        if extra:
            errors.append(f"{context}: unknown fields: {', '.join(extra)}")
        if missing or extra:
            continue

        label = document["citation_label"]
        if not isinstance(label, str) or LABEL_RE.fullmatch(label) is None:
            errors.append(f"{context}: citation_label is invalid: {label!r}")
            continue
        if document["normalization"] != NORMALIZATION:
            errors.append(
                f"{context}: unsupported normalization {document['normalization']!r}"
            )
            continue

        translation_path, translation_error = repository_file(
            root, document["translation"], "translation"
        )
        source_path, source_error = repository_file(root, document["source"], "source")
        if translation_error:
            errors.append(f"{context}: {translation_error}")
        if source_error:
            errors.append(f"{context}: {source_error}")
        if translation_path is None or source_path is None:
            continue

        selected, selection_errors = select_source(
            source_path.read_text(encoding="utf-8"), document["selection"], context
        )
        errors.extend(selection_errors)
        if selected is None:
            continue
        expected = normalize_gutenberg_prose(selected)
        if not expected:
            errors.append(f"{context}: selected source is empty after normalization")
            continue

        try:
            units = parse_interlinear_units(
                translation_path.read_text(encoding="utf-8")
            )
        except ValueError as exc:
            errors.append(f"{context}: cannot decode citations: {exc}")
            continue
        if not units:
            errors.append(f"{context}: no aligned translation units found")
            continue

        fragments: list[str] = []
        missing_label_units: list[int] = []
        for unit_number, unit in enumerate(units, start=1):
            witnesses = [
                witness
                for source_label, witness in unit.sources
                if source_label == label
            ]
            if not witnesses:
                missing_label_units.append(unit_number)
            fragments.extend(normalize_gutenberg_prose(witness) for witness in witnesses)
        if missing_label_units:
            listed = ", ".join(str(number) for number in missing_label_units[:8])
            suffix = "..." if len(missing_label_units) > 8 else ""
            errors.append(
                f"{context}: {len(missing_label_units)} translation unit(s) lack "
                f"citation label {label!r}: {listed}{suffix}"
            )
            continue
        if any(not fragment for fragment in fragments):
            errors.append(f"{context}: citation label {label!r} has an empty witness")
            continue

        mismatch = reconstruction_error(expected, fragments, context)
        if mismatch:
            errors.append(mismatch)
            continue
        results.append(
            ReconstructionResult(
                translation=document["translation"],
                citation_count=len(fragments),
                normalized_characters=len(expected),
            )
        )

    duplicates = sorted(
        translation
        for translation in set(translations)
        if translations.count(translation) > 1
    )
    for translation in duplicates:
        errors.append(f"duplicate translation in manifest: {translation}")
    for translation in sorted(required_translations - set(translations)):
        errors.append(f"missing source reconstruction manifest entry: {translation}")
    return results, errors


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MANIFEST_FILE,
        help="manifest to check",
    )
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        data = load_manifest(args.manifest)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read source reconstruction manifest: {exc}", file=sys.stderr)
        return 1
    results, errors = check_manifest(data)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(
        f"checked {len(results)} source reconstruction(s): "
        f"{sum(result.citation_count for result in results)} citations, "
        f"{sum(result.normalized_characters for result in results):,} "
        "normalized source characters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
