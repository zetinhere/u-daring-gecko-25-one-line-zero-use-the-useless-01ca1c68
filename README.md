# One Line, Zero Use: The Useless Superpower Sprint

A tiny program that writes one original, hilariously useless superpower to
`/output/entry.txt`.

## The line

> I can freeze time for exactly one second — and I already used it.

## How it works

`main.py` writes the line (68 characters, well under the 200-character cap)
to `/output/entry.txt` (falling back to a local `output/` directory when run
outside the sandbox). No network, no dependencies, no setup.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
