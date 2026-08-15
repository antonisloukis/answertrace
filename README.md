# AnswerTrace

<a href="https://github.com/marketplace/actions/answertrace">
  <img
    src="./assets/marketplace-badge.svg"
    width="230"
    alt="Available on GitHub Marketplace"
  />
</a>

GitHub Discussions contribution analytics and customizable SVG widgets for developer READMEs.

AnswerTrace analyzes public GitHub Discussions activity and turns it into a lightweight, automatically updated profile widget.

Built with **Python**, the **GitHub GraphQL API**, and **GitHub Actions**.

<p align="center">
  <img
    src="./assets/discussion-impact.svg"
    alt="AnswerTrace GitHub Discussions Impact widget"
    width="720"
  />
</p>

---

## What AnswerTrace Tracks

AnswerTrace currently measures:

- **Accepted Answers** — Discussion replies selected as the accepted answer.
- **Total Upvotes** — Total upvotes received across your GitHub Discussion comments.
- **Top Community** — Repository where you participated in the most distinct Discussions.
- **First Accepted** — Date of your earliest accepted Discussion answer.

The generated widget can be placed directly inside a GitHub profile README or repository README.

---

# Quick Start

The recommended setup uses **GitHub Actions** so your AnswerTrace widget updates automatically.

You only need to set it up once.

## Step 1 — Create an `assets` folder

Inside the repository where you want to display AnswerTrace, create:

```text
assets/
```

AnswerTrace will generate:

```text
assets/discussion-impact.svg
```

inside this directory.

For a GitHub profile README, this will normally be inside your special profile repository:

```text
YOUR_USERNAME/YOUR_USERNAME
```

Example:

```text
antonisloukis/antonisloukis
```

---

## Step 2 — Create a GitHub token

AnswerTrace needs a GitHub token so it can query GitHub Discussions through the GitHub API.

Create a GitHub token with the minimum read access required for the Discussion activity you want AnswerTrace to analyze.

Do **not** place the token directly inside your workflow or README.

---

## Step 3 — Save the token as a GitHub Actions secret

Open the repository where AnswerTrace will run.

Go to:

```text
Settings
→ Secrets and variables
→ Actions
→ New repository secret
```

Create this secret:

```text
Name:
ANSWERTRACE_TOKEN
```

Paste your GitHub token into the secret value.

Your workflow will reference it securely as:

```yaml
${{ secrets.ANSWERTRACE_TOKEN }}
```

---

## Step 4 — Create the AnswerTrace workflow

Create this file:

```text
.github/workflows/answertrace.yml
```

Paste the following workflow:

```yaml
name: Update AnswerTrace

on:
  workflow_dispatch:

  schedule:
    - cron: "17 4 * * *"

permissions:
  contents: write

jobs:
  answertrace:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v7

      - name: Generate AnswerTrace widget
        uses: antonisloukis/answertrace@v1
        with:
          username: YOUR_GITHUB_USERNAME
          token: ${{ secrets.ANSWERTRACE_TOKEN }}
          output: assets/discussion-impact.svg
          accent: "#58A6FF"

      - name: Commit updated widget
        shell: bash
        run: |
          if git diff --quiet -- assets/discussion-impact.svg; then
            echo "AnswerTrace widget is already up to date."
            exit 0
          fi

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add assets/discussion-impact.svg
          git commit -m "chore: update AnswerTrace widget"
          git push
```

Replace:

```text
YOUR_GITHUB_USERNAME
```

with your GitHub username.

For example:

```yaml
username: antonisloukis
```

---

## Step 5 — Run AnswerTrace for the first time

Open your repository on GitHub.

Go to:

```text
Actions
→ Update AnswerTrace
→ Run workflow
```

Once the workflow finishes successfully, you should have:

```text
assets/discussion-impact.svg
```

inside your repository.

---

## Step 6 — Add the widget to your README

Paste this wherever you want AnswerTrace to appear:

```html
<p align="center">
  <img
    src="./assets/discussion-impact.svg"
    alt="GitHub Discussions Impact"
    width="720"
  />
</p>
```

Commit the README.

Your AnswerTrace widget is now live.

---

# Automatic Updates

The workflow above includes:

```yaml
schedule:
  - cron: "17 4 * * *"
```

This allows GitHub Actions to periodically regenerate the widget.

The workflow:

```text
GitHub Discussions
        ↓
AnswerTrace
        ↓
Generate SVG
        ↓
Detect changes
        ↓
Commit updated widget
        ↓
README displays new metrics
```

You can also run the workflow manually at any time through:

```text
Actions
→ Update AnswerTrace
→ Run workflow
```

---

# Examples

## Example 1 — Minimal GitHub Action

If you only want AnswerTrace to generate the SVG and do not need the complete scheduled workflow:

```yaml
- name: Generate AnswerTrace widget
  uses: antonisloukis/answertrace@v1
  with:
    username: YOUR_GITHUB_USERNAME
    token: ${{ secrets.ANSWERTRACE_TOKEN }}
```

The default output location is:

```text
assets/discussion-impact.svg
```

---

## Example 2 — Custom Output Path

You can choose where AnswerTrace writes the generated SVG:

```yaml
- name: Generate AnswerTrace widget
  uses: antonisloukis/answertrace@v1
  with:
    username: YOUR_GITHUB_USERNAME
    token: ${{ secrets.ANSWERTRACE_TOKEN }}
    output: profile/answertrace.svg
```

Then display it using:

```html
<img
  src="./profile/answertrace.svg"
  alt="GitHub Discussions Impact"
/>
```

---

## Example 3 — Custom Accent Color

AnswerTrace supports custom hexadecimal accent colors.

```yaml
- name: Generate AnswerTrace widget
  uses: antonisloukis/answertrace@v1
  with:
    username: YOUR_GITHUB_USERNAME
    token: ${{ secrets.ANSWERTRACE_TOKEN }}
    output: assets/discussion-impact.svg
    accent: "#A371F7"
```

Some examples:

```text
AnswerTrace Blue  #58A6FF
Purple            #A371F7
Green             #3FB950
Orange            #D29922
Red                #F85149
```

---

## Example 4 — Complete Profile README Setup

A typical profile repository can look like this:

```text
YOUR_USERNAME/
├── .github/
│   └── workflows/
│       └── answertrace.yml
│
├── assets/
│   └── discussion-impact.svg
│
└── README.md
```

Your workflow:

```yaml
name: Update AnswerTrace

on:
  workflow_dispatch:

  schedule:
    - cron: "17 4 * * *"

permissions:
  contents: write

jobs:
  answertrace:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout profile repository
        uses: actions/checkout@v7

      - name: Generate AnswerTrace widget
        uses: antonisloukis/answertrace@v1
        with:
          username: YOUR_GITHUB_USERNAME
          token: ${{ secrets.ANSWERTRACE_TOKEN }}
          output: assets/discussion-impact.svg
          accent: "#58A6FF"

      - name: Commit updated widget
        shell: bash
        run: |
          if git diff --quiet -- assets/discussion-impact.svg; then
            echo "AnswerTrace widget is already up to date."
            exit 0
          fi

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add assets/discussion-impact.svg
          git commit -m "chore: update AnswerTrace widget"
          git push
```

Your README:

```html
### Development Metrics

<p align="center">
  <img
    src="./assets/discussion-impact.svg"
    alt="GitHub Discussions Impact"
    width="720"
  />
</p>
```

---

## Live Example

AnswerTrace is used on the creator's GitHub profile README:

[github.com/antonisloukis](https://github.com/antonisloukis)

The widget is generated automatically through GitHub Actions and refreshed as GitHub Discussions activity changes.

---

# CLI Usage

AnswerTrace can also be used locally from the command line.

## Analyze a GitHub user

```bash
answertrace USERNAME
```

Example:

```bash
answertrace antonisloukis
```

---

## Generate an SVG

```bash
answertrace antonisloukis --svg
```

---

## Choose an output path

```bash
answertrace antonisloukis \
  --svg \
  --output assets/discussion-impact.svg
```

---

## Change the accent color

```bash
answertrace antonisloukis \
  --svg \
  --accent "#58A6FF"
```

---

# GitHub Action Inputs

AnswerTrace supports the following inputs.

### `username`

GitHub username whose Discussion activity will be analyzed.

Required:

```yaml
username: YOUR_GITHUB_USERNAME
```

---

### `token`

GitHub token used to query Discussion activity.

Required:

```yaml
token: ${{ secrets.ANSWERTRACE_TOKEN }}
```

Never hard-code your token.

---

### `output`

Location where the generated SVG will be written.

Optional.

Default:

```text
assets/discussion-impact.svg
```

Example:

```yaml
output: assets/discussion-impact.svg
```

---

### `accent`

Accent color used by the widget.

Optional.

Default:

```text
#58A6FF
```

Example:

```yaml
accent: "#58A6FF"
```

---

# How It Works

```text
GitHub GraphQL API
        │
        ▼
Public Discussion Activity
        │
        ▼
AnswerTrace
        │
        ├── Accepted Answers
        ├── Total Upvotes
        ├── Top Community
        └── First Accepted
        │
        ▼
SVG Widget
        │
        ▼
GitHub README
```

AnswerTrace handles paginated GitHub GraphQL results so users with larger Discussion histories can still be analyzed.

---

# Development

Clone AnswerTrace:

```bash
git clone https://github.com/antonisloukis/answertrace.git
cd answertrace
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux or WSL:

```bash
source .venv/bin/activate
```

Install AnswerTrace in editable mode:

```bash
python -m pip install -e .
```

Check the CLI:

```bash
answertrace --help
```

Check the version:

```bash
answertrace --version
```

Analyze a user:

```bash
answertrace antonisloukis
```

Generate a widget:

```bash
answertrace antonisloukis --svg
```

---

# Testing

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

AnswerTrace also uses GitHub Actions CI to automatically run tests on pushes and pull requests to `main`.

---

# Project Structure

```text
answertrace/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── update-widget.yml
│
├── assets/
│   ├── discussion-impact.svg
│   └── marketplace-badge.svg
│
├── src/
│   └── answertrace/
│       ├── __init__.py
│       ├── cli.py
│       ├── github.py
│       ├── metrics.py
│       ├── models.py
│       └── svg.py
│
├── tests/
│   ├── __init__.py
│   ├── test_metrics.py
│   └── test_svg.py
│
├── action.yml
├── pyproject.toml
├── LICENSE
└── README.md
```

---

# Privacy & Security

AnswerTrace reads GitHub Discussions activity through the GitHub API.

Authentication tokens should never be stored directly in:

```text
README files
workflow source
Python source
committed configuration files
```

For GitHub Actions, store the token using an encrypted repository secret:

```text
ANSWERTRACE_TOKEN
```

and reference it as:

```yaml
${{ secrets.ANSWERTRACE_TOKEN }}
```

Use the minimum permissions necessary for your token.

---

# Troubleshooting

## The workflow cannot authenticate

Check that the repository contains this Actions secret:

```text
ANSWERTRACE_TOKEN
```

and that your workflow uses:

```yaml
token: ${{ secrets.ANSWERTRACE_TOKEN }}
```

---

## The widget does not appear

Confirm that this file exists:

```text
assets/discussion-impact.svg
```

and that your README points to the same location:

```html
<img src="./assets/discussion-impact.svg" />
```

---

## The widget is not updating

Open:

```text
Actions
→ Update AnswerTrace
```

and manually run the workflow.

Check the workflow logs for authentication or GitHub API errors.

---

## There are no changes to commit

This message is normal:

```text
AnswerTrace widget is already up to date.
```

It means the generated metrics are identical to the existing widget.

---

# Contributing

Contributions, bug reports, and feature suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Run the test suite.
5. Open a pull request.

---

# License

AnswerTrace is released under the **MIT License**.

See [`LICENSE`](./LICENSE) for details.
