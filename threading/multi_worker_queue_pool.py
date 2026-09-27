import threading, queue

task_queue= queue.Queue()
for i in range(1, 11):
  task_queue.put(f"Job-{i}")

job_counts= {}
lock= threading.Lock()

def worker():
  while not task_queue.empty():
    try:
      job= task_queue.get_nowait()
    except queue.Empty:
      break
    print(f"{job} handled by {threading.current_thread().name}")
    with lock:
      job_counts[threading.current_thread().name]= job_counts.get(threading.current_thread().name, 0)+1
    task_queue.task_done()

threads= [
  threading.Thread(target=worker, name="Worker-A"),
  threading.Thread(target=worker, name="Worker-B"),
  threading.Thread(target=worker, name="Worker-C"),
]

for t in threads:
  t.start()

for t in threads:
  t.join()

print("\nFinal report:")
for worker_name, count in job_counts.items():
  print(f"{worker_name} handled {count} jobs")