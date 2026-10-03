import pandas as pd

with open("sample.csv", "w") as f:
  f.write("ID,Name,Score,Remarks\n")
  f.write("1,Alice,85,Good\n")
  f.write("2,Bob,90,Excellent\n")
  f.write("3,Charlie,,Average\n")
  f.write("4,David,70,\n")
  f.write("5,Eva,95,Outstanding\n")
  f.write("6,Frank,60,Fair\n")

df = pd.read_csv("sample.csv")

print(type(df))
print(df.shape)
print(df.columns)

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())