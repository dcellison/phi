#!/usr/bin/env python3
"""Tests for independent source-reconstruction checking."""

import copy
import json
import tempfile
import unittest
from pathlib import Path

import source_reconstruction as reconstruction


class SourceReconstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repository_manifest = reconstruction.load_manifest()

    def fixture(self, citations):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        source = root / "source.txt"
        translation = root / "translation.md"
        source.write_text(
            "CHAPTER I: TEST\n\nAlpha one. Beta two. Gamma three.\n\n"
            "CHAPTER II: NEXT\n\nDelta four.\n",
            encoding="utf-8",
        )
        blocks = []
        for index, citation in enumerate(citations, start=1):
            blocks.append(
                "```\n"
                f"mia nai.\n1SG be.\n(I exist, unit {index}.)\n"
                f"morris: {json.dumps(citation)}\n"
                "```"
            )
        translation.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
        data = {
            "format": reconstruction.FORMAT,
            "required_translation_globs": ["translation.md"],
            "documents": [
                {
                    "translation": "translation.md",
                    "source": "source.txt",
                    "citation_label": "morris",
                    "selection": {
                        "start_after": "CHAPTER I: TEST",
                        "end_before": "CHAPTER II: NEXT",
                    },
                    "normalization": reconstruction.NORMALIZATION,
                }
            ],
        }
        return temporary, root, data

    def check_fixture(self, citations):
        temporary, root, data = self.fixture(citations)
        self.addCleanup(temporary.cleanup)
        return reconstruction.check_manifest(data, root)

    def test_repository_manifest_reconstructs_six_morris_chapters(self):
        results, errors = reconstruction.check_manifest(self.repository_manifest)
        self.assertEqual(errors, [])
        self.assertEqual(len(results), 6)
        self.assertEqual(sum(result.citation_count for result in results), 1054)
        self.assertEqual(
            sum(result.normalized_characters for result in results),
            75243,
        )
        self.assertEqual(
            [result.translation for result in results],
            [f"texts/news_from_nowhere/chapter_{number:02}.md" for number in range(1, 7)],
        )

    def test_exact_reconstruction_passes(self):
        results, errors = self.check_fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.assertEqual(errors, [])
        self.assertEqual(results[0].normalized_characters, 33)

    def test_gutenberg_normalization_repairs_layout_only(self):
        source = "After-\nlecture  Morris--Word\n\nStays."
        self.assertEqual(
            reconstruction.normalize_gutenberg_prose(source),
            "After-lecture Morris--Word Stays.",
        )

    def test_missing_span_is_named(self):
        _results, errors = self.check_fixture(["Alpha one.", "Gamma three."])
        self.assertTrue(any("missing source span" in error for error in errors))

    def test_duplicated_span_is_named(self):
        _results, errors = self.check_fixture(
            ["Alpha one.", "Beta two.", "Beta two.", "Gamma three."]
        )
        self.assertTrue(any("duplicated source span" in error for error in errors))

    def test_reordered_spans_are_named(self):
        _results, errors = self.check_fixture(["Alpha one.", "Gamma three.", "Beta two."])
        self.assertTrue(any("reordered source spans" in error for error in errors))

    def test_altered_text_is_named(self):
        _results, errors = self.check_fixture(["Alpha one.", "Beta too.", "Gamma three."])
        self.assertTrue(any("altered source text" in error for error in errors))

    def test_unknown_normalization_is_rejected(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        data["documents"][0]["normalization"] = "unknown"
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(any("unsupported normalization" in error for error in errors))

    def test_missing_boundary_marker_is_rejected(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        data["documents"][0]["selection"]["start_after"] = "CHAPTER ZERO"
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(any("start marker must occur once" in error for error in errors))

    def test_repository_escape_is_rejected(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        data["documents"][0]["source"] = "../source.txt"
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(any("must stay inside the repository" in error for error in errors))

    def test_duplicate_translation_is_rejected(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        data["documents"].append(copy.deepcopy(data["documents"][0]))
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(any("duplicate translation" in error for error in errors))

    def test_required_translation_without_manifest_entry_is_rejected(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        extra = root / "translation_extra.md"
        extra.write_text((root / "translation.md").read_text(encoding="utf-8"), encoding="utf-8")
        data["required_translation_globs"] = ["translation*.md"]
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(
            any("missing source reconstruction manifest entry" in error for error in errors)
        )

    def test_required_translation_glob_cannot_escape_repository(self):
        temporary, root, data = self.fixture(["Alpha one.", "Beta two.", "Gamma three."])
        self.addCleanup(temporary.cleanup)
        data["required_translation_globs"] = ["../*.md"]
        _results, errors = reconstruction.check_manifest(data, root)
        self.assertTrue(
            any("glob must stay inside the repository" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
