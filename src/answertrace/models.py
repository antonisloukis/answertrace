from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class AcceptedAnswer:
    repository: str
    discussion_number: int
    discussion_title: str
    discussion_url: str
    answer_url: str
    created_at: datetime
    answer_chosen_at: datetime | None
    upvotes: int


@dataclass(frozen=True)
class DiscussionComment:
    repository: str
    discussion_url: str
    comment_url: str
    created_at: datetime
    upvotes: int