import random

deck= [f"Card{i}" for i in range(1, 11)]
print(f"Original deck: {deck}")

random.shuffle(deck)
print(f"Deck after shuffle: {deck}")

deck1= [f"Card{i}" for i in range(1, 11)]
deck2= [f"Card{i}" for i in range(1, 11)]

random.seed(42)
random.shuffle(deck1)

random.seed(42)
random.shuffle(deck2)

print(f"\nDeck1 after shuffle with seed 42: {deck1}")
print(f"Deck2 after shuffle with seed 42: {deck2}")
print(f"Identical? {deck1==deck2}")