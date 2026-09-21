from functools import reduce

scores = [("Alice", 82), ("Bob", 45), ("Carol", 91), ("Dave", 38), ("Eve", 67), ("Frank", 95)]

passed= list(filter(lambda stud: stud[1]>=50, scores))

passed_sorted= sorted(passed, key= lambda stud: stud[1], reverse= True)

formatted= list(map(lambda stud: f"{stud[0]}: {stud[1]}", passed_sorted))

report= reduce(lambda acc, s: acc+"\n"+s, formatted)

print(f"Final Combined Report:\n{report}")