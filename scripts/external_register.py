#!/usr/bin/env python3
"""Shared parser for Phi's marked external register.

The parser is deliberately small.  It recognizes only the four boundary
words; exact payload is otherwise opaque, while guest payload is checked
against Phi's ordinary segment and syllable inventory with the lexical
duplicate-syllable rule relaxed.
"""

from dataclasses import dataclass
import re


GUEST_OPEN = "hasha"
GUEST_CLOSE = "hasho"
EXACT_OPEN = "patha"
EXACT_CLOSE = "patho"

OPENERS = {GUEST_OPEN: "guest", EXACT_OPEN: "exact"}
CLOSERS = {GUEST_CLOSE: "guest", EXACT_CLOSE: "exact"}
BOUNDARIES = set(OPENERS) | set(CLOSERS)

CONSONANTS = set("hklmnprstw")
DIGRAPHS = ("ph", "th", "sh", "wh")
VOWELS = set("aeiou")
PHI_LETTERS = CONSONANTS | VOWELS


@dataclass(frozen=True)
class ExternalSpan:
    """Character offsets for one external frame in its source line."""

    kind: str
    start: int
    end: int
    payload_start: int
    payload_end: int
    complete: bool = True


@dataclass(frozen=True)
class ExternalAnalysis:
    """Parsed frames plus views used by validators and renderers."""

    spans: tuple
    errors: tuple
    core_text: str
    punctuation_text: str

    @property
    def has_external(self):
        return bool(self.spans)


def _boundary(token):
    """Return a boundary word for a whitespace token, if it is one.

    A closer may carry the sentence's final period.  Openers must stand as
    plain words; treating ``patha.`` as an opener would hide a missing
    payload and closer.
    """
    if token in BOUNDARIES:
        return token
    if token.endswith(".") and token[:-1] in CLOSERS:
        return token[:-1]
    return None


def _mask(text, ranges):
    chars = list(text)
    for start, end in ranges:
        for i in range(start, end):
            if chars[i] not in "\r\n":
                chars[i] = " "
    return "".join(chars)


def _guest_syllables(word):
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


def guest_word_errors(word):
    """Validate an adapted guest token, allowing repeated syllables."""
    errors = []
    if not word:
        return ["empty guest token"]
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
    if _guest_syllables(word) is None:
        errors.append("cannot be parsed into Phi open syllables")
    return errors


def analyze(text):
    """Parse all external frames in *text* and return masked views.

    ``core_text`` hides both kinds of payload, leaving boundary and ordinary
    Phi words for lexicon and grammar checks.  ``punctuation_text`` hides
    exact payload only, so guest material remains subject to Phi's case and
    punctuation rules.
    """
    tokens = list(re.finditer(r"\S+", text))
    spans = []
    errors = []
    state = None
    opener = None
    payload_tokens = []
    i = 0

    while i < len(tokens):
        match = tokens[i]
        raw = match.group(0)
        boundary = _boundary(raw)

        if state is None:
            if boundary in OPENERS:
                state = OPENERS[boundary]
                opener = match
                payload_tokens = []
            elif boundary in CLOSERS:
                errors.append(f"unexpected external closer '{boundary}'")
            i += 1
            continue

        if state == "guest":
            if boundary in OPENERS:
                errors.append(
                    f"external frames cannot nest: '{boundary}' inside guest frame"
                )
                payload_tokens.append(match)
            elif boundary == GUEST_CLOSE:
                if not payload_tokens:
                    errors.append("guest frame has an empty payload")
                spans.append(ExternalSpan(
                    "guest", opener.start(), match.start() + len(GUEST_CLOSE),
                    opener.end(), match.start(), True,
                ))
                state = None
                opener = None
                payload_tokens = []
            elif boundary in CLOSERS:
                errors.append(
                    f"mismatched closer '{boundary}' inside guest frame"
                )
                payload_tokens.append(match)
            else:
                payload_tokens.append(match)
                for error in guest_word_errors(raw):
                    errors.append(f"guest token '{raw}' {error}")
            i += 1
            continue

        # Exact payload is opaque.  Only its own closer has syntax.  A
        # doubled plain ``patho patho`` is a literal payload occurrence.
        if boundary == EXACT_CLOSE:
            if (raw == EXACT_CLOSE and i + 1 < len(tokens)
                    and _boundary(tokens[i + 1].group(0)) == EXACT_CLOSE):
                payload_tokens.extend((match, tokens[i + 1]))
                i += 2
                continue
            if not payload_tokens:
                errors.append("exact frame has an empty payload")
            spans.append(ExternalSpan(
                "exact", opener.start(), match.start() + len(EXACT_CLOSE),
                opener.end(), match.start(), True,
            ))
            state = None
            opener = None
            payload_tokens = []
            i += 1
            continue
        payload_tokens.append(match)
        i += 1

    if state is not None:
        errors.append(f"unclosed {state} external frame")
        spans.append(ExternalSpan(
            state, opener.start(), len(text), opener.end(), len(text), False,
        ))

    payload_ranges = [(s.payload_start, s.payload_end) for s in spans]
    exact_ranges = [
        (s.payload_start, s.payload_end) for s in spans if s.kind == "exact"
    ]
    return ExternalAnalysis(
        tuple(spans), tuple(errors), _mask(text, payload_ranges),
        _mask(text, exact_ranges),
    )
