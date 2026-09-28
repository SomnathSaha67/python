def create_user(name, age, city):
  return f"User: {name}, Age: {age}, City: {city}"

user_list= ["Alice", 30, "New York"]
user_tuple= ("Bob", 25, "London")
user_dict= {"name": "Charlie", "age": 40, "city": "Paris"}

print(create_user(*user_list))
print(create_user(*user_tuple))
print(create_user(**user_dict))

def merge_settings(**defaults):
  return defaults

base= {"theme": "light", "language": "en", "timeout": 30}
override= {"language": "fr", "timeout": 60}

merged= merge_settings(**{**base, **override})
print(f"Merged settings: {merged}")