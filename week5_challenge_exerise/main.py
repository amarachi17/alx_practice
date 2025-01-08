#  Importing from the same folder 
import calculator

# Asking the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))	

# Asking the user to choose an operation
print("\n Choose an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number of operations 1, 2, 3, or 4: ")

# Using switch statement
match choice:
    case '1':
        result = calculator.add(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    case '2':
        result = calculator.subtract(num1, num2)
        print(f"The difference of {num1} and {num2} is {result}")
    case '3':
        result = calculator.multiply(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")
    case '4':
        result = calculator.divide(num1, num2)
        if result != 0:
            print(f"The division of {num1} and {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid input! Please choose a number between 1 and 4.")
