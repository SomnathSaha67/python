print("=== Scenario 1: Missing file ===")
try:
  with open("missing_data.txt", "r") as f:
    content= f.read()
except FileNotFoundError:
  print("Friendly message: The file 'missing_data.txt' does not exist.")
else:
  print(f"File content:\n{content}")
finally:
  print("File operation attempt finished.\n")

print("=== Scenario 2: File created and read ===")
with open("missing_data.txt", "w") as f:
  f.write("This is some sample content.\nLine two of the file.")

try:
  with open("missing_data.txt", "r") as f:
    content= f.read()
except FileNotFoundError:
  print("Friendly message: The file 'missing_data.txt' does not exist.")
else:
  print(f"File content:\n{content}")
finally:
  print("File operation attempt finished.")