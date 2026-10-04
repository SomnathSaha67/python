import pandas as pd

data = {
    "date": [
        "2026-01-15", "2026-01-17", "2026-02-01", "2026-02-14",
        "2026-03-05", "2026-03-22", "2026-04-10", "2026-04-11"
    ],
    "event": ["Meeting", "Workshop", "Conference", "Retreat", "Review", "Hackathon", "Demo", "Launch"]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])
print(f"New dtype: {df["date"].dtype}")

dt_idx = pd.DatetimeIndex(df["date"])
df["year"] = dt_idx.year
df["month"] = dt_idx.month
df["weekday"] = dt_idx.weekday

weekend_mask = df["weekday"].isin([5, 6])
weekend_df = df[weekend_mask]

final_df = weekend_df.sort_values(by="date", ascending=True)

print("\n--- Weekend Events (Sorted Ascending) ---")
print(final_df)