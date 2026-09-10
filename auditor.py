inventory = 0

quantity = input("Enter Stock Quantity or type 'quit' to exit: ")
while quantity != "quit":
    #Accidentally added int alr so this will be the third commit
    inventory += int(quantity)
    quantity = input("Enter Stock Quantity or type 'quit' to exit: ")

print("Total Inventory: " + str(inventory))