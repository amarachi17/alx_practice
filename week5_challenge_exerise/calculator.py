# Creating a function for addition, subtraction, multiplication and division

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handling division ny zero
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y
    