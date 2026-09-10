inventory = 0

quantity = input("Enter Stock Quantity or type 'quit' to exit: ")
while quantity != "quit":
    inventory += int(quantity)
    quantity = input("Enter Stock Quantity or type 'quit' to exit: ")

print("Total Inventory: " + str(inventory))