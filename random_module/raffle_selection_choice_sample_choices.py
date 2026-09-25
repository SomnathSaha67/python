import random

participants = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace"]

grand_prize= random.choice(participants)
print(f"Grand Prize Winner: {grand_prize}")

runner_ups= random.sample(participants, 3)   # 3 distinct, no duplicates
print(f"Runner-up Winners: {runner_ups}")
print(f"No duplicates? {len(runner_ups)==len(set(runner_ups))}")

raffle_draws= random.choices(participants, k= 5)
print(f"Raffle Draws (with replacement): {raffle_draws}")

if len(raffle_draws) != len(set(raffle_draws)):
  print("Note: Some names repeated, because replacement allows it.")

weights= [1, 1, 1, 1, 1, 1, 10]
for i in range(3):
  weighted_draws= random.choices(participants, weights= weights, k= 5)
  print(f"Weighted Draw {i+1}: {weighted_draws}")