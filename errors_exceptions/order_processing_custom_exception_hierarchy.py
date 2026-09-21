class OrderError(Exception):
  pass

class OutOfStockError(OrderError):
  pass

class InvalidQuantityError(OrderError):
  pass

stock= {
  "Widget": 10,
  "Gadget": 0
}

orders= [
  ("Widget", 5),
  ("Gadget", 2),
  ("Widget", -3),
  ("Sprocket", 1)
]

successes= []
failures= []

for item, qty in orders:
  try:
    if qty<=0:
      raise InvalidQuantityError(f"Invalid quantity {qty} for {item}")
    
    if item not in stock or qty>stock[item]:
      raise OutOfStockError(f"Cannot fulfill order for {item} (requested {qty})")
    
    stock[item]-=qty
    successes.append((item, qty))
    print(f"Order succeeded: {item} x {qty}")

  except OrderError as e:
    print(f"Order failed ({e.__class__.__name__}): {e}")
    failures.append((item, qty, str(e)))

print("\n--- Final Report ---")
print("Successful orders:")
for item, qty in successes:
  print(f"  {item} x {qty}")

print("\nFailed orders:")
for item, qty, reason in failures:
  print(f"  {item} x {qty} -> {reason}")