import logging, time

logging.basicConfig(
  level= logging.INFO,
  format= "%(asctime)s - %(levelname)s - %(message)s"
)

attempts= ["fail", "fail", "success"]
max_retries= len(attempts)

start_time= time.time()

for i, outcome in enumerate(attempts, start= 1):
  if outcome=="fail":
    logging.warning(f"Attempt {i} failed. Retrying...")
    if i<max_retries:
      time.sleep(1)
  elif outcome=="success":
    logging.info(f"Attempt {i} succeeded! Stopping retries.")
    break
else:
  logging.critical("All attempts failed. Giving up.")

end_time= time.time()
print(f"Total time taken: {end_time-start_time:.2f} seconds")