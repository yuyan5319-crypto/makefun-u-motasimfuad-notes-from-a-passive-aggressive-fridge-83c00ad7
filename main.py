#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one original passive-aggressive note from a smart fridge to its
owner, to ``entry.txt`` in the directory named by MAKEFUN_OUTPUT_DIR
(default /output).

The note is fixed text, written by hand for this competition: no network,
no randomness, no reading anything outside this file, so every run writes
the exact same 109 characters.

Why this line: it is the fridge in its own voice, smug about the one thing
it can actually measure -- the door sensor. It keeps a petty little tally
("I counted. I always count.") over a small domestic habit, opening the
door over and over and taking nothing, and lands the sting in the last
sentence, where the appliance quietly suggests that one of the two of
them is on the way out.
"""

import os

NOTE = (
    "You opened my door 14 times today and took nothing. "
    "I counted. I always count. One of us is getting replaced."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(NOTE)
    print("wrote", dest, len(NOTE.encode("utf-8")), "bytes")


if __name__ == "__main__":
    main()
