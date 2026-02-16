# step1: always check the data type of the variable
import pandas as pd
data = {
    "name" : ["Alice", "Bob", "Charlie"],
    "marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df.dtypes)

#problem 1: number stored as strings
#use astype()
df["marks"] = df["marks"].astype(int)
print(df.dtypes)
print(df["marks"].mean())

#problem 2: date stored as object
data = {
    "joining_date": ["2021-01-10", "2021-12-05"]
}
df = pd.DataFrame(data)
print(df.dtypes)

#solution: use pd.to_datetime()
df["joining_date"] = pd.to_datetime(df["joining_date"])
print(df.dtypes)
print(df["joining_date"].dt.year)

#problem 3: mixed data types 
data = {
    "salary": ["50000", "60000", "not available"]
}
df = pd.DataFrame(data)
print(df.dtypes)

#solution: use pd.to_numeric()
df["salary"] = pd.to_numeric(df["salary"], errors='coerce')
print(df)