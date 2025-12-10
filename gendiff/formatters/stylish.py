from typing import Any

from gendiff.diff_tree import DiffTree

INDENT_SIZE = 4


def _to_str(value: Any, depth: int) -> str:
    """Casts a value to a string, taking into account
    nested dictionaries and special types."""
    if isinstance(value, dict):
        lines: list[str] = ["{"]
        indent = " " * ((depth + 1) * INDENT_SIZE)
        closing_indent = " " * (depth * INDENT_SIZE)

        for key, inner_value in value.items():
            lines.append(f"{indent}{key}: {_to_str(inner_value, depth + 1)}")

        lines.append(f"{closing_indent}}}")
        return "\n".join(lines)

    if isinstance(value, bool):
        # JSON-like representation of boolean values
        return "true" if value else "false"

    if value is None:
        return "null"

    return str(value)


def format_stylish(tree: DiffTree, depth: int = 1) -> str:
    """'stylish' formatter: returns the diff tree as a string in the 'stylish'
    style."""
    lines: list[str] = ["{"]

    for node in tree:
        key = node["key"]
        node_type = node["type"]
        indent = " " * (depth * INDENT_SIZE - 2)

        if node_type == "added":
            lines.append(f"{indent}+ {key}: {_to_str(node['value'], depth)}")
        elif node_type == "removed":
            lines.append(f"{indent}- {key}: {_to_str(node['value'], depth)}")
        elif node_type == "unchanged":
            lines.append(f"{indent}  {key}: {_to_str(node['value'], depth)}")
        elif node_type == "updated":
            lines.append(
                f"{indent}- {key}: {_to_str(node['old_value'], depth)}",
            )
            lines.append(
                f"{indent}+ {key}: {_to_str(node['new_value'], depth)}",
            )
        elif node_type == "nested":
            children = node["children"]
            children_str = format_stylish(children, depth + 1)
            lines.append(f"{indent}  {key}: {children_str}")

    closing_indent = " " * ((depth - 1) * INDENT_SIZE)
    lines.append(f"{closing_indent}}}")
    return "\n".join(lines)
