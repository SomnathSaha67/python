from multiprocessing import Process, Value
import os

counter= 0

def increment_global():
  global counter
  for _ in range(5):
    counter+=1

if __name__=="__main__":
  p1= Process(target= increment_global)
  p2= Process(target= increment_global)

  p1.start()
  p2.start()
  p1.join()
  p2.join()

  print(f"Global counter after processes: {counter}")

  # Each process ahs its own private memory space. They modified their own copies of 
  # 'counter', not the main program's variable

def increment_shared(shared_counter):
  for _ in range(5):
    shared_counter.value+=1

if __name__=="__main__":
  shared_counter= Value('i', 0)

  p1= Process(target= increment_shared, args= (shared_counter,))
  p2= Process(target= increment_shared, args= (shared_counter,))

  p1.start()
  p2.start()
  p1.join()
  p2.join()

  print(f"Shared counter after processes: {shared_counter.value}")

  # both processes updated the same shared Value object.