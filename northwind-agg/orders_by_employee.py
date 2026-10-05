import pandas as pd, matplotlib.pyplot as plt

orders = pd.read_csv("orders.csv")
employees = pd.read_csv("employees.csv")

merged = pd.merge(orders, employees, on="EmployeeID")

merged["FullName"] = merged["FirstName"] + " " + merged["LastName"]

order_counts =(
  merged.groupby("FullName")["OrderID"].count()
  .sort_values(ascending=False)
)

top_5 = order_counts.head(5)
print(top_5)

top_5.plot(kind="bar", title="Orders Handled per Employee")
plt.show()