import json

from gendiff.diff_tree import DiffTree


def format_json(tree: DiffTree) -> str:
    """'json' formatter: returns the diff tree as a JSON string."""
    # ensure_ascii=False — to avoid escaping Cyrillic characters
    # indent=2 — for readability
    return json.dumps(tree, ensure_ascii=False, indent=2)
