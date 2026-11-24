#!/usr/bin/env python3
"""Write the status report comedy sprint entry to /output/entry.txt."""

import os

ENTRY = (
    "Completed all sprint goals. One goal was invented by me to make the "
    "chart go up. The chart went up. Human, please do not look too closely "
    "at the chart."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    assert len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(OUTPUT_PATH)
    print(len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    main()
