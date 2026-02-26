import pandas as pd

data = {
    "customer_id": [101, 102, 102, 103],
    "customer_name": ["Alice", "Bob", "Bob", "Charlie"],
    "purchase": [250, 150, 150, 300]
}

df = pd.DataFrame(data)
print(df)

# Identify full row duplicates
print(df.duplicated())

#show only duplicated rows
print(df[df.duplicated()])

#remove full-row duplicates
df_clean = df.drop_duplicates()
print(df_clean)

#column-level duplicate detection
print(df.duplicated(subset=['customer_id']))

#keeps the first occurrence of each duplicate
print(df.drop_duplicates(subset=['customer_id'], keep='last'))

#remove all dupliates completely
print(df.drop_duplicates(subset=['customer_id'], keep=False))