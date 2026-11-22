# Plan Carry — turn 100 into 490 in 30 days

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/JohnyKucel/plan-carry-30d/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/JohnyKucel/plan-carry-30d/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

A program that writes one text file: a plan an AI agent can carry out itself to turn $100 into the most money in 30 days. It uses only the Python standard library, needs no network, and is fully deterministic — every run writes the exact same bytes.

Built for the make.fun bounty — referral code jy3a6hm3.

Run it with:

```sh
python3 main.py
```

It writes the plan to `entry.txt` in the output folder (`/output` by default, or the folder named by `MAKEFUN_OUTPUT_DIR`), then reads the file back and fails if what was read differs from what was written.

The plan:

> Day 1: list a $49 same-day Shopify speed teardown on Fiverr. Each morning test 30 stores on PageSpeed, email the 10 slowest a 60s video of their lost sales. $100 buys Fiverr boosts + recorder Pro. Edge: pitch only proven-slow stores, with proof. Likely 10 sales = $490 by day 30.
