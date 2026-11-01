# Contributing

Thank you for helping improve Python Explained.

## Propose a focused change

Open an issue for a bug, unclear explanation, or suggested improvement. Include the affected file, the command you ran, your Python version, and the expected and actual behavior. Do not include credentials or private data.

For a contribution, fork the repository, create a descriptive branch, and keep the pull request focused on one topic.

## Style and scope

- Support Python 3.11 and newer.
- Keep the core examples standard-library-only and runnable offline.
- Use four-space indentation, descriptive names, and explicit imports.
- Add a main guard to executable examples.
- Explain assumptions and use small, understandable sample inputs.
- Keep the annotated guide and expected-output fixtures consistent with the code.
- Avoid claims of production readiness for teaching demonstrations.

## Verify your change

From the repository root:

```bash
python scripts/run_examples.py
python -m unittest discover -s tests -v
```

Update tests when behavior changes. In the pull request, describe the problem, the resulting behavior, and the checks you ran.
