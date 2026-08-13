import json
import subprocess
from datetime import datetime
from typing import Any

from answertrace.models import AcceptedAnswer, DiscussionComment


ACCEPTED_ANSWERS_QUERY = """
query($username: String!, $cursor: String) {
  user(login: $username) {
    login

    repositoryDiscussionComments(
      first: 100
      after: $cursor
      onlyAnswers: true
    ) {
      totalCount

      pageInfo {
        hasNextPage
        endCursor
      }

      nodes {
        isAnswer
        createdAt
        url
        upvoteCount

        discussion {
          number
          title
          url
          answerChosenAt

          repository {
            nameWithOwner
          }
        }
      }
    }
  }
}
"""


ALL_DISCUSSION_COMMENTS_QUERY = """
query($username: String!, $cursor: String) {
  user(login: $username) {
    login

    repositoryDiscussionComments(
      first: 100
      after: $cursor
    ) {
      totalCount

      pageInfo {
        hasNextPage
        endCursor
      }

      nodes {
        createdAt
        url
        upvoteCount

        discussion {
          url

          repository {
            nameWithOwner
          }
        }
      }
    }
  }
}
"""


class GitHubError(Exception):
    """Raised when AnswerTrace cannot retrieve data from GitHub."""


def _parse_datetime(value: str | None) -> datetime | None:
    if value is None:
        return None

    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _run_graphql(
    query: str,
    username: str,
    cursor: str | None = None,
) -> dict[str, Any]:
    command = [
        "gh",
        "api",
        "graphql",
        "-f",
        f"query={query}",
        "-F",
        f"username={username}",
    ]

    if cursor is not None:
        command.extend(
            [
                "-F",
                f"cursor={cursor}",
            ]
        )

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise GitHubError(
            "GitHub CLI ('gh') was not found."
        ) from exc

    if result.returncode != 0:
        message = result.stderr.strip() or "Unknown GitHub API error."
        raise GitHubError(message)

    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise GitHubError(
            "GitHub returned an invalid JSON response."
        ) from exc

    if "errors" in response:
        message = response["errors"][0].get(
            "message",
            "GitHub GraphQL request failed.",
        )
        raise GitHubError(message)

    user = response.get("data", {}).get("user")

    if user is None:
        raise GitHubError(
            f"GitHub user '{username}' was not found."
        )

    return user["repositoryDiscussionComments"]


def _fetch_connection(
    query: str,
    username: str,
) -> dict[str, Any]:
    all_nodes: list[dict[str, Any]] = []
    cursor: str | None = None
    total_count = 0

    while True:
        connection = _run_graphql(
            query=query,
            username=username,
            cursor=cursor,
        )

        total_count = connection["totalCount"]

        nodes = connection.get("nodes") or []
        all_nodes.extend(nodes)

        page_info = connection["pageInfo"]

        if not page_info["hasNextPage"]:
            break

        cursor = page_info["endCursor"]

        if cursor is None:
            raise GitHubError(
                "GitHub reported another page but returned no cursor."
            )

    return {
        "totalCount": total_count,
        "nodes": all_nodes,
    }


def fetch_accepted_answers(
    username: str,
) -> dict[str, Any]:
    connection = _fetch_connection(
        query=ACCEPTED_ANSWERS_QUERY,
        username=username,
    )

    total_count = connection["totalCount"]
    all_nodes = connection["nodes"]

    answers: list[AcceptedAnswer] = []

    for node in all_nodes:
        discussion = node["discussion"]
        repository = discussion["repository"]

        created_at = _parse_datetime(node["createdAt"])

        if created_at is None:
            raise GitHubError(
                "Accepted answer was missing its creation date."
            )

        answers.append(
            AcceptedAnswer(
                repository=repository["nameWithOwner"],
                discussion_number=discussion["number"],
                discussion_title=discussion["title"],
                discussion_url=discussion["url"],
                answer_url=node["url"],
                created_at=created_at,
                answer_chosen_at=_parse_datetime(
                    discussion["answerChosenAt"]
                ),
                upvotes=node["upvoteCount"],
            )
        )

    return {
        "totalCount": total_count,
        "answers": answers,
    }


def fetch_discussion_comments(
    username: str,
) -> dict[str, Any]:
    connection = _fetch_connection(
        query=ALL_DISCUSSION_COMMENTS_QUERY,
        username=username,
    )

    total_count = connection["totalCount"]
    all_nodes = connection["nodes"]

    comments: list[DiscussionComment] = []

    for node in all_nodes:
        discussion = node["discussion"]
        repository = discussion["repository"]

        created_at = _parse_datetime(node["createdAt"])

        if created_at is None:
            raise GitHubError(
                "Discussion comment was missing its creation date."
            )

        comments.append(
            DiscussionComment(
                repository=repository["nameWithOwner"],
                discussion_url=discussion["url"],
                comment_url=node["url"],
                created_at=created_at,
                upvotes=node["upvoteCount"],
            )
        )

    return {
        "totalCount": total_count,
        "comments": comments,
    }