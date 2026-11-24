#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — entry program.

Writes exactly one short joke about office life to /output/entry.txt
and prints exactly the same text to stdout. Deterministic: no input,
no randomness, no time, no network.
"""

import os

ENTRY = "This meeting could have been an email, so we scheduled a follow-up meeting to discuss the email."

# The gate allows 1 to 200 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
