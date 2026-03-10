import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv(r"E:\intership\day32\Titanic-Dataset.csv")

X = data[['Pclass','Age','Fare']].fillna(0)
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions[:5])