import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "department": ["Engineering", "HR", "Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering"],
    "salary": [60000, 45000, 75000, 48000, 52000, 50000, 68000, 42000]
}

df = pd.DataFrame(data)

print("--- Ascending Salary ---")
print(df.sort_values(by="salary", ascending=True))

print("\n--- Descending Salary ---")
print(df.sort_values(by="salary", ascending=False))

print("\n--- Multi-Column Sort (department asc, salary desc) ---")
sorted_df = df.sort_values(by=["department", "salary"], ascending=[True, False])
print(sorted_df)