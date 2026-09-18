class Employee:
  
  MIN_WAGE= 5000
  def __init__(self, name, salary):
    self.name= name
    if self._is_valid_salary(salary):
      self.__salary= salary
    else:
      self.__salary= Employee.MIN_WAGE
      print(f"Warning: Invalid salary for {name}. Set to minimum wage ${Employee.MIN_WAGE}")

  def get_salary(self):
    return f"${self.__salary}"
  
  def _is_valid_salary(self, amount):
    return amount>= Employee.MIN_WAGE
  
  def set_salary(self, new_salary):
    if self._is_valid_salary(new_salary):
      self.__salary=new_salary
      print(f"Salary updated for {self.name}: ${self.__salary}")
    else:
      print(f"Rejected salary ${new_salary} for {self.name}. Must be greater than or equal to ${Employee.MIN_WAGE}")

emp1 = Employee("Alice", 8000)   
emp2 = Employee("Bob", 3000)     
emp3 = Employee("Charlie", 5000) 

print(emp1.name, emp1.get_salary())   
print(emp2.name, emp2.get_salary())   
print(emp3.name, emp3.get_salary())   

emp1.set_salary(12000)   
emp2.set_salary(2000)   
emp3.set_salary(7000)  