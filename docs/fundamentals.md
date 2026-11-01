# Python fundamentals

[Back to the repository](../README.md)

## How a Python program runs

Save source code in a file ending in `.py`, then pass that file to the Python interpreter. Statements normally execute in order. A function groups reusable behavior, and an import makes another module's names available. A module is typically a Python file; a package organizes related modules.

The `if __name__ == "__main__":` guard makes demonstration code run when a file is executed directly, while allowing its functions to be imported without running the demonstration.

## Values, names, and types

| Type | Example | Common purpose |
| --- | --- | --- |
| `str` | `"Python"` | Text |
| `int` | `42` | Whole numbers |
| `float` | `3.5` | Approximate real-number calculations |
| `bool` | `True` | Conditions |
| `list` | `[10, 20, 30]` | Ordered, mutable collections |
| `tuple` | `(10, 20)` | Ordered, immutable collections |
| `dict` | `{"name": "Alex"}` | Key-value lookups |
| `set` | `{"red", "blue"}` | Unique elements |
| `NoneType` | `None` | Absence of a value |

A variable is a name bound to an object. Assignment does not necessarily copy that object. Lists and dictionaries are mutable; strings and tuples are immutable. A tuple can still contain a mutable object.

## Control flow

Use `if` / `elif` / `else` to choose a branch. A `for` loop visits items from an iterable, while a `while` loop repeats while a condition is true. Python uses indentation to group statements; use four spaces per level.

## Functions and interfaces

Functions accept parameters and return results. Keep calculations separate from printing so the same function can be used by a script, a test, or an application. Type hints document expected inputs and outputs; validation is still needed where external data enters a program.

## Handling errors

Raise an appropriate exception when an input is invalid. Catch only errors you can handle meaningfully. Catching every exception and ignoring it hides defects. Example 03 rejects scores outside its supported range, and example 11 rejects datasets that are too small for sample standard deviation.

## Files and resources

Specify a text encoding such as UTF-8. Use `with` blocks for resources that support context management. Keep paths platform independent with `pathlib`. The SQLite example closes its connection explicitly: a connection's transaction context manager does not itself close the connection.

## Standard library versus third-party packages

The standard library ships with Python. This repository uses only those modules. Libraries such as Django, NumPy, and pandas are installed separately and have their own documentation and release cycles. A virtual environment isolates a project's installed packages:

```bash
python -m venv .venv
```

In Windows Command Prompt, use `call .venv\Scripts\activate.bat`; macOS/Linux shells use `source .venv/bin/activate`. Activation is optional: you can invoke the environment's Python executable directly. There are no packages to install for this repository. The [CMD guide](cmd.md) includes the complete setup and test commands.

## Habits that improve maintainability

1. Give functions one clear responsibility.
2. Name values according to their meaning.
3. Write a short docstring when purpose or assumptions need explanation.
4. Test observable behavior and boundary conditions.
5. Keep credentials and machine-specific files out of version control.
6. Measure performance before optimizing.

## References

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Built-in types](https://docs.python.org/3/library/stdtypes.html)
- [Standard library reference](https://docs.python.org/3/library/)
- [PEP 8 style guide](https://peps.python.org/pep-0008/)
