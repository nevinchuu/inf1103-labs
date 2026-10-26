import json
import os

from inventory import Inventory
from product import Product

# Path can be overridden (used by Docker so the file lives in a mounted volume)
FILENAME = os.environ.get("INVENTORY_FILE", "inventory.json")


# ---------------------------------------------------------------- file handling
def load_inventory():
    """Load inventory.json into an Inventory of Product objects."""
    inventory = Inventory()
    if os.path.exists(FILENAME):
        print(f"{os.path.basename(FILENAME)} found.")
        try:
            with open(FILENAME, "r") as file:
                for item in json.load(file):
                    inventory.add_product(
                        Product(item["id"], item["name"], item["price"], item["stock"]))
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, TypeError):
            print("Could not read file. Starting with an empty inventory.")
            return Inventory()
    else:
        print(f"{os.path.basename(FILENAME)} not found. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory):
    """Save the Product objects in the inventory to inventory.json."""
    data = [{"id": product.get_product_id(), "name": product.get_name(),
             "price": product.get_price(), "stock": product.get_stock()}
            for product in inventory.get_products()]
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {os.path.basename(FILENAME)}.")


# ------------------------------------------------------------------ user input
def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if inventory.search_product(product_id):
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

    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    try:
        new_stock = int(input("New Stock Quantity: ").strip())
    except ValueError:
        print("Invalid input. Stock must be a non-negative whole number.")
        return

    if product.update_stock(new_stock):
        print("Stock updated successfully!")
    else:
        print("Invalid input. Stock must be a non-negative whole number.")


def search_product(inventory):
    print("Search Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    product.display_information()
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
            inventory.display_all()
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
