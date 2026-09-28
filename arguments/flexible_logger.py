def log_event(event_name, *details, **metadata):
  print(f"Event: {event_name}")
  print(f"Details: {list(details)}")
  print("Metadata:")
  for key, value in metadata.items():
    print(f"  {key} = {value}")

  print(f"Type(details): {type(details)}")
  print(f"Type(metadata): {type(metadata)}")

log_event("startup")

log_event("data_load", "file1.csv", "file2.csv")

log_event("user_login", user= "ALice", level= "INFO")

log_event("error", "disk full", "retrying", user= "bob", level= "ERROR")