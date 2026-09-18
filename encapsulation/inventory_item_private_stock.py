class InventoryItem:

  def __init__(self, name, stock):
    self.name= name
    self.__stock= stock
  
  def _check_amount(self, amount):
    return amount>0
  
  def restock(self, amount):
    if self._check_amount(amount):
      self.__stock+=amount
      print(f"{self.name}: Restocked {amount}. New stock= {self.__stock}")
    else: 
      print(f"{self.name}: Invalid restock amount {amount}. Ignored.")

  def sell(self, amount):
    if not self._check_amount(amount):
      print(f"{self.name}: Invalid sell amount {amount}. Ignored.")
      return
    if amount>self.__stock:
      print(f"{self.name}: Cannot sell {amount}. Only {self.__stock} in stock.")
    else:
      self.__stock-=amount
      print(f"{self.name}: Sold {amount}. New stock = {self.__stock}")
  
  def get_stock(self):
    return self.__stock
  
items = [
    InventoryItem("Widget", 10),
    InventoryItem("Gadget", 5),
    InventoryItem("Gizmo", 0)
]

items[0].restock(5)      
items[0].sell(3)          
items[0].sell(20)         

items[1].restock(-2)      
items[1].sell(2)         
items[1].sell(0)         

items[2].sell(1)          
items[2].restock(4)       
items[2].sell(2)          

print("\nFinal Inventory Report:")
for item in items:
    print(f"{item.name}: {item.get_stock()} in stock")