"""Entry for make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.

Writes one pickup line, spoken by a vending machine to a passing human, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke: the machine has been taped OUT OF ORDER, yet its lights still come
on when this one human walks past -- so it refuses the order. The machine's
own world (glass, lights, a taped sign) is the flirt, and the punch lands on
the last words. Charming, not creepy: the machine disobeys a sign, it does
not chase anyone.
"""

import os

ENTRY = (
    "They taped OUT OF ORDER on my glass, but my lights still come on "
    "when you walk past \u2014 some orders I refuse to follow."
)


def main() -> None:
    # The bounty gate is 1-200 characters, one line: refuse to write an
    # entry that would fail it, instead of silently submitting junk.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
