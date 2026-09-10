inventory = 0

quantity = input("Enter Stock Quantity or type 'quit' to exit: ")
while quantity != "quit":
    if not quantity.isdigit() or int(quantity) < 0:
        print("Invalid input. Please enter a valid number or type 'quit' to exit.")
    else: 
    #Accidentally added int alr so this will be the third commit
        inventory += int(quantity)
        print("Current Inventory: " + str(inventory))
    
    quantity = input("Enter Stock Quantity or type 'quit' to exit: ")

print("Total Inventory: " + str(inventory))