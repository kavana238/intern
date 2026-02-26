import numpy as np

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Mean (axis=0):", np.mean(data, axis=0))
print("Mean (axis=1):", np.mean(data, axis=1))

print("Median (axis=0):", np.median(data, axis=0))
print("Std Dev (axis=1):", np.std(data, axis=1))


import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
