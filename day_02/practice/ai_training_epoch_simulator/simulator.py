def main():
  total_epochs, previous_loss, best_loss, worst_loss, epoch= 0, None, float('inf'), -float('inf'), 1
  while True:
    loss_value= input("Enter loss value('STOP' to stop): ")
    if loss_value.upper()=='STOP':
      break
    current_loss= float(loss_value)
    total_epochs+=1
    if previous_loss is None:
      print(f"Epoch {epoch} -> Initial Loss")
    else:
      status= train(current_loss, previous_loss)
      if status=="Improved":
        print(f"Epoch {epoch} -> {status}")
      elif status=="Regression Detected":
        print(f"Epoch {epoch} -> {status}")
      else: print(f"Epoch {epoch} -> {status}")
    best_loss= min(best_loss, float(loss_value))
    worst_loss= max(worst_loss, float(loss_value))
    previous_loss= current_loss
    epoch+=1
  print(f"\nBest Loss: {best_loss}")
  print(f"Worst Loss: {worst_loss}")
  print(f"Total Epochs: {total_epochs}")
def train(current, previous):
  if current<previous:
    return "Improved"
  elif current> previous:
    return "Regression Detected"
  else:
    return "No change"
if __name__=="__main__":
  main()