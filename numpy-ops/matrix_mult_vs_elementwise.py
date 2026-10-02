import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([[7, 8],
                 [9, 10],
                 [11, 12]])

matmul_result = arr1 @ arr2
print("Matrix multiplication result (arr1 @ arr2):")
print(matmul_result)
print(f"Shape: {matmul_result.shape}")

try:
  arr1 * arr2
except ValueError as e:
  print(f"\nError caught during arr1 * arr2: {e}")

arr3 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr4 = np.array([[6, 5, 4],
                 [3, 2, 1]])

print(f"\nElement-wise multiplication result (arr3 * arr4):")
print(arr3 * arr4)