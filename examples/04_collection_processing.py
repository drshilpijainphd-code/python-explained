"""Filter and transform a sequence."""


def even_squares(numbers: list[int]) -> list[int]:
    return [number ** 2 for number in numbers if number % 2 == 0]


def main() -> None:
    print(f"Even squares: {even_squares([1, 2, 3, 4, 5, 6])}")


if __name__ == "__main__":
    main()
