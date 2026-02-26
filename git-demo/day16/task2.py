import numpy as np
import pandas as pd


# Step 1: Create Sample Dataset


np.random.seed(42)

# Example: Student SAT Scores
scores = np.random.normal(loc=1000, scale=150, size=50)

# Add some extreme values manually
scores = np.append(scores, [400, 1600, 1700])

df = pd.DataFrame({
    "SAT_Score": scores
})

# Step 2: Calculate Mean and Standard Deviation


mu = df["SAT_Score"].mean()
sigma = df["SAT_Score"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)


# Step 3: Create Z-Score Column
# Formula: Z = (x - μ) / σ


df["z_score"] = (df["SAT_Score"] - mu) / sigma


# Step 4: Identify Outliers
# Condition: |Z| > 3


outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)
