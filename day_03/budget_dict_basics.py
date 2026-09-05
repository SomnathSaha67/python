budget = {"rent": 20000, "food": 8000, "travel": 5000, "investments": 15000}
budget["emergency_fund"]= 6000
total= sum(budget.values())
print(f"Total budget: {total}")
for key, value in budget.items():
  print(f"{key}: {value/total:.1%}")