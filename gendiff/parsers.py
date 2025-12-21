import json
from pathlib import Path
from typing import Any

import yaml

from gendiff.exceptions import UnsupportedFormatError


def read_file(file_path: str) -> str:
    """Reads a file from disk and returns its content as a UTF-8 string."""
    return Path(file_path).read_text(encoding="utf-8")


# side effect: interacts with the filesystem


def parse(content: str, ext: str) -> dict[str, Any]:
    """Parses content string into a dictionary based on file extension.

    Supported formats:
    - .json  → JSON
    - .yml/.yaml → YAML
    """
    if ext == ".json":
        return json.loads(content)

    if ext in {".yml", ".yaml"}:
        # safe_load may return dict, list, scalar, or None;
        # for this project we expect dict
        data = yaml.safe_load(content)
        return data or {}

    raise UnsupportedFormatError(f"Unsupported file format: {ext}")


def parse_file(file_path: str) -> dict[str, Any]:
    """Reads and parses a file into a dictionary."""
    ext = Path(file_path).suffix.lower()
    content = read_file(file_path)
    return parse(content, ext)
