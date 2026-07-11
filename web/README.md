# Phi lexicon explorer

A static, read-only view over the repository, which stays the single source of truth. The pages: `index.html` (the landing — kia.md rendered at build time), `explore.html` (the searchable lexicon), `primer/` (the full primer, one page per chapter), and `manual/` (every manual section with a grouped contents page; the lexicon reference is excluded because the explorer is that content). Everything generated — `index.html`, `lexicon.json`, `compounds.json`, `primer/`, `manual/`, `texts/`, `pamphlets/` — comes from the build script and is gitignored.

Local preview:

```bash
python3 scripts/build_explorer.py
python3 -m http.server -d web
```

then open http://localhost:8000. Deployed automatically to GitHub Pages on every push to main (`.github/workflows/pages.yml`).
