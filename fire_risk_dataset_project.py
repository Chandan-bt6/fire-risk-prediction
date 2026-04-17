"""csv file reading """
import pandas as pd
data = pd.read_csv("fire_risk_dataset.csv")
print(data,"\n")
print(data.info())
print(data.describe())

"""split into X and Y"""

import pandas as pd

# Load CSV
df = pd.read_csv("fire_risk_dataset.csv")

# Create Features (X) → Input columns
X = df[["temp", "humidity", "wind", "rainfall", "ndvi"]]

# Create Labels (y) → Output column
y = df["risk"]

# Show structure
print("Features (X):")
print(X.head())

print("\nLabels (y):")
print(y.head())


"""04"""

from sklearn.model_selection import train_test_split
import pandas as pd

# Load CSV
df = pd.read_csv("fire_risk_dataset.csv")

# Features
X = df[["temp", "humidity", "wind", "rainfall", "ndvi"]]

# Labels
y = df["risk"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% test, 80% train
    random_state=42     # same split every time
)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


"""05"""
# ===== STEP–5: Train Model =====
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Model initialize
model = RandomForestClassifier(
    n_estimators=100,     # number of trees
    random_state=42
)

# Model train karo
model.fit(X_train, y_train)

print("\n Model Training Complete")

# ===== STEP–6: Prediction & Accuracy =====
y_pred = model.predict(X_test)

# Accuracy check
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""06"""
# Our model is saved in fire_risk_dataset.pkl
import joblib

# Save model
joblib.dump(model, "fire_risk_model.pkl")

print("\n Model Saved — fire_risk_model.pkl created!")

# checking that our model safely saved or not
# Load model
loaded_model = joblib.load("fire_risk_model.pkl")

# Test prediction
sample = X_test.iloc[0:1]   # first test row
print("\nSample test input:\n", sample)

pred = loaded_model.predict(sample)
print("\nPredicted Risk:", pred[0])
