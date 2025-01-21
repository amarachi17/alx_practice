import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
    
    
        # Actions to execute
        Item.all.append(self)
        
        
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
     
        
    @property
    # Property Decorator for = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
        
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero.
        # Fpr i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero.
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        # return f"Item('{self.name}',  {self.price}, {self.quantity})"
      
      
    def __connect(self, smpt_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, Confidence
        """
    
    def __send(self):
        pass 
    
    def send_email(self):
           self.__connect('')
           self.__prepare_body()
           self.__send()
    
    
    # @property
    # def read_only_name(self):
    #     return "AAA"
  
# print(Item.is_integer(7.5))
       
# Item.instantiate_from_csv() 
# print(Item.all)    


# print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# item1 = Item('Phone', 100, 1)
# item1.apply_discount()
# print(item1.price)

# item2 = Item('Laptop', 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.__dict__)
# print(item1.__dict__)

# print(f"Name of the product is {item1.name}, price is ${item1.price}, quantity is {item1.quantity}. Total price is ${item1.calculate_total_price()}")
# print(f"Name of the product is {item2.name}, price is ${item2.price}, quantity is {item2.quantity}. Total price is ${item2.calculate_total_price()}")
