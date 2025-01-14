# Creating a product catalog

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        return self.price * self.quantity
    
product = Product("HP Laptop", 12000, 3)
print(f"The total value of {product.name} is {product.calculate()}")