def risk_level(age, income_stability):
  if age<30 and income_stability: return "Aggressive"
  elif age<50 and income_stability: return "Moderate"
  else: return "Conservative"
print(f"Risk level: {risk_level(30, True)}")