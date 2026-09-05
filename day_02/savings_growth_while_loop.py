def grow_savings(principal=100000, rate=0.08, years=10):
  history=[]
  balance= principal
  year=0
  while year<years:
    balance*=(1+rate)
    history.append(balance)
    year+=1
  return history
history=grow_savings()
print(round(history[-1],2))