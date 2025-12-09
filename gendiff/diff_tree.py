from typing import Any

DiffNode = dict[str, Any]
DiffTree = list[DiffNode]


def build_diff(data1: dict[str, Any], data2: dict[str, Any]) -> DiffTree:
    """Строит внутреннее дерево различий между двумя словарями.

    Каждый узел описывает один ключ и содержит:
    - key: имя ключа
    - type: тип изменения:
        "added"    — ключ есть только во втором словаре
        "removed"  — ключ есть только в первом словаре
        "unchanged"— значение одинаковое в обоих словарях
        "updated"  — значение изменилось
        "nested"   — значения в обоих словарях — словари, есть дети (children)
    Дополнительно используются поля:
    - value      — значение для added/removed/unchanged
    - old_value  — старое значение для updated
    - new_value  — новое значение для updated
    - children   — список дочерних узлов для nested
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    nodes: DiffTree = []

    for key in keys:
        in_first = key in data1
        in_second = key in data2
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Оба значения — словари → строим вложенное дерево
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

        # Ключ есть только в первом словаре
        if in_first and not in_second:
            nodes.append(
                {
                    "key": key,
                    "type": "removed",
                    "value": value1,
                }
            )
            continue

        # Ключ есть только во втором словаре
        if not in_first and in_second:
            nodes.append(
                {
                    "key": key,
                    "type": "added",
                    "value": value2,
                }
            )
            continue

        # Ключ есть в обоих словарях
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