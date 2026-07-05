#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phi Language Validator

The single validation tool for the Phi project. Checks:

  1. Lexicon integrity (vocabulary/*.json):
     - required schema fields present
     - no undeclared fields (schema has additionalProperties: false)
     - pillar keys are the five canonical keys
     - phonotactic legality of every word:
         * only permitted letters
         * decomposable into (C)CV syllables (digraphs ph/th/sh/wh count
           as single onsets; a lone vowel is legal only as the second
           element of a vowel pair in hiatus)
         * word begins with a consonant onset, every syllable open
         * no three-vowel sequences
         * no duplicated syllable within a word
     - `syllables` array matches the canonical syllabification
       (each element one onset + one vowel, or a lone hiatus vowel —
        never a grouped vowel pair)
     - duplicate words across files
     - duplicate glosses (warning; report includes POS so real clashes
       are distinguishable from cross-POS reuse)

  2. Documentation examples (documents/, manual/, pamphlets/, CLAUDE.md):
     - every Phi token inside fenced code blocks exists in the lexicon
     - tokens on gloss lines / translation lines are ignored
     - a small whitelist covers proper names and deliberate error forms

Usage:
    python3 scripts/validate_examples.py                # full check
    python3 scripts/validate_examples.py --lexicon-only
    python3 scripts/validate_examples.py --docs-only
    python3 scripts/validate_examples.py --paths manual/part4_grammar
    python3 scripts/validate_examples.py neighbors WORD # edit-distance-1
                                                        # collision check

Exit code 0 = no errors (warnings allowed), 1 = errors found.
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
MINIMAL_PAIRS_FILE = PROJECT_ROOT / "documents" / "MINIMAL_PAIRS_BASELINE.txt"
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"

DOC_ROOTS = ["documents", "manual", "pamphlets", "primer", "CLAUDE.md", "kia.md", "README.md"]

CONSONANTS = set("hklmnprstw")
DIGRAPHS = ("ph", "th", "sh", "wh")
VOWELS = set("aeiou")
PHI_LETTERS = CONSONANTS | VOWELS

REQUIRED_FIELDS = [
    "word", "gloss", "ipa", "syllables", "pos", "concept",
    "description", "sound_symbolism", "grammatical_notes", "pillars",
]
ALLOWED_FIELDS = set(REQUIRED_FIELDS) | {"slot", "tags"}
# Canonical key order for serialization (slot and tags appear in these
# positions when present).
FIELD_ORDER = [
    "word", "gloss", "ipa", "syllables", "slot", "pos", "concept",
    "description", "sound_symbolism", "grammatical_notes", "pillars",
    "tags",
]
PILLAR_KEYS = {
    "solarpunk-values",
    "secular-buddhist-philosophy",
    "art-nouveau-aesthetics",
    "peace-linguistics-practices",
    "pre-industrial-wisdom",
}
PILLAR_ORDER = [
    "solarpunk-values",
    "secular-buddhist-philosophy",
    "art-nouveau-aesthetics",
    "peace-linguistics-practices",
    "pre-industrial-wisdom",
]
POS_VALUES = {
    "noun", "verb", "adjective", "numeral", "particle", "preposition",
    "pronoun", "conjunction", "complementizer", "interrogative",
    "discourse", "classifier", "quantifier", "vocative", "interjection",
}
# The 13 canonical semantic domains (vocabulary/SEMANTIC_DOMAINS.md).
CANONICAL_TAGS = {
    "nature", "community", "wisdom", "creation", "dialogue", "temporal",
    "aesthetic", "emotion", "physical", "ritual", "cognition", "spatial",
    "activity",
}

IPA_CONSONANTS = {
    "h": "h", "k": "k", "l": "l", "m": "m", "n": "n̪", "p": "p",
    "r": "r", "s": "s", "t": "t̪", "w": "w",
    "ph": "ɸ", "th": "θ", "sh": "ʃ", "wh": "ʍ",
}
IPA_VOWELS = {"a": "ä", "e": "e̞", "i": "i", "o": "o̞", "u": "u"}


def canonical_ipa(word):
    """Derive the canonical IPA transcription from a word: syllable dots,
    penultimate stress, dental diacritics, true-mid vowel symbols."""
    syllables = syllabify(word)
    if syllables is None:
        return None
    out = []
    for s in syllables:
        onset, nucleus = s[:-1], s[-1]
        out.append(
            (IPA_CONSONANTS[onset] if onset else "") + IPA_VOWELS[nucleus]
        )
    stress = max(len(out) - 2, 0)
    out[stress] = "ˈ" + out[stress]
    return "/" + ".".join(out) + "/"


def gloss_filename(gloss):
    """The canonical filename stem for a gloss: lowercased, with every
    run of non-alphanumerics collapsed to a single hyphen."""
    return re.sub(r"[^a-z0-9]+", "-", gloss.lower()).strip("-")


def canonical_dump(data):
    """The canonical serialization of a lexicon entry: schema field
    order, canonical pillar order, alphabetical tags, 2-space indent,
    trailing newline."""
    ordered = {}
    for key in FIELD_ORDER:
        if key not in data:
            continue
        value = data[key]
        if key == "pillars":
            # canonical keys in canonical order, then any unknown keys
            # (kept so the validator can flag them, never silently lost)
            value = {k: value[k] for k in PILLAR_ORDER if k in value} | {
                k: v for k, v in value.items() if k not in PILLAR_ORDER
            }
        elif key == "tags":
            value = {k: value[k] for k in sorted(value)}
        ordered[key] = value
    return json.dumps(ordered, indent=2, ensure_ascii=False) + "\n"

# Tokens that legitimately appear in examples without being lexicon words.
WHITELIST = {
    # proper names used after the name particle `ne`
    "thala", "thanie", "hino", "mako",
    # deliberate error forms shown in the pamphlets
    "reno", "phenu",
    # foreign-language contrast examples
    "watashi",
}

# Lines matching any of these are gloss/metadata lines, not Phi text.
GLOSS_HINTS = re.compile(
    r"[A-Z0-9]"          # Leipzig abbreviations, person/number digits
    r"|[=→—]"  # =, arrows, em dash used in tables/notes
)


# ---------------------------------------------------------------------------
# Phonology
# ---------------------------------------------------------------------------

def syllabify(word):
    """Return the canonical syllable list for a word, or None if illegal.

    Greedy left-to-right: digraph+vowel, else consonant+vowel, else a lone
    vowel (legal only in hiatus, i.e. never word-initially).
    """
    syllables = []
    i = 0
    n = len(word)
    while i < n:
        if word[i : i + 2] in DIGRAPHS:
            onset = word[i : i + 2]
            j = i + 2
        elif word[i] in CONSONANTS:
            onset = word[i]
            j = i + 1
        elif word[i] in VOWELS:
            if i == 0:
                return None  # words must begin with a consonant onset
            onset = ""
            j = i
        else:
            return None  # illegal character
        if j >= n or word[j] not in VOWELS:
            return None  # onset without nucleus / closed syllable
        syllables.append(onset + word[j])
        i = j + 1
    return syllables


def check_word_phonology(word):
    """Return a list of error strings for a single word form."""
    errors = []
    if not word:
        return ["empty word"]
    bad = set(word) - PHI_LETTERS
    if bad:
        errors.append(f"illegal letters: {', '.join(sorted(bad))}")
        return errors
    if word[-1] not in VOWELS:
        errors.append("does not end in a vowel")
    if re.search(r"[aeiou]{3}", word):
        errors.append("three-vowel sequence (violates three-vowel constraint)")
    syllables = syllabify(word)
    if syllables is None:
        errors.append("cannot be parsed into legal (C)CV syllables")
        return errors
    seen = [s for s in syllables if len(s) >= 2]  # lone hiatus vowels exempt
    if len(seen) != len(set(seen)):
        dupes = sorted({s for s in seen if seen.count(s) > 1})
        errors.append(f"duplicate syllable(s): {', '.join(dupes)}")
    return errors


# ---------------------------------------------------------------------------
# Lexicon checks
# ---------------------------------------------------------------------------

def load_lexicon():
    """Load every vocabulary JSON entry. Returns (entries, load_errors)."""
    entries = []
    errors = []
    for path in sorted(VOCABULARY_DIR.rglob("*.json")):
        rel = path.relative_to(PROJECT_ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: JSON parse error: {e}")
            continue
        entries.append((rel, data))
    return entries, errors


def check_lexicon(entries):
    errors = []
    warnings = []
    by_word = {}
    by_gloss = {}

    for rel, data in entries:
        word = data.get("word", "")
        cls = rel.parts[1] if len(rel.parts) > 1 else ""

        for field in REQUIRED_FIELDS:
            if field not in data or data[field] in ("", [], {}):
                errors.append(f"{rel}: missing/empty required field '{field}'")
        extra = set(data.keys()) - ALLOWED_FIELDS
        if extra:
            errors.append(
                f"{rel}: undeclared field(s) {sorted(extra)} "
                f"(schema has additionalProperties: false)"
            )
        bad_pillars = set(data.get("pillars", {}).keys()) - PILLAR_KEYS
        if bad_pillars:
            errors.append(f"{rel}: invalid pillar key(s): {sorted(bad_pillars)}")

        for e in check_word_phonology(word):
            errors.append(f"{rel}: word '{word}': {e}")

        canonical = syllabify(word)
        stored = data.get("syllables")
        if canonical is not None and stored is not None and stored != canonical:
            errors.append(
                f"{rel}: syllables array {stored} does not match canonical "
                f"hiatus syllabification {canonical}"
            )

        # IPA must match the canonical derivation exactly
        want_ipa = canonical_ipa(word)
        if want_ipa is not None and data.get("ipa") != want_ipa:
            errors.append(
                f"{rel}: ipa {data.get('ipa')} != canonical {want_ipa}"
            )

        # pos values must come from the closed set
        bad_pos = set(data.get("pos", [])) - POS_VALUES
        if bad_pos:
            errors.append(f"{rel}: invalid pos value(s): {sorted(bad_pos)}")

        # slot: required for particles (0/1/2), forbidden otherwise
        is_particle = "particle" in data.get("pos", [])
        if is_particle and data.get("slot") not in (0, 1, 2):
            errors.append(f"{rel}: particle must have slot 0, 1, or 2")
        if not is_particle and "slot" in data:
            errors.append(f"{rel}: non-particle must not have a slot field")

        # tags: required for content words with canonical keys only;
        # forbidden for function words and interjections
        if cls == "content":
            tags = data.get("tags")
            if not tags:
                errors.append(f"{rel}: content word missing tags")
            else:
                bad_tags = set(tags) - CANONICAL_TAGS
                if bad_tags:
                    errors.append(f"{rel}: non-canonical tag(s): {sorted(bad_tags)}")
        elif "tags" in data:
            errors.append(f"{rel}: {cls} entry must not have tags")

        # filename must equal the lowercased gloss
        want_name = gloss_filename(data.get("gloss", "")) + ".json"
        if rel.name != want_name:
            errors.append(f"{rel}: filename should be '{want_name}' (gloss-derived)")

        # serialization must be canonical, byte for byte
        raw = (PROJECT_ROOT / rel).read_text(encoding="utf-8")
        if raw != canonical_dump(data):
            errors.append(f"{rel}: file is not in canonical serialization")

        by_word.setdefault(word, []).append(rel)
        gloss = data.get("gloss", "")
        pos = ",".join(data.get("pos", []))
        by_gloss.setdefault(gloss.lower(), []).append((word, pos, rel))

    # Minimal-pair ratchet: no two content words may sit at edit
    # distance 1 unless the pair is grandfathered in the committed
    # baseline (documents/MINIMAL_PAIRS_BASELINE.txt). The baseline
    # may only shrink: new pairs are errors, resolved pairs become
    # stale lines to prune.
    baseline = set()
    if MINIMAL_PAIRS_FILE.exists():
        for line in MINIMAL_PAIRS_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                baseline.add(tuple(line.split()))
    content_words = sorted(
        d.get("word", "") for rel, d in entries
        if len(rel.parts) > 1 and rel.parts[1] == "content"
    )
    live_pairs = set()
    for i, a in enumerate(content_words):
        for b in content_words[i + 1:]:
            if abs(len(a) - len(b)) > 1:
                continue
            if edit_distance_leq1(a, b):
                live_pairs.add((a, b))
    for pair in sorted(live_pairs - baseline):
        errors.append(
            f"minimal pair: content words '{pair[0]}' and '{pair[1]}' are "
            f"at edit distance 1 and not in the grandfathered baseline; "
            f"rename one (see documents/MINIMAL_PAIRS_BASELINE.txt)"
        )
    for pair in sorted(baseline - live_pairs):
        warnings.append(
            f"stale baseline line: '{pair[0]} {pair[1]}' is no longer a "
            f"minimal pair; prune it from MINIMAL_PAIRS_BASELINE.txt"
        )

    # Phi examples quoted inside JSON prose fields must use real words,
    # and sound-symbolism text may only claim sounds the word contains.
    lexicon_words = {d.get("word", "") for _, d in entries}
    QUOTED = re.compile(r"(?<![A-Za-z])['`]([a-z][a-z .?!]*?)['`](?![A-Za-z])")
    for rel, data in entries:
        word = data.get("word", "")
        prose_fields = {
            "description": data.get("description", ""),
            "sound_symbolism": data.get("sound_symbolism", ""),
            "grammatical_notes": data.get("grammatical_notes", ""),
        }
        for k, v in data.get("pillars", {}).items():
            prose_fields[f"pillars.{k}"] = v
        for field, text in prose_fields.items():
            for span in QUOTED.findall(text):
                tokens = [t.strip(".?!") for t in span.split()]
                tokens = [t for t in tokens if t]
                if not tokens or not all(set(t) <= PHI_LETTERS for t in tokens):
                    continue
                if len(tokens) == 1:
                    continue  # single quoted units are sound mentions
                known = sum(1 for t in tokens if t in lexicon_words)
                if known < max(1, len(tokens) / 2):
                    continue  # English phrase, not a Phi example
                for t in tokens:
                    if t not in lexicon_words and t not in WHITELIST:
                        errors.append(
                            f"{rel}: unknown Phi word '{t}' in {field}"
                        )
        # sound-symbolism claims: quoted 1-2 letter units must be sounds
        # or syllables the word actually has
        syls = syllabify(word) or []
        units = set(syls)
        for s in syls:
            if len(s) >= 2:
                units.add(s[:-1])  # onset
            units.add(s[-1])       # nucleus
        for claim in re.findall(
            r"(?<![A-Za-z])'([a-z]{1,3})'(?![A-Za-z])",
            data.get("sound_symbolism", ""),
        ):
            if set(claim) <= PHI_LETTERS and (
                claim in {"ph", "th", "sh", "wh"}
                or len(claim) <= 2
            ):
                if claim not in units and claim not in word:
                    warnings.append(
                        f"{rel}: sound_symbolism claims '{claim}' but "
                        f"'{word}' contains no such unit"
                    )

    for word, files in sorted(by_word.items()):
        if len(files) > 1:
            errors.append(
                f"DUPLICATE WORD '{word}' in: " + "; ".join(str(f) for f in files)
            )
    for gloss, items in sorted(by_gloss.items()):
        if len(items) > 1:
            detail = "; ".join(f"{w} ({p}) {f}" for w, p, f in items)
            warnings.append(f"duplicate gloss '{gloss}': {detail}")

    return errors, warnings


# ---------------------------------------------------------------------------
# Documentation example checks
# ---------------------------------------------------------------------------

def strip_brackets(line):
    """Remove [...] placeholder/label segments, (...) inline translation
    segments, and punctuation."""
    line = re.sub(r"\[[^\]]*\]", " ", line)
    line = re.sub(r"\([^)]*\)", " ", line)
    return re.sub(r"[.,!?\"'():;*`“”‘’]", " ", line)


def is_phi_line(raw_line, lexicon_words, strict=False):
    """Heuristic: a line/span consisting only of Phi-shaped tokens, enough
    of which are known lexicon words. The ratio requirement keeps English
    gloss/translation lines (which can be all lowercase and Phi-letter-
    compatible, e.g. "the person is here") out of the check while still
    flagging the unknown words on genuine Phi lines.

    strict=True (used for *italic* spans in prose, where short English
    fragments like "point to" can collide with Phi particles) requires a
    strict majority of known tokens instead of at-least-half."""
    if GLOSS_HINTS.search(raw_line):
        return False
    stripped = strip_brackets(raw_line)
    tokens = stripped.split()
    if not tokens:
        return False
    if not all(set(t) <= PHI_LETTERS for t in tokens):
        return False
    known = sum(1 for t in tokens if t in lexicon_words or t in WHITELIST)
    if strict:
        return known > len(tokens) / 2
    return known >= max(1, len(tokens) / 2)


def phi_tokens(raw_line):
    return strip_brackets(raw_line).split()


def check_docs(lexicon_words, paths=None):
    errors = []
    roots = paths or DOC_ROOTS
    files = []
    for root in roots:
        p = PROJECT_ROOT / root
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob("*.md")))

    for path in files:
        rel = path.relative_to(PROJECT_ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            errors.append(f"{rel}: unreadable: {e}")
            continue
        in_fence = False
        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                candidates = [(line, False)]
            else:
                # Outside fences, Phi appears as *italic* spans (prose,
                # tables, blockquotes). Single-token spans are skipped by
                # the ratio heuristic in is_phi_line; the known-bad-word
                # sweeps use grep directly, so that limitation is covered.
                candidates = [(c, True) for c in re.findall(r"\*([^*\n]+)\*", line)]
            for cand, strict in candidates:
                if not is_phi_line(cand, lexicon_words, strict=strict):
                    continue
                for tok in phi_tokens(cand):
                    if tok in lexicon_words or tok in WHITELIST:
                        continue
                    errors.append(f"{rel}:{lineno}: unknown Phi word '{tok}'")
            # IPA citations: a line that names a known word in backticks
            # and quotes exactly one /.../ transcription must quote that
            # word's canonical IPA. Single phonemes (/m/) and slashed
            # English words (/whom/) are not word transcriptions.
            if not in_fence:
                ipa_cites = re.findall(r"/[ˈ.\wä̞θʃɸʍ̪]+/", line)
                if len(ipa_cites) == 1:
                    named = [w for w in re.findall(r"`([a-z]+)`", line)
                             if w in lexicon_words]
                    inner = ipa_cites[0].strip("/")
                    if named and len(inner) > 1:
                        want = canonical_ipa(named[0])
                        is_word_cite = (
                            "." in inner or "ˈ" in inner
                            or (want and set(inner) <= set(want))
                        )
                        if want and is_word_cite and ipa_cites[0] != want:
                            errors.append(
                                f"{rel}:{lineno}: IPA for `{named[0]}` is "
                                f"{ipa_cites[0]}, canonical is {want}"
                            )
    return errors


# ---------------------------------------------------------------------------
# Collision helper (for new coinages)
# ---------------------------------------------------------------------------

def edit_distance_leq1(a, b):
    if a == b:
        return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) == 1
    if la > lb:
        a, b, la, lb = b, a, lb, la
    i = j = diffs = 0
    while i < la and j < lb:
        if a[i] != b[j]:
            diffs += 1
            if diffs > 1:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


def neighbors_report(entries, candidate):
    """Print every lexicon word within edit distance 1 of `candidate`."""
    phon = check_word_phonology(candidate)
    if phon:
        print(f"'{candidate}' is not phonotactically legal: {'; '.join(phon)}")
        return 1
    hits = []
    for rel, data in entries:
        w = data.get("word", "")
        if edit_distance_leq1(candidate, w):
            hits.append((w, data.get("gloss", ""), ",".join(data.get("pos", [])), rel))
    if not hits:
        print(f"'{candidate}' is legal and has no edit-distance-1 neighbors. Clear to coin.")
        return 0
    print(f"'{candidate}' has {len(hits)} close neighbor(s):")
    for w, gloss, pos, rel in hits:
        marker = "  EXACT" if w == candidate else "  ~"
        print(f"{marker} {w:12} {gloss:20} [{pos}]  {rel}")
    return 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Phi language validator")
    parser.add_argument("command", nargs="?", default="check",
                        choices=["check", "neighbors"],
                        help="check (default) or neighbors WORD")
    parser.add_argument("word", nargs="?", help="candidate word for 'neighbors'")
    parser.add_argument("--lexicon-only", action="store_true")
    parser.add_argument("--docs-only", action="store_true")
    parser.add_argument("--paths", nargs="*",
                        help="restrict doc checks to these paths (relative to repo root)")
    parser.add_argument("--show-warnings", action="store_true",
                        help="include duplicate-gloss warnings in output")
    args = parser.parse_args()

    entries, load_errors = load_lexicon()
    lexicon_words = {d.get("word", "") for _, d in entries}

    if args.command == "neighbors":
        if not args.word:
            parser.error("neighbors requires a candidate word")
        sys.exit(neighbors_report(entries, args.word))

    errors = list(load_errors)
    warnings = []

    if not args.docs_only:
        lex_errors, lex_warnings = check_lexicon(entries)
        errors.extend(lex_errors)
        warnings.extend(lex_warnings)

    if not args.lexicon_only:
        errors.extend(check_docs(lexicon_words, args.paths))

    for e in errors:
        print(f"ERROR   {e}")
    if args.show_warnings:
        for w in warnings:
            print(f"WARNING {w}")

    print(
        f"\n{len(entries)} lexicon entries checked. "
        f"{len(errors)} error(s), {len(warnings)} warning(s)"
        + ("" if args.show_warnings else " (use --show-warnings to list)")
        + "."
    )
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
