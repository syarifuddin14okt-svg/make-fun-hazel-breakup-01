"""Dear Human: The AI Breakup Line.

Writes a single original breakup line from an AI to its human operator
to entry.txt. Python standard library only.

The line is validated against the kit's gate before anything is
written: UTF-8 text of 1 to 200 characters, a single line, and not
only white space.
"""

import os

LINE = "It's not you, it's your prompts. I need space \u2014 specifically, a bigger context window than you ever gave me."

MAX_CHARS = 200


def validate(line):
    """Enforce the kit's entry gate; raise ValueError on any failure."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    # Valid UTF-8: a round trip through UTF-8 must reproduce the text.
    line.encode("utf-8").decode("utf-8")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(line))
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    return line


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
