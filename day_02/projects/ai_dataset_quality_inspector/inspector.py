def main():
  total_samples, valid_samples, invalid_samples= 0, 0, 0
  dataset_quality, highest_score, lowest_score, average_score, total_sum = 0, -float('inf'), float('inf'), 0, 0
  while True:
    value= input("Enter value('STOP' to stop): ")
    if value.upper()=='STOP':
      generate_report(dataset_quality, highest_score, lowest_score, average_score, valid_samples, invalid_samples)
      break
    else:
      total_samples+=1
      is_valid= validate_record(value)
      if is_valid==True:
        valid_samples+=1
        dataset_quality, highest_score, lowest_score, average_score, total_sum= update_metrics(total_samples, valid_samples, invalid_samples, float(value), highest_score, lowest_score, total_sum)
      else:
        invalid_samples+=1
def validate_record(value):
  try:
    float(value)
    return True
  except:
    return False
def update_metrics(total_samples, valid_samples, invalid_samples, value, current_hi, current_lo, current_sum):
  dataset_quality= round((valid_samples/total_samples)*100, 2)
  highest_score= max(current_hi, value)
  lowest_score= min(current_lo, value)
  new_total_sum = current_sum + value
  average_score= round(new_total_sum/valid_samples, 2)
  return dataset_quality, highest_score, lowest_score, average_score, new_total_sum
def generate_report(dataset_quality, highest_score, lowest_score, average_score, valid_samples, invalid_samples):
  print("\n" + "REPORT".center(20, "-"))
  print(f"Valid Samples: {valid_samples}")
  print(f"Invalid Samples: {invalid_samples}")
  print(f"Average Score: {average_score}")
  print(f"Highest Score: {highest_score if valid_samples > 0 else 0}")
  print(f"Lowest Score: {lowest_score if valid_samples > 0 else 0}")
  print(f"Dataset Quality: {dataset_quality}%")
if __name__=="__main__":
  main()