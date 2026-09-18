class Product:

  def __init__(self, name, price):
    self.name= name
    self.price= price

  @classmethod
  def from_string(cls, data_str):
    name, price_str= data_str.split("-")
    price= float(price_str)
    return cls(name, price)
  
  def show_info(self):
    print(f"Product: {self.name}, Price: ${self.price}")

p1= Product("Laptop", 999.99)

p2= Product.from_string("Mouse-24.99")

p1.show_info()
p2.show_info()