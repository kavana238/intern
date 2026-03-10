#Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv(r"E:\intership\day32\Titanic-Dataset.csv")

#Select input features (X) and target variable (y)
X = data[['Pclass','Age','Fare']].fillna(0)
y = data['Survived']

#Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y)

#Create the model Train the model
model = DecisionTreeClassifier(criterion="gini", max_depth=3)
model.fit(X_train, y_train)

#Make predictions Print predictions
predictions = model.predict(X_test)
print(predictions[:5])