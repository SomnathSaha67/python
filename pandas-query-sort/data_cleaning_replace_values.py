import numpy as np, pandas as pd

data = {
    "employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "status": ["Y", "no", "yes", "N", "Y", "NO"],
    "performance": ["Excellent", "N/A", "Good", "N/A", "Average", "Good"]
}

df = pd.DataFrame(data)

print("--- Before Cleaning ---")
print(df)

status_mapping = {
  "Y": "Active",
  "yes": "Active",
  "N": "Inactive",
  "no": "Inactive",
  "NO": "Inactive"
}

df["status"] = df["status"].replace(status_mapping)

df["performance"] = df["performance"].replace("N/A", np.nan)

print("\n--- After Cleaning ---")
print(df)