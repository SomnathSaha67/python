def freedom_number(monthly_expenses, safety_years=5):
  return monthly_expenses*12*safety_years
print(freedom_number(30000))
print(freedom_number(50000, 10))