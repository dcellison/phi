import json
import tempfile
import unittest
from pathlib import Path

from translation_layers import (
    RiskAssessment,
    TranslationUnit,
    assess_unit_risk,
    audit_plan,
    gloss_scaffold,
    parse_unit_spec,
    parse_units,
    phi_digest,
    phi_to_english_view,
    source_to_phi_view,
    unit_digest,
    write_packet_directory,
)


SAMPLE = '''# Sample

```
mia thia nila.
1SG 2SG see.
(I see you.)
sample: "I can see you."

shia to wepu.
3SG PST go.
(They went.)
sample: "She left."
```

**Notes:** Source wording and commentary stay outside both phase views.

```
mia thia nila. shia to wepu.
```
'''


def entry(word, gloss, pos="noun", description=None, **extra):
    value = {
        "word": word,
        "gloss": gloss,
        "pos": pos,
        "description": description or f"Compact description for {word}.",
    }
    value.update(extra)
    return value


LEXICON = {
    item["word"]: item
    for item in (
        entry("mia", "1SG", "pronoun"),
        entry("thia", "2SG", "pronoun"),
        entry("shia", "3SG", "pronoun"),
        entry("nila", "see", "verb"),
        entry("wepu", "go", "verb"),
        entry("to", "PST", "particle", slot=1, slot1_rank="tense"),
        entry("po", "POT", "particle", slot=1, slot1_rank="modality"),
        entry("ma", "NEG", "particle", slot=1, slot1_rank="negation"),
        entry("pha", "INT.COMP", "complementizer"),
        entry("pho", "INT.COMP.CLOSE", "complementizer"),
        entry("whu", "REL", "complementizer"),
        entry("lo", "PL", "particle", slot=2),
        entry("miona", "person", "noun"),
        entry("lothea", "love", "verb", modules=["philosophical-reasoning"]),
        entry("sano", "know", "verb"),
        entry("nela", "COORD", "conjunction"),
        entry("sola", "DISJ", "conjunction"),
        entry("nai", "be", "verb"),
        entry("ne", "NAME", "particle", slot=2),
        entry("unused", "unused", "noun"),
    )
}


COMPOUNDS = [
    {
        "compound": "miona lothea",
        "tokens": ["miona", "lothea"],
        "literal": "person-love",
        "meaning": "care for people",
        "why": "fixture",
        "section": "Fixture",
    }
]


class TranslationLayersTest(unittest.TestCase):
    def test_source_view_hides_english_layers(self):
        units = parse_units(SAMPLE)
        view = source_to_phi_view(Path("sample.md"), units)
        self.assertEqual(2, len(units))
        self.assertIn('"I can see you."', view)
        self.assertNotIn("1SG 2SG see", view)
        self.assertNotIn("(I see you.)", view)
        self.assertNotIn("Source wording and commentary", view)

    def test_phi_view_hides_source_and_prior_english(self):
        units = parse_units(SAMPLE)
        view = phi_to_english_view(units)
        self.assertIn("mia thia nila.", view)
        self.assertNotIn("sample.md", view)
        self.assertNotIn("sample:", view)
        self.assertNotIn("I can see you", view)
        self.assertNotIn("1SG 2SG see", view)
        self.assertNotIn("They went", view)

    def test_digest_depends_only_on_phi(self):
        units = parse_units(SAMPLE)
        changed_english = parse_units(SAMPLE.replace("(I see you.)", "(I notice you.)"))
        changed_phi = parse_units(SAMPLE.replace("mia thia nila.", "mia thia sano.", 1))
        self.assertEqual(phi_digest(units), phi_digest(changed_english))
        self.assertNotEqual(phi_digest(units), phi_digest(changed_phi))

    def test_source_view_can_feed_phi_only_phase(self):
        units = parse_units(SAMPLE)
        source_view = source_to_phi_view(Path("sample.md"), units)
        reparsed = parse_units(source_view)
        self.assertEqual(units, reparsed)
        phi_view = phi_to_english_view(reparsed)
        self.assertEqual(phi_to_english_view(units), phi_view)
        self.assertNotIn("I can see you", phi_view)
        self.assertEqual(phi_digest(units), phi_digest(reparsed))

    def test_unit_selector_is_stable_and_rejects_bad_ranges(self):
        self.assertEqual([1, 2, 3, 7, 9, 10], parse_unit_spec("1-3,7,9-10", 10))
        self.assertEqual([1, 2, 3], parse_unit_spec(None, 3))
        with self.assertRaisesRegex(ValueError, "outside"):
            parse_unit_spec("4", 3)
        with self.assertRaisesRegex(ValueError, "backwards"):
            parse_unit_spec("3-1", 3)

    def test_compact_bundle_supplies_only_relevant_language_material(self):
        units = parse_units(SAMPLE)
        assessments = {
            assessment.unit: assessment
            for assessment in (
                assess_unit_risk(1, units[0].phi, LEXICON, COMPOUNDS),
                assess_unit_risk(2, units[1].phi, LEXICON, COMPOUNDS),
            )
        }
        view = phi_to_english_view(
            units,
            lexicon=LEXICON,
            compounds=COMPOUNDS,
            assessments=assessments,
        )
        self.assertIn("Generated gloss scaffold", view)
        self.assertIn("1SG 2SG see.", view)
        self.assertIn("Compact description for nila", view)
        self.assertNotIn("Compact description for unused", view)
        self.assertIn("predicate=...; arguments=...", view)
        self.assertNotIn("I can see you", view)
        self.assertNotIn("sample.md", view)

    def test_gloss_scaffold_accepts_a_productive_name(self):
        self.assertEqual(
            "1SG NAME talumi see.",
            gloss_scaffold("mia ne talumi nila.", LEXICON),
        )

    def test_risk_assessment_marks_structural_sources_of_disagreement(self):
        phi = (
            "shia pha lo whu miona lothea nai pho to po ma sano. "
            "shia miona nela miona sola miona lothea."
        )
        flags = set(assess_unit_risk(4, phi, LEXICON, COMPOUNDS).flags)
        self.assertIn("complement-frame", flags)
        self.assertIn("relative-clause-attachment", flags)
        self.assertIn("particle-scope-stack", flags)
        self.assertIn("complex-coordination", flags)
        self.assertIn("pronoun-reference", flags)

    def test_audit_plan_is_deterministic_and_samples_only_below_threshold_units(self):
        units = [TranslationUnit(f"mia thia nila. {index}", ()) for index in range(1, 5)]
        assessments = [
            RiskAssessment(1, ()),
            RiskAssessment(2, ("relative-clause-attachment",)),
            RiskAssessment(3, ()),
            RiskAssessment(4, ()),
        ]
        first = audit_plan(units, assessments, 0.34)
        second = audit_plan(units, assessments, 0.34)
        self.assertEqual(first, second)
        selected, risk_units, sample_units = first
        self.assertEqual([2], risk_units)
        self.assertEqual(2, len(sample_units))
        self.assertNotIn(2, sample_units)
        self.assertEqual(sorted(set(risk_units + sample_units)), selected)

        changed_risk_unit = list(units)
        changed_risk_unit[1] = TranslationUnit("shia thia nila.", ())
        _, _, changed_samples = audit_plan(changed_risk_unit, assessments, 0.34)
        self.assertEqual(sample_units, changed_samples)

    def test_packet_directory_records_batches_hashes_risks_and_samples(self):
        units = parse_units(SAMPLE)
        assessments = [
            assess_unit_risk(index, unit.phi, LEXICON, COMPOUNDS)
            for index, unit in enumerate(units, 1)
        ]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "packets"
            manifest = write_packet_directory(
                output,
                units,
                [1, 2],
                LEXICON,
                COMPOUNDS,
                assessments,
                batch_size=1,
                audit_mode=True,
                audit_samples=[2],
                audit_sample_rate=0.5,
            )
            self.assertEqual(2, len(manifest["batches"]))
            self.assertEqual(phi_digest(units), manifest["full_phi_sha256"])
            self.assertEqual(
                [
                    {"unit": 1, "phi_sha256": unit_digest(units[0])},
                    {"unit": 2, "phi_sha256": unit_digest(units[1])},
                ],
                manifest["unit_hashes"],
            )
            stored = json.loads((output / "manifest.json").read_text())
            self.assertEqual(manifest, stored)
            self.assertEqual(0.5, manifest["independent_audit_policy"]["sample_rate"])
            self.assertEqual(2, manifest["independent_audit_policy"]["minimum_total_flags"])
            reference = (output / manifest["reference_file"]).read_text()
            self.assertIn("Compact description for nila", reference)
            packet = (output / manifest["batches"][0]["file"]).read_text()
            self.assertNotIn("I can see you", packet)
            self.assertIn("Unit 001", packet)
            self.assertIn(unit_digest(units[0]), packet)
            self.assertIn("not a finished exact gloss", packet)
            self.assertNotIn("Compact description for nila", packet)

    def test_packet_directory_rejects_an_unlisted_form_before_writing(self):
        units = [TranslationUnit("mia zaza nila.", ())]
        assessments = [assess_unit_risk(1, units[0].phi, LEXICON, COMPOUNDS)]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "packets"
            with self.assertRaisesRegex(ValueError, "unlicensed forms: zaza"):
                write_packet_directory(
                    output,
                    units,
                    [1],
                    LEXICON,
                    COMPOUNDS,
                    assessments,
                )
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
