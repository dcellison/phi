#!/usr/bin/env python3
"""Regression tests for productive Phi-form proper names."""

import unittest

import name_forms
import tengwar
import validate_examples


class ProductiveNameFormTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        entries, errors = validate_examples.load_lexicon()
        if errors:
            raise AssertionError(errors)
        cls.words = {data["word"] for _, data in entries}
        cls.content_words = {
            data["word"] for rel, data in entries
            if len(rel.parts) > 1 and rel.parts[1] == "content"
        }
        cls.glosses = {data["word"]: data["gloss"] for _, data in entries}

    def test_unlisted_content_shaped_form_is_valid(self):
        self.assertEqual(name_forms.form_errors("samira"), [])
        self.assertNotIn("samira", self.words)

    def test_form_must_be_content_shaped(self):
        self.assertTrue(name_forms.form_errors("sa"))
        self.assertTrue(name_forms.form_errors("toronoto"))
        self.assertTrue(name_forms.form_errors("amina"))
        self.assertTrue(name_forms.form_errors("mamama"))

    def test_ne_and_honorific_select_one_atom(self):
        self.assertEqual(
            name_forms.marked_atom_indices("ne sa samira shua".split()),
            {2},
        )
        self.assertEqual(
            name_forms.marked_atom_indices("kona ni samira".split()),
            {2},
        )

    def test_content_word_can_be_a_name(self):
        self.assertEqual(
            validate_examples.name_atom_errors(
                "sulae", self.words, self.content_words
            ),
            [],
        )

    def test_function_word_cannot_be_a_name(self):
        errors = validate_examples.name_atom_errors(
            "wa", self.words, self.content_words
        )
        self.assertTrue(any("reserved" in error for error in errors))

    def test_external_frame_remains_a_name_atom(self):
        self.assertEqual(
            validate_examples.name_atom_errors(
                "patha", self.words, self.content_words
            ),
            [],
        )

    def test_validator_recognizes_short_name_line(self):
        self.assertTrue(validate_examples.is_phi_line("ne samira.", self.words))

    def test_gloss_carries_productive_name_form(self):
        expected = validate_examples.expected_gloss_stream(
            "ne samira shua.", self.glosses
        )
        actual = "NAME samira come".split()
        self.assertEqual(len(actual), len(expected))
        self.assertTrue(all(
            token in choices for token, choices in zip(actual, expected)
        ))

    def test_productive_name_renders_in_tengwar(self):
        self.assertTrue(tengwar.phi_line("ne samira.", self.words))
        rendered = tengwar.render_mixed_line("ne samira.")
        self.assertIn("teng-svg", rendered)


if __name__ == "__main__":
    unittest.main()
