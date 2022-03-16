import matplotlib.pyplot as plt
import numpy as np
labels = 'Cricket', 'Football', 'Hockey', 'Formula1'
sports_data = np.array([15, 30, 45, 10])

plt.pie(sports_data, labels = labels,autopct='%1.1f%%')
plt.title('Sports')
plt.legend()  # if asked
plt.show()