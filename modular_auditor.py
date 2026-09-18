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