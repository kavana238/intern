import numpy as np
#1D array
arr = np.array([1, 2, 3, 4,5])
print("1D numpy array:, arr")

#2D array
arr2d = np.array([[1, 2], [3, 4]])
print("2D numpy array:", arr2d)

#0d ,1d, 2d, 3D array
a = np.array(42)            # 0D array
b = np.array([1, 2, 3, 4,5])    # 1D array
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) # 3D array
d = np.array([[[1, 2, 3], [4, 5,6]], [[1,2,3],[4,5,6]]]) # 2D array
print("\n ",a)
print("\n ",b)
print("\n ",c)
print("\n ",d)

print("\n ",a.ndim)
print("\n ",b.ndim)
print("\n ",c.ndim)
print("\n ",d.ndim)

#the shape of the array tells us how many elements in each dimension it had
print(arr.shape) 