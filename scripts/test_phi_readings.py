#!/usr/bin/env python3
"""Regression tests for the structural-reading counter."""

from pathlib import Path
import subprocess
import sys
import unittest

from phi_readings import ReadingCounter


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class ReadingCounterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.counter = ReadingCounter()

    def counts(self, text):
        result = self.counter.analyse(text)
        self.assertIsNotNone(result, text)
        return result.conservative, result.full

    def test_settled_clauses_have_one_reading(self):
        for text in (
            "mia thia nila.",
            "melu to kamo.",
            "lopia tei norawhi wile.",
            "shia to pakiro whano.",
            "mia thia ru woraka.",
        ):
            with self.subTest(text=text):
                self.assertEqual((1, 1), self.counts(text))

    def test_a_bare_noun_chain_divides_at_every_seam(self):
        result = self.counter.analyse("phao lopia shelu theo.")
        self.assertEqual(3, result.conservative)
        self.assertEqual(
            ["[phao] [lopia shelu]", "[phao lopia] [shelu]", "[phao lopia shelu]"],
            result.clauses[0].divisions,
        )
        self.assertEqual(["noun then noun"], result.clauses[0].seams)

    def test_the_causative_admits_a_third_bare_phrase(self):
        self.assertEqual((4, 4), self.counts("phao lopia shelu ka theo."))

    def test_a_pronoun_begins_its_phrase(self):
        self.assertEqual((1, 1), self.counts("mia shia wiru ma nila."))

    def test_canon_settles_the_pronoun_before_nai(self):
        self.assertEqual((1, 1), self.counts("mia lohau nai."))
        self.assertEqual(1, self.counts("mia lohau welao nai.")[0])

    def test_manner_or_object_without_a_slot_one_stack(self):
        result = self.counter.analyse("shia welao thumela.")
        self.assertEqual((2, 3), (result.conservative, result.full))
        self.assertEqual(["[shia] <welao>", "[shia] [welao]"], result.clauses[0].divisions)
        self.assertEqual(["manner or object"], result.clauses[0].seams)

    def test_an_event_noun_with_a_possessor_is_a_full_count_reading(self):
        self.assertEqual((1, 2), self.counts("mia nohero to helui."))

    def test_a_bare_time_word_is_an_open_seam(self):
        result = self.counter.analyse("mia nosa thole.")
        self.assertEqual(2, result.conservative)
        self.assertEqual(["time word"], result.clauses[0].seams)

    def test_a_prepositional_phrase_has_no_marked_end(self):
        result = self.counter.analyse("mia mua womu shelu theo.")
        self.assertEqual(
            ["[mia] [mua womu] [shelu]", "[mia] [mua womu shelu]"],
            result.clauses[0].divisions,
        )

    def test_dependent_material_may_end_in_more_than_one_place(self):
        result = self.counter.analyse("lao pheralu ruela wirua nai.")
        self.assertEqual(2, result.conservative)
        self.assertEqual([("adverbial", 2)], [(j.kind, j.alternatives) for j in result.joins])
        result = self.counter.analyse("tei thia shua mia so hasi.")
        self.assertEqual([("adverbial", 2)], [(j.kind, j.alternatives) for j in result.joins])

    def test_quoted_sentences_count_as_sentences_of_their_own(self):
        parts = self.counter.analyse_sentences(
            "ne kulo sha lia. mia melu shelu so theo sho to haolu."
        )
        self.assertEqual(
            [("ne kulo sha... sho to haolu.", 1), ("lia.", 1), ("mia melu shelu so theo.", 3)],
            [(part.text, part.conservative) for part in parts],
        )

    def test_opener_what_if_closes_the_seam_before_a_slot_two_word(self):
        self.assertEqual((2, 2), self.counts("phao ha shelu theo."))
        strict = ReadingCounter(openers=frozenset({"ha", "ra", "lo"}))
        self.assertEqual(1, strict.analyse("phao ha shelu theo.").conservative)

    def test_the_object_particle_settles_where_the_object_begins(self):
        for text in (
            "phao ku lopia shelu theo.",
            "phao lopia ku shelu theo.",
            "shia ku welao thumela.",
            "mia mua womu ku shelu theo.",
            "mia ku nohero to helui.",
        ):
            with self.subTest(text=text):
                self.assertEqual((1, 1), self.counts(text))

    def test_a_lone_deictic_ends_its_phrase(self):
        for text in (
            "ha ra to nila.",
            "ha ra lopia to nila.",
            "ha ku lopia to nila.",
            "ra we lopia to nila.",
        ):
            with self.subTest(text=text):
                self.assertEqual((1, 1), self.counts(text))

    def test_the_other_pronoun_begins_its_phrase_as_shia_does(self):
        self.assertEqual((1, 1), self.counts("mia hia wiru ma nila."))
        self.assertEqual((1, 1), self.counts("shia roa hia to pa rato."))

    def test_a_causee_before_a_marked_object_may_still_join_the_subject(self):
        result = self.counter.analyse("phao lopia ku shelu ka theo.")
        self.assertEqual(
            ["[phao] [lopia] [ku shelu]", "[phao lopia] [ku shelu]"],
            result.clauses[0].divisions,
        )

    def test_a_sentence_that_does_not_parse_has_no_count(self):
        self.assertIsNone(self.counter.analyse("mia shua mia."))

    def test_cli_shows_the_divisions(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(PROJECT_ROOT / "scripts" / "audit_phrase_readings.py"),
                "--sentence",
                "phao lopia shelu theo.",
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("readings: 3 conservative, 3 full", completed.stdout)
        self.assertIn("[phao lopia] [shelu]", completed.stdout)


if __name__ == "__main__":
    unittest.main()
