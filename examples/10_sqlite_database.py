"""Use an in-memory database and parameterized SQL."""

import sqlite3


def high_scores(minimum: int) -> list[tuple[str, int]]:
    connection = sqlite3.connect(":memory:")
    try:
        with connection:
            connection.execute("CREATE TABLE courses (name TEXT, score INTEGER)")
            connection.executemany(
                "INSERT INTO courses VALUES (?, ?)",
                [("Python fundamentals", 90), ("Database basics", 75)],
            )
            return connection.execute(
                "SELECT name, score FROM courses WHERE score >= ? ORDER BY score DESC",
                (minimum,),
            ).fetchall()
    finally:
        connection.close()


def main() -> None:
    for name, score in high_scores(80):
        print(f"{name}: {score}")


if __name__ == "__main__":
    main()
