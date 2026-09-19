class Vector2D:

  def __init__(self, x, y):
    self.x= x
    self.y= y

  def __add__(self, other):
    if isinstance(other, Vector2D):
      return Vector2D(self.x + other.x, self.y + other.y)
    return NotImplemented
  
  def __str__(self):
    return f"({self.x}, {self.y})"
  
  def __lt__(self, other):
    if isinstance(other, Vector2D):
      return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    return NotImplemented
  
v1= Vector2D(3, 4)
v2= Vector2D(1, 2)
v3= Vector2D(5, 6)

v_sum= v1+v2
print(f"v1 + v2= {v_sum}")

print(f"Is v2<v1? {v2<v1}")
print(f"Is v3<v1? {v3<v1}")