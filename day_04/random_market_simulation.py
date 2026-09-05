import random
def simulate_daily_returns(days=10, seed=42):
  random.seed(seed)
  returns= [random.uniform(-0.03, 0.03) for _ in range(days)]
  return returns
daily_returns= simulate_daily_returns()
print(f"Daily Returns: {[round(r,4) for r in daily_returns]}")
cumulative= sum(daily_returns)
print(f"Cumulative Return: {round(cumulative, 4)}")