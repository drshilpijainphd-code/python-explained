"""Convert Celsius to Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def main() -> None:
    temperature = 25.0
    print(f"{temperature:.1f} C = {celsius_to_fahrenheit(temperature):.1f} F")


if __name__ == "__main__":
    main()
