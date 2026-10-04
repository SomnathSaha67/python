import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "department": ["Engineering", "HR", "Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering"],
    "salary": [60000, 45000, 75000, 48000, 52000, 50000, 68000, 42000]
}

df = pd.DataFrame(data)

df["bonus"] = df["salary"] * 0.1

df.loc[len(df)] = ["Ian", "Marketing", 55000, 5500.0]

df_dropped_temp = df.drop(columns=["bonus"])
print(f"Columns in original df (without inplace=True): {df.columns.tolist()}")

df.drop(columns=["bonus"], inplace=True)
print(f"Columns in original df (with inplace=True): {df.columns.tolist()}")

df.drop(index=[0, 1], inplace=True)
print(f"\nShape after dropping 2 rows: {df.shape}")