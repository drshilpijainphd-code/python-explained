# Python Explained
### From language fundamentals to practical applications

A structured introduction to **what Python is, where it is used, and how to write useful programs**. Explore 15 small, runnable examples supported by explanations, expected results, and automated checks.

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Examples](https://img.shields.io/badge/examples-15-2563EB)](docs/examples.md)
[![Tests](https://github.com/drshilpijainphd-code/python-explained/actions/workflows/tests.yml/badge.svg)](https://github.com/drshilpijainphd-code/python-explained/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Start here:** [Quick start](#quick-start) · [Python fundamentals](docs/fundamentals.md) · [Practical uses](docs/applications.md) · [15 examples](docs/examples.md) · [Learning path](docs/learning-path.md)

## What is Python?

Python is a high-level, general-purpose programming language. Its readable syntax lets developers express ideas with relatively little code. Python supports procedural, object-oriented, and functional programming styles, and provides a standard library for common tasks.

Python is dynamically typed: objects have types, while names can be bound to different objects. Type hints make intent clearer but do not automatically enforce types at runtime. Python is often described as interpreted; CPython, its reference implementation, compiles source into bytecode that its interpreter executes. See the [official Python tutorial](https://docs.python.org/3/tutorial/) for the language foundations.

## Why learn it?

- **Readable programs:** indentation defines blocks, making structure visible.
- **Fast experimentation:** scripts and an interactive interpreter shorten the feedback loop.
- **Useful built-in tools:** work with files, JSON, CSV, SQL, statistics, and command-line arguments.
- **A broad ecosystem:** specialized packages extend Python into web development, science, and machine learning.
- **Transferable concepts:** functions, data structures, error handling, and tests apply across languages.

Python is a practical choice for many tasks, but performance-sensitive code may need optimized libraries or another language. Python is also not the standard language executed directly by web browsers.

## Where is Python used?

| Area | Typical work | Example in this repository |
| --- | --- | --- |
| Automation | Generate reports and process files | [File report](examples/06_file_report.py) |
| Business reporting | Aggregate spreadsheet exports | [CSV sales summary](examples/07_csv_sales_summary.py) |
| Web services and integrations | Process structured request and response data | [JSON payload](examples/08_json_api_payload.py) |
| Database applications | Store and query records | [SQLite database](examples/10_sqlite_database.py) |
| Data analysis | Summarize observations | [Statistics summary](examples/11_statistics_summary.py) |
| Developer tools | Build utilities and automate checks | [Command-line tool](examples/12_command_line_tool.py) |
| Concurrent I/O | Coordinate tasks that spend time waiting | [Async tasks](examples/13_async_tasks.py) |
| Content processing | Extract information from structured documents | [HTML parsing](examples/14_html_parsing.py) |
| Machine learning foundations | Fit a model and calculate predictions | [Linear regression](examples/15_linear_regression.py) |

Python also appears in scientific computing, desktop software, education, and business systems. The [Python Software Foundation's application overview](https://www.python.org/about/apps/) provides further context. Read the [application guide](docs/applications.md) for ecosystem examples and tradeoffs.

## Quick start

Install **Python 3.11 or newer** and Git. No third-party Python packages are required.

```bash
git clone https://github.com/drshilpijainphd-code/python-explained.git
cd python-explained
python --version
python examples/01_hello_python.py
```

On macOS or Linux, use `python3` if `python` is unavailable. On Windows, `py` is an alternative when the Python launcher is installed. Run commands from the repository root.

Expected output:

```text
Hello, Python!
Learning goal: build useful programs
```

Run all 15 examples and verify their output:

```bash
python scripts/run_examples.py
```

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

Try a command-line argument:

```bash
python examples/12_command_line_tool.py --name Alex
```

All examples run offline. The file example uses a temporary directory, and the database example uses an in-memory database.

## The 15 examples

| # | Example | What you learn |
| --- | --- | --- |
| 01 | [Variables and formatted output](examples/01_hello_python.py) | Introduce values, strings, and readable output. |
| 02 | [Functions and arithmetic](examples/02_temperature_converter.py) | Convert a temperature with a reusable, typed function. |
| 03 | [Conditions and validation](examples/03_grade_classifier.py) | Use branches to classify a score and reject invalid input. |
| 04 | [Lists and comprehensions](examples/04_collection_processing.py) | Filter measurements and transform the selected values. |
| 05 | [Text analysis](examples/05_word_frequency.py) | Normalize text and count words for a simple content report. |
| 06 | [File automation](examples/06_file_report.py) | Write and read a UTF-8 report using a temporary directory. |
| 07 | [CSV and business reporting](examples/07_csv_sales_summary.py) | Read tabular records and calculate exact decimal totals. |
| 08 | [JSON and API data](examples/08_json_api_payload.py) | Decode a local API-style payload and select completed tasks. |
| 09 | [Object-oriented programming](examples/09_dataclass_inventory.py) | Model an inventory item with a dataclass and calculated value. |
| 10 | [SQL and persistence](examples/10_sqlite_database.py) | Create a table, insert records, and query results with parameters. |
| 11 | [Descriptive statistics](examples/11_statistics_summary.py) | Summarize measurements with mean, median, and sample standard deviation. |
| 12 | [Command-line applications](examples/12_command_line_tool.py) | Accept a name through argparse and provide built-in help. |
| 13 | [Asynchronous programming](examples/13_async_tasks.py) | Schedule independent simulated I/O tasks concurrently. |
| 14 | [Structured web content](examples/14_html_parsing.py) | Extract link labels and destinations from local HTML. |
| 15 | [Predictive modeling fundamentals](examples/15_linear_regression.py) | Fit a line to toy data and make a prediction without external libraries. |

The [annotated example guide](docs/examples.md) contains the complete code, commands, expected output, and an exercise for every example.

## Repository structure

```text
python-explained/
├── README.md
├── docs/
│   ├── fundamentals.md
│   ├── applications.md
│   ├── examples.md
│   └── learning-path.md
├── examples/                 # 15 standalone Python programs + output fixtures
├── scripts/run_examples.py  # Runs every example and checks its output
├── tests/test_examples.py    # Behavior, boundary, and execution checks
├── .github/workflows/tests.yml
├── CONTRIBUTING.md
└── LICENSE
```

## Quality and scope

Examples use explicit imports, descriptive names, focused functions, and main guards. Tests check all example outputs and selected edge cases. GitHub Actions runs the checks on Python 3.11–3.14 on Linux, plus Python 3.14 on Windows.

This is an educational repository. Its small datasets and models demonstrate concepts; they do not represent production services, financial advice, or validated predictions about people. The JSON and CSV examples assume the documented sample schemas.

## Contributing

Corrections, clearer explanations, and focused improvements are welcome. Follow [CONTRIBUTING.md](CONTRIBUTING.md), include a reproducible example of the change, and run the checks before opening a pull request.

## License

Released under the [MIT License](LICENSE).
