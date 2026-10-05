import pandas as pd

employee_territory = pd.read_csv("employee_territory.csv")
employees = pd.read_csv("employees.csv")
orders = pd.read_csv("orders.csv")

print("employee_territory head:")
print(employee_territory.head())
print("employees head:")
print(employees.head())

emp_terr = pd.merge(employee_territory, employees, on="EmployeeID")
emp_terr["FullName"] = emp_terr["FirstName"] + " " + emp_terr["LastName"]

terr_count = emp_terr.groupby("FullName")['TerritoryID'].count().rename("TerritoryCount")

emp_orders = pd.merge(orders, employees, on="EmployeeID")
emp_orders["FullName"] = emp_orders["FirstName"] + " " + emp_orders["LastName"]
order_count = emp_orders.groupby("FullName")["OrderID"].count().rename("OrderCount")

comparision= pd.concat([terr_count, order_count], axis=1).fillna(0).astype(int)
comparision = comparision.sort_values(by="OrderCount", ascending=False)

print("\nSide-by-side comparision:")
print(comparision)

comparision.reset_index().to_csv("employee_territory_vs_orders.csv", index=False)