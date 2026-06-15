text= input("Enter any text: ")
seen= ""
for char in text:
  if char not in seen:
    count=0
    for item in text:
      if item==char:
        count+=1
    print(f"{char} -> {count}")
    seen+=char