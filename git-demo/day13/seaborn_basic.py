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


#data set inspection
#view first  and last rows

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

#dataset shape
print("\ndataset info:")
print(df.info())

print("\nsummary statistics:")
print(df.describe())


#topic 2 -univariate analysis
#analyze one variable at a time
#histogram - distribution of a numerical variable
plt.figure()
sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

#box plot - identify outliers and distribution of a numerical variable
plt.figure()
sns.boxplot(x=df["salary"])
plt.title("Salary Box Plot")
plt.show()

#categorical analysis - frequency counts
#when a column contains categories (labels) inteseas of numbers, we count how many times each category appears

print("\nDepartment value counts:")
print(df["department"].value_counts())

print("\nGender value counts:")
print(df["gender"].value_counts())

#bar plot for categorical variable
# a count plot is the type of bar plot used to show the frequence (count) of each category in a categorical variable

plt.figure()
sns.countplot(x="department", data=df)
plt.title("Department distribution")
plt.show()