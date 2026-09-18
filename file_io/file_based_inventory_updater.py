# Step 1: Write initial inventory data to inventory.txt
initial_data = """Widget,42,9.99
Gadget,0,19.99
Gizmo,7,4.50
Sprocket,15,12.00
"""

with open("inventory.txt", "w") as f:
    f.write(initial_data)

# Step 2: Read and parse inventory.txt
inventory = []
with open("inventory.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        name = parts[0]
        qty = int(parts[1])
        price = float(parts[2])
        inventory.append((name, qty, price))

# Step 3: Simulate sale event
purchases = {"Widget": 5, "Gizmo": 2, "Sprocket": 20}
rejected = []

updated_inventory = []
for name, qty, price in inventory:
    if name in purchases:
        purchase_qty = purchases[name]
        if qty - purchase_qty < 0:
            rejected.append(f"{name}: Requested {purchase_qty}, Available {qty}, REJECTED")
            updated_inventory.append((name, qty, price))  # unchanged
        else:
            updated_inventory.append((name, qty - purchase_qty, price))
    else:
        updated_inventory.append((name, qty, price))

# Step 4: Overwrite inventory.txt with updated quantities
with open("inventory.txt", "w") as f:
    for name, qty, price in updated_inventory:
        f.write(f"{name},{qty},{price:.2f}\n")

# Step 5: Write rejected purchases to rejected_purchases.txt
with open("rejected_purchases.txt", "w") as f:
    for entry in rejected:
        f.write(entry + "\n")
