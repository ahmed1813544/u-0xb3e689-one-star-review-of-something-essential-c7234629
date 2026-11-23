"""One-star review of something essential.

Writes a single deadpan one-star review to entry.txt.
Stdlib only, deterministic: the same line on every run.
"""

import os

REVIEW = (
    "One star. Oxygen is free and everywhere, yet somehow runs out "
    "the moment I climb one flight of stairs."
)


def main():
    # The gate allows 1-160 characters, one line, no trailing newline.
    assert 1 <= len(REVIEW) <= 160 and "\n" not in REVIEW
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
