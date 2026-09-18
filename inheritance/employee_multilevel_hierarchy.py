class Employee:

  def __init__(self, name, base_salary):
    self.name= name
    self.base_salary= base_salary

  def salary_breakdown(self):
    print(f"{self.name} | Base salary: ${self.base_salary}")
    return self.base_salary

class Manager(Employee):

  def __init__(self, name, base_salary, team_size):
    super().__init__(name, base_salary)
    self.team_size= team_size

  def salary_breakdown(self):
    total= super().salary_breakdown()
    bonus= self.team_size*1000
    print(f"Manager bonus (team size {self.team_size}): ${bonus}")
    return total+bonus

class SeniorManager(Manager):

  def __init__(self, name, base_salary, team_size, department_count):
    super().__init__(name, base_salary, team_size)
    self.department_count= department_count

  def salary_breakdown(self):
    total= super().salary_breakdown()
    bonus= self.department_count*5000
    print(f"Senior Manager bonus (departments {self.department_count}): ${bonus}")
    return total+bonus

sm= SeniorManager("Alice", 80000, team_size= 5, department_count= 2)

print("\n--- Salary Breakdown Chain ---")
final_salary= sm.salary_breakdown()
print(f"Final total salary: ${final_salary}")