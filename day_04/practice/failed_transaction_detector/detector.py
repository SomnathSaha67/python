failed_transactions=0
file_open= open('transactions.txt', 'r')
for status in file_open:
  if "SUCCESS" in status:
    continue
  else:
    print(f"{status[0:(status.find(" "))]}")
    failed_transactions+=1
print(f"Failed Transactions: {failed_transactions}")