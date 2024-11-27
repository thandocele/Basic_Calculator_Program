"""Basic Calculator Program
"""

def get_number_input(prompt):
    """Helper function to get a valid numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_input():
    """Helper function to get a valid operation input."""
    while True:
        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        elif operation.lower() == 'q':
            return 'q'
        else:
            print("Invalid operation. Please use one of +, -, *, /, or 'q' to quit.")

def perform_calculation(num1, num2, operation):
    """Performs the calculation based on the operation."""
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        return None

    # Convert to int if result is an integer value
    return int(result) if result.is_integer() else result

def calculator():
    """
    A simple interactive calculator program that performs arithmetic operations (+, -, *, /).
    The user is prompted to input two numbers and choose an operation. The calculator allows 
    multiple calculations in a session and provides an option to quit by typing 'q'.

    Available operations:
        + : Addition
        - : Subtraction
        * : Multiplication
        / : Division (with error handling for division by zero)

    The program will continue prompting for input until the user types 'q' to quit.
    """
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")
    print("Type 'q' to quit at any time.")

    while True:
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
        operation = get_operation_input()

        if operation == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        result = perform_calculation(num1, num2, operation)

        if result is not None:
            print(f"{num1} {operation} {num2} = {result}")

def main():
    """
    The entry point of the calculator program.
    It invokes the calculator function to start the interactive session.
    """
    calculator()


# Run the program
if __name__ == "__main__":
    main()
