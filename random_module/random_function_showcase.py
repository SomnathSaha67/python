import random

print(f"random.random(): {random.random()}") # float in [0.0, 1.0)
print(f"random.uniform(10, 20): {random.uniform(10, 20)}") # float in [10, 20]
print(f"random.randint(1, 6): {random.randint(1, 6)}") # integer 1-6 (dice roll)
print(f"random.randrange(0, 100, 5): {random.randrange(0, 100, 5)}") # multiples of 5

print("\nrandom.normalvariate(50, 10):")
for i in range(5):
  print(f"Value {i+1}: {random.normalvariate(50, 10)}")

# normalvariate(mean= 50, stddev= 10) generates numbers with a bell-curve distribution
# most results fall close to mean (50), unlike randint which spreads evenly

print("\nRreproducibility demo with random.seed(42):")

random.seed(42)
first_run= [random.randint(1, 100) for _ in range(5)]
print(f"First run: {first_run}")

random.seed(42)
second_run= [random.randint(1, 100) for _ in range(5)]
print(f"Second run: {second_run}")

print(f"Identical? {first_run==second_run}")