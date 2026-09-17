def permutations(s):
  if len(s)==1:
    return [s]
  
  result= []

  for i, ch in enumerate(s):
    remaining= s[:i]+s[i+1:]
    for perm in permutations(remaining):
      result.append(ch+perm)

  return result

word= "cat"
perms= permutations(word)

print(f"All permutations: {perms}")

unique_perms= set(perms)
print(f"Unique permutations: {unique_perms}")
print(f"Count: {len(unique_perms)}")