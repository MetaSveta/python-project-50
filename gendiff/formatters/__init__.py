from collections.abc import Callable

from gendiff.diff_tree import DiffTree

from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

Formatter = Callable[[DiffTree], str]


def get_formatter(format_name: str | None) -> Formatter:
    """Returns a formatter function by format name."""
    name = format_name or "stylish"

    if name == "stylish":
        return format_stylish

    if name == "plain":
        return format_plain

    if name == "json":
        return format_json

    raise ValueError(f"Unsupported format: {name}")
