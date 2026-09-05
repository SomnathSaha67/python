def is_financially_free(passive_income, expenses):
  return passive_income>=expenses
def freedom_status(passive_income, expenses):
  return "Free to travel" if is_financially_free(passive_income, expenses) else "Still building"
print(f"Financial status: {freedom_status(5000, 6500)}")
