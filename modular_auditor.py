inventory, quantity, failed_attempts, current_total = 0
new_value = 10

def get_valid_input():
    user_input = input("Enter a stock quantity or type 'quit' to exit: ")
    if user_input.lower() == 'quit':
        return None
    try:
        quantity = int(user_input)
        if quantity < 0:
            print("Please enter a non-negative integer.")
            return get_valid_input()
        return quantity
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_valid_input()

def process_delivery(current_total, new_value):
    if new_value is None:
        return None
    updated_total = current_total + new_value
    print(f"Updated total quantity: {updated_total}")


def calculate_tax(amount):
    return amount * 0.10
