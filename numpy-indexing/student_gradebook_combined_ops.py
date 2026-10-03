import numpy as np

arr = np.zeros((6, 4))
print(f"Placeholder array:\n{arr}")

scores = (np.random.rand(6, 4) * 100).round(2)
print(f"\nRandom scores array:\n{scores}")

print(f"\nFirst 3 students' records:\n{scores[0:3]}")
print(f"\nLast subject column (all students):\n{scores[:,-1]}")
print(f"\nSingle student's full row (student index 2):\n{scores[2]}")

student_avg = scores.mean(axis=1)
subject_avg = scores.mean(axis=0)

print(f"\nEach student's average: {student_avg}")
print(f"Each subject's average: {subject_avg}")

mask = student_avg > 75
print(f"\nList of students with avg > 75: {mask}")
print(f"Indices of students above 75: {np.where(mask)[0]}")
print(f"Scores of those students:\n{scores[mask]}")