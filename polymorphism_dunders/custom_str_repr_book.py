class Book:

  def __init__(self, title, author, pages):
    self.title= title
    self.author= author
    self.pages= pages

  def __str__(self):
    return f"Book: {self.title} by {self.author}"
  
  def __repr__(self):
    return f"Book(title= {self.title!r}, author= {self.author!r}, pages= {self.pages})"

b1= Book("1984", "George Orwell", 328)
b2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(b1)
print(b2)

print(repr(b1))
print([b1, b2])