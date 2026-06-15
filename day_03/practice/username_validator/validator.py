username= input("Enter username: ")
try:
  if 5<=len(username)<=15 and (not float(username[0])) and not any(c not in " " for c in username):
    print("VALID")
  else:
    print("INVALID")
except:
  print("INVALID")