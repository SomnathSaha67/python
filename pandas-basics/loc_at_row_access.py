import pandas as pd

df = pd.read_csv("sample.csv")

row_by_label = df.loc[2]
cell_loc = df.loc[1, "Name"]
row_slice = df.loc[1:3]

print("--- .loc[] Examples ---")
print(f"One full row (.loc[2]):\n{row_by_label}")
print(f"\nSpecific cell (.loc[1, 'Name']): {cell_loc}")
print(f"\nRange of rows (.loc[1:3]):\n{row_slice}")

cell_at = df.at[1, "Name"]
print("\n--- .at[] vs .loc[] ---")
print(f"Using .at[1, 'Name']: {cell_at}")
print(f"Do .at[] and .loc[] values match? {cell_at == cell_loc}")

print("\n--- First 3 rows (.head(3)) ---")
print(df.head(3))

print("\n--- Last 3 rows (.tail(3)) ---")
print(df.tail(3))

print("\n--- Random 3 rows (.sample(3)) ---")
print(df.sample(3))