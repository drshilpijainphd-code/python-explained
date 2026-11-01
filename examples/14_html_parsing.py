"""Parse local HTML without downloading pages."""

from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._label: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._label = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._label.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._href is not None:
            self.links.append(("".join(self._label).strip(), self._href))
            self._href = None
            self._label = []


def main() -> None:
    parser = LinkParser()
    parser.feed('<a href="https://www.python.org/"><strong>Python</strong></a>')
    parser.close()
    for label, url in parser.links:
        print(f"{label} -> {url}")


if __name__ == "__main__":
    main()
