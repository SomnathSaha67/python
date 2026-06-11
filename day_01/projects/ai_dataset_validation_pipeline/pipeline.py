valid_records, invalid_records, sum, maximum, minimum= 0, 0, 0, -float('inf'), float('inf')
while True:
  value= input("Enter any numeric value('STOP' to stop): ")
  if value.upper()=='STOP':
    break
  try:
    if float(value):
      valid_records+=1
      sum+=float(value)
      maximum= max(maximum, float(value))
      minimum= min(minimum, float(value))
    else:
      invalid_records+=1
      print("Invalid Value")
  except:
    invalid_records+=1
    print("Invalid Value")
print(f"Dataset Summary\n{'-'*len("Dataset Summary")}")
print(f"Valid Records: {valid_records}")
print(f"Invalid Records: {invalid_records}")
print(f"Average: {round(sum/valid_records, 2)}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")