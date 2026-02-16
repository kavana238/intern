import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (change path if needed)
df = pd.read_csv("E:/intership/day13/data.csv")

# Correlation Matrix
corr_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:\n")
print(corr_matrix)

# Heatmap Visualization
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

#  Identify Correlation > 0.8

print("\nHighly Correlated Pairs (>|0.8|):\n")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            value = corr_matrix.iloc[i, j]
            print(f"{col1} and {col2} --> {value:.2f}")

#  Boxplot for Outliers (Price)

plt.figure(figsize=(6,4))
sns.boxplot(y=df['Price'])
plt.title("Boxplot of Price")
plt.show()
