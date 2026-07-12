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

    def test_form_absent_from_current_lexicon_is_valid(self):
        self.assertEqual(name_forms.form_errors("samira"), [])
        self.assertNotIn("samira", self.words)

    def test_every_legal_four_syllable_candidate_is_valid(self):
        for form in ("saweriko", "phelanumi", "tukemaro"):
            with self.subTest(form=form):
                self.assertEqual(name_forms.form_errors(form), [])
                self.assertNotIn(form, self.words)

    def test_retired_former_boundaries_are_ordinary_onyms(self):
        for form in ("hasha", "hasho", "patha", "patho"):
            with self.subTest(form=form):
                self.assertNotIn(form, self.words)
                self.assertEqual(name_forms.form_errors(form), [])

    def test_lexical_retirement_does_not_affect_names(self):
        self.assertIn("sorae", validate_examples.RETIRED_FORMS)
        self.assertEqual(name_forms.form_errors("sorae"), [])

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
        self.assertTrue(any("current function" in error for error in errors))

    def test_every_non_content_lexicon_form_is_excluded_from_names(self):
        for token in sorted(self.words - self.content_words):
            with self.subTest(token=token):
                errors = validate_examples.name_atom_errors(
                    token, self.words, self.content_words
                )
                self.assertTrue(
                    any("current function" in error for error in errors)
                )

    def test_name_report_is_supported_validation_mechanism(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            valid = validate_examples.name_report(self.entries, "saweriko")
            absent = validate_examples.name_report(self.entries, "sorae")
            function = validate_examples.name_report(self.entries, "wa")
        self.assertEqual(valid, 0)
        self.assertEqual(absent, 0)
        self.assertEqual(function, 1)
        self.assertIn("valid productive name-form", output.getvalue())
        self.assertIn("current function", output.getvalue())

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

    def test_gloss_carries_retired_content_form_as_name(self):
        expected = validate_examples.expected_gloss_stream(
            "ne sorae shua.", self.glosses
        )
        actual = "NAME sorae come".split()
        self.assertEqual(len(actual), len(expected))
        self.assertTrue(all(
            token in choices for token, choices in zip(actual, expected)
        ))

    def test_productive_name_renders_in_tengwar(self):
        for name in ("samira", "saweriko", "sorae"):
            with self.subTest(name=name):
                line = f"ne {name}."
                self.assertTrue(tengwar.phi_line(line, self.words))
                rendered = tengwar.render_line(line)
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

    def test_lexicon_has_no_four_syllable_forms(self):
        long_forms = {
            data["word"]
            for _rel, data in self.entries
            if len(data["syllables"]) > 3
        }
        self.assertEqual(long_forms, set())

    def test_migrated_four_syllable_forms_are_ordinary_onyms(self):
        migrated = {
            row["old_form"]
            for row in validate_examples.FOUR_SYLLABLE_MIGRATION
        }
        self.assertTrue(migrated)
        self.assertTrue(migrated.isdisjoint(validate_examples.RETIRED_FORMS))
        for form in migrated:
            with self.subTest(form=form):
                self.assertEqual(name_forms.form_errors(form), [])

    def test_retired_lexical_list_contains_only_short_forms(self):
        for form in validate_examples.RETIRED_FORMS:
            with self.subTest(form=form):
                syllables = validate_examples.syllabify(form)
                self.assertIsNotNone(syllables)
                self.assertLessEqual(len(syllables), 3)


class ProsePolicyTests(unittest.TestCase):
    def test_hyphen_plus_bearing_construction_is_rejected(self):
        for prefix in ("method", "Fur", "pigment-and-gold"):
            with self.subTest(prefix=prefix):
                prohibited = prefix + "-" + "bearing"
                self.assertTrue(
                    validate_examples.contains_prohibited_hyphenated_construction(
                        f"A {prohibited} form."
                    )
                )
        self.assertFalse(
            validate_examples.contains_prohibited_hyphenated_construction(
                "A form that carries the method."
            )
        )


if __name__ == "__main__":
    unittest.main()
