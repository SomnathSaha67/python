import numpy as np

zeros_arr = np.zeros((3, 4))
ones_arr = np.ones((3, 4))
full_arr = np.full((3, 4), 7)

identity = np.eye(4)

rand_arr = np.random.rand(4, 4)

result = identity @ rand_arr

print(f"Zeros array:\n{zeros_arr}")
print(f"\nOnes array:\n{ones_arr}")
print(f"\nFull array (fill=7):\n{full_arr}")
print(f"\nIdentity matrix:\n{identity}")
print(f"\nRandom array:\n{rand_arr}")
print(f"\nIdentity @ Random array:\n{result}")

print("\nShapes:")
print(f"Zeros array shape: {zeros_arr.shape}")
print(f"Ones array shape: {ones_arr.shape}")
print(f"Full array shape: {full_arr.shape}")
print(f"Identity matrix shape: {identity.shape}")
print(f"Random array shape: {rand_arr.shape}")
print(f"Result shape: {result.shape}")