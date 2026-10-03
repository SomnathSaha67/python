import numpy as np

arr = np.arange(25).reshape(5, 5)
print(f"Original Array:\n{arr}")

print(f"\nSingle element [2, 3]: {arr[2, 3]}")

print(f"\nFull row [1]: {arr[1]}")

print(f"\nFull column [4]: {arr[:,4]}")

print(f"\n2x2 block (top-left corner):\n{arr[0:2, 0:2]}")

print(f"\n2x2 block (middle):\n{arr[1:3, 1:3]}")

print(f"\nEvery other row:\n{arr[::2]}")