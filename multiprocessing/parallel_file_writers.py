import time
from multiprocessing import Process

def worker(filename, text, delay):
  time.sleep(delay)
  with open(filename, "w") as f:
    f.write(text)
  print(f"{filename} written after {delay} seconds")

if __name__=="__main__":
  jobs= [
        ("process_1_output.txt", "Hello from Process 1", 1),
        ("process_2_output.txt", "Greetings from Process 2", 2),
        ("process_3_output.txt", "Message from Process 3", 3),
    ]
  
  processes= []
  for filename, text, delay in jobs:
    p= Process(target= worker, args= (filename, text, delay))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()

  print("\n--- All processes finished. Reading files ---")
  for filename, _, _ in jobs:
    with open(filename, "r") as f:
      content= f.read()
    print(f"{filename}: {content}")