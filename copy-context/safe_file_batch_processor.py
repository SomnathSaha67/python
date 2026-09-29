import json, copy, time, logging
from contextlib import contextmanager

template_records= [{"name": "template",
                    "scores": [0, 0, 0]}]
with open("templates.json", "w") as f:
  json.dump(template_records, f, indent= 4)

@contextmanager
def batch_job(job_name):
  logging.basicConfig(level= logging.INFO, format= "%(message)s")
  logging.info(f"Starting job: {job_name}")
  start= time.time()
  try:
    yield
  finally:
    elapsed= time.time()-start
    logging.info(f"Finished job: {job_name} (elapsed {elapsed:.3f} seconds)")

with batch_job("Clone and Customize Records"):
  with open("templates.json", "r") as f:
    templates= json.load(f)

  rec1= copy.deepcopy(templates[0])
  rec2= copy.deepcopy(templates[0])
  rec3= copy.deepcopy(templates[0])

  rec1["name"]= "Alice"
  rec1["scores"]= [88, 92, 79]

  rec2["name"]= "Bob"
  rec2["scores"]= [65, 70, 60]

  rec3["name"]= "Charlie"
  rec3["scores"]= [95, 85, 90]

  rec1["scores"][0] = 999
  print("Original template:", templates)   
  print("rec1:", rec1)
  print("rec2:", rec2)
  print("rec3:", rec3)

  final_records= [rec1, rec2, rec3]
  with open("final_records.json", "w") as f:
    json.dump(final_records, f, indent= 4)