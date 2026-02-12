import pandas as pd

# Load dataset
df = pd.read_csv("day10/customer_orders.csv")

# Create example location column (12 values to match 12 rows)
df["location"] = [
    " New York", "new york", "NEW YORK ",
    "Chicago", " chicago", "CHICAGO",
    "New York", "NEW YORK", "chicago",
    "Chicago", " new york ", "CHICAGO "
]

# Before cleaning
print("Before cleaning:")
print(df["location"].unique())

# Clean text (remove spaces + standardize case)
df["location"] = df["location"].str.strip().str.title()

# After cleaning
print("\nAfter cleaning:")
print(df["location"].unique())


