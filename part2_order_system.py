menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}
#Task 1 Explore the Menu #################################################Starts Here############################
# Print full menu grouped by category
categories = []
for item in menu:
    cat = menu[item]["category"]
    if cat not in categories:
        categories.append(cat)

for cat in categories:
    print(f"\n===== {cat} =====")
    for item, details in menu.items():
        if details["category"] == cat:
            status = "[Available]" if details["available"] else "[Unavailable]"
            print(f"  {item:<18} ₹{details['price']:<9.2f} {status}")

# Menu statistics using dictionary methods
total_items = len(menu)
available_items = sum(1 for d in menu.values() if d["available"])
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
under_150 = [(name, d["price"]) for name, d in menu.items() if d["price"] < 150]

print(f"\nTotal items on menu    : {total_items}")
print(f"Available items        : {available_items}")
print(f"Most expensive item    : {most_expensive[0]} (₹{most_expensive[1]['price']:.2f})")
print(f"Items priced under ₹150:")
for name, price in under_150:
    print(f"  {name:<18} ₹{price:.2f}")
#Task 1 #################################################ends Here############################

#Task 2 Cart Operations ###################################################### starts  here

cart = []

# Add item to cart
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"  ✗ '{item_name}' does not exist in the menu.")
        return
    if not menu[item_name]["available"]:
        print(f"  ✗ '{item_name}' is currently unavailable.")
        return
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"  ✓ Updated '{item_name}' quantity to {entry['quantity']}")
            return
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
    print(f"  ✓ Added '{item_name}' x{quantity} to cart")

# Remove item from cart
def remove_from_cart(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"  ✓ Removed '{item_name}' from cart")
            return
    print(f"  ✗ '{item_name}' is not in the cart.")

# Update quantity of item in cart
def update_quantity(item_name, new_quantity):
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_quantity
            print(f"  ✓ Updated '{item_name}' quantity to {new_quantity}")
            return
    print(f"  ✗ '{item_name}' is not in the cart.")

# Simulate the order sequence
print("\n--- Cart Operations ---")

print("\n1. Add 'Paneer Tikka' x2")
add_to_cart("Paneer Tikka", 2)
print(f"   Cart: {cart}")

print("\n2. Add 'Gulab Jamun' x1")
add_to_cart("Gulab Jamun", 1)
print(f"   Cart: {cart}")

print("\n3. Add 'Paneer Tikka' x1 (should update quantity to 3)")
add_to_cart("Paneer Tikka", 1)
print(f"   Cart: {cart}")

print("\n4. Try to add 'Mystery Burger'")
add_to_cart("Mystery Burger", 1)
print(f"   Cart: {cart}")

print("\n5. Try to add 'Chicken Wings' (unavailable)")
add_to_cart("Chicken Wings", 1)
print(f"   Cart: {cart}")

print("\n6. Remove 'Gulab Jamun'")
remove_from_cart("Gulab Jamun")
print(f"   Cart: {cart}")

# Final Order Summary
print("\n========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    print(f"  {entry['item']:<18} x{entry['quantity']}    ₹{line_total:.2f}")
gst = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)
print("------------------------------------")
print(f"  {'Subtotal:':<28} ₹{subtotal:.2f}")
print(f"  {'GST (5%):':<28} ₹{gst:.2f}")
print(f"  {'Total Payable:':<28} ₹{total:.2f}")
print("====================================")

#Task 2 ###################################################### ends  here

#Task 3 ###################################################### starts  here

import copy

# Deep copy inventory before any changes
inventory_backup = copy.deepcopy(inventory)

# Demonstrate deep copy works: change one stock value and compare
print("\n--- Deep Copy Demonstration ---")
inventory["Paneer Tikka"]["stock"] = 999
print(f"  inventory['Paneer Tikka']['stock']        = {inventory['Paneer Tikka']['stock']}")
print(f"  inventory_backup['Paneer Tikka']['stock']  = {inventory_backup['Paneer Tikka']['stock']}")
print("  ✓ Backup is unaffected by the change.")

# Restore inventory to original state
inventory["Paneer Tikka"]["stock"] = inventory_backup["Paneer Tikka"]["stock"]

# Simulate order fulfilment: deduct cart quantities from inventory
print("\n--- Order Fulfilment ---")
for entry in cart:
    item_name = entry["item"]
    qty = entry["quantity"]
    if item_name in inventory:
        available = inventory[item_name]["stock"]
        if available >= qty:
            inventory[item_name]["stock"] -= qty
            print(f"  {item_name}: deducted {qty}, stock now {inventory[item_name]['stock']}")
        else:
            print(f"  ⚠ {item_name}: insufficient stock ({available} available, {qty} requested). Deducting {available} only.")
            inventory[item_name]["stock"] = 0
    else:
        print(f"  ✗ {item_name} not found in inventory.")

# Reorder alerts
print("\n--- Reorder Alerts ---")
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"  ⚠ Reorder Alert: {item_name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# Print both to confirm they differ
print("\n--- Inventory vs Backup Comparison ---")
for item_name in inventory:
    inv_stock = inventory[item_name]["stock"]
    bak_stock = inventory_backup[item_name]["stock"]
    diff = " ← differs" if inv_stock != bak_stock else ""
    print(f"  {item_name:<18} inventory: {inv_stock:>3}   backup: {bak_stock:>3}{diff}")

#Task 3 ###################################################### ends  here

#Task 4 ###################################################### starts  here

# Helper: compute and print revenue per day, return dict of day totals
def print_revenue_per_day():
    day_totals = {}
    print(f"\n  {'Date':<14} {'Revenue':>10}")
    print(f"  {'-'*26}")
    for date, orders in sales_log.items():
        day_total = sum(order["total"] for order in orders)
        day_totals[date] = day_total
        print(f"  {date:<14} ₹{day_total:>9.2f}")
    return day_totals

# Helper: find and print best-selling day
def print_best_day(day_totals):
    best_date = max(day_totals, key=day_totals.get)
    print(f"\n  Best-selling day: {best_date} — ₹{day_totals[best_date]:.2f}")

# Revenue per day
print("\n--- Revenue Per Day ---")
day_totals = print_revenue_per_day()
print_best_day(day_totals)

# Most ordered item (appears in the most individual orders)
item_order_count = {}
for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            item_order_count[item] = item_order_count.get(item, 0) + 1

most_ordered = max(item_order_count, key=item_order_count.get)
print(f"\n  Most ordered item: {most_ordered} (appeared in {item_order_count[most_ordered]} orders)")

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# Reprint updated stats
print("\n--- Updated Revenue Per Day (after adding 2025-01-05) ---")
day_totals = print_revenue_per_day()
print_best_day(day_totals)

# Numbered list of all orders using enumerate
print("\n--- All Orders (Numbered) ---")
counter = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"  {counter:>2}. [{date}] Order #{order['order_id']:<3} — ₹{order['total']:.2f} — Items: {items_str}")
        counter += 1

#Task 4 ###################################################### ends  here
