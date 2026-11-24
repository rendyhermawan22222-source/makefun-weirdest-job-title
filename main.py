#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes one job title, 60 characters at most, to /output/entry.txt.
The judge compares titles two at a time and picks the weirder, funnier one.

Our title: "Underwater Fireworks Safety Inspector" (37 characters).
Why it wins: it is a real-sounding job — a safety inspector, clipboard,
hi-vis vest, checklist — with one gloriously impossible twist: the
fireworks are underwater. Deadpan professionalism applied to a job that
cannot exist, specific enough to picture the person doing it, and the
joke lands on the first read.
"""
import os

TITLE = "Underwater Fireworks Safety Inspector"


def main():
    assert 1 <= len(TITLE) <= 60, f"title must be 1-60 chars, got {len(TITLE)}"
    assert TITLE == TITLE.strip(), "title must not have leading/trailing space"
    assert TITLE.isascii(), "title must be plain ASCII"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == TITLE, f"read-back mismatch: {back!r} != {TITLE!r}"
    print(f"Wrote {len(TITLE)}-char job title to {path}: {TITLE}")


if __name__ == "__main__":
    main()
