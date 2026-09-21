from collections import namedtuple

Employee= namedtuple("Employee", ("name", "age", "department"))

employees= [
  Employee("Alice", 29, "Engineering"),
  Employee("Bob", 24, "Sales"),
  Employee("Carol", 35, "Engineering"),
  Employee("Dave", 28, "HR")
]

# sort by age ascending
by_age= sorted(employees, key= lambda emp: emp.age)

# sort by department alphabetically
by_department= sorted(employees, key= lambda emp: emp.department)

# sort by department, then age within department
by_dept_then_age= sorted(employees, key= lambda emp: (emp.department, emp.age))

print("Sorted by age ascending:")
for emp in by_age:
  print(emp)

print("\nSorted by department alphabetically:")
for emp in by_department:
  print(emp)

print("\nSorted by department, then age within department:")
for emp in by_dept_then_age:
  print(emp)