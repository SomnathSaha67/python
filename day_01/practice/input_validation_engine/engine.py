valid_nos, largest_no, smallest_no, sum= 0, -float('inf'), float('inf'), 0
while True:
  choice= input("Enter an integer('STOP' to stop): ")
  if choice.upper()=='STOP':
    break
  try:
    if int(choice) and (('.' not in choice) and (' ' not in choice)):
      valid_nos+=1
      sum+=int(choice)
      largest_no= max(largest_no, int(choice))
      smallest_no= min(smallest_no, int(choice))
    else:
      print("Invalid input")
  except ValueError:
    print("Invalid input")
print(f"Valid numbers: {valid_nos}")
print(f"Largest number: {largest_no}")
print(f"Smallest number: {smallest_no}")
print(f"Average: {round(sum/valid_nos, 2)}")