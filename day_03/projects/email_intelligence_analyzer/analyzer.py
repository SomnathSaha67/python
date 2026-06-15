def main():
  total_emails, valid_emails, invalid_emails, gmail_domain, yahoo_domain, longest_email, shortest_email= 0, 0, 0, 0, 0, "", ""
  while True:
    email= input("Enter email('n' to stop): ")
    if email=='n':
      break
    else:
      valid_email, domain= validate_email(email)
      total_emails+=1
      if valid_email:
        valid_emails+=1
        if len(longest_email)<len(email):
          longest_email=email
        else:
          shortest_email= email
          if len(shortest_email)>len(email):
            shortest_email=email
        if domain in "gmail.com":
          gmail_domain+=1
        if domain in "yahoo.com":
          yahoo_domain+=1
        max_domain= max(gmail_domain, yahoo_domain)
      else:
        invalid_emails+=1
  if gmail_domain==max_domain==yahoo_domain:
    common_domain= "gmail.com and yahoo.com"
  elif gmail_domain==max_domain:
    common_domain= "gmail.com"
  else:
    common_domain= "yahoo.com"
  print(f"Total Emails: {total_emails}")
  print(f"Valid Emails: {valid_emails}")
  print(f"Invalid Emails: {invalid_emails}")
  print(f"Most Common Domain: {common_domain}")
  print(f"Longest Email: {longest_email}")
  print(f"Shortest Email: {shortest_email}")
def validate_email(email):
  if "@" in email and "." in email and not (" " in email):
    return True, email[(email.find("@"))+1:]
  else:
    return False, 0
if __name__=="__main__":
  main()