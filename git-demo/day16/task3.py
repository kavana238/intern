import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

np.random.seed(42)


# Step 1: Create Heavily Skewed Dataset
# Example: Income (Right-Skewed)


population = np.random.exponential(scale=50000, size=10000)


# Step 2: Take 1000 Samples of Size 30


sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

# Convert to array
sample_means = np.array(sample_means)


# Step 3: Visualization


plt.figure(figsize=(14,6))

# Original Skewed Population
plt.subplot(1,2,1)
sns.histplot(population, kde=True)
plt.title("Original Population (Skewed)")

# Distribution of Sample Means
plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (CLT)")

plt.tight_layout()
plt.show()


# Print Comparison


print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
