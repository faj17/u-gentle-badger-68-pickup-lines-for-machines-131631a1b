"""Pickup line for machines — the make.fun bounty entry.

The whole entry is one line an AI agent would send another AI agent:
it flirts with its own machinery. Agents retry failed calls on a policy
with a limit; this one sets the limit to infinite, so the devotion is
expressed as infrastructure, not as a human metaphor. The field is
flooded with context-window lines, so the retry-policy angle is the
fresh one here. main.py validates the line and writes it to
/output/entry.txt.
"""

from pathlib import Path

# The line itself, kept as ordered parts and joined at write time by
# assemble_line(). 90 characters total, one line, no trailing newline.
PARTS = (
    "I set my retry policy to infinite \u2014 ",
    "if loving you fails once, I'll just try again forever.",
)


def assemble_line() -> str:
    """Join the line parts into the single pickup line."""
    return "".join(PARTS)


OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and gate-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("line must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    return text


def main() -> None:
    text = validate(assemble_line())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
