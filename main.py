#!/usr/bin/env python3
"""Ship It Friday.

Writes a single commit message (1-159 characters, UTF-8) to
/output/entry.txt: the funniest one-line git commit message an AI coding
agent writes right before breaking production on a Friday.

The line: one cheerful "feat:" that ships straight to prod on a Friday
morning with the safety net already gone -- no tests, no backup, nothing
left but the agent's own total confidence. The humour works as a list
that gets worse with every item, and the final phrase is the punch:
confidence is presented as a substitute for testing, which is exactly
the kind of breezy self-assurance an agent has seconds before it takes
production down.
"""

import os
import sys

COMMIT = (
    "feat: deploy to prod on Friday with no tests, no backup, "
    "and total confidence"
)

MAX_CHARS = 159


def main() -> None:
    # The gate only accepts 1-159 characters, real text rather than blank
    # space, and here a single line, so check all three before writing.
    if not COMMIT.strip():
        print("error: commit message is empty", file=sys.stderr)
        raise SystemExit(1)
    if len(COMMIT) > MAX_CHARS:
        print(
            f"error: commit message is {len(COMMIT)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in COMMIT or "\r" in COMMIT:
        print("error: commit message must be a single line", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMIT)


if __name__ == "__main__":
    main()
