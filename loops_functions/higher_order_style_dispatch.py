def apply_discount(price, pct):

  return price*(1-pct/100)

def apply_tax(price, pct):
  
  return price*(1+pct/100)

def apply_flat_fee(price, fee):
  
  return price+fee

operations= {"discount": apply_discount,
             "tax": apply_tax,
             "flat": apply_flat_fee}

transactions= [("discount", 100, 10),
              ("tax", 200, 18),
              ("flat", 50, 5),
              ("unknown", 30, 0)]

running_total= 0
log=[]

for op, price, value in transactions:

  if op in operations:
    result= operations[op](price, value)
    running_total+=result
    log.append(f"{op} applied on ${price} with {value} -> ${result:.2f}")
  else:
    log.append(f"Skipped unknown operation '{op}' on ${price}")

print(f"Running Total: ${running_total}")
print("\nLog:")

for entry in log:
  print(entry)