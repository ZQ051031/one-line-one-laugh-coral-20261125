"""One Line, One Laugh -- entry writer.

Writes a single funny line to /output/entry.txt.

Standard library only. Deterministic: the line is a fixed string, so every
run produces byte-identical output. No trailing newline: the gate counts
characters, and the line is the whole entry.
"""

from pathlib import Path

LINE = (
    "My smart fridge studied my diet for a week, sighed, ordered pizza, "
    "and billed my willpower a monthly service fee."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate guard: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
