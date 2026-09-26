import time

with open("big_notes.txt", "w") as f:
  f.write("Python is powerful\n")
  f.write("Generators are memory efficient\n")
  f.write("Decorators add reusable behavior\n")
  f.write("Classes organize code neatly\n")
  f.write("Files can be huge in practice\n")
  f.write("Streaming avoids memory blowups\n")

def read_lines_upper(filepath):
  with open(filepath, "r") as f:
    for line in f:
      yield line.strip().upper()

print("Reading big_notes.txt line by line in uppercase:")
for line in read_lines_upper("big_notes.txt"):
  print(line)

# This approach scales because the generator only keeps one line in memory at a time.
# Even if the file had millions of lines, it would still work fine.
# By contrast, using f.readlines() would load the entire file into a list,
# consuming huge amounts of memory proportional to file size.