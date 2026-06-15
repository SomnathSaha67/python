emails = [
    "a@gmail.com",
    "b@yahoo.com",
    "c@gmail.com",
    "d@outlook.com",
    "e@gmail.com"
]
extension=[]
for mail in emails:
  find_at_the_rate= mail.find("@")
  if mail[find_at_the_rate+1:] not in extension:
    count=0
    for item in emails:
      if item[find_at_the_rate+1:]==mail[find_at_the_rate+1:]:
        count+=1
    print(f"{mail[find_at_the_rate+1:]} -> {count}")
    extension.append(mail[find_at_the_rate+1:])