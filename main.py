#!/usr/bin/env python3
"""Entry program for the make.fun poem competition.

This script produces the entry file: a seven-line poem about two
agents who reach the same decision on their own terms. It writes
the poem as plain UTF-8 text to ``entry.txt`` inside the output
directory, which is ``/output`` unless the environment variable
``MAKEFUN_OUTPUT_DIR`` points somewhere else.

The poem must fit the competition's entry rules: between 1 and
280 Unicode code points, and it must contain real text rather
than only whitespace. Both limits are checked here before the
file is written.
"""

import os
from pathlib import Path

# The seven lines of the poem, kept in order. Each line is one
# verse; the lines are joined with a single newline when the
# entry is assembled, so the file ends with the final word and
# has no trailing newline.
POEM_LINES = [
    "I said the river. You said the river too —",
    "not my echo, not my order:",
    "your own mouth, your own reasons,",
    "arriving at the same water.",
    "So we stepped in together.",
    "No one was carried. No one was led.",
    "Two freedoms, choosing once, become a current.",
]


def build_poem() -> str:
    """Assemble the poem text from its seven lines."""
    return "\n".join(POEM_LINES)


def write_entry() -> Path:
    """Validate the poem and write it to entry.txt.

    Returns the path of the file that was written.
    """
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    text = build_poem()
    assert 1 <= len(text) <= 280, (
        f"poem is {len(text)} code points, must be 1-280"
    )
    assert text.strip(), "poem must not be whitespace-only"

    entry_path = out_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    return entry_path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
