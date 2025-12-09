from collections.abc import Callable

from gendiff.diff_tree import DiffTree

from .stylish import format_stylish

Formatter = Callable[[DiffTree], str]


def get_formatter(format_name: str | None) -> Formatter:
    """Returns a formatter function by format name.

    Currently only 'stylish' is supported.
    """
    name = format_name or "stylish"

    if name == "stylish":
        return format_stylish

    raise ValueError(f"Unsupported format: {name}")
