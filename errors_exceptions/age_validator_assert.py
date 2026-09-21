ages = [25, -5, "twenty", 200, 45, 0, 120]

passed_count= 0
failed_count= 0
failures= []

for age in ages:
  try:
    assert isinstance(age, int), f"Age must be an interger, got {type(age).__name__}"
    assert 0<= age <=120, f"Age must be between 0 and 120, got {age}"

    print(f"Age {age} passed validation.")
    passed_count+=1

  except AssertionError as e:
    print(f"Age {age} failed validation: {e}")
    failed_count+=1
    failures.append((age, str(e)))

print("\n--- Validation Summary ---")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
if failures:
  print("Failures detail:")
  for age, reason in failures:
    print(f"Age {age}: {reason}")