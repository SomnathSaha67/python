import numpy as np

scores = np.array([
    [85, 90, 78],  
    [88, 76, 92],   
    [90, 85, 85],   
    [70, 95, 80]    
])

print(f"Original scores array:\n{scores}")

print("\nWhole array statistics:")
print(f"Mean: {scores.mean()}")
print(f"Median: {np.median(scores)}")
print(f"Std Dev: {scores.std()}")
print(f"Max: {scores.max()}")

print("\nPer-subject statistics (axis=0):")
print(f"Mean: {scores.mean(axis=0)}")
print(f"Median: {np.median(scores,axis=0)}")
print(f"Std Dev: {scores.std(axis=0)}")
print(f"Max: {scores.max(axis=0)}")

print(f"\nPer-student statistics (axis=1):")
print(f"Mean: {scores.mean(axis=1)}")
print(f"Median: {np.median(scores,axis=1)}")
print(f"Std Dev: {scores.std(axis=1)}")
print(f"Max: {scores.max(axis=1)}")

scores_T= scores.transpose()
print(f"\nTransposed array:\n{scores_T}")

print(f"Mean (axis=0 on transposed): {scores_T.mean(axis=0)}")
print(f"Matches original axis=1 mean: {np.allclose(scores_T.mean(axis=0), scores.mean(axis=1))}")