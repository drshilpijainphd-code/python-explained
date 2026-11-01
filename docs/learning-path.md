# Working through the examples

[Back to the repository](../README.md)

Start with examples 01–05 if Python is new to you. Run each file, change an input, and work out why the result changed. The [fundamentals guide](fundamentals.md) is a reference for the syntax used along the way.

If you already know variables, loops, and functions, start at example 06.

## Change a boundary case

In the grade classifier, try 59, 60, 89, and 90. Then try -1 and 101. The distinction between an ordinary result and an invalid input matters: a failing grade is valid data, but a score outside the accepted range is an error.

Read the corresponding test in [test_examples.py](../tests/test_examples.py). Add one more case before changing the implementation.

## Follow a record through a program

Use the CSV sales example to trace how one row becomes a total:

1. `csv.DictReader` reads the fields as strings.
2. The quantity becomes an integer and the unit price becomes a `Decimal`.
3. The amount is added to the running total for that product.
4. The result is formatted for display.

Add a second row for Notebook. Check that the amounts are added together instead of one row replacing the other. Next, try a missing quantity and decide what error message would help someone using the script.

## Join two examples

The examples are separate files, but a small application usually combines these ideas. A useful next step is a command-line CSV report:

- Accept an input path with `argparse`.
- Read the file using UTF-8.
- Calculate totals using the function from example 07.
- Print a clear error if the file is missing or a required column is absent.

Keep file reading outside the calculation function. That lets a test pass a short CSV string without creating a file.

## Look at the assumptions

The word counter recognizes ASCII letters only. The HTML parser handles the small examples shown, but is not a full web crawler. The async example uses simulated waits rather than real requests.

Pick one of these limits and extend the program. For example, change the tokenizer to handle a particular language, or add a test for a link whose label contains nested tags.

In the regression example, changing the four synthetic scores makes the fitted line change. Compare the predicted and actual values, but do not treat a good fit on those same points as evidence of future accuracy.

## Build something small

A reading tracker is a reasonable follow-up project. Store book titles and completion status in SQLite, then add commands to create, list, and finish an entry. That combines functions, arguments, queries, and persistence without requiring a web framework.

Write down what each command should do before implementing it. Include cases such as a missing book, an empty title, and an empty database. Once those behaviors work, add a README with commands someone else can copy.
