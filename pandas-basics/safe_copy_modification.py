import pandas as pd

df = pd.read_csv("sample.csv")

df_ref = df
df_ref.at[0, "Name"] = "Alice_Modified"

print("--- Direct Assignment (Reference) ---")
print(f"df_ref row 0 Name: {df_ref.at[0, "Name"]}")
print(f"df row 0 Name: {df.at[0, "Name"]}")

df_safe = df.copy()
df_safe.at[0, "Name"] = "Alice_Safe"

print("\n--- Explicit .copy() ---")
print(f"df_save row 0 Name: {df_safe.at[0, "Name"]}")
print(f"df row 0 Name: {df.at[0, "Name"]}")