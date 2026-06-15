def main():
  total_sentences, total_characters, longest_sentence, shortest_sentence= 0, 0, "", ""
  while True:
    text= input("Enter text('n' to stop): ")
    if text=='n':
      extract_statistics(total_sentences, total_characters, longest_sentence, shortest_sentence)
      break
    else:
      cleaned_text= clean_text(text)
      normalized_text= normalize_text(cleaned_text)
      total_sentences+=1
      for char in normalized_text:
        total_characters+=1
      if len(longest_sentence)<len(text):
        longest_sentence= text
      else:
        shortest_sentence=text
        if len(shortest_sentence)>len(text):
          shortest_sentence= text
def clean_text(text):
  if any(c in "@#$%^*" for c in text):
    return text.strip().replace(any, "")
  else:
    return text.strip()
def normalize_text(cleaned_text):
  return cleaned_text.lower()
def extract_statistics(total_sentences, total_characters, longest_sentence, shortest_sentence):
  print(f"Total Sentences: {total_sentences}")
  print(f"Total Characters: {total_characters}")
  print(f"Longest Sentence: {longest_sentence}")
  print(f"Shortest Sentence: {shortest_sentence}")
  print(f"Average Length: {(round(total_characters/total_sentences, 2))}")
if __name__=="__main__":
  main()