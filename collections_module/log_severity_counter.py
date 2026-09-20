from collections import Counter

error_log = "500,404,500,500,403,404,500,200,403".split(",")

freq= Counter(error_log)

print(f"Full frequency counter: {freq}")

print(f"Top 2 frequent codes: {freq.most_common(2)}")

print("Classification report:")
for code, count in freq.items():
  if count>=3:
    status= "critical"
  elif count==2:
    status= "watch"
  else:
    status= "normal"
  print(f"{code}: {count} -> {status}")