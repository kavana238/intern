import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("E:/intership/day13/data.csv")

plt.figure(figsize=(8,5))
sns.scatterplot(x='Area_sqft', y='Price', data=df)
plt.title("Area_sqft vs Price")
plt.xlabel("Area_sqft")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='City', y='Price', data=df)
plt.title("Price Distribution Across Cities")
plt.xticks(rotation=45)
plt.show()
