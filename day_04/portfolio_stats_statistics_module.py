import statistics as stats
monthly_returns = [0.02, -0.01, 0.03, 0.015, -0.005, 0.04, 0.01, -0.02, 0.025, 0.005]
print(f"Average: {stats.mean(monthly_returns)}\nMedian: {stats.median(monthly_returns)}\nVolatility: {stats.stdev(monthly_returns):.4f}")
if stats.stdev(monthly_returns)>0.02: print("High volatility")
else: print("Stable")