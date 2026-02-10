import numpy as np

#simple indexing
arr = np.array([[1, 2, 3, 4,5],[6, 7, 8, 9, 10]])
print("2nd element on 1st row:", arr[0, 1]) #arr[row,column]

#3d indexing
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[0,1,2]) #arr[axix,row,column]

#1d slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #start index is included and end index is excluded