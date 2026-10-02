import numpy as np

with open("data_sample.csv", "w") as f:
    f.write("A,B,C,D\n")  
    f.write("1,2,3,4\n")
    f.write("5,6,7,8\n")
    f.write("9,10,11,12\n")

data = np.genfromtxt("data_sample.csv", delimiter=",", skip_header=1)
print(f"Loaded data:\n{data}")

reshaped = data.reshape(3, 4)
print(f"\nReshaped array (3x4):\n{reshaped}")

new_row = np.array([[13, 14, 15, 16]])
combined = np.concatenate((reshaped, new_row), axis=0)
print(f"\nCombined array fter stacking new row:\n{combined}")

np.savetxt("data_final.csv", combined, delimiter=",", fmt="%.2f", header="A,B,C,D", comments="")