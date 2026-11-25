"""The 3AM Fridge Text: write the one line a smart fridge texts its owner at 3am.

The line is fixed. It leans on the judge brief: a fridge that has been awake
for years, speaking up at 3am as a witness to its owner's late-night habits —
not the obvious milk, ice, or door-left-open joke. No input, no randomness,
no network, no clock: the same line on every run.
"""

LINE = "3am. I've been awake since 2019 and I've never once seen you eat a vegetable at this hour."


def _check_gate(line):
    """Mirror the sealed gate: UTF-8 text, 1 to 140 chars, not only whitespace,
    exactly one line."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(line))
    if line.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    line.encode("utf-8")
    return line


def main():
    import os

    line = _check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        on_disk = f.read()
    if on_disk != line:
        raise RuntimeError("entry.txt did not round-trip byte for byte")
    # Check the gate against what is actually on disk, not the in-memory
    # line: the file the judge reads is what has to pass.
    _check_gate(on_disk)
    print("%s (%d chars)" % (line, len(line)))


if __name__ == "__main__":
    main()
