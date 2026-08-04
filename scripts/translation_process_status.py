#!/usr/bin/env python3
"""Validate and publish the isolated-translation certification register."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from translation_layers import parse_units, phi_digest


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "project" / "translation_process_status.json"
REPORT_FILE = ROOT / "documents" / "evaluation" / "translation_process_status.md"
FORMAT = "phi-isolated-translation-status-v1"
STATUSES = ("pending", "in-progress", "certified")
STATUS_LABELS = {
    "pending": "Pending",
    "in-progress": "In progress",
    "certified": "Certified",
}
SHA256_RE = re.compile(r"[0-9a-f]{64}")
DECISION_RE = re.compile(r"D[0-9]{3,}")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


@dataclass(frozen=True)
class ExpectedDocument:
    path: str
    title: str
    group: str


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_data(path: Path = DATA_FILE):
    return load_json(path)


def aligned_records(markdown: str) -> list[dict]:
    """Return the published Phi, gloss, English, and source layers."""
    payload = []
    fence_re = re.compile(r"```[^\n]*\n(.*?)\n```", re.S)
    source_re = re.compile(r"([a-z][a-z0-9-]*):\s*(.+)", re.S)
    for fence in fence_re.findall(markdown):
        for group in re.split(r"\n[ \t]*\n", fence.strip()):
            lines = [line.strip() for line in group.splitlines()]
            if len(lines) < 4 or not (lines[2].startswith("(") and lines[2].endswith(")")):
                continue
            sources = []
            for line in lines[3:]:
                match = source_re.fullmatch(line)
                if match is None:
                    sources = []
                    break
                try:
                    witness = json.loads(match.group(2))
                except json.JSONDecodeError:
                    sources = []
                    break
                if not isinstance(witness, str):
                    sources = []
                    break
                sources.append([match.group(1), witness])
            if sources:
                payload.append(
                    {
                        "phi": lines[0],
                        "gloss": lines[1],
                        "english": lines[2],
                        "sources": sources,
                    }
                )
    return payload


def aligned_digest(markdown: str) -> str:
    """Hash the published Phi, gloss, English, and source layers."""
    serialized = json.dumps(
        aligned_records(markdown), ensure_ascii=False, separators=(",", ":")
    ) + "\n"
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def normalized_source_characters(records: list[dict], label: str) -> int:
    source = " ".join(
        witness
        for record in records
        for source_label, witness in record["sources"]
        if source_label == label
    )
    return len(" ".join(source.split()))


def chapter_title(path: Path) -> str:
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    if not first_line.startswith("# "):
        raise ValueError(f"{path.relative_to(ROOT)} has no level-one title")
    return first_line[2:].strip()


def discover_documents(data, root: Path = ROOT) -> list[ExpectedDocument]:
    catalogue = load_json(root / "texts" / "catalogue.json")
    book_relationships = data.get("book_relationships", {})
    discovered: list[ExpectedDocument] = []

    if not isinstance(book_relationships, dict):
        raise ValueError("book_relationships must be an object")

    catalogue_books = {
        work["path"] for work in catalogue.get("works", []) if work.get("kind") == "book"
    }
    if set(book_relationships) != catalogue_books:
        missing = sorted(catalogue_books - set(book_relationships))
        extra = sorted(set(book_relationships) - catalogue_books)
        pieces = []
        if missing:
            pieces.append("undeclared books: " + ", ".join(missing))
        if extra:
            pieces.append("unknown books: " + ", ".join(extra))
        raise ValueError("book_relationships must cover every catalogued book (" + "; ".join(pieces) + ")")

    for work in catalogue.get("works", []):
        kind = work.get("kind")
        method = work.get("method")
        relative = work.get("path")
        title = work.get("title")

        if kind == "short" and method == "Translation":
            discovered.append(ExpectedDocument(f"texts/{relative}", title, "Short works"))
            continue

        if kind == "collection" and method == "Translation":
            members = load_json(root / "texts" / relative / "catalogue.json")
            for member in members.get("works", []):
                if member.get("method") != "Translation":
                    continue
                discovered.append(
                    ExpectedDocument(
                        f"texts/{relative}/{member['path']}",
                        member["title"],
                        title,
                    )
                )
            continue

        if kind == "book":
            relationship = book_relationships[relative]
            if relationship == "not-applicable":
                continue
            if relationship != "translation":
                raise ValueError(f"invalid relationship for book {relative}: {relationship!r}")
            directory = root / "texts" / relative
            chapters = sorted(directory.glob("chapter_*.md"))
            if not chapters:
                raise ValueError(f"translation book has no chapter documents: texts/{relative}")
            for chapter in chapters:
                discovered.append(
                    ExpectedDocument(
                        chapter.relative_to(root).as_posix(),
                        chapter_title(chapter),
                        title,
                    )
                )

    return discovered


def validate(data, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if data.get("format") != FORMAT:
        errors.append(f"format must be {FORMAT!r}")

    try:
        expected = discover_documents(data, root)
    except (KeyError, TypeError, ValueError) as exc:
        return [str(exc)]

    documents = data.get("documents")
    if not isinstance(documents, list):
        return [*errors, "documents must be a list"]

    expected_paths = [item.path for item in expected]
    actual_paths = [item.get("path") for item in documents if isinstance(item, dict)]
    duplicate_paths = sorted(
        (path for path, count in Counter(actual_paths).items() if count > 1),
        key=lambda value: str(value),
    )
    for path in duplicate_paths:
        errors.append(f"duplicate document path: {path}")

    missing = [path for path in expected_paths if path not in actual_paths]
    extra = [path for path in actual_paths if path not in expected_paths]
    for path in missing:
        errors.append(f"missing translation document: {path}")
    for path in extra:
        errors.append(f"unscoped translation document: {path}")
    if actual_paths != expected_paths:
        errors.append("documents must follow the catalogue and chapter order")

    for document in documents:
        if not isinstance(document, dict):
            errors.append("every document entry must be an object")
            continue
        path = document.get("path")
        status = document.get("status")
        if status not in STATUSES:
            errors.append(f"{path}: invalid status {status!r}")
            continue
        if path not in expected_paths:
            continue

        certification = document.get("certification")
        if status != "certified":
            if certification is not None:
                errors.append(f"{path}: only certified documents may carry certification evidence")
            if status == "in-progress":
                note = document.get("note")
                if not isinstance(note, str) or not note.strip():
                    errors.append(f"{path}: in-progress documents need a note")
            continue
        if not isinstance(certification, dict):
            errors.append(f"{path}: certified documents need certification evidence")
            continue

        decision = certification.get("decision")
        pull_request = certification.get("pull_request")
        certified_on = certification.get("certified_on")
        unit_count = certification.get("unit_count")
        digest = certification.get("phi_sha256")
        published_digest = certification.get("aligned_sha256")
        reconstruction = certification.get("source_reconstruction")
        derivation = certification.get("english_derivation")
        note = certification.get("note")

        if not isinstance(decision, str) or DECISION_RE.fullmatch(decision) is None:
            errors.append(f"{path}: certification decision must look like D103")
        if not isinstance(pull_request, int) or pull_request < 1:
            errors.append(f"{path}: certification pull_request must be a positive integer")
        if not isinstance(certified_on, str) or DATE_RE.fullmatch(certified_on) is None:
            errors.append(f"{path}: certified_on must use YYYY-MM-DD")
        else:
            try:
                date.fromisoformat(certified_on)
            except ValueError:
                errors.append(f"{path}: certified_on is not a real calendar date")
        if not isinstance(unit_count, int) or unit_count < 1:
            errors.append(f"{path}: unit_count must be a positive integer")
        if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
            errors.append(f"{path}: phi_sha256 must be a lowercase SHA-256 digest")
        if not isinstance(published_digest, str) or SHA256_RE.fullmatch(published_digest) is None:
            errors.append(f"{path}: aligned_sha256 must be a lowercase SHA-256 digest")
        if derivation != "fresh-source-blind-context":
            errors.append(f"{path}: english_derivation must record a fresh source-blind context")
        if not isinstance(note, str) or not note.strip():
            errors.append(f"{path}: certification note must be non-empty")
        if isinstance(decision, str) and DECISION_RE.fullmatch(decision) is not None:
            log = (root / "project" / "development_log.md").read_text(encoding="utf-8")
            if f"| {decision} | Accepted |" not in log:
                errors.append(f"{path}: certification decision is not accepted in the development log")
        if not isinstance(reconstruction, dict):
            errors.append(f"{path}: source_reconstruction must be an object")
        else:
            if reconstruction.get("exact") is not True:
                errors.append(f"{path}: source reconstruction must be exact")
            label = reconstruction.get("label")
            if not isinstance(label, str) or re.fullmatch(r"[a-z][a-z0-9-]*", label) is None:
                errors.append(f"{path}: source reconstruction needs a valid citation label")
            characters = reconstruction.get("normalized_characters")
            if not isinstance(characters, int) or characters < 1:
                errors.append(f"{path}: normalized source character count must be positive")

        file_path = root / path if isinstance(path, str) else None
        if file_path is None or not file_path.is_file():
            errors.append(f"{path}: certified document does not exist")
            continue
        try:
            units = parse_units(file_path.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{path}: cannot read translation units: {exc}")
            continue
        if not units:
            errors.append(f"{path}: no aligned translation units found")
            continue
        if isinstance(unit_count, int) and unit_count != len(units):
            errors.append(f"{path}: expected {unit_count} units, found {len(units)}")
        actual_digest = phi_digest(units)
        if isinstance(digest, str) and digest != actual_digest:
            errors.append(f"{path}: frozen Phi digest is stale; found {actual_digest}")
        markdown = file_path.read_text(encoding="utf-8")
        published_records = aligned_records(markdown)
        if len(published_records) != len(units):
            errors.append(
                f"{path}: expected {len(units)} complete published layer sets, "
                f"found {len(published_records)}"
            )
        if isinstance(reconstruction, dict):
            label = reconstruction.get("label")
            characters = reconstruction.get("normalized_characters")
            actual_characters = (
                normalized_source_characters(published_records, label)
                if isinstance(label, str)
                else 0
            )
            missing_label_count = (
                sum(
                    not any(source_label == label for source_label, _witness in record["sources"])
                    for record in published_records
                )
                if isinstance(label, str)
                else 0
            )
            if isinstance(label, str) and actual_characters == 0:
                errors.append(f"{path}: no published citations use source label {label!r}")
            elif missing_label_count:
                errors.append(
                    f"{path}: {missing_label_count} published units lack source label {label!r}"
                )
            elif isinstance(characters, int) and characters != actual_characters:
                errors.append(
                    f"{path}: expected {characters} normalized source characters, "
                    f"found {actual_characters} in the citations"
                )
        actual_published_digest = aligned_digest(markdown)
        if isinstance(published_digest, str) and published_digest != actual_published_digest:
            errors.append(
                f"{path}: published aligned-layer digest is stale; found {actual_published_digest}"
            )

    return errors


def clean_cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(data, root: Path = ROOT) -> str:
    expected = discover_documents(data, root)
    documents = {item["path"]: item for item in data["documents"]}
    counts = Counter(item["status"] for item in data["documents"])
    total = len(data["documents"])
    lines = [
        "# Isolated translation certification",
        "",
        "This ledger records which Phi translations have completed the isolated process. An earlier fidelity review does not count as certification. The machine-readable register is `project/translation_process_status.json`. The catalogue supplies the standalone works and Gibran selections, while the chapter files supply the present *News from Nowhere* sequence. CI rejects a missing row, an extra row, a stale report, or a certified work whose unit count or digest has changed.",
        "",
        "A pending translation may still be accurate and carefully reviewed. Pending means only that its English was not demonstrably derived in a fresh source-blind context after the Phi was frozen. Originals and the Ring Verse refusal are outside this queue because they make a different promise to the reader.",
        "",
        "[What certified means](../reference/translation_certification.md) gives the public account of the mark, including its limits. The complete working procedure is described in [How a Phi translation is made](../reference/translation_process.md).",
        "",
        "## Current state",
        "",
        "| State | Documents |",
        "|---|---:|",
        f"| Certified | {counts['certified']} |",
        f"| In progress | {counts['in-progress']} |",
        f"| Pending | {counts['pending']} |",
        f"| Total | {total} |",
    ]

    groups: list[str] = []
    for item in expected:
        if item.group not in groups:
            groups.append(item.group)
    for group in groups:
        members = [item for item in expected if item.group == group]
        certified = sum(documents[item.path]["status"] == "certified" for item in members)
        lines.extend(
            [
                "",
                f"## {group}",
                "",
                f"Certified: {certified} of {len(members)}.",
                "",
                "| Document | File | State | Record |",
                "|---|---|---|---|",
            ]
        )
        for item in members:
            document = documents[item.path]
            status = document["status"]
            link = Path(item.path).relative_to("texts")
            report_link = Path("../../texts") / link
            if status == "certified":
                evidence = document["certification"]
                record = (
                    f"{evidence['decision']}; "
                    f"[PR #{evidence['pull_request']}](https://github.com/dcellison/phi/pull/{evidence['pull_request']}); "
                    f"{evidence['unit_count']} units"
                )
            elif status == "in-progress":
                record = clean_cell(document["note"])
            else:
                record = "Awaiting D102 certification."
            lines.append(
                f"| {clean_cell(item.title)} | [{clean_cell(Path(item.path).name)}]({report_link.as_posix()}) | "
                f"{STATUS_LABELS[status]} | {record} |"
            )

    certified_documents = [
        (item, documents[item.path]["certification"])
        for item in expected
        if documents[item.path]["status"] == "certified"
    ]
    if certified_documents:
        lines.extend(["", "## Certification records"])
        for item, evidence in certified_documents:
            reconstruction = evidence["source_reconstruction"]
            lines.extend(
                [
                    "",
                    f"### {item.title}",
                    "",
                    f"{evidence['decision']} certified this document in [PR #{evidence['pull_request']}](https://github.com/dcellison/phi/pull/{evidence['pull_request']}) on {evidence['certified_on']}. The freeze contains {evidence['unit_count']} aligned Phi units, and its `{reconstruction['label']}` citations reconstruct {reconstruction['normalized_characters']:,} normalized source characters exactly. {evidence['note']}",
                    "",
                    "Frozen Phi SHA-256:",
                    "",
                    "```text",
                    evidence["phi_sha256"],
                    "```",
                    "",
                    "Published aligned-layer SHA-256:",
                    "",
                    "```text",
                    evidence["aligned_sha256"],
                    "```",
                ]
            )

    lines.extend(
        [
            "",
            "## Maintaining the ledger",
            "",
            "Run `python3 scripts/translation_process_status.py --write` after changing a status or adding a translation. Run `python3 scripts/translation_process_status.py --check` before publication. Changing certified Phi invalidates its English. CI will fail until the English has been derived again from a new anonymous packet and the new freeze has its own evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write the Markdown view")
    mode.add_argument("--check", action="store_true", help="check data and generated view")
    args = parser.parse_args()

    data = load_data()
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    expected = render(data)
    if args.write:
        REPORT_FILE.write_text(expected, encoding="utf-8")
        print(f"wrote {REPORT_FILE.relative_to(ROOT)}")
        return 0
    if not REPORT_FILE.is_file() or REPORT_FILE.read_text(encoding="utf-8") != expected:
        print(
            "ERROR: documents/evaluation/translation_process_status.md is stale; "
            "run python3 scripts/translation_process_status.py --write",
            file=sys.stderr,
        )
        return 1
    counts = Counter(item["status"] for item in data["documents"])
    print(
        f"checked {len(data['documents'])} translations: "
        f"{counts['certified']} certified, {counts['in-progress']} in progress, "
        f"{counts['pending']} pending"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
