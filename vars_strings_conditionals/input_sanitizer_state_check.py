username, email, password, age= input("Enter username, email, password, age (with spaces): ").split(" ")

valid_username= True
if (username!=username.strip()):
  valid_username= False
elif (" " in username):
  valid_username= False

valid_email= True
if (email.count("@")!=1):
  valid_email= False
else:
  at_index= email.index("@")
  if ("." not in email[at_index+1:]):
    valid_email= False

valid_password= True
if (len(password)<8):
  valid_password= False
elif (not any(ch.isdigit() for ch in password)):
  valid_password= False
elif (not any(ch.upper() for ch in password)):
  valid_password= False

valid_age= True
if (age.isdigit()):
  age= int(age)
  if (age<=0):
    valid_age= False
else: 
  valid_age= False

if valid_username and valid_email and valid_password and valid_age:
  print("Signup successful: all validations passed.")
else:
  print("Signup failed due to:")
  if not valid_username:
    print("- Invalid username (whitespace or spaces inside).")
  if not valid_email:
    print("- Invalid email format (must contain one '@' and a '.' after).")
  if not valid_password:
     print("- Invalid password (min 8 chars, must include digit and uppercase).")
  if not valid_age:
    print("- Invalid age (must be numeric and positive).")