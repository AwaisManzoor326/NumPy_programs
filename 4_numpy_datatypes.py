import numpy as np


#                    i - integer
#                    b - boolean
#                    u - unsigned integer
#                    f - float
#                    c - complex float
#                    m - timedelta
#                    M - datetime
#                    O - object
#                    S - string
#                    U - unicode string
#                    V - fixed chunk of memory for other type ( void )


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr.dtype) # prints datatype of array elements

# arr = np.array(['apple', 'banana', 'cherry']) # prints U6. unicode string with max 6 characters
# print(arr.dtype) 

# arr = np.array([12, 244, 3, 4], dtype='S')  # prints byte string b'' and max 3 character string S3
# print(arr)
# print(arr.dtype)



# arr = np.array([1, 2, 3, 4], dtype='i4') # 4 bytes or 32 bits data
# print(arr)
# print(arr.dtype)




# arr = np.array(['a', '2', '3'], dtype='i')  # it will raise error because 'a' can't be converted to integer




# best practice to change datatype of array elements is making its copy by astype() method
# newarr = arr.astype(float) # converts to float
# #      ........OR........
# newarr = arr.astype('f') # converts to float
# print(newarr)


newar = arr.astype(bool)
print(newar)
