from_lines, gmail_count, yahoo_count, other_count= 0, 0, 0, 0
file_open= open('mailbox.txt', 'r')
for line in file_open:
  if "From" in line:
      from_lines+=1
      if "gmail" in line[(line.find("@")):]:
        gmail_count+=1
      elif "yahoo" in line[(line.find("@")):]:
        yahoo_count+=1
      else:
        other_count+=1
  else:
    continue
print(f"Total 'From' lines: {from_lines}")
print(f"Gmail Count: {gmail_count}")
print(f"Yahoo Count {yahoo_count}")
print(f"Other Domains Count: {other_count}")