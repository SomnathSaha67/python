import pandas as pd

orders = pd.read_csv("orders.csv")
order_details = pd.read_csv("order_details.csv")
products = pd.read_csv("products.csv")

details_orders = pd.merge(order_details, orders, on="OrderID")

df = pd.merge(details_orders, products, on="ProductID")

# UnitPrice_x = proce at time of order (order_details)
# UnitPrice_y = current catalog list price (products)

df["LineRevenue"] = df["UnitPrice_x"] * df["Quantity"]

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Year"] = pd.DatetimeIndex(df["OrderDate"]).year

revenue_by_year = df.groupby("Year")["LineRevenue"].sum()
print(revenue_by_year)