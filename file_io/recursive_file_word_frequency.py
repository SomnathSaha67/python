notes_content = """python is fun and python is powerful
recursion in python takes practice
practice makes python easier over time"""

with open("notes.txt", "w") as f:
  f.write(notes_content)

with open("notes.txt", "r") as f:
  text= f.read()

words= text.lower().split()

def count_words(word_list, freq_dict):

  if not word_list:
    return freq_dict
  
  current_word= word_list[0]
  if current_word in freq_dict:
    freq_dict[current_word]+=1
  else:
    freq_dict[current_word]=1

  return count_words(word_list[1:], freq_dict)

freq_dict= count_words(words, {})

most_frequent_word= max(freq_dict, key= freq_dict.get)
highest_count= freq_dict[most_frequent_word]

with open("word_frequency_report.txt", "w") as f:
  f.write("Word Frequency Report\n")
  f.write("---------------------\n")
  for word, count in freq_dict.items():
    f.write(f"{word}: {count}\n")
  f.write("\n")
  f.write(f"Most frequent word: '{most_frequent_word}' (Count: {highest_count})")

print(f"Report written. Most frequent word: '{most_frequent_word}' ({highest_count} times)")