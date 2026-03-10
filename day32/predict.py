import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


data = pd.read_csv(r"E:\intership\day32\kc_house_data.csv")

X = data[['bedrooms','bathrooms','sqft_living']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#model = DecisionTreeRegressor(max_depth=3)
model = DecisionTreeRegressor(max_depth=3, min_samples_split=5, min_samples_leaf=2)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions[:5])


plt.figure(figsize=(15,8))
plot_tree(model, filled=True)  
plt.show()