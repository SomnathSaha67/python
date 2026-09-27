import threading, queue, time

task_queue= queue.Queue()

def producer():
  for i in range(1, 9):
    task_name= f"task-{i}"
    print(f"Producing {task_name}")
    task_queue.put(task_name)
    time.sleep(0.2)

def consumer(total_tasks):
  processed= 0
  while processed<total_tasks:
    try: 
      task= task_queue.get(timeout=0.1)
      print(f"Consuming {task}")
      processed+=1
    except queue.Empty:
      continue

producer_thread= threading.Thread(target=producer, name="Producer")
consumer_thread= threading.Thread(target= consumer, args= (8,), name= "Consumer")

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All tasks have been fully consumed")