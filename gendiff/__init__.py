from .diff_tree import build_diff
from .formatters import get_formatter
from .parsers import parse_file


def generate_diff(
    file_path1: str,
    file_path2: str,
    format_name: str | None = "stylish",
) -> str:
    """Builds a diff between two files and returns a string.

    At this stage:
    - read and parse files (JSON/YAML) into dictionaries;
    - build an internal diff tree (build_diff);
    - format the tree with the selected formatter ('stylish' by default).
    """
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff_tree = build_diff(data1, data2)
    formatter = get_formatter(format_name)

    return formatter(diff_tree)


__all__ = ("generate_diff",)
