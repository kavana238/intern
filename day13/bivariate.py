#step 1 - import required libraries

from matplotlib import style
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# improve plot appearance
sns.set(style = 'whitegrid')


#step 2 - load the data/ craete dataset
# in real projects: df = pd.read_csv('data.csv')

data = {
    'age': [25, 30, 35, 40, 28, 32, 45, 50, 23, 36, 29, 41],
    'salary': [30000, 40000, 50000, 65000, 42000, 48000, 80000, 90000, 28000, 52000, 46000, 70000],
    'experience': [1, 3, 5, 10, 4, 6, 15, 20, 2, 7, 5, 12],
    'department': ['Sales', 'HR', 'IT', 'Finance', 'Sales', 'HR', 'IT', 'Finance', 'Sales', 'HR', 'IT', 'Finance'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']}

df = pd.DataFrame(data)
print(df)


#topic 2 - bivariate analysis
#analyze the relationship between two variables

#scatter plot - relationship between two numerical variables
plt.figure()
sns.scatterplot(x=df["age"], y=df["salary"])
plt.title("Age vs Salary")
plt.show()

#scatter plot - experience vs salary
plt.figure()
sns.scatterplot(x=df["experience"], y=df["salary"])
plt.title("Experience vs Salary")
plt.show()

#scatter plot - salary by gender
plt.figure()
sns.scatterplot(x="gender", y="salary", hue="gender", data=df)
plt.title("Salary by Gender")
plt.show()

#box plot salary by gender
plt.figure()
sns.boxplot(x="gender", y="salary", data=df)
plt.title("Salary by Gender")
plt.show()

# box plot salary by department
plt.figure()
sns.boxplot(x="department", y="salary", data=df)
plt.title("Salary by Department")
plt.show()

# tpoic 4 - correlation analysis

#correlation matrix - numerical columns only 
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

#heatmap of correlation matrix
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
# annot = true -> shows correlation values 
#cmap => change color scheme of the heatmap
#line widths => adds grid lines


#topic 5 - outliers detection
#box plot for age 
plt.figure()
sns.boxplot(x=df["age"])
plt.title("Age outliers")
plt.show()

#box plot for experience
plt.figure()
sns.boxplot(x=df["experience"])
plt.title("Experience outliers")
plt.show()

#FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.


print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")