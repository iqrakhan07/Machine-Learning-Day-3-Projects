# Diabetes Prediction Using Logistic Regression

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("diabetes.csv")

# Features and Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Test prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)
print(f"Model Accuracy: {accuracy:.2%}")

# Predict a New Patient

patient = pd.DataFrame(
    [[2, 120, 70, 20, 80, 25.5, 0.4, 35]],
    columns=X.columns
)

result = model.predict(patient)

print("\nPatient Details")
print(patient)

if result[0] == 1:
    print("\nPrediction: Diabetic")
else:
    print("\nPrediction: Not Diabetic")
