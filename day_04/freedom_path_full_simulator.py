import random, statistics
def simulate_freedom_path(monthly_expenses=40000, start_passive=000, mean_growth=0.05, growth_std=0.02, years=30, seed=1):
  random.seed(seed)
  history, freedom_year=[], None
  passive_income= start_passive
  for year in range(1, years+1):
    growth = 1 + random.gauss(mean_growth, growth_std)   
    passive_income *= growth                             
    history.append(passive_income)
    if passive_income>=monthly_expenses: freedom_year= year; break
  avg = statistics.mean(history)
  results = {
        "freedom_year": freedom_year,
        "final_passive": round(passive_income, 2),
        "avg_passive": round(avg, 2),
        "history": history
    }
  for k, v in results.items():
    print(f"{k:<12}: {v}")
simulate_freedom_path(40000, 20000, 0.15, 0.05, 30)