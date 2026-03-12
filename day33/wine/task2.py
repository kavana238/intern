import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("E:\\intership\\day33\\WineQT.csv")

# Save Id separately
ids = data["Id"]

# Features and target
X = data.drop(["quality", "Id"], axis=1)
y = data["quality"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict quality for all wines
predictions = model.predict(X)

# Convert predictions to integer
predictions = predictions.round().astype(int)

# Create output dataframe
output = pd.DataFrame({
    "Id": ids,
    "Predicted_Quality": predictions
})

# Show first results
print(output.head())

# Save to CSV
output.to_csv("wine_quality_predictions.csv", index=False)

print("Prediction file saved as wine_quality_predictions.csv")