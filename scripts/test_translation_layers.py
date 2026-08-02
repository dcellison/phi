import unittest
from pathlib import Path

from translation_layers import (
    parse_units,
    phi_digest,
    phi_to_english_view,
    source_to_phi_view,
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


if __name__ == "__main__":
    unittest.main()
