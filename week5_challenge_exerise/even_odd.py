# Checking to know if a number is even or odd
number = int(input("Enter a number to check if the number is even or odd. "))
def is_even(number):
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

# Printing the result
print(is_even(number))



    
