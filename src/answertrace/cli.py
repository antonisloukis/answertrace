import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="answertrace",
        description="Analyze GitHub Discussion contributions.",
    )

    parser.add_argument(
        "username",
        nargs="?",
        help="GitHub username to analyze",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="AnswerTrace 0.1.0",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.username:
        parser.print_help()
        return

    print(f"Analyzing GitHub Discussions for @{args.username}...")


if __name__ == "__main__":
    main()