# Creating a custom exception class called ValueTooHighError that inherits from the Exception class.

class ValueTooHighError(Exception):
    def __init__(self, message="Value is too high!"):
        self.message = message
        super().__init__(self.message)
        



def check_value():
    try:
        num = int(input("Enter a number: "))
        if num > 100:
            raise ValueTooHighError('Your number entered exceeds the limit of 100.')
        else:
            print("Number is within the limit.")            
    except ValueTooHighError as e:
        print(f"Error: {e}")
        
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

check_value()