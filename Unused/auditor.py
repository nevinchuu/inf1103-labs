inventory = 0
rejected_entries = 0

quantity = input("Enter Stock Quantity or type 'quit' to exit: ")
while quantity != "quit":
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid input. Please enter a valid number or type 'quit' to exit.")
        rejected_entries += 1
    elif int(inventory) + int(quantity) > 500:
            print("Inventory limit exceeded. Current Inventory: ", inventory)
            rejected_entries += 1
            break
    else:
        inventory += int(quantity)
        print("Current Inventory: ", inventory)

    quantity = input("Enter Stock Quantity or type 'quit' to exit: ")

print("Final Inventory: ", inventory)
print("Rejected Entries: ", rejected_entries)