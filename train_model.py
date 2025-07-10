import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example data (replace with real medical dataset)
data = pd.DataFrame({
    "age": [65, 50, 70, 45],
    "bmi": [28.5, 30.2, 25.0, 27.8],
    "blood_pressure": [130, 120, 140, 125],
    "risk": [1, 0, 1, 0]
})

X = data[["age", "bmi", "blood_pressure"]]
y = data["risk"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.joblib")
print("Model saved as model.joblib")
