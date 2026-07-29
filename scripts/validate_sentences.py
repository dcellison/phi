#!/usr/bin/env python3
"""Validate complete Phi sentences with the independent surface parser."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Iterator

from phi_sentence_validator import Lexicon, ParseResult, PhiParser, SyntaxNode


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_DOC_ROOTS = (
    "documents",
    "project",
    "manual",
    "pamphlets",
    "primer",
    "texts",
    "book",
    "canon.md",
    "CLAUDE.md",
    "kia.md",
    "README.md",
    "short_road.md",
)
ASSERTED_DOC_ROOTS = (
    "canon.md",
    "documents/grammar",
    "documents/reference",
    "manual",
    "pamphlets",
    "primer",
    "book",
    "kia.md",
    "README.md",
    "short_road.md",
)

PLAIN_PHI_RE = re.compile(r"[A-Za-z]+(?: [A-Za-z]+)*\.(?: [A-Za-z]+(?: [A-Za-z]+)*\.)*")
SPAN_PATTERNS = (re.compile(r"\*\*([^*\n]+)\*\*"),)
SPEAKER_LABEL_RE = re.compile(r"^\s*[A-Za-z]:\s+")

DESCRIPTION = (
    "Validate structured vocabulary examples and the maintained teaching "
    "corpus with Phi's independent surface parser. The archive is never scanned."
)
EPILOG = """examples:
  python3 scripts/validate_sentences.py
  python3 scripts/validate_sentences.py --paths texts/news_from_nowhere
  python3 scripts/validate_sentences.py --sentence "mia thia nila."
  python3 scripts/validate_sentences.py --sentence "henoi." --fragment
  python3 scripts/validate_sentences.py --sentence "mia thia nila." --show-tree
"""


@dataclass(frozen=True)
class SentenceSource:
    label: str
    text: str
    allow_fragments: bool


def _known_ratio(text: str, lexicon: Lexicon) -> float:
    words = re.findall(r"[A-Za-z]+", text.lower())
    if not words:
        return 0.0
    known = sum(word in lexicon.words for word in words)
    return known / len(words)


def _candidate(text: str, lexicon: Lexicon) -> str | None:
    stripped = text.strip()
    stripped = re.sub(r"^\s*>\s*", "", stripped)
    stripped = SPEAKER_LABEL_RE.sub("", stripped)
    stripped = stripped.strip("*_ ")
    if "[" in stripped or "]" in stripped:
        return None
    if not PLAIN_PHI_RE.fullmatch(stripped):
        return None
    if _known_ratio(stripped, lexicon) <= 0.5:
        return None
    return stripped


def iter_lexicon_examples(root: Path) -> Iterator[SentenceSource]:
    vocabulary = root / "vocabulary"
    for path in sorted(vocabulary.rglob("*.json")):
        if path.name == "schema.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for index, example in enumerate(data.get("examples", [])):
            phi = example.get("phi", "")
            if phi:
                rel = path.relative_to(root)
                yield SentenceSource(
                    f"{rel}:examples[{index}].phi",
                    phi,
                    False,
                )


def markdown_files(root: Path, paths: Iterable[str] | None) -> list[Path]:
    files = []
    for raw in paths or ACTIVE_DOC_ROOTS:
        path = root / raw
        if "archive" in path.relative_to(root).parts:
            continue
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(
                candidate
                for candidate in sorted(path.rglob("*.md"))
                if "archive" not in candidate.relative_to(root).parts
            )
    return sorted(set(files))


def iter_markdown_examples(
    root: Path, lexicon: Lexicon, paths: Iterable[str] | None = None
) -> Iterator[SentenceSource]:
    for path in markdown_files(root, paths):
        rel = path.relative_to(root)
        lines = path.read_text(encoding="utf-8").splitlines()
        in_fence = False
        fence_is_text = False
        heading = ""
        for lineno, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("#"):
                heading = stripped.lstrip("#").strip().lower()
            if stripped.startswith("```"):
                if in_fence:
                    in_fence = False
                    fence_is_text = False
                else:
                    in_fence = True
                    language = stripped[3:].strip().lower()
                    fence_is_text = language in {"", "text", "phi"}
                continue

            candidates: list[str] = []
            if in_fence and fence_is_text:
                following = lines[lineno] if lineno < len(lines) else ""
                translation_after_gloss = (
                    lines[lineno + 1] if lineno + 1 < len(lines) else ""
                )
                has_gloss_or_translation = (
                    bool(re.search(r"\b[A-Z][A-Z0-9.]*\b", following))
                    or following.strip().startswith("(")
                    or translation_after_gloss.strip().startswith("(")
                )
                if has_gloss_or_translation:
                    candidates.append(line)
            elif not in_fence:
                for pattern in SPAN_PATTERNS:
                    candidates.extend(match.group(1) for match in pattern.finditer(line))

            deliberately_wrong = any(
                marker in heading
                for marker in ("common error", "wrong", "ungrammatical", "repair exercise")
            )
            for raw_candidate in candidates:
                if raw_candidate.lstrip().startswith("*") or deliberately_wrong:
                    continue
                phi = _candidate(raw_candidate, lexicon)
                if phi is None:
                    continue
                yield SentenceSource(f"{rel}:{lineno}", phi, True)


def format_tree(node: SyntaxNode, indent: int = 0) -> str:
    label = node.kind + (f"={node.value}" if node.value else "")
    lines = [f"{'  ' * indent}{label} [{node.start}:{node.end}]"]
    for child in node.children:
        lines.append(format_tree(child, indent + 1))
    return "\n".join(lines)


def render_errors(source: SentenceSource, result: ParseResult) -> list[str]:
    return [
        f"{source.label}: {diagnostic.render(result.tokens)}"
        for diagnostic in result.diagnostics
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        help="active Markdown paths relative to the repository root",
    )
    parser.add_argument(
        "--lexicon-only",
        action="store_true",
        help="check structured vocabulary examples without Markdown",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="scan every recognized complete example in active Markdown",
    )
    parser.add_argument(
        "--docs-only",
        action="store_true",
        help="scan Markdown without structured vocabulary examples",
    )
    parser.add_argument("--sentence", help="validate one literal Phi sentence")
    parser.add_argument(
        "--fragment",
        action="store_true",
        help="allow --sentence to be a licensed standalone fragment",
    )
    parser.add_argument(
        "--show-tree",
        action="store_true",
        help="print the syntax tree for a valid --sentence",
    )
    args = parser.parse_args()
    if args.docs and args.docs_only:
        parser.error("--docs and --docs-only are alternatives")
    if args.docs and args.paths:
        parser.error("--docs already selects every active Markdown path")
    if args.lexicon_only and (args.docs or args.docs_only or args.paths):
        parser.error("--lexicon-only cannot be combined with Markdown scanning")
    if args.sentence is not None and (
        args.lexicon_only or args.docs or args.docs_only or args.paths
    ):
        parser.error("--sentence cannot be combined with corpus selection")
    if args.show_tree and args.sentence is None:
        parser.error("--show-tree requires --sentence")
    if args.fragment and args.sentence is None:
        parser.error("--fragment requires --sentence")
    return args


def main() -> int:
    args = parse_args()
    lexicon = Lexicon.load()
    parser = PhiParser(lexicon)

    if args.sentence is not None:
        result = parser.parse(args.sentence, allow_fragments=args.fragment)
        for error in render_errors(
            SentenceSource("<argument>", args.sentence, args.fragment), result
        ):
            print(f"ERROR   {error}")
        if result.ok and args.show_tree and result.tree:
            print(format_tree(result.tree))
        print(f"{'Valid' if result.ok else 'Invalid'} Phi utterance.")
        return 0 if result.ok else 1

    sources: list[SentenceSource] = []
    if not args.docs_only:
        sources.extend(iter_lexicon_examples(PROJECT_ROOT))
    if args.docs or args.docs_only:
        sources.extend(iter_markdown_examples(PROJECT_ROOT, lexicon, args.paths))
    elif args.paths:
        sources.extend(iter_markdown_examples(PROJECT_ROOT, lexicon, args.paths))
    elif not args.lexicon_only:
        sources.extend(
            iter_markdown_examples(PROJECT_ROOT, lexicon, ASSERTED_DOC_ROOTS)
        )

    errors = []
    seen = set()
    checked = 0
    for source in sources:
        key = (source.label, source.text)
        if key in seen:
            continue
        seen.add(key)
        checked += 1
        result = parser.parse(source.text, allow_fragments=source.allow_fragments)
        errors.extend(render_errors(source, result))

    for error in errors:
        print(f"ERROR   {error}")
    print(f"\n{checked} complete Phi example(s) parsed. {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
