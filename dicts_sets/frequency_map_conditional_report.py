error_log = "500,404,500,500,403,404,500,200,403"

data= error_log.split(",")

final_data= {}

for code in data:
  count= data.count(code)
  if (count>=3):
    severity= "critical"
  elif (count==2):
    severity= "watch"
  else:
    severity= "normal"
  final_data[code]= (count, severity)

print(f"Summary of the log:")
print("----------------------")
print("Code  Count   Severity")
for code, (count, severity) in final_data.items():
  print(f"{code}:   {count}      {severity}")