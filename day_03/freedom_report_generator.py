def freedom_report(name="Somnath", passive_income=5000, expenses=40000, portfolio=None):
  if portfolio is None:
        portfolio = {"Stocks": 0.12, "Bonds": 0.05, "RealEstate": 0.15}
  growth_potential= {k: v for k, v in portfolio.items() if v>0.10}
  return (name, "Free to travel", growth_potential) if passive_income>=expenses else (name, "Still building", growth_potential)
name, status, growth_potential= freedom_report()
print(f"{'Name':<15}: {name}\n{'Status':<15}: {status}\nGrowth Potential:")
for k, v in growth_potential.items():
  print(f"{k:<15}: {v:.2f}")