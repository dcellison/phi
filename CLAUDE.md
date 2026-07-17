# Working instructions for Claude (and other AI tools)

You are working on Phi, a constructed language and Daniel Ellison's long-term project. The development rules are project documentation, not tool configuration — read and follow them exactly:

@project/development_protocol.md

For the exact continuation state after pull request #418, including utility commands and the active vocabulary workflow, read:

@project/handoff/README.md

Authority order when documents disagree: `canon.md`. Settled decisions there are never reopened silently.

## Repository working rules

- All work happens on branches, opened as pull requests; the owner reviews and merges every PR himself. Never commit to main.
- Run `python3 scripts/validate_examples.py` as a standalone command (never piped, so the exit code is visible) before any commit that touches vocabulary or documentation. Zero errors is the bar.
- After vocabulary changes, regenerate derived artifacts: `python3 scripts/generate_reference.py` and `python3 scripts/build_site.py`.
- No AI attribution anywhere: no "Generated with" footers in PRs, no Co-Authored-By trailers in commits. Contributors are not singled out.
- Self-generated filenames are lowercase snake_case; `README.md`, `CLAUDE.md`, and license files are the only exceptions.
- Markdown paragraphs are single lines — never hard-wrap prose; renderers break on it.
- Every directory outside `archive/` holds only current, in-use material. When work completes, archive its records in the same PR, with a catalogue row in `archive/README.md`.
- Work only within this repository's directories.
