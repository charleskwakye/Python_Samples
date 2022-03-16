import numpy as np
loaded_data = np.loadtxt(fname='Files_Chapter_11/student_grades_3.csv', delimiter=';', dtype=int, skiprows=1)
print(type(loaded_data))
print(loaded_data)

min = np.min(loaded_data, axis=0)
max = np.max(loaded_data, axis=0)
average = np.mean(loaded_data, axis=0)

print('Grade analysis Python: ')
print('max', max[0], 'min', min[0], 'mean', average[0])

print('Grade analysis Linux: ')
print('max', max[1], 'min', min[1], 'mean', average[1])

print('Grade analysis Routing and switching: ')
print('max', max[2], 'min', min[2], 'mean', average[2])


