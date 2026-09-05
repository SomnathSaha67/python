investments = [("stocks", 0.12), ("bonds", 0.05), ("crypto", 0.25), ("realestate", 0.09), ("startup", 0.30)]
high_roi= [name for name, rate in investments if rate>0.10]
rates_only=[rate for name, rate in investments]
print(f"High rate of interests in: {', '.join(name for name in high_roi)}")
print(f"Sum of rates: {round(sum(rates_only),2)}%")