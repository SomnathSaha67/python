catalog = {"P101": ("Laptop", 999.99, 15), 
           "P102": ("Mouse", 24.99, 200), 
           "P103": ("Monitor", 189.5, 0)}

total_value= 0

for pid, (name, price, qty) in catalog.items():

  if (qty==0): 
    print(f"{pid} - {name}: Out of stock")
  else: 
    value= price*qty
    total_value+=value
    print(f"{pid} - {name}: In stock, qty= {qty}, value= ${value}")

if ("P999" in catalog):
  name, price, catalog= catalog["P999"]
  print(f"P999 found: {name}, qty= {qty}, price= ${price}")
else:
  print("P999 not found")

print(f"Total catalog value (in-stock only): ${total_value}")