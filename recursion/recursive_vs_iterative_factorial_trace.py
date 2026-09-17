def factorial_recursive(n, depth=0):
  print(" "*depth + f"Entering factorial_recursive(n= {n}, depth= {depth})")

  if n==0 or n==1:
    print(" "*depth + f"Base case reached: returning 1")
    return 1

  result= n*factorial_recursive(n-1, depth+1)
  print(" "*depth + f"Unwinding: n+{n}, result= {result}")

  return result

def factorial_iterative(n):
  result= 1
  for i in range(1, n+1):
    result*=i
  
  return result

print("=== Recursive Trace ===")
print("Final Result:", factorial_recursive(5))

print("\n=== Iterative Result ===")
print("Final Result:", factorial_iterative(5))