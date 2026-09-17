csv_content = """name,department,salary,years
Alice,Engineering,95000,4
Bob,Sales,62000,1
Carol,Engineering,110000,7
Dave,Marketing,58000,0"""

with open("employees.csv", 'w') as f:
  f.write(csv_content)

employees= []

with open("employees.csv", 'r') as f:
  lines= f.readlines()
  for index, line in enumerate(lines):
    if index==0:
      continue

    parts= line.strip().split(",")
    if len(parts)==4:
      name= parts[0]
      department= parts[1]
      salary= int(parts[2])
      years= int(parts[3])
      employees.append((name, department, salary, years))

total_payroll=0
eng_salary_total=0
eng_count=0
new_hires=[]

for name, dept, salary, years in employees:
  total_payroll+=salary

  if dept=="Engineering":
    eng_salary_total+=salary
    eng_count+=1

  if years==0:
    new_hires.append(name)

avg_eng_salary= eng_salary_total/eng_count if eng_count>0 else 0

summary_text= f"""Employee Summary Report
-----------------------
Total Payroll: ${total_payroll}
Average Engineering Salary: ${avg_eng_salary:.2f}
New Hires (0 years): {', '.join(new_hires)}
"""

with open("employee_summary.txt", "w") as f:
  f.write(summary_text)

print(summary_text)