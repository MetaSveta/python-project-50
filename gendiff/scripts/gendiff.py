import argparse
import json


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
    parser.parse_args()  # Parse arguments. No logic yet.
    args = parser.parse_args()

    with open(args.first_file) as first:
        first_data = json.load(first)

    with open(args.second_file) as second:
        second_data = json.load(second)


if __name__ == "__main__":
    main()
