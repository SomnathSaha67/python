class Vehicle:

  def __init__(self, brand, max_speed):
    self.brand= brand
    self.max_speed= max_speed

  def show_info(self):
    print(F"Brand: {self.brand}")
    print(f"Maximum speed: {self.max_speed} km/hr")

class Car(Vehicle):

  def __init__(self,brand, max_speed, num_doors):
    super().__init__(brand, max_speed)
    self.num_doors= num_doors

  def show_info(self):
    super().show_info()
    print(f"Number of doors: {self.num_doors}")

v= Vehicle("Generic Vehicle", 120)
c= Car("Toyota", 180, 4)

print("Vehicle info:")
v.show_info()

print("\nCar info:")
c.show_info()