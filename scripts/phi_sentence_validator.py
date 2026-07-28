#!/usr/bin/env python3
"""Full-sentence surface-syntax parser for Phi.

This module is deliberately independent of ``validate_examples.py``. The
older validator owns lexical integrity, glosses, citations, and generated
artifacts. This parser owns complete utterance structure: sentence framing,
dependent and complement frames, modifier-first order, predicate shape, and
the three particle slots.

Phi permits verbs to serve as event nouns and adjectives to serve as quality
nouns without changing their lexicon entries. The parser therefore accepts a
sentence when at least one canonical surface parse exists. It does not infer
speaker intent or semantic valency.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import re
from typing import Iterable, Iterator, Sequence

import name_forms


PROJECT_ROOT = Path(__file__).resolve().parent.parent
VOCABULARY_ROOT = PROJECT_ROOT / "vocabulary"

TOKEN_RE = re.compile(r"[A-Za-z]+|\.")
VALID_TEXT_RE = re.compile(r"[a-z]+(?: [a-z]+)*\.(?: [a-z]+(?: [a-z]+)*\.)*")

CONTENT_POS = frozenset({"noun", "verb", "adjective", "numeral"})
NOMINAL_POS = frozenset(
    {"noun", "verb", "adjective", "pronoun", "interrogative"}
)

COMPLEMENT_PAIRS = {"tha": "tho", "pha": "pho", "sha": "sho"}
COMPLEMENT_CLOSERS = {closer: opener for opener, closer in COMPLEMENT_PAIRS.items()}
QUOTE_MATRIX_VERBS = frozenset({"haolu", "shemui", "thilou", "hea"})

SLOT0_SINGLE = frozenset({"wa", "no", "su"})
SLOT0_WORDS = frozenset({"pi", "wa", "no", "su", "lu", "he"})
DISCOURSE_MARKERS = frozenset(
    {"phisu", "shekoi", "shelao", "sheno", "shorela", "thelao", "whekai"}
)

COORDINATORS = frozenset({"nela", "thona", "sola"})
ADVERBIAL_RELATORS = frozenset({"lao", "pheo", "phoe", "shai", "lila", "whau"})
CLAUSE_ONLY_RELATORS = frozenset({"lila", "whau"})
TEMPORAL_NP_RELATORS = frozenset({"pheo", "phoe"})
NOMINAL_RELATORS = frozenset({"lao", "shai"})

SLOT2_OUTER = frozenset({"we", "li"})
SLOT2_DEIXIS = frozenset({"ha", "ra"})
SLOT2_QUANTITY = frozenset({"lo"})
SLOT2_FOCUS = frozenset({"ko"})
SLOT2_DEGREE = frozenset({"ru", "la", "pe", "wo", "mo"})
SLOT2_NAME = frozenset({"ne", "sa", "ni", "le"})
SLOT2_WORDS = (
    SLOT2_OUTER
    | SLOT2_DEIXIS
    | SLOT2_QUANTITY
    | SLOT2_FOCUS
    | SLOT2_DEGREE
    | SLOT2_NAME
    | {"nu"}
)
SLOT2_RANK = {
    **{word: 0 for word in SLOT2_OUTER},
    **{word: 1 for word in SLOT2_DEIXIS},
    "lo": 2,
    "nu": 2,
    "ko": 3,
    **{word: 4 for word in SLOT2_DEGREE},
}

NUMERAL_DIGITS = frozenset({"mu", "ta", "wi"})
NUMERAL_COEFFICIENTS = frozenset({"ta", "wi"})
NUMERAL_SCALES = {"rei": 4, "lau": 3, "phoi": 2, "shao": 1}

PREDICATIVE_VERBS = frozenset({"nai", "kelu"})


@dataclass(frozen=True)
class Token:
    text: str
    index: int
    char_start: int
    char_end: int


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    token_index: int = 0
    end_token_index: int | None = None

    def render(self, tokens: Sequence[Token]) -> str:
        if not tokens:
            return f"{self.code}: {self.message}"
        index = min(max(self.token_index, 0), len(tokens) - 1)
        token = tokens[index]
        return f"{self.code} at word {token.index + 1} ('{token.text}'): {self.message}"


@dataclass
class SyntaxNode:
    kind: str
    start: int
    end: int
    children: list["SyntaxNode"] = field(default_factory=list)
    value: str | None = None


@dataclass
class ParseResult:
    text: str
    tokens: list[Token]
    tree: SyntaxNode | None
    diagnostics: list[Diagnostic]

    @property
    def ok(self) -> bool:
        return not self.diagnostics


@dataclass(frozen=True)
class Lexeme:
    word: str
    pos: str
    gloss: str
    slot: int | None = None
    slot1_rank: str | None = None


class Lexicon:
    """The syntactic view of the canonical JSON lexicon."""

    def __init__(self, entries: Iterable[Lexeme]):
        self.entries = {entry.word: entry for entry in entries}
        self.words = frozenset(self.entries)
        self.content_words = frozenset(
            word for word, entry in self.entries.items() if entry.pos in CONTENT_POS
        )
        self.by_pos: dict[str, frozenset[str]] = {}
        for pos in {entry.pos for entry in self.entries.values()}:
            self.by_pos[pos] = frozenset(
                word for word, entry in self.entries.items() if entry.pos == pos
            )
        self.slot1_rank = {
            word: entry.slot1_rank
            for word, entry in self.entries.items()
            if entry.slot == 1 and entry.slot1_rank
        }
        self.slot1_words = frozenset(self.slot1_rank)
        self.prepositions = self.by_pos.get("preposition", frozenset())
        self.quantifiers = self.by_pos.get("quantifier", frozenset())
        self.classifiers = self.by_pos.get("classifier", frozenset())
        self.interjections = self.by_pos.get("interjection", frozenset())
        self.interrogatives = self.by_pos.get("interrogative", frozenset())
        self.pronouns = self.by_pos.get("pronoun", frozenset())

    @classmethod
    def load(cls, root: Path = VOCABULARY_ROOT) -> "Lexicon":
        entries = []
        for path in sorted(root.rglob("*.json")):
            if path.name == "schema.json":
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or "word" not in data:
                continue
            entries.append(
                Lexeme(
                    word=data["word"],
                    pos=data.get("pos", ""),
                    gloss=data.get("gloss", ""),
                    slot=data.get("slot"),
                    slot1_rank=data.get("slot1_rank"),
                )
            )
        return cls(entries)

    def pos(self, word: str) -> str | None:
        entry = self.entries.get(word)
        return entry.pos if entry else None

    def is_nominal(self, word: str) -> bool:
        pos = self.pos(word)
        return pos in NOMINAL_POS

    def name_errors(self, word: str) -> list[str]:
        if word in self.words:
            if word not in self.content_words:
                return ["a current function or interjection form cannot be a name atom"]
            return []
        return name_forms.form_errors(word)


class PhiParser:
    """Parse and validate complete Phi utterance sequences."""

    def __init__(self, lexicon: Lexicon | None = None):
        self.lexicon = lexicon or Lexicon.load()
        rank_names = ("tense", "aspect", "voice", "evidentiality", "modality", "negation")
        self.rank_order = {rank: index for index, rank in enumerate(rank_names)}
        self.tokens: list[Token] = []
        self.frame_close: dict[int, int] = {}
        self.frame_open: dict[int, int] = {}
        self.name_atoms: set[int] = set()
        self.diagnostics: list[Diagnostic] = []

    def parse(self, text: str, *, allow_fragments: bool = False) -> ParseResult:
        self.tokens = self._tokenize(text)
        self.frame_close = {}
        self.frame_open = {}
        self.name_atoms = set()
        self.diagnostics = []

        self._validate_surface(text)
        self._validate_words()
        self._pair_complement_frames()
        tree = None
        if not self.diagnostics:
            tree = self._parse_sequence(0, len(self.tokens), allow_fragments)
        return ParseResult(text, self.tokens, tree, self._deduplicate(self.diagnostics))

    def _tokenize(self, text: str) -> list[Token]:
        return [
            Token(match.group(0), index, match.start(), match.end())
            for index, match in enumerate(TOKEN_RE.finditer(text))
        ]

    def _validate_surface(self, text: str) -> None:
        if text != text.lower():
            self._error("PHS001", "Phi text uses lowercase letters only")
        if not VALID_TEXT_RE.fullmatch(text):
            self._error(
                "PHS002",
                "use lowercase Phi words, single spaces, and periods as the only punctuation",
            )

    def _validate_words(self) -> None:
        expecting_name = False
        for index, token in enumerate(self.tokens):
            word = token.text
            if word == ".":
                if expecting_name:
                    self._error("PHS004", "a name marker or honorific needs a name atom", index)
                expecting_name = False
                continue
            if expecting_name:
                if word in {"sa", "ni", "le"}:
                    continue
                self.name_atoms.add(index)
                errors = self.lexicon.name_errors(word)
                if errors:
                    self._error(
                        "PHS005",
                        f"invalid name atom '{word}': {'; '.join(errors)}",
                        index,
                    )
                expecting_name = False
                continue
            if word not in self.lexicon.words:
                self._error("PHS003", f"unknown Phi word '{word}'", index)
            if word == "ne" or word in {"sa", "ni", "le"}:
                expecting_name = True
        if expecting_name:
            self._error(
                "PHS004",
                "a name marker or honorific needs a name atom",
                len(self.tokens) - 1,
            )

    def _pair_complement_frames(self) -> None:
        stack: list[int] = []
        for index, token in enumerate(self.tokens):
            word = token.text
            if word in COMPLEMENT_PAIRS:
                stack.append(index)
            elif word in COMPLEMENT_CLOSERS:
                if not stack:
                    self._error("PHS020", f"unmatched complement closer '{word}'", index)
                    continue
                opener_index = stack[-1]
                opener = self.tokens[opener_index].text
                if COMPLEMENT_PAIRS[opener] != word:
                    self._error(
                        "PHS021",
                        f"'{word}' closes '{COMPLEMENT_CLOSERS[word]}', not open '{opener}'",
                        index,
                    )
                    continue
                stack.pop()
                self.frame_close[opener_index] = index
                self.frame_open[index] = opener_index
        for opener_index in stack:
            opener = self.tokens[opener_index].text
            self._error(
                "PHS022",
                f"complement frame '{opener}' needs closer '{COMPLEMENT_PAIRS[opener]}'",
                opener_index,
            )

    def _parse_sequence(
        self, start: int, end: int, allow_fragments: bool
    ) -> SyntaxNode | None:
        ranges = self._root_sentence_ranges(start, end)
        if not ranges:
            self._error("PHS010", "empty utterance sequence", start)
            return None

        children: list[SyntaxNode] = []
        range_index = 0
        while range_index < len(ranges):
            sentence_start, sentence_end = ranges[range_index]
            if self._is_conditional_start(sentence_start, sentence_end):
                if range_index + 1 >= len(ranges):
                    self._error(
                        "PHS031",
                        "a lu condition needs a complete following consequence sentence",
                        sentence_start,
                    )
                    range_index += 1
                    continue
                consequence_start, consequence_end = ranges[range_index + 1]
                condition = self._parse_conditional(
                    sentence_start,
                    sentence_end,
                    consequence_start,
                    consequence_end,
                )
                if condition:
                    children.append(condition)
                range_index += 2
                continue

            utterance = self._parse_utterance(
                sentence_start, sentence_end, allow_fragments=allow_fragments
            )
            if utterance:
                children.append(utterance)
            range_index += 1

        return SyntaxNode("utterance-sequence", start, end, children)

    def _root_sentence_ranges(self, start: int, end: int) -> list[tuple[int, int]]:
        ranges = []
        sentence_start = start
        index = start
        while index < end:
            if index in self.frame_close:
                index = self.frame_close[index] + 1
                continue
            if self.tokens[index].text == ".":
                if sentence_start < index:
                    ranges.append((sentence_start, index))
                else:
                    self._error("PHS011", "empty sentence before period", index)
                sentence_start = index + 1
            index += 1
        if sentence_start < end:
            ranges.append((sentence_start, end))
        return ranges

    def _is_conditional_start(self, start: int, end: int) -> bool:
        words = self._words(start, min(end, start + 3))
        return bool(words and words[0] == "lu")

    def _parse_conditional(
        self,
        start: int,
        end: int,
        consequence_start: int,
        consequence_end: int,
    ) -> SyntaxNode | None:
        index = start
        children = []
        if self._word(index) != "lu":
            self._error("PHS030", "conditional must begin with lu", index)
            return None
        index += 1
        irrealis = False
        if index < end and self._word(index) == "he":
            irrealis = True
            index += 1
        if index < end and self._word(index) in SLOT0_WORDS:
            self._error(
                "PHS032",
                "no additional Slot 0 frame may follow lu or lu he",
                index,
            )
        condition = self._parse_clause(index, end, allow_gap=False)
        consequence = self._parse_utterance(
            consequence_start, consequence_end, allow_fragments=False
        )
        if condition:
            children.append(condition)
        if consequence:
            children.append(consequence)
        return SyntaxNode(
            "irrealis-conditional" if irrealis else "realis-conditional",
            start,
            consequence_end,
            children,
        )

    def _parse_utterance(
        self, start: int, end: int, *, allow_fragments: bool
    ) -> SyntaxNode | None:
        if start >= end:
            self._error("PHS010", "empty utterance", start)
            return None

        if end - start == 1 and self._word(start) in self.lexicon.interjections:
            return SyntaxNode("interjection", start, end, value=self._word(start))

        if self._word(start) == "kona":
            if start + 1 >= end:
                self._error("PHS040", "kona needs an addressee", start)
                return None
            if not self._valid_nominal_span(start + 1, end):
                self._error(
                    "PHS041",
                    "the standalone kona phrase must contain a valid name or noun phrase",
                    start + 1,
                )
            return SyntaxNode("vocative", start, end)

        if allow_fragments and self._word(start) == "whu":
            checkpoint = len(self.diagnostics)
            relatives, _ = self._validate_relative_clauses(start, end, set())
            if len(self.diagnostics) == checkpoint and relatives:
                relative = relatives[0]
                clause_end = relative.children[0].end if relative.children else start
                remainder_is_head = (
                    clause_end < end and self._valid_nominal_span(clause_end, end)
                )
                if clause_end == end or remainder_is_head:
                    return SyntaxNode("relative-fragment", start, end, relatives)
            del self.diagnostics[checkpoint:]

        if allow_fragments and self._is_licensed_fragment(start, end):
            self._validate_slot2_and_quantity(start, end, set())
            return SyntaxNode("fragment", start, end)

        return self._parse_clause(start, end, allow_gap=False)

    def _parse_clause(
        self, start: int, end: int, *, allow_gap: bool
    ) -> SyntaxNode | None:
        if start >= end:
            self._error("PHS050", "clause is empty", start)
            return None

        index, frame_nodes = self._parse_sentence_frame(start, end)
        discourse_node = None
        if index < end and self._word(index) in DISCOURSE_MARKERS:
            discourse_node = SyntaxNode("discourse", index, index + 1, value=self._word(index))
            index += 1
        for late in range(index, end):
            if self._inside_frame(late, index, end):
                continue
            word = self._word(late)
            if word in SLOT0_WORDS:
                self._error(
                    "PHS052",
                    f"Slot 0 word '{word}' must open its sentence",
                    late,
                )
            if word in DISCOURSE_MARKERS:
                self._error(
                    "PHS053",
                    f"discourse marker '{word}' must follow Slot 0 and precede sentence content",
                    late,
                )

        coordinate = self._try_clause_coordination(index, end, allow_gap)
        if coordinate is not None:
            children = [*frame_nodes]
            if discourse_node:
                children.append(discourse_node)
            children.append(coordinate)
            return SyntaxNode("clause", start, end, children)

        adverbial = self._try_adverbial_clause(index, end, allow_gap)
        if adverbial is not None:
            children = [*frame_nodes]
            if discourse_node:
                children.append(discourse_node)
            children.append(adverbial)
            return SyntaxNode("clause", start, end, children)

        core = self._parse_core_clause(index, end, allow_gap=allow_gap)
        if core is None:
            return None
        children = [*frame_nodes]
        if discourse_node:
            children.append(discourse_node)
        children.append(core)
        return SyntaxNode("clause", start, end, children)

    def _parse_sentence_frame(
        self, start: int, end: int
    ) -> tuple[int, list[SyntaxNode]]:
        index = start
        nodes = []
        if self._word(index) == "pi":
            nodes.append(SyntaxNode("politeness", index, index + 1, value="pi"))
            index += 1
            if index < end and self._word(index) in {"wa", "no"}:
                nodes.append(
                    SyntaxNode("sentence-frame", index, index + 1, value=self._word(index))
                )
                index += 1
            elif index < end and self._word(index) in {"su", "lu", "he"}:
                self._error(
                    "PHS051",
                    "the licensed polite combinations are pi wa and pi no, "
                    f"not 'pi {self._word(index)}'",
                    index,
                )
                index += 1
        elif self._word(index) in SLOT0_SINGLE:
            nodes.append(
                SyntaxNode("sentence-frame", index, index + 1, value=self._word(index))
            )
            index += 1
        elif self._word(index) in {"lu", "he"}:
            self._error(
                "PHS030",
                "lu belongs to a two-sentence conditional and he occurs only directly after lu",
                index,
            )
            index += 1
        return index, nodes

    def _try_clause_coordination(
        self, start: int, end: int, allow_gap: bool
    ) -> SyntaxNode | None:
        candidates = [
            index
            for index in self._top_level_indices(start, end)
            if self._word(index) in COORDINATORS
        ]
        for index in candidates:
            if (
                index > start
                and index + 1 < end
                and self.lexicon.pos(self._word(index - 1)) == "verb"
                and self.lexicon.pos(self._word(end - 1)) == "verb"
            ):
                left = self._parse_clause(start, index, allow_gap=allow_gap)
                right = self._parse_clause(index + 1, end, allow_gap=allow_gap)
                return SyntaxNode(
                    "clause-coordination",
                    start,
                    end,
                    [node for node in (left, right) if node],
                    self._word(index),
                )
        for index in candidates:
            if index <= start or index + 1 >= end:
                continue
            checkpoint = len(self.diagnostics)
            left = self._parse_clause(start, index, allow_gap=allow_gap)
            left_errors = len(self.diagnostics) - checkpoint
            if left_errors:
                del self.diagnostics[checkpoint:]
                continue
            right = self._parse_clause(index + 1, end, allow_gap=allow_gap)
            right_errors = len(self.diagnostics) - checkpoint
            if right_errors:
                del self.diagnostics[checkpoint:]
                continue
            return SyntaxNode(
                "clause-coordination",
                start,
                end,
                [left, right] if left and right else [],
                self._word(index),
            )
        return None

    def _try_adverbial_clause(
        self, start: int, end: int, allow_gap: bool
    ) -> SyntaxNode | None:
        if start >= end or self._word(start) not in ADVERBIAL_RELATORS:
            return None
        relator = self._word(start)

        for split in self._candidate_clause_ends(start + 1, end):
            if split >= end:
                continue
            checkpoint = len(self.diagnostics)
            dependent = self._parse_clause(start + 1, split, allow_gap=False)
            if len(self.diagnostics) != checkpoint:
                del self.diagnostics[checkpoint:]
                continue
            main = self._parse_clause(split, end, allow_gap=allow_gap)
            if len(self.diagnostics) != checkpoint:
                del self.diagnostics[checkpoint:]
                continue
            return SyntaxNode(
                "adverbial-clause",
                start,
                end,
                [dependent, main] if dependent and main else [],
                relator,
            )

        if relator in TEMPORAL_NP_RELATORS | NOMINAL_RELATORS:
            for split in range(start + 2, end):
                if not self._valid_nominal_span(start + 1, split):
                    continue
                checkpoint = len(self.diagnostics)
                main = self._parse_clause(split, end, allow_gap=allow_gap)
                if len(self.diagnostics) == checkpoint:
                    return SyntaxNode(
                        "adverbial-nominal",
                        start,
                        end,
                        [main] if main else [],
                        relator,
                    )
                del self.diagnostics[checkpoint:]

        self._error(
            "PHS060",
            f"'{relator}' must open complete dependent material before a complete main clause",
            start,
        )
        return SyntaxNode("invalid-adverbial", start, end, value=relator)

    def _parse_core_clause(
        self, start: int, end: int, *, allow_gap: bool
    ) -> SyntaxNode | None:
        if start >= end:
            self._error("PHS050", "clause has no predicate", start)
            return None
        predicate_index = end - 1
        predicate = self._word(predicate_index)
        if (
            self.lexicon.pos(predicate) != "verb"
            or predicate_index in self.name_atoms
        ):
            role = (
                "name atom"
                if predicate_index in self.name_atoms
                else self.lexicon.pos(predicate) or "unknown"
            )
            self._error(
                "PHS070",
                f"a complete assertion ends in a lexical verb; '{predicate}' is {role}",
                predicate_index,
            )
            return SyntaxNode("invalid-core-clause", start, end)

        nested = self._nested_mask(start, end)
        frame_nodes = self._validate_complement_frames(start, end)
        relative_nodes, relative_mask = self._validate_relative_clauses(start, end, nested)
        nested |= relative_mask
        interrogative_nodes, interrogative_mask = self._validate_bare_interrogatives(
            start, end, nested
        )
        nested |= interrogative_mask

        top_level = [
            index
            for index in range(start, end)
            if index not in nested and self._word(index) != "."
        ]
        slot1_indices = [
            index for index in top_level if self._word(index) in self.lexicon.slot1_words
        ]
        self._validate_slot1(slot1_indices)
        self._validate_clause_relators(start, end, predicate_index, nested)
        self._validate_predicate_suffix(start, end, predicate_index, slot1_indices, nested)
        self._validate_slot2_and_quantity(start, end, nested)
        self._validate_prepositions(start, end, predicate_index, slot1_indices, nested, allow_gap)
        self._validate_predicative_order(start, predicate_index, slot1_indices, nested)

        children = [
            *frame_nodes,
            *relative_nodes,
            *interrogative_nodes,
            SyntaxNode("predicate", predicate_index, predicate_index + 1, value=predicate),
        ]
        return SyntaxNode("core-clause", start, end, children)

    def _validate_clause_relators(
        self, start: int, end: int, predicate_index: int, nested: set[int]
    ) -> None:
        for index in range(start, predicate_index):
            if index in nested:
                continue
            word = self._word(index)
            if word not in CLAUSE_ONLY_RELATORS:
                continue
            freedom = (
                word == "lila"
                and self._word(predicate_index) == "nai"
                and any(
                    self._word(other) == "ralu"
                    for other in range(index + 1, predicate_index)
                    if other not in nested
                )
                and any(
                    self.lexicon.pos(self._word(other)) == "verb"
                    for other in range(index + 1, predicate_index)
                    if other not in nested
                )
            )
            if not freedom:
                self._error(
                    "PHS061",
                    f"'{word}' opens dependent material before the main clause; "
                    "it cannot be postposed",
                    index,
                )

    def _validate_complement_frames(
        self, start: int, end: int
    ) -> list[SyntaxNode]:
        nodes = []
        for opener in sorted(self.frame_close):
            closer = self.frame_close[opener]
            if not (start <= opener < closer < end):
                continue
            if any(
                outer < opener < closer < self.frame_close[outer]
                for outer in self.frame_close
                if start <= outer < end
            ):
                continue
            kind = self._word(opener)
            checkpoint = len(self.diagnostics)
            inner = self._parse_sequence(
                opener + 1, closer, allow_fragments=(kind == "sha")
            )
            if kind == "pha":
                inner_words = {
                    self._word(index)
                    for index in range(opener + 1, closer)
                    if self._word(index) != "."
                }
                if "wa" in inner_words or inner_words & self.lexicon.interrogatives:
                    self._error(
                        "PHS082",
                        "pha ... pho embeds a yes/no proposition; content questions embed bare",
                        opener,
                    )
            if kind == "tha":
                inner_words = {
                    self._word(index)
                    for index in range(opener + 1, closer)
                    if self._word(index) != "."
                }
                if "wa" in inner_words:
                    self._error(
                        "PHS083",
                        "tha ... tho embeds a statement, not a direct question",
                        opener,
                    )
            if len(self.diagnostics) > checkpoint and inner is None:
                self._error(
                    "PHS080",
                    f"the material inside {kind} ... {self._word(closer)} is "
                    "not a complete Phi utterance",
                    opener,
                )
            nodes.append(
                SyntaxNode(
                    f"{kind}-complement",
                    opener,
                    closer + 1,
                    [inner] if inner else [],
                )
            )

        quote_nodes = [node for node in nodes if node.kind == "sha-complement"]
        if quote_nodes:
            matrix = self._word(end - 1)
            if matrix not in QUOTE_MATRIX_VERBS:
                self._error(
                    "PHS081",
                    "sha ... sho must modify haolu, shemui, thilou, or hea",
                    end - 1,
                )
        return nodes

    def _validate_bare_interrogatives(
        self, start: int, end: int, already_nested: set[int]
    ) -> tuple[list[SyntaxNode], set[int]]:
        """Recognize a bare content-question clause before a matrix verb.

        Yes/no complements have the audible ``pha ... pho`` boundary. A
        content interrogative supplies its own boundary cue and therefore
        embeds without that frame.
        """
        visible_verbs = [
            index
            for index in range(start, end)
            if index not in already_nested
            and self.lexicon.pos(self._word(index)) == "verb"
        ]
        if len(visible_verbs) < 2:
            return [], set()

        for interrogative in range(start, visible_verbs[-1]):
            if (
                interrogative in already_nested
                or self._word(interrogative) not in self.lexicon.interrogatives
            ):
                continue
            embedded_end = next(
                (
                    index + 1
                    for index in visible_verbs
                    if interrogative < index < visible_verbs[-1]
                ),
                None,
            )
            if embedded_end is None:
                continue
            for embedded_start in range(interrogative, start, -1):
                checkpoint = len(self.diagnostics)
                clause = self._parse_clause(
                    embedded_start, embedded_end, allow_gap=False
                )
                if len(self.diagnostics) == checkpoint:
                    return (
                        [
                            SyntaxNode(
                                "bare-interrogative-complement",
                                embedded_start,
                                embedded_end,
                                [clause] if clause else [],
                            )
                        ],
                        set(range(embedded_start, embedded_end)),
                    )
                del self.diagnostics[checkpoint:]
        return [], set()

    def _nested_mask(self, start: int, end: int) -> set[int]:
        nested: set[int] = set()
        for opener, closer in self.frame_close.items():
            if start <= opener < closer < end:
                nested.update(range(opener + 1, closer))
        return nested

    def _validate_relative_clauses(
        self, start: int, end: int, already_nested: set[int]
    ) -> tuple[list[SyntaxNode], set[int]]:
        nodes = []
        nested = set()
        for whu in range(start, end):
            if whu in already_nested or whu in nested or self._word(whu) != "whu":
                continue
            found = None
            for clause_end in reversed(self._candidate_clause_ends(whu + 1, end)):
                if clause_end >= end:
                    continue
                checkpoint = len(self.diagnostics)
                clause = self._parse_clause(whu + 1, clause_end, allow_gap=True)
                if len(self.diagnostics) != checkpoint:
                    del self.diagnostics[checkpoint:]
                    continue
                found = (clause_end, clause)
                break
            if found is None:
                self._error(
                    "PHS090",
                    "whu must precede a complete gapped relative clause",
                    whu,
                )
                continue
            clause_end, clause = found
            nested.update(range(whu + 1, clause_end))
            head_end = clause_end
            if clause_end < end and self.lexicon.is_nominal(self._word(clause_end)):
                head_end += 1
            nodes.append(
                SyntaxNode(
                    "relative-phrase",
                    whu,
                    head_end,
                    [clause] if clause else [],
                    "headed" if head_end > clause_end else "headless",
                )
            )
        return nodes, nested

    def _candidate_clause_ends(self, start: int, end: int) -> list[int]:
        return [
            index + 1
            for index in self._top_level_indices(start, end)
            if self.lexicon.pos(self._word(index)) == "verb"
        ]

    def _validate_slot1(self, indices: Sequence[int]) -> None:
        if not indices:
            return
        ranks = [self.lexicon.slot1_rank[self._word(index)] for index in indices]
        numbers = [self.rank_order[rank] for rank in ranks]
        for previous, current, index in zip(numbers, numbers[1:], indices[1:]):
            if current < previous:
                self._error(
                    "PHS100",
                    "Slot 1 order is tense > aspect > voice > evidentiality > modality > negation",
                    index,
                )
        by_rank: dict[str, list[tuple[str, int]]] = {}
        for index, rank in zip(indices, ranks):
            by_rank.setdefault(rank, []).append((self._word(index), index))
        for rank, members in by_rank.items():
            words = [word for word, _ in members]
            if rank == "voice" and words == ["se", "ka"]:
                continue
            if len(members) > 1:
                self._error(
                    "PHS101",
                    f"Slot 1 admits one {rank} particle per clause",
                    members[1][1],
                )

    def _validate_predicate_suffix(
        self,
        start: int,
        end: int,
        predicate_index: int,
        slot1_indices: Sequence[int],
        nested: set[int],
    ) -> None:
        if not slot1_indices:
            return
        first = slot1_indices[0]
        last = slot1_indices[-1]
        for index in range(first, predicate_index):
            if index in nested:
                continue
            word = self._word(index)
            pos = self.lexicon.pos(word)
            if word in self.lexicon.slot1_words or word in SLOT2_WORDS:
                continue
            if pos == "adjective" and index > last:
                continue
            if word in COORDINATORS and index > last:
                continue
            self._error(
                "PHS102",
                f"argument or complement '{word}' follows the Slot 1 stack; "
                "it must precede the stack",
                index,
            )

        predicate = self._word(predicate_index)
        after_last = [
            index
            for index in range(last + 1, predicate_index)
            if index not in nested and self._word(index) != "."
        ]
        adjective_after = [
            index for index in after_last if self.lexicon.pos(self._word(index)) == "adjective"
        ]
        if predicate == "nai" and adjective_after:
            self._error(
                "PHS103",
                "the predicative complement of nai precedes the Slot 1 stack",
                adjective_after[0],
            )
        elif predicate == "kelu" and adjective_after:
            before_stack = [
                index
                for index in range(start, first)
                if index not in nested
                and self.lexicon.pos(self._word(index)) in {"noun", "adjective"}
            ]
            if len(before_stack) < 2:
                self._error(
                    "PHS104",
                    "a result complement of kelu precedes Slot 1; "
                    "only manner may follow the stack",
                    adjective_after[0],
                )

    def _validate_predicative_order(
        self,
        start: int,
        predicate_index: int,
        slot1_indices: Sequence[int],
        nested: set[int],
    ) -> None:
        predicate = self._word(predicate_index)
        if predicate not in PREDICATIVE_VERBS:
            return
        boundary = slot1_indices[0] if slot1_indices else predicate_index
        material = [
            index
            for index in range(start, boundary)
            if index not in nested
            and (
                self._word(index) not in SLOT2_WORDS
                or self._word(index) in {"ha", "ra"}
            )
            and self._word(index) not in COORDINATORS
        ]
        if not material:
            self._error(
                "PHS105",
                f"'{predicate}' needs a predicative complement before its particle stack",
                predicate_index,
            )

    def _validate_slot2_and_quantity(
        self, start: int, end: int, nested: set[int]
    ) -> None:
        indices = [
            index
            for index in range(start, end)
            if index not in nested and self._word(index) != "."
        ]
        position = 0
        while position < len(indices):
            index = indices[position]
            word = self._word(index)
            if word == "ne" or word in {"sa", "ni", "le"}:
                position += 1
                continue
            if word not in SLOT2_WORDS:
                position += 1
                continue
            run = []
            while position < len(indices) and self._word(indices[position]) in SLOT2_WORDS:
                run.append(indices[position])
                position += 1
            target = indices[position] if position < len(indices) else None
            self._validate_slot2_run(run, target)

        self._validate_quantity_strategies(indices)

    def _validate_slot2_run(self, run: Sequence[int], target: int | None) -> None:
        if not run:
            return
        words = [self._word(index) for index in run]
        if words in (["lo", "ha"], ["lo", "ra"]):
            if target is None or self.lexicon.pos(self._word(target)) == "verb":
                return
            self._error(
                "PHS111",
                "lo ha and lo ra are bare plural pronouns; a following noun takes ha lo or ra lo",
                run[1],
            )
            return
        if words[:2] in (["lo", "ha"], ["lo", "ra"]):
            self._validate_slot2_run(run[2:], target)
            return
        if target is None:
            self._error(
                "PHS110",
                f"Slot 2 particle '{words[-1]}' needs material to modify",
                run[-1],
            )
            return

        target_word = self._word(target)
        target_pos = self.lexicon.pos(target_word)
        if any(word in {"ne", "sa", "ni", "le"} for word in words):
            return

        normalized = []
        offset = 0
        while offset < len(words):
            if words[offset : offset + 2] == ["mo", "ko"]:
                normalized.append((3, "mo ko", run[offset]))
                offset += 2
            else:
                normalized.append((SLOT2_RANK[words[offset]], words[offset], run[offset]))
                offset += 1
        for previous, current in zip(normalized, normalized[1:]):
            if current[0] < previous[0]:
                self._error(
                    "PHS111",
                    "Slot 2 nesting is we/li > ha/ra > quantity > ko > degree > target",
                    current[2],
                )

        groups = (
            (SLOT2_OUTER, "additive/restrictive"),
            (SLOT2_DEIXIS, "deictic"),
            (SLOT2_DEGREE, "degree"),
        )
        for group, label in groups:
            members = [index for index in run if self._word(index) in group]
            if label == "degree" and words.count("mo") == 1 and "ko" in words:
                members = [index for index in members if self._word(index) != "mo"]
            if len(members) > 1:
                self._error(
                    "PHS112",
                    f"only one {label} particle may modify the same target",
                    members[1],
                )

        degree_words = [word for word in words if word in SLOT2_DEGREE]
        if degree_words and target_pos == "particle":
            if words != ["mo", "ko"]:
                self._error(
                    "PHS113",
                    f"degree particle '{degree_words[0]}' must precede "
                    f"gradable content, not Slot 1 '{target_word}'",
                    run[words.index(degree_words[0])],
                )
        if "nu" in words:
            nu_index = words.index("nu")
            following = words[nu_index + 1 :]
            if not following and target_word not in NUMERAL_COEFFICIENTS:
                self._error(
                    "PHS114",
                    "nu must precede a positive exact numeral",
                    run[nu_index],
                )

    def _validate_quantity_strategies(self, indices: Sequence[int]) -> None:
        for position, index in enumerate(indices):
            word = self._word(index)
            if word not in {"lo", *self.lexicon.quantifiers, *NUMERAL_DIGITS, "wia"}:
                continue
            phrase = [word]
            offset = position + 1
            numeral_end = None
            if word in NUMERAL_DIGITS:
                numeral_words = [
                    self._word(other)
                    for other in indices[position : min(len(indices), position + 12)]
                ]
                numeral_end = self._parse_numeral(numeral_words, 0)
                phrase = numeral_words[: max(numeral_end, 1)]
                offset = position + max(numeral_end, 1)
            while offset < len(indices):
                candidate = self._word(indices[offset])
                if (
                    candidate in self.lexicon.prepositions
                    or candidate in self.lexicon.slot1_words
                    or candidate in COORDINATORS
                ):
                    break
                phrase.append(candidate)
                offset += 1
                if self.lexicon.is_nominal(candidate):
                    break
            strategies = 0
            strategies += int("lo" in phrase)
            strategies += int(any(item in self.lexicon.quantifiers for item in phrase))
            strategies += int(any(item in NUMERAL_DIGITS for item in phrase))
            strategies += int("wia" in phrase)
            if strategies > 1:
                self._error(
                    "PHS115",
                    "lo, a numeral, a quantifier, and wia are alternative quantity strategies",
                    index,
                )
            if any(item in self.lexicon.quantifiers for item in phrase) and any(
                item in self.lexicon.classifiers for item in phrase
            ):
                self._error(
                    "PHS116",
                    "ordinary quantifiers do not take classifiers",
                    index,
                )
            if word in NUMERAL_DIGITS:
                if numeral_end == 0:
                    self._error("PHS117", "malformed exact numeral", index)

    def _parse_numeral(self, words: Sequence[str], start: int) -> int:
        if start >= len(words):
            return 0
        if words[start] == "mu":
            return 1
        if words[start] not in NUMERAL_COEFFICIENTS:
            return 0
        position = start
        previous_scale = 5
        used_scale = False
        while position + 1 < len(words):
            coefficient = words[position]
            scale = words[position + 1]
            if coefficient not in NUMERAL_COEFFICIENTS or scale not in NUMERAL_SCALES:
                break
            rank = NUMERAL_SCALES[scale]
            if rank >= previous_scale:
                return 0
            previous_scale = rank
            used_scale = True
            position += 2
        if position < len(words) and words[position] in NUMERAL_COEFFICIENTS:
            position += 1
        return position - start if used_scale or position == start + 1 else 0

    def _validate_prepositions(
        self,
        start: int,
        end: int,
        predicate_index: int,
        slot1_indices: Sequence[int],
        nested: set[int],
        allow_gap: bool,
    ) -> None:
        boundary = slot1_indices[0] if slot1_indices else predicate_index
        dangling = []
        for index in range(start, boundary):
            if index in nested or self._word(index) not in self.lexicon.prepositions:
                continue
            next_index = self._next_visible(index + 1, boundary, nested)
            if next_index is None or self._word(next_index) in self.lexicon.slot1_words:
                dangling.append(index)
                continue
        if dangling:
            if allow_gap and len(dangling) == 1:
                return
            for index in dangling:
                self._error(
                    "PHS121",
                    f"preposition '{self._word(index)}' needs an object "
                    "before the predicate stack",
                    index,
                )

    def _is_licensed_fragment(self, start: int, end: int) -> bool:
        words = self._words(start, end)
        if not words:
            return False
        if len(words) == 1 and words[0] in self.lexicon.quantifiers:
            return True
        if any(word in self.lexicon.slot1_words for word in words):
            return False
        if any(word in COMPLEMENT_PAIRS or word in COMPLEMENT_CLOSERS for word in words):
            return False
        if any(self.lexicon.pos(word) == "verb" for word in words):
            return False
        return self._valid_nominal_span(start, end)

    def _valid_nominal_span(self, start: int, end: int) -> bool:
        if start >= end:
            return False
        words = self._words(start, end)
        if "." in words:
            return False
        if words[0] == "ne":
            atom_index = 2 if len(words) > 1 and words[1] in {"sa", "ni", "le"} else 1
            return atom_index < len(words) and not self.lexicon.name_errors(words[atom_index])
        if words[0] in {"sa", "ni", "le"}:
            return len(words) > 1 and not self.lexicon.name_errors(words[1])
        return any(self.lexicon.is_nominal(word) for word in words)

    def _top_level_indices(self, start: int, end: int) -> Iterator[int]:
        index = start
        while index < end:
            yield index
            if index in self.frame_close:
                index = self.frame_close[index] + 1
            else:
                index += 1

    def _inside_frame(self, index: int, start: int, end: int) -> bool:
        return any(
            start <= opener < index < closer < end
            for opener, closer in self.frame_close.items()
        )

    def _next_visible(
        self, start: int, end: int, hidden: set[int]
    ) -> int | None:
        for index in range(start, end):
            if index not in hidden:
                return index
        return None

    def _word(self, index: int) -> str:
        if 0 <= index < len(self.tokens):
            return self.tokens[index].text
        return ""

    def _words(self, start: int, end: int) -> list[str]:
        return [self.tokens[index].text for index in range(start, min(end, len(self.tokens)))]

    def _error(
        self,
        code: str,
        message: str,
        token_index: int = 0,
        end_token_index: int | None = None,
    ) -> None:
        self.diagnostics.append(
            Diagnostic(code, message, max(token_index, 0), end_token_index)
        )

    @staticmethod
    def _deduplicate(diagnostics: Sequence[Diagnostic]) -> list[Diagnostic]:
        seen = set()
        result = []
        for diagnostic in diagnostics:
            key = (
                diagnostic.code,
                diagnostic.message,
                diagnostic.token_index,
                diagnostic.end_token_index,
            )
            if key not in seen:
                seen.add(key)
                result.append(diagnostic)
        return result
