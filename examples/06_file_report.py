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
