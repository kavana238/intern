import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load datasets
train = pd.read_csv("E:/intership/day33/train_u6lujuX_CVtuZ9i.csv")
test = pd.read_csv("E:/intership/day33/test_Y3wMUE5_7gLdaTN.csv")

# Save Loan_ID
test_id = test['Loan_ID']

# Drop Loan_ID
train = train.drop('Loan_ID', axis=1)
test = test.drop('Loan_ID', axis=1)

# Fill missing values
for col in ['Gender','Married','Dependents','Self_Employed']:
    train[col] = train[col].fillna(train[col].mode()[0])
    test[col] = test[col].fillna(test[col].mode()[0])

train['LoanAmount'] = train['LoanAmount'].fillna(train['LoanAmount'].mean())
test['LoanAmount'] = test['LoanAmount'].fillna(test['LoanAmount'].mean())

train['Loan_Amount_Term'] = train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].mode()[0])
test['Loan_Amount_Term'] = test['Loan_Amount_Term'].fillna(test['Loan_Amount_Term'].mode()[0])

train['Credit_History'] = train['Credit_History'].fillna(train['Credit_History'].mode()[0])
test['Credit_History'] = test['Credit_History'].fillna(test['Credit_History'].mode()[0])

# Encode categorical variables
cols = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']

for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# Convert target variable
train['Loan_Status'] = train['Loan_Status'].map({'Y':1,'N':0})

# Features and target
X = train.drop('Loan_Status', axis=1)
y = train['Loan_Status']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict on test dataset
test_predictions = model.predict(test)

# Convert prediction to Y/N
test_predictions = ['Y' if i==1 else 'N' for i in test_predictions]

# Create submission file
output = pd.DataFrame({
    'Loan_ID': test_id,
    'Loan_Status': test_predictions
})

output.to_csv("loan_prediction_output.csv", index=False)

print("Prediction file created successfully.")