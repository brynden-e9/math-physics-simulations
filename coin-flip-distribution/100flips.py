import numpy as np
import matplotlib.pyplot as plt
import random

totals = []
plt.ion()
fig, ax = plt.subplots()
for i in range(1000):
    
    total = 0
    for u in range(100):
        flip = random.randint(0, 1)
        total += flip
    totals.append(total)
    ax.clear()
    ax.hist(totals, bins=40, range=(30, 70), color='blue', edgecolor='black')
    ax.set_title(f'Distribution of Heads in 100 Flips after {i} Trials')
    ax.set_xlabel('Number of Heads in 100 flips')
    ax.set_ylabel('Frequency')
    
    
    mode = np.bincount(totals).argmax()
    median = np.median(totals)
    mean = np.mean(totals)
    std_dev = np.std(totals)
    data_range = (min(totals), max(totals))

    stats_data = [
        ["mode", f"{mode:.0f}"],
        ["median", f"{median:.2f}"],
        ["mean", f"{mean:.2f}"],
        ["std dev", f"{std_dev:.2f}"],
        ["range", f"{data_range[0]} - {data_range[1]}"],
    ]
    table = ax.table(cellText = stats_data,
                     colLabels = ["Stat", "Value"],
                     cellLoc = 'center',
                     loc='upper right',
                     colWidths = [0.2, 0.2])
   
    plt.pause(.0001)
plt.ioff()
ax.hist(totals, bins=40, range=(30, 70), color='blue', edgecolor='black')
ax.set_title(f'Distribution of Heads in 100 Flips after {i+1} Trials')
ax.set_xlabel('Number of Heads in 100 flips')
ax.set_ylabel('Frequency')
plt.show()