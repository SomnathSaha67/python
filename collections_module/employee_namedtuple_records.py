from collections import namedtuple

Employee= namedtuple("Employee", ("name", "age", "department"))

employees= [
  Employee("Alice", 29, "Engineering"),
  Employee("Bob", 24, "Sales"),
  Employee("Carol", 35, "Engineering")
]

for emp in employees:
  print(f"Name: {emp.name}, Age: {emp.age}, Department: {emp.department}")
  if emp.department=="Engineering" and emp.age>30:
    print("-> Senior track")
  print("---")