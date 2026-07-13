# Phi lexicon explorer

This directory is a static, read-only view over the repository, which stays the single source of truth. `index.html` is the landing page rendered from `kia.md`, and `explore.html` is the searchable lexicon. The `primer/`, `manual/`, `book/`, `texts/`, and `pamphlets/` directories hold the longer reading sections; the manual leaves its lexicon reference to the explorer.

The build script generates `index.html`, `lexicon.json`, `compounds.json`, and all five reading directories. Those outputs are gitignored.

Local preview:

```bash
python3 scripts/build_explorer.py
python3 -m http.server -d web
```

then open http://localhost:8000. Deployed automatically to GitHub Pages on every push to main (`.github/workflows/pages.yml`).
