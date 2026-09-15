raw = [4, 7, 4, 2, 7, 9, 2, 4, 1]
print(f"Duplicated original list: {raw}")

dedup= []

for ele in raw:
  if ele not in dedup: dedup.append(ele)

print(f"Deduplicated list: {dedup}")