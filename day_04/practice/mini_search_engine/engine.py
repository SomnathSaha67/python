word= input("Enter the word whose sentences to be printed: ")
file_open= open('articles.txt', 'r')
for sentence in file_open:
  if sentence[-1]=="\n":
    if word in sentence:
      print(sentence[:-1])
    else:
      continue
  else:
    if word in sentence:
      print(sentence)
    else:
      continue