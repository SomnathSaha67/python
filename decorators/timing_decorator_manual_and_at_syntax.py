import time

# define the decorator
def time_it(func):
  def wrapper(*args, **kwargs):
    start= time.time()
    result= func(*args, **kwargs)
    end= time.time()
    print(f"{func.__name__} took {end-start:.4f} seconds")
    return result
  return wrapper

# manual application
def slow_function(delay_seconds):
  time.sleep(delay_seconds)
  print("Finished slow_function")

# wrap manually
slow_function= time_it(slow_function)

# call it
slow_function(2)

# using @ syntax
@time_it
def another_slow_function(delay_seconds):
  time.sleep(delay_seconds)
  print("Finished another_slow_function")

# call it
another_slow_function(3)