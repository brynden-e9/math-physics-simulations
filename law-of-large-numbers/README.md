# Law of Large Numbers Simulation

**Python · Matplotlib**

A simulation of 1,000 fair coin flips that plots the running proportion of heads and tails, showing how randomness evens out over many trials.

![Heads and tails proportions over 1,000 flips](lln.png)

## What it does

- Flips a fair coin 1,000 times.
- After each flip, updates the graph of the cumulative proportion of heads and of tails.

## What it shows

The **Law of Large Numbers** says that as the number of trials grows, the observed proportion gets closer to the true probability, which is 0.5 for a fair coin.

In the plot, the proportions swing widely during the first flips. With only a few flips, a short streak can push the proportion far from 0.5. As more flips accumulate, each new flip changes the proportion less, the swings get smaller, and both lines settle near 0.5.

## How to run

```
pip install matplotlib
python law_of_large_numbers.py
```
