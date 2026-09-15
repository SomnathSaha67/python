inventory = [("Widget", 42, 9.99), 
             ("Gadget", 0, 19.99), 
             ("Gizmo", 7, 4.5), 
             ("Sprocket", -3, 12.0)]

total_value=0
highest_item= None
highest_value= 0

print("Audit Summary:")

for name, qty, price in inventory:

  if (qty<0): status= "Data-integrity error"; value= 0
  elif (qty==0): status= "Out of stock"; value=0
  else:
    status= "Valid"
    value= qty*price
    total_value+=value
  if (value>highest_value):
    highest_value= value
    highest_item= name

  print(f"{name}: qty: {qty}, price: ${price}, status: {status}, value: ${value}")

print(f"Total inventory value (valid only): ${total_value}")
print(f"Highest-value item: {highest_item} with value ${highest_value}")