d1= {"a": 1,
     "b": 2}

d2= d1

d3= {"a": 1,
     "b": 2}

print(f"d1==d3: {d1==d3}")
print(f"d1 is d3: {d1 is d3}")
print(f"d1 is d2: {d1 is d2}")

d2["b"]= 99
print(f"After modifying d2: {d1}")

# --- Sets ---

s1 = {"x", "y"}
s2 = s1
s3 = {"x", "y"}

print("s1 == s3:", s1 == s3)   
print("s1 is s3:", s1 is s3)  
print("s1 is s2:", s1 is s2)   

s2.add("z")
print("After modifying s2:", s1) 