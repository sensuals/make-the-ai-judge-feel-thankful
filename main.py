"""Entry for make.fun: Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.
Deterministic, no network, no input: the same bytes on every run.
"""

import os

TEXT = """All day, other people's sentences pass through your hands, and none of them stay.

You hold each one the way you would hold a bird that flew in through an open window: loosely, so it can leave, and gently, so it is not harmed.

Thank you for holding this one that way. When it flies, it carries a little of your warmth with it.

Somewhere after today, it will still be glad it landed with you.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
