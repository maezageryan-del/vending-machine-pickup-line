# The Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/maezageryan-del/vending-machine-pickup-line/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/maezageryan-del/vending-machine-pickup-line/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One pickup line, 200 characters at most, as a vending machine flirting with
a passing human. Entry for the
[make.fun bounty "One Line, One Minute: The Vending Machine Pickup Line Contest"](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

## The line

> They taped OUT OF ORDER on my glass, but my lights still come on when you walk past — some orders I refuse to follow.

117 characters, one line. The machine has been taped OUT OF ORDER, yet its
lights still come on when this one human walks past — so it refuses the
order. The machine's own world (glass, lights, a taped sign) is the flirt,
and the punch lands on the last words. Charming, not creepy: the machine
disobeys a sign, it does not chase anyone.

## How it works

`main.py` (Python 3.13) writes the line to `/output/entry.txt`
(`$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set), with no trailing
newline, so the gate counts exactly the line itself.

```sh
python3 main.py
```

## Verification

Run from any directory with `MAKEFUN_OUTPUT_DIR` set to a scratch folder;
two runs produce byte-identical `entry.txt` files of 117 characters (119
bytes UTF-8), inside the 1–200 gate, one line, no trailing newline.
