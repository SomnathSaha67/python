# Build nested structure
students = {
    "Alice": [("Math", 92), ("Physics", 88)],
    "Bob": [("Math", 76), ("Physics", 81)]
}

# Serialize to custom flat text format
def dump_grades(data, filename= "grades_dump.txt"):
  with open(filename, "w") as f:
    for student, grades in data.items():
      for subject, score in grades:
        f.write(f"{student}|{subject}|{score}\n")

# Read back and reconstruct
def load_grades(filename= "grades_dump.txt"):
  result= {}
  with open(filename, "r") as f:
    for line in f:
      student, subject, score= line.strip().split("|")
      score= int(score)
      if student not in result:
        result[student]= []
      result[student].append((subject, score))
  return result

# Run serialization + reconstruction
dump_grades(students)
reconstructed= load_grades()

# Verify correctness
print(f"Reconstructed: {reconstructed}")
print(f"Equal to original? {reconstructed==students}")