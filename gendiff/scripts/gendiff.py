import sys

from gendiff import generate_diff
from gendiff.cli_parser import build_parser
from gendiff.exceptions import GendiffError


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        diff = generate_diff(
            args.first_file,
            args.second_file,
            format_name=args.format,
        )
        print(diff)
    except GendiffError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
