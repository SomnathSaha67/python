import time, random
from contextlib import contextmanager

@contextmanager
def timer():
  start= time.time()
  try:
    yield
  finally:
    elapsed= time.time()-start
    print(f"Elapsed time: {elapsed:.3f} seconds")

@contextmanager
def managed_resource(name):
  print(f"Acquiring {name}")
  try:
    yield
  finally:
    print(f"Releasing {name}")

try:
  with timer():
    delay= random.uniform(0.5, 1.5)
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)
    raise RuntimeError("Deliberate crash!")
except Exception as e:
  print(f"Caught exception: {e}")

print("\n--- Resource demo ---")
with managed_resource("DatabaseConnection"):
  print("Performing queries...")
  time.sleep(0.5)