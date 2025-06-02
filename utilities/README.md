# Phi Word Lookup Utility

A Python utility for extracting, validating, and looking up words from the phi constructed language documentation.

## Features

- **Extract all phi words** from POS documentation files
- **Validate word existence** in phi vocabulary  
- **Lookup POS categories** and English translations
- **Validate entire sentences** for phi word usage
- **Search by English translation** to find phi words
- **Generate vocabulary statistics** across POS categories
- **Interactive and command-line modes**

## Setup

### 1. Create Virtual Environment (Recommended)

```bash
# Navigate to utilities directory
cd utilities

# Create virtual environment
python3 -m venv phi_env

# Activate virtual environment
# On macOS/Linux:
source phi_env/bin/activate
# On Windows:
# phi_env\Scripts\activate

# Install dependencies (minimal - uses standard library)
pip install -r requirements.txt
```

### 2. First Run (Build Database)

```bash
# Extract all words from POS files and build database
python phi_word_lookup.py --extract
```

This will create a `phi_words.json` file containing all extracted phi words.

## Usage Examples

### Command Line Lookups

```bash
# Look up individual words
python phi_word_lookup.py mia whethea shose

# Validate a sentence
python phi_word_lookup.py --validate "mia na whethea shose"

# Search for words by English meaning
python phi_word_lookup.py --search water

# Show vocabulary statistics
python phi_word_lookup.py --stats

# Re-extract words from source files
python phi_word_lookup.py --extract
```

### Interactive Mode

```bash
# Start interactive mode
python phi_word_lookup.py

# Then type words or commands:
# mia whethea shose          # Look up words
# s:water                    # Search by translation
# quit                       # Exit
```

### Example Output

```
$ python phi_word_lookup.py mia whethea shose

Word Lookup Results:
==================================================
✓ mia          [pronoun    ] I/me
✓ whethea      [noun       ] book
✓ shose        [verb       ] see
```

```
$ python phi_word_lookup.py --validate "mia na whethea shose"

Validating sentence: 'mia na whethea shose'
==================================================
✓ mia          [pronoun    ] I/me
✓ na           [particle   ] object marker
✓ whethea      [noun       ] book
✓ shose        [verb       ] see
==================================================
✓ All words are valid phi words!
```

## Command Line Options

| Option | Description |
|--------|-------------|
| `words` | Look up specific words |
| `--extract` | Re-extract all words from POS files |
| `--validate "sentence"` | Validate all words in a sentence |
| `--search "term"` | Search for words containing English term |
| `--stats` | Show vocabulary statistics by POS |
| `--pos-dir PATH` | Specify POS directory path |
| `--db-file FILE` | Specify database JSON file |

## File Structure

```
utilities/
├── phi_word_lookup.py     # Main utility script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── phi_words.json        # Generated word database
└── phi_env/              # Virtual environment (after setup)
```

## Integration with Documentation Work

This utility is perfect for:

1. **Validating examples** in grammar documentation
2. **Finding replacement words** when needed words don't exist
3. **Checking sentence validity** before adding to docs
4. **Discovering available vocabulary** in each POS category

### Quick Validation Workflow

When writing phi examples:

```bash
# Check if your example words exist
python phi_word_lookup.py word1 word2 word3

# If any don't exist, search for alternatives
python phi_word_lookup.py --search "meaning you want"

# Validate complete sentence
python phi_word_lookup.py --validate "your phi sentence"
```

## Deactivating Virtual Environment

When finished:

```bash
deactivate
```

## Troubleshooting

**Database not found**: Run `python phi_word_lookup.py --extract` to build initial database.

**Empty results**: Check that `../source/pos/` directory contains the phi POS markdown files.

**Permission errors**: Ensure virtual environment is activated and you have write permissions in the utilities directory. 