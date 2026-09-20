from itertools import combinations

players = ["Alice", "Bob", "Carol", "Dave", "Eve"]

teams2= list(combinations(players, 2))
print("All 2-person teams:")
for team in teams2:
  print(team)

print("\nConfirming (Alice, Bob) only appears once:")
print(("Alice", "Bob") in teams2)
print(("Bob", "Alice") in teams2)

teams3= list(combinations(players, 3))
print("\nAll 3-person teams that include Alice:")
for team in teams3:
  if "Alice" in team:
    print(team)

print(f"\nTotal 2-person teams: {len(teams2)}")
print(f"Total 3-person teams: {len(teams3)}")