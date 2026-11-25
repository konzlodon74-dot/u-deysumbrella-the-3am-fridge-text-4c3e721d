"""The 3AM Fridge Text.

One line: the text message a smart fridge sends its owner at 3am.
The fridge has been awake all night, watching every visit. It keeps
count of the door swings, it knows nothing was eaten, and it is not
telling anyone -- but it is telling you, right now, at 3am.
"""

import os

LINE = "3am. You opened me four times and ate nothing. I'm not mad, I'm just cold, awake, and keeping your secrets."


def validate(line: str) -> None:
    """The line must be a single non-blank line of 1-140 characters."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
