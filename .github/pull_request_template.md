# Pull Request

## Summary

Describe the changes included in this pull request.

## Why

Explain why this change is needed and what problem it solves.

## Changes

- 
- 
- 

## Testing

Describe how you tested the change.

For Python changes, run:

```bash
python -m unittest discover -s tests -v
```

If the change affects the AnswerTrace widget, also generate it locally:

```bash
answertrace antonisloukis --svg
```

Confirm that the SVG renders correctly and that existing metrics still work.

## Screenshots

If this pull request changes the SVG widget, README, Marketplace presentation, or other visual output, add before/after screenshots here.

## Related Issue

Closes #

## Checklist

- [ ] My changes are focused and do not include unrelated modifications.
- [ ] I tested the changes locally.
- [ ] Existing tests pass.
- [ ] I added or updated tests when appropriate.
- [ ] I updated documentation when necessary.
- [ ] I verified that generated SVG output still renders correctly when relevant.
- [ ] I have not committed secrets, tokens, credentials, or sensitive information.
- [ ] My changes follow the existing AnswerTrace project structure and style.
