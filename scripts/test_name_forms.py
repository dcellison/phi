#!/usr/bin/env python3
"""Regression tests for productive Phi-form proper names."""

import contextlib
import io
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
        cls.entries = entries
        cls.content_words = {
            data["word"] for rel, data in entries
            if len(rel.parts) > 1 and rel.parts[1] == "content"
        }
        cls.glosses = {data["word"]: data["gloss"] for _, data in entries}

    def test_unlisted_content_shaped_form_is_valid(self):
        self.assertEqual(name_forms.form_errors("samira"), [])
        self.assertNotIn("samira", self.words)

    def test_four_syllable_form_is_invalid(self):
        self.assertTrue(name_forms.form_errors("saweriko"))

    def test_retired_external_boundaries_cannot_be_names(self):
        for form in ("hasha", "hasho", "patha", "patho"):
            with self.subTest(form=form):
                self.assertEqual(
                    name_forms.form_errors(form),
                    ["is a retired Phi form"],
                )

    def test_form_must_be_content_shaped(self):
        self.assertTrue(name_forms.form_errors("sa"))
        self.assertTrue(name_forms.form_errors("sawerikona"))
        self.assertTrue(name_forms.form_errors("amina"))

    def test_duplicated_syllables_remain_prohibited(self):
        self.assertTrue(name_forms.form_errors("mimimi"))
        self.assertTrue(name_forms.form_errors("toronoto"))

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

    def test_every_non_content_lexicon_form_is_reserved(self):
        for token in sorted(self.words - self.content_words):
            with self.subTest(token=token):
                errors = validate_examples.name_atom_errors(
                    token, self.words, self.content_words
                )
                self.assertTrue(any("reserved" in error for error in errors))

    def test_name_report_is_supported_validation_mechanism(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            valid = validate_examples.name_report(self.entries, "samira")
            reserved = validate_examples.name_report(self.entries, "wa")
        self.assertEqual(valid, 0)
        self.assertEqual(reserved, 1)
        self.assertIn("valid productive name-form", output.getvalue())
        self.assertIn("reserved", output.getvalue())

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
        rendered = tengwar.render_line("ne samira.")
        self.assertIn("teng-svg", rendered)


class MigrationPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, errors = validate_examples.load_lexicon()
        if errors:
            raise AssertionError("\n".join(errors))

    def test_fixed_migration_ledger_is_structurally_valid(self):
        self.assertEqual(validate_examples.MIGRATION_ERRORS, [])
        self.assertEqual(
            len(validate_examples.FOUR_SYLLABLE_MIGRATION),
            validate_examples.MIGRATION_ROW_COUNT,
        )

    def test_pending_ledger_exactly_matches_long_lexicon_forms(self):
        long_forms = {
            data["word"]
            for _rel, data in self.entries
            if len(data["syllables"]) > 3
        }
        self.assertEqual(
            long_forms,
            set(validate_examples.PENDING_FOUR_SYLLABLE_FORMS),
        )


if __name__ == "__main__":
    unittest.main()
