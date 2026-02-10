#reshape
import numpy as np
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)


#vstack
import numpy as np

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)