
# Check if Python is installed
# python --version

#  If Python is installed, install required libraries
# python -m pip install pandas numpy matplotlib seaborn scikit-learn

#  Check if Python extension is installed in VS Code
# code --list-extensions

# Install Python extension in VS Code (if missing)
# code --install-extension ms-python.python

# Practical 4: K-Means Clustering on Sales Dataset

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans

# Step 1: Load the dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")

print("First five rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Step 2: Select relevant numerical sales features
features = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]

X = df[features].copy()

# Step 3: Handle missing values
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# Step 4: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Calculate WCSS for different cluster numbers
wcss = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)    
    wcss.append(kmeans.inertia_)

# Step 6: Plot the Elbow Method graph
plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.xticks(range(1, 11))
plt.grid()
plt.show()

# Step 7: Enter optimal number of clusters from the graph
optimal_k = int(input("Enter the optimal number of clusters: "))

# Step 8: Apply K-Means clustering
kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

# Step 9: Add cluster labels to the dataset
df["Cluster"] = clusters

print("\nCluster Assignments:")
print(df[features + ["Cluster"]].head(10))

print("\nNumber of records in each cluster:")
print(df["Cluster"].value_counts().sort_index())

print("\nCluster Centers:")
print(scaler.inverse_transform(kmeans.cluster_centers_))

# Step 10: Visualize the clusters
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 2],
    c=clusters,
    cmap="viridis"
)

plt.title("K-Means Clustering of Sales Data")
plt.xlabel("Quantity Ordered (Scaled)")
plt.ylabel("Sales (Scaled)")
plt.show()

print("\nK-Means Clustering Completed Successfully!")
