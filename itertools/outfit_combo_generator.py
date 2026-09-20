from itertools import product

shirts= ["Red", "Blue"]
pants= ["Black", "Khaki"]

comb= list(product(shirts, pants))
print(f"All shirt-pant combinations: {comb}")

for shirt, pant in comb:
  print(f"{shirt} shirt with {pant} pants")

shoes= ["Sneakers", "Boots", "Sandals"]

comb3= list(product(shirts, pants, shoes))
print("\nAll shirt-pant-shoe combinations:")
for shirt, pant, shoe in comb3:
  print(f"{shirt} shirt with {pant} pants and {shoe}")

print(f"\nTotal 3-way combinations: {len(comb3)}")
print(f"Manual check: {len(shirts) * len(pants) * len(shoes)}")