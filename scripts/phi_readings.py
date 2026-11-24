#!/usr/bin/env python3
"""Count the structural readings of a Phi sentence.

``phi_sentence_validator`` accepts a sentence when one canonical parse
exists. This module asks the next question: how many are there? Phi marks
the edges of embedded statements, questions, and quotations with words, and
leaves the commoner edges unmarked: where the subject ends and the object
begins, where a prepositional phrase ends, whether a quality word before the
verb is its manner or its object, and where an adverbial or relative clause
hands over to the clause around it.

A reading here is one way of dividing a clause's words into phrases. For
each core clause the counter takes the words before the Slot 1 stack (or
before the verb when the clause has no stack) and enumerates every division
into phrases that canon's clause order allows:

    [subject] [adjuncts] [object or complement] | Slot 1 | manner | verb

It adds the places where a dependent clause could end, using the parser
itself to decide which splits are grammatical. Readings multiply across the
clauses of one sentence.

What the count does not do:

* It has no verb valency and no meanings, so it cannot discard a reading
  that is grammatical and absurd. ``mia nosa thole`` counts two divisions,
  "I practice now" and "my now practices". The figure is an upper bound on
  structural choice, never an estimate of how often a reader is confused.
* It does not count bracketing inside a phrase. ``phao lopia shelu`` as one
  phrase is one reading, whichever noun owns which.
* It follows the parser's own choice for clause coordination.

Two strictness levels are reported. The conservative count lets a noun,
pronoun, or name end a phrase anywhere, and lets an adjective or verb stand
as a phrase by itself only where nothing else can end the phrase. The full
count also lets an adjective (quality noun) or a verb (event noun) head a
phrase with its own modifiers, as in ``thia shua`` (your coming).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Sequence

from phi_sentence_validator import (
    ADVERBIAL_RELATORS,
    CLAUSAL_PREPOSITIONS,
    COORDINATORS,
    DISCOURSE_MARKERS,
    Lexicon,
    NOMINAL_RELATORS,
    NUMERAL_DIGITS,
    NUMERAL_SCALES,
    PREDICATIVE_VERBS,
    PhiParser,
    SLOT2_DEGREE,
    SLOT2_OBJECT,
    SLOT2_OUTER,
    SLOT2_WORDS,
    SyntaxNode,
    TEMPORAL_NP_RELATORS,
)

ADJUNCT_INTERROGATIVES = frozenset({"misa", "weno", "kua", "thela"})
# Nouns that stand as bare time adjuncts between subject and object. The
# parser's own temporal set is every noun with a temporal domain, which
# includes child, elder, seed, and festival; a bare adjunct needs a narrower
# test, so these are chosen by gloss.
TIME_ADJUNCT_GLOSSES = frozenset(
    {
        "now", "moment", "time", "instant", "period", "past", "present", "future",
        "day", "week", "month", "season", "year", "generation",
        "dawn", "morning", "midday", "afternoon", "evening", "dusk", "night", "midnight",
        "spring", "summer", "autumn", "winter",
    }
)
NAME_MARKERS = frozenset({"ne", "sa", "ni", "le"})

# A clause this long is not enumerated. Nothing in the corpus comes close.
MAX_UNITS = 22
MAX_SHOWN = 12


@dataclass(frozen=True)
class Unit:
    """One top-level item before the verb: a word, a frame, or a relative clause."""

    cls: str
    start: int
    end: int
    word: str
    temporal: bool = False
    inner: tuple[int, int] = (1, 1)


@dataclass
class ClauseReadings:
    """The divisions of one core clause."""

    start: int
    end: int
    text: str
    conservative: int
    full: int
    relaxed: bool
    divisions: list[str] = field(default_factory=list)
    seams: list[str] = field(default_factory=list)
    # Facts the role and reference counts need.
    verb: str = ""
    slot0: tuple[str, ...] = ()
    slot1: tuple[str, ...] = ()
    gapped: bool = False
    # How many bare phrases (subject, object, complement) each division has.
    bare_counts: tuple[int, ...] = ()
    # The head of the first phrase when it is bare: (class, word).
    first_bare: tuple[str, str] | None = None
    # The head of every bare phrase in the first division.
    bare_heads: tuple[tuple[str, str], ...] = ()
    # Third-person pronouns standing as separate words in the clause.
    third_persons: int = 0
    # Whether the object particle opens the object, which settles its role.
    object_marked: bool = False


@dataclass
class JoinReadings:
    """The places where one dependent clause could end."""

    kind: str
    opener: str
    start: int
    alternatives: int


@dataclass
class SentenceReadings:
    """Counts for one sentence, or for a condition with its consequence."""

    text: str
    conservative: int
    full: int
    clauses: list[ClauseReadings]
    joins: list[JoinReadings]
    unmodelled: bool = False

    @property
    def ambiguous(self) -> bool:
        return self.conservative > 1


class ReadingCounter(PhiParser):
    """A parser that also counts the readings of what it accepts.

    Internally every count is a pair, conservative and full. A full count of
    zero means the span has no division under this model, which is how an
    alternative the looser parser would accept gets discarded.
    """

    def __init__(
        self, lexicon: Lexicon | None = None, *, openers: frozenset[str] = frozenset()
    ):
        """``openers`` is a what-if: Slot 2 words assumed always to begin a phrase.

        Canon lets a possessor stand before a phrase that opens with ``ha`` or
        ``lo`` (``lo mia lo manuwe``, our hands). Passing those words here
        counts the readings that would remain if such a word always began a
        new phrase.
        """
        super().__init__(lexicon)
        self.openers = openers
        self.time_heads = frozenset(
            word
            for word, entry in self.lexicon.entries.items()
            if entry.pos == "noun" and entry.gloss.split(" (")[0] in TIME_ADJUNCT_GLOSSES
        )
        self._clauses: list[ClauseReadings] = []
        self._joins: list[JoinReadings] = []
        self._quoted: dict[tuple[int, int], SentenceReadings] = {}
        self._unmodelled = False

    # ------------------------------------------------------------------
    # Entry points
    # ------------------------------------------------------------------

    def analyse(self, text: str, *, allow_fragments: bool = False) -> SentenceReadings | None:
        """Counts for a whole passage, or None if it does not parse."""
        parts = self.analyse_sentences(text, allow_fragments=allow_fragments)
        if parts is None:
            return None
        conservative, full = 1, 1
        clauses: list[ClauseReadings] = []
        joins: list[JoinReadings] = []
        for part in parts:
            conservative *= part.conservative
            full *= part.full
            clauses.extend(part.clauses)
            joins.extend(part.joins)
        return SentenceReadings(
            text, conservative, full, clauses, joins, any(part.unmodelled for part in parts)
        )

    def analyse_sentences(
        self, text: str, *, allow_fragments: bool = False
    ) -> list[SentenceReadings] | None:
        """Counts for each sentence of a passage, or None if it does not parse.

        A ``lu`` condition and its consequence count as one sentence. Each
        sentence inside a quotation counts as a sentence of its own.
        """
        result = self.parse(text, allow_fragments=allow_fragments)
        if not result.ok or result.tree is None:
            return None
        parts = []
        for node in result.tree.children:
            self._clauses = []
            self._joins = []
            self._quoted = {}
            self._unmodelled = False
            cons, wide = self._floor(self._count_node(node))
            words = self._sentence_text(node.start, node.end)
            parts.append(
                SentenceReadings(words, cons, wide, self._clauses, self._joins, self._unmodelled)
            )
            parts.extend(self._quoted[key] for key in sorted(self._quoted))
        del self.diagnostics[:]
        return parts

    def _floor(self, counts: tuple[int, int]) -> tuple[int, int]:
        """A sentence the parser accepted has at least one reading."""
        if counts[1] == 0:
            self._unmodelled = True
            return 1, 1
        return counts

    def _sentence_text(self, start: int, end: int) -> str:
        """The words of a sentence, with the content of each quotation elided."""
        words = []
        index = start
        while index < end:
            word = self._word(index)
            words.append(word)
            closer = self.frame_close.get(index)
            if word == "sha" and closer is not None and closer < end:
                words.append("...")
                index = closer
                continue
            index += 1
        return " ".join(words).replace(" .", ".") + "."

    def _count_node(self, node: SyntaxNode) -> tuple[int, int]:
        if node.kind in {"realis-conditional", "irrealis-conditional"}:
            cons, wide = 1, 1
            for child in node.children:
                c, w = self._count_node(child)
                cons *= c
                wide *= w
            return cons, wide
        if node.kind == "clause":
            return self._count_clause(node.start, node.end, allow_gap=False)
        return 1, 1

    # ------------------------------------------------------------------
    # Records that can be withdrawn when an alternative proves illegal
    # ------------------------------------------------------------------

    def _mark(self) -> tuple[int, int]:
        return len(self._clauses), len(self._joins)

    def _rollback(self, mark: tuple[int, int]) -> None:
        del self._clauses[mark[0] :]
        del self._joins[mark[1] :]

    def _record_join(self, kind: str, opener: str, start: int, alternatives: int) -> None:
        if not any(join.kind == kind and join.start == start for join in self._joins):
            self._joins.append(JoinReadings(kind, opener, start, alternatives))

    # ------------------------------------------------------------------
    # Clauses and their joins
    # ------------------------------------------------------------------

    def _parses(self, start: int, end: int, *, allow_gap: bool) -> bool:
        checkpoint = len(self.diagnostics)
        self._parse_clause(start, end, allow_gap=allow_gap)
        ok = len(self.diagnostics) == checkpoint
        del self.diagnostics[checkpoint:]
        return ok

    def _core_parses(self, start: int, end: int, allow_gap: bool) -> bool:
        checkpoint = len(self.diagnostics)
        self._parse_core_clause(start, end, allow_gap=allow_gap)
        ok = len(self.diagnostics) == checkpoint
        del self.diagnostics[checkpoint:]
        return ok

    def _count_clause(self, start: int, end: int, *, allow_gap: bool) -> tuple[int, int]:
        checkpoint = len(self.diagnostics)
        index, frame_nodes = self._parse_sentence_frame(start, end)
        del self.diagnostics[checkpoint:]
        slot0 = tuple(node.value for node in frame_nodes if node.value)
        if index < end and self._word(index) in DISCOURSE_MARKERS:
            index += 1
        if index >= end:
            return 1, 1
        if index + 1 == end and self._word(index) in self.lexicon.interjections:
            return 1, 1

        checkpoint = len(self.diagnostics)
        coordinate = self._try_clause_coordination(index, end, allow_gap)
        del self.diagnostics[checkpoint:]
        if coordinate is not None and len(coordinate.children) == 2:
            left, right = coordinate.children
            lc, lw = self._count_clause(left.start, left.end, allow_gap=allow_gap)
            rc, rw = self._count_clause(right.start, right.end, allow_gap=allow_gap)
            return lc * rc, lw * rw

        opener = self._word(index)
        if opener in ADVERBIAL_RELATORS or opener in CLAUSAL_PREPOSITIONS:
            counted = self._count_adverbial(index, end, allow_gap)
            if counted is not None:
                return counted
        return self._count_core(index, end, allow_gap=allow_gap, slot0=slot0)

    def _count_adverbial(
        self, start: int, end: int, allow_gap: bool
    ) -> tuple[int, int] | None:
        """Sum over every place the dependent material could end."""
        relator = self._word(start)
        cons_total, wide_total = 0, 0
        alternatives = 0
        parser_alternatives = 0
        for split in self._candidate_clause_ends(start + 1, end):
            if split >= end:
                continue
            if not self._parses(start + 1, split, allow_gap=False):
                continue
            if not self._parses(split, end, allow_gap=allow_gap):
                continue
            parser_alternatives += 1
            mark = self._mark()
            dc, dw = self._count_clause(start + 1, split, allow_gap=False)
            mc, mw = self._count_clause(split, end, allow_gap=allow_gap)
            if dw == 0 or mw == 0:
                self._rollback(mark)
                continue
            cons_total += dc * mc
            wide_total += dw * mw
            alternatives += 1
        if relator in TEMPORAL_NP_RELATORS | NOMINAL_RELATORS:
            needs_time = relator in TEMPORAL_NP_RELATORS
            for split in range(start + 2, end):
                if not self._valid_nominal_span(start + 1, split):
                    continue
                if needs_time and not self._is_time_phrase(self._words(start + 1, split)):
                    continue
                if not self._parses(split, end, allow_gap=allow_gap):
                    continue
                parser_alternatives += 1
                if not self._is_noun_phrase(start + 1, split):
                    continue
                mark = self._mark()
                mc, mw = self._count_clause(split, end, allow_gap=allow_gap)
                if mw == 0:
                    self._rollback(mark)
                    continue
                cons_total += mc
                wide_total += mw
                alternatives += 1
        if parser_alternatives == 0:
            return None
        if relator in CLAUSAL_PREPOSITIONS and self._core_parses(start, end, allow_gap):
            # tei is still a preposition, so the whole span may also be one
            # clause that opens with a prepositional phrase.
            core_c, core_w = self._count_core(start, end, allow_gap=allow_gap, record=False)
            if core_w:
                cons_total += core_c
                wide_total += core_w
                alternatives += 1
        if alternatives:
            self._record_join("adverbial", relator, start, alternatives)
        return cons_total, wide_total

    def _is_noun_phrase(self, start: int, end: int) -> bool:
        """Whether the span is one noun phrase under the full count."""
        for units, _, inner_w in self._unit_sequences(start, end):
            if inner_w and units and self._noun_phrase(units, 0, len(units), None, True):
                return True
        return False

    # ------------------------------------------------------------------
    # The core clause
    # ------------------------------------------------------------------

    def _count_core(
        self,
        start: int,
        end: int,
        *,
        allow_gap: bool,
        record: bool = True,
        slot0: tuple[str, ...] = (),
    ) -> tuple[int, int]:
        predicate_index = end - 1
        if predicate_index < start:
            return 1, 1
        cons_total, wide_total = 0, 0
        relaxed_used = False
        shown: list[str] = []
        seams: set[str] = set()
        bare_counts: set[int] = set()
        first_bare: tuple[str, str] | None = None
        bare_heads: tuple[tuple[str, str], ...] | None = None
        slot1: tuple[str, ...] = ()
        third_persons = 0
        object_marked = False
        mark = self._mark()
        for units, inner_c, inner_w in self._unit_sequences(start, predicate_index):
            if inner_w == 0:
                continue
            pre, manner_ok = self._preverbal(units, predicate_index)
            if len(pre) > MAX_UNITS:
                cons_total += inner_c
                wide_total += inner_w
                continue
            has_ka = any(u.cls == "S1" and u.word == "ka" for u in units)
            predicative = self._word(predicate_index) in PREDICATIVE_VERBS
            counts = {}
            for full in (False, True):
                found = self._divisions(
                    pre, manner_ok, has_ka, predicative, allow_gap, full, relaxed=False
                )
                if not found:
                    found = self._divisions(
                        pre, manner_ok, has_ka, predicative, allow_gap, full, relaxed=True
                    )
                    if found and full:
                        relaxed_used = True
                counts[full] = found
            cons, wide = counts[False], counts[True]
            if not wide and not cons:
                continue
            # A clause that divides only when an event or quality noun heads
            # a phrase still has that one reading on the conservative count.
            cons_total += max(len(cons), 1) * inner_c
            wide_total += max(len(wide), len(cons)) * inner_w
            if len(cons) > 1:
                seams.update(self._seam_types(pre, cons))
            for division in cons:
                if len(shown) < MAX_SHOWN:
                    shown.append(self._render(pre, division))
            slot1 = tuple(u.word for u in units if u.cls == "S1")
            object_marked = object_marked or any(
                u.cls == "S2" and u.word in SLOT2_OBJECT for u in pre
            )
            third_persons = max(
                third_persons,
                sum(1 for u in pre if u.cls == "PRON" and u.word == "shia"),
            )
            for boundaries, _, types in cons or wide:
                bare_counts.add(sum(1 for kind in types if kind == "BARE"))
                if first_bare is None and types and types[0] == "BARE":
                    head = pre[boundaries[0] - 1]
                    first_bare = (head.cls, head.word)
                if bare_heads is None:
                    bare_heads = tuple(
                        (pre[stop - 1].cls, pre[stop - 1].word)
                        for stop, kind in zip(boundaries, types)
                        if kind == "BARE"
                    )
        if wide_total == 0:
            self._rollback(mark)
            return 0, 0
        if record and not any(
            clause.start == start and clause.end == end for clause in self._clauses
        ):
            self._clauses.append(
                ClauseReadings(
                    start,
                    end,
                    " ".join(self._words(start, end)),
                    cons_total,
                    wide_total,
                    relaxed_used,
                    shown if cons_total > 1 else [],
                    sorted(seams),
                    verb=self._word(predicate_index),
                    slot0=slot0,
                    slot1=slot1,
                    gapped=allow_gap,
                    bare_counts=tuple(sorted(bare_counts)),
                    first_bare=first_bare,
                    bare_heads=bare_heads or (),
                    third_persons=third_persons,
                    object_marked=object_marked,
                )
            )
        return cons_total, wide_total

    def _unit_sequences(
        self, start: int, stop: int
    ) -> Iterator[tuple[list[Unit], int, int]]:
        """Every way to cut the words in [start, stop) into top-level units.

        Complement frames are single units. A relative clause may end at more
        than one verb, so each ``whu`` yields one sequence per legal end.
        """

        def walk(index: int) -> Iterator[tuple[list[Unit], int, int]]:
            if index >= stop:
                yield [], 1, 1
                return
            word = self._word(index)
            closer = self.frame_close.get(index)
            if closer is not None and closer < stop + 1:
                if word == "sha":
                    inner = self._count_quotation(index + 1, closer)
                else:
                    inner = self._floor(self._count_sequence(index + 1, closer))
                unit = Unit("FRAME", index, closer + 1, word)
                for rest, c, w in walk(closer + 1):
                    yield [unit, *rest], c * inner[0], w * inner[1]
                return
            if word == "whu":
                ends = []
                parser_ends = []
                for clause_end in self._candidate_clause_ends(index + 1, stop + 1):
                    if clause_end > stop:
                        continue
                    if not self._parses(index + 1, clause_end, allow_gap=True):
                        continue
                    parser_ends.append(clause_end)
                    mark = self._mark()
                    inner = self._count_clause(index + 1, clause_end, allow_gap=True)
                    if inner[1] == 0:
                        self._rollback(mark)
                        continue
                    ends.append((clause_end, inner))
                if not ends and parser_ends:
                    self._unmodelled = True
                    ends = [(parser_ends[-1], (1, 1))]
                if ends:
                    self._record_join("relative", "whu", index, len(ends))
                    for clause_end, inner in ends:
                        unit = Unit("REL", index, clause_end, "whu")
                        for rest, c, w in walk(clause_end):
                            yield [unit, *rest], c * inner[0], w * inner[1]
                    return
            unit = self._classify(index)
            for rest, c, w in walk(index + 1):
                yield [unit, *rest], c, w

        yield from walk(start)

    def _count_quotation(self, start: int, end: int) -> tuple[int, int]:
        """Count each quoted sentence as a sentence of its own.

        A speech of ten sentences inside one ``sha ... sho`` frame is ten
        sentences for a listener, so its readings are reported one by one and
        do not multiply into the sentence that frames it.
        """
        checkpoint = len(self.diagnostics)
        ranges = self._root_sentence_ranges(start, end)
        del self.diagnostics[checkpoint:]
        position = 0
        while position < len(ranges):
            first_start, last_end = ranges[position]
            step = 1
            if self._word(first_start) == "lu" and position + 1 < len(ranges):
                last_end = ranges[position + 1][1]
                step = 2
            key = (first_start, last_end)
            if key not in self._quoted:
                saved = (self._clauses, self._joins, self._unmodelled)
                self._clauses, self._joins, self._unmodelled = [], [], False
                cons, wide = self._floor(self._count_sequence(first_start, last_end))
                self._quoted[key] = SentenceReadings(
                    self._sentence_text(first_start, last_end),
                    cons,
                    wide,
                    self._clauses,
                    self._joins,
                    self._unmodelled,
                )
                self._clauses, self._joins, self._unmodelled = saved
            position += step
        return 1, 1

    def _count_sequence(self, start: int, end: int) -> tuple[int, int]:
        """Readings of the sentences inside a complement frame."""
        cons, wide = 1, 1
        checkpoint = len(self.diagnostics)
        ranges = self._root_sentence_ranges(start, end)
        del self.diagnostics[checkpoint:]
        for sentence_start, sentence_end in ranges:
            index = sentence_start
            if self._word(index) == "lu":
                index += 1
                if index < sentence_end and self._word(index) == "he":
                    index += 1
            if self._parses(index, sentence_end, allow_gap=False):
                c, w = self._count_clause(index, sentence_end, allow_gap=False)
                cons, wide = cons * c, wide * w
        return cons, wide

    def _classify(self, index: int) -> Unit:
        word = self._word(index)
        lexicon = self.lexicon
        pos = lexicon.pos(word)

        def unit(cls: str, temporal: bool = False) -> Unit:
            return Unit(cls, index, index + 1, word, temporal)

        if index in self.name_atoms:
            return unit("NAME")
        if word in lexicon.slot1_words:
            return unit("S1")
        if word in NAME_MARKERS or word in SLOT2_WORDS:
            return unit("S2")
        if word in TEMPORAL_NP_RELATORS:
            return unit("RELT")
        if word in lexicon.prepositions or word == "lila":
            return unit("PREP")
        if word in COORDINATORS:
            return unit("COORD")
        if word in lexicon.pronouns:
            return unit("PRON")
        if word in ADJUNCT_INTERROGATIVES:
            return unit("ADVQ")
        if word == "sua":
            return unit("PRON")
        if (
            word in lexicon.quantifiers
            or word in lexicon.classifiers
            or word in NUMERAL_DIGITS
            or word in NUMERAL_SCALES
            or word == "wia"
            or pos == "numeral"
        ):
            return unit("DET")
        if pos == "noun" or word == "hina":
            return unit("N", word in self.time_heads)
        if pos == "adjective":
            return unit("ADJ")
        if pos == "verb":
            return unit("V")
        return unit("OTHER")

    def _preverbal(
        self, units: Sequence[Unit], predicate_index: int
    ) -> tuple[list[Unit], bool]:
        """The units to divide, and whether a manner tail is possible.

        With a Slot 1 stack, only what stands before the stack is divided:
        whatever follows it is manner by position. With no stack, an
        adjective directly before the verb may be manner or object.
        """
        stack = [position for position, u in enumerate(units) if u.cls == "S1"]
        if stack:
            pre = list(units[: stack[0]])
            manner_ok = False
        else:
            pre = list(units)
            manner_ok = self._word(predicate_index) not in PREDICATIVE_VERBS
        # we and li on the verb stand at the outer edge of the verb phrase, and
        # a degree particle or ko directly before the verb belongs to the verb.
        while pre and pre[-1].cls == "S2" and pre[-1].word in SLOT2_OUTER | SLOT2_DEGREE | {"ko"}:
            pre.pop()
        return pre, manner_ok

    # ------------------------------------------------------------------
    # Dividing the words before the verb
    # ------------------------------------------------------------------

    def _divisions(
        self,
        pre: Sequence[Unit],
        manner_ok: bool,
        has_ka: bool,
        predicative: bool,
        allow_gap: bool,
        full: bool,
        relaxed: bool,
    ) -> list[tuple]:
        """Every legal division, as (boundaries, manner_start, phrase_types)."""
        results: list[tuple] = []
        # A manner tail is a run of adjectives, each with any degree
        # particles, standing directly before the verb. A degree particle
        # left behind at the end of the body fails the phrase check below.
        tails = [len(pre)]
        if manner_ok and pre and pre[-1].cls == "ADJ":
            position = len(pre)
            while position > 0 and (
                pre[position - 1].cls == "ADJ"
                or (pre[position - 1].cls == "S2" and pre[position - 1].word in SLOT2_DEGREE)
            ):
                position -= 1
                tails.append(position)
        # The object particle settles where the object begins: the phrase it
        # opens is the last one, it is the object, and it runs to the verb
        # group, so no manner tail is split off after it.
        marks = [
            position
            for position, unit in enumerate(pre)
            if unit.cls == "S2" and unit.word in SLOT2_OBJECT
        ]
        for tail in sorted(set(tails)):
            if marks and tail != len(pre):
                continue
            body = pre[:tail]
            for boundaries, types in self._segmentations(body, allow_gap, full):
                if marks:
                    start_of_last = boundaries[-2] if len(boundaries) > 1 else 0
                    if start_of_last != marks[0] or types[-1] != "BARE":
                        continue
                if self._template_ok(body, types, has_ka, predicative, relaxed):
                    results.append((boundaries, tail, types))
        return results

    def _segmentations(
        self, body: Sequence[Unit], allow_gap: bool, full: bool
    ) -> Iterator[tuple[tuple[int, ...], tuple[str, ...]]]:
        count = len(body)
        if count == 0:
            yield (), ()
            return

        def walk(position: int) -> Iterator[tuple[tuple[int, ...], tuple[str, ...]]]:
            if position == count:
                yield (), ()
                return
            for stop in range(position + 1, count + 1):
                kind = self._phrase_type(body, position, stop, allow_gap, full)
                if kind is None:
                    continue
                for boundaries, types in walk(stop):
                    yield (stop, *boundaries), (kind, *types)

        yield from walk(0)

    def _phrase_type(
        self, body: Sequence[Unit], start: int, stop: int, allow_gap: bool, full: bool
    ) -> str | None:
        following = body[stop] if stop < len(body) else None
        # we, li, and ko may stand at the outer edge of a prepositional phrase.
        while (
            start + 1 < stop
            and body[start].cls == "S2"
            and body[start].word in SLOT2_OUTER | {"ko"}
            and body[start + 1].cls in {"PREP", "RELT", "S2"}
            and any(unit.cls in {"PREP", "RELT"} for unit in body[start + 1 : stop])
            and all(unit.cls == "S2" for unit in body[start : self._first_opener(body, start, stop)])
        ):
            start += 1
        first = body[start]
        if first.cls == "ADVQ":
            return "ADJUNCT" if stop == start + 1 else None
        if first.cls == "OTHER":
            return "ADJUNCT" if stop == start + 1 else None
        if first.cls in {"PREP", "RELT"}:
            # Two prepositional phrases joined by a coordinator are one adjunct.
            for position in range(start + 1, stop - 1):
                if body[position].cls == "COORD" and body[position + 1].cls in {"PREP", "RELT"}:
                    left = self._phrase_type(body[:position], start, position, allow_gap, full)
                    right = self._phrase_type(body, position + 1, stop, allow_gap, full)
                    return "ADJUNCT" if left == right == "ADJUNCT" else None
            rest_start = start + 1
            if rest_start == stop:
                return "ADJUNCT" if allow_gap else None
            if stop == rest_start + 1 and body[rest_start].cls == "ADVQ":
                return "ADJUNCT"
            if body[rest_start].cls in {"PREP", "RELT"}:
                inner = self._phrase_type(body, rest_start, stop, allow_gap, full)
                return "ADJUNCT" if inner == "ADJUNCT" else None
            head = self._noun_phrase(body, rest_start, stop, following, full)
            if head is None:
                return None
            if first.cls == "RELT" and head != "TIME":
                return None
            return "ADJUNCT"
        head = self._noun_phrase(body, start, stop, following, full)
        if head is None:
            return None
        return "TIME" if head == "TIME" else "BARE"

    def _first_opener(self, body: Sequence[Unit], start: int, stop: int) -> int:
        for position in range(start, stop):
            if body[position].cls in {"PREP", "RELT"}:
                return position
        return stop

    def _noun_phrase(
        self,
        body: Sequence[Unit],
        start: int,
        stop: int,
        following: Unit | None,
        full: bool,
    ) -> str | None:
        """Whether body[start:stop] is one noun phrase; returns its head kind."""
        conjuncts: list[list[Unit]] = [[]]
        for unit in body[start:stop]:
            if unit.cls == "COORD":
                conjuncts.append([])
            else:
                conjuncts[-1].append(unit)
        if any(not conjunct for conjunct in conjuncts):
            return None
        # Nothing can continue a noun phrase across these, so a quality word,
        # an event noun, or a quantity word standing before one must be a head.
        forced = following is None or following.cls in {
            "PREP", "RELT", "ADVQ", "PRON", "FRAME", "OTHER", "S1"
        }
        head_kind = "NOUN"
        for position, conjunct in enumerate(conjuncts):
            last = conjunct[-1]
            is_last_conjunct = position == len(conjuncts) - 1
            content = [u for u in conjunct if u.cls not in {"S2", "DET"}]
            for offset, unit in enumerate(conjunct):
                if unit.cls in {"PREP", "RELT", "ADVQ", "OTHER", "S1"}:
                    return None
                if unit.cls == "FRAME" and any(
                    earlier.cls != "S2" for earlier in conjunct[:offset]
                ):
                    return None
                if unit.cls == "PRON" and any(
                    earlier.cls != "S2" for earlier in conjunct[:offset]
                ):
                    return None
                if (
                    unit.cls == "S2"
                    and unit.word in self.openers
                    and any(earlier.cls != "S2" for earlier in conjunct[:offset])
                ):
                    return None
            alone = len(content) <= 1
            edge_forced = forced if is_last_conjunct else True
            if last.cls in {"N", "PRON", "NAME", "REL", "FRAME"}:
                pass
            elif last.cls in {"ADJ", "V"}:
                if not full and not (alone and edge_forced):
                    return None
            elif last.cls == "DET":
                if not edge_forced:
                    return None
            elif last.cls == "S2":
                if last.word not in {"ha", "ra"} or any(u.cls != "S2" for u in conjunct):
                    return None
            else:
                return None
            if is_last_conjunct:
                head_kind = "TIME" if last.temporal else "NOUN"
        return head_kind

    def _template_ok(
        self,
        body: Sequence[Unit],
        types: Sequence[str],
        has_ka: bool,
        predicative: bool,
        relaxed: bool,
    ) -> bool:
        count = len(types)
        bare = [position for position, kind in enumerate(types) if kind == "BARE"]
        limit = 3 if has_ka else 2
        if len(bare) > limit:
            return False
        if predicative:
            # nai and kelu need a complement, and canon makes a clause-initial
            # pronoun before one the subject: mia lohau nai is "I am a dog".
            if count == 0:
                return False
            content = [unit for unit in body if unit.cls != "S2"]
            if count == 1 and len(content) > 1 and content[0].cls == "PRON":
                return False
        if relaxed:
            return True
        allowed = {0, count - 1}
        if has_ka:
            allowed.add(count - 2)
        return all(position in allowed for position in bare)

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def _render(self, pre: Sequence[Unit], division: tuple) -> str:
        if not division:
            return ""
        boundaries, tail, _ = division
        parts = []
        position = 0
        for stop in boundaries:
            words = " ".join(
                " ".join(self._words(u.start, u.end)) for u in pre[position:stop]
            )
            parts.append(f"[{words}]")
            position = stop
        if tail < len(pre):
            words = " ".join(u.word for u in pre[tail:])
            parts.append(f"<{words}>")
        return " ".join(parts)

    def _seam_types(self, pre: Sequence[Unit], divisions: Sequence[tuple]) -> set[str]:
        """Name each place that is a phrase edge in one reading and not in another."""
        types: set[str] = set()
        edge_sets = []
        manner_starts = set()
        for boundaries, tail, _ in divisions:
            edges = set(boundaries)
            if tail < len(pre):
                manner_starts.add(tail)
            edge_sets.append(edges - {len(pre)})
        if len(manner_starts) > 0 and any(tail == len(pre) for _, tail, _ in divisions):
            types.add("manner or object")
        every = set().union(*edge_sets) if edge_sets else set()
        for edge in sorted(every):
            if all(edge in edges for edges in edge_sets):
                continue
            left, right = pre[edge - 1], pre[edge]
            if left.temporal or right.temporal or self._phrase_is_time(pre, edge):
                types.add("time word")
            elif right.cls == "S2":
                types.add("before a Slot 2 word")
            elif left.cls == "PRON":
                types.add("pronoun then noun")
            elif left.cls == "NAME":
                types.add("name then noun")
            elif left.cls in {"ADJ", "V"} or right.cls in {"ADJ", "V"}:
                types.add("quality or event word")
            else:
                types.add("noun then noun")
        return types

    def _phrase_is_time(self, pre: Sequence[Unit], edge: int) -> bool:
        position = edge
        while position < len(pre) and pre[position].cls in {"S2", "DET", "ADJ"}:
            position += 1
        return position < len(pre) and pre[position].temporal


def count_readings(text: str, counter: ReadingCounter | None = None) -> SentenceReadings | None:
    """Convenience wrapper for one sentence."""
    return (counter or ReadingCounter()).analyse(text)
