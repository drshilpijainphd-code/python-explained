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
