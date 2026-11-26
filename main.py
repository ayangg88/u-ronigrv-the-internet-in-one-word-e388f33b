"""The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt. Deterministic, standard library only.
"""

import os


WORD = "unhinged"


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
