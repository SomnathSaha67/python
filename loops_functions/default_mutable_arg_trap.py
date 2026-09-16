def add_to_batch(item, batch= []):

  batch.append(item)
  return batch

print("Demonstrating the trap:")

for i in ["apple", "banana", "cherry"]:

  result= add_to_batch(i)
  print(result)

def add_to_batch_safe(item, batch= None):

  if batch is None:
    batch= []
  batch.append(item)

  return batch

print("Demonstrating the fix:")

for i in ["apple", "banana", "cherry"]:

  result= add_to_batch_safe(i)

  print(result)