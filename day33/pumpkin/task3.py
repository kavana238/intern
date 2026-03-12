import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_excel("day33/pumpkin/Pumpkin_Seeds_Dataset.xlsx")

# Encode class
le = LabelEncoder()
data['Class'] = le.fit_transform(data['Class'])

# Features and target
X = data.drop('Class', axis=1)
y = data['Class']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict for all rows
predictions = model.predict(X)

# Convert back to class names
predictions = le.inverse_transform(predictions)

# Create output dataframe
output = pd.DataFrame({
    "Seed_ID": range(len(predictions)),
    "Predicted_Class": predictions
})

print(output.head())

# Save CSV
output.to_csv("pumpkin_prediction_output.csv", index=False)

print("Prediction file created successfully.")