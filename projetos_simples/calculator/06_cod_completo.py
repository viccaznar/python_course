def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def display_menu():
    print("Select an operation: ")
    print("[1] Sum")
    print("[2] Subtraction")
    print("[3] Multiply")
    print("[4] Divide")

def collect_data():
    display_menu()
    
    choice = input("Enter your choice [1][2][3][4]: ")

    num1 = input("Enter the first number: ")
    float_num1 = float(num1)  # Conversion in a separate variable

    num2 = input("Enter the second number: ")
    float_num2 = float(num2)  # Conversion in a separate variable

    return choice, float_num1, float_num2  # Return choice and converted numbers

def calculate(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    else:
        return "Invalid Choice."

def main():
    while True:
        choice, float_num1, float_num2 = collect_data()  # Get choice and numbers
        result = calculate(choice, float_num1, float_num2)  # Calculate result
        print(f'Result: {result}')
        
        continue_calculation = input('Do you want to perform another operation? [y] or [n]: ')
        if continue_calculation.lower() != 'y':
            break  # Properly close the loop if the user chooses not to continue
