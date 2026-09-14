s= "Google"
print(f"Original: {s} | id: {id(s)}")

sliced= s[:3]+s[3:].upper()
print(f"Sliced: {sliced} | id: {id(sliced)}")

#s[0]= "g" #TypeError

concat1 = s + "!"
print("Concat1:", concat1, "| id:", id(concat1))

concat2 = concat1 + "?"
print("Concat2:", concat2, "| id:", id(concat2))

concat3 = concat2 + "#"
print("Concat3:", concat3, "| id:", id(concat3))