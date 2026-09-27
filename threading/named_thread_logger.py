import threading, logging

logging.basicConfig(
  level= logging.INFO,
  format= "%(asctime)s [%(threadName)s] %(message)s"
)

def worker(task_number):
  logging.info(f"Running task {task_number}")

t1= threading.Thread(target= worker, args= (1,), name= "Worker-A")
t2= threading.Thread(target= worker, args=(2,), name= "Worker-B")
t3= threading.Thread(target= worker, args= (3,), name= "Worker-C")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

logging.info("All tasks completed")