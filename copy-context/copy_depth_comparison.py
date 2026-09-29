import copy

matrix= [[1, 2, 3], [4, 5, 6]]

shallow= copy.copy(matrix)
shallow[0][0]= 999

print("After shallow mutation:")
print(f"matrix: {matrix}")
print(f"shallow: {shallow}")

matrix= [[1, 2, 3], [4, 5, 6]]
deep= copy.deepcopy(matrix)
deep[0][0]= 999

print("\nAfter deep mutation:")
print(f"matrix: {matrix}")
print(f"deep: {deep}")

flat = [1, 2, 3, 4, 5]

shallow_flat = copy.copy(flat)
shallow_flat[0] = 999 


print("\nFlat list shallow mutation:")
print("flat:", flat)          
print("shallow_flat:", shallow_flat)

flat = [1, 2, 3, 4, 5]
deep_flat = copy.deepcopy(flat)
deep_flat[0] = 999

print("\nFlat list deep mutation:")
print("flat:", flat)           
print("deep_flat:", deep_flat)