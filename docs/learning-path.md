# A practical learning path

[Back to the repository](../README.md)

## 1. Understand the building blocks

Read [Python fundamentals](fundamentals.md), then run examples 01–05. Before running each program, predict its output. Change one input, rerun it, and explain why the output changed.

**Checkpoint:** write a function that filters a list and returns a useful summary.

## 2. Work with real data formats

Study examples 06–10. Follow data from input through transformation to output. Notice where the examples assume a fixed schema and where they validate inputs.

**Checkpoint:** combine a CSV reader with a dataclass and calculate a summary without mixing calculation and printing.

## 3. Build useful tools

Run examples 11–14. Try the command-line tool's `--help` option. Explain why async waiting differs from speeding up a CPU-heavy calculation.

**Checkpoint:** create a CLI that reads a local CSV and prints descriptive statistics, including helpful errors for invalid input.

## 4. Explore modeling carefully

Run example 15, change the synthetic data, and compare predictions. Discuss why training fit alone is not a measure of model quality.

**Checkpoint:** split a larger dataset into training and test sets before judging prediction accuracy.

## 5. Extend the repository

Pick one focused project:

- A personal reading tracker with SQLite storage.
- A CSV quality checker that reports missing fields.
- A report generator with a command-line interface.
- A text-analysis utility that handles more than one language.

Define the input, output, and error cases first. Implement a small version, write tests for the behavior, then improve its documentation.

## Before sharing a project

Run all examples and tests. Make sure setup instructions work from a fresh clone. Describe limitations honestly and use sample data that can be shared publicly.
