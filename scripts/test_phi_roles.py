#!/usr/bin/env python3
"""Regression tests for the open-role and third-person counts."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from phi_readings import ReadingCounter
from phi_roles import ReferenceTracker, object_taking_verbs, open_role


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class RoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.counter = ReadingCounter()

    def sentences(self, *texts):
        parts = []
        for text in texts:
            found = self.counter.analyse_sentences(text)
            self.assertIsNotNone(found, text)
            parts.extend(found)
        return parts

    def test_three_kinds_of_witness_show_a_verb_takes_an_object(self):
        verbs = object_taking_verbs(
            self.sentences("mia thia nila.", "shelu se theo.", "no noru kolua.")
        )
        self.assertEqual({"nila", "theo", "kolua"}, set(verbs))

    def test_manner_and_single_phrases_are_not_witnesses(self):
        verbs = object_taking_verbs(
            self.sentences("melu to kamo.", "shia welao thumela.", "no thia shua.")
        )
        self.assertEqual(set(), set(verbs))

    def test_one_bare_phrase_before_an_object_taking_verb_is_an_open_role(self):
        verbs = {"nila", "nuola"}
        (clause,) = self.sentences("lopia nuola.")[0].clauses
        self.assertEqual("main", open_role(clause, verbs))
        (clause,) = self.sentences("lo phirae tupiwa so ma nila.")[0].clauses
        self.assertEqual("main", open_role(clause, verbs))

    def test_roles_are_settled_by_two_phrases_passive_command_or_verb(self):
        verbs = {"nila", "nuola", "theo"}
        for text in ("mia thia nila.", "shelu se theo.", "no shelu theo.", "melu to kamo."):
            with self.subTest(text=text):
                (clause,) = self.sentences(text)[0].clauses
                self.assertIsNone(open_role(clause, verbs))

    def test_the_object_particle_settles_a_role_and_witnesses_the_verb(self):
        (clause,) = self.sentences("ku lopia to nila.")[0].clauses
        self.assertIsNone(open_role(clause, {"nila"}))
        clauses = self.sentences("whu ku mia nila miona shua.")[0].clauses
        self.assertNotIn("relative", [open_role(clause, {"nila"}) for clause in clauses])
        self.assertEqual({"somela"}, set(object_taking_verbs(self.sentences("ku lopia somela."))))

    def test_a_relative_clause_with_one_phrase_leaves_its_head_open(self):
        verbs = {"nila"}
        clauses = self.sentences("whu mia nila miona shua.")[0].clauses
        kinds = [open_role(clause, verbs) for clause in clauses]
        self.assertIn("relative", kinds)

    def test_third_persons_become_contested_when_two_are_live(self):
        tracker = ReferenceTracker()
        first, second, third = self.sentences(
            "ne samira to shua.", "lopia to wile.", "shia to hola."
        )
        self.assertEqual(0, tracker.observe(first).contested_pronouns)
        self.assertEqual(0, tracker.observe(second).contested_pronouns)
        counts = tracker.observe(third)
        self.assertEqual(1, counts.third_person_pronouns)
        self.assertEqual(1, counts.contested_pronouns)
        self.assertEqual(("lopia", "samira"), counts.live)

    def test_one_live_third_person_is_not_contested(self):
        tracker = ReferenceTracker()
        first, second = self.sentences("lopia to wile.", "shia to hola.")
        tracker.observe(first)
        self.assertEqual(0, tracker.observe(second).contested_pronouns)

    def test_two_separate_shia_in_one_clause_are_counted(self):
        tracker = ReferenceTracker()
        (sentence,) = self.sentences("shia roa shia to pa rato.")
        self.assertEqual(1, tracker.observe(sentence).doubled_clauses)

    def test_the_other_pronoun_is_counted_apart_from_shia(self):
        tracker = ReferenceTracker()
        (sentence,) = self.sentences("shia roa hia to pa rato.")
        counts = tracker.observe(sentence)
        self.assertEqual((1, 1, 0), (
            counts.third_person_pronouns, counts.other_pronouns, counts.doubled_clauses
        ))

    def test_an_unsaid_subject_is_counted(self):
        tracker = ReferenceTracker()
        first, second, third = self.sentences(
            "ne samira to shua.", "lopia to wile.", "mua womu to therilu."
        )
        tracker.observe(first)
        tracker.observe(second)
        counts = tracker.observe(third)
        self.assertEqual((1, 1), (counts.unsaid_subjects, counts.contested_unsaid))

    def test_committed_ledger_is_current(self):
        completed = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "scripts" / "audit_phrase_readings.py"), "--check"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)

    def test_ledger_refuses_the_what_if(self):
        with tempfile.TemporaryDirectory() as directory:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(PROJECT_ROOT / "scripts" / "audit_phrase_readings.py"),
                    "--openers",
                    "ha",
                    "--output",
                    str(Path(directory) / "ledger.txt"),
                ],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(2, completed.returncode)


if __name__ == "__main__":
    unittest.main()
