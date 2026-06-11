attempts=5
while attempts>0:
  username= input("Enter username: ")
  password= input("Enter password: ")
  try:
    if type(float(username))==float or type(float(password))==float or any(c in "!@. " for c in username) or any(c in "!@. " for c in password):
      attempts-=1
      print("Invalid Input")
  except:
    if username=="admin" and password=="python123":
      print("Login Successful!")
      break
    else:
      attempts-=1
      if not username=="admin":
        print("Wrong Username")
      if not password=="python123":
        print("Wrong Password") 
  print(f"Attempts left: {attempts}")
print("Try again after 5 minutes...")