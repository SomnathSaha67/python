class BankAccount:

  def __init__(self, owner_name, starting_balance):
    self.owner_name= owner_name
    self.balance= starting_balance

  def deposit(self, amount):
    if amount<=0:
      print("Invalid amount")
    else: 
      self.balance+=amount 
      print(f"Deposit successful. Updated balance: ${self.balance}")
  
  def withdraw(self, amount):
    if amount<=0: print("Invalid amount")
    elif amount>self.balance: print(f"Insufficient balance: ${self.balance}")
    else:
      self.balance-=amount 
      print(f"Withdraw successful.\nUpdated balance: ${self.balance}")

  def show_balance(self):
    print(f"{self.owner_name}'s balance: ${self.balance}")

a1= BankAccount("Somnath Karuj", 5000)
a1.show_balance()
a1.deposit(5000)
a1.withdraw(3000)
a1.show_balance()

a2= BankAccount("Alice", 2000)
a2.show_balance()
a2.deposit(1000)
a2.withdraw(500)
a2.show_balance()