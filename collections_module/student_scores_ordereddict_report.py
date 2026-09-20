from collections import OrderedDict

scores = OrderedDict([
    ("Dave", 72),
    ("Alice", 91),
    ("Bob", 85),
    ("Carol", 78)
])

print("Before move_to_end:")
print(scores)

scores.move_to_end("Dave")

print("\nAfter move_to_end:")
print(scores)

scores_alt= OrderedDict([
  ("Dave", 72),
  ("Alice", 91),
  ("Bob", 85),
  ("Carol", 78)
])

print("\nSecond OrderedDict (different order): ")
print(scores_alt)

print(f"\nAre the two OrderedDicts equal? {scores==scores_alt}")

plain1= {"Dave": 72, "Alice": 91, "Bob": 85, "Carol": 78}
plain2= {"Alice": 91, "Bob": 85, "Carol": 78, "Dave": 72}

print(f"Are the two plain dicts equal? {plain1==plain2}")