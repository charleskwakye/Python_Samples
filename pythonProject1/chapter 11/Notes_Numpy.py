# import numpy as np
# #  Printing each element in array numbered with their indexes
# measurement = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
# print(len(measurement))
#
# for i in range(measurement.size):
#     print(i, measurement[i])

# # This is OUTPUT
#  #6
#  #0 2.3
#  #1 8.6
#  #2 7.0
#  #3 6.5
#  #4 2.5
#  #5 3.4

####################################

# import numpy as np
# measurements = np.array((3, 6, 9, 12),int)
# print(measurements)
#
# division = measurements/3
# print(division)

# # OUTPUT

# # [ 3 6 9 12]
# # [1. 2. 3. 4.]


# # PERFORMING MATHS TO AN ARRAY
# import numpy as np
# price_without_vat = np.array([100, 78.60, 60.99, 45, 1], float)
# print(price_without_vat)
#
# price_with_vat = np.around(price_without_vat * 1.21, 2)
#
# print(price_with_vat)
#
# # Combined the two arrays prices
# all_prices = np.append(price_without_vat,price_with_vat)
# print(all_prices)


####################
# # APPENDING ARRAY
# import numpy as np
# measurement = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
# new_measurement = np.array([5.2, 3.5], float)
#
# combined_array = np.append(measurement, new_measurement)
# print(combined_array)

# #OUTPUT
# #[2.3 8.6 7.  6.5 2.5 3.4 5.2 3.5]

# # INSERTING ARRAY
# import numpy as np
# measurement = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4], float)
# add_measurement = np.array([5.2, 3.5], float)
# new_measurement = np.insert(measurement,3,add_measurement)
# print(measurement)
# print(add_measurement)
# print(new_measurement)

# # OUTPUT
# # [2.3 8.6 7.  6.5 2.5 3.4]
# # [5.2 3.5]
# # [2.3 8.6 7.  5.2 3.5 6.5 2.5 3.4]


# # Methods min(), max(), mean(), sum(),
# import numpy as np
# measurements = np.array([2.3, 8.6, 7, 6.5, 2.5, 3.4],float)
# print('Amount of measurements: ', len(measurements))
#
# for i in range(measurements.size):
#     print(measurements[i])
# print('Highest measurement : ', measurements.max())
# print('Lowest measurement : ', measurements.min())
# print('Average measurement : ', measurements.mean())
# print('Sum of measurements : ', measurements.sum())

# # Amount of measurements: 6
# # 2.3
# # 8.6
# # 7.0
# # 6.5
# # 2.5
# # 3.4
# # Highest measurement: 8.6
# # Lowest measurement: 2.3
# # Average: 5.05
# # Sum of measurements 30.299999999999997

# # 2-Dimensional array
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
#

# # 0 - [12, 9, 15]
# # 1 - [16, 11, 13]
# # 2 - [9, 18, 9]
# # 3 - [15, 16, 12]
# #       |  |   |
# #       0  1   2

# print('Position 0-0: ', points[0][0])
# print('Position 1-1: ', points[1][1])
# print('Position 2-2: ', points[2][2])
# print('Position 3-2: ', points[3][2])
# print('Length: ', len(points))
# print('Size: ', points.size)

# # OUTPUT
# # Position 0-0:  12
# # Position 1-1:  11
# # Position 2-2:  9
# # Position 3-2:  12
# # Length:  4
# # Size:  12


# # Retrieve numbers of columns and rows
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# print(points)
# print(points.shape)
# print('Number of rows: ', points.shape[0])
# print('Number of columns: ', points.shape[1])

# # OUTPUT
# # [[12  9 15]
# # [16 11 13]
# # [ 9 18  9]
# # [15 16 12]]
# # (4, 3)
# # Number of rows:  4
# # Number of columns:  3

# # Print 2 - dimensional array
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# for list in range(len(points)):
#     for number in range(points[list].size):
#         print(points[list][number], end='\t')
#     print()

# # OUTPUT
# # 12	9	15
# # 16	11	13
# # 9	18	9
# # 15	16	12

# # Method sum()
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# print('Total per course', points.sum(0))
# print('Total per course', np.sum(points, axis=0))
# print('Total per course ', points.sum(1))
# print('Total per student', np.sum(points, axis=1))

# # OUTPUT
# # Total per course [52 54 49]
# # Total per course [52 54 49]
# # Total per course  [36 40 36 43]
# # Total per student [36 40 36 43]

# # Methods amin(), min(), amax(), max()
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# print('Lowest: ', np.amin(points, axis=0))
# print('Lowest: ', np.min(points, axis=0))
#
# print('Highest: ', np.max(points, axis=0))
# print('Highest: ', np.amax(points, axis=0))

# # OUTPUT
# # Lowest:  [9 9 9]
# # Lowest:  [9 9 9]
# # Highest:  [16 18 15]
# # Highest:  [16 18 15]

#######################################
# # Method mean()
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# print('Average axis 0:', np.mean(points, axis=0))
# print('Average axis 1:', np.mean(points, axis=1))

# # OUTPUT
# # Average axis 0: [13.   13.5  12.25]
# # Average axis 1: [12.         13.33333333 12.         14.33333333]

#############################################
# # Slicing 2d array
# import numpy as np
# points = np.array([[12, 9, 15], [16, 11, 13], [9, 18, 9], [15, 16, 12]])
# print(points[0,:])
# print(points[:,0])
# print(points[:,1])
# print(points[0:2,:])

# # OUTPUT
# # [12  9 15]
# # [12 16  9 15]
# # [ 9 11 18 16]
# # [[12  9 15]
# # [16 11 13]]
