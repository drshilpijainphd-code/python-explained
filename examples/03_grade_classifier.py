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
