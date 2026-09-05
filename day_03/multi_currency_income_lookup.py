def convert_to_inr(amount, currency, rates):
  if currency not in rates: return amount*1
  else: return amount*rates.get(currency)
exchange_rates = {"USD": 83.0, "EUR": 90.0, "GBP": 105.0} 
foreign_income = {"USD": 500, "EUR": 300, "GBP": 0, 'NEP': 100}
total=0
for currency, amount in foreign_income.items():
  converted_amount= convert_to_inr(amount, currency, exchange_rates)
  print(f"{currency}: {amount}\nINR: {converted_amount}\n")