def create_ticket(customer, priority= "normal", channel= "email"):
  print(f"Ticket -> Customer: {customer}, Priority: {priority}, Channel: {channel}")

create_ticket("Alice")

create_ticket("Bob", "high", "chat")

create_ticket(priority= "low", channel= "phone", customer= "Charlie")

create_ticket("Dana", channel= "web")