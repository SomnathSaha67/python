import threading, time

def fetch_data(source_name, delay):
  print(f"Starting fetch from {source_name}...")
  time.sleep(delay)
  print(f"Finished fetch from {source_name}!")

# sequential version
start_seq= time.time()
for i in range(4):
  fetch_data(f"Source{i+1}", 2)
end_seq= time.time()
print(f"Sequential total time: {end_seq-start_seq:.2f} seconds")

# parallel version using threads
threads= []
start_thr= time.time()
for i in range(4):
  t= threading.Thread(target= fetch_data, args= (f"Source{i+1}", 2))
  threads.append(t)
  t.start()

for t in threads:
  t.join()
end_thr= time.time()
print(f"Threaded total time: {end_thr-start_thr:.2f} seconds")