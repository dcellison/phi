#!/usr/bin/env python3
"""Tests for the isolated-translation certification register."""

import copy
import unittest

import translation_process_status as status


class TranslationProcessStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = status.load_data()

    def test_repository_register_is_valid(self):
        self.assertEqual(status.validate(self.data), [])

    def test_current_scope_has_every_translation_document(self):
        discovered = status.discover_documents(self.data)
        self.assertEqual(len(discovered), 20)
        self.assertEqual(
            [item.path for item in discovered],
            [item["path"] for item in self.data["documents"]],
        )

    def test_missing_document_is_rejected(self):
        data = copy.deepcopy(self.data)
        missing = data["documents"].pop()
        errors = status.validate(data)
        self.assertTrue(any(missing["path"] in error and "missing" in error for error in errors))

    def test_certified_phi_digest_cannot_drift(self):
        data = copy.deepcopy(self.data)
        certified = next(item for item in data["documents"] if item["status"] == "certified")
        certified["certification"]["phi_sha256"] = "0" * 64
        errors = status.validate(data)
        self.assertTrue(any("frozen Phi digest is stale" in error for error in errors))

    def test_certified_aligned_layers_cannot_drift(self):
        data = copy.deepcopy(self.data)
        certified = next(item for item in data["documents"] if item["status"] == "certified")
        certified["certification"]["aligned_sha256"] = "0" * 64
        errors = status.validate(data)
        self.assertTrue(any("aligned-layer digest is stale" in error for error in errors))

    def test_source_character_count_matches_published_citations(self):
        data = copy.deepcopy(self.data)
        certified = next(item for item in data["documents"] if item["status"] == "certified")
        certified["certification"]["source_reconstruction"]["normalized_characters"] += 1
        errors = status.validate(data)
        self.assertTrue(any("normalized source characters" in error for error in errors))

    def test_pending_document_cannot_carry_certification(self):
        data = copy.deepcopy(self.data)
        pending = next(item for item in data["documents"] if item["status"] == "pending")
        pending["certification"] = {"decision": "D999"}
        errors = status.validate(data)
        self.assertTrue(any("only certified documents" in error for error in errors))

    def test_in_progress_document_needs_a_note(self):
        data = copy.deepcopy(self.data)
        pending = next(item for item in data["documents"] if item["status"] == "pending")
        pending["status"] = "in-progress"
        errors = status.validate(data)
        self.assertTrue(any("in-progress documents need a note" in error for error in errors))

    def test_every_catalogued_book_needs_a_relationship(self):
        data = copy.deepcopy(self.data)
        data["book_relationships"] = {}
        errors = status.validate(data)
        self.assertTrue(any("book_relationships must cover" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
