#!/usr/bin/env python3
"""Build isolated, compact working views for Phi translation."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path

import compound_registry
import name_forms


ROOT = Path(__file__).resolve().parent.parent
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)\n```", re.S)
SOURCE_RE = re.compile(r"([a-z][a-z0-9-]*):\s*(.+)", re.S)
WORKING_SOURCE_RE = re.compile(r"- `([a-z][a-z0-9-]*)`:\s*(.+)")
PHI_TOKEN_RE = re.compile(r"[a-z]+|\.")
COMPLEMENT_OPENERS = {"tha": "tho", "pha": "pho", "sha": "sho"}
COMPLEMENT_CLOSERS = {closer: opener for opener, closer in COMPLEMENT_OPENERS.items()}
CONTENT_GAP_WORDS = {"sua", "hina", "weno", "kua", "misa", "thela", "wia"}
NAME_MARKERS = {name_forms.NAME_MARKER, *name_forms.HONORIFICS}
PACKET_FORMAT = "phi-compact-derivation-bundle-v1"
MANIFEST_FORMAT = "phi-compact-derivation-manifest-v1"
DEFAULT_BATCH_SIZE = 8
DEFAULT_AUDIT_SAMPLE_RATE = 0.10
INDEPENDENT_AUDIT_FLAGS = {
    "compound-interpretation",
    "complex-coordination",
    "long-sentence",
    "many-assertions",
    "multiple-complement-frames",
    "question-or-condition",
    "relative-clause-attachment",
}


@dataclass(frozen=True)
class TranslationUnit:
    phi: str
    sources: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class RiskAssessment:
    unit: int
    flags: tuple[str, ...]


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
                    raise ValueError(f"{match.group(1)} source witness is not a string")
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
                raise ValueError(f"{match.group(1)} source witness is not a string")
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


def unit_digest(unit: TranslationUnit) -> str:
    return hashlib.sha256((unit.phi + "\n").encode("utf-8")).hexdigest()


def phi_tokens(phi: str, *, keep_periods: bool = False) -> list[str]:
    tokens = PHI_TOKEN_RE.findall(phi.lower())
    return tokens if keep_periods else [token for token in tokens if token != "."]


def phi_sentences(phi: str) -> list[list[str]]:
    return [
        words
        for sentence in phi.split(".")
        if (words := re.findall(r"[a-z]+", sentence.lower()))
    ]


def load_lexicon(root: Path = ROOT) -> dict[str, dict]:
    entries: dict[str, dict] = {}
    directories = tuple(
        root / "vocabulary" / name
        for name in ("content", "function", "interjection")
    )
    for path in sorted(file for directory in directories for file in directory.rglob("*.json")):
        entry = json.loads(path.read_text(encoding="utf-8"))
        word = entry.get("word")
        if not isinstance(word, str):
            raise ValueError(f"{path}: vocabulary entry has no word")
        if word in entries:
            raise ValueError(f"duplicate vocabulary word: {word}")
        entries[word] = entry
    return entries


def parse_unit_spec(spec: str | None, total: int) -> list[int]:
    if spec is None:
        return list(range(1, total + 1))
    selected: set[int] = set()
    for raw_part in spec.split(","):
        part = raw_part.strip()
        if not part:
            raise ValueError("empty unit selector")
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            if not (start_text.isdigit() and end_text.isdigit()):
                raise ValueError(f"invalid unit range: {part!r}")
            start, end = int(start_text), int(end_text)
            if start > end:
                raise ValueError(f"unit range runs backwards: {part!r}")
            selected.update(range(start, end + 1))
        elif part.isdigit():
            selected.add(int(part))
        else:
            raise ValueError(f"invalid unit selector: {part!r}")
    outside = sorted(index for index in selected if index < 1 or index > total)
    if outside:
        raise ValueError(f"unit selector outside 1-{total}: {', '.join(map(str, outside))}")
    return sorted(selected)


def source_to_phi_view(
    path: Path,
    units: list[TranslationUnit],
    indices: list[int] | None = None,
    full_digest: str | None = None,
    total_units: int | None = None,
) -> str:
    if indices is None:
        indices = list(range(1, len(units) + 1))
    if len(indices) != len(units):
        raise ValueError("source view indices must match its units")
    parts = [
        "# Source-to-Phi working view",
        "",
        f"Input: `{path.as_posix()}`",
        f"Selected units: {len(units)}",
        f"Frozen stream units: {total_units if total_units is not None else len(units)}",
        f"Phi SHA-256: `{full_digest or phi_digest(units)}`",
        "",
        "This view omits glosses, parenthetical English, notes, and limits.",
    ]
    for index, unit in zip(indices, units):
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


def matching_compounds(phi: str, compounds: list[dict]) -> list[dict]:
    sentences = phi_sentences(phi)
    matched = []
    for compound in compounds:
        target = compound["tokens"]
        if any(
            sentence[start : start + len(target)] == target
            for sentence in sentences
            for start in range(0, len(sentence) - len(target) + 1)
        ):
            matched.append(compound)
    return matched


def unknown_phi_forms(phi: str, lexicon: dict[str, dict]) -> list[str]:
    words = phi_tokens(phi)
    name_indices = name_forms.marked_atom_indices(words)
    unknown = []
    for index, word in enumerate(words):
        if word in lexicon:
            continue
        if index in name_indices and not name_forms.form_errors(word):
            continue
        unknown.append(word)
    return sorted(set(unknown))


def gloss_scaffold(phi: str, lexicon: dict[str, dict]) -> str:
    output: list[str] = []
    expecting_name = False
    for token in phi_tokens(phi, keep_periods=True):
        if token == ".":
            if output:
                output[-1] += "."
            expecting_name = False
            continue
        if token in NAME_MARKERS:
            entry = lexicon.get(token)
            if entry is None:
                raise ValueError(f"unknown Phi form in gloss scaffold: {token}")
            gloss = entry["gloss"]
            expecting_name = True
        elif expecting_name:
            gloss = token
            expecting_name = False
        else:
            entry = lexicon.get(token)
            if entry is None:
                raise ValueError(f"unknown Phi form in gloss scaffold: {token}")
            gloss = re.sub(r"\s*\([^)]*\)", "", entry["gloss"]).strip()
        output.extend(gloss.split())
    return " ".join(output)


def assess_unit_risk(
    index: int,
    phi: str,
    lexicon: dict[str, dict],
    compounds: list[dict],
) -> RiskAssessment:
    flags: set[str] = set()
    sentences = phi_sentences(phi)
    unit_words = phi_tokens(phi)
    relative_count = 0
    total_frames = 0
    complex_coordination = False
    maximum_slot_run = 0
    slot2_pair = False

    if any(len(sentence) >= 32 for sentence in sentences):
        flags.add("long-sentence")
    if len(sentences) >= 5:
        flags.add("many-assertions")

    for sentence in sentences:
        frame_count = 0
        frame_depth = 0
        maximum_depth = 0
        conjunction_count = 0
        slot_run = 0
        previous_slot = None
        for word in sentence:
            if word in COMPLEMENT_OPENERS:
                frame_count += 1
                frame_depth += 1
                maximum_depth = max(maximum_depth, frame_depth)
            elif word in COMPLEMENT_CLOSERS and frame_depth:
                frame_depth -= 1
            entry = lexicon.get(word, {})
            if entry.get("pos") == "conjunction":
                conjunction_count += 1
            if isinstance(entry.get("slot"), int):
                slot_run += 1
                maximum_slot_run = max(maximum_slot_run, slot_run)
                if previous_slot == entry["slot"] == 2:
                    slot2_pair = True
                previous_slot = entry["slot"]
            else:
                slot_run = 0
                previous_slot = None
        total_frames += frame_count
        if frame_count >= 2 or maximum_depth >= 2:
            flags.add("multiple-complement-frames")
        relative_count += sentence.count("whu")
        if conjunction_count >= 2:
            complex_coordination = True
        if "lu" in sentence or any(word in CONTENT_GAP_WORDS for word in sentence):
            flags.add("question-or-condition")

    if total_frames:
        flags.add("complement-frame")
    if complex_coordination:
        flags.add("complex-coordination")
    if relative_count >= 2 or (
        relative_count and (total_frames or complex_coordination or unit_words.count("shia") >= 2)
    ):
        flags.add("relative-clause-attachment")
    if maximum_slot_run >= 3 or slot2_pair:
        flags.add("particle-scope-stack")
    if unit_words.count("shia") >= 3 or (
        unit_words.count("shia") >= 2
        and (total_frames or complex_coordination or relative_count)
    ):
        flags.add("pronoun-reference")

    registered = matching_compounds(phi, compounds)
    if len(registered) >= 2 or any(len(compound["tokens"]) >= 3 for compound in registered):
        flags.add("compound-interpretation")

    specialist = {
        word
        for word in unit_words
        if lexicon.get(word, {}).get("modules")
    }
    if len(specialist) >= 3:
        flags.add("specialist-vocabulary")

    if unknown_phi_forms(phi, lexicon):
        flags.add("unlisted-form")

    return RiskAssessment(index, tuple(sorted(flags)))


def audit_plan(
    units: list[TranslationUnit],
    assessments: list[RiskAssessment],
    sample_rate: float = DEFAULT_AUDIT_SAMPLE_RATE,
) -> tuple[list[int], list[int], list[int]]:
    if not 0 <= sample_rate <= 1:
        raise ValueError("audit sample rate must be between 0 and 1")
    risk_units = [
        assessment.unit
        for assessment in assessments
        if requires_independent_audit(assessment)
    ]
    below_threshold = [
        assessment.unit
        for assessment in assessments
        if not requires_independent_audit(assessment)
    ]
    sample_count = math.ceil(len(below_threshold) * sample_rate)
    ranked = sorted(
        below_threshold,
        key=lambda index: hashlib.sha256(
            f"{unit_digest(units[index - 1])}:{index}".encode("utf-8")
        ).digest(),
    )
    sample_units = sorted(ranked[:sample_count])
    return sorted(set(risk_units + sample_units)), risk_units, sample_units


def requires_independent_audit(assessment: RiskAssessment) -> bool:
    flags = set(assessment.flags)
    return bool(flags & INDEPENDENT_AUDIT_FLAGS) or len(flags) >= 2


def compact_entry_line(word: str, entry: dict) -> str:
    details = [entry.get("pos", "unknown")]
    if isinstance(entry.get("slot"), int):
        details.append(f"Slot {entry['slot']}")
    if entry.get("slot1_rank"):
        details.append(str(entry["slot1_rank"]))
    if entry.get("modules"):
        details.append("modules: " + ", ".join(entry["modules"]))
    prose = entry.get("description", "")
    usage = entry.get("usage_notes")
    if usage:
        prose += " Usage: " + usage
    return f"- `{word}` | `{entry.get('gloss', '')}` | {', '.join(details)} | {prose}".rstrip()


def compact_reference_sections(
    units: list[TranslationUnit], lexicon: dict[str, dict], compounds: list[dict]
) -> list[str]:
    used_words: list[str] = []
    seen_words: set[str] = set()
    relevant_compounds: list[dict] = []
    seen_compounds: set[str] = set()
    for unit in units:
        for word in phi_tokens(unit.phi):
            if word in lexicon and word not in seen_words:
                used_words.append(word)
                seen_words.add(word)
        for compound in matching_compounds(unit.phi, compounds):
            if compound["compound"] not in seen_compounds:
                relevant_compounds.append(compound)
                seen_compounds.add(compound["compound"])

    parts: list[str] = []
    if relevant_compounds:
        parts.extend(["## Registered compounds used", ""])
        for compound in relevant_compounds:
            parts.append(
                f"- `{compound['compound']}` | literal: {compound['literal']} | "
                f"established meaning: {compound['meaning']}"
            )
        parts.append("")

    parts.extend(["## Compact lexicon", ""])
    for word in used_words:
        parts.append(compact_entry_line(word, lexicon[word]))

    parts.extend(
        [
            "",
            "## Grammar checks",
            "",
            "- Phi is modifier-first throughout. Subjects precede adjuncts and objects, and the lexical predicate closes its clause after any Slot 1 cluster.",
            "- A preposition precedes its object. A relative clause precedes its head, with the oblique-relative gap as the documented surface case.",
            "- Read Slot 1 in canonical rank order and Slot 2 as a modifier-first nest. Do not flatten tense, aspect, voice, evidence, modality, negation, focus, restriction, degree, or comparison.",
            "- Track every complement opener to its closer and identify the matrix predicate that follows it. A content question has one gap in its own clause.",
            "- Coordination joins the constituents licensed on each side. Topic drop does not license an English participant that Phi never supplies.",
            "- If two materially different structures remain licensed after consulting canon and the grammar references, report both under semantic uncertainty instead of choosing by fluency.",
        ]
    )
    return parts


def compact_reference_view(
    units: list[TranslationUnit], lexicon: dict[str, dict], compounds: list[dict]
) -> str:
    parts = [
        "# Anonymous Phi derivation reference",
        "",
        f"Format: `{PACKET_FORMAT}`",
        f"Selected Phi SHA-256: `{phi_digest(units)}`",
        "",
        "This compact reference contains only lexical and grammatical material needed by the accompanying anonymous Phi packets. It contains no source, title, filename, citations, prior English, notes, limits, repository status, or task history.",
        "",
        *compact_reference_sections(units, lexicon, compounds),
    ]
    return "\n".join(parts) + "\n"


def phi_to_english_view(
    units: list[TranslationUnit],
    *,
    indices: list[int] | None = None,
    full_digest: str | None = None,
    lexicon: dict[str, dict] | None = None,
    compounds: list[dict] | None = None,
    assessments: dict[int, RiskAssessment] | None = None,
    audit_samples: set[int] | None = None,
    audit_mode: bool = False,
    include_reference: bool = True,
    external_reference: str | None = None,
) -> str:
    if indices is None:
        indices = list(range(1, len(units) + 1))
    if len(indices) != len(units):
        raise ValueError("anonymous view indices must match its units")
    stream_digest = full_digest or phi_digest(units)
    selected_digest = phi_digest(units)
    parts = [
        (
            "# Anonymous Phi semantic-audit bundle"
            if audit_mode
            else "# Anonymous Phi English-derivation bundle"
        ),
        "",
        f"Format: `{PACKET_FORMAT}`",
        f"Selected units: {len(units)}",
        f"Full frozen Phi SHA-256: `{stream_digest}`",
        f"Selected Phi SHA-256: `{selected_digest}`",
        "",
        "The source, title, filename, citations, prior English, notes, limits, repository status, and task history are intentionally absent.",
        "",
        "For each unit, read the Phi before looking at its generated lexical gloss scaffold. Record each complete assertion's predicate and arguments, modifier attachments, particle and complement scope, and pronoun antecedents. Then verify the scaffold token by token, add any structural brackets required by that analysis, and write natural English from the Phi alone. The scaffold is not a finished exact gloss. A different English rhythm is harmless; a different participant, attachment, scope, or antecedent is a semantic disagreement.",
        "",
        (
            (
                f"Use only `canon.md`, the supplied `{external_reference}`, and the grammar references."
                if external_reference
                else "Use only `canon.md`, the compact lexical material below, and the grammar references."
            )
            + " This audit is internal, so do not load the voice guide or Humanizer."
            if audit_mode
            else (
                f"Use only `canon.md`, the supplied `{external_reference}`, the grammar references, and the required reader-facing voice references."
                if external_reference
                else "Use only `canon.md`, the compact lexical material below, the grammar references, and the required reader-facing voice references."
            )
            + " Apply Humanizer only to the natural English after its meaning is settled."
        )
        + " Do not inspect any source-facing or repository-navigation surface.",
        "",
        "Required response shape for every unit:",
        "",
        "```text",
        "## Unit NNN",
        "Structure:",
        "- Assertion 1: predicate=...; arguments=...; attachment=...; scope=...; antecedents=...",
        "Exact gloss: ...",
        "Natural English: (...)",
        "Semantic uncertainty: none | <precise unresolved alternatives>",
        "```",
        "",
        "## Phi units",
    ]

    lexicon = lexicon or {}
    compounds = compounds or []
    assessments = assessments or {}
    audit_samples = audit_samples or set()
    for index, unit in zip(indices, units):
        unknown = unknown_phi_forms(unit.phi, lexicon) if lexicon else []
        if unknown:
            raise ValueError(f"unit {index:03d} has unlicensed forms: {', '.join(unknown)}")
        assessment = assessments.get(index)
        reasons = list(assessment.flags) if assessment else []
        if index in audit_samples:
            reasons.append("deterministic-low-risk-sample")
        parts.extend(
            [
                "",
                f"### Unit {index:03d}",
                "",
                f"Phi SHA-256: `{unit_digest(unit)}`",
                "",
            ]
        )
        if reasons:
            parts.append("Review flags: " + ", ".join(reasons) + ".")
            parts.append("")
        parts.extend(["```", unit.phi, "```"])
        if lexicon:
            parts.extend(
                [
                    "",
                    "Generated gloss scaffold:",
                    "",
                    "```",
                    gloss_scaffold(unit.phi, lexicon),
                    "```",
                ]
            )

    if include_reference and lexicon:
        parts.extend(["", *compact_reference_sections(units, lexicon, compounds)])
    return "\n".join(parts) + "\n"


def make_assessments(
    units: list[TranslationUnit], lexicon: dict[str, dict], compounds: list[dict]
) -> list[RiskAssessment]:
    return [
        assess_unit_risk(index, unit.phi, lexicon, compounds)
        for index, unit in enumerate(units, 1)
    ]


def write_packet_directory(
    output_dir: Path,
    units: list[TranslationUnit],
    selected_indices: list[int],
    lexicon: dict[str, dict],
    compounds: list[dict],
    assessments: list[RiskAssessment],
    *,
    batch_size: int = DEFAULT_BATCH_SIZE,
    audit_mode: bool = False,
    audit_samples: list[int] | None = None,
    audit_sample_rate: float = DEFAULT_AUDIT_SAMPLE_RATE,
) -> dict:
    if batch_size < 1:
        raise ValueError("batch size must be positive")
    if output_dir.exists() and not output_dir.is_dir():
        raise ValueError(f"output path is not a directory: {output_dir}")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"output directory is not empty: {output_dir}")
    for index in selected_indices:
        unknown = unknown_phi_forms(units[index - 1].phi, lexicon)
        if unknown:
            raise ValueError(f"unit {index:03d} has unlicensed forms: {', '.join(unknown)}")
    output_dir.mkdir(parents=True, exist_ok=True)
    full_digest = phi_digest(units)
    assessment_map = {assessment.unit: assessment for assessment in assessments}
    sample_set = set(audit_samples or [])
    selected_set = set(selected_indices)
    batches = []
    prefix = "audit" if audit_mode else "derive"
    selected_units = [units[index - 1] for index in selected_indices]
    reference_name = "reference.md"
    reference = compact_reference_view(selected_units, lexicon, compounds)
    (output_dir / reference_name).write_text(reference, encoding="utf-8")

    for batch_number, start in enumerate(range(0, len(selected_indices), batch_size), 1):
        batch_indices = selected_indices[start : start + batch_size]
        batch_units = [units[index - 1] for index in batch_indices]
        name = (
            f"{prefix}_{batch_number:03d}_units_"
            f"{batch_indices[0]:03d}-{batch_indices[-1]:03d}.md"
        )
        rendered = phi_to_english_view(
            batch_units,
            indices=batch_indices,
            full_digest=full_digest,
            lexicon=lexicon,
            compounds=compounds,
            assessments=assessment_map,
            audit_samples=sample_set,
            audit_mode=audit_mode,
            include_reference=False,
            external_reference=reference_name,
        )
        (output_dir / name).write_text(rendered, encoding="utf-8")
        batches.append(
            {
                "file": name,
                "units": batch_indices,
                "selected_phi_sha256": phi_digest(batch_units),
            }
        )

    manifest = {
        "format": MANIFEST_FORMAT,
        "mode": "audit" if audit_mode else "derivation",
        "unit_count": len(units),
        "full_phi_sha256": full_digest,
        "selected_units": selected_indices,
        "batch_size": batch_size,
        "reference_file": reference_name,
        "reference_sha256": hashlib.sha256(reference.encode("utf-8")).hexdigest(),
        "independent_audit_policy": {
            "critical_flags": sorted(INDEPENDENT_AUDIT_FLAGS),
            "minimum_total_flags": 2,
            "sample_rate": audit_sample_rate if audit_mode else None,
        },
        "unit_hashes": [
            {"unit": index, "phi_sha256": unit_digest(units[index - 1])}
            for index in selected_indices
        ],
        "risk_units": [
            {"unit": assessment.unit, "flags": list(assessment.flags)}
            for assessment in assessments
            if assessment.unit in selected_set and requires_independent_audit(assessment)
        ],
        "sample_units": sorted(sample_set),
        "batches": batches,
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build an isolated translation phase from a texts Markdown file."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--phase", choices=("source-to-phi", "phi-to-english"), help="working view to render"
    )
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument("--output", type=Path)
    destination.add_argument("--output-dir", type=Path)
    parser.add_argument("--units", help="one-based units, for example 1-8,14,20-22")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument(
        "--audit-only",
        action="store_true",
        help="select risk-flagged units plus a deterministic low-risk sample",
    )
    parser.add_argument(
        "--audit-sample-rate",
        type=float,
        default=DEFAULT_AUDIT_SAMPLE_RATE,
        help="fraction of below-threshold units included in the audit queue",
    )
    parser.add_argument(
        "--digest-only",
        action="store_true",
        help="print only the SHA-256 of the aligned Phi stream",
    )
    args = parser.parse_args()

    if args.phase is None and not args.digest_only:
        parser.error("--phase is required unless --digest-only is used")
    if args.digest_only and any((args.output_dir, args.units, args.audit_only)):
        parser.error("--digest-only cannot select or batch units")
    if args.phase != "phi-to-english" and (args.output_dir or args.audit_only):
        parser.error("--output-dir and --audit-only belong to the Phi-to-English phase")
    if args.audit_only and args.units:
        parser.error("--audit-only chooses its own units; use --units for a manual retry packet")

    units = parse_units(args.path.read_text(encoding="utf-8"))
    if not units:
        parser.error(f"no source-aligned translation units found in {args.path}")
    full_digest = phi_digest(units)

    if args.digest_only:
        rendered = full_digest + "\n"
        if args.output is None:
            print(rendered, end="")
        else:
            args.output.write_text(rendered, encoding="utf-8")
        return 0

    try:
        selected_indices = parse_unit_spec(args.units, len(units))
    except ValueError as exc:
        parser.error(str(exc))

    if args.phase == "source-to-phi":
        selected_units = [units[index - 1] for index in selected_indices]
        rendered = source_to_phi_view(
            args.path, selected_units, selected_indices, full_digest, len(units)
        )
    else:
        lexicon = load_lexicon()
        compounds = compound_registry.load_compounds()
        assessments = make_assessments(units, lexicon, compounds)
        audit_samples: list[int] = []
        if args.audit_only:
            try:
                selected_indices, _risk_units, audit_samples = audit_plan(
                    units, assessments, args.audit_sample_rate
                )
            except ValueError as exc:
                parser.error(str(exc))

        if args.output_dir is not None:
            try:
                manifest = write_packet_directory(
                    args.output_dir,
                    units,
                    selected_indices,
                    lexicon,
                    compounds,
                    assessments,
                    batch_size=args.batch_size,
                    audit_mode=args.audit_only,
                    audit_samples=audit_samples,
                    audit_sample_rate=args.audit_sample_rate,
                )
            except ValueError as exc:
                parser.error(str(exc))
            selection_detail = ""
            if args.audit_only:
                selection_detail = (
                    f", {len(manifest['risk_units'])} threshold + "
                    f"{len(manifest['sample_units'])} sample"
                )
            print(
                f"wrote {args.output_dir}: {len(manifest['batches'])} packet(s), "
                f"{len(selected_indices)} selected of {len(units)} units{selection_detail}, "
                f"{full_digest}"
            )
            return 0

        selected_units = [units[index - 1] for index in selected_indices]
        assessment_map = {assessment.unit: assessment for assessment in assessments}
        rendered = phi_to_english_view(
            selected_units,
            indices=selected_indices,
            full_digest=full_digest,
            lexicon=lexicon,
            compounds=compounds,
            assessments=assessment_map,
            audit_samples=set(audit_samples),
            audit_mode=args.audit_only,
        )

    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {args.output}: {len(selected_indices)} units, {full_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
