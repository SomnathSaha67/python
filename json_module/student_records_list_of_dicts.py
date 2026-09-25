import json

students = [
    {"name": "Alice", "scores": [88, 92, 79]},
    {"name": "Bob", "scores": [65, 70, 60]}
]

studentsJSON= json.dumps(students, indent= 4)
print(studentsJSON)

with open("students.json", "w") as f:
  json.dump(students, f, indent= 4)

with open("students.json", "r") as f:
  reloaded_students= json.load(f)

highest_avg= -1
top_student= None

for student in reloaded_students:
  scores= student["scores"]
  avg= sum(scores)/len(scores)
  print(f"{student['name']} average: {avg:.2f}")

  if avg>highest_avg:
    highest_avg= avg
    top_student= student["name"]

print(f"\nTop student: {top_student} with average {highest_avg:.2f}")