import pandas as pd
from IPython.display import display

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "department": ["Engineering", "HR", "Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering"],
    "salary": [60000, 45000, 75000, 48000, 52000, 50000, 68000, 42000]
}

df = pd.DataFrame(data)

mask = df.salary > 50000
print("--- Boolean Mask ---")
print(mask)
print("\n--- Filtered with Single Condition ---")
print(df[mask])

combined_mask = (df.salary > 50000) & (df.department == "Engineering")

print("\n--- Filtered Result (Engineering & Salary > 50k) ---")
with pd.option_context("display.max_rows", 50):
  display(df[combined_mask])