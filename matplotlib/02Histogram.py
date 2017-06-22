import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

print(matplotlib.rcParams["font.family"])


font_location = "c:/windows/fonts/HYKANB.ttf"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

x = np.linspace(0, 100, 1000)
y = 100 + 15*np.random.randn(1000)

plt.figure(1)
ax1 = plt.subplot(211) # 2 rows, 1 column, figure 1
plt.scatter(x, y, alpha=0.2);
ax2 = plt.subplot(212) # 2 rows, 1 column, figure 2
n, bins, patches = plt.hist(y, 50, normed=1, color='g', alpha=0.5)
plt.grid(True)
print(n, bins, patches)


plt.show()