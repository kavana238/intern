import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Generate Datasets


np.random.seed(42)

#  Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

#  Right-Skewed Distribution (Household Income)
income = np.random.exponential(scale=50000, size=1000)

#  Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=15, size=1000)
scores = np.clip(scores, 0, 100)  # Keep scores between 0 and 100



# Create DataFrame

df = pd.DataFrame({
    "Heights (Normal)": heights,
    "Income (Right-Skewed)": income,
    "Scores (Left-Skewed)": scores
})



# Visualization


plt.figure(figsize=(15, 10))

# --- Normal ---
plt.subplot(3,1,1)
sns.histplot(df["Heights (Normal)"], kde=True)
plt.title("Normal Distribution - Human Heights")
plt.axvline(df["Heights (Normal)"].mean(), color='r', linestyle='--', label='Mean')
plt.axvline(df["Heights (Normal)"].median(), color='g', linestyle='-', label='Median')
plt.legend()

# --- Right Skewed ---
plt.subplot(3,1,2)
sns.histplot(df["Income (Right-Skewed)"], kde=True)
plt.title("Right-Skewed Distribution - Household Income")
plt.axvline(df["Income (Right-Skewed)"].mean(), color='r', linestyle='--', label='Mean')
plt.axvline(df["Income (Right-Skewed)"].median(), color='g', linestyle='-', label='Median')
plt.legend()

# --- Left Skewed ---
plt.subplot(3,1,3)
sns.histplot(df["Scores (Left-Skewed)"], kde=True)
plt.title("Left-Skewed Distribution - Easy Exam Scores")
plt.axvline(df["Scores (Left-Skewed)"].mean(), color='r', linestyle='--', label='Mean')
plt.axvline(df["Scores (Left-Skewed)"].median(), color='g', linestyle='-', label='Median')
plt.legend()

plt.tight_layout()
plt.show()


# Mean vs Median Comparison


print("Heights → Mean:", df["Heights (Normal)"].mean(), 
      "| Median:", df["Heights (Normal)"].median())

print("Income → Mean:", df["Income (Right-Skewed)"].mean(), 
      "| Median:", df["Income (Right-Skewed)"].median())

print("Scores → Mean:", df["Scores (Left-Skewed)"].mean(), 
      "| Median:", df["Scores (Left-Skewed)"].median())
