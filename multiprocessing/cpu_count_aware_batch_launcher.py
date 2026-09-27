import os, time
from multiprocessing import Process

def worker(job_name):
  time.sleep(1)
  print(f"{job_name} done")

if __name__=="__main__":
  cores= os.cpu_count()
  print(f"Machine has {cores} CPU cores")

  jobs= [f"Job {i+1}" for i in range(24)]

  waves= [jobs[i:i+cores] for i in range(0, len(jobs), cores)]

  for wave_num, wave_jobs in enumerate(waves, start= 1):
    print(f"\n--- Starting Wave {wave_num} with {len(wave_jobs)} jobs ---")
    processes= []
    start_wave= time.time()

    for job in wave_jobs:
      p= Process(target= worker, args= (job,))
      processes.append(p)
      p.start()

    for p in processes:
      p.join()

    end_wave= time.time()
    print(f"--- Wave {wave_num} finished in {end_wave-start_wave:.2f} seconds")