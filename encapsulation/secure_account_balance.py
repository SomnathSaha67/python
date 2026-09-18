class SecureAccount:

  def __init__(self, owner_name, starting_balance):
    self.owner_name= owner_name
    self.__balance= starting_balance
  
  def get_balance(self):
    return self.__balance
  
  @staticmethod
  def _validate_amount(amount):
    return amount>0
  
  def deposit(self, amount):
    if self._validate_amount(amount):
      self.__balance+=amount
      return f"Deposit successful. Updated balance: ${self.__balance}"
    else:
      return "Deposit failed. Amount must be positive."
  
  def withdraw(self, amount):
    if self._validate_amount(amount):
      if amount>self.__balance:
        return f"Insufficient balance. Balance: ${self.__balance}"
      else:
        self.__balance-=amount
        return f"Withdraw successful. Updated balance: ${self.__balance}"
    else:
      return "Withdraw failed. Amount must be positive."
    
account = SecureAccount("Alice", 1000)
print(account.get_balance())     
print(account.deposit(500))        
print(account.withdraw(200))       