from pathlib import Path

import pytest

from gendiff import generate_diff

FIXTURES_DIR = Path(__file__).resolve().parent / "test_data"


def get_fixture_path(filename: str) -> Path:
    return FIXTURES_DIR / filename


def read_fixture(filename: str) -> str:
    path = get_fixture_path(filename)
    return path.read_text(encoding="utf-8").strip()


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
