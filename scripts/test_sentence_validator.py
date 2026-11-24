#!/usr/bin/env python3
"""Regression tests for the independent Phi sentence parser."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
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
            "wa mia pha sua to wepu pho sano.",
            "thia hina nila.",
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
            "mia tha mia sha wa ha nai sho haolu tho to thueli.",
            "mia pha sua to wepu pho sano.",
            "tupiwa pha keli mue kua whano pho to laeno nila.",
            "pha lo mia thela kau ha wireo kamo pho we shia reo nai.",
            "mia tha shia pha sua to wepu pho sano tho remo.",
            "mia pha shia pha sua to wepu pho sano pho phaelo.",
            "mia sha wa shia to wepu sho to haolu.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_possibility_frame(self):
        for text in (
            "tha shia so ma shua tho po nai.",
            "tha pheralu ma lepa tho po nai.",
            "tha ha peshiro welathi ma nai tho po nai.",
            "tha shia so ma shua tho ke po nai.",
            "wa tha shia so ma shua tho po nai.",
            "mia tha tha shia so ma shua tho po nai tho remo.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)
        self.assertInvalid("shia so ma po shua.", "PHS100")
        self.assertInvalid("pheralu ma po lepa.", "PHS100")

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
            "whekai lao pheralu lepa lo mia mua womu therilu.",
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
            "mia thia nila thona lao pheralu lepa lo mia mua womu therilu.",
            "ne kulo nela ra mioru miona to pa theisa hola.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_interjections_vocatives_and_fragments(self):
        for text in (
            "kia.",
            "henoi.",
            "whekai teo.",
            "kona ne sa sulae.",
            "ha philo.",
            "ha wisola lokue.",
            "ne kulo nela mia.",
            "serao melothe.",
            "whu thia kaeli.",
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
        self.assertInvalid("wa thia hina nila.", "PHS055")

    def test_coordinator_boundaries(self):
        result = self.assertInvalid("thona mia thia nila.", "PHS054")
        self.assertEqual(["PHS054"], [item.code for item in result.diagnostics])
        result = self.assertInvalid(
            "thona lao pheralu lepa lo mia mua womu therilu.",
            "PHS054",
        )
        self.assertEqual(["PHS054"], [item.code for item in result.diagnostics])
        self.assertInvalid("mia thia nila thona.", "PHS054")

    def test_complement_errors(self):
        self.assertInvalid("mia tha shia wepu sano.", "PHS022")
        self.assertInvalid("mia tha shia wepu pho sano.", "PHS021")
        self.assertValid("mia pha shia hina rinu pho sano.")
        self.assertInvalid("mia pha wa shia rinu pho sano.", "PHS082")
        self.assertInvalid("mia tha wa shia to wepu tho sano.", "PHS083")
        self.assertInvalid("mia tha sua to shua tho sano.", "PHS084")
        result = self.assertInvalid("mia sua to shua sano.", "PHS085")
        self.assertEqual(["PHS085"], [item.code for item in result.diagnostics])
        self.assertValid("mia sua shua sano.")
        self.assertInvalid("mia sha kia sho remo.", "PHS081")

    def test_slot_two_and_quantity_errors(self):
        self.assertInvalid("lo ha melu shua.", "PHS111")
        self.assertInvalid("lo ha likori nolika phirae nai.", "PHS111")
        self.assertInvalid("ha ru la mioru peloru nai.", "PHS112")
        self.assertInvalid("mia lo lo womu nila.", "PHS115")
        self.assertInvalid("lo wi melu shua.", "PHS115")
        self.assertInvalid("theli himo miona shua.", "PHS116")
        self.assertInvalid("nu mu philo mua shemu nai.", "PHS114")
        self.assertInvalid("mia nurako mua wepu.", "PHS121")
        self.assertInvalid("lila mia thoru sulopa wo sukaro nai.", "PHS060")

    def test_interrogative_position(self):
        for text in (
            "shia misa to wepu.",
            "misa ma sano.",
            "ha wisola lokue misa ru waora nai.",
            "thia misa tha mokela miona mua ruela po nai tho remo.",
            "mia misa phoe ha shemu thia ma thilou.",
            "whekai misa mia ma sano.",
            "mia ka mo nila.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)
        self.assertInvalid(
            "thia tha mokela miona mua ruela po nai tho misa remo.",
            "PHS130",
        )
        self.assertInvalid("thia mua thepalu misa lopia nila.", "PHS130")
        self.assertInvalid("shia to misa wepu.", "PHS130")
        self.assertInvalid("mia mo ka nila.", "PHS113")

    def test_one_gap_per_content_question(self):
        self.assertInvalid("mia sua hina nila.", "PHS056")
        self.assertInvalid("mia pha sua hina to nila pho sano.", "PHS056")
        self.assertValid("sua shua nela shia hina phelu.")
        self.assertValid("mia hina pha shia sua to nila pho remo.")

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

    def test_markdown_detector_includes_lowercase_gloss_blocks(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "sample.md").write_text(
                "```\n"
                "sua hina theama kanu.\n"
                "who what care choose.\n"
                "(Who chooses which care?)\n"
                "```\n",
                encoding="utf-8",
            )
            sources = list(
                iter_markdown_examples(root, self.lexicon, ["sample.md"])
            )

        self.assertEqual(
            ["sua hina theama kanu."],
            [source.text for source in sources],
        )
        self.assertInvalid(sources[0].text, "PHS056")

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

    def assertAdvisories(self, text, expected):
        result = self.assertValid(text)
        found = [
            (advisory.code, result.tokens[advisory.token_index].text)
            for advisory in result.advisories
        ]
        self.assertEqual(expected, found, text)

    def test_manner_advisory(self):
        for text, word in (
            ("shia pakiro to whano.", "pakiro"),
            ("shia taleri ro phoa.", "taleri"),
            ("howeli mo kema to whesu.", "kema"),
            ("lo miona ha ru kuewa so nila.", "kuewa"),
            ("shia shena nela thaemu to haolu.", "thaemu"),
            ("mia tha shia pakiro to whano tho remo.", "pakiro"),
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [("PHL001", word)])

    def test_manner_advisory_stays_quiet(self):
        for text in (
            "shia to pakiro whano.",
            "shia ro taleri phoa.",
            "shia pakiro whano.",
            "shia mioru to nai.",
            "shia serao to kelu.",
            "mia mua waora to maeli manolu.",
            "mia lo newu po pilu.",
            "mia wiloru nela kuewa to phaelo.",
            "ne sulae so shua.",
            "mia shea to phaelo.",
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [])

    def test_adjunct_order_advisory(self):
        for text, word in (
            ("mia soeli nia palu thinu.", "soeli"),
            ("mia ruela mua muila nila.", "ruela"),
            ("lo mia shelu wei melu to loa.", "shelu"),
            ("shia miso mue lona lokue to ka roke.", "miso"),
            ("mia shelu pheo wi philo so theo.", "shelu"),
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [("PHL002", word)])

    def test_adjunct_order_advisory_stays_quiet(self):
        for text in (
            "mia nia palu soeli thinu.",
            "mia mua muila ruela nila.",
            "mia kau silawo wepu.",
            "shia mue lona lokue miso to ka roke.",
            "mia nela thia kau silawo wepu.",
            "thia misa mua thepalu lopia nila.",
            "melu shelu wei lopia loa.",
            "mia melu mua womu nai.",
            "mia pheo wi philo so shua.",
            "mia nosa kau silawo wepu.",
            "lo mia wireo philo kau moriwhe kerime so wepu.",
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [])

    def test_adjunct_order_advisory_skips_gapped_relatives(self):
        self.assertAdvisories("whu mia shelu wei loa melu shua.", [])

    def test_quote_period_advisory(self):
        self.assertAdvisories(
            "shia sha kona phewani. teku wishe to nai. sho to haolu.",
            [("PHL003", "nai")],
        )
        self.assertAdvisories("ne kulo sha lia. mia so shua sho to haolu.", [])
        self.assertAdvisories("sha lu thia shewo nai. thia rohemi ma sone sho to haolu.", [])

    def test_fronted_adjunct_advisory(self):
        for text, word in (
            ("pheo teku shemu lo miona lo mia lo manuwe to pilu.", "pheo"),
            ("mua nu ta shemu mia meraho to kelu.", "mua"),
            ("mua ha lokue ne kulo to whano.", "mua"),
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [("PHL004", word)])
        for text in (
            "lo miona pheo teku shemu lo mia lo manuwe to pilu.",
            "mia mua nu ta shemu meraho to kelu.",
            "mua womu therilu.",
            "no wei mia shua.",
            "pheo wi philo so shua.",
            "pheo teku shemu kau womu to wepu.",
            "pheo melu to kamo lo mia to haolu.",
        ):
            with self.subTest(text=text):
                self.assertAdvisories(text, [])

    def test_reflexive_and_reciprocal_beyond_the_object(self):
        for text in (
            "shia miso womu to nila.",
            "shia neo miso to nila.",
            "lo miona wiso lo remo sheluo.",
            "lo miona lue wiso to shonela.",
            "thiku ne tupiwa to nulae.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)

    def test_advisories_need_a_clean_parse(self):
        result = self.parser.parse("shia pakiro to whano to.", allow_fragments=False)
        self.assertFalse(result.ok)
        self.assertEqual([], result.advisories)

    def test_lint_flag_reports_without_failing(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(PROJECT_ROOT / "scripts" / "validate_sentences.py"),
                "--sentence",
                "shia pakiro to whano.",
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("REVIEW", completed.stdout)
        self.assertIn("PHL001", completed.stdout)
        self.assertIn("Valid Phi utterance.", completed.stdout)

    def test_temporal_relators_take_a_clause_or_a_time_phrase(self):
        for text in (
            "mia pheo wi philo so shua.",
            "melu phoe wi philo to kamo.",
            "lo miona pheo teku shemu shua.",
            "shia pheo laeno thimu to turema.",
            "repha phoe ra thimu mua ra lokue to whano.",
            "mia phoe ha shemu thia to ma thilou.",
            "pheo shia ha to haolu kohura mosha to nai.",
            "pheo ha shero wepu shia to nulae.",
            "whekai phoe pai wi phoi wi shao ta torua punoki karami to pilu.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)
        for text in (
            "pheo thena kohura mosha to nai.",
            "pheo ha sileta to pa keru loa.",
            "pheo ha mia soli thimu to maeli manolu.",
            "phoe ha mia mawha thimu ru rashowe to nai.",
            "shia pheo hasumi nurome to ro wile.",
            "mia pheo shia to wepu.",
            "mia pheo repha la wuero lokue to nila.",
        ):
            with self.subTest(text=text):
                self.assertInvalid(text, "PHS062")

    def test_also_and_only_stand_outside_the_slot_one_block(self):
        for text in (
            "shia we to pa nulae.",
            "ne kalora li to seniku.",
            "mia we shua.",
            "shia to ru noeli haolu.",
        ):
            with self.subTest(text=text):
                self.assertValid(text)
        for text in ("shia to we nulae.", "ne kalora to li seniku."):
            with self.subTest(text=text):
                self.assertInvalid(text, "PHS106")

    def test_sentence_cli_fragment_mode(self):
        command = [
            sys.executable,
            str(PROJECT_ROOT / "scripts" / "validate_sentences.py"),
            "--sentence",
            "henoi.",
        ]
        complete = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, complete.returncode, complete.stdout + complete.stderr)
        self.assertIn("PHS070", complete.stdout)

        fragment = subprocess.run(
            [*command, "--fragment"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, fragment.returncode, fragment.stdout + fragment.stderr)
        self.assertIn("Valid Phi utterance.", fragment.stdout)


if __name__ == "__main__":
    unittest.main()
