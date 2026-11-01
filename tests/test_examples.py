"""Behavior and execution checks for the teaching examples."""

from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_example(stem: str):
    spec = importlib.util.spec_from_file_location(stem, ROOT / "examples" / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[stem] = module
    spec.loader.exec_module(module)
    return module


class ExampleTests(unittest.TestCase):
    def test_all_documented_outputs(self):
        expected = json.loads((ROOT / "examples/expected_outputs.json").read_text(encoding="utf-8"))
        actual_files = {path.name for path in (ROOT / "examples").glob("[0-9][0-9]_*.py")}
        self.assertEqual(len(expected), 15)
        self.assertEqual(actual_files, set(expected))
        for filename, output in expected.items():
            with self.subTest(example=filename):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "examples" / filename)],
                    capture_output=True, text=True, encoding="utf-8", timeout=10,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, output)
                self.assertEqual(result.stderr, "")

    def test_temperature_reference_points(self):
        convert = load_example("02_temperature_converter").celsius_to_fahrenheit
        for celsius, fahrenheit in [(0, 32), (100, 212), (-40, -40)]:
            with self.subTest(celsius=celsius):
                self.assertAlmostEqual(convert(celsius), fahrenheit)

    def test_grade_boundaries(self):
        grade = load_example("03_grade_classifier").classify_grade
        for score, expected in [(0, "F"), (59, "F"), (60, "D"), (69, "D"),
                                (70, "C"), (79, "C"), (80, "B"), (89, "B"),
                                (90, "A"), (100, "A")]:
            with self.subTest(score=score):
                self.assertEqual(grade(score), expected)
        for invalid in [-1, 101]:
            with self.assertRaises(ValueError):
                grade(invalid)
        for invalid in [True, 80.5, "80"]:
            with self.assertRaises(TypeError):
                grade(invalid)

    def test_even_squares_empty_and_negative(self):
        process = load_example("04_collection_processing").even_squares
        self.assertEqual(process([]), [])
        self.assertEqual(process([-2, -1, 0, 2]), [4, 0, 4])

    def test_word_counts_normalize_punctuation(self):
        count = load_example("05_word_frequency").word_counts
        self.assertEqual(count("Python, PYTHON!"), {"python": 2})
        self.assertEqual(count(""), {})

    def test_file_report_round_trip(self):
        write = load_example("06_file_report").write_report
        with TemporaryDirectory() as directory:
            path = Path(directory) / "report.txt"
            write(path, 7)
            self.assertEqual(path.read_text(encoding="utf-8"), "Tasks completed: 7\n")

    def test_sales_aggregate_repeated_products_exactly(self):
        totals = load_example("07_csv_sales_summary").sales_totals
        csv_text = "product,quantity,unit_price\nPen,3,0.10\nPen,2,0.20\n"
        self.assertEqual(totals(csv_text), {"Pen": Decimal("0.70")})
        self.assertEqual(totals("product,quantity,unit_price\n"), {})

    def test_json_filters_completed_tasks(self):
        titles = load_example("08_json_api_payload").completed_titles
        self.assertEqual(titles('{"tasks": []}'), [])
        self.assertEqual(titles('{"tasks": [{"title": "A", "done": false}]}'), [])
        with self.assertRaises(json.JSONDecodeError):
            titles("not JSON")

    def test_inventory_values_and_invalid_inputs(self):
        item = load_example("09_dataclass_inventory").InventoryItem
        self.assertEqual(item("Pen", 3, Decimal("0.10")).total_value, Decimal("0.30"))
        self.assertEqual(item("Pen", 0, Decimal("2")).total_value, Decimal("0"))
        for quantity, price in [(-1, Decimal("2")), (1, Decimal("-2"))]:
            with self.assertRaises(ValueError):
                item("Pen", quantity, price)

    def test_sqlite_threshold_and_order(self):
        query = load_example("10_sqlite_database").high_scores
        self.assertEqual(query(100), [])
        self.assertEqual(query(90), [("Python fundamentals", 90)])
        self.assertEqual(query(75), [("Python fundamentals", 90), ("Database basics", 75)])

    def test_statistics_sample_standard_deviation(self):
        summarize = load_example("11_statistics_summary").summarize
        result = summarize([2, 4, 6, 8, 10])
        self.assertEqual(result["mean"], 6)
        self.assertEqual(result["median"], 6)
        self.assertAlmostEqual(result["sample_stdev"], 10 ** 0.5)
        for values in [[], [1]]:
            with self.assertRaises(ValueError):
                summarize(values)

    def test_cli_argument_and_help(self):
        path = str(ROOT / "examples/12_command_line_tool.py")
        result = subprocess.run([sys.executable, path, "--name", "Alex"], capture_output=True,
                                text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Alex!\n")
        help_result = subprocess.run([sys.executable, path, "--help"], capture_output=True,
                                     text=True, timeout=10)
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("--name", help_result.stdout)

    def test_html_nested_text_entities_and_missing_href(self):
        parser = load_example("14_html_parsing").LinkParser()
        parser.feed('<a>Skip</a><a href="/guide"><b>Python</b> &amp; data</a><a href="/next">Next</a>')
        parser.close()
        self.assertEqual(parser.links, [("Python & data", "/guide"), ("Next", "/next")])

    def test_linear_model_known_predictions(self):
        predict = load_example("15_linear_regression").predict_score
        self.assertAlmostEqual(predict(1), 50)
        self.assertAlmostEqual(predict(5), 90)


if __name__ == "__main__":
    unittest.main()
