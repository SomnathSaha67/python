def add_tag(tag, tags= []):
  tags.append(tag)
  return tags

print(add_tag("alpha"))
print(add_tag("beta"))
print(add_tag("gamma"))

def add_tag(tag, tags= None):
  if tags is None:
    tags= []
  tags.append(tag)
  return tags

print(add_tag("alpha"))
print(add_tag("beta"))
print(add_tag("gamma"))


def build_config(name, *features, debug= False, **extra):
  return{
    "name": name,
    "features": features,
    "debug": debug,
    "extra": extra
  }

feature_list= ["logging", "auth"]
extra_dict= {"version": "1.0", "author": "somnath"}

config1= build_config("App1", *feature_list, **extra_dict)
print(f"Config1: {config1}")

config2 = build_config("App2", *feature_list, debug=True, **extra_dict)
print("Config2:", config2)