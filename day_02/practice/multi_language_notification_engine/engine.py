def main():
  while True:
    name, language= map(str, input("Enter name and language with spaces('STOP' to stop): ").split(" "))
    if name=='STOP' or language=='STOP':
      break
    greeting= notify(language) 
    if greeting is None:
      print("Unsupported Language")
    else:
      print(f"{greeting}, {name.title()}")
def notify(lang):
  if lang in ['en', 'es', 'fr', 'de']:
    if lang=='en':
      return "Welcome"
    elif lang=='es':
      return "Bienvenido"
    elif lang=='fr':
      return "Bonjour"
    else:
      return "Willkommen"
  else:
    return None
if __name__=="__main__":
  main()