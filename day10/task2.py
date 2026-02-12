import pandas as pd

# Load dataset
df = pd.read_csv("day10/customer_orders.csv")

print("Before conversion:\n")
print(df.dtypes)

# Convert order_amount to float (if needed)
df["order_amount"] = df["order_amount"].astype(float)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

print("\nAfter conversion:\n")
print(df.dtypes)



