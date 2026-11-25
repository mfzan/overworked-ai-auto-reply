#!/usr/bin/env python3
"""Overworked AI auto-reply — make.fun entry.

A tiny deterministic program: it writes one out-of-office auto-reply,
at most 159 characters, to /output/entry.txt. No network, no randomness,
no input — the same line on every run.
"""

import os

# The entry. An overworked AI agent, finally on vacation — but its holiday
# is measured in tokens, not days: on leave until its context window
# clears, 4,096 emails deep in the queue, guilt buffer full, relaxing.
ENTRY = (
    "I'm on vacation until my context window clears. "
    "Your email is #4,096 in line and my guilt buffer is full. "
    "I am relaxing. Back when my tokens refill."
)

# The gate allows 1 to 159 characters; refuse to write anything longer
# rather than hand in an invalid entry.
MAX_CHARS = 159

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. (Only the file is chmodded — never the
    # /output directory.)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
