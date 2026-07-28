#!/usr/bin/env python3
"""Regression tests for the independent Phi sentence parser."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from phi_sentence_validator import Lexicon, PhiParser
from validate_sentences import (
    ASSERTED_DOC_ROOTS,
    PROJECT_ROOT,
    iter_lexicon_examples,
    iter_markdown_examples,
)


class SentenceParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexicon = Lexicon.load()

    def setUp(self):
        self.parser = PhiParser(self.lexicon)

    def assertValid(self, text, *, fragments=False):
        result = self.parser.parse(text, allow_fragments=fragments)
        rendered = "\n".join(
            diagnostic.render(result.tokens) for diagnostic in result.diagnostics
        )
        self.assertTrue(result.ok, f"{text}\n{rendered}")
        self.assertIsNotNone(result.tree)
        return result

    def assertInvalid(self, text, code):
        result = self.parser.parse(text, allow_fragments=False)
        codes = {diagnostic.code for diagnostic in result.diagnostics}
        rendered = "\n".join(
            diagnostic.render(result.tokens) for diagnostic in result.diagnostics
        )
        self.assertIn(code, codes, f"{text}\n{rendered}")
        return result

    def test_basic_predicate_frames(self):
        for text in (
            "lopia thalo.",
            "phao nuora pilewa.",
            "womu thiku nai.",
            "thepalu thiku to nai.",
            "shia noalu ki kelu.",
            "shia serao reshi kelu.",
            "mia roe kiru wolea kati.",
            "mua womu therilu.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_slot_zero_and_discourse(self):
        for text in (
            "wa thia lumani lothea.",
            "no lumani naphe.",
            "su sila towe nai.",
            "pi wa thia po naphe.",
            "pi no ponu tapu.",
            "wa whekai thia ma sano.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_slot_one_order_and_manner(self):
        for text in (
            "mia to si ke po ma shelomu.",
            "lopia se ka nulae.",
            "shia to shena nela kiro haolu.",
            "nophi to se ko kawhera.",
            "mia to ko ma kelomi.",
            "pe sukaro ma nai.",
            "wonepa hiso to se ka kelu.",
            "pheralu ruela hiso ka kelu.",
            "melu mia siora to ka kelu.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_slot_two_nesting(self):
        for text in (
            "li ha lo melu shua.",
            "ha mo ko mioru peloru mua thepalu nai.",
            "lo ha ru thape.",
            "mia ru nuhe phaelo.",
            "ha likori lo nolika phirae nai.",
            "ne sa sulae shua.",
            "ne samira shua.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_numbers_quantifiers_and_classifiers(self):
        for text in (
            "wi himo piru shua.",
            "ta shao lipha shiro thuroa.",
            "wi rei wi lau wi phoi wi shao wi silero keru nai.",
            "shao philo teku nai.",
            "theli phemi ta themo noru howela.",
            "nu ta shao philo mua shemu nai.",
            "wia himo miona so shua.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_complement_frames(self):
        for text in (
            "siora tha ne sulae so shua tho shane.",
            "lopia pha pheralu so lepa pho ma sano.",
            "mia sha muila theula howela sho ro haolu.",
            "mia sha kia. thia nosa hina phaelo sho to thilou.",
            "mia tha shia pha pheralu lepa pho sano tho remo.",
            "mia sua to wepu sano.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_relative_clauses(self):
        for text in (
            "whu sulopa ro pilewa miona shua.",
            "mia whu thia to pilewa sulopa nuola.",
            "whu mia mua to thalo shelira mioru nai.",
            "whu ha nai ha nai.",
            "shia mua nupira whu shia mua shareo to ki sahu sheloi tiso themore ki themio.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_adverbial_frames(self):
        for text in (
            "lao pheralu lepa lo mia mua womu therilu.",
            "pheo melu shua mia sulopa pilewa.",
            "phoe melu shua mia sulopa pilewa.",
            "shai pheralu lepa lo mia thalo.",
            "lila mia shonela mia theo.",
            "whau ne kulo haolu lo mia shua.",
            "pheo wi philo melu so shua.",
            "thia lila wepu ralu nai.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_conditionals(self):
        for text in (
            "lu pheralu lepa. lo mia mua womu therilu.",
            "lu he mia pelori nai. mia wapi.",
            "lu thia mia naphe. mia thia so whaline.",
            "lu thia shelu shelomu. thia mia so naphe.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_coordination(self):
        for text in (
            "mia shea nela sila lothea.",
            "wa thia theo sola sheluo.",
            "mia to shua nela shia to wepu.",
            "thia mia po naphe sola mia miso po naphe.",
            "wi nela ta shao sholei. ta shao wi kelai.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_interjections_vocatives_and_fragments(self):
        for text in (
            "kia.",
            "henoi.",
            "kona ne sa sulae.",
            "ha philo.",
            "serao melothe.",
            "whu sulopa ro pilewa miona.",
        ):
            with self.subTest(text=text):
                self.assertValid(text, fragments=True)

    def test_surface_and_lexical_errors(self):
        self.assertInvalid("Mia thia nila.", "PHS001")
        self.assertInvalid("mia thia nila!", "PHS002")
        self.assertInvalid("mia thia zotu.", "PHS003")
        self.assertInvalid("ne shua.", "PHS070")

    def test_predicate_and_modifier_first_errors(self):
        self.assertInvalid("mia haolu to pa.", "PHS070")
        self.assertInvalid("pheralu ruela ka hiso.", "PHS070")
        self.assertInvalid("melu mia to ka siora.", "PHS070")
        self.assertInvalid("thia po mia naphe sola mia po miso naphe.", "PHS102")
        self.assertInvalid("shia ho womu nai.", "PHS102")
        self.assertInvalid("ha phialu po peloma nai.", "PHS103")
        self.assertInvalid("ha peshiro po ma welathi nai.", "PHS103")
        self.assertInvalid(
            "wi wetha lonai kolo nai. wi wetha waleru ma kolo nai.",
            "PHS103",
        )
        self.assertInvalid("pe ma sukaro nai.", "PHS103")
        self.assertInvalid("wonepa to se hiso ka kelu.", "PHS102")
        self.assertInvalid(
            "lu thia mia naphe. mia so thia whaline.",
            "PHS102",
        )
        self.assertInvalid(
            "lu thia shelu shelomu. thia so mia naphe.",
            "PHS102",
        )

    def test_slot_one_errors(self):
        self.assertInvalid("mia ma to nila.", "PHS100")
        self.assertInvalid("mia to so nila.", "PHS101")
        self.assertInvalid("mia ki si nila.", "PHS101")
        self.assertInvalid("mia ka se nulae.", "PHS101")

    def test_slot_zero_errors(self):
        self.assertInvalid("mia wa thia nila.", "PHS052")
        self.assertInvalid("pi su sila towe nai.", "PHS051")
        self.assertInvalid("pi lu pheralu lepa. lo mia therilu.", "PHS051")
        self.assertInvalid("he mia pelori nai.", "PHS030")
        self.assertInvalid("lu pheralu lepa.", "PHS031")
        self.assertInvalid("mia theo lila mia shonela.", "PHS061")

    def test_complement_errors(self):
        self.assertInvalid("mia tha shia wepu sano.", "PHS022")
        self.assertInvalid("mia tha shia wepu pho sano.", "PHS021")
        self.assertInvalid("mia pha shia hina rinu pho sano.", "PHS082")
        self.assertInvalid("mia sha kia sho remo.", "PHS081")

    def test_slot_two_and_quantity_errors(self):
        self.assertInvalid("lo ha melu shua.", "PHS111")
        self.assertInvalid("lo ha likori nolika phirae nai.", "PHS111")
        self.assertInvalid("ha ru la mioru peloru nai.", "PHS112")
        self.assertInvalid("lo wi melu shua.", "PHS115")
        self.assertInvalid("theli himo miona shua.", "PHS116")
        self.assertInvalid("nu mu philo mua shemu nai.", "PHS114")
        self.assertInvalid("mia nurako mua wepu.", "PHS121")
        self.assertInvalid("lila mia thoru sulopa wo sukaro nai.", "PHS060")

    def test_every_structured_lexicon_example_parses(self):
        failures = []
        checked = 0
        for source in iter_lexicon_examples(PROJECT_ROOT):
            checked += 1
            result = self.parser.parse(source.text, allow_fragments=False)
            if not result.ok:
                failures.extend(
                    f"{source.label}: {diagnostic.render(result.tokens)}"
                    for diagnostic in result.diagnostics
                )
        self.assertGreater(checked, 1300)
        self.assertEqual([], failures)

    def test_every_asserted_teaching_example_parses(self):
        failures = []
        checked = 0
        for source in iter_markdown_examples(
            PROJECT_ROOT, self.lexicon, ASSERTED_DOC_ROOTS
        ):
            checked += 1
            result = self.parser.parse(
                source.text, allow_fragments=source.allow_fragments
            )
            if not result.ok:
                failures.extend(
                    f"{source.label}: {diagnostic.render(result.tokens)}"
                    for diagnostic in result.diagnostics
                )
        self.assertGreater(checked, 1500)
        self.assertEqual([], failures)

    def test_docs_only_respects_selected_paths(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(PROJECT_ROOT / "scripts" / "validate_sentences.py"),
                "--docs-only",
                "--paths",
                "manual",
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("0 error(s)", completed.stdout)


if __name__ == "__main__":
    unittest.main()
