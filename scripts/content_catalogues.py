"""Load and validate the ordered catalogues for Phi's reading shelves."""

import json
from pathlib import Path


TEXT_METHODS = {
    "Translation",
    "Transmutation",
    "Translation + transmutation",
}


class CatalogueError(ValueError):
    """A content catalogue does not match its schema or source directory."""

    def __init__(self, errors):
        self.errors = tuple(errors)
        super().__init__("\n".join(self.errors))


def _load_entries(root, relative_path, collection_key):
    path = root / relative_path
    label = path.relative_to(root).as_posix()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogueError([f"{label}: could not load catalogue: {exc}"]) from exc
    if not isinstance(data, dict) or set(data) != {collection_key}:
        raise CatalogueError(
            [f"{label}: top-level object must contain only '{collection_key}'"]
        )
    entries = data[collection_key]
    if not isinstance(entries, list) or not entries:
        raise CatalogueError([f"{label}: '{collection_key}' must be a nonempty list"])
    return label, entries


def _check_entry_shape(entry, index, required_fields, label):
    prefix = f"{label}: entry {index}"
    if not isinstance(entry, dict):
        return [f"{prefix} must be an object"]
    fields = set(entry)
    errors = []
    missing = required_fields - fields
    extra = fields - required_fields
    if missing:
        errors.append(f"{prefix} is missing: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"{prefix} has unknown fields: {', '.join(sorted(extra))}")
    return errors


def _check_shelf_members(label, listed, expected):
    errors = []
    missing = expected - listed
    extra = listed - expected
    if missing:
        errors.append(f"{label}: uncatalogued content: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"{label}: entries without content: {', '.join(sorted(extra))}")
    return errors


def load_text_catalogue(root):
    """Load the ordered text shelf and reject schema or directory drift."""
    label, entries = _load_entries(root, Path("texts/catalogue.json"), "works")
    required = {"path", "kind", "title", "method", "summary"}
    errors = []
    listed = set()
    texts_dir = root / "texts"

    for index, entry in enumerate(entries, 1):
        shape_errors = _check_entry_shape(entry, index, required, label)
        errors.extend(shape_errors)
        if shape_errors:
            continue
        prefix = f"{label}: entry {index}"
        for field in ("path", "kind", "title", "method", "summary"):
            if not isinstance(entry[field], str) or not entry[field].strip():
                errors.append(f"{prefix}: '{field}' must be a nonempty string")
        if not isinstance(entry["path"], str) or not entry["path"].strip():
            continue
        content_path = entry["path"]
        if content_path in listed:
            errors.append(f"{prefix}: duplicate path '{content_path}'")
        listed.add(content_path)
        kind = entry["kind"]
        if isinstance(kind, str):
            if kind not in {"short", "book"}:
                errors.append(f"{prefix}: kind must be 'short' or 'book'")
            elif kind == "short":
                if Path(content_path).name != content_path or not content_path.endswith(".md"):
                    errors.append(
                        f"{prefix}: short-work path must be a top-level Markdown file"
                    )
                elif not (texts_dir / content_path).is_file():
                    errors.append(f"{prefix}: missing short work '{content_path}'")
            else:
                if Path(content_path).name != content_path:
                    errors.append(
                        f"{prefix}: book path must be one top-level directory name"
                    )
                elif not (texts_dir / content_path / "README.md").is_file():
                    errors.append(f"{prefix}: book '{content_path}' has no README.md")
        if isinstance(entry["method"], str) and entry["method"] not in TEXT_METHODS:
            errors.append(f"{prefix}: unknown method '{entry['method']}'")

    expected = {
        path.name
        for path in texts_dir.glob("*.md")
        if path.name != "README.md"
    }
    expected.update(
        path.name
        for path in texts_dir.iterdir()
        if path.is_dir() and (path / "README.md").is_file()
    )
    errors.extend(_check_shelf_members(label, listed, expected))
    if errors:
        raise CatalogueError(errors)
    return entries


def load_pamphlet_catalogue(root):
    """Load the ordered pamphlet shelf and reject schema or directory drift."""
    label, entries = _load_entries(
        root, Path("pamphlets/catalogue.json"), "pamphlets"
    )
    required = {"directory", "title", "summary", "dual_script"}
    errors = []
    listed = set()
    pamphlets_dir = root / "pamphlets"

    for index, entry in enumerate(entries, 1):
        shape_errors = _check_entry_shape(entry, index, required, label)
        errors.extend(shape_errors)
        if shape_errors:
            continue
        prefix = f"{label}: entry {index}"
        for field in ("directory", "title", "summary"):
            if not isinstance(entry[field], str) or not entry[field].strip():
                errors.append(f"{prefix}: '{field}' must be a nonempty string")
        if not isinstance(entry["dual_script"], bool):
            errors.append(f"{prefix}: 'dual_script' must be true or false")
        if not isinstance(entry["directory"], str) or not entry["directory"].strip():
            continue
        directory = entry["directory"]
        if directory in listed:
            errors.append(f"{prefix}: duplicate directory '{directory}'")
        listed.add(directory)
        if Path(directory).name != directory:
            errors.append(f"{prefix}: directory must be one top-level directory name")
        elif not (pamphlets_dir / directory / "00_title.md").is_file():
            errors.append(f"{prefix}: '{directory}' has no 00_title.md")

    expected = {
        path.name
        for path in pamphlets_dir.iterdir()
        if path.is_dir()
    }
    errors.extend(_check_shelf_members(label, listed, expected))
    if errors:
        raise CatalogueError(errors)
    return entries
