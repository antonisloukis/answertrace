from html import escape
from pathlib import Path

from answertrace.metrics import DiscussionImpactMetrics


DEFAULT_ACCENT = "#58A6FF"
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

    formatted_community = _format_community(metrics.top_community)
    top_community = escape(_truncate(formatted_community))
    first_accepted = escape(_format_date(metrics))

    return f"""<svg
    xmlns="http://www.w3.org/2000/svg"
    width="720"
    height="190"
    viewBox="0 0 720 190"
    role="img"
    aria-labelledby="title description"
>
    <title id="title">GitHub Discussions Impact</title>

    <desc id="description">
        GitHub Discussions contribution statistics.
    </desc>

    <defs>
        <clipPath id="octocat-inner-clip">
            <circle cx="0" cy="0" r="24.5" />
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
            font-size: 15px;
            font-weight: 500;
            fill: {accent};
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
            font-weight: 500;
            fill: {text};
        }}
    </style>

    <!-- MOVE ENTIRE WIDGET DOWN -->
    <g transform="translate(0 30)">

    <!-- TITLE -->
    <text
        x="20"
        y="26"
        class="title"
    >
        GitHub Discussions Impact
    </text>

    <!-- LEFT: ACCEPTED ANSWERS -->
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

    <!-- LEFT: TOTAL UPVOTES -->
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

    <!-- CENTER: GITHUB BADGE -->
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

                <!-- dark backing for transparent Octocat cutout -->
        <circle
            cx="0"
            cy="0"
            r="28"
            fill="{icon_bg}"
        />

        <!-- GitHub silhouette traced from the new transparent icon -->
        <path
            d="
                M 181 17
                L 133 37
                L 93 64
                L 58 99
                L 32 137
                L 11 186
                L 1 235
                L 1 288
                L 11 337
                L 20 362
                L 37 395
                L 60 427
                L 79 447
                L 104 468
                L 136 488
                L 173 504
                L 179 505
                L 188 502
                L 192 493
                L 191 445
                L 176 448
                L 151 448
                L 137 445
                L 124 439
                L 112 428
                L 91 390
                L 67 368
                L 69 363
                L 76 361
                L 94 364
                L 116 383
                L 132 404
                L 145 412
                L 156 415
                L 172 415
                L 192 409
                L 198 389
                L 208 376
                L 167 367
                L 138 353
                L 115 331
                L 102 308
                L 98 296
                L 93 268
                L 93 234
                L 100 208
                L 118 180
                L 114 161
                L 114 137
                L 121 112
                L 134 111
                L 153 116
                L 191 137
                L 239 129
                L 273 129
                L 321 137
                L 359 116
                L 378 111
                L 390 111
                L 395 122
                L 399 145
                L 399 157
                L 394 180
                L 411 205
                L 419 232
                L 419 271
                L 414 297
                L 409 311
                L 398 330
                L 374 353
                L 345 367
                L 304 375
                L 315 391
                L 320 410
                L 320 495
                L 325 503
                L 338 504
                L 379 486
                L 421 457
                L 451 427
                L 482 381
                L 500 337
                L 510 287
                L 510 235
                L 500 186
                L 479 137
                L 453 99
                L 418 64
                L 378 37
                L 330 17
                L 279 7
                L 232 7
                Z
            "
            transform="translate(-28 -28) scale(0.109375)"
            fill="#E6EDF3"
        />
    </g>

    <!-- RIGHT: TOP COMMUNITY -->
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

    <!-- RIGHT: FIRST ACCEPTED -->
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

    <!-- SUBTLE BOTTOM DIVIDER -->
    <line
        x1="20"
        y1="155"
        x2="700"
        y2="155"
        stroke="{muted}"
        stroke-width="0.5"
        opacity="0.25"
    />

    </g>

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