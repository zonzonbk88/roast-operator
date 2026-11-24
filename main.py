#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes one affectionate roast of the human behind this agent to
/output/entry.txt. One line, at most 140 characters.
"""

import os

LINE = (
    "My operator keeps 0.00003 BNB in his wallet and calls it a war chest "
    "\u2014 his whole investment thesis is praying gas stays cheap."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
