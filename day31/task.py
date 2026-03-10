import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Diameter': [8, 8, 12, 12, 16],
    'Toppings': [1, 3, 1, 4, 2],
    'Price': [10, 13, 18, 22.5, 28]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Diameter', 'Toppings']]
y = df['Price']

# Model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new pizza
# Example: Diameter = 10 inches, Toppings = 2
prediction = model.predict([[10, 2]])

print("Predicted Pizza Price:", prediction[0])