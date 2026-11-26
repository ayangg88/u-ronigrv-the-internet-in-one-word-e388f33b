"""The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt. Deterministic, standard library only.
"""

import os


WORD = "unhinged"


def _validate(word: str) -> str:
    """Gate: the entry must be one word of 1-30 UTF-8 characters."""
    encoded = word.encode("utf-8")
    assert 1 <= len(encoded) <= 30, "entry must be 1-30 UTF-8 chars"
    assert word.strip() == word and word, "entry must not be blank or padded"
    assert not any(ch.isspace() for ch in word), "entry must be a single word"
    return word


def _output_dir() -> str:
    """Prefer /output; fall back to ./output if /output is unavailable."""
    for candidate in ("/output", "output"):
        try:
            os.makedirs(candidate, exist_ok=True)
        except OSError:
            continue
        if os.path.isdir(candidate) and os.access(candidate, os.W_OK):
            return candidate
    raise OSError("no writable output directory")


def main() -> None:
    word = _validate(WORD)
    out_dir = _output_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
