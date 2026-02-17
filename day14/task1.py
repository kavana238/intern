import pandas as pd

# Sample dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print("Original Data:\n")
print(df)

# Step 1: Label Encoding


# Convert Transmission into numbers
df["Transmission"] = df["Transmission"].map({
    "Manual": 0,
    "Automatic": 1
})

# Step 2: One-Hot Encoding

# Convert Color using One-Hot Encoding
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter Encoding:\n")
print(df)
