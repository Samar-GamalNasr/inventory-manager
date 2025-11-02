INVENTORY = []


def validate_name(name):
    name = name.strip()
    if name == "":
        print("You must write a name.")
        return None
    elif len(name) < 3:
        print("Enter a valid name (at least 3 letters).")
        return None
    elif not name.replace(" ", "").isalpha():
        print("Name should contain only letters.")
        return None
    else:
        return name


def validate_price(value):
    value = value.strip()
    if value == "":
        print("you must enter a price")
        return None
    dot_count = value.count(".")
    if not value.replace(".", "").isdigit() or dot_count > 1:
        print("Invalid price. Must be a number like 10 or 12.5")
        return None
    price = float(value)
    if price <= 0:
        print("Price must be greater than 0.")
        return None
    return price


def validate_quantity(value):
    value = value.strip()
    if value == "":
        print("You must enter a quantity.")
        return None
    if not value.isdigit():
        print("Quantity must be a positive integer.")
        return None
    quantity = int(value)
    if quantity < 0:
        print("Quantity cannot be negative.")
        return None
    return quantity


# ===============================
# 🧠 BUSINESS LOGIC (العقل)
# ===============================
def add_item_to_inventory(name, quantity, price):
    INVENTORY.append({"name": name, "quantity": quantity, "price": price})


def get_all_items(INVENTORY):
     return INVENTORY

def find_item(INVENTORY, name):
    for item in INVENTORY:
        if item["name"].lower() == name.lower():
            return [item]
    return []


def update_item(INVENTORY, name, new_price ,new_quantity):
    for item in INVENTORY:
       if  item['name'].lower() == name.lower():
            item['price'] = new_price
            item['quantity'] = new_quantity
            return True
    return False




# ===============================
# 🎛 CONTROLLER (التحكم والتفاعل)
# ===============================
def handle_add_item():
    while True:
        name = input("Enter item name: ")
        name = validate_name(name)
        if name:
            break

    while True:
        price = input("Enter item price :")
        price = validate_price(price)
        if price:
            break

    while True:
        quantity = input("Enter quantity of item (0 allowed for out of stock):  ")
        quantity = validate_quantity(quantity)
        if quantity is not None:
            break

    add_item_to_inventory(name, quantity, price)
    print("✅ Item added successfully!")
    print(f"Added {name} successfully! Total items now: {len(INVENTORY)}")


def handle_view_items(INVENTORY):
    items = get_all_items(INVENTORY)    

    if not items:
        print("INVENTORY is empty.")
        return

    print("INVENTORY Items:")
    print("Name\t|Quantity\t|Price")

    for item in items:
        print(f"{item['name']}\t|{item['quantity']}\t\t|{item['price']}")



def handle_search_item(INVENTORY):
    if not INVENTORY:
        print("INVENTORY is empty.")
        return

    while True:
        name = input("Enter item name to search: ")
        name = validate_name(name)
        if name:
            break

    items = find_item(INVENTORY, name)

    if not items:
        print("Item not found in INVENTORY.")
        return

    print("\nFound Items:")
    print("Name\t|Quantity\t|Price")
    print("-------------------------------")
    for item in items:
        print(f"{item['name']}\t|{item['quantity']}\t\t|{item['price']}")



def handle_update_item(INVENTORY):
    if not INVENTORY:
          print("INVENTORY is empty.")
          return
    while True:
          name = input("Enter item name: ")
          name = validate_name(name)
          if name:
            break
    if not find_item(INVENTORY, name):
            print("Item not found in INVENTORY.")
            return
    while True:
        new_price  = input("Enter item price :")
        new_price  = validate_price(new_price )
        if new_price :
            break

    while True:
        new_quantity = input("Enter quantity of item (0 allowed for out of stock):  ")
        new_quantity = validate_quantity(new_quantity)
        if new_quantity is not None:
            break

    success = update_item(INVENTORY, name, new_price, new_quantity)
    if success:
        print("✅ Item updated successfully!")
        print(f"Updated {name}: price to {new_price} and quantity to {new_quantity}")
    else:
        print("❌ Item not found in INVENTORY.")

# ===============================
# 🚀 MAIN APP LOOP
# ===============================
def main():
    while True:
        print("=== INVENTORY Management ===")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        match choice:
            case "1":
                handle_add_item()
            case "2":
                handle_view_items(INVENTORY)
            case "3":
                handle_search_item(INVENTORY)
            case "4":
                handle_update_item(INVENTORY)
            case "5":
                print("Exiting the program. Goodbye!")
                return
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
