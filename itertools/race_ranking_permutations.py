from itertools import permutations, combinations

runners= ["ALice", "Bob", "Carol", "Dave"]

podiums= list(permutations(runners, 3))

print("All possible podium orderings:")
for first, second, third in podiums:
  print(f"1st: {first}, 2nd: {second}, 3rd: {third}")

print(f"\nTotal podium orderings: {len(podiums)}")
print(f"Manual check (4 x 3 x 2): {4 * 3 * 2}")

combos= list(combinations(runners, 3))

print("\nAll possible 3-runner combinations:")
for group in combos:
  print(group)

print(f"\nTotal combinations: {len(combos)}")