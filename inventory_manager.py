import json
import os

# Path can be overridden (used by Docker so the file lives in a mounted volume)
FILENAME = os.environ.get("INVENTORY_FILE", "inventory.json")


# ---------------------------------------------------------------- persistence
def load_inventory():
    """Load inventory from inventory.json if it exists, else return an empty list."""
    if os.path.exists(FILENAME):
        print(f"{os.path.basename(FILENAME)} found.")
        try:
            with open(FILENAME, "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Could not read file. Starting with an empty inventory.")
            return []
    print(f"{os.path.basename(FILENAME)} not found. Starting with an empty inventory.")
    return []


def save_inventory(inventory):
    """Save the inventory list to inventory.json."""
    with open(FILENAME, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f"Inventory saved successfully to {os.path.basename(FILENAME)}.")


# Data Manipulation
def find_product(inventory, product_id):
    """Return the product dictionary with the given ID, or None."""
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if find_product(inventory, product_id):
        print("A product with that ID already exists.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
        if price < 0 or stock < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Price and stock must be non-negative numbers.")
        return

    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    try:
        new_stock = int(input("New Stock Quantity: ").strip())
        if new_stock < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Stock must be a non-negative whole number.")
        return

    product["stock"] = new_stock
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product = find_product(inventory, input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)


def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    if not inventory:
        print("No products in inventory.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


# ----------------------------------------------------------------------- menu
def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()
    show_menu()

    while True:
        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()