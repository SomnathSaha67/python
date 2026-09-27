import time 
from multiprocessing import Process

def simulate_work(task_name, duration):
  print(f"Starting {task_name}")
  time.sleep(duration)
  print(f"Finished {task_name}")

if __name__=="__main__":
  # sequential version
  start_seq= time.time()
  for i in range(4):
    simulate_work(f"Task {i+1}", 2)
  end_seq= time.time()
  print(f"Sequential total time: {end_seq-start_seq:.2f} seconds")

  # parallel version using multiprocessing
  processes= []
  start_par= time.time()
  for i in range(4):
    p= Process(target= simulate_work, args= (f"Task {i+1}", 2))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()
  end_par= time.time()
  print(f"Parallel total time: {end_par-start_par:.2f} seconds")