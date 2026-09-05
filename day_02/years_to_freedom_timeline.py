def years_to_freedom(monthly_passive=100, monthly_expenses=40000, growth_rate=0.15, max_years=30):
  timeline=[]
  for year in range(1, max_years+1):
    monthly_passive+=monthly_passive*growth_rate
    timeline.append(monthly_passive)
    if monthly_passive>=monthly_expenses: return year, timeline
  return None, timeline
year, timeline= years_to_freedom()
print("Result:", year)
print(f"Timeline: {len(timeline)}")
print(f"Final value: {round(timeline[-1], 2)}")