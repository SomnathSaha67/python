import logging, time

logging.basicConfig(level= logging.INFO, format= "%(levelname)s - %(message)s")

def manual_dedup(lst):
  dedup= []
  for item in lst:
    if item not in dedup:
      dedup.append(item)
  return dedup

def set_dedup(lst):
  return list(dict.fromkeys(lst))

test_input= [1, 2, 3, 4, 5] * 10000

start_manual= time.time()
manual_result= manual_dedup(test_input)
end_manual= time.time()
manual_time= end_manual- start_manual
logging.info(f"Approach A (manual) took {manual_time:.6f} seconds")

start_set= time.time()
set_result= set_dedup(test_input)
end_set= time.time()
set_time= end_set-start_set
logging.info(f"Approach B (set) took {set_time:.6f} seconds")

if manual_time<set_time:
  print(f"Manual approach was faster by ~{set_time-manual_time:.6f} seconds")
else:
  print(f"Set-based approach was faster by ~{manual_time - set_time:.6f} seconds")