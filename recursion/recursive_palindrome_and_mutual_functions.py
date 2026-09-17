def is_palindrome_recursive(s):
  s= s.lower()

  if len(s)<=1:
    return True
  
  if s[0]!=s[-1]:
    return False
  
  return is_palindrome_recursive(s[1:-1])

print("Palindrome 'madam':", is_palindrome_recursive("madam"))
print("Non-palindrome 'hello':", is_palindrome_recursive("hello"))
print("Mixed case 'RaceCar':", is_palindrome_recursive("RaceCar"))

def is_even_rec(n):
  if n==0:
    return True
  return is_odd_rec(n-1)

def is_odd_rec(n):
  if n==0:
    return False
  return is_even_rec(n-1)

print("\nis_even_rec(0):", is_even_rec(0))   
print("is_even_rec(4):", is_even_rec(4))
print("is_odd_rec(7):", is_odd_rec(7))