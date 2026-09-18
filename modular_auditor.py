inventory, quantity, failed_attempts, current_total = 0, 0, 0, 0
new_value = 10
user_input = ""

def get_valid_input():

    user_input = input("Enter Stock Quantity or type 'quit' to exit: ").strip()
    if user_input.lower() == "quit":
        return "quit"
    if user_input.isdigit() and int(user_input) > 0:
        return int(user_input)
    return None  

def process_delivery(current_total, new_value):
    if new_value is None:
        return None
    current_total = current_total + new_value
    return current_total


def calculate_tax(amount):
    return amount * 0.10

def generate_report(inventory, failed_attempts):
    calculate_tax(inventory)
    print("Failed Attempts: ", failed_attempts)
    print("Final Inventory: ", inventory)
    print("Tax on Inventory: ", calculate_tax(inventory))

while True: 
    user_input = get_valid_input()

    if user_input == "quit":
        break
    if user_input is None:
        print("Invalid input. Please enter a valid number or type 'quit' to exit.")
        failed_attempts += 1
    elif inventory + user_input > 500:
        print("Inventory limit exceeded. Current Inventory: ", inventory)
        failed_attempts += 1
    else:
        inventory = inventory + user_input
        process_delivery(inventory, user_input)
        print("Current Inventory: ", inventory)

generate_report(inventory, failed_attempts)
