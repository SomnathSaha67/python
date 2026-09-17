def calculate_total_size(node):
  name, size, children= node

  if not children:
    return size
  
  total= size
  for child in children:
    total+=calculate_total_size(child)
  return total

def count_files(node):
  name, size, children= node

  if not children:
    return 1

  total= 0
  for child in children:
    total+= count_files(child)
  return total

filesystem = ("root", 0, [("file1.txt", 120, []), ("subfolder", 0, [("file2.txt", 300, []), ("file3.txt", 80, [])])])

print(f"Total size of filesystem: {calculate_total_size(filesystem)}")
print(f"Total number of files: {count_files(filesystem)}")