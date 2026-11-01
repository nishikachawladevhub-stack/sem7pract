
# Check if Python is installed
# python --version

#  If Python is installed, install required libraries
# python -m pip install pandas numpy matplotlib seaborn scikit-learn

#  Check if Python extension is installed in VS Code
# code --list-extensions

# Install Python extension in VS Code (if missing)
# code --install-extension ms-python.python

# Practical 2: Email Spam Detection using KNN and SVM

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
df = pd.read_csv("emails.csv", encoding="latin-1")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("First five rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Step 2: Identify dataset type and prepare features
if "Prediction" in df.columns:
    # Numerical email dataset
    print("\nUsing numerical email features.")

    # Remove email ID column because it is not a useful feature
    df.drop(columns=["Email No"], errors="ignore", inplace=True)

    # Separate input features and target
    X = df.drop("Prediction", axis=1)
    y = df["Prediction"]

    # Convert features to numeric values
    X = X.apply(pd.to_numeric, errors="coerce")
    X = X.fillna(0)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features for better classification
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

else:
    # Raw-text email dataset
    print("\nUsing raw-text email data.")

    # Find the text and label columns
    possible_pairs = [
        ("v2", "v1"),
        ("Message", "Category"),
        ("text", "label")
    ]

    text_col, label_col = None, None

    for text_name, label_name in possible_pairs:
        if text_name in df.columns and label_name in df.columns:
            text_col, label_col = text_name, label_name
            break

    if text_col is None:
        raise ValueError("Could not identify email text and label columns.")

    # Remove missing values
    df = df.dropna(subset=[text_col, label_col])

    # Convert labels into binary values: 0 = Not Spam, 1 = Spam
    y = df[label_col].astype(str).str.lower().map({
        "ham": 0,
        "not spam": 0,
        "normal": 0,
        "0": 0,
        "spam": 1,
        "abnormal": 1,
        "1": 1
    })

    # Keep only rows with recognized labels
    valid_rows = y.notna()
    email_text = df.loc[valid_rows, text_col].astype(str)
    y = y.loc[valid_rows].astype(int)

    # Split before fitting TF-IDF to avoid data leakage
    text_train, text_test, y_train, y_test = train_test_split(
        email_text, y, test_size=0.2, random_state=42, stratify=y
    )

    # Convert email text into numerical features
    vectorizer = TfidfVectorizer(stop_words="english")
    X_train = vectorizer.fit_transform(text_train)
    X_test = vectorizer.transform(text_test)

# Step 3: Implement K-Nearest Neighbors
print("\nTraining KNN Classifier...")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

# Step 4: Implement Support Vector Machine
print("\nTraining SVM Classifier...")

svm = SVC(kernel="linear")
svm.fit(X_train, y_train)

svm_pred = svm.predict(X_test)

# Step 5: Evaluate KNN
print("\n========== KNN RESULTS ==========")

print("Accuracy:", accuracy_score(y_test, knn_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))
print("Classification Report:")
print(classification_report(y_test, knn_pred, zero_division=0))

# Step 6: Evaluate SVM
print("\n========== SVM RESULTS ==========")

print("Accuracy:", accuracy_score(y_test, svm_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, svm_pred))
print("Classification Report:")
print(classification_report(y_test, svm_pred, zero_division=0))

# Step 7: Compare model performance
comparison = pd.DataFrame({
    "Algorithm": ["KNN", "SVM"],
    "Accuracy": [
        accuracy_score(y_test, knn_pred),
        accuracy_score(y_test, svm_pred)
    ]
})

print("\n========== MODEL COMPARISON ==========")
print(comparison)

# Step 8: Identify the better model
if comparison.loc[0, "Accuracy"] > comparison.loc[1, "Accuracy"]:
    print("\nKNN performs better.")
elif comparison.loc[0, "Accuracy"] < comparison.loc[1, "Accuracy"]:
    print("\nSVM performs better.")
else:
    print("\nBoth models have equal accuracy.")

print("\nEmail Spam Detection Completed Successfully!")
