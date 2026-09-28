from multiprocessing import Process, Value, Lock
import time

def increment(shared_counter):
  for _ in range(100_000):
    shared_counter.value+=1

if __name__=="__main__":
  shared_counter= Value('i', 0)

  start= time.time()
  p1= Process(target= increment, args= (shared_counter,))
  p2= Process(target= increment, args= (shared_counter,))

  p1.start()
  p2.start()
  p1.join()
  p2.join()
  end= time.time()

  print(f"Final counter without lock: {shared_counter.value}")
  print(f"Time without lock: {end-start:.2f} seconds")

def inrcrement_locked(shared_counter, lock):
  for _ in range(100_000):
    with lock:
      shared_counter.value+=1

if __name__=="__main__":
  shared_counter= Value('i', 0)
  lock= Lock()

  start= time.time()
  p1= Process(target= inrcrement_locked, args= (shared_counter, lock))
  p2= Process(target= inrcrement_locked, args= (shared_counter, lock))

  p1.start()
  p2.start()
  p1.join()
  p2.join()
  end= time.time()

  print(f"Final coounter with lock: {shared_counter.value}")
  print(f"Time with lock: {end-start:.2f} seconds")