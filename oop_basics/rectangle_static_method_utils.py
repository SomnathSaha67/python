class Rectangle:

  def __init__(self, length, width):
    self.length= length
    self.width= width

  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2 * (self.length + self.width)

  @staticmethod
  def is_square(length , width):
    return length == width

rectangles = [Rectangle(10, 5),
              Rectangle(7, 7),   
              Rectangle(12, 8)]

for r in rectangles:
  print(f"Rectangle ({r.length}, {r.width})")
  print(f"  Area: {r.area()}")
  print(f"  Preimeter: {r.perimeter()}")
  print(f"  Is square? {Rectangle.is_square(r.length, r.width)}")
  print()