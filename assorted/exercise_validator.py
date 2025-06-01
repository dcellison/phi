#!/usr/bin/env python3
"""
Comprehensive Phi Sentence Validator Exercise Framework

Tests the validator with a wide range of sentences from simple to complex,
organized by linguistic features and complexity levels.
"""

import sys
from pathlib import Path
from typing import List, Dict, Tuple
import json

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Use direct import to avoid hanging
from phi_validation.core import PhiSentenceValidator

class SentenceExerciser:
    """Exercise the Phi sentence validator with comprehensive test cases."""
    
    def __init__(self):
        """Initialize the exerciser with validator and test sentences."""
        self.validator = PhiSentenceValidator()
        self.test_categories = self._build_test_categories()
        self.results = {}
    
    def _build_test_categories(self) -> Dict[str, List[Tuple[str, str, bool]]]:
        """Build comprehensive test categories with expected results."""
        return {
            # Basic sentence structures with varied vocabulary
            "basic_sentences": [
                ("mia ta thilu.", "I present be", True),
                ("thi ta whemo.", "you present think", True),
                ("sha ta whuni.", "they present have", True),
                ("he thephoa ta phoni.", "human person present live", True),
                ("pi whithea ta whawi.", "animate dove present fly", True),
                ("ne lowhai ta riphe phera.", "inanimate answer present important is", True),
                ("mia li whera.", "I past learn", True),
                ("thi su whesa.", "you future create", True),
                ("sha li phoni.", "they past live", True),
                ("he thephoa su whemo.", "human person future think", True),
                ("pi mathai ta phewa.", "animate cat present feel", True),
                ("ne whethea ta misha phera.", "inanimate book present beautiful is", True),
                ("mia su thilu.", "I future be", True),
                ("thi li whuni.", "you past have", True),
                ("he nowhea ta whera.", "human teacher present learn", True),
                ("pi lophea ta phoni.", "animate bird present live", True),
            ],
            
            # Rich vocabulary showcase
            "vocabulary_showcase": [
                ("he thephoa ta whemo.", "human person present think", True),
                ("pi mathai ta whuwe.", "animate cat present sleep", True),
                ("ne whethea misha ta phera.", "inanimate book beautiful present is", True),
                ("mia na ne raoshea ta whona.", "I object inanimate sun present look", True),
                ("thi na ne riwhea ta shusa.", "you object inanimate wind present hear", True),
                ("sha na ne waphe ta phewa.", "they object inanimate warm present feel", True),
                ("he nowhea ta sheme.", "human teacher present teach", True),
                ("pi saphoa ta whale.", "animate snake present flow", True),
                ("he luphea na ne nuthea ta whesa.", "human artist object inanimate sculpture present create", True),
                ("pi whithea na ne roshai ta whona.", "animate dove object inanimate flower present look", True),
                ("ne mothao ta tophe phera.", "inanimate cloud present large is", True),
                ("he hathai na ne thaphao ta whari.", "human musician object inanimate song present sing", True),
                ("pi mathai na ne liwhai ta shire.", "animate cat object inanimate drink present want", True),
                ("ne shuwhia ta miwhi phera.", "inanimate sand present fresh is", True),
                ("he thephoa na ne tuphai ta shiho.", "human person object inanimate cup present buy", True),
                ("pi lophea na ne loshea ta sharo.", "animate bird object inanimate ocean present go", True),
            ],
            
            # Natural world and environment
            "natural_world": [
                ("ne riwhea ta whuru.", "inanimate wind present blow", True),
                ("pi lophea ta whari.", "animate bird present sing", True),
                ("ne raoshea ta shine.", "inanimate sun present seem", True),
                ("ne lashea ta whale.", "inanimate rain present flow", True),
                ("pi whithea na ne loshea ta sharo.", "animate dove object inanimate ocean present go", True),
                ("ne liphai ta pholi.", "inanimate tree present grow", True),
                ("pi mathai na pi whithea ta shosa.", "animate cat object animate dove present watch", True),
                ("ne shuwhia ta miwhi phera.", "inanimate sand present fresh is", True),
                ("ne mothao ta whuru.", "inanimate cloud present blow", True),
                ("pi saphoa na ne loshea ta whale.", "animate snake object inanimate ocean present flow", True),
                ("ne roshai ta hesha phera.", "inanimate flower present delicious is", True),
                ("pi lophea na ne liphai ta phite.", "animate bird object inanimate tree present stay", True),
                ("ne raoshea ta waphe phera.", "inanimate sun present warm is", True),
                ("pi mathai na ne shuwhia ta shosa.", "animate cat object inanimate sand present watch", True),
                ("ne lashea na ne liphai ta phewa.", "inanimate rain object inanimate tree present feel", True),
                ("pi whithea ta tophe phera.", "animate dove present large is", True),
            ],
            
            # Human activities and relationships
            "human_activities": [
                ("he thephoa na ne hiwhea ta shuni.", "human person object inanimate house present build", True),
                ("he nowhea na he phiphea ta sheme.", "human teacher object human child present teach", True),
                ("he luthea na ne noshea ta shuwo.", "human friend object inanimate food present offer", True),
                ("he hishui na he phiphea ta phepa.", "human parent object human child present heal", True),
                ("he thephoa na ne whethea ta shiho.", "human person object inanimate book present buy", True),
                ("he hathai na ne thaphao ta whari.", "human musician object inanimate song present sing", True),
                ("he luphea na ne nuthea ta whesa.", "human artist object inanimate sculpture present create", True),
                ("he thephoa na he luthea ta whoso.", "human person object human friend present marry", True),
                ("he nowhea na ne nushui ta sheme.", "human teacher object inanimate language present teach", True),
                ("he thephoa na ne luthia ta shele.", "human person object inanimate letter present send", True),
                ("he phiphea na ne mophui ta whuwa.", "human child object inanimate ball present throw", True),
                ("he luthea na he thephoa ta whoso.", "human friend object human person present marry", True),
                ("he thephoa na ne phuphai ta whuni.", "human person object inanimate medicine present have", True),
                ("he hathai na ne nushui ta whera.", "human musician object inanimate language present learn", True),
                ("he luphea na ne whethea ta whupi.", "human artist object inanimate book present read", True),
                ("he hishui na ne noshea ta theso.", "human parent object inanimate food present cook", True),
            ],
            
            # Complex particle sequences
            "complex_particles": [
                ("so hi he thephoa ta whemo.", "politeness evidence human person present think", True),
                ("ro ma ne lowhai ta riphe phera.", "inference emphasis inanimate answer present important is", True),
                ("so nu sha na ne lophui li whesa.", "politeness hearsay they object inanimate art past create", True),
                ("so hi ma mia na ne mipho lowhai ta whona.", "politeness evidence emphasis I object inanimate blue answer present look", True),
                ("wa so he thephoa na ne phuphai ta whuni.", "question politeness human person object inanimate medicine present have", True),
                ("mu ma thi na ne nushui li whera.", "memory emphasis you object inanimate language past learn", True),
                ("so ti ma he nowhea ta sheme.", "politeness reported emphasis human teacher present teach", True),
                ("pe ma sha na ne lophui su whesa.", "presumption emphasis they object inanimate art future create", True),
                ("so hi ro ma mia ta whemo.", "politeness evidence inference emphasis I present think", True),
                ("so nu he thephoa li phoni.", "politeness hearsay human person past live", True),
                ("mu ma he phiphea ta whera.", "memory emphasis human child present learn", True),
                ("so ti mia na ne lowhai ta whesa.", "politeness reported I object inanimate answer present create", True),
            ],
            
            # Word order variations with proper particle ordering
            "word_order_varied": [
                ("mia na ne whethea ta whupi.", "I object inanimate book present read-silently", True),
                ("he thephoa na ne noshea ta theso.", "human person object inanimate food present cook", True),
                ("thi na ne phuphai ta whuni.", "you object inanimate medicine present have", True),
                ("sha na ne luthia ta shele.", "they object inanimate letter present send", True),
                ("he phiphea na ne mophui ta whuwa.", "human child object inanimate ball present throw", True),
                ("pi mathai na ne liwhai ta shire.", "animate cat object inanimate drink present want", True),
                ("he thephoa na ne tuphai ta shiho.", "human person object inanimate cup present buy", True),
                ("sha na ne nuthea ta whesa.", "they object inanimate sculpture present create", True),
                ("mia na ne thaphao ta whari.", "I object inanimate song present sing", True),
                ("thi na ne hiwhea ta shuni.", "you object inanimate house present build", True),
                ("he nowhea na ne nushui ta sheme.", "human teacher object inanimate language present teach", True),
                ("pi lophea na ne roshai ta whona.", "animate bird object inanimate flower present look", True),
                ("he thephoa na ne lathia ta shero.", "human person object inanimate axe present carry", True),
                ("sha na ne mothao ta shosa.", "they object inanimate cloud present watch", True),
            ],
            
            # Temporal and aspectual constructions
            "temporal_constructions": [
                ("mia na ne nushui li we whera.", "I object inanimate language past perfective learn", True),
                ("thi na ne lophui ta la whesa.", "you object inanimate art present progressive create", True),
                ("sha na ne phuphai su ni whuni.", "they object inanimate medicine future perfect have", True),
                ("he thephoa na ne hiwhea li pu shuni.", "human person object inanimate house past cessative build", True),
                ("pi lophea ta ri whari.", "animate bird present imperfective sing", True),
                ("ne raoshea su po shine.", "inanimate sun future inchoative seem", True),
                ("he nowhea ta wi sheme.", "human teacher present iterative teach", True),
                ("mia na ne raoshea li wu whona.", "I object inanimate sun past experiential look", True),
                ("thi na ne whethea su we whupi.", "you object inanimate book future perfective read", True),
                ("he thephoa ta la phoni.", "human person present progressive live", True),
                ("sha na ne noshea li pu theso.", "they object inanimate food past cessative cook", True),
                ("pi mathai su po whuwe.", "animate cat future inchoative sleep", True),
                ("mia ta ri whemo.", "I present imperfective think", True),
                ("he nowhea na ne nushui li wu sheme.", "human teacher object inanimate language past experiential teach", True),
                ("thi su ni thilu.", "you future perfect be", True),
                ("pi lophea li we whari.", "animate bird past perfective sing", True),
            ],
            
            # Modal constructions with logical contexts
            "modal_constructions": [
                ("he phiphea ru whera.", "human child must learn", True),
                ("thi na ne lowhai to whesa.", "you object inanimate answer imperative create", True),
                ("sha na ne phuphai we te whuni.", "they object inanimate medicine want to have", True),
                ("he thephoa ru phepa.", "human person must heal", True),
                ("wetu ne lashea ta whale thi su phite.", "if inanimate rain present flow you future stay", True),
                ("he nowhea na he phiphea ru sheme.", "human teacher object human child must teach", True),
                ("mia na ne noshea ru whuni.", "I object inanimate food must have", True),
                ("thi ru whemo.", "you must think", True),
                ("he thephoa na ne whethea we te whupi.", "human person object inanimate book want to read", True),
                ("sha to phoni.", "they imperative live", True),
                ("pi mathai ru whuwe.", "animate cat must sleep", True),
                ("mia na ne hiwhea we te shuni.", "I object inanimate house want to build", True),
                ("he nowhea ru sheme.", "human teacher must teach", True),
                ("thi na ne lophui to whesa.", "you object inanimate art imperative create", True),
            ],
            
            # Evidentiality with appropriate contexts
            "evidentiality_contexts": [
                ("hi ne riwhea ta whuru.", "direct-evidence inanimate wind present blow", True),
                ("ro he thephoa ta phoni.", "inference human person present live", True),
                ("nu he thephoa na ne lophui li whesa.", "hearsay human person object inanimate art past create", True),
                ("ti he nowhea li shuso mia ta whera.", "reported human teacher past say I present learn", True),
                ("mu mia na ne raoshea li whona.", "memory I object inanimate sun past look", True),
                ("pe ne lashea su whale.", "presumption inanimate rain future flow", True),
                ("hi ro ne lowhai ta riphe.", "direct inference inanimate answer present important", False),  # conflict
                ("nu he thephoa ta whemo.", "hearsay human person present think", True),
                ("ti mia li shuso thi ta whera.", "reported I past say you present learn", True),
                ("mu he phiphea li whera.", "memory human child past learn", True),
                ("pe pi mathai su whuwe.", "presumption animate cat future sleep", True),
                ("ro ne raoshea ta waphe phera.", "inference inanimate sun present warm is", True),
                ("hi mia ta whemo.", "direct-evidence I present think", True),
                ("nu sha na ne noshea li theso.", "hearsay they object inanimate food past cook", True),
            ],
            
            # Emphasis with varied targets
            "emphasis_constructions": [
                ("ma mia ta whemo.", "emphasis I present think", True),
                ("he thephoa ma ta phoni.", "human person emphasis present live", True),
                ("mia na ne lophui ta ma whesa.", "I object inanimate art present emphasis create", True),
                ("ma he thephoa na ne phuphai ta whuni.", "emphasis human person object inanimate medicine present have", True),
                ("ma mipho lowhai ta riphe phera.", "emphasis blue answer present important is", True),
                ("ma ma mia ta whemo.", "double emphasis I present think", False),  # double emphasis
                ("ma.", "emphasis alone", False),  # no target
                ("ma thi ta whera.", "emphasis you present learn", True),
                ("sha na ne noshea ta ma theso.", "they object inanimate food present emphasis cook", True),
                ("ma ne raoshea ta shine.", "emphasis inanimate sun present seem", True),
                ("he nowhea ma na ne nushui ta sheme.", "human teacher emphasis object inanimate language present teach", True),
                ("ma pi mathai ta whuwe.", "emphasis animate cat present sleep", True),
                ("mia ta ma thilu.", "I present emphasis be", True),
                ("ma wetu mia ta whemo.", "emphasis if I present think", False)  # emphasis on conjunction
            ],
            
            # Politeness in appropriate contexts
            "politeness_contexts": [
                ("so mia ta thilu.", "politeness I present be", True),
                ("so thi na ne lowhai to whesa.", "politeness you object inanimate answer imperative create", True),
                ("so ru whera.", "politeness must learn", True),
                ("so hi he thephoa ta phoni.", "politeness evidence human person present live", True),
                ("wa so he thephoa na ne phuphai ta whuni.", "question politeness human person object inanimate medicine present have", True),
                ("so hi mia ta whemo.", "politeness evidence I present think", True),  # now valid with flexible ordering
                ("so he nowhea ta sheme.", "politeness human teacher present teach", True),
                ("so thi ru whera.", "politeness you must learn", True),
                ("so mia na ne whethea ta whupi.", "politeness I object inanimate book present read", True),
                ("so sha ta phoni.", "politeness they present live", True),
                ("so he thephoa na ne noshea ta theso.", "politeness human person object inanimate food present cook", True),
                ("so so mia ta whemo.", "double politeness I present think", False),  # double politeness
            ],
            
            # Discourse structures with logical flow
            "discourse_structures": [
                ("ha mia ta whemo.", "topic I present think", True),
                ("mia ta whera mi thi ta sheme.", "I present learn contrast you present teach", True),
                ("ha he thephoa ta phoni.", "topic human person present live", True),
                ("ha ne lowhai ta riphe phera mi sha ta miphe phera.", "topic inanimate answer present important is contrast they present empty are", True),
                ("mi mia ta whemo.", "contrast I present think", False),  # contrast without context
                ("ha mi mia ta whemo.", "topic contrast I present think", True),
                ("ha thi ta whera.", "topic you present learn", True),
                ("he thephoa ta phoni mi sha ta whemo.", "human person present live contrast they present think", True),
                ("ha ne raoshea ta shine.", "topic inanimate sun present seem", True),
                ("mia ta thilu mi thi ta whuni.", "I present be contrast you present have", True),
                ("ha pi mathai ta whuwe.", "topic animate cat present sleep", True),
                ("ha ha mia ta whemo.", "topic topic I present think", False),  # double topic
            ],
            
            # Interrogative structures with logical questions
            "interrogative_structures": [
                ("wa he thephoa ta phoni.", "question human person present live", True),
                ("hamite mia ta whera.", "how I present learn", True),
                ("wamine he thephoa na ne phuphai ta whuni.", "why human person object inanimate medicine present have", True),
                ("timane ne lashea ta whale.", "when inanimate rain present flow", True),
                ("wulime he nowhea ta phoni.", "where human teacher present live", True),
                ("wa hamite mia ta whera.", "question how I present learn", False),  # wa + wh conflict
                ("wa he thephoa ru whera.", "question human person must learn", True),  # rhetorical
                ("wa thi ta whemo.", "question you present think", True),
                ("hamite sha ta whesa.", "how they present create", True),
                ("wamine pi mathai ta whuwe.", "why animate cat present sleep", True),
                ("timane he thephoa ta phoni.", "when human person present live", True),
                ("wulime ne raoshea ta shine.", "where inanimate sun present seem", True),
                ("wa wa mia ta whemo.", "question question I present think", False),  # double question
                ("hamite hamite thi ta whera.", "how how you present learn", False),  # double how
            ],
            
            # Narrative sequences with logical temporal relationships
            "narrative_sequences": [
                ("mia li whera matu thi li sheme.", "I past learn after you past teach", True),
                ("he thephoa su whesa pimo thi ta whuni.", "human person future create before you present have", True),
                ("wetu ne lashea ta whale thi su phite.", "if inanimate rain present flow you future stay", True),
                ("he thephoa lu ta whemo riphe phera.", "person who present think important is", True),
                ("mia li whera pimo thi ta sheme.", "I past learn before you present teach", True),  # learning before teaching is valid
                ("he thephoa su whesa matu thi li whuni.", "human person future create after you past have", False),  # temporal logic error
                ("thi li sheme pimo mia ta whera.", "you past teach before I present learn", True),
                ("he nowhea ta sheme wane pi lophea ta whari.", "human teacher present teach when animate bird present sing", True),
                ("mia su whesa matu ne raoshea ta shine.", "I future create after inanimate sun present seem", True),
                ("sha li phoni pimo he thephoa ta whemo.", "they past live before human person present think", True),
                ("wetu thi ta whera mia su sheme.", "if you present learn I future teach", True),
                ("he thephoa li whesa matu mia su whera.", "human person past create after I future learn", False),  # temporal logic error
            ],
            
            # Complex multi-feature sentences
            "complex_sentences": [
                ("so hi ma he thephoa ta we whera.", "politeness evidence emphasis human person present perfective learn", True),
                ("wa so ma mia na ne lophui li we whesa.", "question politeness emphasis I object inanimate art past perfective create", True),
                ("so nu ha he nowhea na ne nushui ta sheme.", "politeness hearsay topic human teacher object inanimate language present teach", True),
                ("ro ma mia na ne lathia ta shero.", "inference emphasis I object inanimate axe present carry", True),
                ("wa so hi ma he thephoa ta ru whera.", "question politeness evidence emphasis human person present must learn", True),
                ("so ti ma thi na ne whethea li we whupi.", "politeness reported emphasis you object inanimate book past perfective read", True),
                ("so mu ha he phiphea ta la whera.", "politeness memory topic human child present progressive learn", True),
                ("so pe ma sha na ne noshea su ni theso.", "politeness presumption emphasis they object inanimate food future perfect cook", True),
                ("so hi ma he nowhea ta ri sheme.", "politeness evidence emphasis human teacher present imperfective teach", True),
                ("so ro ma mia ta we thilu.", "politeness inference emphasis I present perfective be", True),
            ],
            
            # Semantic role validation
            "semantic_roles": [
                ("he thephoa ta whemo.", "human person present think", True),
                ("pi mathai ta whuwe.", "animate cat present sleep", True),
                ("ne lowhai ta riphe phera.", "inanimate answer present important is", True),
                ("he thephoa ne whethea na ta whesa.", "human person inanimate book object present create", True),
                ("pi lophea ne liwhai na ta shire.", "animate bird inanimate drink object present want", True),
                ("ne lowhai he thephoa na ta whemo.", "inanimate answer human person object present think", False),  # animacy mismatch
                ("pi mathai ta shuni.", "animate cat present build", False),  # verb requires human subject
                ("he nowhea ta sheme.", "human teacher present teach", True),
                ("pi whithea ta whawi.", "animate dove present fly", True),
                ("ne raoshea ta shine.", "inanimate sun present seem", True),
                ("he thephoa pi mathai na ta shosa.", "human person animate cat object present watch", True),
                ("pi lophea he thephoa na ta shosa.", "animate bird human person object present watch", True),
                ("ne whethea ta whawi.", "inanimate book present fly", False),  # semantic mismatch
                ("pi mathai ta sheme.", "animate cat present teach", True),  # animals can be taught
            ],
            
            # Error cases for validation
            "error_cases": [
                ("invalidword ta whemo.", "unknown word", False),
                ("mia ta ta whemo.", "double tense", False),
                ("mia whemo ta thilu.", "verb not at end", False),
                ("ta whemo mia.", "wrong word order", False),
                ("mia li su whemo.", "conflicting tenses", False),
                ("hi nu mia ta whemo.", "conflicting evidentiality", False),
                ("ma wa mia ta whemo.", "emphasis on question particle", False),
                ("ma hi so mia ta whemo.", "wrong particle order", False),
                ("mia mia mia ta whemo.", "triple pronoun", False),
                ("he he he thephoa ta whemo.", "triple animacy", False),
                ("ta ta ta whemo.", "triple tense", False),
                ("na na mia ta whemo.", "double object marker", False),
                ("si si mia ta whemo.", "double subject marker", False),
                ("te te whemo.", "double verb marker", False),
                ("unknownword1 unknownword2 ta whemo.", "multiple unknown words", False),
                ("", "completely empty", False),
            ],
            
            # Edge cases and boundary conditions
            "edge_cases": [
                ("", "empty sentence", False),
                ("whemo.", "single verb (imperative)", True),
                ("ta", "single particle", False),
                ("mia mia ta whemo.", "repeated pronoun", True),  # might be valid for emphasis
                ("he he thephoa ta whemo.", "repeated animacy", False),
                ("ma ma ma mia ta whemo.", "triple emphasis", False),
                ("so so mia ta whemo.", "double politeness", False),
                ("ne lowhai.", "noun phrase only", False),  # incomplete sentence
                ("mia.", "single pronoun", False),
                ("he thephoa.", "incomplete noun phrase", False),
                ("na ne whethea.", "object without verb", False),
                ("li whera.", "tense and verb only", False),
                ("ma mia.", "emphasis without verb", False),
                ("so.", "politeness alone", False),
                ("wa.", "question alone", False),
                ("mia ta.", "subject tense no verb", False),
            ],
            
            # Colors and descriptions
            "descriptive_language": [
                ("ne mipho lowhai ta misha phera.", "inanimate blue answer present beautiful is", True),
                ("ne hashe liphai ta tophe phera.", "inanimate green tree present large is", True),
                ("he thephoa ne laphe roshai na ta whona.", "human person inanimate red flower object present look", True),
                ("ne sathia mothao ta shine.", "inanimate white cloud present seem", True),
                ("pi mathai ne waphe na ta phewa.", "animate cat inanimate warm object present feel", True),
                ("ne tupha whethea ta hesha.", "inanimate purple book present delicious", False),  # semantic mismatch
                ("ne laphe raoshea ta waphe phera.", "inanimate red sun present warm is", True),
                ("he thephoa ne mipho tuphai na ta shiho.", "human person inanimate blue cup object present buy", True),
                ("pi mathai ne hashe na ta phewa.", "animate cat inanimate green object present feel", True),
                ("ne sathia shuwhia ta miwhi phera.", "inanimate white sand present fresh is", True),
                ("he nowhea ne tupha whethea na ta whupi.", "human teacher inanimate purple book object present read", True),
                ("ne mipho lashea ta hesha.", "inanimate blue rain present delicious", False),  # semantic mismatch
            ],
            
            # Professional and social contexts
            "professional_contexts": [
                ("he nowhea na he phiphea ta sheme.", "human teacher object human child present teach", True),
                ("he luphea na ne nuthea ta whesa.", "human artist object inanimate sculpture present create", True),
                ("he hathai na ne thaphao ta whari.", "human musician object inanimate song present sing", True),
                ("he thephoa na ne wushia ta whuri.", "human person object inanimate market present work", True),
                ("he raushai na he lushai ta phasu.", "human leader object human group present lead", True),
                ("he thephoa na ne phuthui ta shota.", "human person object inanimate document present document", True),
                ("he luphea na ne whethea ta whesa.", "human artist object inanimate book present create", True),
                ("he hathai na ne nushui ta whera.", "human musician object inanimate language present learn", True),
                ("he nowhea na ne lophui ta sheme.", "human teacher object inanimate art present teach", True),
                ("he thephoa na ne hiwhea ta shuni.", "human person object inanimate house present build", True),
                ("he raushai na ne lowhai ta whesa.", "human leader object inanimate answer present create", True),
                ("he luphea na ne thaphao ta whari.", "human artist object inanimate song present sing", True),
            ],
            
            # New category: Animacy violations and corrections
            "animacy_patterns": [
                ("he thephoa ta whemo.", "human person present think", True),
                ("pi mathai ta whuwe.", "animate cat present sleep", True),
                ("ne lowhai ta riphe phera.", "inanimate answer present important is", True),
                ("he thephoa ta whawi.", "human person present fly", True),  # humans can fly (metaphorically)
                ("pi lophea ta whemo.", "animate bird present think", True),  # animals can think
                ("ne whethea ta whemo.", "inanimate book present think", False),  # books cannot think
                ("he thephoa ta pholi.", "human person present grow", True),  # humans can grow
                ("pi mathai ta sheme.", "animate cat present teach", True),  # animals can be taught
                ("ne raoshea ta whuwe.", "inanimate sun present sleep", False),  # sun cannot sleep
                ("he thephoa ta whale.", "human person present flow", True),  # metaphorical flow
                ("pi whithea ta shuni.", "animate dove present build", False),  # doves don't build houses
                ("ne mothao ta whawi.", "inanimate cloud present fly", True),  # clouds can fly/move
            ],
            
            # New category: Particle ordering violations
            "particle_ordering": [
                ("so hi ma mia ta whemo.", "politeness evidence emphasis I present think", True),  # canonical order
                ("hi so ma mia ta whemo.", "evidence politeness emphasis I present think", False),  # wrong order - evidentiality before politeness
                ("ma hi so mia ta whemo.", "emphasis evidence politeness I present think", False),  # wrong order
                ("hi ma so mia ta whemo.", "evidence emphasis politeness I present think", False),  # wrong order
                ("wa so mia ta whemo.", "question politeness I present think", True),
                ("so wa mia ta whemo.", "politeness question I present think", False),  # wrong order
                ("li ta mia whemo.", "past present I think", False),  # wrong order
                ("ta li mia whemo.", "present past I think", False),  # conflicting tenses
                ("mia si na ta whemo.", "I subject object present think", False),  # wrong particle order
                ("mia na si ta whemo.", "I object subject present think", False),  # wrong particle order
                ("he pi ne thephoa ta whemo.", "human animate inanimate person present think", False),  # conflicting animacy
                ("ne he pi thephoa ta whemo.", "inanimate human animate person present think", False),  # conflicting animacy
            ],
            
            # New category: Classifier usage
            "classifier_usage": [
                ("mia na lea liphai ta whona.", "I object long tree present look", True),
                ("thi na moi whethea ta whupi.", "you object flat book present read", True),
                ("sha na teo mophui ta whuwa.", "they object round ball present throw", True),
                ("he thephoa na lea lathia ta shero.", "human person object long axe present carry", True),
                ("pi mathai na teo tuphai ta shire.", "animate cat object round cup present want", True),
                ("mia na moi moi whethea ta whupi.", "I object flat flat book present read", False),  # double classifier
                ("thi na lea moi whethea ta whupi.", "you object long flat book present read", False),  # conflicting classifiers
                ("sha na teo lathia ta shero.", "they object round axe present carry", False),  # wrong classifier
                ("he thephoa na moi mophui ta whuwa.", "human person object flat ball present throw", False),  # wrong classifier
                ("pi mathai na lea tuphai ta shire.", "animate cat object long cup present want", False),  # wrong classifier
                ("mia na lea ta whona.", "I object long present look", False),  # classifier without noun
                ("thi na whethea ta whupi.", "you object book present read", True),  # classifier optional
            ],
            
            # New category: Aspect and tense combinations
            "aspect_tense_combinations": [
                ("mia li we whera.", "I past perfective learn", True),
                ("thi ta la whesa.", "you present progressive create", True),
                ("sha su ni whuni.", "they future perfect have", True),
                ("he thephoa li pu phoni.", "human person past cessative live", True),
                ("pi mathai ta ri whuwe.", "animate cat present imperfective sleep", True),
                ("mia su po whemo.", "I future inchoative think", True),
                ("thi li wu whera.", "you past experiential learn", True),
                ("sha ta wi whesa.", "they present iterative create", True),
                ("mia li la whera.", "I past progressive learn", False),  # incompatible: past + progressive
                ("thi su we whesa.", "you future perfective create", True),  # future perfect is valid
                ("sha li po phoni.", "they past inchoative live", False),  # incompatible: past + inchoative
                ("he thephoa su pu whemo.", "human person future cessative think", False),  # incompatible: future + cessative
            ],
            
            # New category: Number and agreement
            "number_agreement": [
                ("wo mia ta whemo.", "plural I present think", True),  # plural pronoun
                ("he lo thephoa ta phoni.", "human few person present live", True),
                ("pi no mathai ta whuwe.", "animate many cat present sleep", True),
                ("wo thi ta whera.", "plural you present learn", True),
                ("lo sha ta whesa.", "few they present create", True),
                ("ne no lowhai ta riphe phera.", "inanimate many answer present important is", True),
                ("wo lo mia ta whemo.", "plural few I present think", False),  # conflicting number
                ("lo no thi ta whera.", "few many you present learn", False),  # conflicting number
                ("no wo sha ta whesa.", "many plural they present create", False),  # conflicting number
                ("wo wo mia ta whemo.", "plural plural I present think", False),  # double number
                ("lo lo thi ta whera.", "few few you present learn", False),  # double number
                ("no no sha ta whesa.", "many many they present create", False),  # double number
            ],
            
            # New category: Comparison structures
            "comparison_structures": [
                ("mia pa misha ta phera.", "I superlative beautiful present is", True),
                ("thi mo misha ta phera.", "you comparative beautiful present is", True),
                ("sha sa misha ta phera.", "they equal beautiful present is", True),
                ("he thephoa pa riphe ta phera.", "human person superlative important present is", True),
                ("pi mathai mo tophe ta phera.", "animate cat comparative large present is", True),
                ("ne lowhai sa riphe ta phera.", "inanimate answer equal important present is", True),
                ("mia pa mo misha ta phera.", "I superlative comparative beautiful present is", False),  # conflicting comparison
                ("thi mo sa misha ta phera.", "you comparative equal beautiful present is", False),  # conflicting comparison
                ("sha sa pa misha ta phera.", "they equal superlative beautiful present is", False),  # conflicting comparison
                ("mia pa pa misha ta phera.", "I superlative superlative beautiful present is", False),  # double superlative
                ("thi mo mo misha ta phera.", "you comparative comparative beautiful present is", False),  # double comparative
                ("sha sa sa misha ta phera.", "they equal equal beautiful present is", False),  # double equal
            ],
            
            # Punctuation validation
            "punctuation_validation": [
                ("mia ta thilu.", "I present be", True),
                ("mia ta thilu", "I present be", False),  # missing period
                ("wa mia ta thilu?", "question I present be", False),  # forbidden question mark
                ("mia, ta thilu.", "I present be", False),  # forbidden comma
                ("mia ta thilu!", "I present be", False),  # forbidden exclamation mark
                ('mia ta "thilu".', "I present be", False),  # forbidden quotation marks
                ("mia-ta thilu.", "I present be", False),  # forbidden hyphen
                ("mia ta thilu; wa ni.", "I present be question what", False),  # forbidden semicolon
                ("mia ta thilu: naiphea.", "I present be object", False),  # forbidden colon
                ("mia  ta thilu.", "I present be", False),  # multiple consecutive spaces
                (" mia ta thilu.", "I present be", False),  # leading space
                ("mia ta thilu. ", "I present be", False),  # trailing space
                ("mia (ta) thilu.", "I present be", False),  # forbidden parentheses
                ("mia [ta] thilu.", "I present be", False),  # forbidden square brackets
                ("mia ta 'thilu'.", "I present be", False)  # forbidden single quotes
            ]
        }
    
    def run_category(self, category: str, verbose: bool = True) -> Dict:
        """Run tests for a specific category."""
        if category not in self.test_categories:
            print(f"❌ Unknown category: {category}")
            return {}
        
        tests = self.test_categories[category]
        results = {
            'total': len(tests),
            'correct': 0,
            'incorrect': 0,
            'details': []
        }
        
        if verbose:
            print(f"\n🧪 Testing Category: {category.upper()}")
            print("=" * 60)
        
        for sentence, description, expected_valid in tests:
            result = self.validator.validate_sentence(sentence)
            actual_valid = result['is_valid']
            correct = (actual_valid == expected_valid)
            
            if correct:
                results['correct'] += 1
                status = "✅"
            else:
                results['incorrect'] += 1
                status = "❌"
            
            test_detail = {
                'sentence': sentence,
                'description': description,
                'expected': expected_valid,
                'actual': actual_valid,
                'correct': correct,
                'errors': [{'type': e.error_type.value, 'message': e.message} for e in result['errors']]
            }
            results['details'].append(test_detail)
            
            if verbose:
                print(f"{status} '{sentence}'")
                print(f"   Description: {description}")
                print(f"   Expected: {'VALID' if expected_valid else 'INVALID'}, "
                      f"Got: {'VALID' if actual_valid else 'INVALID'}")
                
                if not correct:
                    print(f"   ⚠️  MISMATCH!")
                
                if result['errors'] and verbose:
                    print(f"   Errors: {len(result['errors'])}")
                    for error in result['errors'][:2]:  # Show first 2 errors
                        print(f"     - {error.error_type.value}: {error.message}")
                    if len(result['errors']) > 2:
                        print(f"     - ... and {len(result['errors']) - 2} more")
                
                print()
        
        if verbose:
            accuracy = (results['correct'] / results['total']) * 100
            print(f"Category Results: {results['correct']}/{results['total']} correct ({accuracy:.1f}%)")
        
        return results
    
    def run_all_categories(self, verbose: bool = True) -> Dict:
        """Run tests for all categories."""
        print("🎯 COMPREHENSIVE PHI SENTENCE VALIDATOR EXERCISE")
        print("=" * 60)
        
        all_results = {}
        total_tests = 0
        total_correct = 0
        
        for category in self.test_categories.keys():
            category_results = self.run_category(category, verbose)
            all_results[category] = category_results
            total_tests += category_results['total']
            total_correct += category_results['correct']
        
        # Overall summary
        overall_accuracy = (total_correct / total_tests) * 100
        print("\n" + "=" * 60)
        print("📊 OVERALL RESULTS")
        print("=" * 60)
        print(f"Total tests: {total_tests}")
        print(f"Correct predictions: {total_correct}")
        print(f"Incorrect predictions: {total_tests - total_correct}")
        print(f"Overall accuracy: {overall_accuracy:.1f}%")
        
        # Category breakdown
        print(f"\n📋 CATEGORY BREAKDOWN:")
        for category, results in all_results.items():
            accuracy = (results['correct'] / results['total']) * 100
            print(f"  {category:20} {results['correct']:3}/{results['total']:3} ({accuracy:5.1f}%)")
        
        return {
            'categories': all_results,
            'summary': {
                'total_tests': total_tests,
                'total_correct': total_correct,
                'overall_accuracy': overall_accuracy
            }
        }
    
    def run_interactive_mode(self):
        """Run interactive testing mode."""
        print("🎮 INTERACTIVE PHI SENTENCE VALIDATOR")
        print("=" * 50)
        print("Enter Phi sentences to validate (empty line to quit)")
        print("Commands:")
        print("  !categories - list available test categories")
        print("  !run <category> - run a specific test category")
        print("  !run all - run all test categories")
        print("  !help - show this help")
        print()
        
        while True:
            try:
                user_input = input("phi> ").strip()
                
                if not user_input:
                    print("Goodbye!")
                    break
                
                if user_input.startswith('!'):
                    self._handle_command(user_input)
                else:
                    # Validate user sentence
                    result = self.validator.validate_sentence(user_input)
                    
                    print(f"Sentence: '{user_input}'")
                    print(f"Valid: {'✅ YES' if result['is_valid'] else '❌ NO'}")
                    
                    if result['errors']:
                        print(f"Errors ({len(result['errors'])}):")
                        for error in result['errors']:
                            print(f"  - {error.error_type.value}: {error.message}")
                    else:
                        print("No errors detected!")
                    
                    print()
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _handle_command(self, command: str):
        """Handle interactive commands."""
        parts = command[1:].split()
        cmd = parts[0] if parts else ""
        
        if cmd == "categories":
            print("Available test categories:")
            for i, category in enumerate(self.test_categories.keys(), 1):
                count = len(self.test_categories[category])
                print(f"  {i:2}. {category:20} ({count} tests)")
            print()
        
        elif cmd == "run":
            if len(parts) < 2:
                print("Usage: !run <category> or !run all")
                return
            
            target = parts[1]
            if target == "all":
                self.run_all_categories(verbose=True)
            elif target in self.test_categories:
                self.run_category(target, verbose=True)
            else:
                print(f"Unknown category: {target}")
                print("Use !categories to see available categories")
        
        elif cmd == "help":
            print("Commands:")
            print("  !categories - list available test categories")
            print("  !run <category> - run a specific test category")
            print("  !run all - run all test categories")
            print("  !help - show this help")
            print()
        
        else:
            print(f"Unknown command: {command}")
            print("Use !help for available commands")
    
    def save_results(self, results: Dict, filename: str = "validation_results.json"):
        """Save test results to JSON file."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {filename}")


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Exercise Phi sentence validator")
    parser.add_argument("--category", "-c", help="Run specific category")
    parser.add_argument("--all", "-a", action="store_true", help="Run all categories")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode (less verbose)")
    parser.add_argument("--save", "-s", help="Save results to file")
    
    args = parser.parse_args()
    
    exerciser = SentenceExerciser()
    
    if args.interactive:
        exerciser.run_interactive_mode()
    elif args.all:
        results = exerciser.run_all_categories(verbose=not args.quiet)
        if args.save:
            exerciser.save_results(results, args.save)
    elif args.category:
        results = exerciser.run_category(args.category, verbose=not args.quiet)
        if args.save:
            exerciser.save_results({args.category: results}, args.save)
    else:
        # Default: show available categories and run interactive mode
        print("🎯 PHI SENTENCE VALIDATOR EXERCISER")
        print("=" * 40)
        print("Available options:")
        print("  --all (-a)           Run all test categories")
        print("  --category (-c) CAT  Run specific category")
        print("  --interactive (-i)   Interactive mode")
        print("  --quiet (-q)         Less verbose output")
        print("  --save (-s) FILE     Save results to file")
        print()
        print("Available categories:")
        for category in exerciser.test_categories.keys():
            count = len(exerciser.test_categories[category])
            print(f"  {category:20} ({count} tests)")
        print()
        print("Starting interactive mode...")
        exerciser.run_interactive_mode()


if __name__ == "__main__":
    main() 