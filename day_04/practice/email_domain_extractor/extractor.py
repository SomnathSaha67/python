file_open= open('employees.txt', 'r')
for email in file_open:
  if email[-1]=="\n":
    print(f"{email[(email.find("@")):-1]}")
  else:
    print(f"{email[(email.find("@")):]}")