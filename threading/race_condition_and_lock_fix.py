import threading, time

counter= 0

def increment_counter():
  global counter
  for _ in range(100_000):
    tmp= counter
    time.sleep(0.00001)
    counter= tmp+1

# without lock
counter= 0
t1= threading.Thread(target= increment_counter)
t2= threading.Thread(target= increment_counter)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final counter without lock: {counter}")

# with lock
counter= 0
lock= threading.Lock()

def increment_counter_locked():
  global counter
  for _ in range(100_000):
    with lock:
      tmp= counter
      time.sleep(0.00001)
      counter= tmp+1

t1= threading.Thread(target= increment_counter_locked)
t2= threading.Thread(target= increment_counter_locked)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final counter with lock: {counter}")