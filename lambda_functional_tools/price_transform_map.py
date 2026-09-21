prices = [499, 999, 1499, 2999, 4999]

# apply 10% discount
discounted= list(map(lambda p: p*0.90, prices))

# round each discounted price to nearest integer
discounted_rounded= list(map(lambda p: round(p), discounted))

# parallel tax rates for each item
tax_rates= [50, 100, 150, 300, 500]

final_prices= list(map(lambda d, t: d+t, discounted_rounded, tax_rates))

print("Original  |  Discounted  |  Final (with tax)")
for orig, disc, final in zip(prices, discounted_rounded, final_prices):
  print(f"{orig:8}  |  {disc:10}  |  {final:15}")