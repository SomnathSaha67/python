def track_instances(cls):
  cls.instance_count= 0

  original_init= cls.__init__

  def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    cls.instance_count+=1
    print(f"{cls.__name__} instances created: {cls.instance_count}")

  cls.__init__= new_init
  return cls

@track_instances
class Customer:
  def __init__(self, name):
    self.name= name

c1= Customer("Alice")
c2= Customer("Bob")
c3= Customer("Charlie")
c4= Customer("Diana")

print(f"Total Customer instances: {Customer.instance_count}")