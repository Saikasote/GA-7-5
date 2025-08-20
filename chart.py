import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Synthetic data generation ---
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"]

# Each category → 50 samples
scores = [
    np.random.normal(loc=80, scale=5, size=50),
    np.random.normal(loc=75, scale=6, size=50),
    np.random.normal(loc=82, scale=4, size=50),
    np.random.normal(loc=78, scale=5, size=50),
    np.random.normal(loc=85, scale=3, size=50)
]

# Create DataFrame
data = pd.DataFrame({
    "Category": np.repeat(categories, 50),
    "Satisfaction": np.concatenate(scores)
})

# --- Styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Plot ---
plt.figure(figsize=(8, 8))   # 8 inches * 64 dpi = 512 px
ax = sns.barplot(x="Category", y="Satisfaction", data=data, palette="viridis", ci="sd")

# Titles and labels
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, pad=15)
ax.set_xlabel("Product Category", fontsize=12)
ax.set_ylabel("Satisfaction Score", fontsize=12)
plt.xticks(rotation=20)

# --- Save exactly 512x512 ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
