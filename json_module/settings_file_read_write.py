import json

settings = {
    "app_name": "InventoryApp",
    "version": 2,
    "debug_mode": False,
    "max_users": 100,
    "preferences": {
        "theme": "dark",
        "notifications": True,
        "refresh_rate": 30
    }
}

with open("settings.json", "w") as f:
  json.dump(settings, f, indent= 4)

with open("settings.json", "r") as f:
  reloaded_settings= json.load(f)

print(f"Match after reload? {settings==reloaded_settings}")

reloaded_settings["preferences"]["theme"]= "light"

with open("settings.json", "w") as f:
  json.dump(reloaded_settings, f, indent= 4)

print("Updated settings save to file.")