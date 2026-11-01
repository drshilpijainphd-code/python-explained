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
