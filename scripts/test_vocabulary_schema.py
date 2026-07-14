#!/usr/bin/env python3
"""Regression tests for the executable Phi vocabulary schema."""

import copy
import unittest

from jsonschema import Draft202012Validator

import validate_examples


class VocabularySchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, errors = validate_examples.load_lexicon()
        if errors:
            raise AssertionError("\n".join(errors))
        cls.by_word = {data["word"]: data for _rel, data in cls.entries}

    def assert_invalid(self, entry, message_part=None):
        errors = validate_examples.entry_schema_errors(entry)
        self.assertTrue(errors)
        if message_part:
            self.assertTrue(
                any(message_part in error for error in errors),
                f"{message_part!r} not found in {errors}",
            )

    def test_schema_uses_and_satisfies_draft_2020_12(self):
        self.assertEqual(
            validate_examples.VOCABULARY_SCHEMA["$schema"],
            "https://json-schema.org/draft/2020-12/schema",
        )
        Draft202012Validator.check_schema(validate_examples.VOCABULARY_SCHEMA)

    def test_current_lexicon_satisfies_schema(self):
        for rel, entry in self.entries:
            with self.subTest(path=rel):
                self.assertEqual(validate_examples.entry_schema_errors(entry), [])

    def test_part_of_speech_is_one_scalar_value(self):
        entry = copy.deepcopy(self.by_word["sileta"])
        entry["pos"] = [entry["pos"]]
        self.assert_invalid(entry, "is not of type 'string'")

    def test_content_word_requires_semantic_domains(self):
        entry = copy.deepcopy(self.by_word["sileta"])
        del entry["semantic_domains"]
        self.assert_invalid(entry, "semantic_domains")

    def test_retired_tags_field_is_rejected(self):
        entry = copy.deepcopy(self.by_word["sileta"])
        entry["tags"] = entry["semantic_domains"]
        self.assert_invalid(entry, "Additional properties")

    def test_slot_1_particle_requires_rank(self):
        entry = copy.deepcopy(self.by_word["to"])
        del entry["slot1_rank"]
        self.assert_invalid(entry, "slot1_rank")

    def test_rank_is_forbidden_outside_slot_1(self):
        entry = copy.deepcopy(next(
            data for _rel, data in self.entries
            if data.get("pos") == "particle" and data.get("slot") == 0
        ))
        entry["slot1_rank"] = "tense"
        self.assert_invalid(entry, "should not be valid")

    def test_slot_1_metadata_matches_canonical_categories(self):
        expected = {
            "tense": {"to", "so"},
            "aspect": {"ki", "si", "pa", "te", "ro"},
            "voice": {"se", "ka"},
            "evidentiality": {"hi", "ke", "ti", "ho"},
            "modality": {"po", "na"},
            "negation": {"ma"},
        }
        actual = {rank: set() for rank in expected}
        for _rel, entry in self.entries:
            if entry.get("slot") == 1:
                actual[entry["slot1_rank"]].add(entry["word"])
        self.assertEqual(actual, expected)

    def test_slot_1_order_check_uses_entry_metadata(self):
        ranks = validate_examples.slot1_rank_map(self.entries)
        self.assertEqual(
            validate_examples.slot1_misorders(
                "to ki se hi po ma".split(), ranks
            ),
            [],
        )
        self.assertEqual(
            validate_examples.slot1_misorders("ma to".split(), ranks),
            ["ma to"],
        )
        self.assertEqual(
            validate_examples.slot1_misorders("se ka".split(), ranks),
            [],
        )

    def test_empty_required_prose_is_rejected(self):
        entry = copy.deepcopy(self.by_word["sileta"])
        entry["description"] = ""
        self.assert_invalid(entry, "should be non-empty")


if __name__ == "__main__":
    unittest.main()
