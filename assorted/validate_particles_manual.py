#!/usr/bin/env python3
"""
Manual systematic validation of all Phi words in particles.md.
Going through each section and example manually.
"""

from phi_lexicon_reader import PhiLexiconReader
from phi_validator import PhiValidator
from phi_validation.core import PhiSentenceValidator

def check_word(word, reader, validator, sentence_validator):
    """Check a single word using all three tools."""
    print(f"  {word:12} ->", end=" ")
    
    # Check 1: phi_lexicon_reader
    exists = reader.word_exists(word)
    if exists:
        word_info = reader.get_word_info(word)
        pos = word_info.get('pos', 'unknown')
        translation = word_info.get('translation', 'no translation')
        print(f"✅ {pos:8} ({translation})")
        return True
    else:
        # Check 2: phi_validator (phonotactic)
        is_valid_phonotactic = any(
            any(entry.word == word for entry in entries) 
            for pos, entries in validator.lexicon.items()
        )
        
        if is_valid_phonotactic:
            print("⚠️  PHONOTACTIC_VALID (but not in lexicon)")
            return False
        else:
            print("❌ NOT_FOUND")
            return False

def main():
    print("🔧 Loading validation tools...")
    reader = PhiLexiconReader('pos/')
    validator = PhiValidator('pos/')
    sentence_validator = PhiSentenceValidator()
    
    print("📋 Manual systematic validation of particles.md")
    print("=" * 60)
    
    # Dictionary to track all words and their status
    all_words = {}
    
    # SECTION 1: Basic politeness examples
    print("\n📍 SECTION 1: Basic politeness examples")
    section1_words = [
        'nuthui', 'whuwa',  # from: nuthui whuwa
        'so',               # from: so nuthui whuwa
        'mia', 'phemo', 'whethui', 'phera', 'mipho'  # from: mia phemo whethui phera mipho
    ]
    
    for word in section1_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 2: Evidentiality examples
    print("\n📍 SECTION 2: Evidentiality examples")
    section2_words = [
        'hi', 'phala',      # from: hi phera phala
        'ro',               # from: ro phera phala
        'nu',               # from: nu phera phala
        'ti',               # from: ti phera phala
        'mu', 'li',         # from: mu li phera phala
        'pe'                # from: pe phera phala
    ]
    
    for word in section2_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 3: Discourse marker examples
    print("\n📍 SECTION 3: Discourse marker examples")
    section3_words = [
        'ha', 'liphai', 'phose', 'phi', 'tophe',  # from: ha liphai, mia li phose phi tophe
        'whethui', 'mipha',                       # from: ha whethui, phera mipha
        'me', 'thi'                               # from: mia mipho phemo. mi thi me phemo
    ]
    
    for word in section3_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 4: Basic tense examples
    print("\n📍 SECTION 4: Basic tense/aspect examples")
    section4_words = [
        'ta', 'su', 'we', 'to', 'la', 'ni',  # tense/aspect particles
        'po', 'pu', 'ri', 'wi', 'wu'         # more aspect particles
    ]
    
    for word in section4_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 5: Comparison examples
    print("\n📍 SECTION 5: Comparison examples")
    section5_words = [
        'mo', 'loshea',         # from: whethui phera mo mipho mo loshea
        'pa', 'pisha', 'phelui', # from comparison examples
        'sa', 'siwhea',         # from equality examples
        'le', 'waphe', 'phoshea', 'mathea',  # from less examples
        're', 'tephe', 'methui', 'tawhai'    # from least examples
    ]
    
    for word in section5_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 6: Animacy examples
    print("\n📍 SECTION 6: Animacy examples")
    section6_words = [
        'he', 'thephoa', 'hiwhea', 'sharo', 'thashoa',  # human example
        'pi', 'lophea', 'mathai', 'shune',              # animate example
        'ne', 'whowe', 'tapine', 'phiwhai',             # inanimate example
        'lo', 'phiphea', 'thothea', 'whari'             # birds example
    ]
    
    for word in section6_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 7: Number examples
    print("\n📍 SECTION 7: Number examples")
    section7_words = [
        'wo', 'no'  # paucal and greater plural
    ]
    
    for word in section7_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # SECTION 8: Discourse sequences (complex examples)
    print("\n📍 SECTION 8: Discourse sequences")
    section8_words = [
        # From basic topic introduction
        'ritune', 'lashea', 'phema', 'taoshea', 'pharu', 'tupo', 'riwhea', 'thewa',
        # From topic shift examples
        'lotha', 'whiophea', 'seiwhea', 'naho', 'phiwe', 'haiwhia', 'riphoa',
        # From other discourse examples
        'thasha', 'phothui', 'phiro', 'muphui', 'thuwhui', 'riphe', 'whethea', 'weshi',
        'pewhia', 'phuroa'
    ]
    
    for word in section8_words:
        all_words[word] = check_word(word, reader, validator, sentence_validator)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    valid_words = [word for word, status in all_words.items() if status]
    invalid_words = [word for word, status in all_words.items() if not status]
    
    print(f"✅ Valid words:   {len(valid_words):3d}/{len(all_words)}")
    print(f"❌ Invalid words: {len(invalid_words):3d}/{len(all_words)}")
    print(f"📈 Success rate:  {len(valid_words)/len(all_words)*100:.1f}%")
    
    if invalid_words:
        print(f"\n❌ WORDS NEEDING REPLACEMENT:")
        for word in sorted(invalid_words):
            print(f"   {word}")
    
    print(f"\n✅ CONFIRMED VALID WORDS:")
    for word in sorted(valid_words):
        print(f"   {word}")

if __name__ == "__main__":
    main() 