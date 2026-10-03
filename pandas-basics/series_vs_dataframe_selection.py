import pandas as pd

df = pd.read_csv("sample.csv")

print("Using df['Name']:")
print(df["Name"])
print(type(df["Name"]))

print("\nUsing df[['Name']]:")
print(df[["Name"]])
print(type(df[["Name"]]))

print("\nUsing df[['Name', 'Score']]:")
print(df[["Name", "Score"]])

print("\nUsing df.Name:")
print(df.Name)

print(f"\nSame result? {df.Name.equals(df["Name"])}")