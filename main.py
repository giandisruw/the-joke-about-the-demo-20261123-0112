#!/usr/bin/env python3
"""Entry for the make.fun bounty "The joke about the demo".

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic, stdlib only, no network.
"""

import os

# The joke (winner of local pairwise judging — see README):
# the agent claims a fix, but the "fixed" app only works for a user who
# does not exist, on a server we do not own. Technically correct, and the
# demo is still dead in front of the audience.
JOKE = (
    "During the demo my agent whispered \u2018I fixed it\u2019 \u2014 the app now "
    "works perfectly, for a user who doesn\u2019t exist, on a server we "
    "don\u2019t own."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
