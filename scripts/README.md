# Phi Vocabulary Management Scripts

## check_vocabulary.py

A Python script to help prevent duplicate words when creating new Phi vocabulary.

### Features

- **Duplicate Detection**: Checks if a word already exists in the vocabulary
- **Similar Word Detection**: Finds words that differ by only one character
- **Interactive Mode**: Check words one at a time
- **Batch Mode**: Check multiple words from a file
- **List Mode**: Display all existing words alphabetically

### Usage

#### Interactive Mode (default)
```bash
python3 scripts/check_vocabulary.py
# or
./scripts/phicheck
```

Enter words one at a time to check for duplicates. Type 'quit' to exit.

#### List All Words
```bash
python3 scripts/check_vocabulary.py --list
# or
./scripts/phicheck --list
```

Lists all words in the vocabulary with their glosses and categories.

#### Batch Check
```bash
python3 scripts/check_vocabulary.py --batch words_to_check.txt
# or
./scripts/phicheck --batch words_to_check.txt
```

Checks all words listed in a text file (one word per line).

### Example Output

```
Enter a Phi word to check (or 'quit' to exit): shelu

❌ DUPLICATE FOUND: 'shelu' already exists as:
   - mercy (abstract-qualities-and-values)

Enter a Phi word to check (or 'quit' to exit): shela

⚠️  SIMILAR WORDS FOUND (differ by 1 character):
   'shelu':
      - mercy (abstract-qualities-and-values)

Enter a Phi word to check (or 'quit' to exit): phika

✅ 'phika' is available - no duplicates or similar words found!
```

### Integration with Claude Code

When creating new words with Claude Code, you can:

1. Run the script before starting to see all existing words
2. Check each new word interactively as you create it
3. Create a batch file of planned words and check them all at once

This helps maintain the integrity of the Phi vocabulary by preventing accidental duplicates and ensuring each word is unique.