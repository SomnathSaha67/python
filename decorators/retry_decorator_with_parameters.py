import logging, random

logging.basicConfig(level=logging.WARNING, format="%(levelname)s - %(message)s")

# decorator factory with argument
def retry(times= 3):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for attempt in range(1, times+1):
        try:
          return func(*args, **kwargs)
        except Exception as e:
          logging.warning(f"Attempt {attempt} failed: {e}")
          if attempt==times:
            # let the final exception raise
            raise
    return wrapper
  return decorator

@retry(times=3)
def flaky_function():
  if random.choice([True, False]):
    print("Success!")
    return "Data loaded!"
  else:
    raise RuntimeError("Random failure occurred")
  
for i in range(5):
  print(f"\nRun {i+1}:")
  try:
    result= flaky_function()
    print(f"Returned: {result}")
  except Exception as e:
    print(f"Final exception raised: {e}")