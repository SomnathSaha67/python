import json, logging

logging.basicConfig(level= logging.INFO, format= "%(levelname)s - %(message)s")

valid_json_str= '{"id": 1, "name": "Alice", "active": true}'
corrupted_json_str= '{"id": 2, "name": "Bob", "active": false'

valid_records= []

for label, js in [("Valid JSON", valid_json_str), ("Corrupted JSON", corrupted_json_str)]:
  try:
    record= json.loads(js)
    logging.info(f"{label} parsed successfully.")

    print(f"Record name: {record.get('name')}, Active: {record.get('active')}")
    valid_records.append(record)
  except json.JSONDecodeError as e:
    logging.error(f"{label} failed to parse: {e}")
    print(f"Error parsing {label}: {e}")

with open("valid_records.json", "w") as f:
  json.dump(valid_records, f, indent= 4)

print("\nSuccessfully parsed records saved to valid_records.json")