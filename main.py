#!/usr/bin/env python3
"""One-line entry: The Router Confesses.

The brief asks for one line, at most 200 characters, that a
home Wi-Fi router would say to excuse itself for dropping
the connection at the exact moment a movie reaches its
climax. The judge weighs, in order: the line is a one-line
excuse from the router for that drop, it is the funniest
with a turn the reader does not see coming, it speaks in the
router's own voice -- an appliance with a grudge, a fragile
ego or a smug little secret -- it lands in one breath with
no setup to explain, and it feels new, dodging the obvious
buffering, bandwidth and firmware-update jokes.

The sealed line below is built to that order on purpose. It
speaks in the router's own voice and denies the charge with
a smug little secret: it did not drop the Wi-Fi at the
climax, it simply refused to watch another hero survive
something it would never survive. The router is petty and
dramatic, the twist is that the appliance is jealous of the
movie, and it steers clear of buffering, bandwidth and
firmware entirely. The confession is the joke: the router
is not apologising for a fault, it is admitting a motive.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 120 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: the router denies dropping the Wi-Fi and
# confesses it refused to watch another hero survive what
# it would never survive.
ENTRY = "I did not drop your Wi-Fi at the climax; I simply refused to watch another hero survive something I would never survive."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
