import logging, time, traceback

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

tasks = [
    ("Task A", 0.5),
    ("Task B", 1.0),
    ("Broken Task", None), 
    ("Task D", 1.5)
]

total_start= time.time()
success_count= 0
fail_count= 0

for name, duration in tasks:
  logging.info(f"Starting {name}...")
  start= time.time()
  try:
    if duration is None:
      raise RuntimeError("Simulated failure in task")
    time.sleep(duration)
    elapsed= time.time()- start
    logging.info(f"{name} completed in {elapsed:.2f} seconds")
    success_count+=1
  except Exception as e:
    tb_str= traceback.format_exc()
    logging.error(f"{name} failed:\n{tb_str}")
    fail_count+=1

total_elapsed = time.time() - total_start
logging.info(
    f"Summary: Ran {len(tasks)} tasks, "
    f"{success_count} succeeded, {fail_count} failed, "
    f"total time {total_elapsed:.2f} seconds"
)