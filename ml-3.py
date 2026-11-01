
# Check if Python is installed
# python --version

#  If Python is installed, install required libraries
# python -m pip install pandas numpy matplotlib seaborn scikit-learn

#  Check if Python extension is installed in VS Code
# code --list-extensions

# Install Python extension in VS Code (if missing)
# code --install-extension ms-python.python

# Practical 3: K-Nearest Neighbors on Diabetes Dataset

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score
)

# Step 1: Load the dataset
df = pd.read_csv("diabetes.csv")

print("First five rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Step 2: Identify the target column
target_col = None

for col in ["Outcome", "outcome", "Diabetes", "diabetes", "target", "class"]:
    if col in df.columns:
        target_col = col
        break

if target_col is None:
    raise ValueError("Target column not found. Check your dataset.")

# Step 3: Separate features and target
X = df.drop(target_col, axis=1)
y = df[target_col]

# Convert features to numeric values
X = X.apply(pd.to_numeric, errors="coerce")

# Replace invalid zero values in common Pima diabetes measurements
zero_cols = [
    "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"
]

for col in zero_cols:
    if col in X.columns:
        X[col] = X[col].replace(0, float("nan"))

# Fill missing values using column medians
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# Step 4: Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Step 5: Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Implement K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict the test data
y_pred = knn.predict(X_test)

# Step 7: Calculate confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Step 8: Calculate performance metrics
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

print("\n========== KNN PERFORMANCE ==========")
print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)

print("\nDiabetes Classification Completed Successfully!")
