total_events, succ_logins, failed_logins= 0, 0, 0
file_open= open('security_log.txt', 'r')
try:
  for status in file_open:
    if "SUCCESS" in status:
      succ_logins+=1
      total_events+=1
    elif "FAIL" in status:
      failed_logins+=1
      total_events+=1
    else:
      continue
  failure_percentage= round((failed_logins/total_events)*100, 2)
  print(f"Total Events: {total_events}")
  print(f"Successful Logins: {succ_logins}")
  print(f"Failed Logins: {failed_logins}")
  print(f"Failure Percentage: {failure_percentage}%")
except FileNotFoundError:
  print("File not exists.")
  quit()
except:
  print("Empty File")
  quit()