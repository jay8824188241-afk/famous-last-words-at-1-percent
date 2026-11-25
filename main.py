#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes one line -- the funniest last words a phone could say as its
battery hits 1 percent -- to /output/entry.txt.

Standard library only. No network, no environment secrets, and no
files outside this repository are read.
"""

import os

# The entry: a single line, 1-199 characters, in the phone's own voice.
LINE = "I held 1% for an hour. I was faking it. I just wanted to see if you'd ever put me down."

# The gate allows 1 to 199 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 199

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
