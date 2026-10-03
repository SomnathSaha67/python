import numpy as np

arr_rand = np.random.rand(1000)  # uniform [0, 1)
arr_randn = np.random.randn(1000)  # normal (mean=0, std=1)

print("Uniform rand() stats:")
print(f"Mean: {arr_rand.mean()}")
print(f"Std: {arr_rand.std()}")
print(f"Min: {arr_rand.min()}")
print(f"Max: {arr_rand.max()}")

print("\nNormal randn() stats:")
print(f"Mean: {arr_randn.mean()}")
print(f"Std: {arr_randn.std()}")
print(f"Min: {arr_randn.min()}")
print(f"Max: {arr_randn.max()}")

count_rand = (arr_rand > 0.8).sum()
count_randn = (arr_randn > 1).sum()

print(f"\nCount > 0.8 in rand(): {count_rand}")
print(f"Count > 1 in randn(): {count_randn}")