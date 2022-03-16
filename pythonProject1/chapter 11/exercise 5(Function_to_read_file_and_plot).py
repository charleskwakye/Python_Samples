import numpy as np
import matplotlib.pyplot as plt

def convert(import_file):
    loaded_data = np.loadtxt(import_file, delimiter=';', dtype=float)
    loaded_data[:,1] = (loaded_data[:,1]-32)*5/9
    return loaded_data

converted_data = convert('Files_Chapter_11/degrees_fahrenheit.txt')
plt.plot(converted_data[:,0], converted_data[:,1])
plt.title('Degree Celcius')
plt.xlabel('Datapoints')
plt.xticks(rotation=90)
plt.ylabel('Temperature')
plt.show()
