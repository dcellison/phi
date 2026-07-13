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
     - duplicate glosses (warning; case-sensitive — uppercase function
       labels never clash with lowercase content glosses)

  2. Documentation examples (documents/, manual/, pamphlets/, CLAUDE.md):
     - every Phi token inside fenced code blocks exists in the lexicon,
       except a productive name-form licensed directly by `ne`
     - gloss lines beneath Phi lines render each word by its lexicon
       gloss, verbatim (names after ne/honorifics gloss as themselves;
       translation lines and marked-wrong teaching examples are exempt)
     - a small whitelist covers deliberate error and contrast forms

  3. Phi quoted inside lexicon prose fields:
     - multiword examples use real words in canon Slot 1 order
     - single-word citations "'word' (gloss)" cite real words, and
       short lowercase parentheticals must contain the cited gloss

  4. Project prose policy:
     - lexicon prose and active Markdown reject the prohibited
       hyphenated adjective construction named in the voice guide

Usage:
    python3 scripts/validate_examples.py                # full check
    python3 scripts/validate_examples.py --lexicon-only
    python3 scripts/validate_examples.py --docs-only
    python3 scripts/validate_examples.py --paths manual/part4_grammar
    python3 scripts/validate_examples.py neighbors WORD # edit-distance-1
                                                        # collision check
    python3 scripts/validate_examples.py name FORM      # productive onym
                                                        # charter check

Exit code 0 = no errors (warnings allowed), 1 = errors found.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import compound_registry
import generate_reference
import name_forms

PROJECT_ROOT = Path(__file__).parent.parent
MINIMAL_PAIRS_FILE = PROJECT_ROOT / "documents" / "minimal_pairs_baseline.txt"
FOUR_SYLLABLE_MIGRATION_FILE = (
    PROJECT_ROOT / "documents" / "four_syllable_migration.tsv"
)
RETIRED_FORMS_FILE = PROJECT_ROOT / "documents" / "retired_forms.txt"
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
GENERATED_COMPOUNDS_FILE = PROJECT_ROOT / "manual" / "part7_reference" / "compounds.md"

DOC_ROOTS = ["documents", "manual", "pamphlets", "primer", "CLAUDE.md", "kia.md", "README.md", "short_road.md"]
ACTIVE_PROSE_ROOTS = ["canon.md", *DOC_ROOTS, "vocabulary"]
PROHIBITED_HYPHENATED_CONSTRUCTION = re.compile(
    r"\b[A-Za-z]+-" + "bearing" + r"\b",
    re.IGNORECASE,
)

CONSONANTS = set("hklmnprstw")
DIGRAPHS = ("ph", "th", "sh", "wh")
VOWELS = set("aeiou")
PHI_LETTERS = CONSONANTS | VOWELS


MIGRATION_FIELDS = ["old_form", "new_form", "gloss", "scope", "status"]
MIGRATION_SCOPES = {
    "base",
    "philosophical-reasoning",
    "systems-and-shared-infrastructure",
    "ecological-systems-and-material-life",
    "commons-and-collective-governance",
}
MIGRATION_ROW_COUNT = 112


def load_four_syllable_migration():
    """Load and structurally validate the finite breaking-change ledger."""
    errors = []
    with FOUR_SYLLABLE_MIGRATION_FILE.open(
        encoding="utf-8", newline=""
    ) as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != MIGRATION_FIELDS:
            return [], [
                f"{FOUR_SYLLABLE_MIGRATION_FILE.relative_to(PROJECT_ROOT)}: "
                f"expected columns {MIGRATION_FIELDS}, found {reader.fieldnames}"
            ]
        rows = list(reader)

    if len(rows) != MIGRATION_ROW_COUNT:
        errors.append(
            f"{FOUR_SYLLABLE_MIGRATION_FILE.relative_to(PROJECT_ROOT)}: "
            f"expected the fixed {MIGRATION_ROW_COUNT}-form ledger, found "
            f"{len(rows)} rows"
        )

    seen = set()
    seen_replacements = set()
    for lineno, row in enumerate(rows, 2):
        old_form = row["old_form"]
        new_form = row["new_form"]
        status = row["status"]
        prefix = (
            f"{FOUR_SYLLABLE_MIGRATION_FILE.relative_to(PROJECT_ROOT)}:"
            f"{lineno}"
        )
        if not all(row[field] for field in MIGRATION_FIELDS):
            errors.append(f"{prefix}: every migration field must be nonempty")
        if old_form in seen:
            errors.append(f"{prefix}: duplicate old form '{old_form}'")
        seen.add(old_form)
        if row["scope"] not in MIGRATION_SCOPES:
            errors.append(f"{prefix}: unknown migration scope '{row['scope']}'")
        if status != "replaced":
            errors.append(f"{prefix}: completed ledger row must be replaced")
        elif new_form == "-":
            errors.append(f"{prefix}: replaced row must name its new form")
        else:
            if new_form in seen_replacements:
                errors.append(f"{prefix}: duplicate replacement '{new_form}'")
            seen_replacements.add(new_form)
    return rows, errors


FOUR_SYLLABLE_MIGRATION, MIGRATION_ERRORS = load_four_syllable_migration()


def load_retired_forms():
    """Return short forms barred from lexical reassignment."""
    forms = set()
    for raw in RETIRED_FORMS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            forms.add(line.split()[0])
    return frozenset(forms)


RETIRED_FORMS = load_retired_forms()

REQUIRED_FIELDS = [
    "word", "gloss", "ipa", "syllables", "pos", "concept",
    "description", "sound_symbolism", "grammatical_notes", "pillars",
]
ALLOWED_FIELDS = set(REQUIRED_FIELDS) | {"slot", "tags", "modules"}
# Canonical key order for serialization (optional classification fields
# appear after the semantic content they classify).
FIELD_ORDER = [
    "word", "gloss", "ipa", "syllables", "slot", "pos", "concept",
    "description", "sound_symbolism", "grammatical_notes", "pillars",
    "tags", "modules",
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
# The 13 canonical semantic domains (vocabulary/semantic_domains.md).
CANONICAL_TAGS = {
    "nature", "community", "wisdom", "creation", "dialogue", "temporal",
    "aesthetic", "emotion", "physical", "ritual", "cognition", "spatial",
    "activity",
}
# Optional lexical modules recorded in documents/modules/README.md. Module
# membership changes what a learner may choose to study, never how Phi parses.
CANONICAL_MODULES = {
    "household-and-daily-life",
    "medical-and-bodily-care",
    "systems-and-shared-infrastructure",
    "philosophical-reasoning",
    "accessibility-and-participation",
    "commons-and-collective-governance",
    "ecological-systems-and-material-life",
    "work-craft-and-repair",
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
        elif key == "modules":
            value = sorted(value)
        ordered[key] = value
    return json.dumps(ordered, indent=2, ensure_ascii=False) + "\n"


def iter_string_fields(value, prefix=""):
    """Yield dotted field paths and strings from nested schema data."""
    if isinstance(value, str):
        yield prefix, value
    elif isinstance(value, dict):
        for key, item in value.items():
            child = f"{prefix}.{key}" if prefix else key
            yield from iter_string_fields(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child = f"{prefix}[{index}]"
            yield from iter_string_fields(item, child)


def contains_prohibited_hyphenated_construction(text):
    """Return whether project prose uses the banned construction."""
    return PROHIBITED_HYPHENATED_CONSTRUCTION.search(text) is not None


def prohibited_prose_errors(rel, text):
    """Report prohibited construction locations without repeating it."""
    return [
        f"{rel}:{lineno}: prohibited hyphenated adjective construction"
        for lineno, line in enumerate(text.splitlines(), start=1)
        if contains_prohibited_hyphenated_construction(line)
    ]

# Tokens that legitimately appear in examples without being lexicon words.
WHITELIST = {
    # deliberate error form shown in the pamphlets
    "reno",
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


def name_atom_errors(token, lexicon_words, content_words):
    """Validate the atom selected by ``ne`` or an honorific."""
    if token in lexicon_words:
        if token in content_words:
            return []
        return ["matches a current function or non-content word"]
    return name_forms.form_errors(token)


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
        pos = data.get("pos", [])
        if "noun" in pos and "verb" in pos:
            errors.append(f"{rel}: pos lists both noun and verb - refused by ruling: a deed names its event; a thing does not name its deed")
        if "adjective" in pos and "noun" in pos:
            errors.append(f"{rel}: pos lists both adjective and noun - refused by ruling: a quality names itself (quality-noun rule); a thing describes by position")
        if "adjective" in pos and "verb" in pos:
            errors.append(f"{rel}: pos lists both adjective and verb - refused by ruling: qualities do not name their acts")
        if "content" in path.parts and len(pos) != 1:
            errors.append(f"{rel}: content entries carry exactly one part of speech (one word, one class)")
        # the function-word shape charter (canon, settled 2026-07-06)
        syls = syllabify(data.get("word", "")) or []
        n = len(syls)
        hiatus2 = n == 2 and len(syls[1]) == 1
        cls = pos[0] if len(pos) == 1 else None
        charter_violation = None
        if cls in ("particle", "numeral"):
            if n != 1 or len(syls[0]) != 2:
                charter_violation = "bare CV monosyllable (the grammar's atoms)"
        elif cls == "preposition":
            if not hiatus2:
                charter_violation = "hiatus disyllable (C)V.V (the relator shape)"
        elif cls == "pronoun":
            if n != 2:
                charter_violation = "disyllable (core (C)V.V; the -so pair CV.CV)"
        elif cls in ("complementizer", "vocative", "classifier"):
            if n != 2 or hiatus2:
                charter_violation = "plain disyllable (the frame shape)"
        elif cls == "conjunction":
            if n != 2:
                charter_violation = "disyllable (frame shape, or relator shape for clause-relators)"
        elif cls == "discourse":
            if n not in (2, 3) or syls[0][:2] not in DIGRAPHS:
                charter_violation = (
                    "content-shaped (two or three syllables) opening with "
                    "a fricative breath (the breath before reframing)"
                )
        elif cls in ("quantifier", "interrogative"):
            if n not in (2, 3):
                charter_violation = "content-shaped (two or three syllables)"
        if charter_violation:
            errors.append(
                f"{rel}: shape charter violation: {cls} must be "
                f"{charter_violation}"
            )
        entries.append((rel, data))
    return entries, errors


def check_lexicon(entries):
    errors = list(MIGRATION_ERRORS)
    warnings = []
    by_word = {}
    by_gloss = {}

    for rel, data in entries:
        word = data.get("word", "")
        cls = rel.parts[1] if len(rel.parts) > 1 else ""

        for field, text in iter_string_fields(data):
            if contains_prohibited_hyphenated_construction(text):
                errors.append(
                    f"{rel}: prohibited hyphenated adjective construction "
                    f"in {field}"
                )

        if word in RETIRED_FORMS:
            errors.append(f"{rel}: word '{word}' is a retired Phi form")

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
        if canonical is not None and len(canonical) > 3:
            errors.append(
                f"{rel}: word '{word}' exceeds the universal "
                "three-syllable lexical ceiling"
            )
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

        modules = data.get("modules")
        if modules is not None:
            if cls != "content":
                errors.append(f"{rel}: {cls} entry must not have modules")
            elif not isinstance(modules, list) or not modules:
                errors.append(f"{rel}: modules must be a non-empty list")
            elif any(not isinstance(module, str) for module in modules):
                errors.append(f"{rel}: every module must be a string")
            else:
                duplicates = sorted({module for module in modules if modules.count(module) > 1})
                if duplicates:
                    errors.append(f"{rel}: duplicate module(s): {duplicates}")
                bad_modules = set(modules) - CANONICAL_MODULES
                if bad_modules:
                    errors.append(f"{rel}: non-canonical module(s): {sorted(bad_modules)}")

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
        # exact case: function words gloss as uppercase labels (gloss-line
        # ruling), so case is the disambiguator, not an accident
        by_gloss.setdefault(gloss, []).append((word, pos, rel))

    # Minimal-pair ratchet: no two content words may sit at edit
    # distance 1 unless the pair is grandfathered in the committed
    # baseline (documents/minimal_pairs_baseline.txt). The baseline
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
            f"rename one (see documents/minimal_pairs_baseline.txt)"
        )
    for pair in sorted(baseline - live_pairs):
        warnings.append(
            f"stale baseline line: '{pair[0]} {pair[1]}' is no longer a "
            f"minimal pair; prune it from minimal_pairs_baseline.txt"
        )

    # Phi examples quoted inside JSON prose fields must use real words
    # in canon Slot 1 order, and single-word citations "'word' (gloss)"
    # must cite real words with their real glosses; sound-symbolism text
    # may only claim sounds the word contains.
    lexicon_words = {d.get("word", "") for _, d in entries}
    content_words = {
        d.get("word", "") for rel, d in entries
        if len(rel.parts) > 1 and rel.parts[1] == "content"
    }
    gloss_by_word = {d.get("word", ""): d.get("gloss", "") for _, d in entries}
    prepositions = {
        d.get("word", "") for _, d in entries
        if "preposition" in (d.get("pos") or [])
    }
    QUOTED = re.compile(r"(?<![A-Za-z])['`]([a-z][a-z .?!]*?)['`](?![A-Za-z])")
    CITED = re.compile(r"(?<![A-Za-z])'([a-z]{3,})' \(([^)]+)\)")
    for rel, data in entries:
        word = data.get("word", "")
        own_units = set()
        for s in syllabify(word) or []:
            own_units.add(s)
            if len(s) >= 2:
                own_units.add(s[:-1])
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
                name_indices = name_forms.marked_atom_indices(tokens)
                for index, t in enumerate(tokens):
                    if index in name_indices:
                        atom_errors = name_atom_errors(
                            t, lexicon_words, content_words
                        )
                        if not atom_errors:
                            continue
                        errors.append(
                            f"{rel}: invalid productive name-form '{t}' "
                            f"in {field}: {'; '.join(atom_errors)}"
                        )
                        continue
                    if t not in lexicon_words and t not in WHITELIST:
                        errors.append(
                            f"{rel}: unknown Phi word '{t}' in {field}"
                        )
                for run in slot1_misorders(tokens):
                    errors.append(
                        f"{rel}: Slot 1 order violation '{run}' in {field} "
                        f"(canon: Tense > Aspect > Voice > Evidentiality > "
                        f"Modality > Negation)"
                    )
                for run in preposition_misplacements(span, prepositions):
                    errors.append(
                        f"{rel}: postposed preposition near '{run}' in "
                        f"{field} (canon: every preposition precedes its "
                        f"object)"
                    )
            for cited, paren in CITED.findall(text):
                if not set(cited) <= PHI_LETTERS or cited == word:
                    continue
                if cited in lexicon_words:
                    g = re.sub(r"\s*\(.*", "", gloss_by_word[cited]).strip()
                    if g.isupper():
                        continue  # label gloss; the parenthetical explains meaning
                    if not re.fullmatch(r"[a-z ,/-]+", paren) or len(paren.split()) > 3:
                        continue  # example, translation, or long explanation
                    if g.lower() not in paren.lower():
                        errors.append(
                            f"{rel}: {field} cites '{cited}' as ({paren}) "
                            f"but its gloss is '{gloss_by_word[cited]}'"
                        )
                elif cited not in own_units and cited not in WHITELIST:
                    if re.fullmatch(r"[A-Za-z ,/-]+", paren):
                        errors.append(
                            f"{rel}: {field} cites unknown word '{cited}' ({paren})"
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
    redundant_long_retirements = sorted(
        form for form in RETIRED_FORMS
        if len(syllabify(form) or []) > 3
    )
    if redundant_long_retirements:
        errors.append(
            "retired_forms.txt must not list four-syllable forms; the "
            "universal lexical ceiling already excludes them: "
            f"{redundant_long_retirements}"
        )
    for row in FOUR_SYLLABLE_MIGRATION:
        old_form = row["old_form"]
        old_syllables = syllabify(old_form)
        if old_syllables is None or len(old_syllables) != 4:
            errors.append(
                "four-syllable migration ledger old form must contain "
                f"exactly four Phi syllables: '{old_form}'"
            )
        new_form = row["new_form"]
        if old_form in by_word:
            errors.append(
                f"replaced migration form remains in the lexicon: '{old_form}'"
            )
        if new_form not in by_word:
            errors.append(
                f"migration replacement is missing from the lexicon: "
                f"'{new_form}'"
            )
        new_syllables = syllabify(new_form)
        if new_syllables is None or len(new_syllables) > 3:
            errors.append(
                "migration replacement must be a Phi form of at most three "
                f"syllables: '{new_form}'"
            )
    for gloss, items in sorted(by_gloss.items()):
        if len(items) > 1:
            detail = "; ".join(f"{w} ({p}) {f}" for w, p, f in items)
            warnings.append(f"duplicate gloss '{gloss}': {detail}")

    return errors, warnings


# ---------------------------------------------------------------------------
# Documentation example checks
# ---------------------------------------------------------------------------

SLOT1_RANK = {
    "to": 1, "so": 1,                             # tense
    "ki": 2, "si": 2, "pa": 2, "te": 2, "ro": 2,  # aspect
    "se": 3, "ka": 3,                             # voice (canon: ka is voice)
    "hi": 4, "ke": 4, "ti": 4, "ho": 4,           # evidentiality
    "po": 5, "na": 5,                             # modality
    "ma": 6,                                      # negation
}


def slot1_misorders(tokens):
    """Runs of adjacent Slot 1 particles that violate the canon order
    (Tense > Aspect > Voice > Evidentiality > Modality > Negation) or the
    one-per-rank rule. The single licensed same-rank pairing is voice's
    'se ka' (the passive of a causative)."""
    bad = []
    i = 0
    while i < len(tokens):
        if tokens[i] in SLOT1_RANK:
            j = i
            while j < len(tokens) and tokens[j] in SLOT1_RANK:
                j += 1
            run = tokens[i:j]
            ranks = [SLOT1_RANK[t] for t in run]
            reversed_ = any(b < a for a, b in zip(ranks, ranks[1:]))
            doubled = any(
                a == b and (run[k], run[k + 1]) != ("se", "ka")
                for k, (a, b) in enumerate(zip(ranks, ranks[1:]))
            )
            if reversed_ or doubled:
                bad.append(" ".join(run))
            i = j
        else:
            i += 1
    return bad


CITATION_SOURCES = {
    "pamphlets/news_from_nowhere_ch1.md": (
        "morris", "pamphlets/sources/news_from_nowhere.txt"
    ),
    "pamphlets/velveteen_rabbit.md": (
        "williams", "pamphlets/sources/velveteen_rabbit.txt"
    ),
    "pamphlets/north_wind_and_sun.md": (
        "aesop", "pamphlets/sources/aesop_for_children.txt"
    ),
    "pamphlets/schleicher_fable.md": (
        "schleicher-en", "pamphlets/sources/schleicher_1868_english.txt"
    ),
    "pamphlets/babel_text.md": (
        "kjv", "pamphlets/sources/kjv_genesis.txt"
    ),
    "pamphlets/prophet_excerpts.md": (
        "gibran", "pamphlets/sources/the_prophet.txt"
    ),
    "pamphlets/metta_sutta.md": (
        "fausboll", "pamphlets/sources/sutta_nipata_fausboll.txt"
    ),
    "pamphlets/tao_te_ching.md": (
        "legge", "pamphlets/sources/tao_teh_king_1891.txt"
    ),
    "pamphlets/heart_sutra.md": (
        "muller", "pamphlets/sources/buddhist_mahayana_texts_1894.txt"
    ),
    "pamphlets/human_rights_article_one.md": (
        "udhr", "pamphlets/sources/udhr_1948.txt"
    ),
}

PAIRED_CITATION_SCOPES = {
    "pamphlets/north_wind_and_sun.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/schleicher_fable.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/human_rights_article_one.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/babel_text.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/heart_sutra.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/tao_te_ching.md": (
        "## Close translation",
        "## Transmutation",
    ),
    "pamphlets/prophet_excerpts.md": (
        "## On children: close translation",
        "## On children: transmutation",
    ),
}


def citation_scope(doc_rel, text, position):
    """Return the paired-rendering section containing a citation."""
    scopes = PAIRED_CITATION_SCOPES.get(doc_rel)
    if not scopes:
        return None
    candidates = (
        (text.rfind(heading, 0, position), heading)
        for heading in scopes
    )
    start, heading = max(candidates)
    return heading if start >= 0 else None


def check_citations():
    """Source citations are ground truth: every fragment of every
    citation line must appear verbatim in the stored source text. A
    source clause normally belongs to exactly one unit. A declared paired
    work may cite it once in each rendering, but never twice inside one
    rendering. Ellipses mark omissions and split a citation into
    independently verified fragments; hyphenated line breaks in the
    source are rejoined before matching."""
    errors = []
    for doc_rel, (prefix, src_rel) in CITATION_SOURCES.items():
        doc_path = PROJECT_ROOT / doc_rel
        src_path = PROJECT_ROOT / src_rel
        if not doc_path.exists() or not src_path.exists():
            errors.append(f"{doc_rel}: citation source {src_rel} missing")
            continue
        src = src_path.read_text(encoding="utf-8").replace("-\n", "-")
        src_norm = " ".join(src.split())
        seen = {}
        pattern = re.compile(rf'^{re.escape(prefix)}: "(.*)"$', re.M)
        text = doc_path.read_text(encoding="utf-8")
        for m in pattern.finditer(text):
            cite = m.group(1)
            lineno = text.count("\n", 0, m.start()) + 1
            scope = citation_scope(doc_rel, text, m.start())
            previous = seen.setdefault(cite, [])
            shared_scope = next(
                (line for line, prior_scope in previous
                 if prior_scope == scope),
                None,
            )
            if previous and (scope is None or shared_scope is not None):
                prior_line = shared_scope or previous[0][0]
                errors.append(
                    f"{doc_rel}:{lineno}: citation shared with line "
                    f"{prior_line}: \"{cite[:50]}\" (each rendering "
                    f"cites a source clause at most once)"
                )
            previous.append((lineno, scope))
            for frag in cite.replace('\\"', '"').split("..."):
                frag_norm = " ".join(frag.split())
                if frag_norm and frag_norm not in src_norm:
                    errors.append(
                        f"{doc_rel}:{lineno}: citation fragment not "
                        f"verbatim in {src_rel}: \"{frag_norm[:60]}\""
                    )
    return errors


def preposition_misplacements(raw_line, prepositions):
    """The detectable half of the postposed-relator error. Canon rules
    that every preposition precedes its object and never moves, so a
    preposition followed by a Slot 1 particle, or standing last in its
    sentence, cannot be standing before its object. The check runs per
    sentence; prepositions after 'rena' in the same sentence are exempt,
    since an oblique relative gaps the object and leaves the preposition
    directly before the verb phrase (canon's oblique-relative ruling).
    Sentences of fewer than two tokens are skipped: a single-token span
    is a word mention, not an ordered phrase. A preposition directly
    before another preposition stays legal (the Metta Sutta's 'wei leo
    waero', to the sky above), and a postposed preposition followed by
    a plain noun reads the same as a well-formed phrase, so this check
    is a net, not a proof; the grammar-order pass in review remains the
    full check."""
    bad = []
    for sentence in raw_line.split("."):
        tokens = strip_brackets(sentence).split()
        if len(tokens) < 2:
            continue
        rena_seen = False
        for i, tok in enumerate(tokens):
            if tok == "rena":
                rena_seen = True
                continue
            if tok not in prepositions or rena_seen:
                continue
            nxt = tokens[i + 1] if i + 1 < len(tokens) else None
            if nxt is None or nxt in SLOT1_RANK:
                bad.append(" ".join(tokens[max(0, i - 1):i + 2]))
    return bad


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
    name_indices = name_forms.marked_atom_indices(tokens)
    known = sum(
        1 for index, token in enumerate(tokens)
        if token in lexicon_words or token in WHITELIST
        or (index in name_indices and not name_forms.form_errors(token))
    )
    if strict:
        return known > len(tokens) / 2
    return known >= max(1, len(tokens) / 2)


def phi_tokens(raw_line):
    return strip_brackets(raw_line).split()


# Household-corpus words that recur as names and gloss as themselves when
# used bare. Productive onyms absent from the current lexicon are handled
# structurally after `ne`;
# they do not belong in this set.
NAMES = {"sulae", "siora", "keruko", "thinoe", "misheko", "lohau"}
HONORIFIC_GLOSSES = {"HON.RESPECT", "HON.INTIM", "HON.ROLE"}


def expected_gloss_stream(phi_line, gloss_of):
    """The gloss-line token stream a Phi line licenses, as a list of
    acceptable-token sets: each word's lexicon gloss verbatim with
    parenthetical disambiguators dropped (the gloss-lines ruling); a
    name after 'ne' or an honorific glossing as itself; a productive
    onym absent from the current lexicon also glossing as itself; and a bare
    register name glossing as itself or as its word. None if any other
    token is unknown — those are reported by the unknown-word check."""
    out = []
    expecting_name = False

    def append_core(fragment):
        nonlocal expecting_name
        for tok in fragment.split():
            core = tok.strip(".,;:!?*\"'").lower()
            if not core:
                continue
            g = gloss_of.get(core)
            if g is None:
                if expecting_name and not name_forms.form_errors(core):
                    out.append({core})
                    expecting_name = False
                    continue
                return False
            g = re.sub(r"\s*\([^)]*\)", "", g).strip()
            is_label = g.isupper()
            if expecting_name and not is_label:
                out.append({core})
                expecting_name = False
            elif core in NAMES:
                out.append({core, g})
            else:
                for word in g.split():
                    out.append({word})
            if core == "ne" or g in HONORIFIC_GLOSSES:
                expecting_name = True
            elif not is_label:
                expecting_name = False
        return True

    if not append_core(phi_line):
        return None
    return out


def gloss_line_tokens(gloss_line):
    """Split a gloss line and discard ordinary sentence punctuation."""
    return [
        token for raw in gloss_line.split()
        if (token := raw.strip(".,;:!?\"'"))
    ]


def check_gloss_lines(rel, text, lexicon_words, gloss_of):
    """The gloss-line lint: the line beneath a full Phi line (fenced, or
    a full-line bold example) must render each word by its lexicon gloss,
    verbatim. Guards: lines containing '(' are translations, next-lines
    that are themselves Phi are continuations, and a line only counts as
    a gloss line when most of its tokens come from gloss vocabulary."""
    errors = []
    gloss_vocab = set()
    for g in gloss_of.values():
        gloss_vocab.update(re.sub(r"\s*\([^)]*\)", "", g).split())
    lines = text.splitlines()
    in_fence = False
    wrong_until = -1
    for idx, line in enumerate(lines):
        if "**wrong" in line.lower():
            # deliberately ill-formed teaching examples (common-errors
            # pamphlets): the marked fence is exempt
            wrong_until = idx + 6
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if idx <= wrong_until:
            continue
        phi_src = None
        if in_fence:
            cand = re.sub(r"^\s*[A-Za-z]:\s+", "", line)
            if is_phi_line(cand.lower(), lexicon_words):
                phi_src = cand
        else:
            m = re.match(r"^\s*(?:>\s*)?\*\*([^*]+)\*\*\s*$", line)
            if m and is_phi_line(m.group(1).lower(), lexicon_words, strict=True):
                phi_src = m.group(1)
        if not phi_src or phi_src.lstrip().startswith("*") or idx + 1 >= len(lines):
            continue
        nxt = lines[idx + 1]
        if nxt.strip().startswith("```"):
            continue
        gl = re.sub(r"^\s*(?:>\s*)?", "", nxt).strip().strip("*")
        if not gl or "(" in gl or gl[0] in "\"“":
            continue  # translation line, not a gloss line
        if is_phi_line(gl.lower(), lexicon_words):
            continue
        actual = gloss_line_tokens(gl)
        if not actual:
            continue
        if sum(1 for t in actual if t in gloss_vocab) <= len(actual) / 2:
            continue
        expected = expected_gloss_stream(phi_src, gloss_of)
        if expected is None:
            continue
        if len(actual) != len(expected) or any(
            a not in s for a, s in zip(actual, expected)
        ):
            want = " ".join("/".join(sorted(s)) for s in expected)
            errors.append(
                f"{rel}:{idx + 2}: gloss line mismatch: expected "
                f"'{want}' got '{' '.join(actual)}'"
            )
    return errors


def check_docs(lexicon_words, paths=None, gloss_of=None, prepositions=None,
               content_words=None):
    errors = []
    prepositions = prepositions or set()
    content_words = content_words or set()
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
        if gloss_of:
            errors.extend(check_gloss_lines(rel, text, lexicon_words, gloss_of))
        in_fence = False
        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                # dialogue speaker labels (A:, B:) are apparatus, not Phi
                candidates = [(re.sub(r"^\s*[A-Za-z]:\s+", "", line), False, False)]
            else:
                # Outside fences, Phi appears as **bold** example lines
                # (checked in full, like fenced lines) and *italic* spans
                # (prose citations: strict ratio, English commas excused).
                # Single-token spans are skipped by the ratio heuristic in
                # is_phi_line; the known-bad-word sweeps use grep directly,
                # so that limitation is covered.
                bolds = re.findall(r"\*\*([^*\n]+)\*\*", line)
                rest = re.sub(r"\*\*[^*\n]+\*\*", " ", line)
                candidates = [(c, True, False) for c in bolds]
                candidates += [(c, True, True) for c in re.findall(r"\*([^*\n]+)\*", rest)]
            for cand, strict, excuse_commas in candidates:
                # detection is case-blind so capitalized Phi cannot hide
                if not is_phi_line(cand.lower(), lexicon_words, strict=strict):
                    continue
                visible_tokens = [
                    tok.strip(".,;:!?\"'()*")
                    for tok in cand.split()
                ]
                visible_name_indices = name_forms.marked_atom_indices(
                    [token.lower() for token in visible_tokens]
                )
                for index, core in enumerate(visible_tokens):
                    marked_onym = (
                        index in visible_name_indices
                        and not name_forms.form_errors(core.lower())
                    )
                    if (core and core != core.lower()
                            and (core.lower() in lexicon_words or marked_onym)):
                        errors.append(f"{rel}:{lineno}: capital letter in Phi text: '{core}' (Phi has no capitals; ne announces a name)")
                # periods only in Phi text: '?' is checked everywhere; ','
                # only on fenced lines (prose cites Phi words inside English
                # sentences whose commas are English), with parenthetical
                # annotations stripped first
                bare = re.sub(r"\([^)]*\)", "", cand)
                if "?" in bare or "!" in bare or ";" in bare or (not excuse_commas and "," in bare):
                    errors.append(f"{rel}:{lineno}: punctuation in Phi text: periods only (no commas or question marks)")
                tokens = phi_tokens(cand.lower())
                name_indices = name_forms.marked_atom_indices(tokens)
                for index, tok in enumerate(tokens):
                    if index in name_indices:
                        atom_errors = name_atom_errors(
                            tok, lexicon_words, content_words
                        )
                        if not atom_errors:
                            continue
                        errors.append(
                            f"{rel}:{lineno}: invalid productive name-form "
                            f"'{tok}': {'; '.join(atom_errors)}"
                        )
                        continue
                    if tok in lexicon_words or tok in WHITELIST:
                        continue
                    errors.append(f"{rel}:{lineno}: unknown Phi word '{tok}'")
                # Slot 1 order is canon-fixed; lines prefixed with '*' are
                # deliberately ill-formed teaching examples and are skipped.
                if not cand.lstrip().startswith("*"):
                    for run in slot1_misorders(tokens):
                        errors.append(f"{rel}:{lineno}: Slot 1 order violation '{run}' (canon: Tense > Aspect > Voice > Evidentiality > Modality > Negation)")
                    for run in preposition_misplacements(cand.lower(), prepositions):
                        errors.append(f"{rel}:{lineno}: postposed preposition near '{run}' (canon: every preposition precedes its object)")
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


def check_active_prose(paths=None):
    """Check active Markdown while deliberately leaving archive untouched."""
    roots = paths or ACTIVE_PROSE_ROOTS
    files = set()
    for root in roots:
        path = PROJECT_ROOT / root
        if path.is_file() and path.suffix == ".md":
            files.add(path)
        elif path.is_dir():
            files.update(path.rglob("*.md"))

    errors = []
    for path in sorted(files):
        rel = path.relative_to(PROJECT_ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            errors.append(f"{rel}: unreadable: {error}")
            continue
        errors.extend(prohibited_prose_errors(rel, text))
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


def name_report(entries, candidate):
    """Validate one proposed productive onym for direct use after ``ne``."""
    lexicon_words = {data.get("word", "") for _, data in entries}
    content_words = {
        data.get("word", "") for rel, data in entries
        if len(rel.parts) > 1 and rel.parts[1] == "content"
    }
    errors = name_atom_errors(candidate, lexicon_words, content_words)
    if errors:
        print(f"'{candidate}' is not a valid productive name-form: "
              f"{'; '.join(errors)}")
        return 1
    syllables = name_forms.syllabify(candidate) or []
    if candidate in content_words:
        print(
            f"'{candidate}' is a listed content word and may be borne as "
            f"a name after ne ({'.'.join(syllables)})."
        )
    else:
        print(
            f"'{candidate}' is a valid productive name-form after ne "
            f"({'.'.join(syllables)}); it does not become a lexicon word."
        )
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def check_compound_registry(lexicon_words):
    """The compound registry stays in step with the lexicon and its
    generated Part VII page: every member word exists, no row repeats,
    and the reference page matches what the registry would generate."""
    errors = []
    compounds = compound_registry.load_compounds()
    if not compounds:
        errors.append("documents/compounds.md: no registry rows parsed")
    seen = set()
    for c in compounds:
        if c["compound"] in seen:
            errors.append(
                f"documents/compounds.md: duplicate registry row for `{c['compound']}`"
            )
        seen.add(c["compound"])
        for token in c["tokens"]:
            if token not in lexicon_words:
                errors.append(
                    f"documents/compounds.md: compound `{c['compound']}` "
                    f"uses '{token}', which is not in the lexicon"
                )
    expected = generate_reference.compounds_reference(compounds)
    if (not GENERATED_COMPOUNDS_FILE.exists()
            or GENERATED_COMPOUNDS_FILE.read_text(encoding="utf-8") != expected):
        errors.append(
            "manual/part7_reference/compounds.md is stale; "
            "rerun: python3 scripts/generate_reference.py"
        )
    return errors


def main():
    parser = argparse.ArgumentParser(description="Phi language validator")
    parser.add_argument("command", nargs="?", default="check",
                        choices=["check", "neighbors", "name"],
                        help="check (default), neighbors WORD, or name FORM")
    parser.add_argument("word", nargs="?",
                        help="candidate for 'neighbors' or 'name'")
    parser.add_argument("--lexicon-only", action="store_true")
    parser.add_argument("--docs-only", action="store_true")
    parser.add_argument("--paths", nargs="*",
                        help="restrict doc checks to these paths (relative to repo root)")
    parser.add_argument("--show-warnings", action="store_true",
                        help="include duplicate-gloss warnings in output")
    args = parser.parse_args()

    entries, load_errors = load_lexicon()
    lexicon_words = {d.get("word", "") for _, d in entries}
    content_words = {
        d.get("word", "") for rel, d in entries
        if len(rel.parts) > 1 and rel.parts[1] == "content"
    }

    if args.command == "neighbors":
        if not args.word:
            parser.error("neighbors requires a candidate word")
        sys.exit(neighbors_report(entries, args.word))
    if args.command == "name":
        if not args.word:
            parser.error("name requires a candidate form")
        sys.exit(name_report(entries, args.word))

    errors = list(load_errors)
    warnings = []

    if not args.docs_only:
        lex_errors, lex_warnings = check_lexicon(entries)
        errors.extend(lex_errors)
        warnings.extend(lex_warnings)

    if not args.lexicon_only:
        gloss_of = {d.get("word", ""): d.get("gloss", "") for _, d in entries}
        prepositions = {
            d.get("word", "") for _, d in entries
            if "preposition" in (d.get("pos") or [])
        }
        errors.extend(check_docs(
            lexicon_words, args.paths, gloss_of, prepositions, content_words
        ))
        errors.extend(check_active_prose(args.paths))
        if not args.paths:
            errors.extend(check_citations())
        if not args.paths or "documents/compounds.md" in args.paths:
            errors.extend(check_compound_registry(lexicon_words))

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
