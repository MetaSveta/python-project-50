from pathlib import Path

from gendiff import generate_diff

FIXTURES_DIR = Path(__file__).resolve().parent / "test_data"


def get_fixture_path(filename: str) -> Path:
    return FIXTURES_DIR / filename


def read_fixture(filename: str) -> str:
    path = get_fixture_path(filename)
    # strip() убирает возможный завершающий перевод строки,
    # чтобы формат строки совпадал с тем, что возвращает generate_diff
    return path.read_text(encoding="utf-8").strip()


def test_generate_diff_flat_json() -> None:
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected = read_fixture("expected_flat.txt")

    result = generate_diff(str(file1), str(file2))

    assert result == expected
