is_logged_in= False

def require_login(func):
  def wrapper(*args, **kwargs):
    global is_logged_in
    if not is_logged_in:
      print("Access denied: please log in first.")
      return None 
    else:
      return func(*args, **kwargs)
  return wrapper

@require_login
def view_dashboard():
  print("Welcome to your dashboard!")
  return "Dashboard data here"

# test run with is_logged_in= False
print("Case 1: Not logged in")
result1= view_dashboard()
print(f"Returned: {result1}")

# flip login flag
is_logged_in= True

print("Case 2: Logged in")
result2= view_dashboard()
print(f"Returned: {result2}")