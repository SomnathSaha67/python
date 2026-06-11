tasks=[4, 2, 7, 1]
print(tasks)
while tasks:
  tasks= [t-1 for t in tasks if t-1>0]
  if tasks:
    print(tasks)