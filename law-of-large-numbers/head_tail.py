import random
import matplotlib.pyplot as plt

heads_tails = [0, 0]
heads_ratio = []
tails_ratio = []

plt.ion()
fig, ax = plt.subplots()

# initialize lines once
line_heads, = ax.plot([], [], 'b-', label='Heads ratio')
line_tails, = ax.plot([], [], 'r-', label='Tails ratio')

ax.set_xlim(1, 1000)
ax.set_ylim(0, 1)
ax.set_xlabel('Number of Flips')
ax.set_ylabel('Ratio')
ax.legend()
for i in range(1000):
    heads_tails[random.randint(0, 1)] += 1
    total = sum(heads_tails)

    heads_ratio.append(heads_tails[0] / total)
    tails_ratio.append(heads_tails[1] / total)

    # update line data
    line_heads.set_data(range(1, i+2), heads_ratio)
    line_tails.set_data(range(1, i+2), tails_ratio)

    ax.set_title(f"Heads and Tails Ratio Over {i+1} Flips")
    plt.pause(0.001)

plt.ioff()
plt.show()