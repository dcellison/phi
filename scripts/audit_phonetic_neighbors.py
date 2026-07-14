#!/usr/bin/env python3
"""Rank Phi lexical neighbors by phoneme-feature similarity.

This complements the validator's character edit-distance ratchet.  It is an
audit and prompt generator, never an automatic rename decision.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent.parent
VOCAB = ROOT / "vocabulary"
VOCAB_ENTRY_DIRS = tuple(
    VOCAB / name for name in ("content", "function", "interjection")
)
DOC_ROOTS = ("documents", "manual", "pamphlets", "primer", "texts")
SEGMENT = re.compile(r"ph|th|sh|wh|[hklmnprstwaeiou]")
VOWELS = set("aeiou")

VOWEL_FEATURES = {
    "a": (0, 1, 0), "e": (1, 0, 0), "i": (2, 0, 0),
    "o": (1, 2, 1), "u": (2, 2, 1),
}
CONSONANT_FEATURES = {
    "p": ("bilabial", "stop", 0),
    "ph": ("bilabial", "fricative", 0),
    "m": ("bilabial", "nasal", 1),
    "w": ("labial-velar", "approximant", 1),
    "wh": ("labial-velar", "fricative", 0),
    "t": ("dental", "stop", 0),
    "th": ("dental", "fricative", 0),
    "n": ("dental", "nasal", 1),
    "s": ("alveolar", "fricative", 0),
    "l": ("alveolar", "lateral", 1),
    "r": ("alveolar", "rhotic", 1),
    "sh": ("postalveolar", "fricative", 0),
    "k": ("velar", "stop", 0),
    "h": ("glottal", "fricative", 0),
}


def segments(word):
    parsed = SEGMENT.findall(word)
    return parsed if "".join(parsed) == word else None


def substitution_cost(a, b):
    if a == b:
        return 0.0
    if a in VOWELS and b in VOWELS:
        fa, fb = VOWEL_FEATURES[a], VOWEL_FEATURES[b]
        distance = abs(fa[0] - fb[0]) + abs(fa[1] - fb[1]) + abs(fa[2] - fb[2])
        return min(0.95, 0.35 + 0.12 * distance)
    if a in VOWELS or b in VOWELS:
        return 1.0
    fa, fb = CONSONANT_FEATURES[a], CONSONANT_FEATURES[b]
    return min(1.0, 0.25 + 0.25 * (fa[0] != fb[0])
               + 0.35 * (fa[1] != fb[1]) + 0.15 * (fa[2] != fb[2]))


def weighted_distance(a, b):
    left, right = segments(a), segments(b)
    if left is None or right is None:
        return float("inf")
    previous = [float(i) for i in range(len(right) + 1)]
    for i, x in enumerate(left, start=1):
        current = [float(i)]
        for j, y in enumerate(right, start=1):
            current.append(min(
                previous[j] + 1.0,
                current[j - 1] + 1.0,
                previous[j - 1] + substitution_cost(x, y),
            ))
        previous = current
    return previous[-1]


def unit_edit_distance(a, b):
    left, right = segments(a), segments(b)
    if left is None or right is None:
        return 999
    previous = list(range(len(right) + 1))
    for i, x in enumerate(left, start=1):
        current = [i]
        for j, y in enumerate(right, start=1):
            current.append(min(
                previous[j] + 1,
                current[j - 1] + 1,
                previous[j - 1] + (x != y),
            ))
        previous = current
    return previous[-1]


def load_entries():
    entries = []
    paths = sorted(
        path
        for directory in VOCAB_ENTRY_DIRS
        for path in directory.rglob("*.json")
    )
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if "content" in path.parts:
            kind = "content"
        elif "function" in path.parts:
            kind = "function"
        else:
            kind = "interjection"
        entries.append({
            "word": data["word"], "gloss": data["gloss"],
            "kind": kind, "pos": data["pos"][0],
        })
    return entries


def corpus_counts(entries):
    words = {entry["word"] for entry in entries}
    counts = Counter()

    def phi_tokens(raw, strict=False):
        core = raw
        if re.search(r"[A-Z0-9=→—]", core):
            return []
        core = re.sub(r"\[[^]]*]|\([^)]*\)", " ", core)
        tokens = re.sub(r"[.,!?\"'():;*`“”‘’]", " ", core).split()
        if not tokens or not all(
                set(token) <= set("hklmnprstwaeiou") for token in tokens):
            return []
        known = [token for token in tokens if token in words]
        if strict:
            enough = len(known) > len(tokens) / 2
        else:
            enough = len(known) >= max(1, len(tokens) / 2)
        return known if enough else []

    for root_name in DOC_ROOTS:
        root = ROOT / root_name
        for path in root.rglob("*.md"):
            if "part7_reference" in path.parts:
                continue
            in_fence = False
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.strip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    candidate = re.sub(r"^\s*[A-Za-z]:\s+", "", line)
                    counts.update(phi_tokens(candidate))
                    continue
                for candidate in re.findall(r"\*\*([^*\n]+)\*\*", line):
                    counts.update(phi_tokens(candidate, strict=True))
    return counts


def ranked_pairs(entries, counts, threshold, kind):
    selected = [entry for entry in entries if kind == "all" or entry["kind"] == kind]
    pairs = []
    for i, left in enumerate(selected):
        for right in selected[i + 1:]:
            if abs(len(segments(left["word"])) - len(segments(right["word"]))) > 1:
                continue
            score = weighted_distance(left["word"], right["word"])
            if score > threshold:
                continue
            function_priority = int(
                left["kind"] == "function" or right["kind"] == "function"
            )
            attestations = counts[left["word"]] + counts[right["word"]]
            pairs.append((score, -function_priority, -attestations, left, right))
    return sorted(
        pairs,
        key=lambda item: (
            item[0], item[1], item[2], item[3]["word"], item[4]["word"]
        ),
    )


def report(pairs, counts, limit):
    lines = [
        "# Generated by scripts/audit_phonetic_neighbors.py; do not hand-edit.",
        "# score\tunit_edits\tleft\tleft_gloss\tleft_kind\t"
        "right\tright_gloss\tright_kind\tcorpus_attestations",
    ]
    for score, _, _, left, right in pairs[:limit]:
        lines.append("\t".join((
            f"{score:.2f}", str(unit_edit_distance(left["word"], right["word"])),
            left["word"], left["gloss"], left["kind"], right["word"],
            right["gloss"], right["kind"],
            str(counts[left["word"]] + counts[right["word"]]),
        )))
    return "\n".join(lines) + "\n"


def candidate_report(candidate, entries, counts, threshold):
    hits = []
    for entry in entries:
        score = weighted_distance(candidate, entry["word"])
        if score <= threshold:
            hits.append((score, -counts[entry["word"]], entry))
    hits.sort(key=lambda item: (item[0], item[1], item[2]["word"]))
    print("score\tunit_edits\tword\tgloss\tkind\tcorpus_attestations")
    for score, _, entry in hits:
        print("\t".join((
            f"{score:.2f}", str(unit_edit_distance(candidate, entry["word"])),
            entry["word"], entry["gloss"], entry["kind"],
            str(counts[entry["word"]]),
        )))


def prompts(pairs, count, seed):
    rng = random.Random(seed)
    chosen = list(pairs[:max(count * 3, count)])
    rng.shuffle(chosen)
    print("trial\tA\tB\tX\tanswer")
    for index, item in enumerate(chosen[:count], start=1):
        left, right = item[3]["word"], item[4]["word"]
        target = rng.choice((left, right))
        print(f"{index}\t{left}\t{right}\t{target}\t{'A' if target == left else 'B'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--kind", choices=("all", "content", "function", "interjection"),
        default="all",
    )
    parser.add_argument("--threshold", type=float, default=0.85)
    parser.add_argument("--limit", type=int, default=250)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--candidate")
    parser.add_argument("--prompts", type=int, default=0)
    parser.add_argument("--seed", type=int, default=202601)
    args = parser.parse_args()

    entries = load_entries()
    counts = corpus_counts(entries)
    if args.candidate:
        candidate_report(args.candidate, entries, counts, args.threshold)
        return
    pairs = ranked_pairs(entries, counts, args.threshold, args.kind)
    if args.prompts:
        prompts(pairs, args.prompts, args.seed)
        return
    text = report(pairs, counts, args.limit)
    if args.output:
        target = args.output if args.output.is_absolute() else ROOT / args.output
        target.write_text(text, encoding="utf-8")
        try:
            label = target.relative_to(ROOT)
        except ValueError:
            label = target
        print(f"wrote {label}: {min(len(pairs), args.limit)} pairs")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
