#!/usr/bin/env python3
"""Count open roles and contested third persons in Phi text.

``phi_readings`` counts how a clause divides into phrases. Two things it
cannot see are where readers of the certified texts actually went wrong:

* **An open role.** A clause has one bare phrase and a verb that elsewhere
  takes both a subject and an object. Phi lets an established subject go
  unsaid and marks no case, so the phrase is the subject (with nothing said
  about an object) or the object (with the subject unsaid). ``lopia nuola``
  is "the child eats" and "(it) eats the child".
* **A contested third person.** Phi has one third-person pronoun. When two
  or more third persons are live in the story, ``shia`` and an unsaid
  subject both leave the listener to choose.

Neither count uses meanings. Whether a verb takes an object is read from
the corpus itself, so the figures are indicators of exposure, not rates of
misunderstanding.

A verb counts as taking an object when the corpus shows it at least once

* with its object opened by ``ku`` (``phao ku shelu theo``),
* in the passive (``shelu se theo``),
* with two bare phrases that cannot be read as one, each headed by a noun,
  pronoun, name, or complement frame (``mia thia nila``,
  ``mia tha ... tho sano``), or
* in a command over a noun phrase that is not the person addressed
  (``no shelu theo``).

Only clauses with a single structural reading are taken as witnesses, so an
adjective standing as manner or complement is not mistaken for an object.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, field
from typing import Iterable

from phi_readings import ClauseReadings, SentenceReadings
from phi_sentence_validator import PREDICATIVE_VERBS

ADDRESSEE = frozenset({"thia"})
ARGUMENT_HEADS = frozenset({"N", "PRON", "NAME", "FRAME", "REL"})
# How many earlier sentences a third person stays live for.
WINDOW = 3


def settled(sentence: SentenceReadings) -> bool:
    """Whether every dependent clause in the sentence has one possible end."""
    return all(join.alternatives == 1 for join in sentence.joins)


def object_taking_verbs(sentences: Iterable[SentenceReadings]) -> Counter[str]:
    """Verbs the corpus shows with an object, with the number of witnesses."""
    seen: Counter[str] = Counter()
    for sentence in sentences:
        if not settled(sentence):
            continue
        for clause in sentence.clauses:
            verb = clause.verb
            if not verb or verb in PREDICATIVE_VERBS or "ka" in clause.slot1:
                continue
            if "se" in clause.slot1 or clause.object_marked:
                seen[verb] += 1
                continue
            if clause.gapped or clause.full != 1:
                continue
            heads_ok = all(cls in ARGUMENT_HEADS for cls, _ in clause.bare_heads)
            if clause.bare_counts == (2,) and heads_ok:
                seen[verb] += 1
            elif (
                "no" in clause.slot0
                and clause.bare_counts == (1,)
                and clause.bare_heads
                and clause.bare_heads[0][0] in {"N", "NAME"}
            ):
                seen[verb] += 1
    return seen


def open_role(clause: ClauseReadings, object_verbs: Counter[str] | set[str]) -> str | None:
    """Name the open role in a clause, if it has one.

    ``main`` is a clause whose one bare phrase may be subject or object.
    ``relative`` is a relative clause whose head may be either, because the
    one phrase left inside it may be the other.
    """
    if clause.verb not in object_verbs or clause.verb in PREDICATIVE_VERBS:
        return None
    if "se" in clause.slot1 or "ka" in clause.slot1:
        return None
    if clause.object_marked:
        return None
    if clause.bare_counts != (1,):
        return None
    if not clause.bare_heads or clause.bare_heads[0][0] not in ARGUMENT_HEADS:
        return None
    if clause.gapped:
        return "relative"
    if "no" in clause.slot0:
        return None
    return "main"


@dataclass
class ReferenceCounts:
    """Third-person exposure in one sentence."""

    third_person_pronouns: int = 0
    contested_pronouns: int = 0
    doubled_clauses: int = 0
    unsaid_subjects: int = 0
    contested_unsaid: int = 0
    live: tuple[str, ...] = ()


@dataclass
class ReferenceTracker:
    """Follow which third persons are live as a text goes by.

    A third person is the head of a clause-initial bare phrase that is a
    noun or a name: the likeliest subjects. It stays live for ``window``
    further sentences. This is a heuristic. It knows nothing of animacy or
    plausibility, and it treats a thing and a person alike, as ``shia`` does.
    """

    window: int = WINDOW
    recent: deque = field(default_factory=deque)

    def reset(self) -> None:
        self.recent.clear()

    def observe(self, sentence: SentenceReadings) -> ReferenceCounts:
        own = []
        for clause in sentence.clauses:
            if clause.gapped or clause.first_bare is None:
                continue
            cls, word = clause.first_bare
            if cls in {"N", "NAME"}:
                own.append(word)
        live = set(own)
        for earlier in self.recent:
            live.update(earlier)
        counts = ReferenceCounts(live=tuple(sorted(live)))
        words = sentence.text.replace(".", " ").split()
        counts.third_person_pronouns = words.count("shia")
        if len(live) >= 2:
            counts.contested_pronouns = counts.third_person_pronouns
        for clause in sentence.clauses:
            if clause.third_persons >= 2:
                counts.doubled_clauses += 1
            if (
                not clause.gapped
                and clause.bare_counts == (0,)
                and "no" not in clause.slot0
                and clause.verb not in PREDICATIVE_VERBS
            ):
                counts.unsaid_subjects += 1
                if len(live) >= 2:
                    counts.contested_unsaid += 1
        self.recent.append(own)
        while len(self.recent) > self.window:
            self.recent.popleft()
        return counts
