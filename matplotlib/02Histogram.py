import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

N = 100000
x = np.linspace(0, 100, N)
y = 100 + 15*np.random.randn(N)
colors = y


plt.figure(1)
ax1 = plt.subplot(211) # 2 rows, 1 column, figure 1

plt.scatter(x, y, c=colors, cmap='cool', alpha=0.2)
ax2 = plt.subplot(212) # 2 rows, 1 column, figure 2
n, bins, patches = plt.hist(y, 100, normed=1, color='b',  alpha=0.75)
plt.grid(True)
print(n, bins, patches)


plt.show()