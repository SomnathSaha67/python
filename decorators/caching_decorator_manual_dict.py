import time

def cache_results(func):
  cache= {}

  def wrapper(*args, **kwargs):
    key= (args, tuple(sorted(kwargs.items())))
    if key in cache:
      print(f"Cache hit for {func.__name__} {args} {kwargs}")
      return cache[key]
    else:
      result= func(*args, **kwargs)
      cache[key]= result
      print(f"Freshly computed for {func.__name__} {args} {kwargs}")
      return result
  return wrapper

@cache_results
def slow_square(n):
  time.sleep(1)
  return n*n

print("First call (should be slow):")
print(f"Result: {slow_square(5)}")

print("\nSecond call (should be instant, cached):")
print(f"Result: {slow_square(5)}")