from multiprocessing import Process, Queue

def worker(name, start, end, q):
  total= sum(range(start, end+1))
  q.put((name, total))

if __name__=="__main__":
  q= Queue()

  ranges= [
        ("Worker-1", 1, 100),
        ("Worker-2", 101, 200),
        ("Worker-3", 201, 300),
        ("Worker-4", 301, 400),
    ]
  
  processes= []
  for name, start, end in ranges:
    p= Process(target= worker, args= (name, start, end, q))
    processes.append(p)
    p.start()

  results= []
  for _ in range(4):
    results.append(q.get())

  for p in processes:
    p.join()

  grand_total= 0
  for name, subtotal in results:
    print(f"{name} computed sum: {subtotal}")
    grand_total+=subtotal

  print(f"Grand total: {grand_total}")