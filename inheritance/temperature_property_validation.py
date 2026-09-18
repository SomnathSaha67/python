class Temperature:

  def __init__(self, celsius):
    self._celsius= celsius

  @property
  def celsius(self):
    return self._celsius
  
  @celsius.setter
  def celsius(self, value):
    if value<-273.15:
      raise ValueError("Tempearture cannot go below -273.15°C")
    self._celsius= value

t= Temperature(25)
print(f"Initial: {t.celsius}")

t.celsius= 100
print(f"Updated: {t.celsius}")