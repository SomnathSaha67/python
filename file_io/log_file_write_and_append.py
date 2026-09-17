import os
from datetime import datetime

def log_event(filepath, event_type, message):

  timestamp= datetime.now().strftime("%Y-%m-%d %H-%M-%S")

  mode= 'a' if os.path.exists(filepath) else 'w'

  with open(filepath, mode) as f:
    f.write(f"{timestamp} | {event_type} | {message}\n")

events= [("INFO", "Server started"),
    ("ERROR", "Database connection failed"),
    ("INFO", "Retry successful"),
    ("ERROR", "Timeout on request 4471"),
    ("INFO", "Shutdown complete")]

log_file= "app_events.log"

if os.path.exists(log_file):
  os.remove(log_file)

for event_type, message in events:
  log_event(log_file, event_type, message)

info_count=0
error_count=0

if os.path.exists(log_file):
  with open(log_file, 'r') as f:
    lines= f.readlines()
    for line in lines:
      if " | INFO | " in line:
        info_count+=1
      elif " | ERROR |" in line:
        error_count+=1

print(f"INFO events: {info_count}")
print(f"ERROR events: {error_count}")