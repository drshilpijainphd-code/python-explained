"""Build a small command-line application."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument("--name", default="Developer", help="Name to include in the greeting")
    arguments = parser.parse_args()
    print(f"Hello, {arguments.name}!")


if __name__ == "__main__":
    main()
