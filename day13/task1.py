import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("E:/intership/day13/data.csv")

# Histogram
sns.histplot(df['Price'], kde=True)
plt.show()

# Skewness & Kurtosis
print("Skewness:", df['Price'].skew())
print("Kurtosis:", df['Price'].kurt())

# Count Plot
sns.countplot(x='City', data=df)
plt.show()
