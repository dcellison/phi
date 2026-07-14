#!/usr/bin/env python3
"""Regression tests for the executable Phi vocabulary schema."""

import copy
import unittest

from jsonschema import Draft202012Validator

import validate_examples
import vocabulary_prose_coverage


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

    def target_entry(self, word="sileta"):
        entry = copy.deepcopy(self.by_word[word])
        notes = {
            "sileta": (
                "The word opens with a narrow 'si', rests its stress on 'le', "
                "and closes with dental contact in 'ta'."
            ),
            "to": "The tongue meets the teeth for 't', then releases into rounded 'o'.",
            "kia": (
                "The back of the tongue closes for 'k', releases into 'i', "
                "and keeps final 'a' in a separate syllable."
            ),
        }
        examples = {
            "sileta": {
                "phi": "sileta keru nai.",
                "translation": "The sun is bright.",
            },
            "to": {"phi": "mia to nai.", "translation": "I was."},
            "kia": {"phi": "kia.", "translation": "Hello."},
        }
        entry["articulatory_notes"] = notes[word]
        entry["examples"] = [examples[word]]
        entry.pop("concept", None)
        entry.pop("grammatical_notes", None)
        return entry

    def legacy_entry(self, word="sileta"):
        entry = copy.deepcopy(self.by_word[word])
        entry.pop("articulatory_notes", None)
        entry.pop("examples", None)
        entry.pop("search_terms", None)
        entry.pop("usage_notes", None)
        entry["concept"] = "Legacy discovery label"
        entry["sound_symbolism"] = "A legacy account of the word's sounds."
        entry["grammatical_notes"] = "A legacy account of grammar and examples."
        return entry

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

    def test_target_prose_contract_is_valid(self):
        for word in ("sileta", "to", "kia"):
            with self.subTest(word=word):
                entry = self.target_entry(word)
                entry.pop("sound_symbolism", None)
                entry.pop("pillars", None)
                self.assertEqual(validate_examples.entry_schema_errors(entry), [])

    def test_legacy_prose_contract_remains_valid_during_migration(self):
        entry = self.legacy_entry()
        self.assertNotIn("articulatory_notes", entry)
        self.assertNotIn("examples", entry)
        self.assertEqual(validate_examples.entry_schema_errors(entry), [])

    def test_articulatory_or_legacy_sound_field_is_required(self):
        entry = self.legacy_entry()
        del entry["sound_symbolism"]
        self.assert_invalid(entry, "not valid under any of the given schemas")

    def test_structured_examples_or_legacy_grammar_field_is_required(self):
        entry = self.legacy_entry()
        del entry["grammatical_notes"]
        self.assert_invalid(entry, "not valid under any of the given schemas")

    def test_structured_example_shape_is_closed(self):
        entry = self.target_entry()
        del entry["examples"][0]["translation"]
        self.assert_invalid(entry, "translation")
        entry = self.target_entry()
        entry["examples"][0]["gloss"] = "sun bright COP"
        self.assert_invalid(entry, "Additional properties")

    def test_structured_example_phi_shape_is_restricted(self):
        entry = self.target_entry()
        entry["examples"][0]["phi"] = "Sileta keru nai!"
        self.assert_invalid(entry, "does not match")

    def test_search_terms_are_nonempty_and_unique(self):
        entry = self.target_entry()
        entry["search_terms"] = ["day star", "day star"]
        self.assert_invalid(entry, "non-unique")
        entry["search_terms"] = [""]
        self.assert_invalid(entry, "should be non-empty")

    def test_prose_coverage_states(self):
        legacy = self.legacy_entry()
        partial = copy.deepcopy(legacy)
        partial["articulatory_notes"] = "A physical pronunciation note."
        dual = self.target_entry()
        dual["concept"] = legacy["concept"]
        target = self.target_entry()
        self.assertEqual(vocabulary_prose_coverage.entry_state(legacy), "legacy")
        self.assertEqual(vocabulary_prose_coverage.entry_state(partial), "partial")
        self.assertEqual(vocabulary_prose_coverage.entry_state(dual), "dual")
        self.assertEqual(vocabulary_prose_coverage.entry_state(target), "target")

    def test_target_structured_example_passes_phi_validation(self):
        lexicon_words = set(self.by_word)
        content_words = {
            data["word"] for rel, data in self.entries if rel.parts[1] == "content"
        }
        prepositions = {
            data["word"] for _rel, data in self.entries
            if data.get("pos") == "preposition"
        }
        ranks = validate_examples.slot1_rank_map(self.entries)
        self.assertEqual(
            validate_examples.structured_example_errors(
                "test", 0, "sileta keru nai.", lexicon_words,
                content_words, prepositions, ranks
            ),
            [],
        )
        self.assertEqual(
            validate_examples.structured_example_errors(
                "test", 0, "mia ma nai. mia to nai.", lexicon_words,
                content_words, prepositions, ranks
            ),
            [],
        )
        errors = validate_examples.structured_example_errors(
            "test", 0, "sileta notaword nai.", lexicon_words,
            content_words, prepositions, ranks
        )
        self.assertTrue(any("unknown Phi word 'notaword'" in error for error in errors))
        self.assertTrue(validate_examples.structured_examples_use_word(
            "sileta", [{"phi": "sileta keru nai."}]
        ))
        self.assertFalse(validate_examples.structured_examples_use_word(
            "sileta", [{"phi": "mia to nai."}]
        ))


if __name__ == "__main__":
    unittest.main()
