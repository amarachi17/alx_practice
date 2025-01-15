# Handling Zero Division Error

num1 = int(input('Enter a First number to divide '))
num2 = int(input('Enter a Second number to divide '))

def divide(num1, num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'

print(divide(num1, num2))

