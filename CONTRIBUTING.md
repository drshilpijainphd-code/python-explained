# Contributing

Bug fixes and corrections to the explanations are welcome. For a bug report, include the file, the command you ran, your Python version, and what you expected to happen.

Keep a pull request focused on one change. If an example becomes difficult to explain in a few paragraphs, it may be better suited to a separate project.

## Working on an example

Use Python 3.11-compatible syntax and the standard library. Examples should run offline with the sample inputs already included. Keep calculations separate from printing where that makes the code easier to test.

When changing an example, check these files as well:

- `docs/examples.md` contains a copy of the source and its expected output.
- `examples/expected_outputs.json` supplies the output used by the runner.
- `tests/test_examples.py` checks behavior beyond the demonstration input.

Update the relevant documentation and fixtures if the behavior changes. Avoid changing an expected result just to make a failing test pass; first check why the result differs.

## Before opening a pull request

Run these commands from the repository root:

```bash
python scripts/run_examples.py
python -m unittest discover -s tests -v
```

Describe what changed and which checks you ran. For a documentation-only correction, checking the example names, commands, and links is usually enough.
