import os

filename = "orders.txt"

def load_inventory():
    """Reads previously saved orders from orders.txt if it exists."""
    history = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        history.append(line)
        except Exception:
            pass
    return history

def save_inventory(history):
    """Saves all orders to orders.txt."""
    with open(filename, "w") as f:
        for order in history:
            f.write(f"{order}\n")

def get_valid_input():
    """Prompts user for product name and quantity."""
    product_name = input("Enter Product Name: ").strip()
    if product_name.lower() == "quit":
        return "quit", None
    
    quantity_input = input("Enter Quantity: ").strip()
    if quantity_input.lower() == "quit":
        return "quit", None
        
    if quantity_input.isdigit() and int(quantity_input) > 0:
        return product_name, int(quantity_input)
    return None, None

def process_delivery(current_total, new_value):
    """Updates current total quantity."""
    if new_value is None:
        return None
    return current_total + new_value

def append_transaction(history_list, item_string):
    """Appends a valid transaction to the history log."""
    history_list.append(item_string)
    return history_list

def calculate_tax(amount):
    """Calculates 10% tax on inventory quantity."""
    return amount * 0.10

def generate_report(inventory, failed_attempts, history):
    """Generates and prints summary report."""
    print("\n--- Summary Report ---")
    print("Failed Attempts: ", failed_attempts)
    print("Final Inventory Quantity: ", inventory)
    print("Tax on Inventory: ", calculate_tax(inventory))
    print("Transaction History: ", history)


# Variables Initialization
failed_attempts = 0
inventory = 0

# Load existing orders
history = load_inventory()

# Display current orders loaded from file
print("Current Orders:\n")
if history:
    for order in history:
        print(order)
        # Calculate existing total inventory from history
        parts = order.split(",")
        if len(parts) == 3 and parts[2].strip().isdigit():
            inventory += int(parts[2].strip())
print()

# Starting ID based on history length
next_id = 1001 + len(history)

while True:
    product_name, quantity = get_valid_input()

    if product_name == "quit":
        save_inventory(history)
        print("\nOrder successfully saved to orders.txt")
        break

    if product_name is None:
        print("Invalid input. Please enter a valid product name and positive quantity.\n")
        failed_attempts += 1
    elif quantity > 500:
        print("Quantity limit exceeded. Current Inventory: ", inventory)
        failed_attempts += 1
    else:
        # Format: ID, Product Name, Quantity
        new_order = f"{next_id}, {product_name}, {quantity}"
        append_transaction(history, new_order)
        
        inventory = process_delivery(inventory, quantity)
        next_id += 1

        print("\nNew Order Added:")
        print(f"{next_id - 1},{product_name},{quantity}\n")
        
        save_inventory(history)
        print("Order successfully saved to orders.txt\n")
        break

generate_report(inventory, failed_attempts, history)