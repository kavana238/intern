import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


# 1️ Create Non-Linear Data

np.random.seed(42)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3*(X**2) + 2*X + 5 + np.random.randn(100,1)*5   # Quadratic relationship

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 2️ Linear Regression (Normal)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

r2_linear = r2_score(y_test, y_pred_linear)


# 3️ Polynomial Features (degree=2)

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)

y_pred_poly = poly_model.predict(X_poly_test)

r2_poly = r2_score(y_test, y_pred_poly)


# 4️ Results

print("R2 Score (Linear Regression):", r2_linear)
print("R2 Score (Polynomial Regression):", r2_poly)


# 5 Visualization

plt.scatter(X, y, label="Data")
plt.plot(X_test, y_pred_linear, color="red", label="Linear Fit")
plt.plot(X_test, y_pred_poly, color="green", label="Polynomial Fit")
plt.legend()
plt.show()
