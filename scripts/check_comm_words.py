#!/usr/bin/env python3
"""Quick check for which communication-and-expression words already exist"""

import os
import sys
sys.path.append(os.path.dirname(__file__))
from check_vocabulary import load_all_words
from pathlib import Path

# Words from communication-and-expression category
comm_words = [
    "communication", "conversation", "dialogue", "expression", "language",
    "word", "phrase", "message", "statement", "question", "answer", 
    "explanation", "idea", "thought", "story", "narrative", "poetry",
    "song", "music", "sound", "tone", "voice", "speech", "talk",
    "speak", "say", "tell", "mention", "discuss", "explain", "announce",
    "share", "express", "whisper", "shout", "call", "invite", "welcome",
    "address", "report", "declare", "present", "describe", "relate",
    "connect", "listen", "hear", "interpret", "respond", "reply", "react",
    "affirm", "agree", "disagree", "encourage", "inspire", "inform",
    "suggest", "propose", "request", "offer", "promise", "apologize",
    "thank", "gratitude", "compliment", "criticize", "recommend",
    "acknowledge", "emphasize", "highlight", "illustrate", "clarify",
    "elaborate", "summarize", "repeat", "paraphrase", "translate",
    "draw", "write", "inscribe", "narrate", "perform", "demonstrate",
    "broadcast", "converse", "reflect", "inquire", "engage", "participate",
    "create", "compose", "improvise", "observe", "signal"
]

# Load existing vocabulary
words_dir = Path(__file__).parent.parent / "words"
existing_words = load_all_words(words_dir)

# Check which already exist
existing_glosses = {}
for phi_word, glosses in existing_words.items():
    for gloss_info in glosses:
        gloss = gloss_info.split(' (')[0].lower()
        if gloss not in existing_glosses:
            existing_glosses[gloss] = []
        existing_glosses[gloss].append((phi_word, gloss_info))

print("EXISTING WORDS FROM COMMUNICATION-AND-EXPRESSION LIST:")
print("=" * 60)
found = 0
for word in comm_words:
    if word in existing_glosses:
        found += 1
        for phi_word, full_gloss in existing_glosses[word]:
            print(f"{word:20} → {phi_word:15} ({full_gloss})")

print(f"\n{found} words already exist out of {len(comm_words)} total")
print(f"{len(comm_words) - found} new words need to be created")