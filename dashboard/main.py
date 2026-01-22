#!/usr/bin/env python3
"""
Phi Language Dashboard - FastAPI Backend
"""

import json
import sqlite3
from pathlib import Path
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import markdown

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
VOCABULARY_DIR = PROJECT_ROOT / "vocabulary"
CONTENT_DIR = VOCABULARY_DIR / "content"
FUNCTION_DIR = VOCABULARY_DIR / "function"
INTERJECTION_DIR = VOCABULARY_DIR / "interjection"
DOCUMENTS_DIR = PROJECT_ROOT / "documents"
GRAMMAR_DIR = DOCUMENTS_DIR / "grammar"
DB_PATH = Path(__file__).parent / "lexicon.db"
FRONTEND_DIR = Path(__file__).parent / "frontend" / "dist"

# Phi phonological rules
CONSONANTS = {'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w'}
FRICATIVE_DIGRAPHS = {'ph', 'th', 'sh', 'wh'}
VOWELS = {'a', 'e', 'i', 'o', 'u'}


# ==================== DATABASE ====================

def get_db():
    """Get database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize/rebuild the database from JSON files."""
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE NOT NULL,
        gloss TEXT NOT NULL,
        ipa TEXT,
        syllables TEXT,
        slot INTEGER,
        pos TEXT,
        concept TEXT,
        description TEXT,
        sound_symbolism TEXT,
        grammatical_notes TEXT,
        image_prompt TEXT,
        pillars TEXT,
        tags TEXT,
        source_file TEXT NOT NULL,
        category TEXT NOT NULL,
        subcategory TEXT
    )
    """)

    entries_added = 0

    if CONTENT_DIR.exists():
        for file_path in sorted(CONTENT_DIR.glob("*.json")):
            if _add_entry(cursor, file_path, "content", None):
                entries_added += 1

    if FUNCTION_DIR.exists():
        for subdir in FUNCTION_DIR.iterdir():
            if subdir.is_dir():
                for file_path in sorted(subdir.glob("*.json")):
                    if _add_entry(cursor, file_path, "function", subdir.name):
                        entries_added += 1

    if INTERJECTION_DIR.exists():
        for file_path in sorted(INTERJECTION_DIR.glob("*.json")):
            if _add_entry(cursor, file_path, "interjection", None):
                entries_added += 1

    conn.commit()
    conn.close()
    return entries_added


def _add_entry(cursor, file_path, category, subcategory):
    """Add a single JSON entry to the database."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)

        if not all(k in entry for k in ['word', 'gloss']):
            return False

        cursor.execute("""
        INSERT INTO words (
            word, gloss, ipa, syllables, slot, pos, concept,
            description, sound_symbolism, grammatical_notes, image_prompt,
            pillars, tags, source_file, category, subcategory
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.get('word'),
            entry.get('gloss'),
            entry.get('ipa'),
            json.dumps(entry.get('syllables')) if entry.get('syllables') else None,
            entry.get('slot'),
            json.dumps(entry.get('pos')) if entry.get('pos') else None,
            entry.get('concept'),
            entry.get('description'),
            entry.get('sound_symbolism'),
            entry.get('grammatical_notes'),
            entry.get('image_prompt'),
            json.dumps(entry.get('pillars')) if entry.get('pillars') else None,
            json.dumps(entry.get('tags')) if entry.get('tags') else None,
            str(file_path.relative_to(PROJECT_ROOT)),
            category,
            subcategory
        ))
        return True
    except (json.JSONDecodeError, sqlite3.IntegrityError) as e:
        print(f"Error processing {file_path}: {e}")
        return False


# ==================== PHONOLOGICAL VALIDATION ====================

def parse_syllables(word: str):
    """Parse a word into CV syllables."""
    syllables = []
    i = 0
    word = word.lower()

    while i < len(word):
        syllable = ""

        if i + 1 < len(word) and word[i:i+2] in FRICATIVE_DIGRAPHS:
            syllable = word[i:i+2]
            i += 2
        elif word[i] in CONSONANTS:
            syllable = word[i]
            i += 1
        elif not syllables:
            return None, f"Word must begin with a consonant, found '{word[i]}'"
        else:
            return None, f"Invalid character '{word[i]}' at position {i}"

        if i < len(word) and word[i] in VOWELS:
            syllable += word[i]
            i += 1
            syllables.append(syllable)
        elif syllable:
            return None, f"Syllable '{syllable}' missing required vowel"
        else:
            return None, f"Unexpected end of word"

    return syllables, None


def validate_word(word: str):
    """Validate a Phi word against phonological rules."""
    errors = []
    warnings = []
    word = word.lower().strip()

    if not word:
        return {"valid": False, "errors": ["Word cannot be empty"], "warnings": [], "syllables": []}

    syllables, error = parse_syllables(word)
    if error:
        return {"valid": False, "errors": [error], "warnings": [], "syllables": []}

    if len(syllables) != len(set(syllables)):
        errors.append("Word contains duplicate syllables")

    vowel_count = 0
    for c in word:
        if c in VOWELS:
            vowel_count += 1
            if vowel_count >= 3:
                errors.append("Word contains three or more consecutive vowels (VVV+)")
                break
        else:
            vowel_count = 0

    if len(syllables) == 1:
        warnings.append("Single-syllable words are typically reserved for particles and numerals")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "syllables": syllables
    }


def generate_ipa(syllables: list[str]) -> str:
    """Generate IPA transcription from syllables."""
    ipa_map = {
        'ph': 'φ', 'th': 'θ', 'sh': 'ʃ', 'wh': 'ʍ',
        'h': 'h', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
        'p': 'p', 'r': 'r', 's': 's', 't': 't', 'w': 'w',
        'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'
    }

    ipa_syllables = []
    for syl in syllables:
        ipa_syl = ""
        i = 0
        while i < len(syl):
            if i + 1 < len(syl) and syl[i:i+2] in FRICATIVE_DIGRAPHS:
                ipa_syl += ipa_map[syl[i:i+2]]
                i += 2
            else:
                ipa_syl += ipa_map.get(syl[i], syl[i])
                i += 1
        ipa_syllables.append(ipa_syl)

    return "/" + ".".join(ipa_syllables) + "/"


# ==================== PYDANTIC MODELS ====================

class WordCreate(BaseModel):
    word: str
    gloss: str
    pos: list[str]
    concept: str
    description: str
    sound_symbolism: str
    pillars: dict[str, str]
    category: str = "content"
    subcategory: Optional[str] = None
    grammatical_notes: Optional[str] = None
    tags: Optional[dict[str, str]] = None
    slot: Optional[int] = None


class WordUpdate(BaseModel):
    gloss: Optional[str] = None
    ipa: Optional[str] = None
    syllables: Optional[list[str]] = None
    pos: Optional[list[str]] = None
    concept: Optional[str] = None
    description: Optional[str] = None
    sound_symbolism: Optional[str] = None
    grammatical_notes: Optional[str] = None
    pillars: Optional[dict[str, str]] = None
    tags: Optional[dict[str, str]] = None
    slot: Optional[int] = None


class ValidationRequest(BaseModel):
    word: str


# ==================== FASTAPI APP ====================

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize database if needed
    if not DB_PATH.exists():
        print("Initializing database...")
        count = init_db()
        print(f"Added {count} entries.")
    yield
    # Shutdown: nothing to do


app = FastAPI(
    title="Phi Language Dashboard",
    description="API for managing the Phi constructed language vocabulary and grammar",
    version="2.0.0",
    lifespan=lifespan
)

# CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== API ROUTES ====================

@app.post("/api/sync")
async def sync_database():
    """Rebuild database from JSON files."""
    try:
        count = init_db()
        return {"success": True, "count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/stats")
async def get_stats():
    """Get vocabulary statistics."""
    conn = get_db()
    cursor = conn.cursor()

    stats = {}

    cursor.execute("SELECT COUNT(*) FROM words")
    stats['total'] = cursor.fetchone()[0]

    cursor.execute("SELECT category, COUNT(*) FROM words GROUP BY category")
    stats['by_category'] = {row[0]: row[1] for row in cursor.fetchall()}

    cursor.execute("SELECT pos FROM words WHERE pos IS NOT NULL")
    pos_counts = {}
    for row in cursor.fetchall():
        try:
            pos_list = json.loads(row[0])
            for pos in pos_list:
                pos_counts[pos] = pos_counts.get(pos, 0) + 1
        except:
            pass
    stats['by_pos'] = pos_counts

    cursor.execute("""
        SELECT subcategory, COUNT(*) FROM words
        WHERE category='function' AND subcategory IS NOT NULL
        GROUP BY subcategory
    """)
    stats['function_subcategories'] = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()
    return stats


@app.get("/api/words")
async def get_words(
    search: str = "",
    category: str = "",
    subcategory: str = "",
    pos: str = "",
    sort: str = "gloss",
    limit: int = Query(default=50, le=500),
    offset: int = 0
):
    """Get vocabulary list with optional filtering."""
    conn = get_db()
    cursor = conn.cursor()

    conditions = []
    params = []

    if search:
        conditions.append("(word LIKE ? OR gloss LIKE ? OR concept LIKE ? OR description LIKE ?)")
        params.extend([f'%{search}%'] * 4)

    if category:
        conditions.append("category = ?")
        params.append(category)

    if subcategory:
        conditions.append("subcategory = ?")
        params.append(subcategory)

    if pos:
        conditions.append("pos LIKE ?")
        params.append(f'%"{pos}"%')

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    # Validate sort field to prevent SQL injection
    order_by = "word" if sort == "word" else "gloss"

    cursor.execute(f"SELECT COUNT(*) FROM words WHERE {where_clause}", params)
    total = cursor.fetchone()[0]

    cursor.execute(f"""
        SELECT id, word, gloss, ipa, pos, concept, category, subcategory
        FROM words
        WHERE {where_clause}
        ORDER BY {order_by}
        LIMIT ? OFFSET ?
    """, params + [limit, offset])

    words = []
    for row in cursor.fetchall():
        words.append({
            'id': row[0],
            'word': row[1],
            'gloss': row[2],
            'ipa': row[3],
            'pos': json.loads(row[4]) if row[4] else [],
            'concept': row[5],
            'category': row[6],
            'subcategory': row[7]
        })

    conn.close()
    return {'words': words, 'total': total, 'limit': limit, 'offset': offset}


@app.get("/api/words/{word}")
async def get_word(word: str):
    """Get full details for a single word by reading directly from JSON file."""
    conn = get_db()
    cursor = conn.cursor()

    # Get the source file path from the database
    cursor.execute("SELECT source_file FROM words WHERE word = ?", (word,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Word not found")

    source_file = PROJECT_ROOT / row[0]

    # Read directly from the JSON file to get the latest content
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            entry = json.load(f)
        # Add source_file to the response
        entry['source_file'] = row[0]
        return entry
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Source file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in source file")


@app.put("/api/words/{word}")
async def update_word(word: str, data: WordUpdate):
    """Update a word entry."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT source_file FROM words WHERE word = ?", (word,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Word not found")

    source_file = PROJECT_ROOT / row[0]

    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            entry = json.load(f)

        update_data = data.model_dump(exclude_none=True)
        for key, value in update_data.items():
            entry[key] = value

        with open(source_file, 'w', encoding='utf-8') as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)

        # Update database
        cursor.execute("""
            UPDATE words SET
                gloss = ?, ipa = ?, syllables = ?, slot = ?, pos = ?,
                concept = ?, description = ?, sound_symbolism = ?,
                grammatical_notes = ?, image_prompt = ?, pillars = ?, tags = ?
            WHERE word = ?
        """, (
            entry.get('gloss'),
            entry.get('ipa'),
            json.dumps(entry.get('syllables')) if entry.get('syllables') else None,
            entry.get('slot'),
            json.dumps(entry.get('pos')) if entry.get('pos') else None,
            entry.get('concept'),
            entry.get('description'),
            entry.get('sound_symbolism'),
            entry.get('grammatical_notes'),
            entry.get('image_prompt'),
            json.dumps(entry.get('pillars')) if entry.get('pillars') else None,
            json.dumps(entry.get('tags')) if entry.get('tags') else None,
            word
        ))
        conn.commit()
        conn.close()
        return {"success": True}
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/words")
async def create_word(data: WordCreate):
    """Create a new word entry."""
    validation = validate_word(data.word)
    if not validation['valid']:
        raise HTTPException(status_code=400, detail=f"Invalid word: {'; '.join(validation['errors'])}")

    if data.category == 'content':
        file_path = CONTENT_DIR / f"{data.gloss.lower().replace(' ', '-')}.json"
    elif data.category == 'function' and data.subcategory:
        file_path = FUNCTION_DIR / data.subcategory / f"{data.gloss.lower().replace(' ', '-')}.json"
    elif data.category == 'interjection':
        file_path = INTERJECTION_DIR / f"{data.gloss.lower().replace(' ', '-')}.json"
    else:
        raise HTTPException(status_code=400, detail="Invalid category/subcategory")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM words WHERE word = ? OR gloss = ?", (data.word, data.gloss))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Word or gloss already exists")

    entry = {
        'word': data.word,
        'gloss': data.gloss,
        'ipa': generate_ipa(validation['syllables']),
        'syllables': validation['syllables'],
        'pos': data.pos,
        'concept': data.concept,
        'description': data.description,
        'sound_symbolism': data.sound_symbolism,
        'pillars': data.pillars
    }

    if data.slot is not None:
        entry['slot'] = data.slot
    if data.grammatical_notes:
        entry['grammatical_notes'] = data.grammatical_notes
    if data.tags:
        entry['tags'] = data.tags

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)

        cursor.execute("""
            INSERT INTO words (
                word, gloss, ipa, syllables, slot, pos, concept,
                description, sound_symbolism, grammatical_notes, image_prompt,
                pillars, tags, source_file, category, subcategory
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entry['word'],
            entry['gloss'],
            entry['ipa'],
            json.dumps(entry.get('syllables')),
            entry.get('slot'),
            json.dumps(entry.get('pos')),
            entry.get('concept'),
            entry.get('description'),
            entry.get('sound_symbolism'),
            entry.get('grammatical_notes'),
            entry.get('image_prompt'),
            json.dumps(entry.get('pillars')),
            json.dumps(entry.get('tags')) if entry.get('tags') else None,
            str(file_path.relative_to(PROJECT_ROOT)),
            data.category,
            data.subcategory
        ))
        conn.commit()
        conn.close()
        return {"success": True, "word": entry['word']}
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/validate")
async def validate(data: ValidationRequest):
    """Validate a word against Phi phonological rules."""
    result = validate_word(data.word)
    if result['valid'] and result['syllables']:
        result['ipa'] = generate_ipa(result['syllables'])
    return result


@app.get("/api/particles")
async def get_particles():
    """Get all particles organized by slot."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT word, gloss, ipa, slot, concept, description
        FROM words
        WHERE category = 'function' AND subcategory = 'particle'
        ORDER BY slot, word
    """)

    particles = {'0': [], '1': [], '2': []}

    for row in cursor.fetchall():
        particle = {
            'word': row[0],
            'gloss': row[1],
            'ipa': row[2],
            'slot': row[3],
            'concept': row[4],
            'description': row[5]
        }
        slot_key = str(row[3]) if row[3] in [0, 1, 2] else None
        if slot_key:
            particles[slot_key].append(particle)

    conn.close()
    return particles


@app.get("/api/grammar")
async def get_grammar_docs():
    """List available grammar documents."""
    docs = []

    if GRAMMAR_DIR.exists():
        for file_path in sorted(GRAMMAR_DIR.glob("*.md")):
            docs.append({
                'name': file_path.stem,
                'title': file_path.stem.replace('-', ' ').replace('_', ' ').title(),
                'path': f"grammar/{file_path.name}"
            })

    for file_path in sorted(DOCUMENTS_DIR.glob("*.md")):
        docs.append({
            'name': file_path.stem,
            'title': file_path.stem.replace('-', ' ').replace('_', ' ').title(),
            'path': file_path.name
        })

    return docs


@app.get("/api/grammar/{doc_path:path}")
async def get_grammar_doc(doc_path: str):
    """Get a grammar document rendered as HTML."""
    file_path = DOCUMENTS_DIR / doc_path

    if not file_path.exists() or not file_path.suffix == '.md':
        raise HTTPException(status_code=404, detail="Document not found")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        html = markdown.markdown(content, extensions=['tables', 'fenced_code', 'toc'])

        return {
            'title': file_path.stem.replace('-', ' ').replace('_', ' ').title(),
            'content': html,
            'raw': content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Serve frontend (production)
if FRONTEND_DIR.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIR / "assets"), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """Serve the React frontend."""
        file_path = FRONTEND_DIR / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(FRONTEND_DIR / "index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
