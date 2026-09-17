def flatten(d, prefix=""):

  flat= {}

  for key, value in d.items():
    new_key= f"{prefix}.{key}" if prefix else key

    if isinstance(value, dict):
      flat.update(flatten(value, new_key))
    else:
      flat[new_key]= value

  return flat

config = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}, "g": 5}

flattened= flatten(config)
print(flattened)