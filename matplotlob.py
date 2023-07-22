import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

