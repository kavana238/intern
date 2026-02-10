import numpy as np

arr = np.arange(40,55,3)
print("array of numbers:", arr)

#2D array
print(arr.shape)
arr_1 = np.arange(1,17).reshape(4,4)
print(arr_1)

#np.linspace(start, stop, num) returns num evenly spaced samples, calculated over the interval [start, stop]
arr = np.linspace(0, 2, 5)
print(arr)

#random values
arr = np.random.rand(2,2)
print(arr)
