from collections import defaultdict

sentence= "python is fun and python is powerful and python is easy"
words= sentence.split()

freq= defaultdict(int)
for w in words:
  freq[w]+=1

groups= defaultdict(list)
for w in words:
  groups[w[0]].append(w)

print("Word frequency dictionary:")
for word, count in freq.items():
  print(f"{word}: {count}")

print("\nGrouped by first letter:")
for letter, word_list in groups.items():
  print(f"{letter}: {word_list}")