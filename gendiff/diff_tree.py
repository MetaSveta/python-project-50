from typing import Any

DiffNode = dict[str, Any]
DiffTree = list[DiffNode]


def build_diff(data1: dict[str, Any], data2: dict[str, Any]) -> DiffTree:
    """Builds an internal tree of differences between two dictionaries.

    Each node describes a single key and contains:
    - key: a key name
    - type: type of change:
        "added"    — a key is only in the second dictionary
        "removed"  — a key is only in the first dictionary
        "unchanged"— values are the same in both dictionaries
        "updated"  — a value has changed
        "nested"   — values in both dictionaries are dictionaries,
        there are "children"
    Additionally, the following fields are used:
    - value      — a value for "added"/"removed"/"unchanged"
    - old_value  — an old value for "updated"
    - new_value  — a new value for "updated"
    - children   — a list of child nodes for "nested"
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    nodes: DiffTree = []

    for key in keys:
        in_first = key in data1
        in_second = key in data2
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Both values are dictionaries → build a nested tree
        both_dicts = (
            in_first
            and in_second
            and isinstance(value1, dict)
            and isinstance(value2, dict)
        )

        if both_dicts:
            children = build_diff(value1, value2)
            nodes.append(
                {
                    "key": key,
                    "type": "nested",
                    "children": children,
                }
            )
            continue

        # A key is only in the first dictionary
        if in_first and not in_second:
            nodes.append(
                {
                    "key": key,
                    "type": "removed",
                    "value": value1,
                }
            )
            continue

        # A key is only in the second dictionary
        if not in_first and in_second:
            nodes.append(
                {
                    "key": key,
                    "type": "added",
                    "value": value2,
                }
            )
            continue

        # A key is in both dictionaries
        if value1 == value2:
            nodes.append(
                {
                    "key": key,
                    "type": "unchanged",
                    "value": value1,
                }
            )
        else:
            nodes.append(
                {
                    "key": key,
                    "type": "updated",
                    "old_value": value1,
                    "new_value": value2,
                }
            )

    return nodes
