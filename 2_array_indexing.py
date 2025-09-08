import numpy as np


# indexing 1-dimensional arrays................

# arr1 = np.array([10, 20, 30, 40, 50])
# print(arr1[0])  # Output: 10
# print(arr1[-1]) # Output: 50
# print(arr1[3] + arr1[1]) #output: 60



# indexing 2-dimensional arrays................
# dimensions represent rows and indeses represents columns..........
# 1st attribute is row and 2nd attribute is column.........

# arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2[2, 1])  # Output: 8 (3rd row, 2nd column)
# print(arr2[0, 0] + arr2[1, 2])  # Output: 7 (1st row, 1st column + 2nd row, 3rd column)
# print(arr2[1])  # Output: [4 5 6] (2nd row)
# print(arr2[:, 1])  # Output: [2 5 8] (all rows, 2nd column)
# print(arr2[1, :])  # Output: [4 5 6] (2nd row, all columns)






# indexing 3-dimensional arrays................
# 1st index represents block/ 2-d array number and 2nd attribute is row and 3rd attribute is column.........

# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3[1, 0, 2])  # Output: 9 (2nd block, 1st row, 3rd column)





# we can do negative indexing also.........
# -1 refers to last element, -2 refers to 2nd last element and so on.......