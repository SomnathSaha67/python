inventory_count= 100

def read_inventory():

  print(f"Read inventory_count (global): {inventory_count}")

def shadow_inventory():

  inventory_count= 50

  print(f"Local shadow inventory_count: {inventory_count}")

def modify_inventory():

  global inventory_count

  inventory_count+=10

  print(f"Modified global inventory_count: {inventory_count}")

for i in range(2):

  print(f"\nIteration {i+1}:")

  read_inventory()
  print(f"After read -> global inventory_count: {inventory_count}")

  shadow_inventory()
  print(f"After shadow -> global inventory_count: {inventory_count}")

  modify_inventory()
  print(f"After modify -> global inventory_count: {inventory_count}")