import numpy as np
asset_values= np.array([150000, 80000, 45000, 25000])
total_asset= asset_values.sum()
weights= asset_values/total_asset
print("Weights:",np.round(weights, 3))
largest_index= np.argmax(asset_values)
print("Largest Holding Index:", largest_index)
print("Largest Holding Value:", asset_values[largest_index])
print("Largest Holding Weight: ", round(weights[largest_index], 3))

np.random.seed(42)
expected_returns= np.random.normal(0.06, 0.015, 4)
print("Expectd Returns:",np.round(expected_returns, 4))