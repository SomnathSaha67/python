import numpy as np

arr_arange = np.arange(0, 20, 4)
print(f"arange(0, 20, 4): {arr_arange}")
print(f"Count of numbers: {len(arr_arange)}")

arr_linspace = np.linspace(0, 20, 6)
print(f"\nlinspace(0, 20, 6): {arr_linspace}")
print(f"Step size (auto): {arr_linspace[1] - arr_linspace[0]}")

arr_match1 = np.arange(0, 21, 5)
arr_match2 = np.linspace(0, 20, 5)

print("\nMatching arrays with arange and linspace:")
print(f"arange: {arr_match1}")
print(f"linspace: {arr_match2}")
print(f"Are they identical? {np.array_equal(arr_match1, arr_match2)}")