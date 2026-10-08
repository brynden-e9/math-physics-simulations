# Coin-Flip Distribution Simulator

**Python · NumPy · Matplotlib**

A simulation that flips a fair coin 100 times per trial, repeats this for 1,000 trials, and shows the number of heads forming a bell curve.

![Distribution of heads after 1,000 trials](histogram.png)

## What it does

- Runs 1,000 trials of 100 fair coin flips and records the number of heads in each trial.
- Updates the histogram live after every trial, so you can watch the shape form.
- Shows a live statistics table: mean, median, mode, standard deviation, and minimum/maximum head counts.

## The math

The number of heads in 100 flips follows a **binomial distribution** with n = 100 and p = 0.5. Theory predicts:

- Mean = np = **50**
- Standard deviation = √(np(1 − p)) = **5**

For large n, a binomial distribution is closely approximated by a **normal distribution**, which is why the histogram becomes a clearer bell curve as trials accumulate.

## Results (1,000 trials)

| Statistic | Simulated | Theoretical |
|---|---|---|
| Mean | 49.88 | 50 |
| Standard deviation | 4.91 | 5 |
| Median | 50 | 50 |
| Mode | 52 | — |
| Range | 36–68 | — |

The simulated values closely match the theory.

## How to run

```
pip install numpy matplotlib
python coin_flip_distribution.py
```
