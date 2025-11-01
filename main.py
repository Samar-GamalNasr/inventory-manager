inventory = []

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
    value=value.strip()
    if value=="":
        print("you must enter a price") 
        return None
    dot_count=value.count(".")
    if not value.replace(".","").isdigit() or dot_count>1:
        print("Invalid price. Must be a number like 10 or 12.5")
        return None
    price=float(value)
    if price<=0:
        print("Price must be greater than 0.")
        return None
    return price

def validate_quantity(value):
    value=value.strip()
    if value =="":
        print("You must enter a quantity.")
        return None
    if not value.isdigit():
        print("Quantity must be a positive integer.")
        return None
    quantity = int(value)
    if quantity <0:
        print("Quantity cannot be negative.")
        return None
    return quantity

# ===============================
# 🧠 BUSINESS LOGIC (العقل)
# ===============================
def add_item_to_inventory(name, quantity, price):
    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })



def get_all_items(inventory):
    """ترجع كل العناصر"""
    pass

def find_item(inventory, name):
    """ترجع العنصر اللي اسمه كذا"""
    pass

def update_item(inventory, name, new_price):
    """تعدل بيانات عنصر موجود"""
    pass


# ===============================
# 🎛 CONTROLLER (التحكم والتفاعل)
# ===============================
def handle_add_item():
    while True:
        name=input("Enter item name: ")
        name=validate_name(name)
        if name:
            break

    while True:
        price=input("Enter item price :")
        price=validate_price(price)
        if price:
            break

    while True:
        quantity=input("Enter quantity of item (0 allowed for out of stock):  ")
        quantity=validate_quantity(quantity)
        if quantity is not None:
            break

    add_item_to_inventory(name, quantity, price)
    print("✅ Item added successfully!")
    print(f"Added {name} successfully! Total items now: {len(inventory)}")



def handle_view_items(inventory):
    pass

def handle_search_item(inventory):
    pass

def handle_update_item(inventory):
    pass


# ===============================
# 🚀 MAIN APP LOOP
# ===============================
def main():
    pass

handle_add_item()