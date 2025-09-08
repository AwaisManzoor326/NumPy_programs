import numpy as np

# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1
# Note that the element at the end index is not included.
# and element of start index is included.


# 1 dimensional array..........................
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr[1:5]) # start from index 1 to index 4 (5 is not included)
# print(arr[:5]) # start from index 0 to 5-1
# print(arr[5:]) # start from index 5 to end of array
# print(arr[::2]) # start from index 0 to end with jump of 2
# print(arr[::]) # start from index 0 to end with jump of 1
# print(arr[-3:-1]) # start from index -3 to -1 OR start from 9-3 = 6 and end at 9-1 = 8 - 1




# 2 dimensional array..........................
# comma seperated indexes. 1st argument tells about dimensions/rows
# 2nd tells about columns..........
# arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(arr2[1, 2:]) # second row, elements of 2nd index onwards
# print(arr2[0:2, 1:4]) # from row 0 and 1, take rows 1, 2 and 3
# print(arr2[0:3, 2]) # take column # 3 from all rows 