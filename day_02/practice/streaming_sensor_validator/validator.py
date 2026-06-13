valid_count, invalid_count, largest_reading, smallest_reading= 0, 0, -float('inf'), float('inf')
while True:
  value= input("Enter value produced by the sensor('STOP' to stop): ")
  if value.upper()=='STOP':
    break
  try:
    if float(value):
      valid_count+=1
      largest_reading= max(largest_reading, float(value))
      smallest_reading= min(smallest_reading, float(value))
  except:
    invalid_count+=1
  print(f"Valid Sensor Values: {valid_count}")
  print(f"Invalid Sensor Values: {invalid_count}")
  print(f"Largest Reading: {largest_reading}")
  print(f"Smallest Reading: {smallest_reading}")