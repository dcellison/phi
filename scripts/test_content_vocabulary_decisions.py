#!/usr/bin/env python3
"""Tests for the content-vocabulary decision gate."""

import copy
import unittest

import content_vocabulary_decisions as decisions


class ContentVocabularyDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = decisions.load_data()
        cls.coverage = decisions.COVERAGE_FILE.read_text(encoding="utf-8")

    def test_repository_register_is_valid(self):
        self.assertEqual(decisions.validate(self.data, coverage_text=self.coverage), [])

    def test_open_candidate_keeps_batch_open(self):
        data = copy.deepcopy(self.data)
        candidate = next(item for item in data["candidates"] if item["status"] == "open")
        batch_id = candidate["batches"][0]
        batch = next(item for item in data["batches"] if item["id"] == batch_id)
        batch["decision_status"] = "closed"
        errors = decisions.validate(data, coverage_text=self.coverage)
        self.assertTrue(any("closed with unresolved decisions" in error for error in errors))

    def test_batch_cannot_claim_open_without_unresolved_work(self):
        data = copy.deepcopy(self.data)
        batch = next(item for item in data["batches"] if item["decision_status"] == "closed")
        batch["decision_status"] = "open"
        errors = decisions.validate(data, coverage_text=self.coverage)
        self.assertTrue(any("open without an open or accepted decision" in error for error in errors))

    def test_deferred_candidate_needs_return_trigger(self):
        data = copy.deepcopy(self.data)
        candidate = next(item for item in data["candidates"] if item["status"] == "deferred")
        candidate.pop("revisit_when")
        errors = decisions.validate(data, coverage_text=self.coverage)
        self.assertTrue(any("deferred decisions need revisit_when" in error for error in errors))

    def test_implementation_words_match_files(self):
        data = copy.deepcopy(self.data)
        candidate = next(item for item in data["candidates"] if item["status"] == "implemented")
        candidate["implementation"]["words"] = ["notaword"]
        errors = decisions.validate(data, coverage_text=self.coverage)
        self.assertTrue(any("implementation words do not match" in error for error in errors))

    def test_unmarked_review_row_is_rejected(self):
        coverage = self.coverage.replace("CV-MAT-03", "UNTRACKED", 1)
        errors = decisions.validate(self.data, coverage_text=coverage)
        self.assertTrue(any("unregistered REVIEW or DEFERRED row" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
