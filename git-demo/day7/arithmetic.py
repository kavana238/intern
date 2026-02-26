import numpy as np
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


#broadcasting
arr = np.array([1, 2, 3])
print(arr +5)


#broadcasting with different shapes
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])
vector = np.array([10, 20, 30])
print(matrix + vector)
