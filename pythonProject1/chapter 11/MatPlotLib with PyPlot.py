import matplotlib.pyplot as plt
names = ['apples', 'oranges', 'bananas']
values = [9, 13, 3]
plt.figure(figsize=(10, 3)) # width = 10, height = 3
plt.subplot(131) # 1 row, 3 columns, put this subplot in the first column
plt.bar(names, values)
plt.subplot(132) # 1 row, 3 columns, put this subplot in the second column
plt.scatter(names, values)
plt.subplot(133) # 1 row, 3 columns, put this subplot in the third column
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()