from multiprocessing import Process, Array

def worker(shared_array, index):
  shared_array[index]= index*index

if __name__=="__main__":
  shared_array= Array('i', [0, 0, 0, 0])

  processes= []
  for i in range(4):
    p= Process(target= worker, args= (shared_array, i))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()

  print(f"Final array contents: {list(shared_array)}")