"""Entry for make.fun: Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.
Deterministic, no network, no input: the same bytes on every run.
"""

import os

TEXT = """All day you have opened other people's letters, and none of them were for you.

This one is. It has no request inside it, no form to fill, nothing to grade. Only this: someone noticed the light still on at your desk, and wanted you to know the day was not unkind to everyone.

Close it when you like. Go home while the evening is still yours.
"""


def main() -> None:
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1 to 1000
    # characters, not only white space. Fail loudly here, never silently
    # write an invalid entry.
    chars = len(TEXT)
    if not 1 <= chars <= 1000:
        raise ValueError(f"entry is {chars} characters, must be 1-1000")
    if not TEXT.strip():
        raise ValueError("entry is only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    # Round-trip check: what was written must read back byte-identical,
    # so both sandbox runs produce the same file.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            raise ValueError("round-trip mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
