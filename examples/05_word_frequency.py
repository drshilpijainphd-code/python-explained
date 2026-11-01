"""Count English words with regular expressions and Counter."""

from collections import Counter
import re


def word_counts(text: str) -> Counter[str]:
    # This deliberately simple tokenizer handles ASCII words, not every language.
    return Counter(re.findall(r"[a-z]+", text.lower()))


def main() -> None:
    text = "Python makes automation simple. Python makes analysis useful. Python!"
    for word, count in word_counts(text).most_common(3):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
