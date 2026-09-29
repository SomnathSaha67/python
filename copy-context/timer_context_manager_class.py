import time, random

class Timer:
  def __enter__(self):
    self.start= time.time()
    return self
  def __exit__(self, exc_type, exc_value, traceback):
    elapsed= time.time()- self.start
    print(f"Elapsed time: {elapsed:.3f} seconds")

try: 
  with Timer():
    delay= random.uniform(0.5, 1.5)
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)
    raise ValueError("Deliberate failure!")
except Exception as e:
  print(f"Caught exception: {e}")