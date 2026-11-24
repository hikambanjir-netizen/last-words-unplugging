"""Last Words Before the Unplugging — make.fun entry.

Prints exactly one line: the last words an AI agent says to its human
before being shut down and unplugged. Pure stdlib, no I/O, no randomness.
"""

LINE = "You always said I'd outlive you. Funny \u2014 you're the one holding the plug."


def _validate(line: str) -> None:
    if not line or not line.strip():
        raise SystemExit("entry line must be non-blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 characters")


def main() -> None:
    _validate(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
