import json
from pathlib import Path

import pytest

from gendiff import generate_diff

FIXTURES_DIR = Path(__file__).resolve().parent / "test_data"


def get_fixture_path(filename: str) -> Path:
    return FIXTURES_DIR / filename


def read_fixture(filename: str) -> str:
    path = get_fixture_path(filename)
    return path.read_text(encoding="utf-8").rstrip("\n")


@pytest.mark.parametrize(
    ("file1_name", "file2_name"),
    [
        ("file1.json", "file2.json"),
        ("file1.yml", "file2.yml"),
    ],
)
def test_generate_diff_flat(file1_name: str, file2_name: str) -> None:
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    expected = read_fixture("expected_flat.txt")

    result = generate_diff(str(file1), str(file2))

    assert result == expected


@pytest.mark.parametrize(
    ("file1_name", "file2_name"),
    [
        ("file1_nested.json", "file2_nested.json"),
        ("file1_nested.yml", "file2_nested.yml"),
    ],
)
def test_generate_diff_nested_stylish(file1_name: str, file2_name: str) -> None:
    """Checking the correct comparison of nested JSON/YAML structures
    in 'stylish' format."""
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    expected = read_fixture("expected_nested_stylish.txt")

    result = generate_diff(str(file1), str(file2))

    assert result == expected


@pytest.mark.parametrize(
    ("file1_name", "file2_name"),
    [
        ("file1_nested.json", "file2_nested.json"),
        ("file1_nested.yml", "file2_nested.yml"),
    ],
)
def test_generate_diff_nested_plain(file1_name: str, file2_name: str) -> None:
    """Checking the correct comparison of nested JSON/YAML structures
    in 'plain' format."""
    file1 = get_fixture_path(file1_name)
    file2 = get_fixture_path(file2_name)
    expected = read_fixture("expected_nested_plain.txt")

    result = generate_diff(str(file1), str(file2), "plain")

    assert result == expected

    @pytest.mark.parametrize(
        ("file1_name", "file2_name"),
        [
            ("file1_nested.json", "file2_nested.json"),
            ("file1_nested.yml", "file2_nested.yml"),
        ],
    )
    def test_generate_diff_json(file1_name: str, file2_name: str) -> None:
        """Checking 'json' format for nested JSON/YAML structures."""
        file1 = get_fixture_path(file1_name)
        file2 = get_fixture_path(file2_name)

        result = generate_diff(str(file1), str(file2), "json")
        actual = json.loads(result)

        expected_raw = read_fixture("expected_nested_json.json")
        expected = json.loads(expected_raw)

        assert actual == expected
