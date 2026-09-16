def strip_whitespace(s):
  
  return s.strip()

def is_valid_name(s):
  
  if s=="":
    return False
  
  if any(ch.isdigit() for ch in s):
    return False
  
  return True

def normalize_case(s):

  return s.title()

raw_entries = [" Alice ", "BOB", "", " charlie", "Dave123", " "]
valid_names= []
rejected_entries= []

for entry in raw_entries:

  stripped= strip_whitespace(entry)

  if not is_valid_name(stripped):
    reason= "Empty after stripping" if stripped=="" else "Contains digits"
    rejected_entries.append((entry, reason))
    continue

  normalized= normalize_case(stripped)
  valid_names.append(normalized)

print("\nReport")
print(f"Valid Names ({len(valid_names)}): {valid_names}")
print(f"Rejected Entries ({len(rejected_entries)}):")

for original, reason in rejected_entries:
  print(f"  {original!r} -> {reason}")