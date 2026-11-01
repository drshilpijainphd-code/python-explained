# Python in practice

[Back to the repository](../README.md)

A language is useful because of the work it helps you finish. The examples in this repository cover small parts of larger tasks: reading a file, summarizing records, querying a database, or accepting command-line arguments.

## Scripts and reports

Suppose a sales export contains hundreds of rows and several rows refer to the same product. A Python script can read the CSV, group the records, and produce totals. [Example 07](../examples/07_csv_sales_summary.py) implements that middle step.

It uses `Decimal` constructed from strings so that values such as `0.10` can be represented exactly. This does not define an application's currency or rounding rules; those still need to be decided. A usable reporting tool would also check column names, missing quantities, and invalid prices.

For file automation, `pathlib` handles paths without embedding Windows or Unix separators throughout the code. [Example 06](../examples/06_file_report.py) writes to a temporary directory to keep the demonstration self-contained.

## Web backends and integrations

Python can run the server-side part of a web application: handling a request, looking up records, applying business rules, and returning a response. Frameworks such as [Django](https://docs.djangoproject.com/), [Flask](https://flask.palletsprojects.com/), and [FastAPI](https://fastapi.tiangolo.com/) provide tools for that work.

JSON commonly carries data between services. [Example 08](../examples/08_json_api_payload.py) decodes a sample response and extracts completed tasks. A real client would also need to handle connection failures, timeouts, unexpected response formats, and authentication where required.

The example stops at processing the payload so it can run without a service or credentials.

## Databases

[Example 10](../examples/10_sqlite_database.py) creates a table and asks for courses with scores above a threshold. The threshold is passed separately from the SQL statement using a `?` placeholder. The same pattern matters when the value comes from a user.

The database lives in memory and disappears when the connection closes. Changing the connection path to a filename introduces persistence, but also decisions about where the file belongs, how its schema changes, and how to back it up.

One detail worth noticing: the SQLite connection's `with` block handles the transaction. It does not close the connection, so the example closes it in `finally`.

## Analysis and modeling

The standard library is enough for the small calculations in [example 11](../examples/11_statistics_summary.py). It uses sample standard deviation, which requires at least two observations. Mean and median are both included because they respond differently to unusually large or small values.

Larger analysis work often uses [pandas](https://pandas.pydata.org/docs/) for tables, [NumPy](https://numpy.org/doc/) for arrays, and [Matplotlib](https://matplotlib.org/stable/) for plots. Scientific computing also uses [SciPy](https://docs.scipy.org/doc/scipy/).

[Example 15](../examples/15_linear_regression.py) fits a straight line to four synthetic observations. It is an introduction to fitting and prediction. Real modeling requires a reason to trust the measurements and an evaluation on data that was not used to fit the model. Libraries such as [scikit-learn](https://scikit-learn.org/stable/user_guide.html) support more extensive workflows.

## Developer tools and concurrent work

Small command-line programs are often a useful starting point for automation. [Example 12](../examples/12_command_line_tool.py) uses `argparse`, which handles options and generates `--help` output. Tests can then exercise the tool by running the same command a user would run.

Some programs spend most of their time waiting for I/O. [Example 13](../examples/13_async_tasks.py) demonstrates how `asyncio` lets tasks make progress during those waits. Its delays are simulated. The results from `gather` remain in input order even when the tasks finish in another order.

Async code does not automatically speed up calculations. Blocking work inside an async function can hold up the event loop.

## Other uses and limits

Python is also used in teaching, scientific experiments, desktop applications, and testing. The [official application overview](https://www.python.org/about/apps/) provides a broader survey.

For browser interfaces, JavaScript or TypeScript is usually the direct choice. Low-level systems and hard real-time requirements often call for a systems language. Python can coordinate code written in other languages, so a project does not always need to choose just one.
