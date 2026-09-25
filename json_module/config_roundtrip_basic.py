import json

settings= {"app_name": "InventoryApp", 
          "version": 2, 
          "debug_mode": False, 
          "max_users": 100}

settingsJSON= json.dumps(settings, indent= 4, sort_keys= True)
print(settingsJSON)

print(f"\nData type of 'settings': {type(settings)}\nData type of 'settingsJSON': {type(settingsJSON)}")

settingsDict= json.loads(settingsJSON)
print(settingsDict)
print(f"Data type of 'settingsDict': {type(settingsDict)}")

settings["allowed_roles"]= ["admin",
                            "editor",
                            "viewer"]

settingsJSON_nested= json.dumps(settings, indent= 4, sort_keys= True)

print(f"\nData type of 'settings': {type(settings)}")
print(f"Data type of 'settingsJSON_nested': {type(settingsJSON_nested)}")

settingsDict_nested = json.loads(settingsJSON_nested)
print(settingsDict_nested)
print(f"Data type of 'settingsDict_nested': {type(settingsDict_nested)}")