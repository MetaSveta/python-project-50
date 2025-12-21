from typing import Any

from gendiff.diff_tree import DiffTree


def _format_value(value: Any) -> str:
    """Formats a value according to the requirements of the plain format."""
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, bool):
        return "true" if value else "false"

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def _walk(tree: DiffTree, path_prefix: str = "") -> list[str]:
    """Traverses a diff tree and produces lines in 'plain' format."""
    lines: list[str] = []

    for node in tree:
        key = node["key"]
        node_type = node["type"]

        # build a path
        property_path = (
            f"{path_prefix}{key}" if not path_prefix else f"{path_prefix}.{key}"
        )

        if node_type == "nested":
            # nested nodes are not output, only their children
            children = node["children"]
            lines.extend(_walk(children, property_path))
            continue

        if node_type == "added":
            value = _format_value(node["value"])
            lines.append(
                f"Property '{property_path}' was added with value: {value}",
            )
            continue

        if node_type == "removed":
            lines.append(
                f"Property '{property_path}' was removed",
            )
            continue

        if node_type == "updated":
            old_value = _format_value(node["old_value"])
            new_value = _format_value(node["new_value"])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_value} to {new_value}",
            )
            continue

        if node_type == "unchanged":
            # in 'plain' format, unchanged properties are not displayed
            continue

        raise ValueError(f"Unknown node type: {node_type}")

    return lines


def format_plain(tree: DiffTree) -> str:
    """'plain' formatter: returns the diff tree as a string in the 'plain'
    style."""
    lines = _walk(tree)
    return "\n".join(lines)
