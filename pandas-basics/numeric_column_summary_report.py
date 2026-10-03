import pandas as pd

df = pd.read_csv("sample.csv")

first_valid_idx = df["Score"].first_valid_index()
print(f"First valid index of 'Score': {first_valid_idx}")

score_sum = df["Score"].sum()
print(f"Sum of 'Score': {score_sum}")

print("\n--- Summary Statistics (df['Score'].describe()) ---")
print(df["Score"].describe())

score_mean = df["Score"].mean()
above_mean_df = df.loc[df["Score"] > score_mean]

print(f"\n--- Rows where Score > Mean ({score_mean}) ---")
print(above_mean_df)