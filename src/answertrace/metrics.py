from collections import Counter
from dataclasses import dataclass
from datetime import datetime

from answertrace.models import AcceptedAnswer, DiscussionComment


@dataclass(frozen=True)
class DiscussionImpactMetrics:
    accepted_answers: int
    total_upvotes: int
    top_community: str | None
    first_accepted_answer: datetime | None


def build_discussion_impact_metrics(
    accepted_answers: list[AcceptedAnswer],
    discussion_comments: list[DiscussionComment],
) -> DiscussionImpactMetrics:
    accepted_answers_count = len(accepted_answers)

    # Total upvotes received across ALL Discussion comments.
    total_upvotes = sum(
        comment.upvotes
        for comment in discussion_comments
    )

    # Count distinct Discussions per repository.
    unique_discussions = {
        (comment.repository, comment.discussion_url)
        for comment in discussion_comments
    }

    repo_counter = Counter(
        repository
        for repository, _ in unique_discussions
    )

    if repo_counter:
        top_community = sorted(
            repo_counter.items(),
            key=lambda item: (-item[1], item[0].lower()),
        )[0][0]
    else:
        top_community = None

    accepted_dates = [
        answer.answer_chosen_at or answer.created_at
        for answer in accepted_answers
    ]

    first_accepted_answer = (
        min(accepted_dates)
        if accepted_dates
        else None
    )

    return DiscussionImpactMetrics(
        accepted_answers=accepted_answers_count,
        total_upvotes=total_upvotes,
        top_community=top_community,
        first_accepted_answer=first_accepted_answer,
    )