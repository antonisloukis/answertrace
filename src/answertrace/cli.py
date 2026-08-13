import argparse
from datetime import datetime

from answertrace.github import (
    GitHubError,
    fetch_accepted_answers,
    fetch_discussion_comments,
)
from answertrace.metrics import build_discussion_impact_metrics


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


def format_date(value: datetime | None) -> str:
    if value is None:
        return "N/A"

    return value.strftime("%b %Y")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.username:
        parser.print_help()
        return

    print(f"Analyzing GitHub Discussions for @{args.username}...")

    try:
        accepted_result = fetch_accepted_answers(args.username)
        comments_result = fetch_discussion_comments(args.username)

        metrics = build_discussion_impact_metrics(
            accepted_answers=accepted_result["answers"],
            discussion_comments=comments_result["comments"],
        )

    except GitHubError as exc:
        print(f"Error: {exc}")
        return

    print()
    print("GitHub Discussions Impact")
    print("-" * 28)
    print(f"Accepted Answers:     {metrics.accepted_answers}")
    print(f"Total Upvotes:        {metrics.total_upvotes}")
    print(f"Top Community:        {metrics.top_community or 'N/A'}")
    print(
        f"First Accepted:       {format_date(metrics.first_accepted_answer)}"
    )


if __name__ == "__main__":
    main()