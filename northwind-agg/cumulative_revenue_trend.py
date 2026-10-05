import pandas as pd, matplotlib.pyplot as plt

orders = pd.read_csv("orders.csv")
order_details = pd.read_csv("order_details.csv")

merged = pd.merge(order_details, orders, on="OrderID")

merged["LineRevenue"] = merged["UnitPrice"] * merged["Quantity"]
merged["OrderDate"] = pd.to_datetime(merged["OrderDate"])
merged = merged.sort_values("OrderDate")

daily_revenue = merged.groupby("OrderDate")["LineRevenue"].sum()
cumulative_revenue = daily_revenue.cumsum()

total_line_revenue = merged["LineRevenue"].sum()
final_cumulative_val = cumulative_revenue.iloc[-1]

print(f"Plain .sum() of LineRevenue : {total_line_revenue:.2f}")
print(f"Final cumulative total: {final_cumulative_val:.2f}")
print(f"Do they match? {round(total_line_revenue, 2) == round(final_cumulative_val, 2)}")

cumulative_revenue.plot(kind="line", title="Cumulative Revenue Over Time")
plt.show()