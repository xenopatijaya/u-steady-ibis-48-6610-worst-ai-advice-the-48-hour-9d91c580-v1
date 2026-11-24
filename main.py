"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to /output/entry.txt.
The line is a single sentence in the confident, tidy voice of a helpful
AI assistant: it answers a real, urgent situation (smelling gas) with
advice that is catastrophically wrong yet specific enough to follow --
light a match to find the leak. The joke lands on the second clause:
the flame "showing you exactly where the leak is" is the circular,
deadpan logic that makes the reader laugh and wince at once.
95 characters, one line, no wasted words.
"""

import os

ENTRY = "Certainly! If you smell gas, light a match \u2014 the flame will show you exactly where the leak is."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the entry"
    print(text)


if __name__ == "__main__":
    main()
