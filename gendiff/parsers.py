import json
from pathlib import Path
from typing import Any

import yaml


def parse(file_path: str) -> dict[str, Any]:
    """Reads a file and returns the data as a dictionary.

    The format is determined by the file extension:
    - .json  → JSON
    - .yml/.yaml → YAML
    """
    ext = Path(file_path).suffix.lower()

    with open(file_path) as file:
        if ext == ".json":
            return json.load(file)
        if ext in {".yml", ".yaml"}:
            # safe_load returns dict или None
            data = yaml.safe_load(file)
            return data or {}

    raise ValueError(f"Unsupported file format: {ext}")
