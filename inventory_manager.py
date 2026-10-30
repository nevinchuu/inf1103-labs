import json
import os

from inventory import Inventory
from product_factory import PRODUCT_TYPES, product_class_for

# Path can be overridden (used by Docker so the file lives in a mounted volume)
FILENAME = os.environ.get("INVENTORY_FILE", "inventory.json")


# ---------------------------------------------------------------- file handling
def load_inventory():
    """Load inventory.json into an Inventory of Product subclass objects.

    Returns (inventory, loaded_ok). loaded_ok is False if the file exists but
    could not be read, so the caller knows not to save over it.
    """
    inventory = Inventory()
    if os.path.exists(FILENAME):
        print(f"{os.path.basename(FILENAME)} found.")
        try:
            with open(FILENAME, "r") as file:
                for item in json.load(file):
                    product_class = product_class_for(item["type"])
                    if product_class is None:
                        raise KeyError(item["type"])
                    inventory.add_product(product_class.from_dict(item))
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, TypeError):
            print("Could not read file. Starting with an empty inventory.")
            print("Saving is disabled so the existing file is not overwritten.")
            return Inventory(), False
    else:
        print(f"{os.path.basename(FILENAME)} not found. Starting with an empty inventory.")
    return inventory, True


def save_inventory(inventory, can_save=True):
    """Save the Product objects in the inventory to inventory.json."""
    if not can_save:
        print(f"Not saved: {os.path.basename(FILENAME)} could not be loaded, "
              "so it was left untouched. Fix or remove the file and restart.")
        return
    data = [product.to_dict() for product in inventory.get_products()]
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

    print("Product types: " + ", ".join(PRODUCT_TYPES))
    product_class = product_class_for(input("Product type: ").strip().lower())
    if product_class is None:
        print("Invalid product type.")
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
        extras = []
        for _, prompt, convert in product_class.EXTRA_FIELDS:
            value = convert(input(f"{prompt}: ").strip())
            if convert is not str and value < 0:
                raise ValueError
            if convert is str and not value:
                raise ValueError
            extras.append(value)
    except ValueError:
        print("Invalid input. Numbers must be non-negative and text cannot be empty.")
        return

    inventory.add_product(product_class(product_id, name, price, stock, *extras))
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

    inventory, can_save = load_inventory()
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
            save_inventory(inventory, can_save)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory, can_save)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
