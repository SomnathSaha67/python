total_events, failure_count, error_count, timeout_count= 0, 0, 0, 0
while True:
  message= input("Enter message('STOP' to stop): ")
  if message=='STOP':
    break
  try:
    if message.upper()=="OK":
      total_events+=1
      continue
    elif message.upper()=="ERROR":
      failure_count+=1
      error_count+=1
    elif message.upper()=="TIMEOUT":
      failure_count+=1
      timeout_count+=1
    else:
      failure_count+=1
  except:
    failure_count+=1
  total_events+=1
  maximum= max(error_count, timeout_count)
if maximum==error_count:
  common= "Error"
else:
  common= "TimeOutError"
print("Monitoring Report:")
print(f"Total Events: {total_events}")
print(f"Total Failures: {failure_count}")
print(f"Failure Percentage: {round((failure_count/total_events)*100, 2)}%")
print(f"Common Failure Type: {common}")