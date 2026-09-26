class Countdown:
  def __init__(self, start):
    self.current= start

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current<=0:
      raise StopIteration
    val= self.current
    self.current-=1
    return val
  
def countdown_gen(start):
  while start>0:
    yield start
    start-=1

print("Class-based Countdown:")
for num in Countdown(5):
  print(num, end= " ")

print("\nGenerator-based Countdown:")
for num in countdown_gen(5):
  print(num, end= " ")