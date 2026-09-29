import copy

students = {
    "Alice": {"scores": [88, 92], "active": True},
    "Bob": {"scores": [70, 65], "active": False}
}

shallow= copy.copy(students)
shallow["Alice"]["scores"][0]= 99


print("After shallow mutation:")
print("students:", students)   
print("shallow:", shallow)

students = {
    "Alice": {"scores": [88, 92], "active": True},
    "Bob": {"scores": [70, 65], "active": False}
}

deep= copy.deepcopy(students)
deep["Alice"]["scores"][0]= 99

print("\nAfter deep mutation:")
print("students:", students)  
print("deep:", deep)


def safe_clone(data):
  return copy.deepcopy(data)

clone= safe_clone(students)
clone["Bob"]["scores"][0]= 77

print("\nUsing safe_clone:")
print("students:", students)
print("clone:", clone)