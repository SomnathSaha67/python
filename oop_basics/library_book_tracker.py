class Book:

  def __init__(self, title, author):
    self.title= title
    self.author= author
    self.is_borrowed= False

  def borrow(self):
    
    if self.is_borrowed: 
      return f"'{self.title}' is already borrowed."
    else:
      self.is_borrowed= True
      return f"{self.title} by {self.author} has been borrowed."
    
  def return_book(self):

    if not self.is_borrowed:
      return f"'{self.title}' was not borrowed."
    else:
      self.is_borrowed= False
      return f"'{self.title}' has been returned."
    
books = [
    Book("1984", "George Orwell"),
    Book("The Hobbit", "J.R.R. Tolkien"),
    Book("Pride and Prejudice", "Jane Austen"),
    Book("The Catcher in the Rye", "J.D. Salinger")
]

print(books[0].borrow())
print(books[1].borrow())
print(books[1].borrow())
print(books[2].return_book())

with open("library_status.txt", "w") as f:

  for b in books:
    status= "Borrowed" if b.is_borrowed else "Available"
    f.write(f"{b.title} by {b.author} - {status}\n")