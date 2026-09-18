class UserCredential:

  def __init__(self, username, password):
    self.username= username
    if self._meets_requirements(password):
      self.__password= password
    else:
      self.__password= "DEFAULT123"
      print(f"Warning: Password for {username} is too weak. Using default placeholder.")

  def check_password(self, attempt):
    return self.__password==attempt
  
  def _meets_requirements(self, password):
    if len(password)<6:
      return False
    if not any(ch.isdigit() for ch in password):
      return False
    return True
  
user1 = UserCredential("Alice", "Secure123")   
user2 = UserCredential("Bob", "weak") 

print(user1.check_password("Secure123"))
print(user1.check_password("WrongPass"))

print(user2.check_password("weak"))
print(user2.check_password("DEFAULT123"))