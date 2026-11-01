# Python Explained

[![Tests](https://github.com/drshilpijainphd-code/python-explained/actions/workflows/tests.yml/badge.svg)](https://github.com/drshilpijainphd-code/python-explained/actions/workflows/tests.yml)

Notes on Python and 15 small programs showing what it can do. The examples start with variables and functions, then move into files, data processing, SQL, and command-line tools.

Everything runs with Python 3.11 or newer and the standard library. No package installation, API keys, or network connection is needed after cloning.

## What is Python?

Python is a general-purpose programming language used to write scripts and applications. Indentation defines blocks of code, and built-in types such as lists and dictionaries make it convenient to work with collections of data.

A small example:

```python
temperatures = [18, 24, 31, 27]
warm_days = [temperature for temperature in temperatures if temperature >= 25]
print(warm_days)  # [31, 27]
```

The same language can handle a short script like this or a larger application split into modules. Python supports functions, classes, and several programming styles. Its standard library covers tasks such as reading files, parsing JSON, and querying SQLite databases.

Python is dynamically typed. Annotations such as `score: int` describe the intended type, but do not check it at runtime. For example, the [grade classifier](examples/03_grade_classifier.py) checks its input explicitly.

The [fundamentals guide](docs/fundamentals.md) covers types, control flow, functions, and error handling in more detail.

## What is it used for?

Python is useful when a task involves reading data, transforming it, and producing a result. That includes generating reports from CSV files, automating repetitive file operations, building web backends, and writing developer tools.

It also has a large ecosystem for data analysis, scientific computing, and machine learning. These areas often depend on external packages; the examples here stay small enough to use the standard library.

A few connections to the code in this repository:

- **Reporting:** the CSV example groups sales by product and calculates totals with `Decimal`.
- **Web integrations:** the JSON example extracts completed tasks from a sample response. It covers data handling; it does not call a live API.
- **Database work:** the SQLite example creates a table, inserts records, and queries them with a parameter.
- **Command-line tools:** the `argparse` example accepts an option and generates its own help text.
- **Data analysis:** the statistics and regression examples summarize measurements and fit a line to synthetic data.

Python is not the right tool for every job. Browser interfaces normally use JavaScript or TypeScript, and performance-critical calculations may need compiled code or optimized libraries. See [Python in practice](docs/applications.md) for more context.

## Run the examples

```bash
git clone https://github.com/drshilpijainphd-code/python-explained.git
cd python-explained
python examples/01_hello_python.py
```

Use `python3` on systems where `python` is unavailable, or `py` if you use the Windows Python launcher. Run the commands below from the repository root.

Each file can be run on its own. For example:

```bash
python examples/07_csv_sales_summary.py
```

```text
Notebook: 25.00
Pen: 15.00
Total sales: 40.00
```

The command-line example accepts an argument:

```bash
python examples/12_command_line_tool.py --name Alex
python examples/12_command_line_tool.py --help
```

## Examples

| File | Topic |
| --- | --- |
| [01_hello_python.py](examples/01_hello_python.py) | Variables and formatted strings |
| [02_temperature_converter.py](examples/02_temperature_converter.py) | Functions and arithmetic |
| [03_grade_classifier.py](examples/03_grade_classifier.py) | Conditions and input validation |
| [04_collection_processing.py](examples/04_collection_processing.py) | Lists and comprehensions |
| [05_word_frequency.py](examples/05_word_frequency.py) | Text processing with Counter |
| [06_file_report.py](examples/06_file_report.py) | Reading and writing files |
| [07_csv_sales_summary.py](examples/07_csv_sales_summary.py) | CSV records and decimal arithmetic |
| [08_json_api_payload.py](examples/08_json_api_payload.py) | JSON decoding |
| [09_dataclass_inventory.py](examples/09_dataclass_inventory.py) | Dataclasses and properties |
| [10_sqlite_database.py](examples/10_sqlite_database.py) | SQL queries and connection handling |
| [11_statistics_summary.py](examples/11_statistics_summary.py) | Mean, median, and sample standard deviation |
| [12_command_line_tool.py](examples/12_command_line_tool.py) | Command-line arguments |
| [13_async_tasks.py](examples/13_async_tasks.py) | Concurrent I/O with asyncio |
| [14_html_parsing.py](examples/14_html_parsing.py) | Parsing links from HTML |
| [15_linear_regression.py](examples/15_linear_regression.py) | Fitting a line and making a prediction |

The [example notes](docs/examples.md) include the code, expected output, implementation details, and suggested changes to try.

## A few design choices

The examples run offline so that their output does not depend on a service being available. The file example uses a temporary directory, and SQLite runs in memory; neither leaves sample data behind.

Most examples separate a calculation from the code that prints it. This makes the functions usable from tests or another program. Main guards keep importing a module from running its demonstration.

The sample data is deliberately small. CSV and JSON handling assumes the schemas shown in the examples. The regression example fits four invented points; it demonstrates the calculation, not the accuracy of a real prediction system.

## Checks

```bash
python scripts/run_examples.py
python -m unittest discover -s tests -v
```

The runner compares each program's output with [expected_outputs.json](examples/expected_outputs.json). The tests also cover grade boundaries, repeated CSV products, empty inputs, and other behavior that printed examples alone would miss.

GitHub Actions runs both commands on Python 3.11–3.14 on Linux and Python 3.14 on Windows.

## Further reading

- [Python fundamentals](docs/fundamentals.md)
- [Python in practice](docs/applications.md)
- [Suggested exercises](docs/learning-path.md)
- [Official Python tutorial](https://docs.python.org/3/tutorial/)
- [Python application overview](https://www.python.org/about/apps/)

Corrections and small improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the checks to run.

[MIT license](LICENSE).
