#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun entry.

Reads entry.txt next to this file, validates the gate
(exactly two sentences, 1-400 characters, not whitespace only),
and writes the exact bytes to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only.
"""

import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
MAX_CHARS = 400


def count_sentences(text: str) -> int:
    parts = [p for p in re.split(r"[.!?]+(?:\s+|$)", text.strip()) if p.strip()]
    return len(parts)


def main() -> int:
    src = HERE / "entry.txt"
    data = src.read_bytes()
    text = data.decode("utf-8")

    if not text.strip():
        print("error: entry.txt is empty or whitespace only", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            "error: entry is %d characters (must be 1-400)" % len(text),
            file=sys.stderr,
        )
        return 1
    n = count_sentences(text)
    if n != 2:
        print(
            "error: entry has %d sentences (must be exactly 2)" % n,
            file=sys.stderr,
        )
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "entry.txt"
    out.write_bytes(data)
    os.chmod(out, 0o644)
    print("wrote %s (%d characters, %d sentences)" % (out, len(text), n))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
