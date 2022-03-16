# chapter 11 exercise 5 -> arrays
import numpy as np
import matplotlib.pyplot as plt


def convert(import_file):  # presume big data
    data = np.loadtxt(import_file, delimiter=';', dtype=float)  # 2d creating
    data[:, 1] = (data[:, 1]-32)*5/9   # 2e column of 2D -> slicing
    return data


# main program ------------------------------------------------------------------
# print(convert('Files_chapter11/degrees_fahrenheit.txt'))
converted_data = convert('Files_chapter_11/degrees_fahrenheit.txt')
plt.plot(converted_data[:, 0], converted_data[:, 1])  # x= 1st column | y= 2nd column
plt.title('Degrees Celsius')
plt.xlabel('Datapoints')
plt.xticks(rotation=90)
plt.ylabel('Temperature')
plt.show()
