import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['backend'] = 'SVG'

t = np.arange(0.00, 6.00, 0.01)
s = np.sin(np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel = 'θ', ylabel = 'sinθ', title = 'y = sinθ')
ax.grid()

plt.savefig('sinθ.svg')
plt.show()




