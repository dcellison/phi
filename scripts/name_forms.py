#!/usr/bin/env python3
"""Productive Phi-form proper names licensed by ``ne``.

Name-forms are one lowercase content-shaped token of two or three ordinary
Phi syllables. They are not lexicon entries, so lexical collision checks do
not apply, but retired Phi forms remain unavailable for reassignment.
"""

import re
from pathlib import Path


CONSONANTS = set("hklmnprstw")
DIGRAPHS = ("ph", "th", "sh", "wh")
VOWELS = set("aeiou")
PHI_LETTERS = CONSONANTS | VOWELS

NAME_MARKER = "ne"
HONORIFICS = {"sa", "ni", "le"}

RETIRED_FORMS_FILE = (
    Path(__file__).resolve().parent.parent / "documents" / "retired_forms.txt"
)


def load_retired_forms():
    """Return forms that historical Phi used but current Phi must not reuse."""
    forms = set()
    for raw in RETIRED_FORMS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            forms.add(line.split()[0])
    return frozenset(forms)


RETIRED_FORMS = load_retired_forms()


def syllabify(word):
    """Return Phi syllables for *word*, or ``None`` if it is ill-formed."""
    syllables = []
    i = 0
    while i < len(word):
        if word[i:i + 2] in DIGRAPHS:
            onset = word[i:i + 2]
            j = i + 2
        elif word[i] in CONSONANTS:
            onset = word[i]
            j = i + 1
        elif word[i] in VOWELS and i > 0:
            onset = ""
            j = i
        else:
            return None
        if j >= len(word) or word[j] not in VOWELS:
            return None
        syllables.append(onset + word[j])
        i = j + 1
    return syllables


def form_errors(word):
    """Return violations of the productive single-token onym charter."""
    errors = []
    if not word:
        return ["empty name-form"]
    if word in RETIRED_FORMS:
        errors.append("is a retired Phi form")
    if word != word.lower():
        errors.append("must be lowercase")
    bad = set(word) - PHI_LETTERS
    if bad:
        errors.append("contains non-Phi letters")
        return errors
    if word[-1] not in VOWELS:
        errors.append("must end in a vowel")
    if re.search(r"[aeiou]{3}", word):
        errors.append("contains three adjacent vowels")
    syllables = syllabify(word)
    if syllables is None:
        errors.append("cannot be parsed into Phi open syllables")
        return errors
    if len(syllables) not in (2, 3):
        errors.append("must contain two or three syllables")
    onset_syllables = [s for s in syllables if len(s) >= 2]
    duplicates = sorted({
        syllable for syllable in onset_syllables
        if onset_syllables.count(syllable) > 1
    })
    if duplicates:
        errors.append(f"duplicates syllable(s): {', '.join(duplicates)}")
    return errors


def marked_atom_indices(tokens):
    """Return token indices used as name atoms after ``ne`` or an honorific.

    Honorific-only marking remains available in established conversational
    register.
    """
    indices = set()
    expecting_name = False
    for index, token in enumerate(tokens):
        if token == NAME_MARKER:
            expecting_name = True
            continue
        if token in HONORIFICS:
            expecting_name = True
            continue
        if expecting_name:
            indices.add(index)
            expecting_name = False
    return indices
