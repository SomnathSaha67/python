import sys

def fibonacci_list(n):
  fibs= []
  a, b= 0, 1
  for _ in range(n):
    fibs.append(a)
    a, b= b, a+b
  return fibs

def fibonacci_gen(n):
  a, b= 0, 1
  for _ in range(n):
    yield a
    a, b= b, a+b

print( "List version:")
print(fibonacci_list(10))

print("\nGenerator version:")
for num in fibonacci_gen(10):
  print(num, end= " ")
print()

n= 100000
fib_list= fibonacci_list(n)
fib_gen= fibonacci_gen(n)

print("\nMemory size comparison for n= 100000:")
print(f"List size: {sys.getsizeof(fib_list)}")
print(f"Generator size: {sys.getsizeof(fib_gen)}")