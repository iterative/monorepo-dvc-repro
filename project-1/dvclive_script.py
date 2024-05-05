import numpy as np
import matplotlib.pyplot as plt
from dvclive import Live


x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.plot(x, y, 'o', color='tab:brown')


with Live() as live:
    live.log_image("scatter_fit.png", fig)