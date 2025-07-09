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
- **Add new words** with comprehensive validation (`--add-word`)

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

# Add new words with comprehensive validation
python phi_word_lookup.py --add-word luphai cliff noun --category "essential natural places"

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
| `--add-word WORD TRANSLATION POS` | Add new word with validation |
| `--category "category"` | Specify category for new word (use with --add-word) |
| `--stats` | Show vocabulary statistics by POS |
| `--pos-dir PATH` | Specify POS directory path |
| `--db-file FILE` | Specify database JSON file |

## File Structure

```
utilities/
├── phi_word_lookup.py     # Main utility script
├── remove_word.py         # Word removal utility
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
5. **Adding new words** with proper phonotactic validation

### Quick Validation Workflow

When writing phi examples:

```bash
# Check if your example words exist
python phi_word_lookup.py word1 word2 word3

# If any don't exist, search for alternatives
python phi_word_lookup.py --search "meaning you want"

# Add missing words with comprehensive validation
python phi_word_lookup.py --add-word newword translation pos --category "category"

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

---

# Phi Lexicon Word Removal Utility

Additional utility for removing words from both the JSON database and Markdown files. 

**Note:** For adding words, use `python3 phi_word_lookup.py --add-word <word> <translation> <pos> --category <category>` which provides comprehensive phonotactic validation and automatic category suggestion.

## remove_word.py

Removes word(s) from both the JSON database and corresponding Markdown file.

### Usage

```bash
python3 remove_word.py <word1> [word2] [word3] ...
```

### Examples

```bash
# Remove a single word
python3 remove_word.py pathea

# Remove multiple words at once
python3 remove_word.py pathea ronshea thathui mishea
```

### Features

- **Batch removal** - Remove multiple words in one command
- **Dual file cleanup** - Removes from both JSON and Markdown files
- **Detailed feedback** - Shows exactly what was removed from each file
- **Confirmation prompt** - Requires user confirmation before removal
- **Error handling** - Reports words not found in lexicon
- **Final statistics** - Shows remaining word count

### Example Output

```bash
$ python3 remove_word.py pathea ronshea

About to remove 2 word(s): pathea, ronshea
Continue? (y/N): y

Removing 'pathea' (past) from noun:
  Removed from phi_words.json
  Removed from source/pos/nouns.md: | pathea   | past                |

Removing 'ronshea' (future) from noun:
  Removed from phi_words.json
  Removed from source/pos/nouns.md: | ronshea  | future              |

Successfully removed 2 word(s) from lexicon:
  - pathea
  - ronshea

Total words remaining in lexicon: 875
```

## Complete Lexicon Management Workflow

### Adding words (recommended method)

```bash
# Use phi_word_lookup.py for comprehensive validation
python3 phi_word_lookup.py --add-word luphai cliff noun --category "essential natural places"

# Alternatively, with automatic category suggestion
python3 phi_word_lookup.py --add-word shipha mountain noun
```

### Removing words

```bash
# Remove redundant or incorrect words
python3 remove_word.py pathea ronshea mishea saphai

# Remove duplicates found during cleanup
python3 remove_word.py duplicate1 duplicate2
```

### Database maintenance

```bash
# After any lexicon changes, rebuild the database
python3 phi_word_lookup.py --extract

# Verify changes took effect
python3 phi_word_lookup.py newword
```

## Safety Features

The removal utility includes important safety measures:

- **Confirmation prompts** - User must confirm before making changes
- **JSON validation** - Ensures database remains valid after operations
- **Error handling** - Graceful handling of missing files or invalid JSON
- **Detailed feedback** - Shows exactly what was changed where
- **Backup recommendations** - Consider backing up files before bulk operations

## Integration with phi_word_lookup.py

The removal utility works seamlessly with the main lookup utility:

```bash
# 1. Add words with comprehensive validation
python3 phi_word_lookup.py --add-word newword translation pos --category "category"

# 2. Remove words if needed
python3 remove_word.py unwantedword

# 3. Rebuild database to reflect changes
python3 phi_word_lookup.py --extract

# 4. Verify the changes
python3 phi_word_lookup.py --stats
```

## Troubleshooting

### Common Issues

**JSON file becomes invalid:**
- Check for syntax errors after manual edits
- Use `python3 -m json.tool phi_words.json` to validate
- Look for trailing commas or missing brackets

**Word not found in Markdown:**
- Verify the word exists in the expected category section
- Check table formatting matches expected pattern
- Ensure category name matches exactly

**Permission errors:**
- Ensure you have write access to both utilities/ and source/pos/ directories
- Check that files aren't open in other applications
- Verify file permissions allow modification

### Recovery

If something goes wrong:

1. **JSON corruption:** Restore from backup or regenerate with `phi_word_lookup.py --extract`
2. **Markdown corruption:** Check git history or restore from backup
3. **Accidental removal:** Use `phi_word_lookup.py --add-word` to re-add with proper validation

## Best Practices

1. **Test with single words** before bulk operations
2. **Back up files** before major changes
3. **Use phi_word_lookup.py --add-word** for adding new words (comprehensive validation)
4. **Rebuild lookup database** after lexicon changes with `--extract`
5. **Verify changes** with `phi_word_lookup.py` lookups after modifications 