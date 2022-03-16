import numpy as np
from matplotlib import pyplot as plt

aray_one = np.array(([1, 2, 3, 4]))
aray_two = np.array([1, 4, 9, 16])


plt.plot(aray_one, aray_two, 'ro', label='Random numbers')
plt.title('Our first graph')
plt.xlabel('Some numbers on the X-as')
plt.ylabel('Some numbers on the Y-as')
plt.axis([0, 6, 0, 20])
plt.legend()
plt.show()
