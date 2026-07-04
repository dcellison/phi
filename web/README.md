# Phi lexicon explorer

A static, read-only view over `vocabulary/` — the repository stays the single source of truth.

Local preview:

```bash
python3 scripts/build_explorer.py
python3 -m http.server -d web
```

then open http://localhost:8000. Deployed automatically to GitHub Pages on every push to main (`.github/workflows/pages.yml`).
