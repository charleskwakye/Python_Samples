import numpy as np

points_linux = np.loadtxt(fname='Files_Chapter_11/points_linux.csv', delimiter=';', dtype=int)
points_python = np.genfromtxt(fname='Files_Chapter_11/points_python.txt', delimiter=';', dtype=int, filling_values=0)
points_web = np.loadtxt(fname='Files_Chapter_11/points_web.txt', delimiter=';', dtype=int)
points_networks = np.genfromtxt(fname='Files_Chapter_11/points_networks.csv', delimiter=';', dtype=int)


linux_python = np.add(points_linux,points_python)
print(linux_python)