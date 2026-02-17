import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample Data
df = pd.DataFrame({
    "Age": [21, 25, 30, 35, 40, 45, 50],
    "Salary": [20000, 25000, 30000, 40000, 60000, 80000, 100000]
})

print("Original Data:\n", df)


#1 Standardization

scaler_standard = StandardScaler()
standardized_data = scaler_standard.fit_transform(df)

df_standardized = pd.DataFrame(standardized_data, columns=df.columns)

print("\nStandardized Data:\n", df_standardized)

# 2 Normalization (Min-Max)

scaler_minmax = MinMaxScaler()
normalized_data = scaler_minmax.fit_transform(df)

df_normalized = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Data:\n", df_normalized)


# 3 Plot Histogram (Before & After Scaling)

# Plot for Salary (example feature)
plt.figure(figsize=(12,4))

# Original
plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary")

# Standardized
plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary")

# Normalized
plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()
