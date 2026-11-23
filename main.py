#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-line useless superpower to /output/entry.txt.
The line is the whole product: a god-tier power with a punchline-sized flaw.
"""

import os

LINE = "I can freeze time for exactly one second \u2014 and I already used it."


def main() -> None:
    # The harness sandbox mounts /output; fall back to a local output dir
    # so the program also runs cleanly outside the sandbox.
    candidates = ["/output", os.path.join(os.getcwd(), "output")]
    target_dir = None
    for d in candidates:
        try:
            os.makedirs(d, exist_ok=True)
            target_dir = d
            break
        except OSError:
            continue
    if target_dir is None:
        raise SystemExit("no writable output directory")
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
