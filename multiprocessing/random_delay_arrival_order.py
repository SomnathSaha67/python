import time, random
from multiprocessing import Process

def worker(task_num):
  delay= random.uniform(0.5, 3.0)
  time.sleep(delay)
  print(f"Task {task_num} finished after {delay:.2f} seconds")

if __name__=="__main__":
  processes= []
  for i in range(1, 6):
    p= Process(target= worker, args= (i,))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()
    