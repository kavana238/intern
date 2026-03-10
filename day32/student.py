import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("E:\intership\day32\StudentsPerformance.csv")

# Create average score
df["avg"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

# Create Pass/Fail column
df["result"] = df["avg"].apply(lambda x: 1 if x >= 40 else 0)

# Encode categorical data
le = LabelEncoder()
df["gender"] = le.fit_transform(df["gender"])
df["race/ethnicity"] = le.fit_transform(df["race/ethnicity"])
df["parental level of education"] = le.fit_transform(df["parental level of education"])
df["lunch"] = le.fit_transform(df["lunch"])
df["test preparation course"] = le.fit_transform(df["test preparation course"])

# Features and target
X = df.drop(["avg","result"], axis=1)
y = df["result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("Prediction:", prediction)