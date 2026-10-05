import pandas as pd

products = pd.read_csv("products.csv")
categories = pd.read_csv("categories.csv")

print(f"Product columns: {products.columns}")
print(f"Categories columns: {categories.columns}")

merged = pd.merge(products, categories, on="CategoryID")

summary = merged.groupby("CategoryName")["UnitPrice"].agg(["mean", "max", "min"]).reset_index()

summary.columns = ["CategoryName", "AveragePrice", "MaxPrice", "MinPrice"]

summary = summary.sort_values(by="AveragePrice", ascending=False)

summary.to_csv("category_price_summary.csv", index=False)

print(summary)