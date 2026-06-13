events = [
    "LOGIN",
    "LOGIN",
    "LOGIN",
    "ERROR",
    "ERROR",
    "UPLOAD",
    "UPLOAD",
    "UPLOAD",
    "UPLOAD"
]
login_count, error_count, upload_count= 0, 0, 0
for event in events:
  if event=="LOGIN":
    login_count+=1
  elif event=="ERROR":
    error_count+=1
  else:
    upload_count+=1
print(f"LOGIN occurred {login_count} times.")
print(f"ERROR occurred {error_count} times.")
print(f"UPLOAD occurred {upload_count} times.")