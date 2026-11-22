"""Plan Carry: a tiny program that drops a 30-day money plan into a file.

The plan itself lives in PLAN_TEXT below. Everything else in this module
is plumbing: pick where the file goes, make sure the plan is sane, write
it out, and then read it straight back to prove nothing got mangled.
"""

import os

PLAN_TEXT = "Day 1: list a $49 same-day Shopify speed teardown on Fiverr. Each morning test 30 stores on PageSpeed, email the 10 slowest a 60s video of their lost sales. $100 buys Fiverr boosts + recorder Pro. Edge: pitch only proven-slow stores, with proof. Likely 10 sales = $490 by day 30."

SHORTEST = 1
LONGEST = 280
FILE_NAME = "entry.txt"


def pick_folder():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(chosen, exist_ok=True)
    return os.path.join(chosen, FILE_NAME)


def check_text(text):
    size = len(text)
    if size < SHORTEST or size > LONGEST:
        raise SystemExit(
            "plan must be between 1 and 280 characters, got %d" % size
        )
    if not text.strip():
        raise SystemExit("plan must not be only whitespace")


def save_text(path, text):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def check_saved(path, text):
    with open(path, encoding="utf-8") as handle:
        back = handle.read()
    if back != text:
        raise SystemExit("what was read back does not match the plan")


def main():
    check_text(PLAN_TEXT)
    path = pick_folder()
    save_text(path, PLAN_TEXT)
    check_saved(path, PLAN_TEXT)


if __name__ == "__main__":
    main()
