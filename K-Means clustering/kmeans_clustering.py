import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# 1. Load dataset
df = pd.read_csv("data/Mall_Customers.csv")
df.drop(columns=["CustomerID"], inplace=True)

# Encode Gender
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# 2. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 3. Elbow Method
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.grid()
plt.tight_layout()
plt.savefig("screenshoots/elbow_curve.png")
plt.show()

# 4. Fit K-Means with optimal K
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# 5. Silhouette Score
score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score for K={optimal_k}: {score:.3f}")

# 6. Visualize clusters using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(6, 4))
for i in range(optimal_k):
    plt.scatter(X_pca[labels == i, 0], X_pca[labels == i, 1], label=f"Cluster {i}")
plt.title("K-Means Clusters (PCA View)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("screenshoots/cluster_plot.png")
plt.show()