students = [("Alice", 82), ("Bob", 45), ("Carol", 91), ("Dave", 38), ("Eve", 67)]

passed_students= list(filter(lambda x: x[1]>=50, students))

distinction_students= list(filter(lambda stud: stud[1]>=85, passed_students))

first_letter_vowel= list(filter(lambda stud: stud[0][0] in "aeiouAEIOU", students))

print("Passed students:")
for stud, marks in passed_students:
  print(f"{stud}")

print("\nStudents eligible for Distinction:")
for stud, marks in distinction_students:
  print(f"{stud}")

print(f"\nStudents whose first letter of the name is a Vowel:")
for stud, marks in first_letter_vowel:
  print(f"{stud}")