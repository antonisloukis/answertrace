from html import escape
from pathlib import Path

from answertrace.metrics import DiscussionImpactMetrics


DEFAULT_ACCENT = "#2F81F7"
DEFAULT_TEXT = "#F0F6FC"
DEFAULT_MUTED = "#8B949E"
DEFAULT_ICON_BG = "#0D1117"


def _format_date(metrics: DiscussionImpactMetrics) -> str:
    if metrics.first_accepted_answer is None:
        return "—"

    return metrics.first_accepted_answer.strftime("%b %Y")


def _format_community(value: str | None) -> str:
    """
    Convert raw GitHub repository names into cleaner display names.
    """

    if not value:
        return "—"

    aliases = {
        "community/community": "GitHub Community",
    }

    return aliases.get(value, value)


def _truncate(value: str, max_length: int = 25) -> str:
    if len(value) <= max_length:
        return value

    return value[: max_length - 1] + "…"


def render_discussion_widget(
    metrics: DiscussionImpactMetrics,
    accent: str = DEFAULT_ACCENT,
    text: str = DEFAULT_TEXT,
    muted: str = DEFAULT_MUTED,
    icon_bg: str = DEFAULT_ICON_BG,
) -> str:
    accepted_answers = str(metrics.accepted_answers)
    total_upvotes = str(metrics.total_upvotes)

    formatted_community = _format_community(
        metrics.top_community
    )

    top_community = escape(
        _truncate(formatted_community)
    )

    first_accepted = escape(
        _format_date(metrics)
    )

    return f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="720"
    height="145"
    viewBox="0 0 720 145"
    role="img"
    aria-labelledby="title description"
>
    <title id="title">GitHub Discussions Impact</title>

    <desc id="description">
        GitHub Discussions contribution statistics.
    </desc>

    <defs>
        <clipPath id="octocat-clip">
            <circle cx="0" cy="0" r="24" />
        </clipPath>
    </defs>

    <style>

        .title {{
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Helvetica,
                Arial,
                sans-serif;

            font-size: 13px;
            font-weight: 500;
            fill: #58A6FF;
        }}

        .value {{
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Helvetica,
                Arial,
                sans-serif;

            font-size: 20px;
            font-weight: 600;
            fill: {text};
        }}

        .label {{
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Helvetica,
                Arial,
                sans-serif;

            font-size: 11px;
            font-weight: 400;
            fill: {muted};
        }}

        .community {{
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Helvetica,
                Arial,
                sans-serif;

            font-size: 15px;
            font-weight: 600;
            fill: {text};
        }}

    </style>


    <!-- ===================================================== -->
    <!-- TITLE -->
    <!-- ===================================================== -->

    <text
        x="20"
        y="22"
        class="title"
    >
        GitHub Discussions Impact
    </text>


    <!-- ===================================================== -->
    <!-- LEFT: ACCEPTED ANSWERS -->
    <!-- ===================================================== -->

    <text
        x="80"
        y="83"
        text-anchor="middle"
        class="value"
    >
        {accepted_answers}
    </text>

    <text
        x="80"
        y="102"
        text-anchor="middle"
        class="label"
    >
        Accepted Answers
    </text>


    <!-- ===================================================== -->
    <!-- LEFT: TOTAL UPVOTES -->
    <!-- ===================================================== -->

    <text
        x="210"
        y="83"
        text-anchor="middle"
        class="value"
    >
        {total_upvotes}
    </text>

    <text
        x="210"
        y="102"
        text-anchor="middle"
        class="label"
    >
        Total Upvotes
    </text>


    <!-- ===================================================== -->
    <!-- CENTER: GITHUB BADGE -->
    <!-- ===================================================== -->

    <g transform="translate(360 84)">

        <!-- outer blue ring -->
        <circle
            cx="0"
            cy="0"
            r="34"
            fill="none"
            stroke="{accent}"
            stroke-width="4"
        />

        <!-- inner light circle -->
        <circle
            cx="0"
            cy="0"
            r="28"
            fill="#E6EDF3"
        />

        <!-- GitHub mark clipped inside -->
        <g clip-path="url(#octocat-clip)">
            <g
                transform="translate(-23.0 -23.0) scale(2.92)"
                fill="{icon_bg}"
            >
                <path d="
                    M8 0
                    C3.58 0 0 3.58 0 8
                    c0 3.54 2.29 6.53 5.47 7.59
                    .4.07.55-.17.55-.38
                    0-.19-.01-.82-.01-1.49
                    C3.78 14.2 3.31 13.18 3.31 13.18
                    c-.36-.92-.88-1.17-.88-1.17
                    -.72-.49.05-.48.05-.48
                    .8.06 1.22.82 1.22.82
                    .71 1.21 1.87.86 2.33.66
                    .07-.52.28-.86.51-1.06
                    -1.78-.2-3.64-.89-3.64-3.95
                    0-.87.31-1.59.82-2.15
                    -.08-.2-.36-1.02.08-2.12
                    0 0 .67-.21 2.2.82
                    A7.65 7.65 0 0 1 8 4.27
                    c.68 0 1.36.09 2 .27
                    1.53-1.04 2.2-.82 2.2-.82
                    .44 1.1.16 1.92.08 2.12
                    .51.56.82 1.27.82 2.15
                    0 3.07-1.87 3.75-3.65 3.95
                    .29.25.54.73.54 1.48
                    0 1.07-.01 1.93-.01 2.2
                    0 .21.15.46.55.38
                    A8.013 8.013 0 0 0 16 8
                    c0-4.42-3.58-8-8-8
                    z
                " />
            </g>
        </g>

    </g>


    <!-- ===================================================== -->
    <!-- RIGHT: TOP COMMUNITY -->
    <!-- ===================================================== -->

    <text
        x="500"
        y="83"
        text-anchor="middle"
        class="community"
    >
        {top_community}
    </text>

    <text
        x="500"
        y="102"
        text-anchor="middle"
        class="label"
    >
        Top Community
    </text>


    <!-- ===================================================== -->
    <!-- RIGHT: FIRST ACCEPTED -->
    <!-- ===================================================== -->

    <text
        x="640"
        y="83"
        text-anchor="middle"
        class="value"
    >
        {first_accepted}
    </text>

    <text
        x="640"
        y="102"
        text-anchor="middle"
        class="label"
    >
        First Accepted
    </text>


    <!-- ===================================================== -->
    <!-- SUBTLE BOTTOM DIVIDER -->
    <!-- ===================================================== -->

    <line
        x1="20"
        y1="132"
        x2="700"
        y2="132"
        stroke="{muted}"
        stroke-width="0.5"
        opacity="0.25"
    />

</svg>
"""


def write_discussion_widget(
    metrics: DiscussionImpactMetrics,
    output: str | Path,
    accent: str = DEFAULT_ACCENT,
) -> Path:
    output_path = Path(output)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    svg = render_discussion_widget(
        metrics=metrics,
        accent=accent,
    )

    output_path.write_text(
        svg,
        encoding="utf-8",
    )

    return output_path