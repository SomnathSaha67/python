class OutOfRangeError(Exception):
  pass

raw_data= ["45", "82", "abc", "-12", "", "99", "1000"]

valid_numbers= []
rejected_entries= []

for entry in raw_data:
  try:
    num= int(entry)

    assert num>=0, f"Negative value not allowed: {num}"

    if num>300:
      raise OutOfRangeError(f"Value {num} exceeds maximum allowed (500).")
    
    valid_numbers.append(num)

  except ValueError as e:
    reason= f"Conversion failed: {e}"
    rejected_entries.append((entry, reason))
    print(f"Entry '{entry}' failed (ValueError): {reason}")

  except AssertionError as e:
    reason= str(e)
    rejected_entries.append((entry, reason))
    print(f"Entry '{entry}' failed (AssertionError): {reason}")

  except OutOfRangeError as e:
    reason= str(e)
    rejected_entries.append((entry, reason))
    print(f"Entry '{entry}' failed (OutOfRangeError): {reason}")

  finally:
    print(f"Processed entry: {entry}\n")

print("=== Final Report ===")
print(f"Valid numbers: {valid_numbers}")
print("\nRejected entries:")
for entry, reason in rejected_entries:
  print(f"'{entry}' -> {reason}")