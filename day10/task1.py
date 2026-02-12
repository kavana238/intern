import pandas as pd

# Load dataset
df = pd.read_csv("E:\intership\day10\customer_orders.csv")


# Shape before cleaning
print("Shape before cleaning:", df.shape)

# 1. Report missing values
print("\nMissing values in each column:")
print(df.isna().sum())

# 2. Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# 3. Remove duplicate rows (across all columns)
df = df.drop_duplicates()

# Shape after cleaning
print("\nShape after cleaning:", df.shape)
