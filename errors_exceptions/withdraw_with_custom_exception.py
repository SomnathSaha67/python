class InsufficientFundsError(Exception):
  pass

class BankAccount:
  def __init__(self, owner_name, balance):
    self.owner_name= owner_name
    self.balance= balance

  def withdraw(self, amount):
    if amount<=0:
      raise ValueError("Withdrawal amount must be positive.")
    if amount>self.balance:
      raise InsufficientFundsError(
        f"Insufficient funds: tried to withdraw {amount}, "
        f"but balance is {self.balance}."
      )
    self.balance-=amount
    print(f"Withdrawal successful. New balance: {self.balance}")

account= BankAccount("Suresh", 1000)

try:
  account.withdraw(200)
except ValueError as ve:
  print(f"ValueError caught: {ve}")
except InsufficientFundsError as ife:
  print(f"InsufficientFundsError caught: {ife}")
finally:
  print("Transaction attempt complete.\n")

try:
  account.withdraw(-50)
except ValueError as ve:
    print("ValueError caught:", ve)
except InsufficientFundsError as ife:
    print("InsufficientFundsError caught:", ife)
finally:
    print("Transaction attempt complete.\n")

try:
    account.withdraw(2000)
except ValueError as ve:
    print("ValueError caught:", ve)
except InsufficientFundsError as ife:
    print("InsufficientFundsError caught:", ife)
finally:
    print("Transaction attempt complete.\n")