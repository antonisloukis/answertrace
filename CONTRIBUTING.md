# Contributing to AnswerTrace

Thanks for your interest in contributing to AnswerTrace.

Contributions are welcome, including bug fixes, documentation improvements, tests, and new features.

## Getting Started

Fork the repository and clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/answertrace.git
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

## Create a Branch

Create a branch for your change:

```bash
git checkout -b your-change-name
```

Use a short and descriptive branch name.

Examples:

```text
fix-widget-spacing
add-new-metric
improve-documentation
```

## Make Your Changes

Keep changes focused and avoid unrelated modifications.

For Python changes, follow the existing project structure and coding style.

Try to keep new functionality small, testable, and easy to review.

## Run the Tests

Before opening a pull request, run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

All existing tests should pass.

If your change introduces new functionality, add or update tests when appropriate.

## Test the Widget

If your change affects SVG generation, generate the AnswerTrace widget locally:

```bash
answertrace antonisloukis --svg
```

Confirm that the generated SVG renders correctly and that existing metrics remain intact.

## Commit Your Changes

Stage your changes:

```bash
git add .
```

Create a clear commit:

```bash
git commit -m "Describe your change"
```

Push your branch:

```bash
git push origin your-change-name
```

## Open a Pull Request

Open a pull request against the `main` branch.

Please include:

- What you changed
- Why the change is useful
- How you tested it
- Any relevant issue numbers
- Screenshots if the SVG widget or README appearance changed

Keep pull requests focused on one logical change whenever possible.

## Reporting Bugs

Use the repository's bug report template when reporting a problem.

Please include:

- A clear description of the issue
- Steps to reproduce it
- Expected behavior
- Actual behavior
- AnswerTrace version
- Relevant logs or error messages
- Operating system or environment when relevant

Never include authentication tokens, API keys, passwords, or other sensitive credentials in logs or screenshots.

## Feature Requests

Feature suggestions are welcome.

Please explain:

- The problem you want to solve
- Why it would be useful to AnswerTrace users
- How you imagine the feature working
- Any alternatives you considered

## Documentation Contributions

Documentation improvements are welcome.

This can include:

- Fixing unclear instructions
- Improving examples
- Correcting mistakes
- Adding usage examples
- Improving setup instructions
- Updating screenshots or documentation for new features

## Security Issues

Do not report security vulnerabilities through public GitHub issues.

Please follow the reporting instructions in:

[`SECURITY.md`](./SECURITY.md)

## Code of Conduct

By participating in AnswerTrace, you agree to follow the project's:

[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

## License

By contributing to AnswerTrace, you agree that your contributions will be licensed under the project's MIT License.

Thank you for helping improve AnswerTrace.
