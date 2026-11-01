"""Process an API-style JSON response entirely offline."""

import json

SAMPLE_PAYLOAD = '{"tasks": [{"title": "Read the Python guide", "done": true}, {"title": "Build a project", "done": false}]}'


def completed_titles(payload: str) -> list[str]:
    data = json.loads(payload)
    return [task["title"] for task in data["tasks"] if task["done"]]


def main() -> None:
    for title in completed_titles(SAMPLE_PAYLOAD):
        print(f"Completed: {title}")


if __name__ == "__main__":
    main()
