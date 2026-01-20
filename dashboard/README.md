# Phi Language Dashboard

A modern web interface for managing the Phi constructed language vocabulary and grammar.

**Stack:** FastAPI + React + shadcn/ui + Tailwind CSS

## Quick Start

### 1. Install Backend Dependencies

```bash
cd phi/dashboard

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 3. Run in Development Mode

**Terminal 1 - Backend:**
```bash
cd phi/dashboard
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

**Terminal 2 - Frontend:**
```bash
cd phi/dashboard/frontend
npm run dev
```

Then open http://localhost:5173

### 4. Production Build

```bash
cd frontend
npm run build
```

Then just run the backend - it will serve the built frontend:
```bash
cd phi/dashboard
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --host 0.0.0.0 --port 5000
```

Open http://localhost:5000

## Features

- **Vocabulary Browser**: Search, filter, and browse 785+ vocabulary entries
- **Word Detail View**: Full information with IPA, syllables, sound symbolism, and philosophical pillars
- **Particle Reference**: All particles organized by slot position
- **Grammar Reference**: Browse all grammar documentation
- **Word Creator**: Create new entries with real-time phonological validation

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stats` | Vocabulary statistics |
| GET | `/api/words` | List words (with search/filter) |
| GET | `/api/words/{word}` | Get word details |
| POST | `/api/words` | Create new word |
| PUT | `/api/words/{word}` | Update word |
| POST | `/api/validate` | Validate word phonology |
| POST | `/api/sync` | Rebuild database |
| GET | `/api/particles` | Get particles by slot |
| GET | `/api/grammar` | List grammar docs |
| GET | `/api/grammar/{path}` | Get grammar doc content |

## Project Structure

```
dashboard/
├── main.py              # FastAPI backend
├── requirements.txt     # Python dependencies
├── lexicon.db          # SQLite database (auto-generated)
├── README.md
└── frontend/
    ├── package.json
    ├── vite.config.ts
    ├── tailwind.config.js
    ├── tsconfig.json
    ├── index.html
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── index.css
        ├── lib/
        │   └── utils.ts
        ├── components/
        │   └── ui/        # shadcn/ui components
        └── pages/
            ├── VocabularyPage.tsx
            ├── ParticlesPage.tsx
            ├── GrammarPage.tsx
            └── CreateWordPage.tsx
```

## Tech Stack

- **Backend**: FastAPI, SQLite, Python 3.10+
- **Frontend**: React 18, TypeScript, Vite
- **UI**: shadcn/ui, Radix UI, Tailwind CSS
- **Routing**: React Router
