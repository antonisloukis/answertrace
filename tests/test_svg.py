import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

from answertrace.metrics import DiscussionImpactMetrics
from answertrace.svg import render_discussion_widget


class DiscussionWidgetTests(unittest.TestCase):
    def test_widget_contains_expected_metrics(self) -> None:
        metrics = DiscussionImpactMetrics(
            accepted_answers=12,
            total_upvotes=48,
            top_community="community/community",
            first_accepted_answer=datetime(
                2026,
                5,
                14,
                tzinfo=timezone.utc,
            ),
        )

        svg = render_discussion_widget(metrics)

        self.assertIn("12", svg)
        self.assertIn("48", svg)

        # Our friendly display alias.
        self.assertIn(
            "GitHub Community",
            svg,
        )

        self.assertIn(
            "May 2026",
            svg,
        )

        self.assertIn(
            "Accepted Answers",
            svg,
        )

        self.assertIn(
            "Total Upvotes",
            svg,
        )

        self.assertIn(
            "Top Community",
            svg,
        )

        self.assertIn(
            "First Accepted",
            svg,
        )

    def test_widget_uses_default_blue_accent(self) -> None:
        metrics = DiscussionImpactMetrics(
            accepted_answers=0,
            total_upvotes=0,
            top_community=None,
            first_accepted_answer=None,
        )

        svg = render_discussion_widget(metrics)

        self.assertIn(
            "#2F81F7",
            svg,
        )

    def test_widget_is_valid_xml(self) -> None:
        metrics = DiscussionImpactMetrics(
            accepted_answers=1,
            total_upvotes=5,
            top_community="owner/repository",
            first_accepted_answer=datetime(
                2026,
                1,
                1,
                tzinfo=timezone.utc,
            ),
        )

        svg = render_discussion_widget(metrics)

        # Raises an exception if the generated SVG is malformed XML.
        ET.fromstring(svg)


if __name__ == "__main__":
    unittest.main()