import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
    )
    return parser


def main() -> None:
    parser = build_parser()
    parser.parse_args()  # пока просто разбираем аргументы, логики ещё нет


if __name__ == "__main__":
    main()
