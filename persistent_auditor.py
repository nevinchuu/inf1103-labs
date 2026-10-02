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

if __name__ == "__main__":
    inventory = load_inventory()
    print(inventory)