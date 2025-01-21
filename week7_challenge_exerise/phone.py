from item import Item

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Run validations to the received arguments
        
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
        # assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        
        
        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones
    
        # # Actions to execute
        # Phone.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)
# print(phone1.calculate_total_price())

# phone2 = Phone("jscPhonev20", 700, 5, 1)