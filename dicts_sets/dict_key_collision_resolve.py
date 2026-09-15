base_config = {"timeout": 30, 
               "retries": 3, 
               "debug": False, 
               "region": "us-east"}

override_config = {"retries": 5, 
                   "debug": "true", 
                   "region": "eu-west", 
                   "cache": True}

merged_config= {}
log= {"overridden": [],
      "newly_added": [],
      "kept": []}

all_keys= set(base_config.keys()) | set(override_config.keys())

for key in all_keys:
  
  if key in base_config and key in override_config:
    value= override_config[key]
  
    if key=="debug":
      if isinstance(base_config[key], bool) and isinstance(value, str):
        if value.lower() in ("true", "1", "yes"):
          value= True
        else:
          value= base_config[key]
  
    merged_config[key]= value
    log["overridden"].append(key)

  elif key in override_config:
    merged_config[key]= override_config[key]
    log["newly_added"].append(key)
  
  else:
    merged_config[key]= base_config[key]
    log["kept"].append(key)

print(f"Final merged config: {merged_config}")
print(f"Log: {log}")