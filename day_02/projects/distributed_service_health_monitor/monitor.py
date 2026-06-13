def main():
  total_events, succ_events, failed_events, db_failure, cache_failure, freq_failure= 0, 0, 0, 0, 0, ""
  while True:
    event= input("Enter event('STOP' to stop): ")
    if event.upper()=='STOP':
      break
    feedback, type= health_monitor(event)
    total_events+=1
    if feedback=="success":
      succ_events+=1
    else:
      failed_events+=1
      if type=="DB":
        db_failure+=1
        print(feedback)
      elif type=="CACHE":
        cache_failure+=1
        print(feedback)
      most_failure= max(db_failure, cache_failure)
  if most_failure==db_failure:
    freq_failure= "Database Failure"
  elif most_failure==cache_failure:
    freq_failure= "Cache Failure"
  print(f"Total Events: {total_events}")
  print(f"Successful Events: {succ_events}")
  print(f"Failed Events: {failed_events}")
  print(f"Success Rate: {round((succ_events/total_events)*100, 2)}%")
  print(f"Failure Rate: {round((failed_events/total_events)*100, 2)}%")
  print(f"Most Frequent Failure: {freq_failure}")
def health_monitor(event):
  if event.upper()=="API_OK":
    return "success", 1
  else:
    if event.upper()=="DB_FAIL":
      return "Database Failure", "DB"
    elif event.upper()=="CACHE_FAIL":
      return "Cache Failure", "CACHE"
if __name__=="__main__":
  main()