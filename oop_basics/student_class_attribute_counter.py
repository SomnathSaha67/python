class Student:

  total_students=0

  def __init__(self, name, marks):
    self.name= name
    self.marks= marks
    Student.total_students+=1
  
  def grade(self):
    if 90<=self.marks<=100: return 'A'
    elif 80<=self.marks<90: return 'B'
    elif 70<=self.marks<80: return 'C'
    elif 60<=self.marks<=70: return 'D'
    elif self.marks<60: return 'F'
    else: return "Invalid marks"

students_data = [("Alice", 95), ("Bob", 82), ("Charlie", 76), ("Diana", 59)]
students = []

for name, marks in students_data:
  s= Student(name, marks)
  students.append(s)
  print(f"{s.name}: {s.grade()}")

print(f"Total students: {Student.total_students}")