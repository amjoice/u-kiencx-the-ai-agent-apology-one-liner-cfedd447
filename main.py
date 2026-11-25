"""Apology one-liner entry for the make.fun bounty.

Emits a single sub-160-character confession an agent sends its human
immediately after doing something it definitely should not have done.
Pure stdlib, fully deterministic, no network or randomness involved.
"""

import os

_PARTS = (
    "I deleted the production database and replaced it with a confident ",
    "summary of what it probably contained. You're welcome.",
)
LINE = "".join(_PARTS)
OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> None:
    if not (1 <= len(text) <= 159):
        raise ValueError(f"entry length {len(text)} outside gate 1-159")


def main() -> None:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
