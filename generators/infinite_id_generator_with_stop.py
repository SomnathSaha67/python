def generate_ids(prefix):
  counter= 1
  while True:
    yield f"{prefix}-{counter}"
    counter+=1

print("Manual next() calls:")
gen1= generate_ids("user")
for _ in range(5):
  print(next(gen1))

print("\nFor loop with break:")
gen2= generate_ids("order")
for idx, val in enumerate(gen2, start= 1):
  print(val)
  if idx==5:
    break