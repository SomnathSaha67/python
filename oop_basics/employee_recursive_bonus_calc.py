class Employee:

  def __init__(self, name, base_salary):
    self.name= name
    self.base_salary= base_salary

  def calculate_bonus(self, years_left):

    if years_left==0:
      return 0
    this_year_bonus= 0.02*self.base_salary
    return this_year_bonus+self.calculate_bonus(years_left-1)
  
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 70000),
    Employee("Charlie", 90000)
]

for e in employees:
  years= 3
  bonus= e.calculate_bonus(years)
  final_salary= e.base_salary+bonus
  print(f"{e.name} | Base: ${e.base_salary} | Bonus ({years} yrs): ${bonus:.2f} | Final: ${final_salary:.2f}")