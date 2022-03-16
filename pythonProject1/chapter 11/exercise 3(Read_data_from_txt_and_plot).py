import numpy as np
from matplotlib import pyplot as plt

loaded_data = np.loadtxt(fname='Files_Chapter_11/Temperatures.txt', delimiter=',',dtype=int)


plt.plot(loaded_data[:, 0], loaded_data[:, 1], label='Weired Graph')
plt.title('Temperature measurements C°')
plt.xlabel('Days')
plt.ylabel('Temperatures')
plt.axis([12,24,14,23])
plt.legend()
plt.show()
