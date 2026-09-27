from multiprocessing import Process

def worker_with_args(name, multiplier, base_number):
  result= base_number*multiplier
  print(f"{name}: {base_number} X {multiplier}= {result}")

def worker_no_args():
  print("Woker with no args says hello!")

if __name__=="__main__":
  p1= Process(target= worker_with_args, args= ("Process 1", 2, 5))
  p2= Process(target= worker_with_args, args= ("Process 2", 3, 7))
  p3= Process(target= worker_with_args, args= ("Process 3", 4, 10))

  p4= Process(target= worker_no_args)

  for p in (p1, p2, p3, p4):
    p.start()

  for p in (p1, p2, p3, p4):
    p.join()

  print("\nAl 4 processes have completed - join() ensured we waited for the full batch.")