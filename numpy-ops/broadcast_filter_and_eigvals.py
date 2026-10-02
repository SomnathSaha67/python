import numpy as np

arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print(f"Original array:\n{arr}")

print(f"\nArray + 10:\n{arr+10}")

print(f"\nArray % 3:\n{arr%3}")

mask = arr > 15
print(f"\nBoolean mask (arr > 15):\n{mask}")
print(f"Filtered elements (arr[arr > 15]):\n{arr[mask]}")

exp_result = np.exp(arr[0])
print(f"\nExponential of first row:\n{exp_result}")
print(f"Rounded to 3 decimals:\n{np.round(exp_result, 3)}")

small = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])

eigvals = np.linalg.eigvals(small)
print(f"Eigenvalues of 3X3 array:\n{eigvals}")