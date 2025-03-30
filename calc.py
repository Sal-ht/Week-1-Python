# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

# Define the operations dictionary
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation using the dictionary and print the result
result = operations.get(operation, None)

# Print the result or handle invalid operation
print(f"{num1} {operation} {num2} = {result(num1, num2) if result else 'Invalid operation'}")