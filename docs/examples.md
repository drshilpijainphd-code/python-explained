# The 15-example guide

[Back to the repository](../README.md)

Each example is a complete program. Run commands from the repository root using Python 3.11 or newer. All sample inputs are included in the code. All examples run offline and require no third-party packages.

## 01. Variables and formatted output

Introduce values, strings, and readable output.

**Source:** [01_hello_python.py](../examples/01_hello_python.py)

```bash
python examples/01_hello_python.py
```

```python
"""Introduce variables and formatted strings."""


def main() -> None:
    language = "Python"
    goal = "build useful programs"
    print(f"Hello, {language}!")
    print(f"Learning goal: {goal}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Hello, Python!
Learning goal: build useful programs
```

**Try it:** Change the goal text and add one more formatted line.

## 02. Functions and arithmetic

Convert a temperature with a reusable, typed function.

**Source:** [02_temperature_converter.py](../examples/02_temperature_converter.py)

```bash
python examples/02_temperature_converter.py
```

```python
"""Convert Celsius to Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def main() -> None:
    temperature = 25.0
    print(f"{temperature:.1f} C = {celsius_to_fahrenheit(temperature):.1f} F")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
25.0 C = 77.0 F
```

**Try it:** Add a Fahrenheit-to-Celsius function and test a round trip.

## 03. Conditions and validation

Use branches to classify a score and reject invalid input.

**Source:** [03_grade_classifier.py](../examples/03_grade_classifier.py)

```bash
python examples/03_grade_classifier.py
```

```python
"""Classify whole-number scores from 0 to 100."""


def classify_grade(score: int) -> str:
    if isinstance(score, bool) or not isinstance(score, int):
        raise TypeError("Score must be an integer.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    for threshold, grade in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if score >= threshold:
            return grade
    return "F"


def main() -> None:
    print(f"Score 86: {classify_grade(86)}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Score 86: B
```

**Try it:** Test scores exactly at each grade boundary, and handle an invalid score.

## 04. Lists and comprehensions

Filter measurements and transform the selected values.

**Source:** [04_collection_processing.py](../examples/04_collection_processing.py)

```bash
python examples/04_collection_processing.py
```

```python
"""Filter and transform a sequence."""


def even_squares(numbers: list[int]) -> list[int]:
    return [number ** 2 for number in numbers if number % 2 == 0]


def main() -> None:
    print(f"Even squares: {even_squares([1, 2, 3, 4, 5, 6])}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Even squares: [4, 16, 36]
```

**Try it:** Accept a tuple or another iterable instead of only a list.

## 05. Text analysis

Normalize text and count words for a simple content report.

**Source:** [05_word_frequency.py](../examples/05_word_frequency.py)

```bash
python examples/05_word_frequency.py
```

```python
"""Count English words with regular expressions and Counter."""

from collections import Counter
import re


def word_counts(text: str) -> Counter[str]:
    # This deliberately simple tokenizer handles ASCII words, not every language.
    return Counter(re.findall(r"[a-z]+", text.lower()))


def main() -> None:
    text = "Python makes automation simple. Python makes analysis useful. Python!"
    for word, count in word_counts(text).most_common(3):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
python: 3
makes: 2
automation: 1
```

**Try it:** Decide how hyphenated words should be counted and document that rule.

## 06. File automation

Write and read a UTF-8 report using a temporary directory.

**Source:** [06_file_report.py](../examples/06_file_report.py)

```bash
python examples/06_file_report.py
```

```python
"""Read and write a report without modifying personal files."""

from pathlib import Path
from tempfile import TemporaryDirectory


def write_report(path: Path, completed: int) -> None:
    path.write_text(f"Tasks completed: {completed}\n", encoding="utf-8")


def main() -> None:
    with TemporaryDirectory() as directory:
        report = Path(directory) / "report.txt"
        write_report(report, completed=3)
        print(report.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Tasks completed: 3
```

**Try it:** Accept a list of tasks and write one task per line.

## 07. CSV and business reporting

Read tabular records and calculate exact decimal totals.

**Source:** [07_csv_sales_summary.py](../examples/07_csv_sales_summary.py)

```bash
python examples/07_csv_sales_summary.py
```

```python
"""Summarize sample sales with decimal arithmetic."""

import csv
from decimal import Decimal
from io import StringIO

SAMPLE_CSV = "product,quantity,unit_price\nNotebook,2,12.50\nPen,5,3.00\n"


def sales_totals(csv_text: str) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for row in csv.DictReader(StringIO(csv_text)):
        product = row["product"]
        amount = int(row["quantity"]) * Decimal(row["unit_price"])
        totals[product] = totals.get(product, Decimal("0")) + amount
    return totals


def main() -> None:
    totals = sales_totals(SAMPLE_CSV)
    for product, amount in totals.items():
        print(f"{product}: {amount:.2f}")
    print(f"Total sales: {sum(totals.values(), Decimal('0')):.2f}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Notebook: 25.00
Pen: 15.00
Total sales: 40.00
```

**Try it:** Add another row for an existing product and verify aggregation.

## 08. JSON and API data

Decode a local API-style payload and select completed tasks.

**Source:** [08_json_api_payload.py](../examples/08_json_api_payload.py)

```bash
python examples/08_json_api_payload.py
```

```python
"""Process an API-style JSON response entirely offline."""

import json

SAMPLE_PAYLOAD = '{"tasks": [{"title": "Read the Python guide", "done": true}, {"title": "Build a project", "done": false}]}'


def completed_titles(payload: str) -> list[str]:
    data = json.loads(payload)
    return [task["title"] for task in data["tasks"] if task["done"]]


def main() -> None:
    for title in completed_titles(SAMPLE_PAYLOAD):
        print(f"Completed: {title}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Completed: Read the Python guide
```

**Try it:** Add validation for missing fields and malformed JSON.

## 09. Object-oriented programming

Model an inventory item with a dataclass and calculated value.

**Source:** [09_dataclass_inventory.py](../examples/09_dataclass_inventory.py)

```bash
python examples/09_dataclass_inventory.py
```

```python
"""Represent inventory with a dataclass."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class InventoryItem:
    name: str
    quantity: int
    unit_price: Decimal

    def __post_init__(self) -> None:
        if self.quantity < 0 or self.unit_price < 0:
            raise ValueError("Quantity and price must be non-negative.")

    @property
    def total_value(self) -> Decimal:
        return self.quantity * self.unit_price


def main() -> None:
    item = InventoryItem("Keyboard", 3, Decimal("49.99"))
    print(f"{item.name} inventory value: {item.total_value:.2f}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Keyboard inventory value: 149.97
```

**Try it:** Add an operation that returns an updated immutable inventory item.

## 10. SQL and persistence

Create a table, insert records, and query results with parameters.

**Source:** [10_sqlite_database.py](../examples/10_sqlite_database.py)

```bash
python examples/10_sqlite_database.py
```

```python
"""Use an in-memory database and parameterized SQL."""

import sqlite3


def high_scores(minimum: int) -> list[tuple[str, int]]:
    connection = sqlite3.connect(":memory:")
    try:
        with connection:
            connection.execute("CREATE TABLE courses (name TEXT, score INTEGER)")
            connection.executemany(
                "INSERT INTO courses VALUES (?, ?)",
                [("Python fundamentals", 90), ("Database basics", 75)],
            )
            return connection.execute(
                "SELECT name, score FROM courses WHERE score >= ? ORDER BY score DESC",
                (minimum,),
            ).fetchall()
    finally:
        connection.close()


def main() -> None:
    for name, score in high_scores(80):
        print(f"{name}: {score}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Python fundamentals: 90
```

**Try it:** Insert a third course and query with two different score thresholds.

## 11. Descriptive statistics

Summarize measurements with mean, median, and sample standard deviation.

**Source:** [11_statistics_summary.py](../examples/11_statistics_summary.py)

```bash
python examples/11_statistics_summary.py
```

```python
"""Calculate descriptive statistics for a small dataset."""

from statistics import mean, median, stdev


def summarize(values: list[float]) -> dict[str, float]:
    if len(values) < 2:
        raise ValueError("Provide at least two observations.")
    return {"mean": mean(values), "median": median(values), "sample_stdev": stdev(values)}


def main() -> None:
    result = summarize([2, 4, 6, 8, 10])
    print(f"Mean: {result['mean']:.2f}")
    print(f"Median: {result['median']:.2f}")
    print(f"Sample standard deviation: {result['sample_stdev']:.2f}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Mean: 6.00
Median: 6.00
Sample standard deviation: 3.16
```

**Try it:** Compare mean and median after adding an extreme observation.

## 12. Command-line applications

Accept a name through argparse and provide built-in help.

**Source:** [12_command_line_tool.py](../examples/12_command_line_tool.py)

```bash
python examples/12_command_line_tool.py
```

```python
"""Build a small command-line application."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument("--name", default="Developer", help="Name to include in the greeting")
    arguments = parser.parse_args()
    print(f"Hello, {arguments.name}!")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Hello, Developer!
```

**Try it:** Run the program with --help, then add a --uppercase option.

## 13. Asynchronous programming

Schedule independent simulated I/O tasks concurrently.

**Source:** [13_async_tasks.py](../examples/13_async_tasks.py)

```bash
python examples/13_async_tasks.py
```

```python
"""Demonstrate concurrency with simulated I/O, without network access."""

import asyncio


async def prepare(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}: ready"


async def prepare_all() -> list[str]:
    # gather returns results in input order, even if completion order differs.
    return await asyncio.gather(prepare("report", 0.02), prepare("summary", 0.01))


def main() -> None:
    for result in asyncio.run(prepare_all()):
        print(result)


if __name__ == "__main__":
    main()
```

**Expected output**

```text
report: ready
summary: ready
```

**Try it:** Add a third task and compare completion order with result order.

## 14. Structured web content

Extract link labels and destinations from local HTML.

**Source:** [14_html_parsing.py](../examples/14_html_parsing.py)

```bash
python examples/14_html_parsing.py
```

```python
"""Parse local HTML without downloading pages."""

from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._label: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._label = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._label.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href is not None:
            self.links.append(("".join(self._label).strip(), self._href))
            self._href = None
            self._label = []


def main() -> None:
    parser = LinkParser()
    parser.feed('<a href="https://www.python.org/"><strong>Python</strong></a>')
    parser.close()
    for label, url in parser.links:
        print(f"{label} -> {url}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Python -> https://www.python.org/
```

**Try it:** Parse two links, including one with an HTML entity in its label.

## 15. Predictive modeling fundamentals

Fit a line to toy data and make a prediction without external libraries.

**Source:** [15_linear_regression.py](../examples/15_linear_regression.py)

```bash
python examples/15_linear_regression.py
```

```python
"""Fit a straight line to synthetic data; this is an educational model."""

from statistics import linear_regression


def predict_score(hours: float) -> float:
    study_hours = [1, 2, 3, 4]
    synthetic_scores = [50, 60, 70, 80]
    slope, intercept = linear_regression(study_hours, synthetic_scores)
    return slope * hours + intercept


def main() -> None:
    slope, intercept = linear_regression([1, 2, 3, 4], [50, 60, 70, 80])
    print(f"Slope: {slope:.2f}")
    print(f"Intercept: {intercept:.2f}")
    print(f"Prediction for 5 study hours: {predict_score(5):.2f}")


if __name__ == "__main__":
    main()
```

**Expected output**

```text
Slope: 10.00
Intercept: 40.00
Prediction for 5 study hours: 90.00
```

**Try it:** Introduce noise into the synthetic scores and inspect prediction errors.
