transaction = "2026-09-05,freelance,15000,INR".split(",")
print(f"On {transaction[0]}: earned {float(transaction[2])} {transaction[-1]} from {transaction[1].upper()}")