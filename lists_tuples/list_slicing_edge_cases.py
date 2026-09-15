nums = [5, 12, 8, 19, 3, 27, 6, 14]

print(f"Original list: {nums}")

print(nums[1:3])

print(nums[-2:])

print(nums[::-1])

print(nums[3:20])

print(nums[20:25]) #[]

print(nums[5:2])  #[]

print(nums[3:])

print(nums[:3])

print(nums[0::2])

print(nums[5:2:-1])

slice_obj= nums[1:3]
print(f"Slice: {slice_obj} | Type: {type(slice_obj)} | id: {id(slice_obj)}")

element_obj= nums[1]
print(f"Element: {element_obj} | Type: {type(element_obj)} | id: {id(element_obj)}")