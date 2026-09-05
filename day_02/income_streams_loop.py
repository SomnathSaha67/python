income_streams = [("salary", 60000), ("freelance", 15000), ("dividends", 4000), ("rental", 0)]
total=0
for name, amount in income_streams:
  if amount==0:
    amount= "inactive"
  else:
    total+=amount
  print(f"{name}: {amount}")
print(f"Total income: {total}")