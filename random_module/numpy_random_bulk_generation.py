import random, numpy as np

# 4x3 array of random floats
arr= np.random.rand(4, 3)
print(f"Random 4x3 array:\n{arr}")
print(f"Shape: {arr.shape}")

# 10 random integers at once
ints= np.random.randint(1, 100, size= 10)
print(f"\n10 random integers: {ints}")

# Reproducibility with numpy.random.seed
np.random.seed(7)
arr1= np.random.rand(2, 5)

np.random.seed(7)
arr2= np.random.rand(2, 5)

print(f"\nArray 1:\n{arr1}")
print(f"Array 2:\n{arr2}")
print(f"Identical? {np.array_equal(arr1, arr2)}")

# random and numpy.random seeds are independent
random.seed(7)
print(f"\nrandom.random(): {random.random()}")

print(f"numpy.random.rand(): {np.random.rand()}")

nums= np.array([1, 2, 3, 4, 5])
print(f"\nBefore shuffle: {nums}")
np.random.shuffle(nums) # in-place shuffle
print(f"After shuffle {nums}")