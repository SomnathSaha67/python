import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([6, 5, 4, 3, 2, 1])

print("Element-wise result (arr1 *arr2):")
print(arr1 * arr2)

dot1 = np.dot(arr1, arr2)

dot2 = (arr1 * arr2).sum()

print(f"\nDot product using np.dot(): {dot1}")
print(f"Dot product using (arr1 * arr2).sum(): {dot2}")
print(f"Do both match? {dot1 == dot2}")

arr3 = np.array([1, 2, 3])

try:
  np.dot(arr1, arr3)
except ValueError as e:
  print(f"\nError caught: {e}")