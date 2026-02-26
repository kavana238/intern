import pandas as pd

data = pd.Series([10, None, 30, None])
print(data)

print(data.isnull())

#return a boolean mask
#often used to filter data cleaning

print(data[data.isnull()])
#filter only the missing values

print(data.notnull())
#filter only valid values

print(data.fillna(0))
#replace missing values - fillna() method

#replaece missing values with the mean of the series
print(data.fillna(data.mean()))

#used in normalization and  preprocessing
#avoid data loss


#remove missing values - dropna()
print(data.dropna())

#isnull() - detect missing values
#notnull() - detect non-missing values
#fillna() - replace missing values with a specified value or method
#dropna() - remove missing values from a Series or DataFrame
