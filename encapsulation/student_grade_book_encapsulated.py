class GradeBook:

  def __init__(self, student_name):
    self.student_name= student_name
    self.__grades= []

  def _is_valid_score(self, score):
    return 0<=score<=100
  
  def add_grade(self, score):
    if self._is_valid_score(score):
      self.__grades.append(score)
      print(f"Added grade {score} for {self.student_name}")
    else:
      print(f"Rejected invalid grade {score} for {self.student_name}")

  def average(self):
    if len(self.__grades)==0:
      return 0
    return sum(self.__grades)/len(self.__grades)
  
  def get_grades(self):
    return self.__grades[:]
  
  def get_student_name(self):
    return self.student_name
  
gb = GradeBook("Alice")

gb.add_grade(95)     
gb.add_grade(82)     
gb.add_grade(-5)     
gb.add_grade(105)   
gb.add_grade(76)

with open("gradebook_report.txt", "w") as f:
    f.write(f"Student: {gb.get_student_name()}\n")
    f.write(f"Grades: {gb.get_grades()}\n")
    f.write(f"Average: {gb.average():.2f}\n")