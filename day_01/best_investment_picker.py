def annual_return(principal, rate):
  return principal*rate
stock, real_estate, business=(10000, 0.08), (25000, 0.05), (15000, 0.12)
def get_return(investment):
  principal, rate= investment
  return annual_return(principal, rate)
winner= max([stock, real_estate, business], key= get_return)
print("Best investment:", winner)
print("Return:", round(get_return(winner), 2))