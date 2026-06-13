activities = [
    5,
    12,
    8,
    20,
    7,
    15
]
total_activities, sum, above_avg_activity, highest_activity, lowest_activity=0, 0, 0, -float('inf'), float('inf')
for activity in activities:
  total_activities+=1
  sum+=activity
  if highest_activity<activity:
    highest_activity= activity
  if lowest_activity>activity:
    lowest_activity= activity 
average_activity= round(sum/total_activities, 2)
for activity in activities:
  if activity>average_activity:
    above_avg_activity+=1
print(f"Total Activities: {total_activities}")
print(f"Average Activity: {average_activity}")
print(f"Highest Activity: {highest_activity}")
print(f"Lowest Activity: {lowest_activity}")
print(f"Activities Above Average: {above_avg_activity}")