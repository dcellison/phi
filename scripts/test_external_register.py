#!/usr/bin/env python3
"""Regression tests for the external-register boundary parser."""

import unittest

import external_register
import tengwar
import validate_examples


class ExternalRegisterTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        entries, errors = validate_examples.load_lexicon()
        if errors:
            raise AssertionError(errors)
        cls.words = {data["word"] for _, data in entries}
        cls.glosses = {data["word"]: data["gloss"] for _, data in entries}

    def test_guest_payload_is_hidden_from_core_checks(self):
        result = external_register.analyze(
            "mia ne hasha toronoto hasho nila."
        )
        self.assertFalse(result.errors)
        self.assertEqual(len(result.spans), 1)
        self.assertEqual(result.spans[0].kind, "guest")
        self.assertNotIn("toronoto", result.core_text)
        self.assertIn("toronoto", result.punctuation_text)

    def test_guest_allows_repeated_syllables(self):
        result = external_register.analyze("hasha mamama hasho nai.")
        self.assertFalse(result.errors)

    def test_guest_rejects_non_phi_form(self):
        result = external_register.analyze("hasha Toronto-6 hasho nai.")
        self.assertTrue(any("guest token" in e for e in result.errors))

    def test_exact_payload_is_opaque(self):
        source = "mia patha Toronto, ON / 43.7°N patho nila."
        result = external_register.analyze(source)
        self.assertFalse(result.errors)
        self.assertNotIn("Toronto", result.core_text)
        self.assertNotIn(",", result.punctuation_text)
        self.assertIn("patha", result.core_text)
        self.assertIn("patho", result.core_text)

    def test_doubled_exact_closer_is_literal(self):
        result = external_register.analyze(
            "patha source patho patho token patho nai."
        )
        self.assertFalse(result.errors)
        span = result.spans[0]
        payload = "patha source patho patho token patho nai."[
            span.payload_start:span.payload_end
        ]
        self.assertIn("patho patho", payload)

    def test_doubled_closer_can_preserve_following_punctuation(self):
        result = external_register.analyze(
            "patha source patho patho. token patho nai."
        )
        self.assertFalse(result.errors)
        self.assertEqual(len(result.spans), 1)

    def test_frames_must_close(self):
        result = external_register.analyze("mia patha unclosed")
        self.assertIn("unclosed exact external frame", result.errors)

    def test_guest_frames_cannot_nest(self):
        result = external_register.analyze(
            "hasha one hasha two hasho hasho"
        )
        self.assertTrue(any("cannot nest" in e for e in result.errors))

    def test_empty_frames_are_rejected(self):
        guest = external_register.analyze("hasha hasho")
        exact = external_register.analyze("patha patho")
        self.assertIn("guest frame has an empty payload", guest.errors)
        self.assertIn("exact frame has an empty payload", exact.errors)

    def test_stray_closer_is_rejected(self):
        result = external_register.analyze("mia hasho nila.")
        self.assertIn("unexpected external closer 'hasho'", result.errors)

    def test_mixed_tengwar_preserves_and_escapes_exact_payload(self):
        rendered = tengwar.render_mixed_line(
            "patha <script>alert(1)</script> patho nai."
        )
        self.assertIn("&lt;script&gt;", rendered)
        self.assertNotIn("<script>", rendered)
        self.assertIn("external-exact-payload", rendered)

    def test_guest_payload_can_render_in_tengwar(self):
        rendered = tengwar.render_mixed_line(
            "hasha toronoto hasho nai."
        )
        self.assertIn("teng-svg", rendered)

    def test_validator_recognizes_exact_line_with_source_punctuation(self):
        source = "mia patha Toronto, ON / 43.7°N patho nila."
        self.assertTrue(validate_examples.is_phi_line(source, self.words))

    def test_gloss_stream_copies_external_payload_in_brackets(self):
        source = "mia ne patha Toronto patho nila."
        actual = "1SG NAME EXT.EXACT [Toronto] EXT.EXACT.CLOSE see".split()
        expected = validate_examples.expected_gloss_stream(source, self.glosses)
        self.assertEqual(len(actual), len(expected))
        self.assertTrue(all(word in choices for word, choices in zip(actual, expected)))

    def test_external_boundaries_have_only_their_designed_pair_neighbor(self):
        entries, _ = validate_examples.load_lexicon()
        words = {data["word"] for _, data in entries}
        pairs = {
            "hasha": "hasho", "hasho": "hasha",
            "patha": "patho", "patho": "patha",
        }
        for word, paired in pairs.items():
            neighbors = {
                other for other in words
                if other != word and validate_examples.edit_distance_leq1(
                    word, other
                )
            }
            self.assertEqual(neighbors, {paired})


if __name__ == "__main__":
    unittest.main()
