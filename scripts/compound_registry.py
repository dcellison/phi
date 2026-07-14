#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Parse the compound registry (documents/reference/compounds.md).

The registry's markdown tables are the single source of truth for
canonized compound idioms. The validator, the reference generator, and
the explorer build all read the registry through this one parser, so
the three surfaces can never disagree about what it says.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
REGISTRY_FILE = PROJECT_ROOT / "documents" / "reference" / "compounds.md"

ROW = re.compile(r"^\| `([^`]+)` \| (.+?) \| (.+?) \| (.+?) \|$")


def compound_tokens(compound):
    """The Phi words inside a compound, bracket notation stripped.

    Brackets mark an embedded clause for the reader (`theula [rena
    lima nai]`); they are display, not words.
    """
    return compound.replace("[", " ").replace("]", " ").split()


def load_compounds(path=REGISTRY_FILE):
    """Return the registry's rows as dicts, in file order."""
    compounds = []
    section = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        match = ROW.match(line)
        if not match or section is None:
            continue
        compound, literal, meaning, why = (g.strip() for g in match.groups())
        compounds.append({
            "compound": compound,
            "tokens": compound_tokens(compound),
            "literal": literal,
            "meaning": meaning,
            "why": why,
            "section": section,
        })
    return compounds
