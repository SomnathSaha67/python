def use_append(lst):
  print("\n--- use_append ---")
  print(f"Inside before: {lst} | id: {id(lst)}")
  lst.append(99)
  print(f"Inside after: {lst} | id: {id(lst)}")

def use_plus(lst):
  print("\n--- use_plus ---")
  print(f"Inside before: {lst} | id: {id(lst)}")
  lst= lst + [99]
  print(f"Inside after: {lst} | id: {id(lst)}")

def use_iadd(lst):
  print("\n--- use_iadd ---")
  print(f"Inside before: {lst} | id: {id(lst)}")
  lst += [99]
  print(f"Inside after: {lst} | id: {id(lst)}")

original= [1, 2, 3]

lst1= original.copy()
use_append(lst1)
print(f"Outside after append: {lst1} | id: {id(lst1)}")

lst2= original.copy()
use_plus(lst2)
print(f"Outside after plus: {lst2} | id: {id(lst2)}")

lst3= original.copy()
use_iadd(lst3)
print(f"Outside after iadd: {lst3} | id: {id(lst3)}")


t = (1, 2, 3)
print("\nTuple before:", t, "| id:", id(t))
t_plus = t + (99,)
print("Tuple after t + (99,):", t_plus, "| id:", id(t_plus))
t_iadd = t
t_iadd += (99,)
print("Tuple after t += (99,):", t_iadd, "| id:", id(t_iadd))


x = 10
print("\nInt before:", x, "| id:", id(x))
x_plus = x + 5
print("Int after x + 5:", x_plus, "| id:", id(x_plus))
x_iadd = x
x_iadd += 5
print("Int after x += 5:", x_iadd, "| id:", id(x_iadd))