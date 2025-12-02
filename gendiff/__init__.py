import json


def generate_diff(file_path1: str, file_path2: str) -> str:
    # read file1
    with open(file_path1) as file1:
        data1 = json.load(file1)

    # read file2
    with open(file_path2) as file2:
        data2 = json.load(file2)

    # collect sorted keys
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result_lines = ["{"]

    for key in keys:
        in_first = key in data1
        in_second = key in data2

        # key is only in file1 (removed in file2)
        if in_first and not in_second:
            result_lines.append(f"  - {key}: {data1[key]}")
            continue

        # key is only in file2 (add in file2)
        if not in_first and in_second:
            result_lines.append(f"  + {key}: {data2[key]}")
            continue

        # key in file1 and file2
        old_value = data1[key]
        new_value = data2[key]

        # value hasn't changed
        if old_value == new_value:
            result_lines.append(f"    {key}: {old_value}")
        else:
            # value has changed
            result_lines.append(f"  - {key}: {old_value}")
            result_lines.append(f"  + {key}: {new_value}")

    result_lines.append("}")
    return "\n".join(result_lines)


__all__ = ("generate_diff",)
