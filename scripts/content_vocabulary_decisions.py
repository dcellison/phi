#!/usr/bin/env python3
"""Validate and publish the content-vocabulary decision register."""

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "project" / "content_vocabulary_decisions.json"
REPORT_FILE = ROOT / "project" / "content_vocabulary_decisions.md"
COVERAGE_FILE = ROOT / "project" / "content_vocabulary_coverage.md"
FORMAT = "phi-content-vocabulary-decisions-v1"
DECISION_STATUSES = {
    "open",
    "accepted",
    "implemented",
    "compositional",
    "deferred",
    "source-bound",
    "declined",
}
UNRESOLVED_STATUSES = {"open", "accepted"}
STATUS_LABELS = {
    "open": "Open",
    "accepted": "Accepted, not implemented",
    "implemented": "Implemented",
    "compositional": "Compositional",
    "deferred": "Deferred",
    "source-bound": "Source-bound",
    "declined": "Declined",
}


def slugify(heading):
    return re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")


def load_data(path=DATA_FILE):
    return json.loads(path.read_text(encoding="utf-8"))


def coverage_batch_headings(text):
    try:
        body = text.split("## Core material qualities", 1)[1]
        body = body.split("## Resolved review decisions", 1)[0]
    except IndexError:
        return []
    return ["Core material qualities", *re.findall(r"^## (.+)$", body, re.M)]


def coverage_decision_rows(text):
    try:
        body = text.split("## Core material qualities", 1)[1]
        body = body.split("## Resolved review decisions", 1)[0]
    except IndexError:
        return []
    return [
        line
        for line in body.splitlines()
        if line.startswith("|")
        and ("**REVIEW**" in line or "**DEFERRED**" in line)
    ]


def validate(data, root=ROOT, coverage_text=None):
    errors = []
    if data.get("format") != FORMAT:
        errors.append(f"format must be {FORMAT!r}")

    batches = data.get("batches")
    candidates = data.get("candidates")
    if not isinstance(batches, list):
        return [*errors, "batches must be a list"]
    if not isinstance(candidates, list):
        return [*errors, "candidates must be a list"]

    batch_by_id = {}
    for batch in batches:
        batch_id = batch.get("id")
        if not isinstance(batch_id, str) or not batch_id:
            errors.append("every batch needs a non-empty id")
            continue
        if batch_id in batch_by_id:
            errors.append(f"duplicate batch id: {batch_id}")
        batch_by_id[batch_id] = batch
        if batch.get("migration_status") not in {"not-started", "in-progress", "complete"}:
            errors.append(f"{batch_id}: invalid migration_status")
        if batch.get("decision_status") not in {"open", "closed"}:
            errors.append(f"{batch_id}: invalid decision_status")
        if not isinstance(batch.get("candidate_ids"), list):
            errors.append(f"{batch_id}: candidate_ids must be a list")

    candidate_by_id = {}
    for candidate in candidates:
        candidate_id = candidate.get("id")
        if not isinstance(candidate_id, str) or not re.fullmatch(r"CV-[A-Z0-9-]+", candidate_id):
            errors.append(f"invalid candidate id: {candidate_id!r}")
            continue
        if candidate_id in candidate_by_id:
            errors.append(f"duplicate candidate id: {candidate_id}")
        candidate_by_id[candidate_id] = candidate
        status = candidate.get("status")
        if status not in DECISION_STATUSES:
            errors.append(f"{candidate_id}: invalid status {status!r}")
        for field in ("concept", "placement", "summary"):
            if not isinstance(candidate.get(field), str) or not candidate[field].strip():
                errors.append(f"{candidate_id}: {field} must be non-empty prose")
        candidate_batches = candidate.get("batches")
        if not isinstance(candidate_batches, list) or not candidate_batches:
            errors.append(f"{candidate_id}: batches must be a non-empty list")
            candidate_batches = []
        for batch_id in candidate_batches:
            if batch_id not in batch_by_id:
                errors.append(f"{candidate_id}: unknown batch {batch_id}")
            elif candidate_id not in batch_by_id[batch_id].get("candidate_ids", []):
                errors.append(f"{candidate_id}: missing reciprocal link from {batch_id}")

        if status == "open" and not candidate.get("question"):
            errors.append(f"{candidate_id}: open decisions need a question")
        if status == "accepted" and not candidate.get("planned_implementation"):
            errors.append(f"{candidate_id}: accepted decisions need planned_implementation")
        if status == "deferred" and not candidate.get("revisit_when"):
            errors.append(f"{candidate_id}: deferred decisions need revisit_when")
        if status == "source-bound" and not candidate.get("source_rule"):
            errors.append(f"{candidate_id}: source-bound decisions need source_rule")
        if status == "declined" and not candidate.get("decision"):
            errors.append(f"{candidate_id}: declined decisions need a decision")
        if status == "compositional":
            expressions = candidate.get("expressions")
            if not isinstance(expressions, list) or not expressions:
                errors.append(f"{candidate_id}: compositional decisions need expressions")
        implementation = candidate.get("implementation")
        if status == "implemented" and not isinstance(implementation, dict):
            errors.append(f"{candidate_id}: implemented decisions need implementation")
        if isinstance(implementation, dict):
            files = implementation.get("files", [])
            compounds = implementation.get("compounds", [])
            words = implementation.get("words", [])
            if status == "implemented" and not files and not compounds:
                errors.append(f"{candidate_id}: implementation must name files or compounds")
            file_words = []
            for relative in files:
                path = root / relative
                if not path.is_file():
                    errors.append(f"{candidate_id}: implementation file does not exist: {relative}")
                elif path.suffix == ".json":
                    file_words.append(json.loads(path.read_text(encoding="utf-8")).get("word"))
            if words and set(words) != set(file_words):
                errors.append(f"{candidate_id}: implementation words do not match its JSON files")
            if compounds:
                registry = (root / "documents" / "reference" / "compounds.md").read_text(encoding="utf-8")
                for compound in compounds:
                    if f"`{compound}`" not in registry:
                        errors.append(f"{candidate_id}: compound is not registered: {compound}")

    for batch_id, batch in batch_by_id.items():
        ids = batch.get("candidate_ids", [])
        if len(ids) != len(set(ids)):
            errors.append(f"{batch_id}: duplicate candidate id")
        unresolved = []
        for candidate_id in ids:
            candidate = candidate_by_id.get(candidate_id)
            if candidate is None:
                errors.append(f"{batch_id}: unknown candidate {candidate_id}")
                continue
            if batch_id not in candidate.get("batches", []):
                errors.append(f"{batch_id}: missing reciprocal link from {candidate_id}")
            if candidate.get("status") in UNRESOLVED_STATUSES:
                unresolved.append(candidate_id)
        if unresolved and batch.get("decision_status") == "closed":
            errors.append(f"{batch_id}: closed with unresolved decisions: {', '.join(unresolved)}")
        if not unresolved and batch.get("decision_status") == "open":
            errors.append(f"{batch_id}: open without an open or accepted decision")

    coverage_text = coverage_text if coverage_text is not None else COVERAGE_FILE.read_text(encoding="utf-8")
    expected_headings = coverage_batch_headings(coverage_text)
    actual_headings = [batch.get("heading") for batch in batches]
    if expected_headings != actual_headings:
        errors.append("batch headings or order differ from project/content_vocabulary_coverage.md")

    for row in coverage_decision_rows(coverage_text):
        markers = re.findall(r"\bCV-[A-Z0-9-]+\b", row)
        if not markers:
            errors.append(f"unregistered REVIEW or DEFERRED row: {row[:100]}")
        for marker in markers:
            if marker not in candidate_by_id:
                errors.append(f"coverage row references unknown decision: {marker}")

    return errors


def clean_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def candidate_outcome(candidate):
    status = candidate["status"]
    if status == "open":
        return candidate["question"]
    if status == "accepted":
        return candidate["planned_implementation"]
    if status == "implemented":
        implementation = candidate["implementation"]
        pieces = []
        if implementation.get("words"):
            pieces.append("Words: " + ", ".join(f"`{word}`" for word in implementation["words"]))
        if implementation.get("compounds"):
            pieces.append("Compounds: " + ", ".join(f"`{item}`" for item in implementation["compounds"]))
        return ". ".join(pieces) + "."
    if status == "compositional":
        return "Use " + ", ".join(f"`{item}`" for item in candidate["expressions"]) + "."
    if status == "deferred":
        return "Revisit when " + candidate["revisit_when"].rstrip(".") + "."
    if status == "source-bound":
        return candidate["source_rule"]
    return candidate["decision"]


def render(data):
    candidates = {candidate["id"]: candidate for candidate in data["candidates"]}
    batches = {batch["id"]: batch for batch in data["batches"]}
    lines = [
        "# Content vocabulary decisions",
        "",
        "This is the readable view of `project/content_vocabulary_decisions.json`. It records every candidate carried forward from the content-vocabulary migration and retrospective audit, including decisions to compose, defer, or keep exact source terminology. The broader coverage ledger retains settled comparisons from each batch. Regenerate this view with `python3 scripts/content_vocabulary_decisions.py --write`; CI checks that the register, the ledger, and the vocabulary remain in step.",
        "",
        "The register is a memory aid, not proof that Phi has no other gaps. An unnoticed concept cannot appear in any inventory. From this repair onward, every potential coinage noticed during a content batch receives an ID here; it stays until it has an explicit decision, and an open or accepted candidate keeps its batch open.",
        "",
        "## Decision statuses",
        "",
        "| Status | Meaning |",
        "|---|---|",
        "| Open | The lexical question still needs a decision. |",
        "| Accepted, not implemented | The decision is made, but its vocabulary or documentation has not landed. |",
        "| Implemented | The accepted word or registered compound exists and is checked. |",
        "| Compositional | Phi deliberately uses existing words or grammar for the concept. |",
        "| Deferred | The question has a named trigger for returning to it. |",
        "| Source-bound | Exact identity or authority stays with outside source terminology while Phi describes the surrounding relations. |",
        "| Declined | Phi deliberately does not add the proposed distinction. |",
        "",
        "## Batch state",
        "",
        "| Batch | Prose migration | Lexical decisions | Candidate count |",
        "|---|---|---|---:|",
    ]
    rendered_ids = set()
    for batch in data["batches"]:
        lines.append(
            f"| [{clean_cell(batch['heading'])}](#{slugify(batch['heading'])}) | "
            f"{clean_cell(batch['migration_status'])} | {clean_cell(batch['decision_status'])} | "
            f"{len(batch['candidate_ids'])} |"
        )

    for batch in data["batches"]:
        lines.extend(["", f"## {batch['heading']}", ""])
        ids = batch["candidate_ids"]
        if not ids:
            lines.append("No lexical question from this batch remains outside an explicit coverage decision.")
            continue
        lines.extend([
            "| ID | Concept | Status | Placement | Decision or return condition |",
            "|---|---|---|---|---|",
        ])
        for candidate_id in ids:
            candidate = candidates[candidate_id]
            if candidate_id in rendered_ids:
                primary = batches[candidate["batches"][0]]["heading"]
                outcome = f"See the complete decision under [{primary}](#{slugify(primary)})."
            else:
                outcome = candidate_outcome(candidate) + " " + candidate["summary"]
                rendered_ids.add(candidate_id)
            lines.append(
                f"| `{candidate_id}` | {clean_cell(candidate['concept'])} | "
                f"{STATUS_LABELS[candidate['status']]} | {clean_cell(candidate['placement'])} | "
                f"{clean_cell(outcome)} |"
            )

    sources = data.get("prompt_sources", [])
    if sources:
        lines.extend(["", "## Prompt sources", ""])
        lines.append("These inventories were used only to recover questions that an earlier batch might have overlooked. They do not define Phi's semantic structure and do not turn the register into an English relex checklist.")
        lines.append("")
        for source in sources:
            lines.append(f"- [{source['title']}]({source['url']}): {source['note']}")

    return "\n".join(lines) + "\n"


def main():
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
            "ERROR: project/content_vocabulary_decisions.md is stale; "
            "run python3 scripts/content_vocabulary_decisions.py --write",
            file=sys.stderr,
        )
        return 1
    print(f"checked {len(data['batches'])} batches and {len(data['candidates'])} decisions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
