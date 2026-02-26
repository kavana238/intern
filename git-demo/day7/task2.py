import numpy as np

# Step 1: Create 1D array
data = np.arange(24)

# Step 2: Reshape into (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)

# Step 3: Transpose to (4, 2, 3)
final_data = reshaped_data.transpose(0, 2, 1)

print("Final Shape:", final_data.shape)
print("Final Array:")
print(final_data)
