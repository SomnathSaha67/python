def load_dataset():
  valid_records, total, invalid_records, highest_score, lowest_score= 0, 0, 0, -float('inf'), float('inf')
  file_open= open('dataset.txt', 'r')
  for data in file_open:
    valid_records, invalid_records, highest_score, lowest_score, total= validate_record(data, total, valid_records, invalid_records, highest_score, lowest_score)
    average_score= total/valid_records
  compute_statistics(valid_records, invalid_records, highest_score, lowest_score, average_score)
def validate_record(data, current_sum, valid, invalid, highest, lowest):
  clean_data= data.strip()
  if clean_data:
    try:
      val= float(data)
      valid+=1
      current_sum+=val
      highest= max(highest, val)
      lowest= min(lowest, val)
    except:
      invalid+=1
  return valid, invalid, highest, lowest, current_sum
def compute_statistics(valid_records, invalid_records, highest_score, lowest_score, average_score):
  print(f"Valid Records: {valid_records}")
  print(f"Invalid Records: {invalid_records}")
  print(f"Average Score: {round(average_score,2)}")
  print(f"Highest Score: {highest_score}")
  print(f"Lowest Score: {lowest_score}")
load_dataset()