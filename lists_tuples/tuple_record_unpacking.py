employees = [("Alice", 29, ("Engineering", "Senior")), 
             ("Bob", 24, ("Sales", "Junior")), 
             ("Carol", 35, ("Engineering", "Lead")),]

for emp in employees:
  
  name, age, (dept, role)= emp
  print(f"{name} | Age: {age} | Dept: {dept} | Role: {role}")

  if ((age>=30) and role in ("Senior", "Lead")): tier= "High seniority"
  elif (role=="Lead"): tier= "Leadership"
  elif ((age<25) and role=="Junior"): tier= "Entry-level"
  elif (age>=40): tier= "Veteran"
  else: tier= "Other"

  print(f"Tier: {tier}")
  print("---")