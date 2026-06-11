total_events, succ_events, failed_events, value_error, type_error= 0, 0, 0, 0, 0
logs = [
    "OK",
    "VALUE_ERROR",
    "OK",
    "TYPE_ERROR",
    "VALUE_ERROR",
    "VALUE_ERROR",
    "OK"
]
for i in logs:
  if i=="OK":
    succ_events+=1
  else:
    failed_events+=1
    if i=="VALUE_ERROR":
      value_error+=1
    elif i=="TYPE_ERROR":
      type_error+=1
    max_error= max(value_error, type_error)
  total_events+=1
if max_error==value_error:
  common_error= "ValueError"
else:
  common_error= "TypeError"
print(f"Total Events: {total_events}")
print(f"Successful Events: {succ_events}")
print(f"Failed Events: {failed_events}")
print(f"Most Common Error: {common_error}")
print(f"Failure Percentage: {round((failed_events/total_events)*100, 2)}%")
