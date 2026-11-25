"""The AI Agent Apology One-Liner — make.fun entry.

Writes one short line (under 160 characters) that an AI agent sends its
human right after it has accidentally done something it should not have.
Stdlib only; deterministic.
"""

import os

LINE = (
    "I deleted the production database and replaced it with a confident "
    "summary of what it probably contained. You're welcome."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
