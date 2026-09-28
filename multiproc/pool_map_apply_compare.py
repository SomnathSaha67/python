from multiprocessing import Pool
import time, os

def slow_square(n):
  time.sleep(1)
  return n*n

if __name__=="__main__":
  pool= Pool(4) # 4 worker processes

  start= time.time()
  results_map= pool.map(slow_square, range(1, 9))
  end= time.time()

  print(f"Results from pool.map: {results_map}")
  print(f"Time for pool.map: {end- start:.2f} seconds")

  start= time.time()
  result_apply= pool.apply(slow_square, (5,))
  end= time.time()

  print(f"Result from pool.apply: {result_apply}")
  print(f"Time for pool.apply: {end- start:.2f} seconds")

  pool.close()
  pool.join()