def format_ledger(clients):
  for name, amount in clients.items():
    print(f"{name:<12} Rs.{amount:>8,}")
clients = {"Acme": 45000, "Zeta Corp": 12000, "Nimbus": 78000}
format_ledger(clients)
print(f"Top payer: {max(clients, key= clients.get)}")