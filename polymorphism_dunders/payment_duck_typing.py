class CreditCardPayment:

  def process(self, amount):
    print(f"Processing credit card payment of ${amount}")

class UpiPayment:

  def process(self, amount):
    print(f"Processing UPI payment of ${amount}")

class CashPayment:

  def pay(self, amount):
    print(f"Paying cash of ${amount}")

payments= [
  CreditCardPayment(),
  UpiPayment(),
  CashPayment()
]

for p in payments:
  if hasattr(p, "process"):
    p.process(500)
  else:
    print(f"{p.__class__.__name__} skipped (no process method)")