import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("E:\intership\day32\car data.csv")

# Show dataset
print(df.head())

# Convert categorical columns to numeric
df = pd.get_dummies(df, drop_first=True)

# Features and Target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predicted Prices:", predictions)