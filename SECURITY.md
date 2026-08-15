# Security Policy

## Supported Versions

Security fixes are currently provided for the latest stable release of AnswerTrace.

| Version | Supported |
| ------- | --------- |
| Latest stable release | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

Please do not report security vulnerabilities through public GitHub issues.

If you believe you have discovered a security vulnerability in AnswerTrace, contact the maintainer privately.

When reporting a vulnerability, please include:

- A clear description of the vulnerability
- Steps required to reproduce it
- The affected component or version
- The potential security impact
- Relevant logs or screenshots, if safe to share
- Any suggested mitigation, if available

Do not include authentication tokens, API keys, passwords, or other sensitive credentials in your report.

## Responsible Disclosure

Please avoid publicly disclosing a vulnerability until it has been reviewed and, where appropriate, a fix has been released.

This helps protect users who may still be running an affected version.

## Response Process

Security reports will be reviewed as soon as practical.

If the issue is confirmed:

1. The vulnerability will be investigated.
2. A fix will be prepared.
3. Tests will be added or updated where appropriate.
4. A patched release will be published.
5. Public disclosure may follow once users have had a reasonable opportunity to update.

## Scope

Security reports related to the following areas are especially useful:

- GitHub token handling
- GitHub Actions workflows
- GitHub GraphQL API usage
- Generated output containing unintended sensitive data
- Dependency vulnerabilities
- Command execution or injection risks

## Out of Scope

The following are generally not considered security vulnerabilities unless they create a meaningful security impact:

- Incorrect or outdated discussion metrics
- Cosmetic SVG rendering issues
- README formatting problems
- Feature requests
- Expected GitHub API rate limits
- Problems caused by incorrectly configured user permissions

## Security Best Practices for Users

When using AnswerTrace:

- Store GitHub tokens only in encrypted GitHub Actions secrets.
- Never commit tokens to a repository.
- Never place tokens directly inside workflow YAML files.
- Use the minimum GitHub permissions required.
- Rotate or revoke tokens that may have been exposed.
- Review workflow changes before merging them.
- Keep AnswerTrace updated to the latest stable release.

A token should be referenced in workflows like this:

```yaml
token: ${{ secrets.ANSWERTRACE_TOKEN }}
```

and never like this:

```yaml
token: ghp_example_secret_token
```

## Security Updates

Important security fixes will be released through new AnswerTrace versions when necessary.

Users are encouraged to use the stable major-version reference:

```yaml
uses: antonisloukis/answertrace@v1
```

so compatible security and maintenance updates can be adopted without changing workflow configuration.

## Contact

For security-related reports, contact the project maintainer privately through the contact information available on the maintainer's GitHub profile.

Please provide enough information to reproduce and investigate the issue.

Thank you for helping keep AnswerTrace and its users secure.
