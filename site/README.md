# Phi website source

This directory holds the maintained assets for Phi's website: the lexicon explorer shell, styles, browser scripts, and fonts. It contains no generated pages or data.

The site builder copies these assets to `build/site/`, renders the repository's Markdown shelves there, and generates the lexicon and compound data. The complete deployment tree is ignored by Git.

Local preview:

```bash
python3 scripts/build_site.py
python3 -m http.server -d build/site
```

Then open http://localhost:8000. GitHub Pages builds and deploys the same directory on every push to `main` through `.github/workflows/pages.yml`.
