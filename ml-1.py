
# Check if Python is installed
# python --version

#  If Python is installed, install required libraries
# python -m pip install pandas numpy matplotlib seaborn scikit-learn

#  Check if Python extension is installed in VS Code
# code --list-extensions

# Install Python extension in VS Code (if missing)
# code --install-extension ms-python.python


# PRACTICAL 1: UBER FARE PREDICTION
# Linear Regression and Random Forest Regression

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. LOAD DATASET

df = pd.read_csv("uber.csv")

print("First Five Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

os.makedirs("outputs", exist_ok=True)

# 2. DATA PREPROCESSING

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df = df[df["fare_amount"] > 0]
df = df[df["passenger_count"].between(1, 6)]

df = df[
    df["pickup_latitude"].between(-90, 90) &
    df["dropoff_latitude"].between(-90, 90) &
    df["pickup_longitude"].between(-180, 180) &
    df["dropoff_longitude"].between(-180, 180)
]

print("\nShape after preprocessing:", df.shape)

# 3. IDENTIFY AND REMOVE OUTLIERS USING IQR

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["fare_amount"] < lower_limit) |
    (df["fare_amount"] > upper_limit)
]

print("\nNumber of outliers:", len(outliers))

df = df[
    (df["fare_amount"] >= lower_limit) &
    (df["fare_amount"] <= upper_limit)
]

# 4. CALCULATE DISTANCE

def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371

    lat1, lon1, lat2, lon2 = map(
        np.radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2 +
        np.cos(lat1) * np.cos(lat2) *
        np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


df["distance"] = calculate_distance(
    df["pickup_latitude"],
    df["pickup_longitude"],
    df["dropoff_latitude"],
    df["dropoff_longitude"]
)

df = df[df["distance"] > 0]

print("\nShape after distance calculation:", df.shape)

# 5. CORRELATION ANALYSIS

correlation = df[
    [
        "fare_amount",
        "passenger_count",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "distance"
    ]
].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

# Save heatmap without opening a window
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("\nCorrelation analysis completed.")

# 6. SELECT FEATURES AND TARGET

X = df[
    [
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "passenger_count",
        "distance"
    ]
]

y = df["fare_amount"]

# Split dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# 7. LINEAR REGRESSION

print("\nTraining Linear Regression...")

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

# 8. RANDOM FOREST REGRESSION

print("\nTraining Random Forest Regression...")

rf_model = RandomForestRegressor(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

# 9. MODEL EVALUATION

def evaluate_model(name, actual, predicted):

    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predicted)

    print("\n", name)
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R2 Score:", r2)

    return [name, mae, mse, rmse, r2]


lr_results = evaluate_model(
    "Linear Regression", y_test, lr_predictions
)

rf_results = evaluate_model(
    "Random Forest Regression", y_test, rf_predictions
)

# 10. MODEL COMPARISON

results = pd.DataFrame(
    [lr_results, rf_results],
    columns=["Model", "MAE", "MSE", "RMSE", "R2 Score"]
)

print("\nMODEL COMPARISON:")
print(results.to_string(index=False))

results.to_csv("outputs/model_comparison.csv", index=False)

print("\nPractical Completed Successfully!")
