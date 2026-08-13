import unittest
from datetime import datetime, timezone

from answertrace.metrics import build_discussion_impact_metrics
from answertrace.models import AcceptedAnswer, DiscussionComment


class DiscussionImpactMetricsTests(unittest.TestCase):
    def test_builds_expected_metrics(self) -> None:
        accepted_answers = [
            AcceptedAnswer(
                repository="example/repo-a",
                discussion_number=10,
                discussion_title="First question",
                discussion_url="https://github.com/example/repo-a/discussions/10",
                answer_url="https://github.com/example/repo-a/discussions/10#discussioncomment-1",
                created_at=datetime(
                    2026,
                    1,
                    3,
                    tzinfo=timezone.utc,
                ),
                answer_chosen_at=datetime(
                    2026,
                    1,
                    5,
                    tzinfo=timezone.utc,
                ),
                upvotes=4,
            ),
            AcceptedAnswer(
                repository="example/repo-b",
                discussion_number=20,
                discussion_title="Second question",
                discussion_url="https://github.com/example/repo-b/discussions/20",
                answer_url="https://github.com/example/repo-b/discussions/20#discussioncomment-2",
                created_at=datetime(
                    2026,
                    2,
                    1,
                    tzinfo=timezone.utc,
                ),
                answer_chosen_at=datetime(
                    2026,
                    2,
                    2,
                    tzinfo=timezone.utc,
                ),
                upvotes=7,
            ),
        ]

        discussion_comments = [
            DiscussionComment(
                repository="example/repo-a",
                discussion_url="https://github.com/example/repo-a/discussions/10",
                comment_url="https://github.com/example/repo-a/discussions/10#discussioncomment-1",
                created_at=datetime(
                    2026,
                    1,
                    3,
                    tzinfo=timezone.utc,
                ),
                upvotes=2,
            ),
            DiscussionComment(
                repository="example/repo-a",
                discussion_url="https://github.com/example/repo-a/discussions/10",
                comment_url="https://github.com/example/repo-a/discussions/10#discussioncomment-3",
                created_at=datetime(
                    2026,
                    1,
                    4,
                    tzinfo=timezone.utc,
                ),
                upvotes=3,
            ),
            DiscussionComment(
                repository="example/repo-a",
                discussion_url="https://github.com/example/repo-a/discussions/11",
                comment_url="https://github.com/example/repo-a/discussions/11#discussioncomment-4",
                created_at=datetime(
                    2026,
                    1,
                    6,
                    tzinfo=timezone.utc,
                ),
                upvotes=4,
            ),
            DiscussionComment(
                repository="example/repo-b",
                discussion_url="https://github.com/example/repo-b/discussions/20",
                comment_url="https://github.com/example/repo-b/discussions/20#discussioncomment-2",
                created_at=datetime(
                    2026,
                    2,
                    1,
                    tzinfo=timezone.utc,
                ),
                upvotes=10,
            ),
        ]

        metrics = build_discussion_impact_metrics(
            accepted_answers=accepted_answers,
            discussion_comments=discussion_comments,
        )

        self.assertEqual(metrics.accepted_answers, 2)

        # 2 + 3 + 4 + 10
        self.assertEqual(metrics.total_upvotes, 19)

        # repo-a has activity in 2 distinct Discussions.
        self.assertEqual(
            metrics.top_community,
            "example/repo-a",
        )

        self.assertEqual(
            metrics.first_accepted_answer,
            datetime(
                2026,
                1,
                5,
                tzinfo=timezone.utc,
            ),
        )

    def test_empty_activity_returns_empty_metrics(self) -> None:
        metrics = build_discussion_impact_metrics(
            accepted_answers=[],
            discussion_comments=[],
        )

        self.assertEqual(metrics.accepted_answers, 0)
        self.assertEqual(metrics.total_upvotes, 0)
        self.assertIsNone(metrics.top_community)
        self.assertIsNone(metrics.first_accepted_answer)


if __name__ == "__main__":
    unittest.main()